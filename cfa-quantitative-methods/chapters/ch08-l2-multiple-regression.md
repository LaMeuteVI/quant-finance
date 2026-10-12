# Chapter 8: Multiple Regression
> **Source**: CFA Program Curriculum 2022, Level II, Reading 2 · Quantitative Methods | Richard A. DeFusco, Dennis W. McLeavey, Jerald E. Pinto, David E. Runkle (contributions from Sanjiv Sabherwal). Items marked **[Ext.]** are standard econometrics added for completeness (not in the 2022 text); verified independently.

## Core Idea
Multiple regression explains Y with several X's, each coefficient being a partial effect holding the others constant. The skill is not running it but vetting it: overall F-test before individual t-tests, adjusted R² rather than R², and a systematic check of the violations (heteroskedasticity, serial correlation, multicollinearity, misspecification) that make the standard errors, and hence every t-stat and p-value, wrong while the coefficients stay (mostly) fine.

## Learning Outcomes Covered
- formulate a multiple regression, interpret partial coefficients and p-values, test coefficients (t) and predict Y
- state the six assumptions of the classical normal multiple regression model
- compute and interpret the F-statistic (overall significance), R² vs adjusted R², read an ANOVA table
- build models with dummy variables (intercept and slope/interaction dummies)
- explain conditional vs unconditional heteroskedasticity, test (Breusch–Pagan), correct (robust SE)
- explain serial correlation, test (Durbin–Watson), correct (Newey–West / Hansen)
- describe multicollinearity: symptoms, consequences, remedies
- identify model misspecification (omitted variables, scaling, pooling, time-series errors) and good-model principles
- interpret a logistic regression (log odds, odds ratio, probability, pseudo-R², likelihood-ratio test)

## Frameworks Introduced
- **Multiple linear regression model**: `Yᵢ = b₀ + b₁X₁ᵢ + … + bₖXₖᵢ + εᵢ` (k slopes, k+1 coefficients).
  - When to use: several drivers of one outcome (factor/style regressions, determinants of spreads, valuation drivers).
  - How: estimate by OLS, F-test the model, t-test each slope (df = n−k−1), then diagnose residuals before interpreting anything.
  - Failure mode: partial slopes change when regressors are added; reading a slope as "the" effect ignores what is held constant.
- **Classical normal multiple regression assumptions (6)**: (1) linear in parameters; (2) X's non-random and *no exact linear relation among them*; (3) `E(ε | X₁..Xₖ) = 0`; (4) constant error variance (homoskedasticity); (5) uncorrelated errors; (6) normal errors.
  - Which breaks what: (2) exact → cannot estimate (perfect collinearity); near → multicollinearity; (3) → bias/inconsistency; (4) → wrong SEs; (5) → wrong SEs (inconsistent coefficients if lagged Y is a regressor); (6) matters little in large samples.
- **Test-the-whole-model-first rule**: run the F-test on H₀: b₁ = … = bₖ = 0 before interpreting individual t-stats. Joint and individual tests can disagree (multicollinearity).
- **Dummy-variable framework**: n categories need n−1 dummies; the omitted one is the base/control group. Intercept dummy shifts the intercept; slope (interaction) dummy `D×X` shifts the slope; both together allow a fully different line.
- **Breusch–Pagan test** for conditional heteroskedasticity: regress squared residuals on the X's; `n·R²` ~ χ²(k), one-tailed.
- **Durbin–Watson test** for first-order serial correlation: DW ≈ 2(1−r).
- **Violation → consequence → detection → correction map** (see table below), with **robust (White / heteroskedasticity-consistent) SE** and **Newey–West (HAC) SE** as default fixes.
- **Model specification principles (5)**: economic reasoning (not data mining); appropriate functional form; parsimony; check assumptions; validate out of sample.
- **Logistic regression (logit)**: models `ln[p/(1−p)]` linearly; estimated by maximum likelihood; evaluated by likelihood-ratio χ² and pseudo-R².

## Key Concepts
- **Partial regression coefficient (partial slope)**: expected change in Y per unit change in Xⱼ, holding the other regressors constant (net of their correlated part).
- **ANOVA table (multiple)**: RSS (explained, df k), SSE (unexplained, df n−k−1), total SS (df n−1).
- **F-statistic**: MSR/MSE with (k, n−k−1) df; one-tailed; tests that all slopes are jointly zero.
- **R²**: RSS/SST; never decreases when a regressor is added (even a junk one).
- **Adjusted R² (R̄²)**: R² penalised for degrees of freedom; can fall when a variable is added, can be negative (treat as 0), always < R² when k ≥ 1.
- **Standard error of estimate (SEE)**: √MSE, residual standard error.
- **Intercept / slope dummy**: shift in level / shift in slope between a category and the base group.
- **Conditional heteroskedasticity**: error variance correlated with the regressors; the serious kind. Unconditional heteroskedasticity (uncorrelated with X) causes no major inference problem.
- **Robust (White-corrected) standard errors**: SEs consistent under conditional heteroskedasticity; coefficients unchanged.
- **Serial correlation (autocorrelation)**: errors correlated across time; positive means same-sign persistence.
- **Newey–West / Hansen standard errors**: correct for serial correlation and heteroskedasticity together.
- **Multicollinearity**: regressors (or combinations) highly but not perfectly correlated; inflates SEs, lowers t-stats.
- **Omitted variable bias**: leaving out a relevant regressor correlated with the included ones biases and makes inconsistent the remaining coefficients.
- **Consistency**: estimates converge to the truth as n grows; heteroskedasticity, serial correlation and multicollinearity leave consistency intact, misspecification does not.
- **Odds / log odds (logit)**: odds = p/(1−p); log odds = ln(odds); the logit slope is the change in log odds per unit X, `e^b` is the odds ratio.
- **Pseudo-R²**: fit measure for MLE models, comparable only across specifications of the same data.
- **Nonstationarity**: trending or random-walk series that make time-series regressions spurious (see ch 09).

## Formulas & Reference Tables
Notation: n observations, k slopes, RSS regression SS, SSE residual SS, SST total SS.
- Prediction: `Ŷ = b̂₀ + b̂₁X₁ + … + b̂ₖXₖ` (prediction intervals need matrix algebra, outside scope)
- t-test of a slope: `t = (b̂ⱼ − bⱼ)/s_b̂ⱼ`, df = n−(k+1); software t = b̂/s tests H₀: b = 0
- `F = (RSS/k) / [SSE/(n−k−1)] = MSR/MSE`, df (k, n−k−1); reject if F > upper-α critical value
- `R² = RSS/SST = 1 − SSE/SST`
- `R̄² = 1 − [(n−1)/(n−k−1)]·(1 − R²)`
- `SEE = √MSE`
- Dummies: intercept `Y = b₀ + d₀D + b₁X`; slope `Y = b₀ + b₁X + d₁(D×X)`; both `Y = b₀ + d₀D + b₁X + d₁(D×X)`; D=1 line is `(b₀+d₀) + (b₁+d₁)X`
- Breusch–Pagan: `BP = n·R²` (R² taken from the regression of squared residuals on the X's) ~ χ²(k); reject H₀ (homoskedastic) if BP > critical
- Durbin–Watson: `DW = Σₜ₌₂ᵀ(ε̂ₜ − ε̂ₜ₋₁)² / Σₜ₌₁ᵀ ε̂ₜ²  ≈ 2(1 − r)`, r = first-order residual autocorrelation; so `r ≈ 1 − DW/2`
- Logit: `ln[p/(1−p)] = b₀ + Σbⱼ Xⱼ`; `p = 1/(1 + exp[−(b₀ + Σbⱼ Xⱼ)])`; `odds = p/(1−p)`; `odds ratio = e^b`
- **[Ext.]** `AIC = n·ln(SSE/n) + 2(k+1)`; `BIC (SBC) = n·ln(SSE/n) + ln(n)·(k+1)`; lower is better; AIC for forecasting, BIC (heavier penalty) for parsimony; compare on the same dependent variable and sample
- **[Ext.]** `VIFⱼ = 1/(1 − R²ⱼ)`, R²ⱼ from regressing Xⱼ on the other X's; VIF > 5 investigate, > 10 serious
- **[Ext.]** Leverage hᵢᵢ (diagonal of the hat matrix); flag `hᵢᵢ > 3(k+1)/n`. Cook's distance `Dᵢ = [eᵢ²/((k+1)·MSE)]·[hᵢᵢ/(1−hᵢᵢ)²]`; flag Dᵢ > 0.5 (investigate), > 1 (likely influential). Studentized deleted residual compared with t (df n−k−2) flags outliers in Y.
- **[Ext.]** Breusch–Godfrey (serial correlation of any order p, valid with lagged Y): regress residuals on X's and p lagged residuals; `(n−p)·R²` ~ χ²(p)

**Violations table**

| Violation | Effect on estimates and inference | How to detect | Correction |
|---|---|---|---|
| Conditional heteroskedasticity | Coefficients still consistent; SE biased (usually too small), t and F inflated, false positives | residual vs X plots; Breusch–Pagan (n·R² ~ χ²_k) | robust (White) SE; or GLS |
| Serial correlation (positive) | Coefficients consistent unless lagged Y is a regressor; SE too small, t and F inflated | Durbin–Watson (DW < d_l reject); [Ext.] Breusch–Godfrey | Newey–West/Hansen SE (also fixes heteroskedasticity); avoid re-specifying carelessly |
| Serial correlation + lagged Y regressor | Coefficients biased and inconsistent | same tests | redesign model (ch 09 AR models) |
| Multicollinearity | Coefficients consistent but imprecise; huge SEs, low t, high R² and significant F | high R² + insignificant t's; VIF [Ext.] (pairwise correlation is only sufficient with 2 regressors) | drop/combine variables; no formal cure |
| Omitted variable correlated with X | Biased, inconsistent coefficients and SEs | theory, change in coefficient when variable added | include the variable |
| Wrong functional form / scaling | Biased, inconsistent | residual plots, theory | log or other transform, scale (e.g. by sales) |
| Pooling different regimes | Spurious correlation | plot clusters | separate regressions or dummies |
| Regressor correlated with error (lagged Y with autocorrelation, measurement error, "forecasting the past") | Biased and inconsistent | reasoning about timing | use information known at time t, proper proxies |
| Nonstationarity | Spurious regression | unit-root tests (ch 09) | difference / cointegration |

**Durbin–Watson decision (positive serial correlation test, one-sided)**: DW < d_l reject H₀ (no serial correlation); d_l ≤ DW ≤ d_u inconclusive; DW > d_u fail to reject. Two-sided: also reject if DW > 4 − d_l. DW = 2 ↔ r = 0; DW = 0 ↔ r = +1; DW = 4 ↔ r = −1.

## Mental Models
- **F before t**: a significant F with insignificant t's is the fingerprint of multicollinearity; an insignificant F kills the model whatever the t's say.
- **Adjusted R² is a cost-benefit test**: a new variable helps only if it raises R̄², roughly if its |t| > 1; use t > ~2 for significance.
- **Robust SEs are free insurance**: they change t-stats, not coefficients; with financial data use them by default (Newey–West for time series).
- **Direction of the bias helps**: positive autocorrelation/heteroskedasticity usually understate SEs, so you overfind "significance". The correction often reverses conclusions (Fisher effect: t = 1.87 under White SE vs 2.29 uncorrected).
- **Think of dummies as separate lines in one regression**: the base category is the reference; coefficients are differences from it.
- **Logit works on the odds scale**: coefficient → log odds, `e^b` → odds multiplier, plug into the sigmoid → probability bounded in (0, 1).
- **Specification beats estimation**: omitted variables, wrong form or look-ahead variables corrupt coefficients, which no robust SE can cure.

## Worked Example
**1. F-test, R² and adjusted R² (bid-ask spread model).** ln(spread/price) on ln(market makers) and ln(market cap), n = 2,587, k = 2. RSS = 3,728.13, SSE = 2,172.89, SST = 5,901.02.
MSR = 1,864.07, MSE = 2,172.89/2,584 = 0.8409, **F = 2,216.75** (critical F₂,₂₅₈₄ at 5% ≈ 3.00), reject. R² = 0.6318; R̄² = 1 − (2,586/2,584)(0.3682) = 0.6315. Slopes −1.5186 and −0.3790 are elasticities: +1% market makers lowers the spread ratio by ~1.52%, holding cap constant. Prediction for 20 market makers, $100m cap: 1.5949 − 1.5186 ln 20 − 0.3790 ln 100 = −4.6998; e^−4.6998 = **0.91%** of price.

**2. Heteroskedasticity then serial correlation (Fisher effect).** T-bill rate on expected inflation, n = 181; slope 1.1744, SE 0.0761. H₀: b₁ = 1: t = 2.29 > 1.97, reject. But Breusch–Pagan: R² of squared-residual regression 0.0666, **BP = 181 × 0.0666 = 12.05 > 3.84** (χ²₁, 5%) so conditional heteroskedasticity. White SE 0.0931 gives t = 1.87, no longer rejects. DW = 0.298, r ≈ 1 − 0.298/2 = 0.851, far below d_l: severe positive serial correlation. Newey–West SE 0.1751 gives t = 0.996. Conclusion flips from "Fisher effect rejected" to "not rejected".

**3. Logit.** log odds of equity financing for a non-R&D investment −0.6577; R&D coefficient 0.90. With R&D: log odds = 0.2423, odds = e^0.2423 = 1.274, p = 1/(1+e^−0.2423) = **56.0%**; odds ratio e^0.90 = **2.46**.

**4. Python OLS check (recomputed, n = 40, seed 7, true b = 1, 2, −1)**: b̂ = 0.980, 2.258, −0.960; t = 4.48, 8.16, −3.50; SSE 57.16, SST 160.45, MSE 1.545, **F = 33.43**, R² = 0.644, R̄² = 0.625, AIC 20.3, BIC 25.3, VIF = 1.30; max leverage 0.206 < 3(3)/40 = 0.225, max Cook's D 0.24 (< 0.5, no influential point).

## Anti-patterns
- **Reading individual t-stats as a test of the whole model**: use F; individual tests ignore interactions among regressors.
- **Maximising R²**: adding junk variables raises R²; judge with adjusted R², AIC/BIC and out-of-sample performance.
- **Using all n dummies**: perfect collinearity (dummy trap); use n−1.
- **Trusting OLS SEs on financial time series**: autocorrelation and heteroskedasticity are the norm; report robust/Newey–West SEs.
- **Diagnosing multicollinearity with pairwise correlations**: low pairwise correlations do not rule it out (only valid as a sufficient check with exactly two regressors).
- **Adding a lagged dependent variable to "fix" autocorrelation**: with serially correlated errors it makes every coefficient biased and inconsistent.
- **Predicting returns with end-of-period characteristics** (market cap, P/B at t+1): they are functions of the dependent variable ("forecasting the past").
- **Using a mismeasured regressor** (actual instead of expected inflation): in a one-regressor model the slope is biased toward zero (0.89 vs 1.17).
- **Linear regression on a binary outcome**: the linear probability model predicts outside [0, 1]; use logit.
- **Data mining**: exploiting one dataset without economic logic and no out-of-sample test.
- **Regressing unscaled sizes**: FCF on CFO of 11 retailers gave R² 0.83, but scaled by sales R² fell to 0.23 (insignificant): the first was just a size effect.

## Exam Focus & Traps
- df: t uses n−(k+1); F uses (k, n−k−1); intercept counts as a coefficient. SST df = n−1.
- Adjusted R² < R² for k ≥ 1; to compare models via R̄² the dependent variable and sample size must be identical.
- F-test is one-tailed (right); Breusch–Pagan is one-tailed χ² with k df; DW has an inconclusive zone.
- Heteroskedasticity: coefficients unaffected, SEs wrong; typical direction "SE too small, t too large", but not always. Only **conditional** heteroskedasticity matters.
- Serial correlation of the positive type inflates F and t; remedy is Newey–West/Hansen (which also covers heteroskedasticity); White SE alone does not fix serial correlation.
- Multicollinearity classic symptom: high R², significant F, low t's. Remedy: drop variable(s). It is not fixed by robust SEs.
- Omitted variable bias requires the omitted variable to be correlated with the included ones.
- Slope dummy coefficient = incremental slope; the D=1 slope is b₁ + d₁ (Growth funds' age effect 0.065 + 0.020).
- Logit: coefficient = change in log odds, not in probability; `e^b` is the odds ratio; p = 1/(1+e^−x). Estimation by MLE, tests by z (or Wald) and likelihood-ratio χ². No true R², only pseudo-R².
- Unit traps: a coefficient on a % variable entered as a fraction (0.01 = 1%): multiply the coefficient by 0.01 for a 1% move.
- ⚠ Correction: the 2022 text writes the logit probability formula as "from Equation 7" and later "Equation 8"; the formula is Equation 15, p = 1/(1+exp[−(b₀+Σbⱼ Xⱼ)]). Minor R² rounding (0.862 vs 0.8627) appears in the FSPTX exhibits. No Level II 2022 errata item applies to this reading.
- Not tested in this 2022 version: AIC/BIC, VIF, leverage and Cook's D (they appeared in earlier editions); the [Ext.] items above are included for professional use.

## Key Takeaways
1. Interpret each slope as a partial effect; its value changes when other regressors enter.
2. Order of vetting: F-test, then t-tests, then adjusted R²/SEE, then residual diagnostics.
3. Use n−1 dummies; slope dummies capture different sensitivities across groups, intercept dummies different levels.
4. Always run Breusch–Pagan and Durbin–Watson (or Breusch–Godfrey) on time-series work and use robust/Newey–West SEs; conclusions can flip.
5. Multicollinearity: look for high R² with insignificant t's (or VIF > 5-10); remedy is dropping or combining variables.
6. Misspecification (omitted variables, wrong scaling, pooling, look-ahead, lagged-Y with autocorrelation, measurement error, nonstationarity) corrupts coefficients, so fix the model, not the SEs.
7. Build models on economic logic, keep them parsimonious, validate out of sample.
8. For binary outcomes use logit: coefficients are log-odds changes, `e^b` is the odds ratio, outputs are probabilities in (0,1), fit judged by likelihood-ratio test and pseudo-R².

## Connects To
- **ch 07**: simple regression, OLS, ANOVA, single-variable t-tests and prediction intervals this chapter generalises.
- **ch 09**: time-series regressions, unit roots, AR models (lagged Y), cointegration; remedy for nonstationarity.
- **ch 10**: logistic regression as a classifier, penalised regression (LASSO) for parsimony, overfitting vs out-of-sample.
- **ch 06**: hypothesis testing logic, Type I error inflation from understated SEs.
- **`cfa-portfolio-management` ch 12**: multifactor models are multiple regressions (factor betas, style analysis).
- **`cfa-portfolio-management` ch 14**: backtesting and data mining pitfalls match the specification principles.
- **`cfa-equity-valuation` ch 09**: regression-based valuation (multiples on fundamentals) and its collinearity risks.
