# Chapter 9: Time-Series Analysis
> **Source**: CFA Program Curriculum 2022, Level II, Reading 3 · Quantitative Methods | DeFusco, McLeavey, Pinto, Runkle

## Core Idea
A time-series model predicts a variable from its own past (trend, autoregressive lags, seasonal lags) and is only valid when the series is covariance stationary and the residuals are not serially correlated. The whole reading is a diagnostic pipeline: plot, detrend or difference, fit AR(p), test residual autocorrelation, add seasonal lags, test for ARCH, then check out-of-sample RMSE. Regressing one trending series on another without checking unit roots and cointegration produces spurious results.

## Learning Outcomes Covered
- calculate predicted values from linear and log-linear trend models; choose between them and state their limits
- state the three conditions for covariance stationarity and why nonstationarity breaks inference
- specify AR(p), compute 1- and 2-step forecasts (chain rule), test residual autocorrelations
- compute the mean-reverting level; contrast in-sample vs out-of-sample forecasts; compare models by RMSE
- explain coefficient instability across sample periods
- characterize random walks (with/without drift), unit roots, the Dickey-Fuller test, first-differencing
- test and correct for seasonality with a seasonal lag; explain ARCH and forecast error variance
- decide when regressing one time series on another is valid (unit roots, Engle-Granger cointegration)
- choose and justify a time-series model for an investment problem

## Frameworks Introduced
- **Linear trend model**: `yₜ = b₀ + b₁t + εₜ`, constant absolute change b₁ per period.
  - When to use: series grows by a constant amount (plot looks like a straight line).
  - How: OLS on t = 1…T; out-of-sample forecast `ŷ_{T+k} = b̂₀ + b̂₁(T+k)`; check Durbin-Watson on residuals.
  - Failure mode: residuals persistently above/below the line (high R² can coexist with DW ≈ 0.4). Trend-fitted series are never covariance stationary.
- **Log-linear trend model**: `ln yₜ = b₀ + b₁t + εₜ`, constant growth rate `e^{b₁} − 1` per period.
  - When to use: series grows by a constant percentage (curved upward on a level plot, straight on a log plot).
  - How: regress ln y on t; forecast `ŷₜ = e^{b̂₀ + b̂₁t}` (exponentiate, do not forget).
- **AR(p) model**: `xₜ = b₀ + b₁xₜ₋₁ + … + b_p xₜ₋p + εₜ`.
  - When to use: stationary series whose current value depends on past values (most financial/accounting series).
  - How: (1) estimate AR(1); (2) compute residual autocorrelations; (3) t-test each against 0 with SE = 1/√T; (4) if any is significant, add a lag and repeat; stop when residuals are clean.
  - Why Durbin-Watson fails here: with a lagged dependent variable as regressor, DW is invalid, use residual autocorrelations instead.
- **Dickey-Fuller unit root test**: regress `xₜ − xₜ₋₁ = b₀ + g₁xₜ₋₁ + εₜ` with g₁ = b₁ − 1.
  - When to use: before fitting an AR model to any series that trends or looks like a random walk.
  - How: H₀: g₁ = 0 (unit root, nonstationary) vs Hₐ: g₁ < 0 (stationary). Compute the usual t-statistic but compare to Dickey-Fuller critical values (larger in absolute value than ordinary t values). Failing to reject means: first-difference and model the differences.
  - Failure mode: an ordinary t-test of b₁ = 1 is invalid because under H₀ the t-statistic is not t-distributed.
- **Engle-Granger cointegration test**: for two series each with a unit root: (1) regress yₜ = b₀ + b₁xₜ + εₜ; (2) Dickey-Fuller test on the residuals using Engle-Granger critical values; (3) fail to reject = not cointegrated (relation spurious); (4) reject = cointegrated (error stationary, regression valid for the long-run relation).
- **Seasonal-lag AR**: add the lag one year back (lag 4 quarterly, lag 12 monthly), e.g. `xₜ = b₀ + b₁xₜ₋₁ + b₂xₜ₋₄ + εₜ`. Detect by a significant residual autocorrelation at the seasonal lag.
- **ARCH(1)**: `εₜ ~ N(0, a₀ + a₁ε²ₜ₋₁)`. Test by regressing `ε̂²ₜ = a₀ + a₁ε̂²ₜ₋₁ + uₜ`; significant a₁ means ARCH. Forecast: `σ̂²ₜ₊₁ = â₀ + â₁ε̂²ₜ`.
- **Nine-step forecasting recipe**: see the decision flow in Formulas & Reference Tables.

## Key Concepts
- **Covariance stationary**: constant finite mean, constant finite variance, and autocovariance cov(yₜ, yₜ₋ₛ) = λₛ that depends only on the lag s (also called weakly stationary).
- **Serial correlation in AR models**: unlike in cross-sectional regression, it makes b̂₀ and b̂₁ inconsistent, not just the standard errors.
- **Autocorrelation (ρₖ)**: correlation of a series with itself k periods back; the standard error of a sample autocorrelation is 1/√T.
- **Mean reversion**: tendency to fall when above the long-run mean and rise when below; all covariance stationary series have a finite mean-reverting level.
- **Chain rule of forecasting**: a 2-step AR(1) forecast plugs the 1-step forecast into the model; forecast error variance grows with the horizon.
- **In-sample vs out-of-sample forecast error**: residuals within the estimation period vs errors in a later period. Out-of-sample matters because the future is out of sample.
- **RMSE**: square root of the mean squared forecast error; smaller is better and the criterion for comparing models out of sample.
- **Random walk**: `xₜ = xₜ₋₁ + εₜ`; best forecast is the last value; variance grows without bound (Var(xₜ) ≈ (t−1)σ²).
- **Random walk with drift**: `xₜ = b₀ + xₜ₋₁ + εₜ`, b₀ ≠ 0; changes have mean b₀.
- **Unit root**: lag coefficient b₁ = 1 (|b₁| > 1 is an explosive root); implies nonstationarity and an undefined mean-reverting level (0/0).
- **First-differencing**: Δxₜ = xₜ − xₜ₋₁; turns a series with a single unit root into a stationary one.
- **n-period simple moving average**: smoothing tool `(xₜ + … + xₜ₋(n−1))/n`; it lags turning points and is not a forecasting model.
- **MA(q) model**: `xₜ = εₜ + θ₁εₜ₋₁ + … + θ_qεₜ₋q`; its autocorrelations cut off to 0 after lag q, while AR autocorrelations decay gradually.
- **ARMA(p,q)**: combines AR lags and MA errors; unstable, hard to specify, rarely better than AR.
- **Cointegration**: two series with unit roots share a long-run relation so their linear combination (the residual) is stationary.
- **Spurious regression**: apparently significant coefficients and high R² produced by regressing nonstationary series.

## Formulas & Reference Tables
```
Linear trend:       ŷₜ = b̂₀ + b̂₁t
Log-linear trend:   ŷₜ = exp(b̂₀ + b̂₁t);  growth per period = e^{b̂₁} − 1
AR(1):              xₜ₊₁ = b₀ + b₁xₜ   (one-step forecast)
2-step (chain):     x̂ₜ₊₂ = b̂₀ + b̂₁x̂ₜ₊₁
Mean-reverting lvl: x* = b₀/(1 − b₁)     (requires |b₁| < 1)
Autocorrelation:    ρ̂ₖ = Σₜ₌ₖ₊₁ᵀ (xₜ−x̄)(xₜ₋ₖ−x̄) / Σₜ₌₁ᵀ (xₜ−x̄)²
Test of ρ(ε,k)=0:   t = ρ̂ₖ / (1/√T),  df = T − 2 (for AR(1))
Dickey-Fuller:      Δxₜ = b₀ + g₁xₜ₋₁ + εₜ,  g₁ = b₁ − 1,  H₀: g₁ = 0
Random walk:        xₜ = xₜ₋₁ + εₜ ;  with drift: xₜ = b₀ + xₜ₋₁ + εₜ
Differenced RW:     yₜ = Δxₜ = εₜ  (b₀=0, b₁=0, mean-reverting level 0)
n-period MA:        (xₜ + xₜ₋₁ + … + xₜ₋(n−1)) / n
MA(q):              xₜ = εₜ + θ₁εₜ₋₁ + … + θ_qεₜ₋q
ARMA(p,q):          xₜ = b₀ + Σ bᵢxₜ₋ᵢ + εₜ + Σ θⱼεₜ₋ⱼ
Seasonal AR(1):     xₜ = b₀ + b₁xₜ₋₁ + b₂xₜ₋₄ + εₜ  (quarterly); forecast uses xₜ₋₃ at t+1
ARCH(1):            σ̂²ₜ₊₁ = â₀ + â₁ε̂²ₜ ;  ARCH(p): σ²ₜ = a₀ + Σ aᵢε²ₜ₋ᵢ
RMSE:               √[ (1/n) Σ (actual − forecast)² ]
```

**Which test/model for which problem**

| Symptom or question | Tool | Action |
|---|---|---|
| Straight-line growth, DW near 2 | Linear trend | Forecast with b₀ + b₁t |
| Constant % growth, DW near 2 | Log-linear trend | Forecast exp(b₀ + b₁t) |
| Trend model residuals autocorrelated (DW far from 2) | Not stationary-clean | Difference (linear trend) or ln then difference (exp. trend), then AR |
| AR residual autocorrelation significant at lag 1-3 | Misspecified AR | Add lags (AR(2), …) |
| Significant residual autocorrelation at lag 4 (qtr) / 12 (mth) | Seasonality | Add seasonal lag |
| Autocorrelations decay slowly | AR process | Use AR |
| Autocorrelations drop to 0 after q lags | MA(q) process | Use MA(q) (rare in practice) |
| Series looks like random walk, b₁ ≈ 1 | Unit root | Dickey-Fuller; difference if H₀ not rejected |
| Squared residuals autocorrelated | ARCH | GLS/robust SEs; predict variance with ARCH formula |
| Regress series y on x | Test both for unit roots | See matrix below |

**Regression of one time series on another (single or multiple X)**

| Unit root in Y? | Unit root in X? | Cointegrated? | Can use regression? |
|---|---|---|---|
| No | No (all) | n/a | Yes, safe |
| Yes | No | n/a | No (error nonstationary) |
| No | Yes | n/a | No |
| Yes | Yes | No | No (spurious) |
| Yes | Yes | Yes | Yes for long-run relation only; not the best short-run model (use error-correction models) |

**Steps to build a forecast (reading's 9-step recipe)**
1. Define the problem; choose causal regression vs pure time-series.
2. Plot: look for linear/exponential trend, seasonality, regime shifts.
3. No seasonality or shift: try linear/log-linear trend; DW OK means done.
4. Serial correlation: make stationary (difference; ln then difference; split sample at the shift; seasonal lags).
5. Fit AR(1), test residual autocorrelations.
6. If significant, raise p until residuals are clean.
7. Check seasonality (graph or seasonal residual autocorrelation); add seasonal lag.
8. Test for ARCH on residuals; if present use GLS or other corrections.
9. Test out-of-sample performance (RMSE) against in-sample.

## Mental Models
- **Thermostat**: a stationary AR(1) pulls the series toward b₀/(1 − b₁) at a speed set by b₁; the smaller b₁, the faster the pull. A random walk has no thermostat.
- **R² lies for nonstationary series**: a random walk regressed on its own lag gives R² ≈ 0.99 yet changes are unpredictable (R² ≈ 0.001 in the differenced regression). Choose the model by stationarity tests, not R².
- **Residuals first**: in time series, the diagnostic is residual autocorrelation (not DW once a lagged dependent variable appears).
- **Longer is not safer**: a longer sample mixes regimes (Fed policy changes, fixed vs floating FX) and can make an unstable pooled model worse than a shorter stationary one.
- **Forecast fan**: each extra step adds error; trust 1-step far more than 12-step.
- **Prefer AR over ARMA**: unless 80+ observations and a strong reason, extra complexity buys instability not accuracy.

## Worked Example
**AR(1) forecast and mean-reverting level (Intel gross margin).** Estimated: `GM_t = 0.1513 + 0.7462·GM_{t−1}`, 65 observations, residual autocorrelation SE = 1/√65 = 0.124; all four lags have |t| < 1.7 so the model is not rejected.
- Mean-reverting level: 0.1513 / (1 − 0.7462) = **0.5961** (59.61%).
- Current GM 63%: 1-step = 0.1513 + 0.7462 × 0.63 = **0.6214**; 2-step = 0.1513 + 0.7462 × 0.6214 = **0.6150**. Further steps: 0.6102, 0.6066, … converging down to 0.5961.
- GM 55% gives 0.5617 (rises); GM 65% gives 0.6363 (falls), consistent with reversion to 59.61%.
- Verify with a loop `x=0.63; repeat 8 times: x = 0.1513 + 0.7462*x`; it prints 0.6214, 0.6150, 0.6102, 0.6066, 0.6040, 0.6020, 0.6005, 0.5994 (converging to 0.5961).

**Differenced log model (AstraZeneca).** `Δln S_t = 0.0222 − 0.5493 Δln S_{t−1}`; sales 8,405 then 8,872. Δ_t = ln(8872/8405) = 0.0541; next Δ = 0.0222 − 0.5493 × 0.0541 = −0.0075; forecast sales = 8,872 × e^{−0.0075} = **$8,806 million** (source rounds to 8,805). The mean-reverting level of the growth series is 0.0222/(1 + 0.5493) = 1.43% per quarter.

**ARCH(1) variance forecast.** With σ̂² = 6.3626 + 0.2754 ε², an error of 0 gives variance 6.3626 and an error of 1 gives 6.638.

**RMSE comparison (out of sample, Jan-Sep 2019 CPI).** AR(1) RMSE 1.9014 vs AR(2) 1.4157; AR(2) wins out of sample and in sample (SE 2.9208 vs 2.9687), but the sample is small and the fitted period mixes regimes (std dev of annualized inflation 2.86% for 1995-2007 vs 3.54% for 2008-2018).

## Anti-patterns
- **Using Durbin-Watson on an AR model**: invalid with a lagged dependent variable; test residual autocorrelations.
- **Ordinary t-test of b₁ = 1**: invalid under a unit root; use Dickey-Fuller critical values.
- **Fitting AR to a trending or random-walk level series**: gives biased b₁ and meaningless tests; difference first.
- **Judging by R²**: high R² on levels of a trend or random walk says nothing about forecastability.
- **Pooling regimes**: one model across policy-regime changes yields wrong order and coefficients; examine plots, split the sample.
- **Regressing unit-root series on each other**: spurious unless cointegrated.
- **Trusting ARMA/GARCH point estimates**: they move with sample and starting values; check robustness.
- **Ignoring ARCH**: standard errors are wrong, lags look significant when they are not.
- **Evaluating only in sample**: the future is out of sample; compare RMSE out of sample.

## Exam Focus & Traps
- Mean-reverting level `b₀/(1 − b₁)`; a random walk gives 0/0 (undefined); a differenced random walk has level 0 (with drift, b₀).
- Linear trend: absolute change per period; log-linear: growth rate is `e^{b₁} − 1`, not b₁ (b₁ = 0.05 gives 5.13%). Forecast must be exponentiated.
- Seasonal lag forecast for quarterly AR(1): `x̂ₜ₊₁ = b₀ + b₁xₜ + b₂xₜ₋₃` (lag 4 relative to t+1).
- Unit root test: H₀ is nonstationary; "fail to reject" means unit root, so difference. Cointegration test H₀ is no cointegration (unit root in residuals).
- Standard error of a residual autocorrelation is 1/√T; critical t uses df = T − 2 (about 2.0).
- Chain rule: 2-step forecast uses the 1-step forecast, not an actual.
- ⚠ **Errata** (L2 2022, Reading 3, Example 17): the sentence should read that the test statistics computed in Exhibits 13 and 14 are not valid because of ARCH in the AR(1) errors. Treat the AR(1) inference as invalid when ARCH is significant.
- ⚠ **Correction** (source arithmetic): Example 15's seasonal-lag forecast prints 0.0107 − 0.0154(0.01) + 0.7549(0.02) = 0.0256, but the printed coefficient on the first lag is −0.1540, giving 0.0107 − 0.1540 × 0.01 + 0.7549 × 0.02 = **0.0243** (2.43%). The source also shows inconsistent figures for the Starbucks log-linear model (R² 0.95 vs 0.9771; DW 0.12 vs 0.26) and the CPI trend (n = 294 vs 228, DW 1.2145 vs 1.09, and a stray e^0.0464 where e^0.0295 − 1 = 2.99% is meant); conclusions are unchanged.
- ARMA is a distractor: limitations are unstable parameters, hard order choice, and unproven forecast gains.
- MA(q) is a different thing from an n-period simple moving average (the latter smooths, the former models errors).

## Key Takeaways
1. Plot first; trending, seasonal or regime-shifting series are not covariance stationary and must be transformed before AR modeling.
2. Use linear trend for constant absolute growth, log-linear for constant percentage growth; a significant DW means a trend alone is insufficient.
3. Build AR models up: AR(1), test residual autocorrelations (SE 1/√T), add lags until clean, then add a seasonal lag if lag 4 or 12 is significant.
4. Mean-reverting level is b₀/(1 − b₁); multi-step forecasts converge toward it and get less certain.
5. Dickey-Fuller (H₀ unit root) before modeling; if unit root, first-difference (after taking logs for exponential growth).
6. Compare models by out-of-sample RMSE and watch coefficient stability across sample periods.
7. Test residuals for ARCH; if present, fix standard errors and use the ARCH equation to forecast variance.
8. Never regress one series on another unless both are stationary or they are cointegrated (Engle-Granger).

## Connects To
- **ch07**: linear regression assumptions (serial correlation, DW) that time series routinely violate.
- **ch08**: multiple regression diagnostics (heteroskedasticity, multicollinearity) reused for multi-series regressions.
- **ch10**: machine-learning forecasting alternatives; overfitting and out-of-sample validation parallel RMSE/stability checks.
- **`pairs-trading-partial-cointegration`**: cointegration is the statistical basis of pairs trading; Engle-Granger here is the simplest test of the spread being stationary.
- **`cfa-economics` ch04**: business-cycle series (GDP, inflation) are the typical subjects of trend and AR models.
