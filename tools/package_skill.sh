#!/usr/bin/env bash
# Package the skill for Claude (app/web) and install it for Claude Code.
#   bash tools/package_skill.sh
set -euo pipefail
cd "$(dirname "$0")/.."
SKILL=skill/youtube-scriptwriter
if grep -q "^STATUS: NOT GENERATED" "$SKILL"/creator.md "$SKILL"/voice.md "$SKILL"/playbook.md "$SKILL"/catalog.md 2>/dev/null; then
  echo "Heads up: some reference files are still placeholders:"
  grep -l "^STATUS: NOT GENERATED" "$SKILL"/*.md
  read -r -p "Package anyway? [y/N] " ok; [[ "$ok" == "y" ]] || exit 1
fi
mkdir -p dist
rm -f dist/youtube-scriptwriter.zip
(cd skill && zip -qr ../dist/youtube-scriptwriter.zip youtube-scriptwriter -x '*.DS_Store')
echo "Built dist/youtube-scriptwriter.zip  -> upload this in Claude's Skills settings"

mkdir -p "$HOME/.claude/skills"
rm -rf "$HOME/.claude/skills/youtube-scriptwriter"
cp -R "$SKILL" "$HOME/.claude/skills/youtube-scriptwriter"
echo "Installed to ~/.claude/skills/youtube-scriptwriter  -> available in Claude Code everywhere"
