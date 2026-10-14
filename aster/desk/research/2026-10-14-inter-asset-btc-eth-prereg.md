# BTC–ETH inter-asset descriptive study — pre-registration

**Date:** 2026-10-14  
**Scope:** BTC/USDT and ETH/USDT spot, daily closes derived from audited pre-cutoff R2 minutes.  
**Purpose:** descriptive dependency and lead–lag triage only; no alpha claim and no strategy registration.

## Fixed design

- Development boundary: `2022-10-11T00:00:00Z`, matching the earlier N2 studies; no holdout bytes are read.
- Horizons: `1, 3, 7, 14, 30, 60` daily bars.
- Raw returns: `r^BTC_t = log(BTC_t/BTC_{t-1})`, same for ETH.
- Contemporaneous association: Pearson and Spearman correlations of same-day horizon returns.
- Lead–lag grid: BTC formation return at `t-k` versus ETH forward return from `t` to `t+h`, and the reverse direction, for `k ∈ {0,1,3,7}` and each horizon. The lag is applied before any correlation is calculated; no future values enter a formation variable.
- Residual diagnostics: OLS residual of ETH horizon return on BTC horizon return, and BTC residual on ETH, estimated on the development sample only. Report correlation of each residual with the lagged leader return.
- Annual stability: repeat the fixed contemporaneous BTC–ETH correlation by calendar year. No year is selected after viewing results.
- Multiple testing: two-sided Pearson p-values across the fixed lead–lag direction × lag × horizon grid; BH-FDR at `q=0.05`. The grid is a diagnostic family, not a set of independent trades.
- Bootstrap: 10,000 circular moving-block resamples with block length `max(5,h)` for the contemporaneous correlation intervals. Seed `20261014`.

## Exclusions

Daily bars with missing close values are excluded pairwise. No forward-fill is allowed. This study does not use post-cutoff data, funding, order books, or current snapshots.

## Decision rule

A descriptive relationship is retained for a future mechanism memo only if it is stable across at least two calendar years, survives BH-FDR, has a bootstrap interval excluding zero, and is economically large enough to exceed conservative costs after considering both legs. No strategy is backtested from this study. Any candidate requires a separate ledger preregistration.

## Artifacts

- Code: `src/aster/research/inter_asset_n2.py`
- CSV: `research/assets/2026-10-14-inter-asset-btc-eth.csv`
- Report: `research/assets/2026-10-14-inter-asset-btc-eth.md`
