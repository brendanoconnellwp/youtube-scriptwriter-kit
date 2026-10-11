# YouTube Scriptwriter kit

This repo builds and maintains a `youtube-scriptwriter` skill (in `skill/youtube-scriptwriter/`) from one creator's YouTube channel. Who that creator is lives in `skill/youtube-scriptwriter/creator.md`: name, channel handle, niche, defaults and writing preferences. Read it before any step below. If it still starts with `STATUS: NOT GENERATED`, help the user fill it in first.

## Pipeline
Setup (unnumbered, run on request or as part of "refresh"):
- Fetch: `tools/fetch_channel.py <channel from creator.md> --out data/mine`: the creator's transcripts and metadata.
- Research: `tools/fetch_research.ps1` (or `.sh`): top videos from the creators in `research-channels.txt`.

Distill steps (these match the README):
1. `prompts/01-voice.md` → `voice.md`
2. `prompts/02-summaries.md` → `data/mine/summaries.json` → `tools/build_catalog.py` → `catalog.md`
3. `prompts/03-playbook.md` → `playbook.md`
4. `prompts/04-exemplars.md` → `exemplars/`

Install: `tools/package_skill.ps1` (or `.sh`): zip for the Claude app, and install to `~/.claude/skills`.

When the user says "run step N", do the matching distill step above. When they say "refresh", run fetch with `--update`, then step 2 (new videos only), then `build_catalog.py`, then package. Re-run voice (step 1) only if they ask, or if 10+ new videos have come in since `voice.md` was last written.

## Rules
- `data/research/` is for pattern analysis only. Never copy other creators' lines into skill files.
- Follow the **Writing preferences** in `creator.md` in every file here, not just in scripts.
- Hand edits the creator makes to `voice.md` or `playbook.md` win. When regenerating, read the current file first and keep their edits unless they say otherwise.
- Generated scripts go in `scripts/`.

## Environment
- Windows: use `py` and the `.ps1` scripts in `tools/`. macOS/Linux: use `python3` and the `.sh` scripts.
