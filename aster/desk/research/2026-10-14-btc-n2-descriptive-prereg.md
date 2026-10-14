# BTC N2 — pre-registration of the descriptive return-dependence study

**Date:** 2026-10-14  
**Scope:** BTC/USDT spot, daily close bars derived from the audited pre-cutoff R2 1-minute store.  
**Exploration cutoff:** `2024-07-01T00:00:00Z`.  
**Purpose:** descriptive signal triage only; this memo is not a strategy registration and cannot advance a ledger hypothesis.

## Data boundary

Use only the pipeline's pre-cutoff BTC daily dataset. To preserve the sealed holdout of `H-20261013-001`, the primary analysis ends at the same development boundary used by its first trial; no observations in that hypothesis' holdout are read. No current exchange data, funding, or order-book data is used.

## Fixed design

For horizons `h ∈ {1, 3, 7, 14, 30, 60}` daily bars:

- formation return: `F_h(t) = log(C_t / C_{t-h})`;
- forward return: `Y_h(t) = log(C_{t+h} / C_t)`;
- primary dependence statistic: Pearson correlation `corr(F_h, Y_h)`;
- direction diagnostic: `mean(sign(F_h) * Y_h)` and continuation hit rate `P(sign(F_h) = sign(Y_h))`;
- inverse diagnostic: repeat with `-F_h`; it must show the mechanical sign reversal and is not an independent discovery;
- one-day lag placebo: use `F_h(t-1)` against `Y_h(t)`; this tests whether apparent alignment depends on exact close timing.

The overlapping horizon structure is retained and disclosed. No ranking of individual calendar buckets, technical indicators, or parameter variants is performed.

## Uncertainty and multiplicity

- 10,000 fixed-seed moving-block bootstrap resamples; block length `max(5, h)`; report 2.5%/97.5% percentile intervals for the primary correlation and mean signed forward return.
- Primary p-values are two-sided Pearson p-values and are explicitly labelled as unadjusted serial-dependence diagnostics; BH-FDR is applied across the six primary horizon tests at `q=0.05`.
- Results are descriptive. A surviving FDR result is a candidate mechanism, not evidence of a tradable edge.

## Falsification / decision rule

Do not pre-register a new BTC momentum or reversal strategy from this study unless at least one horizon has: (a) a bootstrap correlation interval excluding zero, (b) BH-adjusted `q < 0.05`, (c) directionally consistent placebo/inverse diagnostics, and (d) a gross effect large enough to justify a separate costed hypothesis. If no horizon survives, record the family as unconfirmed and move to ETH N0 or a different mechanism. No parameter tuning is allowed from this memo.

## Reproducibility

Implementation: `src/aster/research/btc_n2.py`  
Output: `research/assets/2026-10-14-btc-n2.csv` and `research/assets/2026-10-14-btc-n2.md`  
Seed: `20261014`; bootstrap count: `10000`.
