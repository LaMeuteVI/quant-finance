---
name: cfa-quantitative-methods
description: "CFA Program quantitative methods: Level I (2020 R6-R11) and Level II (2022 R1-R5). Covers time value of money, descriptive statistics, probability, distributions, sampling and confidence intervals, hypothesis testing, linear and multiple regression, time series, machine learning and big data projects. Use when solving TVM or annuity problems, computing EAR, geometric mean, Bayes updates, safety-first ratios, t versus z intervals, t-tests, chi-square and F tests, p-values, Type I and Type II errors, regression diagnostics (heteroskedasticity, Durbin-Watson, multicollinearity), AR models, unit roots, cointegration, LASSO, random forest, precision and recall, or preparing a CFA quantitative quiz."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Quantitative Methods (Levels I and II)
**Source**: CFA Program Curriculum Quantitative Methods: L1 2020 R6-R11, L2 2022 R1-R5 | **Domain**: Fondamentaux | **Chapters**: 11 | **Generated**: 2026-10-05

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch06`
- **Browse** — "what chapters do you have?"
- **Exam mode** — ask for a quiz on a chapter; I build it from its Worked Example and Exam Focus sections.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Time value and descriptive statistics**
- **Time line and shift rule** (ch01): index every flow at its date; annuity and perpetuity formulas value one period before the first payment, then shift with a lump-sum factor. `FV = PV(1+r)^N`, `PV annuity = A[1−(1+r)^−N]/r`, annuity due = ordinary × (1+r), perpetuity `A/r`.
- **EAR** (ch01): `EAR = (1 + rₛ/m)^m − 1`, continuous `e^rₛ − 1`. Compare offers on EAR; match periodic rate and N.
- **Match the average to the question** (ch02): geometric for past compound growth, arithmetic for expected single-period return, median for skewed data, harmonic for equal-money averaging; `harmonic ≤ geometric ≤ arithmetic`; `R_G ≈ R_A − σ²/2`.
- **Dispersion and shape** (ch02): sample variance divides by n−1; CV compares relative risk; Chebyshev `1 − 1/k²` holds for any shape; excess kurtosis > 0 means fat tails.

**Probability and distributions**
- **Probability toolkit** (ch03): `P(A or B) = P(A)+P(B)−P(AB)`; `P(AB) = P(A|B)P(B)`; total probability over exhaustive scenarios; Bayes `P(E|I) = P(I|E)P(E)/P(I)`.
- **Portfolio moments** (ch03): `E(Rp) = Σwᵢ E(Rᵢ)`; `σ²p = ΣΣ wᵢwⱼ Cov`; diversification works through covariance (ρ < 1).
- **Distribution chooser** (ch04): counts of successes are binomial, returns normal, prices lognormal (`E = exp(μ+σ²/2)`), complex payoffs Monte Carlo. Continuous return `r = ln(1+R)`, additive, volatility scales with √T.
- **Roy's safety-first** (ch04): maximize `[E(R)−R_L]/σ`; shortfall probability `N(−SFRatio)`; Sharpe is the case R_L = R_F.

**Inference**
- **CLT and standard error** (ch05): `X̄ ~ N(μ, σ²/n)` for large n; SE = `s/√n`. Quadruple n to halve the width.
- **Confidence interval recipe** (ch05): point estimate ± reliability factor × SE; z if σ known, t with n−1 df otherwise (z acceptable for large n).
- **Four biases** (ch05): data mining, survivorship (sample selection), look-ahead, time period; mixed populations break the CLT story.
- **Seven-step test** (ch06): H₀/Hₐ, statistic, α, rejection points, compute, decide, economic judgment. Type I = α, power = 1−β, p-value = smallest α that rejects.
- **Which test when** (ch06): mean σ known z; mean σ unknown t (n−1); independent means pooled t (n₁+n₂−2) or unpooled; paired t (n−1); variance χ² (n−1); two variances F (larger on top); correlation t (n−2); rank data Spearman, Wilcoxon, Mann-Whitney.

**Regression and time series**
- **OLS and ANOVA** (ch07): slope = Cov/Var, `R² = SSR/SST`, `F = MSR/MSE`, `SEE = √MSE`, `F = t²` in simple regression; prediction interval `Ŷf ± t·s_f`; log-lin, lin-log, log-log forms.
- **Vet in order** (ch08): F, then t, then adjusted R²; use Breusch-Pagan and Durbin-Watson; Newey-West or White standard errors; multicollinearity shows as a significant F with weak t's; logit coefficient is a log-odds change, `e^b` the odds ratio.
- **Stationarity pipeline** (ch09): plot, trend or difference, AR(p) with residual autocorrelation tests (SE 1/√T), seasonal lag, ARCH, out-of-sample RMSE. Mean-reverting level `b₀/(1−b₁)`; Dickey-Fuller H₀ unit root; Engle-Granger for cointegration.

**Machine learning and big data**
- **Algorithm chooser** (ch10): many correlated features PCA; continuous target LASSO or trees; categorical target KNN, SVM, CART, forest; unlabeled data k-means or hierarchical. Bias is underfit, variance is overfit; judge on held-out data.
- **Project pipeline and metrics** (ch11): conceptualize, collect, prepare, explore, train; text becomes a DTM; precision `TP/(TP+FP)`, recall `TP/(TP+FN)`, F1, AUC, RMSE; tune hyperparameters on validation data.

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l1-time-value-of-money.md) | The Time Value of Money | L1 · R6 | Time line, EAR, annuity shift rule, additivity |
| [ch02](chapters/ch02-l1-statistical-concepts-and-market-returns.md) | Statistical Concepts and Market Returns | L1 · R7 | Means, dispersion, Chebyshev, skewness and kurtosis |
| [ch03](chapters/ch03-l1-probability-concepts.md) | Probability Concepts | L1 · R8 | Bayes, total probability, covariance, counting |
| [ch04](chapters/ch04-l1-common-probability-distributions.md) | Common Probability Distributions | L1 · R9 | Binomial, normal, lognormal, Roy's criterion, Monte Carlo |
| [ch05](chapters/ch05-l1-sampling-and-estimation.md) | Sampling and Estimation | L1 · R10 | CLT, confidence intervals, z vs t, sampling biases |
| [ch06](chapters/ch06-l1-hypothesis-testing.md) | Hypothesis Testing | L1 · R11 | Seven steps, which-test table, errors, p-values, nonparametrics |
| [ch07](chapters/ch07-l2-linear-regression.md) | Introduction to Linear Regression | L2 · R1 | OLS, ANOVA, prediction intervals, functional forms |
| [ch08](chapters/ch08-l2-multiple-regression.md) | Multiple Regression | L2 · R2 | F, adjusted R², violations, dummies, logit |
| [ch09](chapters/ch09-l2-time-series-analysis.md) | Time-Series Analysis | L2 · R3 | Trends, AR, unit roots, ARCH, cointegration |
| [ch10](chapters/ch10-l2-machine-learning.md) | Machine Learning | L2 · R4 | Bias-variance, LASSO, trees, PCA, clustering |
| [ch11](chapters/ch11-l2-big-data-projects.md) | Big Data Projects | L2 · R5 | Data prep, text DTM, confusion matrix, tuning |

## Topic Index
- **Adjusted R²** → ch08
- **Annuity, perpetuity** → ch01
- **AR models, mean reversion** → ch09
- **ARCH** → ch09
- **Bayes' formula** → ch03
- **Binomial distribution** → ch04
- **Bias-variance, overfitting** → ch10, ch11
- **Central limit theorem** → ch05
- **Chebyshev's inequality** → ch02
- **Chi-square test** → ch06
- **Cointegration, Dickey-Fuller** → ch09
- **Confidence intervals** → ch05, ch06
- **Confusion matrix, precision, recall** → ch11
- **Correlation, covariance** → ch03, ch06
- **Cross-validation** → ch10, ch11
- **Data mining, survivorship, look-ahead bias** → ch05
- **Durbin-Watson** → ch08, ch09
- **Effective annual rate** → ch01
- **F-test** → ch06, ch07, ch08
- **Frequency distributions, percentiles** → ch02
- **Geometric vs arithmetic mean** → ch02
- **Heteroskedasticity** → ch08
- **Hypothesis testing steps** → ch06
- **Interest rate premiums** → ch01
- **k-means, hierarchical clustering** → ch10
- **LASSO** → ch10
- **Logit, odds ratio** → ch08
- **Lognormal, continuous returns** → ch04
- **Monte Carlo, historical simulation** → ch04
- **Multicollinearity** → ch08
- **Nonparametric tests, Spearman** → ch06
- **Normal distribution, z-scores** → ch04
- **OLS, R², SEE** → ch07
- **p-value** → ch06
- **PCA** → ch10
- **Prediction interval** → ch07
- **Random forest, CART, SVM, KNN** → ch10
- **Roy's safety-first** → ch04
- **Sampling methods, stratified sampling** → ch05
- **Serial correlation, Newey-West** → ch08
- **Skewness, kurtosis** → ch02
- **Standard error** → ch05
- **Student's t-distribution** → ch05, ch06
- **Text data, TF-IDF, DTM** → ch11
- **Time value of money** → ch01
- **Trend models, random walk, unit root** → ch09
- **Type I and Type II error, power** → ch06
- **Variance and standard deviation** → ch02
- **Weighted mean, harmonic mean** → ch02

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, which-test table, thresholds, exam traps

---

## Related Skills
- `cfa-portfolio-management` — mean-variance, Sharpe, market efficiency, backtesting and multifactor models that use these tools
- `cfa-equity-valuation` — regression-based and multiples valuation applications
- `cfa-economics` — macro series that feed trend and AR models
- `cfa-corporate-finance` — NPV, IRR and annuity applications of TVM
- `cfa-fixed-income` — bond pricing as PV of annuity plus lump sum
- `pairs-trading-partial-cointegration` — cointegration applied to trading
- `cfa-level1-curriculum` — personal L1 revision notes on the same readings

## Scope & Limits
Covers the CFA quantitative methods readings only: L1 (2020 curriculum) and L2 (2022, errata applied). Later curricula revise readings, so check current learning outcome statements. Source corrections are flagged in chapters as Correction or Errata (notably the Spearman example and Welch degrees of freedom in ch06, time-series arithmetic in ch09). Derivations, Bayesian estimation, GARCH variants, multivariate statistics and Level III quantitative content are not covered. Curriculum tables round critical values (for example 1.65 versus 1.645); expect small differences with exact software values.
