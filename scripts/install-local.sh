#!/usr/bin/env bash
# Install (or update) the skill in Claude Code for local testing.
# Usage: scripts/install-local.sh           -> ~/.claude/skills/app-footings
#        scripts/install-local.sh --project -> ./.claude/skills/app-footings (current directory)
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)/app-footings"
if [[ "${1:-}" == "--project" ]]; then DEST=".claude/skills"; else DEST="$HOME/.claude/skills"; fi
mkdir -p "$DEST"
rm -rf "$DEST/app-footings"
cp -r "$SRC" "$DEST/"
echo "Installed to $DEST/app-footings"
