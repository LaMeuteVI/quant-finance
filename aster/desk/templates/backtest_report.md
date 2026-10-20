# Backtest report: <H-id> — <strategy> v<version> — <sample>

**Verdict**: PASS | FAIL — <one sentence>
**Artifact**: backtests/<H-id>/<folder>/report.json · **Trial id**: <n> · **Family trials**: <N>

## Hypothesis and prediction
<statement; pre-registered prediction JSON; prereg hash intact: yes/no>

## Setup
- Period: <start> -> <end> (dev | holdout), holdout sealed from <date>
- Universe: <symbols>, survivorship note: <...>
- Costs: fee <x> bps + slippage <y> bps per side; funding: yes/no
- Execution: lag 1 bar, rebalance <frequency>

## Results (net of costs)
| Metric | Base | Costs x2 | Costs x3 | Lag 2 |
|---|---|---|---|---|
| Sharpe (ann.) | | | | |
| CAGR | | | | |
| Max drawdown | | | | |
| Vol (ann.) | | | | |
| Turnover (ann.) | | | | |

Gross vs net: cost drag <x>/yr, funding drag <y>/yr.

## Statistical validity
PSR <.>, DSR <.> (N=<trials>, var SR=<.>), MinTRL <bars> vs <bars> observed, haircut Sharpe <.>, PBO <.> (if sweep), look-ahead test: <passed/violations>.

## Stress and regimes
Worst windows (from report.json) and what happened in each. Regime table.

## Gate checks
<copy `checks` from report.json>

## What was NOT tested / known weaknesses
<honest list>

## Decision and next step
<reject + lesson | next version + diagnosed reason | advance stage>
