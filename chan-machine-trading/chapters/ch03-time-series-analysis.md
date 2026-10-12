# Chapter 3: Time-Series Analysis

> Chan, *Machine Trading*, Chapter 3. ARMA, GARCH, cointegration for trading.

## Core Idea

**Time-series models** for trading: (1) **ARMA** for the mean dynamics, (2) **GARCH** for the variance dynamics, (3) **cointegration** for pairs trading, (4) **regime-switching** for trending vs. mean-reverting markets. The **half-life of mean reversion** is the key concept: `τ = log(2) / log(1/φ)` for an OU process `X_t = φ X_{t-1} + ε_t`.

## Key Concepts

- **ARMA** — the linear mean model.
- **GARCH** — the conditional vol model.
- **Cointegration** — long-run equilibrium between two series.
- **Ornstein-Uhlenbeck (OU) process** — the canonical mean-reversion model.
- **Half-life of mean reversion** — `τ = log(0.5) / log(φ)` for `X_t = φ X_{t-1} + ε_t`.
- **Pairs trading** — long the underperformer, short the outperformer; the cointegrating spread.
- **ADF test on the spread** — confirm the spread is stationary.
- **Regime-switching** — Markov-switching models for trend vs. range.
- **Volatility targeting** — size the position to target a constant vol.
- **Mean reversion test** — test that the spread is stationary.

## Formulas & Tables

- **OU process**: `X_t = φ X_{t-1} + ε_t`; stationary iff `|φ| < 1`.
- **Half-life**: `τ = log(0.5) / log(φ)`.
- **Cointegrating regression**: `Y_t = α + β X_t + ε_t`; `ε_t` is the spread, must be ADF-stationary.
- **Johansen test**: for the rank of cointegration; see `tsay-analysis-financial-time-series` ch07.
- **Vol targeting**: `position = target_vol / realised_vol × signal`.

## Key Takeaways

1. The half-life is the key parameter for mean-reversion strategies.
2. Cointegration is the foundation of pairs trading.
3. Vol targeting normalises the bet size across vol regimes.

## Connects To

- ch01 (Basics), ch02 (Factor Models), `pairs-trading-partial-cointegration`, `tsay-analysis-financial-time-series` ch02, ch07.
