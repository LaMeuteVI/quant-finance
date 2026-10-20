# X2 final desk-path verdict — `intraday-signed-flow-final`: REJECTED

**Date**: 2026-10-20 · **Review**: `Review 2026-10-21` · **Item**: X2
**Family**: `intraday-signed-flow-final`, final fixed-rule evidence n=1
**Ledger**: `H-20261020-024` — rejected; trial 27 is the final fixed-rule desk artifact
**Preregistration**: `research/notes/2026-10-20-X2-final-prereg.md`, written before the final run
**Report**: `backtests/H-20261020-024/20261020T172937Z-dev-intraday_signed_flow-v1.0.0/report.json`
**Grid**: C1b `research/atlas/cost-grid.csv`, SHA-256 `c5a244bbad1e870330613ea6610479ae3aedca00aa55918db8f24da4322e63c7`
**Sample**: dev only; cutoff strictly `< 2024-07-01T00:00:00Z`; holdout not read

## Decision

**REJECTED on the official `config/desk.yaml` dev gates.** This is an economic falsification, not a missing-channel or malformed-panel result. The exact file-by-file aggTrades materialiser reached the strategy with 11,520 active BTC 15m rows, finite values, and all source timestamps before the cutoff.

The final fixed rule is unchanged: causal trailing 500-bar quintiles, top/bottom quintile entry, 3-bar hold, engine lag 1, BTC/ETH spot, C1b spot costs, USD 250,000 AUM.

## Contract evidence from `report.json`

- `base.n_obs`: **11,520**
- `base.sharpe_ann`: **−58.2484921** — gate `>= 0.8`: FAIL
- `base.max_drawdown`: **−0.9996970** — gate `>= −0.35`: FAIL
- `statistics.dsr`: **2.6280334e−135** — gate `>= 0.95`: FAIL
- `stress.costs_x2.sharpe_ann`: **−92.8392135** — gate `>= 0.3`: FAIL
- `walk_forward.n_folds`: **175**
- `walk_forward.stability.mean_sharpe_ann`: **−73.2818699**
- `capacity_max_AUM_usd`: **0.0**
- `gross_price_pnl_ann`: **+0.1684661** (+16.8466%/yr)
- `funding_pnl_ann`: **0.0** — spot-only, no perp legs
- `cost_drag_ann`: **24.7142101**
- `statistics.lookahead.passed`: **true**, 8 checks, 0 violations
- `signed_flow_quality.active_rows`: **11,520**
- `signed_flow_quality.all_values_in_range`: **true**
- `signed_flow_quality.max_index`: **2024-06-30T23:45:00+00:00**
- `passed`: **false**

The report's gross price P&L is positive, but the rule's turnover makes it unharvestable. The negative net result is therefore consistent with the preregistered prediction and does not support promotion.

## Trial accounting

`H-20261020-024` is the final preregistered family record with exactly one desk trial (`trial_id=27`, `n_trials_family=1`, `sr_variance_trials=0.0`). Earlier `H-20261020-023` desk runs were pipeline diagnostics while fixing the active-window data plumbing; they are not counted in this final family and no trial was manually fabricated. The predecessor `H-20261020-022` remains a rejected custom-run record with `dev_trials: 0`; its strided panel was discarded.

## Controls

- No holdout read.
- No live, paper, key, order, or withdrawal action.
- No modification to `risk/`, `execution/`, `policies/`, or `config/risk_limits.yaml`.
- Full suite: **651 passed, 1 skipped**.

## Recomputed contract check

`uv run python research/notes/2026-10-20-verify-x2-report.py backtests/H-20261020-024/20261020T172937Z-dev-intraday_signed_flow-v1.0.0/report.json` returned `CONTRACT PASS` and printed every required metric above.
