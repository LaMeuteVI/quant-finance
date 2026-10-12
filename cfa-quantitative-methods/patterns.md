# Patterns — CFA Quantitative Methods Recipes

## Time-Line TVM Routine
**When to use**: any multi-date cash-flow problem (deferred annuities, retirement funding, loans).
**How**: 1. Draw the line with t = 0 today. 2. Mark each flow and its structure (lump sum, ordinary/due annuity, perpetuity). 3. Match the rate and N to one time unit. 4. Annuity or perpetuity formulas land one period before the first payment, so shift with a lump-sum factor. 5. Add flows only at the same date; solve for the unknown (A, r, N, g).
**Trade-offs**: exact but error-prone on timing; answer is independent of the chosen reference date. (ch 01)

## Quote-to-EAR Conversion
**When to use**: comparing offers with different compounding, or building periodic rates.
**How**: 1. Periodic rate = rₛ/m. 2. `EAR = (1 + rₛ/m)^m − 1` (or `e^rₛ − 1` continuous). 3. For another frequency: `(1 + EAR)^(1/m') − 1`. 4. Compare on EAR.
**Trade-offs**: more frequent compounding raises EAR toward the continuous ceiling. (ch 01)

## Choose the Average and the Dispersion Measure
**When to use**: summarizing returns or multiples.
**How**: 1. Past compound performance: geometric mean of `1+R`. 2. One-period forecast: arithmetic mean. 3. Skewed or outlier data (P/E): median. 4. Equal money invested at varying prices: harmonic. 5. Risk: sample SD (n−1); compare series with different means via CV; downside focus via semideviation; unknown shape: Chebyshev `1 − 1/k²`.
**Trade-offs**: semivariance has no portfolio algebra; CV breaks near a zero mean. (ch 02)

## Skew/Kurtosis Normality Screen
**When to use**: deciding whether normal-based tools (VaR, z-intervals) are safe.
**How**: 1. Compute sample skewness and excess kurtosis. 2. Large n: |SK| > 0.5 or K_E > 1 is unusual. 3. `JB = n[SK²/6 + K_E²/24]`; JB ≥ 6 rejects normality near 5%. 4. If rejected, use Chebyshev, historical simulation or a fat-tailed model.
**Trade-offs**: sample SK/K_E are noisy (SD ≈ √(6/n), √(24/n)); monthly returns fail more than annual. (ch 02, 04)

## Scenario Tree with Total Probability
**When to use**: forecasting EPS or return across regimes; default-premium pricing.
**How**: 1. List mutually exclusive, exhaustive scenarios with probabilities summing to 1. 2. Estimate `E(X|S)` in each. 3. `E(X) = ΣE(X|S)P(S)`. 4. Variance = expected conditional variance + variance of conditional means.
**Trade-offs**: probabilities are subjective; overlapping or missing scenarios break the rule. (ch 03)

## Bayesian Update
**When to use**: revising a probability after new information (earnings beat, test result).
**How**: 1. Priors for each event. 2. Likelihoods `P(Info|Event)`. 3. `P(Info) = ΣP(Info|E)P(E)`. 4. Posterior = likelihood × prior / P(Info). 5. Posteriors must sum to 1.
**Trade-offs**: garbage priors give garbage posteriors; never swap P(I|E) with P(E|I). (ch 03)

## Portfolio Mean and Variance from a Covariance Matrix
**When to use**: n-asset expected return and risk.
**How**: 1. `E(Rp) = Σ wᵢE(Rᵢ)`. 2. `σ²p = ΣΣ wᵢwⱼCov(Rᵢ,Rⱼ)`; for two assets `w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂`. 3. `Cov = ρσᵢσⱼ`; keep % vs decimals consistent.
**Trade-offs**: needs n(n−1)/2 covariances; inputs are unstable. (ch 03)

## Roy's Safety-First Screen
**When to use**: a client with a hard return floor.
**How**: 1. `R_L` = floor in return terms. 2. Compute `SFRatio = [E(R)−R_L]/σ` per candidate. 3. Pick the highest; `P(shortfall) = N(−SFRatio)`. 4. If a riskless asset yields ≥ R_L, hold it.
**Trade-offs**: assumes normal returns; ranking can flip on small input changes. (ch 04)

## Confidence Interval Construction
**When to use**: estimating a mean with a stated confidence.
**How**: 1. Standard error `s/√n` (or σ/√n if known). 2. Reliability factor: z if σ known; t with n−1 df if σ unknown (z acceptable for large n). 3. `X̄ ± factor × SE`. 4. Required n: `(t·s/E)²`.
**Trade-offs**: higher confidence widens the interval; larger n narrows by √n but risks mixing populations. (ch 05)

## Bias Audit of a Backtest
**When to use**: judging any published anomaly or strategy.
**How**: 1. Data mining: how many variables were tried, is there an economic story, is there an out-of-sample test. 2. Survivorship: are failed firms/funds in the database. 3. Look-ahead: was each input public on the signal date. 4. Time period: how many cycles, any structural break. 5. Mixed populations: regimes pooled.
**Trade-offs**: out-of-sample tests are costly and the strategy may be arbitraged once known. (ch 05)

## Seven-Step Hypothesis Test
**When to use**: any formal test.
**How**: 1. H₀ (with =, ≤ or ≥) and Hₐ (the claim). 2. Statistic and distribution (see cheatsheet table). 3. α before looking. 4. Rejection points (α/2 per tail if two-sided). 5. Compute. 6. Reject if beyond a rejection point or p < α. 7. Judge economic significance.
**Trade-offs**: lowering α raises β; only more data lowers both. (ch 06)

## Independent vs Paired Mean Test
**When to use**: comparing two means.
**How**: 1. Independent samples: if variances look similar, pooled t (df n₁+n₂−2); otherwise unpooled t with modified df. 2. Dependent samples (same units, common risk factors): compute differences, one-sample t on d̄ with df n−1. 3. Non-normal small samples: Mann-Whitney or Wilcoxon.
**Trade-offs**: pooling assumes equal variances; pairing needs a real link between observations. (ch 06)

## Variance and Correlation Tests
**When to use**: testing risk levels, changes in volatility, or linear association.
**How**: 1. One variance: `χ² = (n−1)s²/σ₀²`, df n−1. 2. Two variances: F = larger/smaller variance, df (n₁−1, n₂−1), α/2 upper tail for two-sided. 3. Correlation: `t = r√(n−2)/√(1−r²)`, df n−2. 4. Heavy tails or ranks: Spearman.
**Trade-offs**: chi-square and F are not robust to non-normality. (ch 06)

## Regression Vetting Sequence
**When to use**: after estimating any OLS regression.
**How**: 1. Plot data and residuals (LHIN assumptions). 2. F-test the whole model. 3. t-test each slope (df n−k−1). 4. Compare R̄², SEE (and AIC/BIC). 5. Test heteroskedasticity (Breusch-Pagan) and serial correlation (Durbin-Watson). 6. Use robust or Newey-West SE. 7. Check multicollinearity and specification.
**Trade-offs**: robust SE fix inference, not biased coefficients from misspecification. (ch 07, 08)

## Prediction Interval for a Regression Forecast
**When to use**: forecasting an individual Y.
**How**: 1. `Ŷf = b̂₀ + b̂₁Xf`. 2. `s_f = SEE·√[1 + 1/n + (Xf−X̄)²/Σ(X−X̄)²]`. 3. `Ŷf ± t(α/2, n−2)·s_f`.
**Trade-offs**: width grows away from X̄; extrapolation beyond the sample is unreliable. (ch 07)

## Time-Series Forecast Pipeline
**When to use**: forecasting a financial or macro series.
**How**: 1. Plot (trend, seasonality, breaks). 2. Linear trend (constant change) or log-linear (constant growth). 3. If residuals autocorrelated or series trends, run Dickey-Fuller and difference if H₀ not rejected. 4. Fit AR(1); test residual autocorrelations (SE 1/√T); add lags, then a seasonal lag. 5. Test ARCH. 6. Compare out-of-sample RMSE; check coefficient stability.
**Trade-offs**: longer samples mix regimes; ARMA adds instability. (ch 09)

## Cointegration Check Before Regressing Two Series
**When to use**: regressing one time series on another.
**How**: 1. Dickey-Fuller on each. 2. Both stationary: regress freely. 3. One has a unit root: do not regress. 4. Both have unit roots: Engle-Granger (regress, test residuals); cointegrated means a valid long-run relation only.
**Trade-offs**: Engle-Granger critical values differ from plain Dickey-Fuller. (ch 09)

## ML Algorithm Selection and Validation
**When to use**: starting a prediction or clustering problem.
**How**: 1. Many correlated features: PCA. 2. Continuous target: linear then LASSO; non-linear then CART, random forest, neural nets. 3. Categorical target: KNN/SVM (simple), CART/forest/nets (non-linear). 4. No labels: k-means (k known) or hierarchical (unknown); 5. Split train/validation/test (60/20/20); tune on validation; use walk-forward for time series.
**Trade-offs**: flexible models gain accuracy but lose interpretability and overfit. (ch 10)

## Text-to-DTM Pipeline
**When to use**: turning financial text into model inputs.
**How**: 1. Cleanse (html, punctuation with annotations, numbers, white space). 2. Tokenize, lowercase, remove stop words, stem or lemmatize. 3. Build BOW from the training set only; add n-grams if order matters. 4. Fill the DTM with counts or TF-IDF. 5. Prune very frequent and very rare tokens; chi-square or mutual-information selection. 6. Train, evaluate on held-out data.
**Trade-offs**: stop-word removal can delete sentiment words; vocabulary built on the full corpus leaks. (ch 11)

## Classifier Evaluation and Threshold Tuning
**When to use**: choosing the cutoff or model for a classifier.
**How**: 1. Build the confusion matrix on validation data. 2. Costly false positives: maximize precision; costly false negatives: maximize recall; balance: F1 (not accuracy when imbalanced). 3. Vary the p-threshold; pick the best on validation. 4. Compare models by AUC. 5. Compare train and CV error: gap means overfit; both high means underfit.
**Trade-offs**: raising the threshold lifts precision and cuts recall. (ch 10, 11)
