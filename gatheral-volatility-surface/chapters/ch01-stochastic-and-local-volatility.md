# Chapter 1: Stochastic Volatility and Local Volatility

> Gatheral, *The Volatility Surface*, Wiley 2004, Chapter 1, pp. 1–13.

## Core Idea

Two complementary models for the volatility surface. **Stochastic volatility (SV)**: the instantaneous vol is a random process; the implied vol surface is derived from the joint distribution of the vol and the price. **Local volatility (LV)**: the instantaneous vol is a deterministic function of the price and time; the implied vol surface is *exactly* consistent with the observed option prices (Dupire's formula). The two views are *complementary*, not contradictory: SV models are more realistic for the *dynamics*, LV models are more accurate for the *snapshot*.

## Frameworks Introduced

- **Stochastic Volatility (SV)**: `dS/S = μ dt + σ(t) dW_1`, with `σ(t)` following a random process (e.g. Heston, SABR).
- **Local Volatility (LV)**: `dS/S = μ dt + σ(S, t) dW`, with `σ(S, t)` a deterministic function.
- **Dupire's formula**: `σ_loc²(K, T) = [∂C/∂T + (r-q)K ∂C/∂K - qC] / (0.5 K² ∂²C/∂K²)`. The local vol that exactly reproduces the market smile.
- **The relationship**: `σ_loc²(K, T) = E[σ²(S_T, T) | S_T = K]`. The local vol is the conditional expectation of the instantaneous variance.

## Key Concepts

- **Implied vol surface** — the 2D surface of Black-Scholes implied vol as a function of strike and maturity.
- **Stochastic volatility** — the vol is itself random.
- **Local volatility** — the vol is a deterministic function of the price.
- **Dupire's formula** — the LV that exactly fits the market.
- **Risk-neutral vs real-world** — LV is invariant; SV parameters differ.

## Key Takeaways

1. SV is for the *dynamics*; LV is for the *snapshot*.
2. Dupire's formula gives the LV that exactly fits the market.
3. The two views are complementary; use LV for static replication, SV for dynamic hedging.

## Connects To

- ch02 (Heston), ch03 (Implied Vol Surface), ch07 (Asymptotics), `hull-derivatives` ch15 (Volatility Smiles).
