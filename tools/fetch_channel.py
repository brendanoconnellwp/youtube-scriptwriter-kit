#!/usr/bin/env python3
"""
Pull transcripts + metadata for every video on a YouTube channel.

Your own channel (everything):
    python3 tools/fetch_channel.py @YourChannel --out data/mine

Another creator (just their top 15 by views, for the playbook):
    python3 tools/fetch_channel.py @SomeCreator --out data/research --top 15

Later, only grab videos you haven't pulled yet:
    python3 tools/fetch_channel.py @YourChannel --out data/mine --update

If YouTube starts saying "Sign in to confirm you're not a bot", add:
    --cookies-from-browser chrome        (or safari, firefox, brave, edge)

Output (per channel):
    <out>/index.json          metadata for every video (id, title, date, views, ...)
    <out>/<date>_<slug>.md    one clean, timestamped transcript per video
For --out data/research, each creator gets their own subfolder automatically.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp isn't installed. Run:  python3 -m pip install -U yt-dlp")

MANUAL_LANGS = ["en", "en-US", "en-GB", "en-CA", "en-AU"]
AUTO_LANGS = ["en-orig", "en", "en-US"]
NOISE = re.compile(r"\[(music|applause|laughter|inaudible|__)\]", re.I)


# ---------------------------------------------------------------- helpers

def slugify(text, maxlen=60):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text or "").strip("-").lower()
    return s[:maxlen].rstrip("-") or "untitled"


def channel_base(channel):
    if channel.startswith("http"):
        return re.sub(r"/(videos|shorts|streams|featured|playlists)/?$", "", channel.rstrip("/"))
    handle = channel if channel.startswith("@") else "@" + channel
    return f"https://www.youtube.com/{handle}"


def ydl_opts(args, **extra):
    opts = {"quiet": True, "no_warnings": True, "skip_download": True}
    if args.cookies_from_browser:
        opts["cookiesfrombrowser"] = (args.cookies_from_browser,)
    opts.update(extra)
    return opts


def fmt_ts(ms):
    s = int(ms // 1000)
    h, rem = divmod(s, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def bot_hint(err):
    if "not a bot" in str(err).lower() or "sign in" in str(err).lower():
        print("    -> YouTube wants a signed-in session. Re-run with "
              "--cookies-from-browser chrome (or your browser).", file=sys.stderr)


# ---------------------------------------------------------------- listing

def list_videos(args):
    base = channel_base(args.channel)
    tabs = ["videos"] + (["shorts"] if args.include_shorts else [])
    entries, channel_name = [], None
    with yt_dlp.YoutubeDL(ydl_opts(args, extract_flat="in_playlist")) as ydl:
        for tab in tabs:
            try:
                info = ydl.extract_info(f"{base}/{tab}", download=False)
            except yt_dlp.utils.DownloadError as e:
                print(f"  ! couldn't list /{tab}: {e}", file=sys.stderr)
                bot_hint(e)
                continue
            channel_name = channel_name or info.get("channel") or info.get("uploader") or info.get("title")
            for e in info.get("entries") or []:
                if e and e.get("id"):
                    e["_format"] = "short" if tab == "shorts" else "long"
                    entries.append(e)
    return entries, channel_name


# ---------------------------------------------------------------- transcripts

def pick_track(info):
    """Prefer human-made English captions, then YouTube's auto captions."""
    for source, langs in (("subtitles", MANUAL_LANGS), ("automatic_captions", AUTO_LANGS)):
        tracks = info.get(source) or {}
        candidates = langs + sorted(l for l in tracks if l.startswith("en") and l not in langs)
        for lang in candidates:
            for f in tracks.get(lang, []):
                if f.get("ext") == "json3" and f.get("url"):
                    return f["url"], ("auto" if source == "automatic_captions" else "manual")
    return None, None


def parse_json3(raw):
    """Return [(start_ms, text), ...] from YouTube's json3 caption format."""
    data = json.loads(raw)
    out = []
    for ev in data.get("events", []):
        segs = ev.get("segs")
        if not segs:
            continue
        text = "".join(s.get("utf8", "") for s in segs).replace("\n", " ")
        text = NOISE.sub("", text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            out.append((ev.get("tStartMs", 0), text))
    return out


def paragraphs(pieces, target_words=70, max_gap_ms=2500):
    """Group caption pieces into readable, timestamped paragraphs."""
    paras, cur, cur_start, words, last_ms = [], [], None, 0, None
    for ms, text in pieces:
        gap = (ms - last_ms) if last_ms is not None else 0
        if cur and (words >= target_words or (gap > max_gap_ms and words >= 25)):
            paras.append((cur_start, " ".join(cur)))
            cur, words = [], 0
        if not cur:
            cur_start = ms
        cur.append(text)
        words += len(text.split())
        last_ms = ms
    if cur:
        paras.append((cur_start, " ".join(cur)))
    return [f"[{fmt_ts(ms)}] {t}" for ms, t in paras]


def fetch_video(ydl, video_id):
    info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
    url, kind = pick_track(info)
    body = []
    if url:
        raw = ydl.urlopen(url).read().decode("utf-8")
        body = paragraphs(parse_json3(raw))
    return info, body, kind


def write_markdown(path, meta, body, info):
    fm = {k: meta.get(k) for k in
          ("id", "title", "channel", "upload_date", "duration_min", "views", "likes",
           "comments", "format", "captions", "url")}
    lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items()] + ["---", ""]
    lines.append(f"# {meta['title']}\n")
    chapters = info.get("chapters") or []
    if chapters:
        lines.append("## Chapters")
        lines += [f"- {fmt_ts(c['start_time'] * 1000)} {c.get('title', '')}" for c in chapters]
        lines.append("")
    desc = (info.get("description") or "").strip()
    if desc:
        lines += ["## Description", desc[:1500] + ("..." if len(desc) > 1500 else ""), ""]
    lines.append("## Transcript")
    lines += body if body else ["(no English captions available for this video)"]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("channel", help="@handle or channel URL")
    ap.add_argument("--out", required=True, help="data/mine for yours, data/research for others")
    ap.add_argument("--top", type=int, default=0, help="only the N most-viewed videos (0 = all)")
    ap.add_argument("--update", action="store_true", help="skip videos already in index.json")
    ap.add_argument("--include-shorts", action="store_true", help="also pull the Shorts tab")
    ap.add_argument("--sleep", type=float, default=1.5, help="seconds between videos (be polite)")
    ap.add_argument("--cookies-from-browser", metavar="BROWSER", default=None)
    args = ap.parse_args()

    print(f"Listing {channel_base(args.channel)} ...")
    entries, channel_name = list_videos(args)
    if not entries:
        sys.exit("No videos found. Check the handle, or try --cookies-from-browser.")

    out = Path(args.out)
    if out.name == "research":  # one subfolder per creator
        out = out / slugify(channel_name or args.channel.lstrip("@"))
    out.mkdir(parents=True, exist_ok=True)
    index_path = out / "index.json"
    index = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else {}

    if args.top:
        entries.sort(key=lambda e: e.get("view_count") or 0, reverse=True)
        entries = entries[: args.top]
    todo = [e for e in entries if not (args.update and e["id"] in index)]
    print(f"{channel_name}: {len(entries)} videos selected, {len(todo)} to fetch -> {out}/")

    ok = failed = no_caps = 0
    with yt_dlp.YoutubeDL(ydl_opts(args)) as ydl:
        for i, e in enumerate(todo, 1):
            vid = e["id"]
            try:
                info, body, kind = fetch_video(ydl, vid)
            except Exception as err:  # keep going; one bad video shouldn't stop the run
                failed += 1
                print(f"  [{i}/{len(todo)}] FAILED {vid}: {err}", file=sys.stderr)
                bot_hint(err)
                time.sleep(args.sleep)
                continue
            d = info.get("upload_date") or "00000000"
            meta = {
                "id": vid,
                "title": info.get("title"),
                "channel": info.get("channel") or channel_name,
                "upload_date": f"{d[:4]}-{d[4:6]}-{d[6:]}",
                "duration_min": round((info.get("duration") or 0) / 60, 1),
                "views": info.get("view_count"),
                "likes": info.get("like_count"),
                "comments": info.get("comment_count"),
                "format": e.get("_format", "long"),
                "captions": kind or "none",
                "url": f"https://www.youtube.com/watch?v={vid}",
                "tags": info.get("tags") or [],
            }
            fname = f"{meta['upload_date']}_{slugify(meta['title'])}.md"
            write_markdown(out / fname, meta, body, info)
            meta["file"] = fname
            meta["transcript_words"] = sum(len(p.split()) for p in body)
            index[vid] = meta
            index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")  # save as we go
            if body:
                ok += 1
            else:
                no_caps += 1
            print(f"  [{i}/{len(todo)}] {meta['upload_date']}  {meta['views'] or 0:>8,} views  "
                  f"{'(no captions) ' if not body else ''}{meta['title']}")
            time.sleep(args.sleep)

    print(f"\nDone. {ok} transcripts, {no_caps} without captions, {failed} failed. Index: {index_path}")


if __name__ == "__main__":
    main()
