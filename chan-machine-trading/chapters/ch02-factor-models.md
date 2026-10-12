# Chapter 2: Factor Models

> Chan, *Machine Trading*, Chapter 2.

## Core Idea

**Factor models** explain the cross-section of returns via systematic factors. The **Fama-French factors** (Mkt-RF, SMB, HML) are the institutional baseline; the **AQR factors** (Momentum, Quality, Value, Low-Vol) extend the framework. The **Barra risk model** is the institutional risk factor model with 30-80 risk factors. The **cross-sectional regression** of returns on factors gives the betas; the **time-series regression** gives the factor exposures and the alpha.

## Key Concepts

- **Factor model** — `R_i - R_f = α_i + Σ β_{i,k} × λ_k + ε_i`, with `λ_k` the factor premium.
- **Fama-French 3-factor** — Mkt-RF, SMB (size), HML (value).
- **Fama-French 5-factor** — adds RMW (profitability) and CMA (investment).
- **Carhart 4-factor** — adds UMD (momentum).
- **AQR factors** — Momentum, Quality, Value, Low-Vol, Carry.
- **Barra risk model** — the institutional cross-sectional risk model.
- **Alpha** — the intercept; the manager's contribution after factor exposures.
- **Information ratio (IR)** — alpha divided by residual risk; see `grinold-kahn-apm` ch05.
- **Time-series regression** — the regression of the strategy's return on the factor returns.
- **Cross-sectional regression** — the regression of all assets' returns on the factors at a point in time.

## Formulas & Tables

- **Factor model**: `R_i = α_i + Σ β_{i,k} × f_k + ε_i`, with `α_i` the alpha, `β_{i,k}` the factor loadings.
- **The Fama-French 3-factor**: `R_i - R_f = α + β_M × Mkt-RF + β_S × SMB + β_V × HML + ε`.
- **Time-series regression**: regress the strategy's excess return on the factor returns; `α` is the alpha, `β` are the loadings.
- **IR**: `IR = α / σ(α)`.

## Key Takeaways

1. The Fama-French factors are the institutional baseline.
2. The 5-factor model is the modern standard.
3. The Barra risk model is the institutional risk reference.

## Connects To

- ch01 (Basics), `grinold-kahn-apm` ch07, ch08 (Valuation), `tsay-analysis-financial-time-series` ch09 (PCA).
