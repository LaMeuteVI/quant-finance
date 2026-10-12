---
name: aster-postmortem
description: Weekly critic review of paper/live trading vs backtests, writing lessons to the ledger. Run every Sunday.
version: 1.0.0
metadata:
  hermes:
    tags: [quant, postmortem, review, memory]
    category: quant-desk
    requires_toolsets: [terminal]
---

# Weekly post-mortem

## When to Use
Sunday cron, or after any incident or kill-switch event. Workspace `~/Desktop/Livres/Aster/desk`.

## Procedure
1. Integrity: `uv run desk journal verify`. A broken chain is an incident (skill `aster-risk-ops`).
2. Collect the last 7 days from `journal/decisions.jsonl`: decisions, rejections (with reasons), fills, equity snapshots, kill events.
3. For every hypothesis in `paper`, `live_pilot`, `live`: `uv run desk paper review --hypothesis H` (no `--record` unless the 28-day review is due). Compare with its dev report (`desk ledger show H`).
4. Find what losing periods have in common (regime, coin, time, event) and whether the backtest contained similar conditions.
5. Check execution: realised vs modelled slippage, rejected orders, operational errors.
6. Be blunt: which strategy underperforms its backtest and by how much (z-score), which should be paused, which mistake repeats.
7. Write `reports/<date>-postmortem.md` with `templates/postmortem.md`.
8. Write one `desk ledger lesson H "..."` per finding (short, factual, searchable).
9. Pause recommendations go to Samuel; you may set `paused` yourself only for paper strategies.

## Pitfalls
- Judging a strategy on one week (check MinTRL; say "noise" when it is noise).
- Writing narrative lessons without numbers.
- Skipping the lesson write-back: then the research loop does not learn.

## Verification
Report exists; `desk ledger show H` shows new lessons for each strategy discussed.
