# YouTube Scriptwriter kit

Turn your YouTube channel into a Claude skill that writes scripts in your voice, backed by what works on your channel and on channels you study.

You feed it your own transcripts. Claude Code distills them into a voice profile, a catalog of everything you've made, a growth playbook and a few exemplar transcripts. Those files become a skill you install in Claude Code or the Claude app. After that, "write me a video on X" gets you angles, hooks, a beat sheet, a full script, titles, thumbnail ideas and a description that sound like you.

Want to see the output first? `examples/brendan/` has the finished skill files for [@BrendanOConnellWP](https://www.youtube.com/@BrendanOConnellWP), the channel this kit was built for.

```
skill/      the skill itself (this is what gets installed)
  creator.md  who you are: the one file you fill in by hand
prompts/    the distillation steps Claude Code runs over your data
tools/      scrapers, catalog builder, packager
data/       transcripts (yours in mine/, others' in research/)
scripts/    where finished video scripts land
examples/   a finished skill from a real channel, for reference
```

## Get your own copy

Click **Use this template** on GitHub and make your copy **private**. Your transcripts, analytics and draft scripts will live in it. Then clone it somewhere permanent. Your voice file will change over time, and git history lets you see how.

## One-time setup (about 1 to 2 hours, mostly waiting)

### 0. Prereqs
- [Claude Code](https://claude.com/claude-code)
- Python 3 and yt-dlp:
  ```bash
  python3 -m pip install -U yt-dlp      # Windows: py -m pip install -U yt-dlp
  ```

On Windows, use `py` instead of `python3` and the `.ps1` scripts instead of the `.sh` ones throughout.

### 1. Fill in `skill/youtube-scriptwriter/creator.md`
Your name, channel handle, niche, typical audience and video length, where scripts should be saved, and any hard writing rules (for example "no em dashes"). Delete the `STATUS` line when you're done. Everything else reads from this file.

### 2. Pull your channel (5 to 10 min)
```bash
python3 tools/fetch_channel.py @YourChannel --out data/mine
```
Add `--include-shorts` if you want Shorts. If YouTube blocks you with "confirm you're not a bot", re-run with `--cookies-from-browser chrome`.

### 3. Export your analytics (optional, but it makes the playbook much smarter)
YouTube Studio → Analytics → **Advanced mode** → Content tab → set the date range to Lifetime. Add the columns *Impressions click-through rate* and *Average percentage viewed*, then Export → **CSV**. Save the table file as `data/mine/studio.csv`.

### 4. Pick creators to learn from
Edit `research-channels.txt` with 5 to 10 handles, then:
```bash
bash tools/fetch_research.sh 15         # Windows: .\tools\fetch_research.ps1 -Top 15
```
Their transcripts stay local (`data/research/` is gitignored). The playbook step extracts patterns from them, never their lines.

### 5. Distill (in Claude Code)
Open Claude Code in this folder and say, one at a time:
- `run step 1`: builds **voice.md**. **Then read it and edit it hard.** This file is 80% of the quality. Fix anything that doesn't sound like you, and add phrases you use that it missed.
- `run step 2`: summaries + **catalog.md**
- `run step 3`: **playbook.md**
- `run step 4`: picks **exemplars**

### 6. Install
```bash
bash tools/package_skill.sh             # Windows: .\tools\package_skill.ps1
```
- **Claude Code:** installed to `~/.claude/skills/`, so it works in any project.
- **Claude app (web/desktop/mobile):** upload `dist/youtube-scriptwriter.zip` in the Skills section of Claude's settings.

## Using it
Just ask: *"Write me a video on using Claude Code to build a component library"*. It checks your catalog for overlap, pitches 3 angles and hooks, waits for your pick, then writes the beat sheet, full script, titles, thumbnails and description.

Say *"just write it"* to skip the angle step, and *"make a Short from this"* for a 45-second cut.

## Keeping it current
After every few uploads, open Claude Code in this folder and say **"refresh"**. It pulls new videos, summarizes them, rebuilds the catalog and reinstalls the skill. Re-run step 1 about twice a year, or whenever your style shifts.

When a script comes out wrong in a consistent way, don't just fix that script. Add a line to `voice.md` so it never happens again.

## License
The kit (tools, prompts, `SKILL.md`, docs) is MIT licensed. See `LICENSE`. The files in `examples/brendan/` describe and quote a real creator's videos. They're there for reference only and aren't covered by the MIT license. Don't reuse them as your own voice.
