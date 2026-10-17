#!/usr/bin/env bash
# No-agent cron: deterministic paper rebalance for every hypothesis in a paper stage.
# No LLM in the order path. Live trading is never scheduled by this installer.
set -euo pipefail
DESK="__ASTER_DESK__"
cd "$DESK"
"__UV__" run --quiet desk trade run-all --broker paper
