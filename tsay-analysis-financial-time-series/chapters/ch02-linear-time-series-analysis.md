# Chapter 2: Linear Time Series Analysis

> Tsay, Chapter 2. ARMA, ARIMA, identification, estimation, diagnostic checking.

## Core Idea

A **linear time series** is a process where the current value is a linear function of past values and current/past shocks. The **ARMA(p, q)** model is the workhorse: `X_t = φ_1 X_{t-1} + ... + φ_p X_{t-p} + ε_t + θ_1 ε_{t-1} + ... + θ_q ε_{t-q}`. **Stationarity** requires that the roots of the AR polynomial lie outside the unit circle; **invertibility** requires that the roots of the MA polynomial lie outside the unit circle. **ARIMA(p, d, q)** extends ARMA to non-stationary series with `d` differences.

## Key Concepts

- **AR(p)** — autoregressive of order p: `X_t = φ_1 X_{t-1} + ... + φ_p X_{t-p} + ε_t`.
- **MA(q)** — moving average of order q: `X_t = ε_t + θ_1 ε_{t-1} + ... + θ_q ε_{t-q}`.
- **ARMA(p, q)** — the combination.
- **ARIMA(p, d, q)** — ARMA on the `d`-th difference.
- **Stationarity** — the AR roots must lie outside the unit circle.
- **Invertibility** — the MA roots must lie outside the unit circle.
- **Identification** — the Box-Jenkins approach: ACF, PACF, AIC, BIC.
- **Estimation** — maximum likelihood, conditional least squares.
- **Diagnostic checking** — residual ACF, Ljung-Box test.
- **Forecasting** — recursive substitution, mean-squared error.
- **Unit root test (ADF, PP, KPSS)** — tests for non-stationarity.

## Formulas & Tables

- **AR(1)**: `X_t = φ X_{t-1} + ε_t`; stationary iff `|φ| < 1`; mean `μ = 0`; variance `σ²/(1-φ²)`.
- **AR(p) characteristic polynomial**: `Φ(B) = 1 - φ_1 B - ... - φ_p B^p`; roots outside unit circle for stationarity.
- **ACF of AR(1)**: `ρ(h) = φ^|h|`.
- **PACF of AR(1)**: `φ(1) = ρ(1); φ(h) = 0` for `h > 1`.
- **ACF of MA(1)**: `ρ(1) = θ/(1+θ²); ρ(h) = 0` for `h > 1`.
- **PACF of MA(1)**: tails off.
- **Ljung-Box statistic**: `Q(m) = T(T+2) Σ_{h=1}^{m} ρ̂²(h) / (T-h)`; `~χ²(m-p-q)` under H0 of white noise residuals.

## Key Takeaways

1. ARMA(p, q) is the workhorse for linear time series.
2. Box-Jenkins: identify, estimate, diagnose, forecast.
3. Ljung-Box is the diagnostic for residual autocorrelation.

## Connects To

- ch01 (Stylised facts), ch03 (ARCH/GARCH), ch04 (Nonlinear), ch08 (VAR), `lopez-de-prado-afml` ch05 (FFD).
