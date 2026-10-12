# Chapter 7: Multivariate Time Series Analysis

> Tsay, Chapter 7. VAR, VECM, cointegration, Granger causality, impulse response.

## Core Idea

**Multivariate time series** have several components evolving jointly. The **VAR(p)** (Vector Autoregression) is the multivariate extension of AR(p): `Y_t = c + A_1 Y_{t-1} + ... + A_p Y_{t-p} + ε_t`. **Cointegration** (Engle-Granger 1987) is the property that a linear combination of non-stationary series is stationary; the **VECM (Vector Error Correction Model)** captures the short-run dynamics and the long-run equilibrium. **Granger causality** tests whether one series helps predict another. **Impulse response functions** trace the effect of a shock through the system.

## Key Concepts

- **VAR(p)** — `Y_t = c + A_1 Y_{t-1} + ... + A_p Y_{t-p} + ε_t`.
- **Stability** — roots of `det(I - A_1 z - ... - A_p z^p) = 0` outside the unit circle.
- **Granger causality** — `X` Granger-causes `Y` if past `X` helps predict `Y`.
- **Cointegration** — a linear combination of non-stationary series is stationary.
- **Engle-Granger test** — ADF test on the residuals of the cointegrating regression.
- **Johansen test** — the likelihood-based test for the number of cointegrating vectors.
- **VECM** — the error-correction representation of a cointegrated VAR.
- **Impulse response function** — the effect of a unit shock in one variable on the others over time.
- **Variance decomposition** — the fraction of the forecast error variance of each variable attributable to shocks in the others.
- **CCF (cross-correlation function)** — the correlation between `X_t` and `Y_{t-h}` for various lags.

## Formulas & Tables

- **VAR(1)**: `Y_t = c + A Y_{t-1} + ε_t`. Stable iff `|eig(A)| < 1`.
- **Engle-Granger**: `Y_t = α + β X_t + u_t`; test `u_t` for a unit root.
- **Johansen trace test**: `trace = -T × Σ log(1 - λ̂_i)`; compare to critical values.

## Key Takeaways

1. VAR is the workhorse for multivariate time series.
2. Cointegration is the property of a long-run equilibrium.
3. Granger causality tests for predictive information.

## Connects To

- ch02 (Linear), ch08 (Multivariate Vol), ch09 (Bayesian), `pairs-trading-partial-cointegration`.
