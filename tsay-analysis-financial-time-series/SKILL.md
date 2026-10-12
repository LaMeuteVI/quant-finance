---
name: tsay-analysis-financial-time-series
description: "Knowledge base from Ruey S. Tsay, Analysis of Financial Time Series, 2nd ed. (Wiley 2005). Use when modelling financial time series with ARMA/ARIMA, fitting GARCH-family models (ARCH, GARCH, GJR-GARCH, EGARCH, TGARCH, APARCH) for conditional heteroskedasticity, computing realised variance from high-frequency data (bipower variation, two-scale RV, realised kernel), testing for unit roots (ADF, PP, KPSS) and cointegration (Engle-Granger, Johansen), running VAR or VECM multivariate models, building factor models (PCA, Fama-French 5-factor), or applying Bayesian MCMC inference. Covers 10 chapters on financial time series characteristics, linear models, conditional heteroskedasticity, nonlinear models, high-frequency data, VaR, multivariate models, multivariate volatility, principal components, and Bayesian MCMC."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Analysis of Financial Time Series (Tsay)

**Source**: Ruey S. Tsay, *Analysis of Financial Time Series*, 2nd ed. (Wiley 2005) | **Domain**: Fondamentaux | **Chapters**: 10 | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or framework name** (e.g. "GARCH", "VAR", "cointegration", "realised variance"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.

## Core Frameworks & Mental Models

1. **Stylised Facts** (ch01): returns are near zero mean, fat-tailed, negatively skewed for equities; volatility clusters; leverage effect; prices are I(1).
2. **ARMA(p, q) and ARIMA(p, d, q)** (ch02): the workhorse linear models. Box-Jenkins: identify, estimate, diagnose, forecast.
3. **GARCH(1,1) Family** (ch03): the workhorse vol model. GJR captures leverage; EGARCH is the log form; APARCH is the most general.
4. **Nonlinear Models** (ch04): TAR (threshold), MS-AR (Markov switching), STAR (smooth transition), NAR (non-linear AR).
5. **High-Frequency Realised Variance** (ch05): RV, BV (bipower, jump-robust), TSRV (noise-robust), RK (realised kernel).
6. **Value at Risk** (ch06): parametric VaR with GARCH; GARCH-t for fat tails; ES as the modern replacement.
7. **Multivariate Time Series** (ch07): VAR, VECM, Granger causality, Engle-Granger & Johansen cointegration, impulse response.
8. **Multivariate Volatility** (ch08): VEC, BEKK (positive-definite), CCC (constant correlation), DCC (dynamic correlation), factor GARCH.
9. **Principal Components and Factor Models** (ch09): PCA, Fama-French 5-factor model (Mkt-RF, SMB, HML, RMW, CMA).
10. **Bayesian MCMC** (ch10): Bayes' theorem, Gibbs sampler, Metropolis-Hastings, convergence diagnostics.

## Chapter Index

| # | Title | Key Frameworks | File |
|---|---|---|---|
| 1 | Financial Time Series and Their Characteristics | Stylised facts, ADF, unit root | [ch01](./chapters/ch01-financial-time-series-and-their-characteristics.md) |
| 2 | Linear Time Series Analysis | ARMA, ARIMA, Box-Jenkins, Ljung-Box | [ch02](./chapters/ch02-linear-time-series-analysis.md) |
| 3 | Conditional Heteroskedastic Models | ARCH, GARCH, GJR, EGARCH, TGARCH | [ch03](./chapters/ch03-conditional-heteroskedastic-models.md) |
| 4 | Nonlinear Models and Their Applications | TAR, MS-AR, STAR, bilinear | [ch04](./chapters/ch04-nonlinear-models-and-their-applications.md) |
| 5 | High-Frequency Data Analysis | RV, BV, TSRV, RK, microstructure | [ch05](./chapters/ch05-high-frequency-data-analysis.md) |
| 6 | Value at Risk | Parametric VaR, GARCH-t VaR | [ch06](./chapters/ch06-value-at-risk.md) |
| 7 | Multivariate Time Series Analysis | VAR, VECM, cointegration, Granger | [ch07](./chapters/ch07-multivariate-time-series-analysis.md) |
| 8 | Multivariate Volatility Models | VEC, BEKK, DCC, factor GARCH | [ch08](./chapters/ch08-multivariate-volatility-models.md) |
| 9 | Principal Components and Factor Models | PCA, Fama-French 5-factor | [ch09](./chapters/ch09-principal-components-and-factor-models.md) |
| 10 | Bayesian Statistics and MCMC | Bayes, Gibbs, M-H, R-hat | [ch10](./chapters/ch10-bayesian-statistics-and-mcmc.md) |

## Topic Index

- **ADF test** → ch01
- **APARCH** → ch03
- **AR(p)** → ch02
- **ARIMA** → ch02
- **ARCH** → ch03
- **ARMA** → ch02
- **Augmented Dickey-Fuller** → ch01
- **Bayesian inference** → ch10
- **BEKK** → ch08
- **Bipower variation (BV)** → ch05
- **Calendar effects** → ch01
- **CCC (Constant Conditional Correlation)** → ch08
- **Co-integration** → ch07
- **DCC (Dynamic Conditional Correlation)** → ch08
- **EGARCH** → ch03
- **Engle-Granger** → ch07
- **Fama-French factors** → ch09
- **Fat tails (excess kurtosis)** → ch01
- **Factor model** → ch09
- **GARCH** → ch03
- **Gibbs sampler** → ch10
- **GJR-GARCH** → ch03
- **Granger causality** → ch07
- **High-frequency data** → ch05
- **HMM / Markov switching** → ch04
- **Impulse response** → ch07
- **Johansen test** → ch07
- **Ljung-Box** → ch02
- **MA(q)** → ch02
- **MCMC** → ch10
- **Metropolis-Hastings** → ch10
- **Multivariate GARCH** → ch08
- **Multivariate time series** → ch07
- **Neural network (NN-AR)** → ch04
- **Nonlinear models** → ch04
- **PCA** → ch09
- **Realised variance (RV)** → ch05
- **Realised kernel (RK)** → ch05
- **TAR** → ch04
- **TGARCH** → ch03
- **Two-scale realised variance (TSRV)** → ch05
- **Unit root** → ch01
- **VAR** → ch07
- **VECM** → ch07
- **Volatility clustering** → ch01
- **Vol-of-vol** → ch03

## Related Skills

- **`hull-risk-management`** (finance-de-marche) — ch10 (Volatility), ch12 (VaR/ES) — the institutional risk management framework.
- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — ch05 (FFD) for stationary features; ch14 (DSR) for backtest statistics.
- **`hull-derivatives`** (finance-de-marche) — ch15 (Volatility Smiles) for the option-implied vol.
- **`gatheral-volatility-surface`** (finance-de-marche) — the option-vol surface.
- **`grinold-kahn-apm`** (gestion-de-portefeuille) — ch08 (Valuation in Theory) for factor premia.
- **`cfa-quantitative-methods`** (fondamentaux) — the CFA QM curriculum; covers time-series basics.
- **`diebold-mariano-forecast-accuracy`** (fondamentaux) — the forecast-comparison test that complements the time-series models.

## Scope & Limits

- **Coverage**: 2nd edition (2005); 10 chapters covering the canonical time-series curriculum.
- **Edition year**: 2005 — supplemented by:
  - The post-2005 GARCH extensions (GARCH-MIDAS, Realised GARCH).
  - The post-2005 SV extensions (stochastic vol with jumps).
  - The post-2010 machine learning for time series (LSTM, Transformer).
  These extensions are not in the source; the agent should consult modern surveys for the state of the art.
- **What the source does NOT cover**:
  - The Hull options/futures/swap pricing (see `hull-derivatives`).
  - The volatility surface (see `gatheral-volatility-surface`).
  - The ML-based backtest statistics (see `lopez-de-prado-afml`).
  - The institutional active management (see `grinold-kahn-apm`).
- **OCR / extraction quality**: pdftotext output is clean; no reconstruction needed.
- **Translation**: English.
