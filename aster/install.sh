#!/usr/bin/env bash
# Install / update the Aster Hermes profile. Idempotent: safe to re-run after editing this folder.
#   ./install.sh            install or update
#   DELIVER=telegram ./install.sh   deliver cron results to Telegram instead of local files
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DESK="$ROOT/desk"
PARENT="$(cd "$ROOT/.." && pwd)"
PROFILE="aster"
PHOME="${HERMES_ROOT:-$HOME/.hermes}/profiles/$PROFILE"
HPY="$HOME/.hermes/hermes-agent/venv/bin/python"
DELIVER="${DELIVER:-local}"

need() { command -v "$1" >/dev/null || { echo "missing: $1"; exit 1; }; }
need hermes; need uv
UV="$(command -v uv)"
[ -x "$HPY" ] || HPY="python3"
# Skill library: SKILL_DIRS (colon-separated) overrides; else Livres/Skills/<category>/; else the
# flat quant-finance repo this folder lives in.
if [ -z "${SKILL_DIRS:-}" ]; then
  if [ -d "$PARENT/Skills/fondamentaux" ]; then
    SKILL_DIRS="$PARENT/Skills/fondamentaux:$PARENT/Skills/finance-de-marche:$PARENT/Skills/gestion-de-portefeuille:$PARENT/Skills/finance-d-entreprise"
  elif [ -f "$PARENT/quant-orchestrator/SKILL.md" ]; then
    SKILL_DIRS="$PARENT"
  else
    SKILL_DIRS=""; echo "warning: skill library not found; set SKILL_DIRS"
  fi
fi

echo "== 1/6 profile"
if [ ! -d "$PHOME" ] || [ ! -f "$PHOME/config.yaml" ]; then
  # --clone: reuse your default model, provider and keys; Aster gets its own memory and sessions.
  hermes profile create "$PROFILE" --clone \
    --description "Quant research & crypto trading desk: hypotheses, validated backtests, risk, paper/live execution."
fi

echo "== 2/6 identity and skills"
cp "$ROOT/SOUL.md" "$PHOME/SOUL.md"
cp "$ROOT/distribution.yaml" "$PHOME/distribution.yaml"
mkdir -p "$PHOME/skills/quant-desk"
for s in "$ROOT"/skills/*/; do
  rm -rf "$PHOME/skills/quant-desk/$(basename "$s")"
  cp -R "$s" "$PHOME/skills/quant-desk/"
done

echo "== 3/6 config overlay"
[ -f "$PHOME/config.yaml.pre-aster.bak" ] || cp "$PHOME/config.yaml" "$PHOME/config.yaml.pre-aster.bak"
OVERLAY="$(sed -e "s#__ASTER_DESK__#$DESK#g" "$ROOT/config.overlay.yaml")"
OVERLAY="$OVERLAY" SKILL_DIRS="$SKILL_DIRS" "$HPY" - "$PHOME/config.yaml" <<'PY'
import os, sys, yaml
path = sys.argv[1]
cfg = yaml.safe_load(open(path)) or {}
over = yaml.safe_load(os.environ["OVERLAY"]) or {}
dirs = [d for d in os.environ.get("SKILL_DIRS", "").split(":") if d]
if dirs:
    over.setdefault("skills", {})["external_dirs"] = dirs
def merge(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(a.get(k), dict):
            merge(a[k], v)
        elif isinstance(v, list) and isinstance(a.get(k), list):
            a[k] = a[k] + [x for x in v if x not in a[k]]
        else:
            a[k] = v
merge(cfg, over)
yaml.safe_dump(cfg, open(path, "w"), sort_keys=False, allow_unicode=True)
PY

echo "== 4/6 cron scripts"
mkdir -p "$PHOME/scripts"
for f in "$ROOT"/hermes_scripts/*.sh; do
  sed -e "s#__ASTER_DESK__#$DESK#g" -e "s#__UV__#$UV#g" "$f" > "$PHOME/scripts/$(basename "$f")"
  chmod +x "$PHOME/scripts/$(basename "$f")"
done

echo "== 5/6 desk environment"
(cd "$DESK" && "$UV" sync --extra dev --quiet && "$UV" run --quiet desk init >/dev/null && "$UV" run --quiet pytest -q)

echo "== 6/6 scheduled jobs (created PAUSED: you resume them)"
existing="$(hermes -p "$PROFILE" cron list 2>/dev/null || true)"
mk() { # name schedule [args...]
  local name="$1"; shift
  if grep -q "$name" <<<"$existing"; then echo "  exists: $name"; return; fi
  hermes -p "$PROFILE" cron create --name "$name" --paused --deliver "$DELIVER" "$@" >/dev/null && echo "  created: $name"
}
mk aster-daily-desk "30 7 * * *" --workdir "$DESK" --skill aster-desk \
  "Run the Aster daily desk cycle for today following the aster-desk skill. Write reports/<today>-daily.md and reply with the 5-line summary."
mk aster-weekly-postmortem "0 18 * * 0" --workdir "$DESK" --skill aster-postmortem \
  "Run the weekly post-mortem following the aster-postmortem skill. Reply with the decisions needed from Samuel."
mk aster-risk-watchdog "every 15m" --no-agent --script aster-risk-watchdog.sh
mk aster-paper-trade "15 2 * * *" --no-agent --script aster-paper-trade.sh

cat <<EOF

Aster installed.
  Chat:            $PROFILE chat        (or: hermes -p $PROFILE chat)
  Desk:            $DESK
  Jobs (paused):   hermes -p $PROFILE cron list   then   hermes -p $PROFILE cron resume <id>
  Exchange keys:   cp $DESK/config/.env.example $DESK/config/.env  (testnet first; never paste keys in chat)
EOF
