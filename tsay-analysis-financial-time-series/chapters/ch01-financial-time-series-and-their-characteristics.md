# Chapter 1: Financial Time Series and Their Characteristics

> Tsay, *Analysis of Financial Time Series*, 2nd ed. (Wiley 2005), Chapter 1.

## Core Idea

Financial time series have distinctive statistical properties that distinguish them from classical iid or stationary series: (1) **stylised facts** of asset returns: near-zero mean, fat tails (excess kurtosis), volatility clustering, leverage effect, autocorrelation of squared returns but not of returns; (2) **non-stationarity**: prices are typically I(1) (integrated of order 1); returns are typically I(0); (3) **calendar effects**: day-of-week, month-of-year, holiday effects. The chapter establishes the empirical regularities that the rest of the book formalises.

## Key Concepts

- **Asset return** — `r_t = (P_t - P_{t-1}) / P_{t-1}` (simple return) or `r_t = log(P_t / P_{t-1})` (log return).
- **Continuously compounded return** — `r_t = log(P_t) - log(P_{t-1})`.
- **Volatility clustering** — the autocorrelation of squared returns is positive; high-vol periods cluster.
- **Leverage effect** — the negative correlation between returns and future volatility; negative returns increase future vol.
- **Fat tails (excess kurtosis)** — the distribution of returns has heavier tails than the normal; the kurtosis is typically 4-30.
- **Skewness** — the distribution of returns is negatively skewed for individual equities; near zero for indices.
- **Calendar effects** — day-of-week (Monday effect), January effect, holiday effect.
- **Stationarity** — the property of constant mean, variance, and autocorrelation.
- **Unit root** — a non-stationary process with `|φ| = 1` in `X_t = φ X_{t-1} + ε_t`.
- **Augmented Dickey-Fuller (ADF) test** — the test for a unit root.

## Formulas & Tables

- **Simple return**: `R_t = (P_t - P_{t-1}) / P_{t-1}`.
- **Log return**: `r_t = log(P_t) - log(P_{t-1}) ≈ R_t` for small returns.
- **Multi-period return**: `R_{t1, t_k} = Π (1 + R_t) - 1`.
- **ADF test statistic**: `t = γ̂ / SE(γ̂)`, where `γ` is the coefficient on the lagged level in the regression `ΔX_t = α + βt + γX_{t-1} + Σ δ_i ΔX_{t-i} + ε_t`.

## Key Takeaways

1. Returns are near zero mean, fat-tailed, negatively skewed for equities.
2. Volatility is clustered; the leverage effect is real.
3. Prices are I(1); returns are I(0) but not iid.

## Connects To

- ch02 (Linear Time Series), ch03 (Conditional Heteroskedasticity), `hull-risk-management` ch10 (Volatility), `lopez-de-prado-afml` ch05 (FFD).
