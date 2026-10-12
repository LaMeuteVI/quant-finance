# Chapter 5: Fractionally Differentiated Features

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 5, pp. 75–91

## Core Idea

Price series are non-stationary (random-walk-like); returns are stationary but information-destroying. The chapter introduces **fractional differentiation** as a middle ground: a `d ∈ (0, 1]` order of differentiation that is *less* than the `d = 1` (full differencing) needed for stationarity, but *more* than `d = 0` (the raw price). The result is a *stationary* series that *retains* the long-memory of the price. The fixed-width window (FFD) implementation is the practical tool.

## Frameworks Introduced

- **The Fractional Differentiation Operator**:
  - `(1−x)^d = Σ_{k=0}^{∞} (−1)^k × binom(d, k) × x^k = Σ_{k=0}^{∞} w_k × x^k`, where the weights are `w_k = (−1)^k × binom(d, k)`.
  - For `d = 0`: `w_0 = 1`, all others zero — the original series.
  - For `d = 1`: `w_0 = 1, w_k = (−1)^k × binom(1, k) = (−1)^k × 0 = 0` for `k > 0` ... actually for `d = 1`, the weights are `(1, −1, 0, 0, ...)` — the standard first-difference.
  - For `d ∈ (0, 1)`: a long, decaying sequence of weights that produces a stationary, memory-preserving series.

- **The Minimum Order of Fractional Differentiation (FFD)**:
  - The smallest `d` for which the differentiated series passes an Augmented Dickey-Fuller (ADF) stationarity test.
  - Empirically, `d` is in the range `0.2–0.5` for most price series; less than 1 (which would be the full difference) and greater than 0 (which would be the raw price).

- **The Fixed-Width Window (FFD) Implementation**:
  - The weights `w_k` decay quickly for moderate `d`; after some `k*`, the weights are negligibly small. The FFD truncates the series at `k*` (a hyperparameter) and applies only the first `k*` weights.
  - The benefit: the FFD can be applied to a streaming series; only the last `k*` observations are needed.
  - The cost: a small amount of memory is lost (the contributions of the truncated weights).

- **The ADF Test for the FFD Threshold**:
  - For a given `d`, apply the FFD to the series, then run the ADF test. The smallest `d` for which the ADF p-value is below 0.05 (or 0.01) is the FFD threshold.

## Key Concepts

1. **Fractional differentiation** — applying `(1−x)^d` with `d ∈ (0, 1)` to a price series.
2. **Fixed-width window (FFD)** — the practical implementation of fractional differentiation.
3. **Memory** — the long-range dependence of the series; the FFD preserves more memory than the full difference.
4. **Stationarity** — the property of having a constant mean, variance, and autocorrelation function; required for many ML models.
5. **ADF test** — the Augmented Dickey-Fuller test for a unit root; the test for stationarity.
6. **The binomial series** — `(1−x)^d = Σ binom(d, k) (−x)^k`; the generalisation of `d` to non-integer values.
7. **Long memory** — the property of a series whose autocorrelations decay hyperbolically, not exponentially.

## Formulas & Reference Tables

**The fractional differentiation weights**

`w_k = (−1)^k × binom(d, k) = (−1)^k × (d!)/(k! × (d−k)!)` for integer `d`. For non-integer `d`, the gamma function generalises the binomial.

A more useful form:

`w_k = −w_{k−1} × (d − k + 1) / k` for `k ≥ 1`, with `w_0 = 1`.

**The fixed-width window (FFD)**

`X̃_t = Σ_{k=0}^{k*} w_k × X_{t−k}`, where `k*` is the truncation length (typically 100–1000).

**The ADF test statistic**

`ΔX_t = α + β × t + γ × X_{t−1} + Σ_{i=1}^{p} δ_i × ΔX_{t−i} + ε_t`. The null is `γ = 0` (unit root). Reject for low p-value.

**The minimum `d` (FFD threshold)**

`d* = min { d ∈ [0, 1] : ADF(FFD(X, d)) rejects at 95% }`. Empirically, `d* ∈ [0.2, 0.5]` for most price series.

## Mental Models

- **FFD is a memory-preserving differencing.** The full difference destroys memory; FFD preserves the long-range dependence.
- **The FFD threshold is asset-specific.** Equity indices have higher `d*` (more memory); commodity prices have lower.
- **The FFD weights decay slowly for small `d` and fast for `d` near 1.** The implementation must handle the long history for small `d`.

## Worked Example (RECOMPUTED)

*Setup.* 1000 days of an equity price series. Compute the FFD weights for `d = 0.4` with `k* = 100`.

*Step 1 — Compute the FFD weights*.
- `w_0 = 1`.
- `w_1 = −w_0 × (d − 0) / 1 = −0.4`.
- `w_2 = −w_1 × (d − 1) / 2 = 0.4 × (−0.6) / 2 = −0.12`.
- `w_3 = −w_2 × (d − 2) / 3 = 0.12 × (−1.6) / 3 = 0.064`.
- ...

*Step 2 — Apply the FFD*.
- `X̃_t = Σ_{k=0}^{100} w_k × X_{t−k}` for `t = 100, 101, ..., 999`.

*Step 3 — Test for stationarity*.
- Run the ADF test on `X̃`. The p-value should be < 0.05 for `d = 0.4`; the FFD threshold is around `d = 0.3–0.4` for most equity series.

*Sanity check (Python).*
```python
import numpy as np
from statsmodels.tsa.stattools import adfuller
np.random.seed(42)
# Simulate a price series with random-walk + drift
X = np.cumsum(np.random.normal(0.0005, 0.015, 1000)) + 100

def ffd_weights(d, k_max):
    w = np.zeros(k_max+1)
    w[0] = 1.0
    for k in range(1, k_max+1):
        w[k] = -w[k-1] * (d - k + 1) / k
    return w

def ffd_apply(X, d, k_max=100):
    w = ffd_weights(d, k_max)
    out = np.full_like(X, np.nan)
    for t in range(k_max, len(X)):
        out[t] = np.dot(w, X[t-k_max:t+1][::-1])
    return out

# Find d* via grid search
for d in [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0]:
    series = ffd_apply(X, d)
    valid = series[~np.isnan(series)]
    if len(valid) > 50:
        p = adfuller(valid, autolag='AIC')[1]
        print(f"d={d}: ADF p-value = {p:.4f}")
```

## Anti-patterns

- **Using the full difference (`d = 1`)** when the goal is to predict returns. The FFD preserves more information.
- **Using the raw price (`d = 0`)** as a feature in an ML model. The price is non-stationary; the model will fit spurious relationships.
- **Setting `k*` too small.** The FFD weights decay slowly for small `d`; truncating too early loses information.
- **Treating `d*` as a free hyperparameter.** It should be calibrated to the asset's memory; the ADF test is the standard.

## Practitioner Notes

- **2026 update.** FFD is now a standard tool in the quant research workflow. The `mlfinlab` and `fractional_differentiation` Python packages implement the FFD.
- **Memory-aware models** (e.g. RNN, Transformer) can learn the FFD implicitly; the FFD is most useful for classical ML models (linear regression, gradient boosting).
- **The FFD threshold is regime-dependent.** The ADF test should be re-run periodically; `d*` may shift in response to structural breaks.

## Key Takeaways

1. **The FFD** is a memory-preserving differencing; the FFD threshold `d*` is asset-specific.
2. **The FFD weights** are computed via the binomial series; the fixed-width window truncates the long tail.
3. **The ADF test** is the standard for determining `d*`; the threshold is typically 0.2–0.5.
4. **The FFD preserves long memory** that the full difference destroys.
5. **The FFD is most useful for classical ML models**; memory-aware models can learn the FFD implicitly.

## Connects To

- **ch02** (Financial Data Structures): the FFD is applied to the bar data.
- **ch04** (Sample Weights): the FFD features can be weighted by sample uniqueness.
- **ch06** (Ensemble Methods): the FFD is often used as an input to ensemble models.
- **ch08** (Feature Importance): the FFD features can be ranked by MDI / MDA / SFI.
- **`tsay-analysis-financial-time-series` ch02 (Linear Time Series)**: the FFD is the alternative to the ARIMA differencing.
