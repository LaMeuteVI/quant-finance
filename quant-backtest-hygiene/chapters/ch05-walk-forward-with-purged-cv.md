# Chapter 5: Walk-Forward with Purged CV

> Quant Backtest Hygiene, Chapter 5.

## Core Idea

Walk-forward optimisation is the sequential train/test split with a rolling window. The institutional standard: purged k-fold (or CPCV) with an embargo of 1% of the sample size. **The fix**: use the  or  from ; never use standard k-fold on financial time series. **The test**: the OOS performance is the *distribution* across multiple paths, not a single number.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
