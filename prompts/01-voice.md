# Step 1: Distill the creator's voice → skill/youtube-scriptwriter/voice.md

You're building the voice profile a scriptwriting skill will follow every time it writes for the creator named in `skill/youtube-scriptwriter/creator.md`. Read that file first. Quality here decides everything downstream.

## Inputs
- `data/mine/index.json`: metadata, including views, for every video.
- `data/mine/*.md`: timestamped transcripts. These are auto-captions, so ignore misheard words and spelling. You're after rhythm, phrasing and structure.

## Method
1. Load index.json and rank the long-form videos by views. Read **every** transcript fully if the total is under ~250k words. Otherwise read the top 15 and the 10 most recent in full, and skim the rest (first 2 minutes and last minute of each).
2. Take notes as you go: actual phrases, openers, transitions, how they set up a demo, how they handle mistakes on camera, jokes, and recurring opinions.
3. Compare their best-performing videos with their weakest. Do the voice or delivery differ? Note it.
4. Watch for drift. If their style changed noticeably over time, weight the recent style and note the shift.

## Write `skill/youtube-scriptwriter/voice.md` (remove the STATUS line), under ~1,800 words:

1. **Who's talking.** 3 to 4 sentences: their stance, what they're known for, and how they relate to the viewer (peer? guide? been-there dev?).
2. **Openings.** How they actually start videos, with 3 to 5 short verbatim examples and timestamps/video titles.
3. **Explaining things.** Their patterns for teaching: analogies, "here's why", show-then-tell or tell-then-show, level of assumed knowledge.
4. **Sentence rhythm.** Typical length, fragments, questions to the viewer, filler they really use (keep a little, it's human), and words they lean on.
5. **Signature phrases.** 10 to 20 real phrases/verbal habits, each with how often it shows up (often/sometimes).
6. **Transitions and structure.** How they move between sections and signal what's next.
7. **Humor and personality.** What kind, how often, with examples.
8. **Opinions and recurring themes.** Positions they take repeatedly (on tools, their niche's ecosystem, AI, clients...).
9. **Screen demos.** How they talk while clicking through something.
10. **Sponsor reads and CTAs.** How they ask for likes/subs, point to other videos, and handle sponsor segments.
11. **Never.** Things absent from their speech that generic AI scripts add: hype words, a "YouTuber voice", fake enthusiasm. List them explicitly. Include every rule under **Writing preferences** in `creator.md`.
12. **Calibration pair.** One paragraph of a *generic AI YouTube script* on a topic from their niche, then the same content rewritten in their voice. This example teaches the skill more than any rule.

Keep verbatim quotes short (under ~20 words each). When done, print a 5-line summary and the 3 things you're least sure about, so the creator knows what to check.
