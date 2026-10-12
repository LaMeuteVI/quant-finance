# Chapter 10: Volatility

> Hull 4e, pp. 201–229. The ARCH/GARCH family, EWMA, realised volatility, implied vol.

## Core Idea

Volatility is the standard deviation of returns; it is *time-varying* and *clustered* (volatility is correlated across time). The standard models: (1) **EWMA** (exponentially weighted moving average) — `σ_t² = λ × σ_{t-1}² + (1-λ) × r_{t-1}²`; (2) **GARCH(1,1)** — the workhorse with `σ_t² = ω + α × r_{t-1}² + β × σ_{t-1}²`; (3) **GJR-GARCH** — the asymmetric version that captures the leverage effect; (4) **EGARCH** — the exponential version. **Implied volatility** is the volatility that makes the Black-Scholes price match the market; the **VIX** is the 30-day implied volatility of the S&P 500.

## Key Concepts

- **ARCH (Engle 1982)** — autoregressive conditional heteroskedasticity.
- **GARCH (Bollerslev 1986)** — generalisation with both autoregressive and moving-average components.
- **GJR-GARCH (Glosten-Jagannathan-Runkle 1993)** — asymmetric; captures leverage.
- **EWMA (RiskMetrics 1996)** — the J.P. Morgan standard; λ ≈ 0.94 for daily data.
- **RiskMetrics** — the J.P. Morgan standard for VaR.
- **Implied volatility** — the vol that matches the market price.
- **VIX** — the 30-day implied volatility of the S&P 500; the "fear gauge".
- **Volatility smile** — the dependence of implied vol on strike; see `hull-derivatives` ch15.
- **Volatility risk premium** — the difference between implied and realised volatility; positive on average for equity indices.
- **Realised volatility** — the historical vol computed from intraday or daily returns.

## Formulas & Tables

- **GARCH(1,1)**: `σ_t² = ω + α × r_{t-1}² + β × σ_{t-1}²`; persistence = α + β (must be < 1 for stationarity).
- **EWMA**: `σ_t² = λ × σ_{t-1}² + (1-λ) × r_{t-1}²`; with λ = 0.94, the half-life of a shock is ~11 days.
- **GJR-GARCH**: `σ_t² = ω + α × r_{t-1}² + γ × I_{r<0} × r_{t-1}² + β × σ_{t-1}²`; the asymmetry term γ captures the leverage effect.
- **VIX formula**: based on a strip of S&P 500 options, weighted to 30-day constant maturity.

## Key Takeaways

1. GARCH(1,1) is the institutional default for vol forecasting.
2. EWMA is the simpler alternative (RiskMetrics).
3. The volatility risk premium is positive on average for equity indices.
4. The VIX is the market's "fear gauge"; a high VIX signals stress.

## Connects To

- ch12 (VaR), ch14 (Model-Building), `tsay-analysis-financial-time-series` ch05 (GARCH), `hull-derivatives` ch15 (Volatility Smiles).
