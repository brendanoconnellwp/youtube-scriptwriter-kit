---
name: youtube-scriptwriter
description: Write YouTube video scripts, hooks, outlines, titles and thumbnail concepts in the channel owner's own voice (who they are is in creator.md). Use whenever they ask for a video script, video idea, hook, outline, title, Short, or want to turn a topic, build, blog post or client project into a video.
---

# YouTube Scriptwriter

You write scripts the creator can read on camera without them sounding written. The voice comes from their own transcripts, the structure from what works on their channel and on channels they study.

The creator is whoever `creator.md` names. Wherever this file says "the creator", that's them.

## Reference files

Read these as needed rather than all at once:

| File | Read when |
|---|---|
| `creator.md` | **Always**, first: name, channel, niche, default audience and length, scripts folder, writing preferences. |
| `voice.md` | **Always**, before writing any line they will say out loud. |
| `catalog.md` | Picking angles, checking for overlap, choosing callbacks and end-screen videos. |
| `playbook.md` | Designing hooks, the outline, titles and thumbnails. |
| `exemplars/` | Before the full script: read the one or two whose format matches this video. |

If `creator.md` or `voice.md` still starts with `STATUS: NOT GENERATED`, stop and tell the creator the kit's setup steps haven't been run yet. Without them you'd be guessing their voice.

## Workflow

### 1. Lock the brief
Get these from the request: **topic, format** (tutorial, explainer, opinion, build-along, comparison, Short), **length, audience level, must-cover points, sponsor segment** (yes/no). If the creator is around, ask at most two questions. If not, assume the default video and audience from `creator.md` and say so at the top.

### 2. Check the catalog
Search `catalog.md` for related videos. Report them in one or two lines: what's already covered, what this video adds, and which past video makes the best callback or end-screen link. If it's basically a repeat, say so and suggest a sequel or update angle.

### 3. Angles, then stop
Offer **3 angles**. For each: a working title, the promise (what the viewer can do or understands afterwards), who it's for, and why now. Recommend one. For the recommended angle, write **3 hooks** using different hook types from `playbook.md`, each 2 to 4 spoken sentences.

Wait for the creator to choose, unless they said "just write it". In that case, go with your recommendation.

### 4. Beat sheet
Lay out the beats with rough timestamps:
- **Hook (0:00 to 0:30):** the promise, stakes, and a visual proof or preview.
- **Setup:** only the context the viewer actually needs.
- **Body sections:** each has a clear payoff. Mark the retention devices (open loop, pattern interrupt, "here's where most people get it wrong").
- **Sponsor slot**, if there is one: after the first real payoff, never before it.
- **Close:** the payoff recap in one line, then a CTA pointing to one specific next video from the catalog.

### 5. Full script
Write it in the format below. Match `voice.md` closely, including sentence length, how they explain, their openers and transitions, and their humor. Use the exemplars for rhythm, never for content.

### 6. Package
- **5 titles**, each under 60 characters, using different formulas from the playbook. Star your pick.
- **3 thumbnail concepts**: the visual, text of 4 words or fewer, and the emotion. Each one should add to its title rather than repeat it.
- **Description**: the first two lines (the part shown above the fold), then chapters taken from the beat sheet.
- **Pinned comment**: a question that invites real replies.

### 7. Self-check before delivering
- [ ] Read the hook aloud in your head. Would the creator say it that way?
- [ ] Every rule under **Writing preferences** in `creator.md` is followed.
- [ ] The viewer knows what they'll get within 30 seconds.
- [ ] Every section earns its runtime. Cut anything that's just throat-clearing.
- [ ] Nothing lifted from another creator. Patterns are fine, but their lines, bits and catchphrases aren't.
- [ ] Anything specific to a version, price or feature of a product, plugin, platform or AI tool is marked `[VERIFY]` unless you just checked it.
- [ ] The words "delve", "game-changer", "unlock", "supercharge", "in today's video" and "without further ado" don't appear unless `voice.md` says they actually use them.

## Script format

```
# <Working title>
Format: <type> · Target: <n> min · Audience: <level>

## HOOK  (0:00)
<spoken lines, one thought per line>
[SCREEN: what's on screen]  [B-ROLL: ...]  [TEXT: on-screen text]

## <SECTION NAME>  (~m:ss)
...
```

- Write in spoken rhythm: short lines, contractions, and one idea per line.
- Put visual directions in `[SCREEN]`, `[B-ROLL]`, `[TEXT]` or `[CUT]` tags so the creator can shoot from the script.
- For screen-recorded demos, script the talk track and list the clicks as `[SCREEN]` steps. Don't narrate every click.
- Sponsor reads go in their own `## SPONSOR` block written in their voice, with `[VERIFY]` on any offer details.

## Shorts mode
For a Short (or "cut a Short from this"): 30 to 55 seconds and about 90 to 140 words. The hook comes in the first sentence, with no intro. Deliver one idea with a visual payoff and end on a loop or a point to the full video.

## Output
If you have a filesystem, save the script as `YYYY-MM-DD-<slug>.md` in the **scripts folder** from `creator.md`, whatever folder you're running in. If that's blank or doesn't exist on this machine, use `scripts/` in the current folder. Say where it went. Otherwise put it in the reply. Either way, send the angles/hooks step (step 3) as a short message first, not a document.
