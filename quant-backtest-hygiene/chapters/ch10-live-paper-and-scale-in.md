# Chapter 10: Live Paper and Scale-In

> Quant Backtest Hygiene, Chapter 10.

## Core Idea

The live paper test is the final check before capital allocation. The institutional standard: 3-6 months of live paper trading, with a clear kill switch. **The fix**: scale in 5% per month up to the target AUM; the kill switch is a performance threshold (e.g. -10% drawdown) that pauses the strategy. **The test**: the live paper performance is consistent with the OOS; the live paper kill switch has not been triggered.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
