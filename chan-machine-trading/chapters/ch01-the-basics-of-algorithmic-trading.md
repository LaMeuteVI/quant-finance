# Chapter 1: The Basics of Algorithmic Trading

> Chan, *Machine Trading* (formerly *Quantitative Trading* 2e), Wiley 2017, Chapter 1.

## Core Idea

Algorithmic trading is the discipline of designing, coding, and deploying automated trading strategies. The main categories: **(1) mean-reversion** (pairs trading, statistical arbitrage, ETF arbitrage), **(2) momentum** (cross-sectional momentum, time-series momentum), **(3) high-frequency** (market-making, statistical arbitrage at the tick level), **(4) event-driven** (earnings, M&A, macro). The chapter covers the structural requirements: data infrastructure, backtesting framework, execution algorithm, risk management, regulatory compliance.

## Key Concepts

- **Algorithmic trading** — automated strategy execution.
- **Mean-reversion** — the price reverts to a moving average.
- **Pairs trading** — long the underperformer, short the outperformer; statistical arbitrage.
- **Momentum** — long the past winners, short the past losers.
- **Statistical arbitrage** — pairs trading with multiple legs.
- **ETF arbitrage** — long the constituents, short the ETF (or vice versa) when the ETF deviates.
- **High-frequency trading (HFT)** — sub-second latency strategies.
- **Execution algorithm** — VWAP, TWAP, Implementation Shortfall.
- **Backtesting** — the historical simulation of the strategy.
- **Slippage** — the difference between the expected and actual execution price.

## Key Takeaways

1. The four strategy families: mean-reversion, momentum, HFT, event-driven.
2. Execution is as important as the signal.
3. Backtesting is necessary but not sufficient.

## Connects To

- ch02 (Factor Models), ch03 (Time Series), ch04 (AI), `hull-risk-management` ch05 (Trading), `lopez-de-prado-afml` ch11 (Dangers of Backtesting).
