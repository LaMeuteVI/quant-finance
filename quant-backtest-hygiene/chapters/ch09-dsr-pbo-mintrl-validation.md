# Chapter 9: DSR / PBO / MinTRL

> Quant Backtest Hygiene, Chapter 9.

## Core Idea

The DSR, PBO, and MinTRL are the institutional backtest statistics (see `lopez-de-prado-afml` ch14). **The test**: DSR ≥ 0.95; PBO ≤ 0.10; MinTRL ≤ the OOS history length. **The fix**: if any fails, the strategy is not yet significant; collect more data, reduce the number of trials, or abandon the strategy.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
