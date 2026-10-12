# Chapter 19: Estimating Default Probabilities

> Hull 4e, pp. 401–427. PD estimation: ratings, market-implied, Merton, hazard rate.

## Core Idea

**Default probabilities (PDs)** can be estimated from: (1) **historical default rates** (Moody's, S&P, Fitch); (2) **market-implied default probabilities** (from CDS spreads or risky bond prices); (3) the **Merton model** (structural: equity as a call on assets); (4) **hazard rate models** (reduced-form: PD is the intensity of a Poisson process). The **Merton model** gives `PD = N(-d_2)` where `d_2 = (log(V_0/D + (r - σ_V²/2) T) / (σ_V √T))`, with `V_0` the asset value, `D` the debt face value, `σ_V` the asset volatility.

## Key Concepts

- **Cumulative vs marginal PD** — cumulative over a horizon vs marginal for a year.
- **Rating transition matrix** — Moody's, S&P, Fitch; the historical default rates by rating.
- **Merton model** — structural model; equity = call on assets.
- **Hazard rate (intensity)** — reduced-form model; PD(t, t+Δt) = 1 - exp(-λ(t) × Δt).
- **Credit spread** — the yield spread over the risk-free rate.
- **CDS spread** — the cost of credit protection; a market-implied PD.
- **Recovery rate** — the fraction of face value recovered in default; typically 40% for senior unsecured.
- **Merton d1, d2**: `d_1 = (log(V_0/D) + (r + σ_V²/2) T) / (σ_V √T)`, `d_2 = d_1 - σ_V √T`.
- **PD from Merton**: `PD = N(-d_2)`.
- **Risky duration** — the duration of a corporate bond, accounting for default.

## Formulas & Tables

- **Merton d1, d2**: as above.
- **Merton PD**: `PD = N(-d_2)`.
- **Merton equity value**: `E = V_0 N(d_1) - D exp(-rT) N(d_2)`.
- **Risky bond price**: `P = exp(-rT) × (1 - PD) + exp(-rT) × PD × R`, where `R` is the recovery rate (in decimals).
- **CDS-implied PD**: `PD = (1 - exp(-CDS_spread × T)) / (1 - R)`.
- **Hazard rate from CDS**: `λ(t) = CDS_spread(t) / (1 - R)`.

## Key Takeaways

1. PDs come from ratings, market-implied, Merton, or hazard-rate models.
2. The Merton model is the structural foundation; the hazard rate is the reduced-form alternative.
3. The CDS spread is the most liquid market-implied PD.

## Connects To

- ch20 (CVA), ch21 (Credit VaR), ch15-17 (Basel/FRTB credit risk), `tsay-analysis-financial-time-series` ch05 (Time series of credit spreads).
