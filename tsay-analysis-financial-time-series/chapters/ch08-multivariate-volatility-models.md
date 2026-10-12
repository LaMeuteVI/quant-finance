# Chapter 8: Multivariate Volatility Models and Financial Applications

> Tsay, Chapter 8. VEC, BEKK, DCC, factor GARCH.

## Core Idea

**Multivariate GARCH** models the dynamics of the covariance matrix. **VEC (Vector ARMA)** is the direct extension of GARCH to the multivariate case. **BEKK** (Baba-Engle-Kraft-Kroner 1990) ensures positive-definiteness. **CCC (Constant Conditional Correlation)** (Bollerslev 1990) assumes constant correlation but time-varying vol. **DCC (Dynamic Conditional Correlation)** (Engle 2002) generalises CCC to time-varying correlation. **Factor GARCH** reduces dimensionality via a few common factors.

## Key Concepts

- **Multivariate GARCH** — the joint dynamics of the covariance matrix.
- **VEC** — `H_t = C + A' ε_{t-1} ε_{t-1}' A + B' H_{t-1} B`.
- **BEKK** — `H_t = C C' + A' ε_{t-1} ε_{t-1}' A + B' H_{t-1} B`; positive-definite by construction.
- **CCC** — `H_t = D_t R D_t`, with `D_t` diagonal of vol and `R` constant correlation.
- **DCC** — `H_t = D_t R_t D_t`, with `R_t` time-varying.
- **Factor GARCH** — `r_t = Λ f_t + ε_t`, with `f_t` a low-dimensional factor.
- **RiskMetrics** — the J.P. Morgan multivariate EWMA; a special case of BEKK with `A = B`.

## Formulas & Tables

- **BEKK(1,1)**: `H_t = C C' + A' ε_{t-1} ε_{t-1}' A + B' H_{t-1} B`.
- **DCC**: `Q_t = (1 - a - b) × Q̄ + a × z_{t-1} z_{t-1}' + b × Q_{t-1}`; `R_t = diag(Q_t)^{-1/2} Q_t diag(Q_t)^{-1/2}`.
- **Factor GARCH**: `H_t = Λ D_t Λ' + Σ`, with `D_t` diagonal.

## Key Takeaways

1. BEKK ensures positive-definiteness; DCC allows time-varying correlation.
2. Factor GARCH reduces dimensionality for large portfolios.
3. The CCC/DCC family is the institutional standard.

## Connects To

- ch03 (Univariate GARCH), ch07 (Multivariate linear), ch09 (Bayesian), `hull-risk-management` ch11 (Correlations), `hull-risk-management` ch14 (Model-Building).
