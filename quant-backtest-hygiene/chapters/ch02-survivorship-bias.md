# Chapter 2: Survivorship Bias

> Quant Backtest Hygiene, Chapter 2.

## Core Idea

Survivorship bias is the omission of delisted assets from the backtest. The institutional danger: the backtest universe is the *current* S&P 500, not the historical S&P 500. The bias is *upward*: the delisted assets had below-average returns. **The fix**: use the historical constituent list (CRSP for US, equivalent for other markets). **The test**: the backtest P&L must be the same on the current and the historical constituent lists.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
