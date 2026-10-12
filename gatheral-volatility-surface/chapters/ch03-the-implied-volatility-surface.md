# Chapter 3: The Implied Volatility Surface

> Gatheral, *The Volatility Surface*, Chapter 3, pp. 25–42.

## Core Idea

The **implied volatility surface** is the 2D surface `σ_BS(K, T)` of Black-Scholes implied volatilities as a function of strike `K` and maturity `T`. The surface has a characteristic shape: **smile** (U-shape in strike, symmetric for FX, skewed for equities), **term structure** (the smile flattens at long maturities), and **skew** (the slope of the smile). The **SVI (Stochastic Volatility Inspired) parameterisation** `w(k) = a + b(ρ(k - m) + sqrt((k - m)² + σ²))` fits the surface with 5 parameters; the **arbitrage-free conditions** (no-butterfly-arbitrage, no-calendar-arbitrage) are the key constraints.

## Key Concepts

- **Implied vol surface** — the 2D surface of BS implied vols.
- **Smile** — the U-shape in strike.
- **Skew** — the slope of the smile; negative for equities, symmetric for FX.
- **Term structure** — the maturity dependence; smile flattens at long maturities.
- **SVI parameterisation** — `w(k) = a + b(ρ(k - m) + sqrt((k - m)² + σ²))`, 5 parameters, fit to the surface.
- **Butterfly arbitrage** — negative probability density; bounded by the second derivative of call prices.
- **Calendar arbitrage** — negative total variance as maturity increases; bounded by the time derivative.
- **SVI arbitrage-free conditions** (Gatheral-Jacquier 2011, the "raw SVI" conditions): the surface must satisfy the SVI parametric form *and* the no-butterfly + no-calendar conditions simultaneously.

## Formulas & Tables

- **SVI parameterisation**: `w(k) = a + b(ρ(k - m) + sqrt((k - m)² + σ²))`.
- **Total variance**: `w(k) = σ²_BS × T`.
- **Log-moneyness**: `k = log(K/F)`, with `F` the forward price.
- **No-butterfly-arbitrage (SVI)**: `b ≥ 0`, `0 ≤ |ρ| < 1`, `a + b σ sqrt(1-ρ²) ≥ 0`.
- **No-calendar-arbitrage (SVI)**: `∂_t b (1 ± ρ) ≤ 0` and `∂_t a - ∂_t b σ sqrt(1-ρ²) ≥ 0` for all `k`.

## Worked Example (RECOMPUTED)

*Setup.* SVI parameters `a = 0.04, b = 0.5, ρ = -0.7, m = 0, σ = 0.4`. Forward `F = 100`. Strike `K = 90` (log-moneyness `k = log(90/100) = -0.1054`).

*Step 1*: `w(k) = 0.04 + 0.5 × (-0.7 × (-0.1054) + sqrt(0.1054² + 0.16)) = 0.04 + 0.5 × (0.0738 + sqrt(0.01111 + 0.16)) = 0.04 + 0.5 × (0.0738 + 0.4133) = 0.04 + 0.5 × 0.4871 = 0.04 + 0.2435 = 0.2835`.
*Step 2*: For T = 0.5 years, `σ²_BS = 0.2835 / 0.5 = 0.567`; `σ_BS = 0.753` (75.3%).

## Key Takeaways

1. The SVI parameterisation fits the surface with 5 parameters.
2. The no-butterfly and no-calendar conditions are the arbitrage-free constraints.
3. The Gatheral-Jacquier 2011 conditions are the "raw SVI" reference.

## Connects To

- ch01 (SV/LV), ch02 (Heston), ch04 (Heston-Nandi), ch05 (Jumps), ch07 (Asymptotics), ch11 (Vol Derivatives), `frtb-market-risk-bcbs457`.
