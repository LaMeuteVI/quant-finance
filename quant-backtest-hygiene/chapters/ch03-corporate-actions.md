# Chapter 3: Corporate Actions

> Quant Backtest Hygiene, Chapter 3.

## Core Idea

Corporate actions (splits, dividends, M&A, spinoffs) must be correctly handled. The institutional danger: the price series is not adjusted for splits; the dividend is not reinvested; the M&A consideration is not in the price. **The fix**: use a total-return index (TR) that includes dividends; use a split-adjusted price series. **The test**: the price ratio before/after a split must be 1:2 (or 2:1); the dividend must be in the total return.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
