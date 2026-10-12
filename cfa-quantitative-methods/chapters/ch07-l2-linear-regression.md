# Chapter 7: Introduction to Linear Regression
> **Source**: CFA Program Curriculum 2022, Level II, Reading 1 · Quantitative Methods | Authors: Pamela Peterson Drake, Richard A. DeFusco, Dwight Moore et al. (CFA Institute)

## Core Idea
Simple linear regression explains the variation of one dependent variable (Y) with one independent variable (X) by fitting the line that minimises squared residuals. Its value rests on four assumptions (linearity, homoskedasticity, independence, normality) that you check on the residual plots, and on a small toolkit (R², F, SEE, t-tests, prediction interval) that tells you whether the line is worth using.

## Learning Outcomes Covered
- describe the model, its parts (dependent/independent variable, intercept, slope, error) and interpret coefficients
- explain the OLS estimation criterion and compute slope/intercept
- state the four assumptions and read residual plots for violations
- decompose variation (SST = SSR + SSE); compute and interpret R², F-statistic, standard error of estimate (SEE) from an ANOVA table
- test hypotheses on slope, intercept and correlation (t-tests, p-values), including indicator variables
- compute a predicted value and a prediction interval
- choose among log-lin, lin-log, log-log functional forms

## Frameworks Introduced
- **Simple linear regression model**: `Yᵢ = b₀ + b₁Xᵢ + εᵢ`, i = 1..n (cross-section) or t = 1..T (time series).
  - When to use: one explanatory variable, a roughly linear relation, a need to quantify sensitivity (beta, elasticity, growth) or to forecast.
  - How: estimate b₀, b₁ by OLS, inspect residuals, test fit (F, R²), test coefficients (t), then forecast with an interval.
  - Failure mode: nonlinearity, regimes, autocorrelation or outliers invalidate standard errors even if R² looks good.
- **Four assumptions of the classic model (LHIN)**: Linearity (linear in the parameters), Homoskedasticity (constant residual variance), Independence (uncorrelated residuals, X non-stochastic), Normality (residuals normal; X and Y need not be).
  - When to use: always, as a checklist after estimation using residual plots (residuals vs X, vs time, histogram/normal plot).
  - How: patterns against X signal non-linearity; fan or regime-dependent spread signals heteroskedasticity; seasonal or serial pattern signals autocorrelation; fat tails or skew signal non-normality (matters mostly in small samples; the CLT rescues large n).
- **ANOVA decomposition**: SST = SSR + SSE (total = explained + unexplained variation).
  - How: R² = SSR/SST; F = MSR/MSE; SEE = √MSE. Together they judge fit.
- **Six-step hypothesis test** (state H₀/Hₐ, choose statistic, set α, decision rule, compute, decide) applied to slope, intercept, correlation.
- **Prediction interval**: `Ŷf ± t(α/2, n−2) · sf`, wider than a confidence interval for the mean because it includes residual noise.
- **Functional-form selection**: transform to straighten the relation, then choose by R², F, SEE (comparable only when Y is the same) and random residuals.

## Key Concepts
- **Dependent variable (Y, explained/predicted)**: the variable whose variation the model tries to explain.
- **Independent variable (X, explanatory/predictor)**: the variable used to explain Y.
- **Intercept (b₀)**: expected Y when X = 0; with a dummy X it is the mean of the group coded 0.
- **Slope (b₁)**: expected change in Y per one-unit change in X; with a dummy X it is the difference in group means.
- **Residual (eᵢ)**: Yᵢ − Ŷᵢ, the observed minus fitted value. Residuals sum to zero by construction; OLS minimises their sum of squares.
- **Ordinary least squares (OLS)**: estimation method choosing b₀, b₁ to minimise Σeᵢ².
- **SST / SSR / SSE**: total, regression (explained) and error (unexplained) sums of squares.
- **Coefficient of determination (R²)**: share of Y's variance explained; in simple regression R² = r² (square of correlation).
- **Standard error of the estimate (SEE, root MSE)**: absolute measure of fit, the typical distance of observations from the line, in Y's units.
- **F-statistic**: MSR/MSE; tests H₀: all slopes = 0; one-sided right tail.
- **Mean square regression / error (MSR, MSE)**: SSR/k and SSE/(n−k−1).
- **p-value**: smallest significance level at which H₀ is rejected (software default: H₀ coefficient = 0, two-sided).
- **Indicator (dummy) variable**: X taking only 0 or 1; regression on it reproduces a difference-in-means test.
- **Cross-sectional vs time-series regression**: many entities at one date (i = 1..n) versus one entity over many dates (t = 1..T).
- **Homoskedasticity / heteroskedasticity**: constant versus non-constant residual variance.
- **Log-lin, lin-log, log-log**: transformations for non-linear relations.

## Formulas & Reference Tables
Notation: n observations, k independent variables (k = 1 here), X̄, Ȳ sample means, Ŷᵢ fitted value.

- Slope: `b̂₁ = Cov(X,Y)/Var(X) = Σ(Xᵢ−X̄)(Yᵢ−Ȳ) / Σ(Xᵢ−X̄)²`
- Intercept: `b̂₀ = Ȳ − b̂₁X̄` (the line passes through (X̄, Ȳ))
- Fitted value: `Ŷᵢ = b̂₀ + b̂₁Xᵢ`; residual `eᵢ = Yᵢ − Ŷᵢ`
- Variation: `SST = Σ(Yᵢ−Ȳ)²`, `SSR = Σ(Ŷᵢ−Ȳ)²`, `SSE = Σ(Yᵢ−Ŷᵢ)²`, `SST = SSR + SSE`
- `R² = SSR/SST = 1 − SSE/SST = r²`
- `MSR = SSR/k` (=SSR when k=1); `MSE = SSE/(n−k−1)` (n−2 here)
- `F = MSR/MSE`, df = (1, n−2); and `F = t²` for the slope in simple regression
- `SEE = √MSE = √[SSE/(n−2)]`
- Sample variance of Y = SST/(n−1)
- Slope SE: `s_b₁ = SEE / √Σ(Xᵢ−X̄)²`; t-test `t = (b̂₁ − B₁)/s_b₁`, df = n−2
- Intercept SE: `s_b₀ = SEE · √[1/n + X̄²/Σ(Xᵢ−X̄)²]`; `t = (b̂₀ − B₀)/s_b₀`
- Correlation test: `t = r√(n−2)/√(1−r²)`, df = n−2; equals the slope t-stat
- Forecast: `Ŷf = b̂₀ + b̂₁Xf`
- SE of forecast: `s_f = SEE · √[1 + 1/n + (Xf−X̄)²/Σ(Xᵢ−X̄)²]`; note Σ(Xᵢ−X̄)² = (n−1)s²_X
- Prediction interval: `Ŷf ± t_crit(α/2, n−2) · s_f`

| ANOVA source | SS | df | MS | F |
|---|---|---|---|---|
| Regression | SSR | k (=1) | SSR/k | MSR/MSE |
| Error | SSE | n−k−1 (=n−2) | SSE/(n−k−1) | |
| Total | SST | n−1 | | |

| Functional form | Equation | Slope means | Typical use |
|---|---|---|---|
| Lin-lin | Y = b₀ + b₁X | ΔY per ΔX (absolute/absolute) | baseline |
| Log-lin | ln Y = b₀ + b₁X | % change in Y per unit ΔX (growth rate per period) | exponential growth (revenues vs time) |
| Lin-log | Y = b₀ + b₁ ln X | ΔY per % change in X | diminishing returns (margin vs unit sales) |
| Log-log | ln Y = b₀ + b₁ ln X | % change in Y per % change in X (elasticity) | elasticities (revenue vs advertising) |

| Assumption | Violation | Residual-plot tell |
|---|---|---|
| Linearity | curved true relation | residuals vs X form a U or arch |
| Homoskedasticity | different volatility regimes or fanning | spread differs across X or time |
| Independence | autocorrelation, seasonality | residual pattern over time (e.g. Q4 jumps) |
| Normality | skew, fat tails, outliers | non-bell histogram, bent normal plot |

## Mental Models
- **Fit is not significance, and neither is truth**: R² is descriptive, F tests that the slope is non-zero, SEE is the absolute scale of error. Use all three plus residual plots.
- **Prediction is hardest at the edges**: the forecast error is minimal at X̄ and widens as Xf moves away; extrapolating far outside the sample is a different, riskier exercise.
- **Slope = covariance / variance of X**: more spread in X shrinks the slope's standard error and raises t. To measure a slope precisely, vary X.
- **A dummy regression is a t-test in disguise**: intercept = mean of the base group, slope = difference in means, t identical to the pooled two-sample test.
- **Transform before you complicate**: when residuals curve, try ln on X, Y or both before adding machinery. Compare candidates by SEE if Y is unchanged.
- **Outliers decide the line**: one wild month can fabricate R² = 99%; look at the data before trusting the statistics.

## Worked Example
ROA (Y, %) regressed on CAPEX (X, %) for six companies: X = 0.7, 0.4, 5, 10, 8, 12.5; Y = 6, 4, 15, 20, 10, 20 (recomputed).
1. X̄ = 6.1, Ȳ = 12.5, Σ(X−X̄)² = 122.64, Σ(X−X̄)(Y−Ȳ) = 153.3. Slope = 153.3/122.64 = **1.25**; intercept = 12.5 − 1.25×6.1 = **4.875**.
2. SST = 239.50, SSR = 191.625, SSE = 47.875. R² = 0.8001; the correlation is +0.8945.
3. MSE = 47.875/4 = 11.96875; SEE = 3.4596; F = 191.625/11.96875 = **16.01** vs F-crit(1,4; 5%) = 7.71, so the slope differs from zero.
4. s_b₁ = 3.4596/√122.64 = 0.3124; t = 1.25/0.3124 = **4.001**, and t² = F = 16.01. Critical ±2.776 (df = 4), so reject H₀: b₁ = 0 (two-sided p ≈ 0.016; **⚠ Correction**: the curriculum's quoted p = 0.008 is the one-tail value, since its own formula multiplies by 2). Testing H₀: b₁ = 1 gives t = 0.80, so a one-to-one relation cannot be rejected.
5. Forecast CAPEX = 6: Ŷf = 4.875 + 1.25×6 = 12.375. s_f = 3.4596×√(1 + 1/6 + 0.01/122.64) = 3.737; 95% PI = 12.375 ± 2.776×3.737 = **[2.00, 22.75]**.
Interpretation: a strong, significant fit, yet the interval is wide because n = 6; the narrow R² story hides forecast uncertainty.

Second check (R&D example): NPM = 16.5 − 1.3·RDR, n = 8, SEE = 1.862, Σ(X−X̄)² = 30, X̄ = 7.5. At RDR = 5, s_f = 2.150 and the PI is 10 ± 5.26; at RDR = 15 (far from X̄) s_f = 3.225, PI = −3 ± 7.89, wider and with a negative margin, a sign of extrapolation.

## Anti-patterns
- **Reading R² as proof of causality or as the F-test**: R² measures association; significance requires the F or t test, and causation requires theory/design.
- **Comparing R²/F across models with different dependent variables**: ln Y vs Y fits are not comparable without back-transforming; compare residual plots instead.
- **Forecasting a log-lin model without exponentiating**: the prediction of ln Y must be converted back with eˣ.
- **Requiring X or Y to be normal**: only the residuals need normality; but do inspect X and Y for outliers.
- **Using a single line across regimes**: pooling normal-rate and low-rate years produced a slope of 1.20 where the regimes had 1.02 and −0.28.
- **Using a confidence interval instead of a prediction interval for an individual forecast**: the former omits the residual noise (the "1" inside the root).
- **Ignoring autocorrelated residuals in time-series regressions**: standard errors and t-stats are then unreliable.

## Exam Focus & Traps
- Degrees of freedom: simple regression is n−2 for t, (1, n−2) for F; SST has n−1.
- F is one-sided right-tailed; t for the slope can be two- or one-sided; critical t one-sided 5% at df 4 = 2.132, two-sided = 2.776.
- In simple regression F = t² and r² = R²; sign of r follows the sign of the slope.
- SEE is √MSE, not MSE; the sample std dev of Y is √[SST/(n−1)].
- Lin-log slope: change in Y for a *relative* change in X; log-lin: relative change in Y for an *absolute* change in X; log-log slope = elasticity.
- Dummy-variable intercept = base-category mean; slope = difference in means (a test of the slope is a test of equal means).
- s_f is always larger than SEE; it is smallest at Xf = X̄; prediction intervals use s_f, not s_b.
- Questions where outliers (a month of 72% return) inflate R² to 0.99: correcting the data cuts R² to 0.68 and the slope from 1.07 to 0.62.
- p-value: small p means reject H₀; p is the smallest significance level for rejection.

## Key Takeaways
1. Always plot X vs Y and residuals; the four assumptions are verified visually first, statistically second.
2. R² = SSR/SST, F = MSR/MSE, SEE = √MSE: use all three; SEE is the only absolute measure.
3. Test slope with t = (b̂ − B)/s_b, df = n−2; for simple regression this is equivalent to F and to the correlation test.
4. Forecast with Ŷf = b₀ + b₁Xf and a prediction interval whose width grows with distance from X̄ and shrinks with n and fit.
5. A dummy X turns the regression into a group-mean comparison.
6. If the relation curves, transform (log-lin for growth, lin-log for diminishing returns, log-log for elasticities) and re-check residuals.
7. Detect regimes and outliers before trusting the fit; they can invert the story.
8. Heteroskedasticity or autocorrelation do not bias the slope but invalidate its standard errors (see ch 8).

## Connects To
- **ch 08**: extends this to several regressors, adjusted R², F-test of joint significance, and detailed violation diagnostics.
- **ch 09**: time-series regressions with autocorrelation, unit roots and trends (log-lin trend models).
- **ch 06**: hypothesis testing mechanics (Type I/II errors, p-values) reused here.
- **ch 02**: covariance, correlation and scatter plots underlie the OLS slope.
- **`cfa-portfolio-management` ch 12**: factor models and market-model betas are regressions.
- **`cfa-equity-valuation` ch 09**: regression-based valuation of multiples against growth.
