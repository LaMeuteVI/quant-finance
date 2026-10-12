# Chapter 2: Standardised Approach — Sensitivities-Based Method (SA-SBM)

> BCBS 457, MAR21.

## Core Idea

The **Sensitivities-Based Method (SBM)** is the FRTB SA core. For each risk factor (e.g. an interest rate at a specific tenor, an FX rate, an equity price, a commodity price, a credit spread), the bank computes **sensitivities** (delta = first derivative, vega = sensitivity to vol, curvature = second derivative). The sensitivities are aggregated within a **bucket** (a defined group of risk factors with similar characteristics), then aggregated across buckets using prescribed **correlation parameters**.

## Frameworks Introduced

- **Delta risk** — `Δ × P`, the linear sensitivity to a small move in the risk factor.
- **Vega risk** — `Λ × P`, the sensitivity to a small move in the implied vol.
- **Curvature risk** — the second-order sensitivity; the additional loss beyond the delta approximation.
- **Bucket structure** — risk factors are bucketed by asset class and risk type (e.g. IR buckets: 0-2y, 2-5y, 5-10y, 10-15y, 15-20y, 20-30y).
- **Correlation parameters** — prescribed within and across buckets; e.g. intra-bucket correlation 0.5-0.99, inter-bucket correlation 0.25-0.75.

## Formulas & Tables

- **Delta risk charge**: `Σ_buckets √(Σ_i Σ_j ρ_ij × Δ_i × Δ_j)` (intra-bucket), with prescribed `ρ_ij`.
- **Vega risk charge**: same structure with vega sensitivities.
- **Curvature risk charge**: the curvature scenario is a shock of `± RW` (risk weight) per bucket; the curvature risk is the maximum loss under these scenarios.
- **Risk weights** vary by asset class: e.g. for interest rates, 0.5-3% per bucket; for equities, 25-70%; for FX, 10-15%; for commodities, 18-60%; for credit, 0.5-13% (IG) or 1.5-22% (HY).

## Key Takeaways

1. The SBM is sensitivities-based, not VaR.
2. The three risk types: delta, vega, curvature.
3. The risk weights and correlations are prescribed by the regulator.
4. The aggregation is bucket-by-bucket then across buckets.

## Connects To

- ch01 (Introduction), ch03 (Default Risk), ch04 (Residual Risk), `hull-risk-management` ch17 (FRTB preview), ch14 (Model-Building).
