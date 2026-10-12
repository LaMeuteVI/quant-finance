# Chapter 6: Hypothesis Testing
> **Source**: CFA Program Curriculum 2020, Level I, Reading 11 · Quantitative Methods | DeFusco, McLeavey, Pinto, Runkle

## Core Idea
Hypothesis testing turns a claim about a population parameter into a decision rule: assume the null is true, compute how surprising the sample is, and reject only if the evidence beats a pre-set significance level. Every test has the same skeleton, `(sample statistic − hypothesized value) / standard error`, and the whole skill is choosing the right statistic and distribution (z, t, chi-square, F) for the parameter (mean, mean difference, variance, correlation) and the sampling design (one sample, independent samples, paired samples).

## Learning Outcomes Covered
- define hypotheses, list the steps of a test, choose null and alternative (one- vs two-tailed)
- explain test statistic, Type I and Type II errors, significance level, decision rule, power, and the confidence-interval link
- separate statistical from economic significance; interpret the p-value
- test a single mean (large or small sample; variance known or unknown)
- test equality of two means (independent samples, equal or unequal variances) and the mean of paired differences
- test a single variance (chi-square), the equality of two variances (F), and zero correlation (t)
- distinguish parametric from nonparametric tests and when to use the latter (Spearman rank correlation, Wilcoxon, Mann-Whitney, sign test)

## Frameworks Introduced
- **Seven steps of hypothesis testing**: (1) state H0 and Ha; (2) identify the test statistic and its distribution; (3) specify the significance level α; (4) state the decision rule (rejection points); (5) collect data and compute the statistic; (6) make the statistical decision; (7) make the economic or investment decision.
  - When to use: every formal test. Steps 1 to 6 are statistical; step 7 adds costs, taxes, risk and plausibility.
  - Failure mode: choosing α after seeing the statistic compromises objectivity; stopping at step 6 confuses significance with value.
- **Null/alternative design**: Ha holds the claim you want evidence for ("hoped-for" condition); H0 is the status quo that gets the benefit of the doubt. The three formulations: `H0: θ=θ0 vs Ha: θ≠θ0` (two-tailed), `H0: θ≤θ0 vs Ha: θ>θ0` (right-tailed), `H0: θ≥θ0 vs Ha: θ<θ0` (left-tailed). The hypotheses must exhaust all parameter values; the test is always run at the point of equality θ=θ0, with the same calculation for all three forms and different rejection regions.
  - Use "≠" when you are neutral; use one-sided when theory gives a direction (risk premium > 0, receivable days slowed, variance of witching days higher).
- **Error trade-off (Type I vs Type II)**: Type I = reject a true H0, probability α (the significance level); Type II = fail to reject a false H0, probability β; **power = 1−β** = probability of rejecting a false H0.

  | Decision | H0 true | H0 false |
  |---|---|---|
  | Do not reject H0 | correct (1−α) | Type II error (β) |
  | Reject H0 | Type I error (α) | correct (power, 1−β) |

  - How to use: only α is specified in practice (β depends on which alternative value is true, so it has no single number). Lowering α raises β; the only way to lower both at once is a larger n. Prefer the more powerful test when two are available. Conventional α: 0.10 (some evidence), 0.05 (strong), 0.01 (very strong).
- **Decision rule by critical value**: reject H0 if the statistic is more extreme than the rejection point(s). Two-tailed uses α/2 in each tail; one-tailed uses α in one tail. Failing to reject is not "accepting" H0 (a court says "not guilty", not "innocent").
- **p-value approach**: p = the smallest significance level at which H0 can be rejected (the probability, under H0, of a statistic at least as extreme as observed). Reject if p < α. Smaller p means stronger evidence. Reporting p lets readers apply their own α.
- **Confidence-interval duality**: a two-sided test at significance α rejects H0: θ=θ0 exactly when θ0 lies outside the (1−α) confidence interval. Practitioners prefer the test statistic because it yields a p-value and handles one-sided cases.
- **Statistical vs economic significance**: the standard error shrinks with n, so a huge sample rejects tiny, worthless deviations. Always compare the magnitude of the effect with transaction costs, taxes, risk, and an economic rationale (step 7).
- **"Which test when" decision procedure**: (1) What parameter? mean, difference of means, variance, ratio of variances, correlation. (2) Is σ known? (3) One sample, two independent samples, or paired? (4) Are normality assumptions credible? If not, use a nonparametric alternative. The master table is in Formulas.

## Key Concepts
- **Hypothesis**: statement about one or more populations; **null (H0)** is the hypothesis tested and presumed true until evidence contradicts; **alternative (Ha)** is accepted when H0 is rejected.
- **Test statistic**: sample-based quantity used to decide; usually `(sample statistic − value under H0)/standard error`.
- **Significance level (α)**: probability of a Type I error; chosen before the test.
- **Rejection point / critical value**: threshold the statistic is compared with; the region beyond it is the rejection (critical) region, the complement the "acceptance" region (better: do-not-reject region).
- **Power of a test**: probability of correctly rejecting a false null (1−β).
- **Statistically significant**: statistic falls in the rejection region (p < α).
- **p-value (marginal significance level)**: smallest α at which H0 is rejected.
- **t-test**: statistic follows a t-distribution (df-indexed, fat-tailed, symmetric); robust to moderate non-normality except outliers and strong skew.
- **z-test**: statistic follows the standard normal; correct when σ is known, used as large-sample alternative.
- **Pooled variance**: weighted average of two sample variances, valid when population variances are assumed equal.
- **Paired comparisons test**: t-test on differences between dependent (matched) observations; handles correlation between the two series.
- **Chi-square distribution**: asymmetric, bounded below by 0, df-indexed (n−1 for a variance); sensitive to non-normality.
- **F-distribution**: asymmetric, bounded below by 0, two df (numerator and denominator); ratio of two chi-squares each divided by its df; sensitive to non-normality.
- **Parametric vs nonparametric**: parametric tests concern distribution parameters and assume a distribution; nonparametric tests use ranks or signs, make few assumptions, and suit ranked data, strong non-normality, or non-parameter questions.
- **Spearman rank correlation (rS)**: correlation computed on ranks; robust to non-normal data and ordinal data.

## Formulas & Reference Tables
**Master test table ("which test when")**

| Hypothesis about | Conditions | Test statistic | Distribution, df | Reject (two-tail) |
|---|---|---|---|---|
| One mean, σ known | normal pop., or large n | `z=(X̄−μ0)/(σ/√n)` | standard normal | \|z\| > z_{α/2} |
| One mean, σ unknown | normal pop. (small n) or large n | `t=(X̄−μ0)/(s/√n)` | t, df = n−1 | \|t\| > t_{α/2,n−1} |
| One mean, σ unknown, large n | any shape, CLT | `z=(X̄−μ0)/(s/√n)` | standard normal (alternative to t) | \|z\| > z_{α/2} |
| Difference of two means, independent samples, variances unknown but equal | both normal | `t=[(X̄1−X̄2)−(μ1−μ2)] / √(s_p²/n1 + s_p²/n2)`, `s_p²=[(n1−1)s1²+(n2−1)s2²]/(n1+n2−2)` | t, df = n1+n2−2 | \|t\| > t_{α/2} |
| Difference of two means, independent, variances unknown and unequal | both normal | `t=[(X̄1−X̄2)−(μ1−μ2)] / √(s1²/n1 + s2²/n2)` | t, modified df (below) | \|t\| > t_{α/2} |
| Mean of paired differences | dependent samples, differences normal | `t=(d̄−μd0)/s_d̄`, `s_d̄=s_d/√n` | t, df = n−1 (n = pairs) | \|t\| > t_{α/2} |
| One variance | normal pop. | `χ²=(n−1)s²/σ0²` | chi-square, df = n−1 | χ² > χ²_{α/2} or < χ²_{1−α/2} |
| Equality of two variances | independent samples, both normal | `F=s1²/s2²` (put larger on top) | F, df1 = n1−1, df2 = n2−1 | F > F_{α/2} (upper) |
| Correlation = 0 | bivariate normal | `t=r√(n−2)/√(1−r²)` | t, df = n−2 | \|t\| > t_{α/2} |
| Rank correlation = 0 (nonparametric) | any; n > 30 for t approx. | `t=r_S√(n−2)/√(1−r_S²)`; small n use special table | t, df = n−2 (large n) | \|t\| > t_{α/2} or table |

**Other formulas**
- Modified (Welch) df, curriculum form: `df=(s1²/n1+s2²/n2)² / [ (s1²/n1)²/n1 + (s2²/n2)²/n2 ]`. **⚠ Correction (note):** the standard Welch-Satterthwaite form divides by `n−1` in each term; the curriculum divides by `n`. Compute the t-statistic first (the decision is often obvious), then df; round and use the nearest table row. Exam answers follow the curriculum form.
- Paired standard error with correlation: `s_d² = s_A² + s_B² − 2·r·s_A·s_B`, then `s_d̄ = s_d/√n`.
- Chi-square confidence interval for σ²: `(n−1)s²/χ²_{α/2} ≤ σ² ≤ (n−1)s²/χ²_{1−α/2}` (asymmetric).
- Spearman: `r_S = 1 − 6Σd_i² / [n(n²−1)]`; ties get average ranks; correct only if the ranks have no ties (with ties it is approximate; the exact method is Pearson on ranks).
- F reciprocal property: `F_{a,b}(α) = 1/F_{b,a}(1−α)`; if you compute F<1, invert it and swap df.
- F and chi-square: `F=(χ1²/m)/(χ2²/n)`.
- Variance of the t-distribution: `df/(df−2)`.
- Test statistic template: `(sample statistic − value under H0) / standard error`. The significance level and decision are tied: two-tailed 5% uses ±1.96 (z) because α/2=0.025 in each tail.

**Critical values for z-tests**

| α | Two-tailed ≠ | Right-tailed > | Left-tailed < |
|---|---|---|---|
| 0.10 | ±1.645 | 1.28 | −1.28 |
| 0.05 | ±1.96 | 1.645 | −1.645 |
| 0.01 | ±2.575 | 2.33 | −2.33 |

**t critical values (verified in Python)**

| df | one-tail .05 | one-tail .025 | one-tail .01 | one-tail .005 |
|---|---|---|---|---|
| 23 | 1.714 | 2.069 | 2.500 | 2.807 |
| 29 | 1.699 | 2.045 | 2.462 | 2.756 |
| 49 | 1.677 | 2.010 | 2.405 | 2.680 |
| 59 | 1.671 | 2.001 | 2.391 | 2.662 |
| 70 | 1.667 | 1.994 | 2.381 | 2.648 |
| ∞ | 1.645 | 1.960 | 2.326 | 2.576 |

**Test selection summary: what the sample design tells you**

| Question | Samples | Use |
|---|---|---|
| Is a mean equal to a number? | one | t (z if σ known) |
| Do two groups have the same mean? | independent (different firms/periods) | pooled t (equal variances) or Welch-type t (unequal) |
| Did the same units change, or do two correlated series differ? | dependent (before/after, two strategies on the same months) | paired t on differences |
| Is risk (variance) equal to a number? | one | chi-square |
| Is risk the same in two groups? | independent | F |
| Is the correlation zero? | one paired sample | t with n−2 df |
| Assumptions fail or data are ranks | any | nonparametric |

**Parametric to nonparametric alternatives**

| Parametric | Nonparametric |
|---|---|
| t/z on a single mean | Wilcoxon signed-rank |
| t on difference of means (independent) | Mann-Whitney U |
| paired t | Wilcoxon signed-rank, sign test |
| t on correlation | Spearman rank correlation |
| (question not about a parameter) | runs test (randomness), Kolmogorov-Smirnov (distribution fit) |

## Mental Models
- **Courtroom**: H0 = presumed innocent; rejecting needs strong evidence; "not guilty" (fail to reject) does not prove innocence. Type I = convicting the innocent (α), Type II = acquitting the guilty (β).
- **Signal-to-noise**: every test statistic is distance from the null measured in standard errors. Larger n shrinks noise, so tiny effects become "significant"; ask whether the effect size matters.
- **Dependent data, difference first**: if the two series share a driver (same market, same firms, before/after), difference them and run a one-sample t on the differences. The correlation is absorbed in s_d, so this beats an independent-samples test.
- **Variance tests are fragile, mean tests are sturdy**: t is robust to moderate non-normality; chi-square and F are not. Check normality (or go nonparametric) before trusting a variance test.
- **Confidence interval and test are the same fact**: if the null value is outside the (1−α) interval, reject at α.
- **Put the bigger variance on top** of the F ratio: one right-tail critical value, and the statistic is ≥ 1.

## Worked Example
**1. One mean, t, two-tailed (verified in Python).** Sendar Equity Fund: 24 months, mean 1.50%, s = 3.60%, benchmark expected 1.10%, normal returns, α = 0.10. H0: μ=1.10 vs Ha: μ≠1.10. `t=(1.50−1.10)/(3.60/√24)=0.40/0.7348=0.544`, df = 23, critical ±1.714. Not rejected (two-sided p = 0.59). 90% CI `1.50 ± 1.714×0.7348 = [0.240, 2.760]` contains 1.10, same decision.

**2. One mean, one-tailed.** Receivables: n = 50, mean 49 days, s = 8, H0: μ ≤ 45 vs Ha: μ > 45. `t=4/(8/√50)=3.536`, df = 49; critical 1.677 (5%) and 2.405 (1%); one-sided p = 0.00045. Reject at both levels: payments have slowed.

**3. Large-sample z.** US equity risk premium 1900 to 2017: 118 years, mean 7.5%, s = 19.5%. `SE=19.5/√118=1.795%`, `z=7.5/1.795=4.18 > 1.645`, p = 0.000015 (verified 1.5×10⁻⁵). Reject H0: risk premium ≤ 0; 7.5% a year is also economically large.

**4. Two means, independent, pooled (verified).** SENSEX monthly returns, 2012-14 (n=36, mean 1.694, SD 4.115) vs 2015-17 (n=36, mean 0.665, SD 3.779), equal variances plausible. `s_p²=(35×16.933+35×14.281)/70=15.607`; `t=1.029/√(15.607×2/36)=1.029/0.931=1.11`, df=70; critical ±1.667/1.994/2.648. Do not reject at any level (p = 0.27).

**5. Two means, unequal variances (verified).** Defaulted-bond recovery: electricity n=39, mean 48.03, SD 22.67; retail n=33, mean 33.40, SD 34.19. SDs differ widely, so use the unpooled statistic: `t=14.63/√(513.93/39+1168.96/33)=14.63/6.971=2.099`. Curriculum df: `(48.60)²/[(13.178)²/39+(35.423)²/33]=55.61 → 56`; the nearest table row is 60 (critical ±1.671 at 10%). Reject at 10%; also reject at 5% (critical about ±2.00); do not reject at 1% (critical about ±2.67). With the standard Welch df of 53.9 the two-sided p-value is 0.041. A pooled test would give t = 2.17 on 70 df: close here, but not in general.

**6. Paired.** Two ETFs (worldwide vs US), 60 months, mean difference −0.27%, s_d = 1.00%. `t=−0.27/(1.00/√60)=−2.09`, df = 59, 1% critical ±2.66, so not rejected at 1% (two-sided p = 0.041, so it would be rejected at 5%: the curriculum asks only for 1%). Samples are dependent (nine of ten top holdings of the world fund are US stocks), so the paired test is correct. Quarterly returns of two metals portfolios (24 pairs, mean difference −0.65, s_d = 6.71): `t=−0.65/(6.71/√24)=−0.475`, critical ±2.069, not rejected.

**7. Variance, chi-square, left-tailed.** Sendar again: claim σ < 4%. H0: σ² ≥ 16 vs Ha: σ² < 16; `χ²=23×3.6²/16=18.63`, df 23; lower 5% critical 13.09; not rejected. (A 95% CI for σ² is [7.83, 25.50], i.e. σ in [2.80%, 5.05%].)

**8. Two variances, F.** KOSPI weekly variance before the crisis 18.203 vs after 3.919 (418 weeks each): `F=18.203/3.919=4.645`, df 417/417; two-tailed 1% uses the 0.005 table (book: 1.61 at df=120; exact 1.29); reject. Quadruple-witching days (n=16, SD 1.217) vs normal days (n=138, SD 0.821): `F=(1.217/0.821)²=2.20`, df 15/137, one-tail 5% critical 1.75 (book, df=120) or 1.74 exact; reject, so witching days are more volatile.

**9. Correlation.** JPY vs CAD returns, r = 0.5132, n = 84: `t=0.5132√82/√(1−0.2634)=5.415`, critical ±1.99 (df=82); reject ρ=0. Sample-size effect: r = 0.58 with n=12 gives t=2.252 (just significant, critical 2.228); r = 0.35 with n=32 gives t=2.046 (just significant, critical 2.042); r=0.35 at n=12 is not significant.

**10. Spearman rank (⚠ Correction).** Ten 5-star emerging-market funds: Sharpe ratios vs expense ratios. The source ranks the Sharpe values 0.65 and 0.68 as a tied 5.5 each; they are not tied (0.68 is rank 5, 0.65 rank 6). Correct ranks give `Σd²=213.5` and `r_S=1−6×213.5/(10×99)=−0.294` (source: −0.327). The conclusion is unchanged: critical value for n = 10, α = 0.05 two-tailed (0.025 column) is 0.6364, so we do not reject. (Large-sample t form does not apply for n=10: `t=−0.87`, df 8, critical 2.306 gives the same answer.)

**11. Data-mining arithmetic.** Test 100 useless predictors at 5%: expect 5 false hits; probability of at least one = 1−0.95¹⁰⁰ = 99.4%.

## Anti-patterns
- **Saying "accept H0"**: you only fail to reject; absence of evidence is not evidence of absence (check power).
- **Choosing α, tails or hypotheses after seeing the data**; or switching to one-tailed to rescue significance.
- **Treating p = 0.04 and p = 0.06 as different worlds**, or p as the probability that H0 is true.
- **Equating significance with importance**: with n large enough, a 0.1 bp edge is "significant".
- **Independent-samples test on dependent data** (two funds in the same market, before/after on the same firms): mis-states the standard error; use paired.
- **Pooling variances without checking** (SD ratio far from 1); use the unpooled statistic when unsure.
- **Chi-square/F tests on skewed or fat-tailed returns**: they are not robust to non-normality.
- **Running many tests and reporting the winner** (data mining, ch 05), no multiplicity adjustment or out-of-sample check.
- **Using n−1 df for a correlation test** (it is n−2) or n instead of n−1 for the variance test.
- **Using a parametric test on ranks or ordinal data** (manager rankings, scope-of-hedging scores).

## Exam Focus & Traps
- **Pick the null so that "=" is in it** (H0 always contains ≤, ≥ or =); the claim to support goes in Ha. Test at the equality point.
- **Rejection regions**: right-tailed means reject if stat > critical; left-tailed means reject if stat < −critical; two-tailed splits α. 1.645 is one-tail 5% and two-tail 10%.
- **Which distribution?** mean (σ known) z; mean (σ unknown) t df n−1; two independent means pooled t df n1+n2−2 or approximate t; paired t df n−1 (n = pairs, not total observations); variance chi-square df n−1; two variances F with (n1−1, n2−1); correlation t with n−2.
- **F convention**: larger sample variance in the numerator; for a two-tailed test at α, look up α/2 in the upper tail; for one-tailed at α use α. If given F < 1, invert and swap df.
- **Chi-square two-tailed**: two different critical values (upper α/2 and lower 1−α/2); one-tailed "less than": lower α point.
- **Type I = α = significance level; power = 1−β**; decreasing α raises β; only a larger sample lowers both.
- **p-value rule**: reject if p < α; smaller p, stronger evidence; "smallest significance level at which H0 can be rejected".
- **Test vs CI**: H0 value outside the CI means reject at the matching α (95% CI to 5% two-sided test).
- **Statistical vs economic significance**: the standard answer to "significant but small" is to account for costs, taxes and risk.
- **When to choose nonparametric**: assumptions fail, data are ranks, or the question is not about a parameter (runs test, K-S); if parametric assumptions hold, parametric is preferred (sharper conclusions).
- **Table rounding**: critical values come from tables at the nearest df (df=59 uses row 60, df=417 uses 120); 2.575/2.58, 1.645/1.65 differences are expected.
- **Spearman rank**: n > 30 may use the t form; otherwise use the table; ties get average ranks.
- **Sample-size effect on correlation tests**: a given r is more likely significant as n rises.

## Key Takeaways
1. Every test: state H0/Ha, choose statistic and α, set rejection points, compute, decide, then ask whether the result is economically meaningful.
2. Test statistic = (estimate − null value) / standard error; the distribution depends on the parameter (z/t for means, chi-square for one variance, F for two variances, t for correlation).
3. Type I (α) and Type II (β) errors trade off; power = 1−β; only more data cuts both.
4. p-value is the smallest α at which you reject; confidence intervals and two-sided tests agree.
5. Independent samples use pooled (equal variances, df n1+n2−2) or unpooled t; dependent samples use a paired t on differences (df n−1).
6. Variance tests (chi-square, F) are asymmetric, bounded at zero and not robust to non-normality; correlation test uses df n−2.
7. Significance is not importance: huge samples reject trivial effects; always add costs, taxes, risk and a story.
8. Use nonparametric tests (Wilcoxon, Mann-Whitney, sign, Spearman) when normality fails or data are ranks, but prefer the parametric test when its assumptions hold.

## Connects To
- **ch 05**: confidence intervals, standard errors, t vs z, data-mining and other biases that invalidate the significance level.
- **ch 04**: normal, standard normal and quantiles used for z-tests; lognormal/normal assumptions behind returns tests.
- **ch 02**: sample mean, variance, correlation, ranks and measurement scales (ordinal data call for nonparametric tests).
- **ch 07**: slope and correlation t-tests, F-test of the regression, p-values (df n−2).
- **ch 08**: t-tests on coefficients, joint F-tests, Type I/II trade-offs in model selection.
- **ch 09**: unit-root and autocorrelation tests are hypothesis tests built on the same logic.
- **ch 10**: out-of-sample validation replaces significance testing for ML models.
- **`cfa-portfolio-management` ch 03**: market-efficiency tests (abnormal returns, event studies) are z-tests of mean abnormal return equal to zero.
- **`cfa-portfolio-management` ch 14**: backtesting and multiple-testing risk.
