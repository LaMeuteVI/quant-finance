# Chapter 6: Intraday Trading and Market Microstructure

> Chan, *Machine Trading*, Chapter 6. Order flow, bid-ask, market impact, HFT.

## Core Idea

**Intraday trading** and **market microstructure** are the discipline of how trades happen and what drives short-term prices. **Order flow imbalance** (signed volume), **bid-ask bounce**, **market impact** (square-root law), and **HFT** (sub-second latency) are the key concepts. The **Kyle (1985) lambda** is the price impact per share traded.

## Key Concepts

- **Order flow imbalance** — `OFI_t = buy_volume - sell_volume`; signed volume.
- **Bid-ask bounce** — the half-spread; the cost of liquidity.
- **Market impact** — `σ × √(Q/ADV) × Y`; the canonical impact model.
- **Kyle's lambda** — `λ = ΔP / Q`; the price impact per share.
- **HFT** — sub-second latency strategies; market-making, statistical arbitrage.
- **Order book** — the list of pending buy/sell orders.
- **Limit order book imbalance** — `OFI_BB = (Bid_size_t - Ask_size_t) / (Bid_size_t + Ask_size_t)`; a predictor of short-term price moves.
- **Trade classification** — Lee-Ready (1991); see `lopez-de-prado-afml` ch02.
- **Adverse selection** — the information content of an order; the dealer's concern.
- **Inventory risk** — the dealer's risk of holding inventory; the source of bid-ask spread.

## Formulas & Tables

- **Kyle's lambda**: `λ = ΔP / Q`; the price impact per share.
- **Market impact (square-root law)**: `Impact(Q) = σ × √(Q/ADV) × Y`.
- **Order flow imbalance (cumulative)**: `Θ_t = Σ_{i=1}^{t} sign(e_{t,i}) × |e_{t,i}|`; the running signed volume.

## Key Takeaways

1. The order book is the institutional structure.
2. Order flow imbalance is a short-term predictor.
3. The square-root law is the canonical impact model.

## Connects To

- ch01 (Basics), `lopez-de-prado-afml` ch02 (Information-driven bars), `hull-risk-management` ch16 (Transaction costs), `hull-derivatives` ch19 (Order book for options).
