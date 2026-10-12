# Chapter 5: Options Strategies

> Chan, *Machine Trading*, Chapter 5. Vol trading: dispersion, vol risk premium, gamma scalping.

## Core Idea

**Options-based strategies** are: (1) **dispersion trading** (long single-name vol, short index vol), (2) **vol risk premium harvesting** (short index vol, long realised), (3) **gamma scalping** (long the underlying option, dynamic rebalancing), (4) **covered calls / protective puts** (the institutional overlay). The **implied-realised vol spread** is the central concept.

## Key Concepts

- **Vol risk premium** — the difference between implied and realised vol; positive on average for equity indices.
- **Dispersion** — the difference between single-name and index vol; trading the correlation.
- **Covered call** — long the stock, short the call; the institutional income overlay.
- **Protective put** — long the stock, long the put; the institutional hedge.
- **Gamma scalping** — long the option, dynamic rebalancing of the underlying to profit from realised vol.
- **Vega exposure** — sensitivity to implied vol; the source of P&L for vol trades.
- **Theta decay** — the daily time-decay; the cost of holding a long-vol position.
- **Skew trading** — trading the shape of the smile; see `gatheral-volatility-surface` ch03.

## Key Takeaways

1. The vol risk premium is the most consistent source of vol-edge.
2. Dispersion trading isolates the correlation bet.
3. Gamma scalping requires dynamic rebalancing.

## Connects To

- ch01 (Basics), `gatheral-volatility-surface` (the vol surface), `hull-derivatives` ch15 (Volatility Smiles), `hull-risk-management` ch12 (VaR for option books).
