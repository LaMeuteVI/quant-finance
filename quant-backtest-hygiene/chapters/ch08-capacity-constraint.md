# Chapter 8: Capacity Constraint

> Quant Backtest Hygiene, Chapter 8.

## Core Idea

The capacity constraint is the AUM at which the strategy's transaction cost reaches the breakeven. The institutional standard: report the capacity for each AUM level; the backtest P&L must be net of the *expected* cost at the strategy's AUM. **The test**: the AUM capacity is the smaller of (a) the AUM at which the breakeven turnover equals the strategy's turnover, and (b) the AUM at which the position size reaches 5% of the average daily volume.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
