#!/usr/bin/env bash
# No-agent cron: prints only when the kill switch is on or losses near a limit (empty stdout = silent tick).
set -euo pipefail
DESK="__ASTER_DESK__"
cd "$DESK"
exec "__UV__" run --quiet desk risk status --alert-only
