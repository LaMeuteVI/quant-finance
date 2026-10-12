# Chapter 19: Microstructural Features

> López de Prado, AFML, Chapter 19, pp. 281–302.

## Core Idea

**Microstructural features** capture the short-term dynamics of the order book: the **order flow imbalance (OFI)**, the **VPIN (Volume-Synchronised Probability of Informed Trading)**, the **trade-sign imbalance**, the **quote imbalance**, and the **roll measure**. These features are predictive of short-term price moves; they are the workhorses of HFT strategies.

## Key Concepts

- **Order flow imbalance (OFI)** — the running sum of signed volume.
- **VPIN** — the volume-synchronised probability of informed trading; the institutional flow-toxicity measure.
- **Trade-sign imbalance** — the imbalance of buy vs sell trades; the simplest microstructure feature.
- **Quote imbalance** — `(bid_size - ask_size) / (bid_size + ask_size)`; a predictor of the next mid-price move.
- **Roll measure** — the bid-ask bounce estimator; `Roll = -cov(ΔP_t, ΔP_{t-1})`.
- **Corwin-Schultz spread** — the high-low spread estimator; a daily proxy for the bid-ask.
- **Amihud illiquidity** — `|return| / volume`; the price impact per dollar traded.
- **Kyle's lambda** — the price impact per share; see `chan-machine-trading` ch06.
- **Hasbrouck's lambda** — the price impact per dollar; the daily version of Kyle's lambda.

## Formulas & Tables

- **OFI**: `OFI_t = Σ_{i=1}^{N_t} sign(e_{t,i}) × |e_{t,i}|` (or in ticks, just `sign(e_{t,i})`).
- **Roll measure**: `Roll = -cov(ΔP_t, ΔP_{t-1})`; if positive, the bid-ask bounce.
- **Corwin-Schultz**: `Spread = (2 × (log(H_t/L_t))² - (log(H_t/L_t) × log(...))) ^ 0.5`; the daily bid-ask spread estimator.
- **Amihud illiquidity**: `ILLIQ_t = |r_t| / Volume_t`.
- **VPIN**: `VPIN = Σ |buy_volume - sell_volume| / (N × bucket_volume)`.

## Key Takeaways

1. The OFI is the most useful microstructure feature.
2. The VPIN is the institutional flow-toxicity measure.
3. The Roll, Corwin-Schultz, and Amihud are the daily proxies for the bid-ask and impact.

## Connects To

- ch02 (Financial Data Structures), ch18 (Entropy), `chan-machine-trading` ch06 (Intraday), `hull-derivatives` ch19 (Order book for options).
