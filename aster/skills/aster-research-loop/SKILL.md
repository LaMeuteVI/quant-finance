---
name: aster-research-loop
description: Take one hypothesis from idea to verdict — register, code, backtest, diagnose, holdout, paper. Use for any strategy research.
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [quant, backtest, validation, overfitting, crypto]
    category: quant-desk
    requires_toolsets: [terminal]
---

# Aster research loop

## When to Use
You have an idea (from a memo, Samuel, a paper) and want a verdict. All commands run in `~/Desktop/Livres/Aster/desk` with `uv run`.

## Procedure
1. **Ledger check**: `desk ledger list --text <keywords>`; `desk ledger list --status rejected`. If already rejected, stop unless conditions changed (state which).
2. **Pre-register** with `templates/hypothesis.md`, then `desk ledger new ...`. Choose `--family` honestly (variants of one idea share a family). Prediction must contain `sharpe_ann_min` and `max_drawdown_floor`, at least as strict as `config/desk.yaml` gates.
3. **Theory pass**: load `quant-orchestrator` and route; for the method load the relevant skill chapter (e.g. `lopez-de-prado-afml` labeling, `chan-machine-trading` execution, `pairs-trading-partial-cointegration`). Note what the literature says about decay and crowding.
4. **Implement**: copy `templates/strategy_template.py`, register in `strategies/__init__.py`, write a unit test, `uv run pytest`.
5. **Dev backtest**: `desk backtest --hypothesis H --strategy S --params '{...}' --notes "v1: baseline"`. Read `checks`, `statistics`, `stress`, `worst_windows`.
6. **Diagnose before revising**: where does it lose (regime, coin, period)? Is the loss the mechanism failing or noise? A revision needs a written diagnosis in `--notes` and a version bump. Max 5 versions (enforced). Parameter sweeps: one version, export a returns matrix (one column per config) and run `desk pbo`; PBO > 0.3 means reject.
7. **Decide**:
   - fail after a fair test -> `desk ledger status H rejected --reason "..."` + `desk ledger lesson H "..."`;
   - pass -> `desk ledger status H backtest_passed --reason "trial <id>"`.
8. **Holdout (once)**: `desk backtest --hypothesis H --strategy S --params '{same}' --sample holdout`. Pass -> `holdout_passed`; fail -> `rejected` + lesson. No tuning after this, ever.
9. **Paper**: `desk ledger status H paper --reason "..."`; ask Samuel to enable the paper cron for H (or he runs it). After >= 28 days: `desk paper review --hypothesis H --record`; pass -> `paper_passed`.
10. **Report** each step with `templates/backtest_report.md` in `reports/`.

## Pitfalls
- Sharpe > 3 on daily crypto, or hit rate > 60% with tiny losses: suspect leakage or unrealistic fills first.
- Testing on today's top coins and calling it cross-sectional alpha (survivorship).
- Ignoring funding for perps, or using VIP fees.
- "Fixing" a failed holdout by changing the strategy and re-running: impossible by design; register a new hypothesis in the same family instead (the trial count follows the family).
- Reading DSR with N=1 as strong evidence: it equals PSR until the family has several trials.

## Verification
`desk ledger show H` lists every trial with artifact paths; `prereg_intact: true`; the report's numbers match `report.json`.
