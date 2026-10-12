# Chapter 6: Value at Risk

> Tsay, Chapter 6. VaR computation under various assumptions.

## Core Idea

**Value at Risk (VaR)** is the loss threshold exceeded with probability `1 - α`. Tsay's treatment is from a time-series perspective: how to compute VaR given a fitted **mean-variance model** (`r_t = μ_t + σ_t ε_t`, with `μ_t` the conditional mean and `σ_t` the conditional vol). The VaR is `VaR_α = -μ_t + z_α × σ_t` (where `z_α` is the standard normal quantile at `1 - α` for `r_t`). For non-normal returns, use the empirical quantile or a GARCH-t model.

## Key Concepts

- **VaR_α** — the loss threshold at confidence `α`.
- **Expected Shortfall (ES_α)** — the conditional expected loss beyond VaR; see `hull-risk-management` ch12.
- **Parametric VaR** — closed-form under normality.
- **Empirical VaR** — the empirical quantile of the fitted residuals.
- **GARCH-t VaR** — the GARCH with Student-t residuals; the institutional default for fat-tailed returns.
- **Backtesting** — Kupiec POF, Christoffersen; see `hull-risk-management` ch12 and `diebold-mariano-forecast-accuracy`.
- **The 1-day vs 10-day VaR** — the square-root-of-time rule.

## Formulas & Tables

- **Parametric VaR**: `VaR_α = -(μ_t + z_α × σ_t)` where `z_α` is the `(1-α)`-quantile of `N(0,1)`.
- **GARCH-t VaR**: `VaR_α = -(μ_t + t_α(ν) × σ_t × √((ν-2)/ν))`.
- **ES_α**: `ES_α = -μ_t + σ_t × φ(z_α) / (1-α)`, where `φ` is the standard normal density.

## Key Takeaways

1. The mean-variance decomposition `r_t = μ_t + σ_t ε_t` is the foundation.
2. The GARCH-t is the institutional default for fat-tailed returns.
3. ES is the modern replacement for VaR.

## Connects To

- ch03 (GARCH), ch07 (Multivariate), `hull-risk-management` ch12, `diebold-mariano-forecast-accuracy`.
