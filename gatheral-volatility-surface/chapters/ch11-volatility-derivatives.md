# Chapter 11: Volatility Derivatives

> Gatheral, *The Volatility Surface*, Chapter 11, pp. 133–155.

## Core Idea

**Volatility derivatives** are derivatives whose payoff depends on the realised volatility. **Variance swaps** have a payoff of `notional × (realised variance - strike)`. **Volatility swaps** have a payoff of `notional × (realised vol - strike)`. The pricing of variance swaps is **model-free** (under continuous trading, the variance swap can be replicated by a static position in options). The **log contract** is the building block: `E[log(S_T/S_0)] = -0.5 × ∫_0^T σ²_t dt - ∫_0^T r_t dt`.

## Key Concepts

- **Variance swap** — payoff on realised variance; statically replicable.
- **Volatility swap** — payoff on realised vol; convexity adjustment required.
- **VIX** — the 30-day variance swap rate on the S&P 500.
- **Model-free replication** — the static replication of a variance swap.
- **The log contract** — `E[-log(S_T/S_0)] = 0.5 × ∫_0^T σ²_t dt + ∫_0^T r_t dt` (under risk-neutral measure).
- **Convexity adjustment** — the difference between the vol swap and the variance swap.
- **SVI-based variance swap rate** — `VSR = √(∫_0^T w(k, T) dQ(K) / T)`, where `dQ` is the risk-neutral measure.

## Formulas & Tables

- **Variance swap rate (model-free)**: `VSR² × T = 2 × ∫_0^∞ (C(K, T) - C_ATM) / K² dK - (r-q)T`.
- **Log contract**: `E[-log(S_T/S_0)] = 0.5 × ∫_0^T σ²_t dt + ∫_0^T r_t dt`.
- **Convexity adjustment** (vol swap to variance swap): `vol² ≈ variance - 1/2 × variance² / ...` (a series expansion).

## Key Takeaways

1. The variance swap is statically replicable; the model-free formula is the institutional standard.
2. The log contract is the building block of the variance swap pricing.
3. The vol swap requires a convexity adjustment.

## Connects To

- ch03 (Implied Vol Surface), ch07 (Asymptotics), `hull-derivatives` ch20 (Exotic Options), ch25 (Real Options).
