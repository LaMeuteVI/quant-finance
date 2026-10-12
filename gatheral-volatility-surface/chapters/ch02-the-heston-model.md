# Chapter 2: The Heston Model

> Gatheral, *The Volatility Surface*, Chapter 2, pp. 15–24.

## Core Idea

The **Heston model** is the workhorse stochastic volatility model. The SDE is `dS/S = √v dW_1, dv = κ(θ - v) dt + σ_v √v dW_2`, with `dW_1 dW_2 = ρ dt`. The model has closed-form solutions for European options via the characteristic function; the parameters are: `v_0` (initial variance), `κ` (mean reversion speed), `θ` (long-run variance), `σ_v` (vol-of-vol), `ρ` (correlation). The Heston model produces a *smile* that steepens as the vol-of-vol rises; the *skew* is driven by the correlation `ρ` (negative for equities, producing the observed left skew).

## Key Concepts

- **Heston SDE** — the coupled SDE for the price and variance.
- **Mean reversion** — the variance reverts to `θ` with speed `κ`.
- **Vol-of-vol** — the volatility of the volatility; `σ_v`.
- **Correlation** — the `ρ` between the price and variance innovations; negative for equities.
- **Characteristic function** — the Fourier transform of the option price; the basis for the Heston closed form.
- **Feller condition** — `2 κ θ > σ_v²`; ensures the variance stays positive.
- **Heston implied vol** — the BS implied vol that matches the Heston price; requires numerical inversion.
- **Risk-neutral vs real-world** — the Heston parameters differ; the *risk-neutral* parameters are what matter for pricing.

## Formulas & Tables

- **Heston SDE**: `dS/S = √v dW_1`, `dv = κ(θ - v) dt + σ_v √v dW_2`, `dW_1 dW_2 = ρ dt`.
- **Characteristic function**: `φ(u) = exp(C(τ, u) + D(τ, u) v_0 + iu log S_0)`, with `C, D` closed-form in `τ, u, κ, θ, σ_v, ρ`.
- **Feller condition**: `2 κ θ > σ_v²`.
- **Heston price**: `C = S_0 P_1 - K exp(-rT) P_2`, where `P_1, P_2` are computed by inverse Fourier transform of `φ`.

## Key Takeaways

1. Heston is the workhorse SV model; closed-form via characteristic function.
2. The skew is driven by the correlation `ρ`; the smile by the vol-of-vol `σ_v`.
3. The Feller condition ensures positive variance.

## Connects To

- ch01 (SV vs LV), ch03 (Implied Vol Surface), ch04 (Heston-Nandi), `hull-derivatives` ch17 (Volatility Surfaces), ch20 (Exotic Options).
