# Cheatsheet — CFA Quantitative Methods (L1 · L2)

## Decision rules
| When | Do | Because |
|---|---|---|
| Comparing cash flows at different dates | Move all to one date on a time line | Money has a date stamp (ch01) |
| Annuity or perpetuity starts at t = k | Value sits at t = k−1; discount it back | Formula lands one period before first payment (ch01) |
| Stated rate with sub-annual compounding | Use periodic rate or EAR | `1 + rₛ` is not a growth factor (ch01) |
| Past multi-period return | Geometric mean of (1+R) | Arithmetic overstates compounding (ch02) |
| Forecast of next single period | Arithmetic mean | Expected one-period outcome (ch02) |
| Outliers or skew (P/E) | Median | Mean follows outliers (ch02) |
| Distribution shape unknown | Chebyshev `1 − 1/k²` | Normal 68/95/99 only if normal (ch02) |
| P(A or B) | Add, subtract overlap | Overlap double counts (ch03) |
| Revising probability on news | Bayes with total probability | Posteriors reverse the arrow (ch03) |
| Count of binary successes | Binomial | Needs independence, constant p (ch04) |
| Returns vs prices | Normal for returns, lognormal for prices | Prices cannot go below 0 (ch04) |
| Floor-driven client | Max `[E(R)−R_L]/σ` | Minimizes shortfall probability under normality (ch04) |
| Mean CI, σ unknown | t with n−1 df | Estimated σ adds tail risk; z only if σ known or n large (ch05) |
| Pooling more years of data | Check one population first | Mixed regimes give wrong answers (ch05) |
| Backtest looks great | Audit data mining, survivorship, look-ahead, period | Bias, not skill (ch05) |
| Claim to support | Put it in Hₐ; test at equality | H₀ gets benefit of the doubt (ch06) |
| Related samples (before/after, two funds, same months) | Paired t on differences | Correlation shrinks s_d (ch06) |
| Large n, tiny effect "significant" | Check economic size and costs | SE shrinks with n (ch06) |
| Regression done | F, then t's, then diagnostics | Joint before individual (ch07, 08) |
| Time-series or financial regression | Newey-West/robust SE | Autocorrelation and heteroskedasticity inflate t (ch08) |
| Trending or random-walk series | Dickey-Fuller; difference if H₀ not rejected | R² on levels is spurious (ch09) |
| AR residual test | Residual autocorrelations (SE 1/√T), not DW | Lagged Y invalidates DW (ch09) |
| Choosing between ML models | Out-of-sample error, simplest adequate | In-sample fit rewards overfitting (ch10) |
| Imbalanced classes | Precision/recall/F1, rebalance training | Accuracy rewards the majority class (ch11) |

## Which test when (statistic, distribution, df)
| Hypothesis | Statistic | Distribution, df |
|---|---|---|
| One mean, σ known | `(X̄−μ₀)/(σ/√n)` | z |
| One mean, σ unknown | `(X̄−μ₀)/(s/√n)` | t, n−1 (z alt. if n ≥ 30) |
| Two means, independent, equal variances | pooled `s_p²`, `Δ/√(s_p²/n₁ + s_p²/n₂)` | t, n₁+n₂−2 |
| Two means, independent, unequal variances | `Δ/√(s₁²/n₁ + s₂²/n₂)` | t, modified df |
| Paired differences | `(d̄−μ_d0)/(s_d/√n)` | t, n−1 |
| One variance | `(n−1)s²/σ₀²` | χ², n−1 |
| Two variances | `s₁²/s₂²` (larger on top) | F, (n₁−1, n₂−1) |
| Correlation = 0 | `r√(n−2)/√(1−r²)` | t, n−2 |
| Slope or intercept | `(b̂−B)/s_b` | t, n−k−1 |
| All slopes zero | `MSR/MSE` | F, (k, n−k−1) |
| Unit root | `ĝ/SE(ĝ)` vs special values | Dickey-Fuller |

## Decision tree: which test
1. Parameter: mean, variance or correlation? 2. Mean: σ known (z) or not (t)? 3. One sample, independent samples, or paired? 4. Equal variances plausible (pooled) or not (unpooled)? 5. Assumptions fail or data are ranks: nonparametric (Wilcoxon, Mann-Whitney, sign, Spearman).

## Trade-off matrix
| Choice | Gain | Give up |
|---|---|---|
| Lower α | Fewer false positives | Power; β rises (ch06) |
| Larger sample | Narrower CI, more power | Risk of mixing populations, cost (ch05) |
| t instead of z | Correct for unknown σ | Slightly wider (ch05) |
| Parametric vs nonparametric | Sharper conclusions | Needs assumptions (ch06) |
| Robust SE | Valid inference | Efficiency only (ch08) |
| More regressors | Higher R² | Adjusted R², collinearity, overfit (ch08) |
| Complex ML model | Fits non-linearity | Interpretability, variance (ch10) |
| Higher p-threshold | Precision | Recall (ch11) |

## Thresholds and defaults
| Item | Value |
|---|---|
| z two-tail 90/95/99% | 1.645 / 1.96 / 2.576 (reading rounds 1.65, 1.96, 2.58) |
| z one-tail 10/5/1% | 1.28 / 1.645 / 2.33 |
| "Large" sample | n ≥ 30 |
| Significance levels | 0.10 some, 0.05 strong, 0.01 very strong evidence |
| Normality screen (n ≥ 100) | |skew| > 0.5 or excess kurtosis > 1; JB ≥ 6 rejects |
| Annualize daily vol | × √250 (curriculum) |
| Variance inflation factor | > 5 investigate, > 10 serious |
| Durbin-Watson | 2 = none; 0 = r +1; 4 = r −1 |
| Sample autocorrelation SE | 1/√T |
| k-fold k / data split | 5 or 10 / 60-20-20 |
| IQR outlier fences | Q1 − 1.5·IQR, Q3 + 1.5·IQR (3.0 extreme) |
| PCA components kept | ≈ 85–95% of variance |
| AUC | 0.5 random, 1.0 perfect |

## Tells & smells
- Significant F but insignificant t's: multicollinearity.
- High R² on trending series, DW far below 2: spurious regression or autocorrelation.
- "Noticed that..." or no economic story behind a pattern: data mining.
- Fund database lists only current funds: survivorship.
- Big train–CV gap: overfit; both errors high: underfit.
- 99% accuracy on rare-event data: majority-class model.
- Mean P/E far above median: outlier distortion.

## Exam traps
| Trap | Correct |
|---|---|
| Annuity due vs ordinary | Due = ordinary × (1+r); "starts today" means due |
| Mean ordering | harmonic ≤ geometric ≤ arithmetic |
| Sample variance divisor | n−1 (population N) |
| P(A or B) | P(A) + P(B) − P(AB) |
| "x or more" binomial | 1 − F(x−1) |
| z.05 value | 1.645 one-tail 5% and two-tail 10% |
| Standard error | σ/√n or s/√n (not σ/n) |
| CI at df n−1 | t for unknown σ; wider than z |
| Estimator properties | s² with divisor n is biased |
| Failing to reject | Not "accept" H₀ |
| Type I / power | α / 1−β; lowering α raises β |
| Paired df | Pairs − 1, not total observations |
| F-statistic | Larger variance on top; two-tail uses α/2 |
| Correlation test df | n−2 |
| p-value | Reject if p < α |
| Simple regression | F = t², R² = r², df n−2 |
| Multiple regression df | t: n−k−1; F: (k, n−k−1); adjusted R² < R² |
| Log-log slope | Elasticity (% per %) |
| Heteroskedasticity | Only conditional matters; coefficients fine, SE wrong |
| Multicollinearity fix | Drop/combine variables, not robust SE |
| Log-linear trend growth | e^b₁ − 1, not b₁ |
| Mean-reverting level | b₀/(1−b₁); random walk undefined |
| Unit-root test | H₀ nonstationary; fail to reject means difference |
| Precision vs recall | FP in precision's denominator; FN in recall's |
| ⚠ Source corrections | Spearman example ranks (ch06), Welch df uses n−1 in standard form (ch06), ch09 seasonal forecast 0.0243 |
