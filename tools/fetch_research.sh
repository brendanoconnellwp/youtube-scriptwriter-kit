#!/usr/bin/env bash
# Pull the top N videos from every channel in research-channels.txt.
#   bash tools/fetch_research.sh            (top 15 each)
#   bash tools/fetch_research.sh 25         (top 25 each)
#   bash tools/fetch_research.sh 15 --cookies-from-browser chrome
set -euo pipefail
cd "$(dirname "$0")/.."
TOP="${1:-15}"; shift || true
grep -vE '^\s*(#|$)' research-channels.txt | while read -r ch; do
  echo "=== $ch ==="
  python3 tools/fetch_channel.py "$ch" --out data/research --top "$TOP" "$@" || echo "!! $ch failed, continuing"
done
