# Chapter 9: Interest Rate Risk

> Hull 4e, pp. 175–199. Duration, convexity, key rate durations, and the full-revaluation VaR.

## Core Idea

Interest rate risk is the risk of loss from a move in the yield curve. The standard measures are: (1) **duration** (the first-order sensitivity to a parallel shift); (2) **convexity** (the second-order sensitivity); (3) **key rate durations** (sensitivities to specific points on the curve); (4) **DV01** (dollar value of a 1bp move, the basis-point sensitivity); (5) **full-revaluation VaR** (the most accurate; uses the full revaluation logic, not a duration approximation). The **principal components analysis (PCA)** of yield-curve changes identifies the three main movements: level, slope, curvature.

## Key Concepts

- **Macaulay duration** — the weighted average time to cash flow.
- **Modified duration** — `D_mod = D_mac / (1 + y)`.
- **DV01** — `DV01 = D_mod × MV / 10000`; the dollar change for a 1bp move.
- **Convexity** — `C = Σ t(t+1) × CF_t / (1+y)^{t+2}`; the second derivative.
- **Key rate duration** — the sensitivity to a specific maturity on the curve.
- **DV01 vector** — the vector of DV01s at each maturity; the basis for key-rate VaR.
- **PCA of yield curve** — level, slope, curvature as the three main factors.
- **Full revaluation** — recomputing the position's value under each scenario; the only fully accurate method.
- **Yield-curve risk** — the risk of a non-parallel shift; the key rate and PCA approaches.

## Formulas & Tables

- **Duration approximation**: `ΔP ≈ -D_mod × Δy × P`
- **Convexity correction**: `ΔP ≈ -D_mod × Δy × P + 0.5 × C × (Δy)² × P`
- **DV01**: `DV01 = D_mod × P / 10000`
- **PCA factor loadings** (level, slope, curvature) from the historical covariance of yield changes.

## Key Takeaways

1. Duration is a first-order approximation; convexity is the second-order correction.
2. Key rate durations are needed for non-parallel shifts.
3. Full revaluation is the only fully accurate method; the duration approximation fails for options (gamma).

## Connects To

- ch12 (VaR), ch14 (Model-Building), ch17 (FRTB — interest rate risk), `ilmanen-yield-curve`.
