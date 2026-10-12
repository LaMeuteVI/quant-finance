# Chapter 1: Testing Equality of Forecast Accuracy

> **Source**: Francis X. Diebold & Roberto S. Mariano (1995), "Comparing Predictive Accuracy", *Journal of Business & Economic Statistics*, 13(3), 253–280. Section 1 of the paper. ⚠ OCR source; formulas reconstructed.

## Core Idea

The Diebold–Mariano (DM) test is a **two-forecast comparison test** for the null hypothesis that two competing forecasts have **the same accuracy**. The test is *non-parametric* in the loss function (the loss can be asymmetric, non-quadratic), and *robust* to serial and contemporaneous correlation in the forecast errors. The test statistic is constructed from the *differential loss* `d_t = e_{1t} − e_{2t}` between the two forecasts, and the asymptotic distribution is standard normal under the null.

The DM test is the institutional default for forecast comparison; the modern extensions (Clark-West, Hansen SPA, White Reality Check) handle the nested and many-model cases.

## Frameworks Introduced

- **The Diebold–Mariano Test Statistic**:
  - Let `e_{1t}` be the loss of forecast 1, `e_{2t}` the loss of forecast 2, and `d_t = e_{1t} − e_{2t}` the differential loss.
  - The DM statistic is `DM = d̄ / √(V̂(d̄))`, where `d̄ = (1/N) Σ_t d_t` is the sample mean differential loss and `V̂(d̄)` is a HAC-robust estimate of the variance of `d̄`.
  - Under H0 (equal accuracy), `DM ~ N(0, 1)` asymptotically.
  - *When to use*: every time you compare two competing forecasts and need a test of equal accuracy.
  - *Why it works*: the test is *non-parametric* in the loss (any loss function works), and the HAC variance estimator is robust to serial and contemporaneous correlation.
  - *Failure mode*: small samples; the DM statistic is badly size-distorted in small N. Use the Harvey-Leybourne-Newbold (1997) small-sample correction.

- **The Loss Function `L(e_t)`**:
  - The loss function is *general*: it can be squared error (`L(e) = e²`), absolute error (`L(e) = |e|`), asymmetric (e.g. `L(e) = e` for under-prediction and `L(e) = 2e` for over-prediction), or any other function.
  - The choice of loss function is *substantive*: it encodes the cost of the forecast error to the user.
  - *When to use*: every time you set up a forecast comparison. The loss function is the key modelling decision.

- **The HAC Variance Estimator**:
  - `V̂(d̄) = (1/N²) × Σ_t (d_t − d̄)² + (2/N²) × Σ_{h=1}^{H} w_h × Σ_{t=h+1}^{N} (d_t − d̄)(d_{t−h} − d̄)`, where `w_h` is a kernel weight (Bartlett, Parzen, etc.) and `H` is the bandwidth.
  - The HAC estimator is robust to serial correlation in `d_t`.
  - *When to use*: always, in practice. The iid assumption is rarely satisfied in financial data.

- **The Forecast Comparison Setup**:
  - Forecast 1: the *proposed* forecast. Forecast 2: the *baseline* (e.g. the random walk, the consensus, the seasonal naïve).
  - The DM test answers: "Is forecast 1 significantly better (lower loss) than forecast 2?"
  - The test is *directional*: a positive DM statistic means forecast 1 has *higher* differential loss (i.e. forecast 1 is *worse*); a negative DM statistic means forecast 1 is *better*.

## Key Concepts

1. **Differential loss `d_t`** — the difference in losses between the two forecasts.
2. **Loss function `L(e)`** — the cost of the forecast error; the modelling choice.
3. **DM statistic** — the t-statistic of the differential loss; `N(0,1)` under H0.
4. **HAC variance** — the Heteroskedasticity-Autocorrelation Consistent variance estimator; robust to serial correlation.
5. **The bandwidth `H`** — the truncation lag for the HAC estimator; typically `H = ⌊N^(1/3)⌋` (Newey-West rule).
6. **Forecast 1 vs forecast 2** — the proposed vs the baseline; the test is *directional*.
7. **Two-sided vs one-sided** — the DM test can be one-sided (forecast 1 better than forecast 2) or two-sided.
8. **Asymptotic vs exact** — the asymptotic DM is `N(0, 1)`; the exact small-sample distribution is non-standard. Use the HLN (1997) correction for small N.

## Formulas & Reference Tables

**The DM statistic (one-sided)**

`DM = d̄ / √(V̂(d̄))`. Reject H0 (forecast 1 has same accuracy as forecast 2) in favour of H1 (forecast 1 has *lower* loss) if `DM < −z_α`.

**The HAC variance (Newey-West)**

`V̂(d̄) = (γ̂_0 + 2 × Σ_{h=1}^{H} (1 − h/(H+1)) × γ̂_h) / N`, where `γ̂_h = (1/N) × Σ_{t=h+1}^{N} (d_t − d̄)(d_{t−h} − d̄)`.

**The bandwidth (Newey-West rule)**

`H = ⌊N^(1/3)⌋`.

**The HLN (1997) small-sample correction**

`DM* = √((N + 1 − 2h + h(h−1)/N) / N) × DM`, where `h` is the forecast horizon. For `h = 1` and `N = 100`, the correction is approximately 1.05 (the DM statistic is divided by 1.05 to correct for small-sample size distortion).

**The loss function examples**

- Squared error: `L(e) = e²`.
- Absolute error: `L(e) = |e|`.
- Absolute percentage error: `L(e) = |e / y_t|`.
- Linex (asymmetric): `L(e) = exp(α × e) − α × e − 1` for `α > 0` (penalises positive errors more than negative).

## Mental Models

- **The DM test is a *t*-test on the differential loss.** The non-parametric loss function is the key innovation.
- **The HAC variance is essential.** Iid assumptions are wrong for financial data.
- **The small-sample correction is essential.** The uncorrected DM is badly size-distorted in small N.
- **The choice of loss function is a substantive modelling decision.** It encodes the user's preferences.

## Worked Example (RECOMPUTED)

*Setup.* Two competing forecasts over 100 periods. Differential losses: mean `d̄ = −0.05` (forecast 1 has lower loss on average), HAC variance `V̂(d̄) = 0.01`.

*Step 1 — DM statistic*:
- `DM = d̄ / √(V̂(d̄)) = -0.05 / √0.01 = -0.05 / 0.1 = -0.5`.

*Step 2 — Two-sided test at 95%*:
- Critical values: ±1.96. `|DM| = 0.5 < 1.96`. **Do not reject H0**. The forecasts are not significantly different in accuracy.

*Step 3 — One-sided test (forecast 1 better) at 95%*:
- Critical value: −1.645. `DM = -0.5 > -1.645`. **Do not reject H0** (forecast 1 is not significantly better).

*Step 4 — HLN small-sample correction*:
- With N = 100, h = 1: correction factor `√((100 + 1 − 2 + 0) / 100) = √(99/100) = 0.995`. So `DM* = DM / 0.995 = -0.503`. **Negligible correction.**

*Step 5 — With serial correlation*:
- Suppose `d_t` has AR(1) coefficient 0.3. The HAC bandwidth is `H = ⌊100^(1/3)⌋ = 4`. The HAC variance is *larger* than the iid variance, and the DM statistic is correspondingly *smaller* (in absolute value).

*Sanity check (Python).*
```python
import numpy as np
from scipy.stats import norm

N = 100
d_bar = -0.05
V_hat = 0.01
DM = d_bar / np.sqrt(V_hat)
print(f"DM = {DM:.3f}")  # -0.5
print(f"95% two-sided critical: ±1.96; |DM| < 1.96, do not reject")
print(f"95% one-sided (forecast 1 better): -1.645; DM > -1.645, do not reject")

# HLN correction
h = 1
DM_star = DM / np.sqrt((N + 1 - 2*h + h*(h-1)/N) / N)
print(f"DM* (HLN corrected) = {DM_star:.3f}")
```

## Anti-patterns

- **Using the iid variance in the presence of serial correlation.** Use the HAC variance.
- **Using the uncorrected DM in small samples.** Use the HLN correction.
- **Ignoring the choice of loss function.** The loss function is the modelling decision.
- **Comparing more than two forecasts with the DM test.** Use Hansen SPA or White Reality Check instead.
- **Using the DM test with nested forecasts.** Use the Clark-West (2001) correction.

## Key Takeaways

1. **The DM test** is the institutional default for two-forecast comparison.
2. **The differential loss** is the test statistic; the loss function is a modelling choice.
3. **The HAC variance** is essential; iid assumptions are wrong for financial data.
4. **The HLN (1997) small-sample correction** is essential for small N.
5. **The DM test is for *two* forecasts**; use Hansen SPA or White Reality Check for many.

## Connects To

- **ch02** (Extant Tests): the DM test's improvements over the pre-1995 tests.
- **ch03** (Monte Carlo Analysis): the size and power properties of the DM test.
- **ch04** (Empirical Example): the exchange-rate forecast comparison.
- **`lopez-de-prado-afml` ch14 (Backtest Statistics)**: the DSR is the multiple-testing-corrected version of the DM test for many models.
- **`hull-risk-management` ch12 (VaR and ES)**: the backtest of a VaR model uses the same DM-style comparison.
- **`grinold-kahn-apm` ch20 (The Historical Record)**: the comparison of mutual fund performance uses a related test.
- **`tsay-analysis-financial-time-series` ch08 (Vector Autoregressive Models)**: the DM test is used in multivariate forecasting.
