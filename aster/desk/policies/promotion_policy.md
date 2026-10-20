# Promotion policy: from paper to real money

Promotion to `live_pilot` and `live` is Samuel's decision, made with `desk promote` in his own terminal. Aster's job is to prepare an evidence pack and a recommendation, including the case against.

## Evidence pack (reports/YYYY-MM-DD-promotion-H-xxx.md)
1. Ledger extract: pre-registration, all trials (count, versions, notes), lessons.
2. Dev and holdout reports: Sharpe, DSR, PSR, MinTRL vs actual track length, max DD, stress results, regime breakdown, PBO if a sweep was run.
3. Paper record: days, z-score vs backtest, slippage realised vs modelled, rejected orders and reasons.
4. Capacity estimate at the proposed capital and at 10x.
5. What would make us stop: explicit kill criteria for this strategy (e.g. drawdown > 1.5x worst backtest drawdown, live Sharpe below 0 after MinTRL bars).
6. Skeptic section: the three strongest reasons this is not real.

## Gates
| To | Minimum |
|---|---|
| `live_pilot` | `paper_passed`; capital <= `capital_cap_usd`; kill criteria written; testnet run of >= 7 days without operational errors |
| `live` (scale up) | >= 90 days live pilot; live results within the backtest distribution (z >= -2); no unexplained incident; capital increase <= 2x per step |

## Demotion (automatic recommendation, human decision)
Recommend `paused` when: kill switch tripped by this strategy, live drawdown beyond its kill criterion, realised costs > 2x modelled, regime change that invalidates the mechanism, or data/venue incident.
