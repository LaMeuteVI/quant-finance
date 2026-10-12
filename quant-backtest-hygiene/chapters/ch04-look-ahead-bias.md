# Chapter 4: Look-Ahead Bias

> Quant Backtest Hygiene, Chapter 4.

## Core Idea

Look-ahead bias is the use of future data in features or labels. The institutional danger: the feature is standardised with the full-sample mean; the label is the realised return that includes the close-to-close; the split is done without purging. **The fix**: features standardised *at each timestamp*; labels are the triple-barrier (see  ch03); the CV is purged (see  ch07). **The test**: shift the labels by one day; if the OOS performance is similar, the backtest had look-ahead.

## Key Takeaways

1. This check is mandatory for every backtest.
2. The cross-references (above) provide the methodology.
3. A backtest that fails this check is not a strategy.

## Connects To

See the SKILL.md "Related Skills" for the full cross-reference map.
