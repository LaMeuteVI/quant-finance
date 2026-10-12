# Chapter 6: Spread Stationarity

> Quant Backtest Hygiene, Chapter 6.

## Core Idea

For pairs trading and statistical arbitrage, the spread must be stationary. The institutional test: ADF (Augmented Dickey-Fuller) on the spread; reject H0 (unit root) at 95%. The institutional response: if non-stationary, the strategy is spurious; abandon it. **The test**: the half-life of the mean reversion must be positive; the half-life must be shorter than the strategy's holding period.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
