#!/usr/bin/env bash
# Build dist/app-footings-<version>.zip with the skill folder at the root of the archive.
set -euo pipefail
cd "$(dirname "$0")/.."
VERSION="$(cat VERSION)"
mkdir -p dist
OUT="dist/app-footings-${VERSION}.zip"
rm -f "$OUT"
zip -qr "$OUT" app-footings -x "*.DS_Store"
echo "Built $OUT"
