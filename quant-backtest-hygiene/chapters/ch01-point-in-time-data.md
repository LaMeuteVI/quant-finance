# Chapter 1: Point-in-Time Data

> Quant Backtest Hygiene, Chapter 1.

## Core Idea

PIT data is the discipline of using only the data that was available at the time of the decision. The institutional danger: macroeconomic data is *revised* (the Fed GDP release is a chain of vintages); equity fundamentals are restated; the data vendor provides the *current* version, not the *historical* version. **The fix**: subscribe to Bloomberg PIT, FRED ALFRED, or CRSP/Compustat PIT. **The test**: the backtest P&L must be reproducible from the PIT data; if it requires the *current* version, the backtest is invalid.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
