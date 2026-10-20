# X2 final desk-path preregistration — exact signed-flow panel, family n=1

**Date**: 2026-10-20 · **Review**: `Review 2026-10-21` · **Item**: X2 final corrected desk run
**Family**: `intraday-signed-flow-final` — new family, n = 1
**Parent diagnostic**: `H-20261020-022` was rejected without a desk trial because its research runner used a strided tick sample; that panel was invalid. `H-20261020-023` is retained as a pipeline diagnostic; this final hypothesis is registered separately before the final desk run.
**Cutoff**: strict pre-cutoff data, `< 2024-07-01T00:00:00Z`
**Holdout**: not requested and must not be read.
**Cost grid**: C1b `research/atlas/cost-grid.csv`, SHA-256 `c5a244bbad1e870330613ea6610479ae3aedca00aa55918db8f24da4322e63c7`

## Hypothesis

On BTC/USDT and ETH/USDT spot, a bar's taker-side signed-volume imbalance predicts the next few 15-minute returns. Go long when the current imbalance is at or above its causal trailing 80th percentile, short at or below its trailing 20th percentile, hold for 3 bars, and remain flat between entries. The signal is traded through the desk pipeline, with C1b spot taker costs at the preregistered AUM of USD 250,000.

## Fixed rule

- Input: exact Binance spot aggTrades, columns `quantity` and `is_buyer_maker`.
- Signed flow: `+quantity` when `is_buyer_maker=False` (taker buy), `-quantity` otherwise; divide by total quantity per 15m bar.
- Thresholds: trailing 500-bar 80th/20th percentiles, shifted one bar for causality, minimum 250 observations.
- Holding: 3 bars, one position per symbol, maximum gross 1.0 across the two-symbol book.
- Costs: C1b spot grid; no maker assumption; no funding and no perp legs.
- Execution: engine lag 1, so bar-t signal is held from the next tradable bar.

## Universe and sample

- Universe: `BTC/USDT`, `ETH/USDT`.
- Timeframe: `15m`.
- Available aggTrades: BTC 2022-01 through 2022-04; ETH 2022-01 through 2022-02.
- The materialiser aggregates each Parquet partition's numerator and denominator before combining partitions; it never uses a strided sample.
- The materialiser asserts every source timestamp is before the cutoff and writes a provenance manifest.

## Prediction written before the final desk run

The earlier Q22 memo reported 15m Q4-Q0 spreads of +7.16 bps (BTC) and +14.37 bps (ETH), while the preregistered hurdle was 6 bps, not the memo's 60 bps. The desk run is judged by `config/desk.yaml` only:

- `min_obs >= 500`;
- `sharpe_ann >= 0.8`;
- `max_drawdown >= -0.35`;
- `DSR >= 0.95`;
- stress costs x2 `sharpe_ann >= 0.3`.

Prediction: the exact panel reaches the strategy and both axes fail `sharpe_ann` after C1b spot costs; the mechanism may remain positive gross but should be unharvestable at the prescribed 3-bar turnover. The same 6 bps hurdle is retained; it is not changed to 60 bps.

## Falsification and accounting

Reject if any official dev gate fails. Report, from the desk `report.json`: Sharpe, DSR, stress x2, walk-forward stability, capacity, funding P&L, gross price P&L, cost decomposition, observations, and the exact C1b grid. A failed channel load, all-zero weights, missing statistics, or implausible bar-volatility diagnostic is an infrastructure failure, not a falsification.

This is one final fixed-rule run in a new family at n=1. Diagnostic desk attempts with the same fixed rule do not constitute additional strategy versions. No parameter tuning, second version, holdout, live, paper, key, order, or protected risk/execution/policy/config-risk change is authorized.
