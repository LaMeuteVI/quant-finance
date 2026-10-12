# Chapter 5: Sampling and Estimation
> **Source**: CFA Program Curriculum 2020, Level I, Reading 10 · Quantitative Methods | DeFusco, McLeavey, Pinto, Runkle

## Core Idea
A sample statistic is a random variable, so every number computed from data carries sampling error. The central limit theorem (CLT) tells you how that error behaves (sample means are approximately normal with standard error σ/√n), which lets you wrap a point estimate in a confidence interval: `point estimate ± reliability factor × standard error`. The practical skill is picking the right reliability factor (z vs t), and spotting biased samples (data mining, survivorship, look-ahead, time-period) before any statistics are computed.

## Learning Outcomes Covered
- define simple random sampling, sampling distribution, sampling error; contrast with stratified random sampling
- distinguish time-series from cross-sectional data
- explain the CLT and compute and interpret the standard error of the sample mean
- state the desirable properties of an estimator (unbiased, efficient, consistent); point estimate vs confidence interval
- describe the t-distribution and its degrees of freedom
- build confidence intervals for a mean with known variance, unknown variance, and unknown variance with a large sample
- discuss sample-size selection and data-mining, sample selection, survivorship, look-ahead and time-period biases

## Frameworks Introduced
- **Simple random vs stratified random sampling**: simple = every population member has the same probability of selection; stratified = split the population into strata (cells) by classification criteria, draw simple random samples from each in proportion to stratum size, pool them.
  - When to use: simple random for unbiased inference when the population is homogeneous; stratified when subgroups must be represented (bond indexing by duration, sector, credit quality, call exposure) or when you want smaller variance than simple random sampling.
  - How: define the strata; count cells with the multiplication rule (3 issuer types × 10 maturity buckets × 2 coupon classes = 60 cells, so at least 60 bonds); sample each cell proportionally to its market weight. Systematic sampling (every kth member) is the fallback when members cannot be listed; it is only approximately random.
  - Failure mode: once extra screens (e.g., liquidity) pick bonds inside a cell, the sample is no longer random. That is acceptable when the goal is to replicate an index, not to infer a population parameter.
- **Central limit theorem and standard error of the mean**: for any population with mean μ and finite variance σ², the distribution of X̄ from samples of size n is approximately N(μ, σ²/n) when n is large (rule of thumb n ≥ 30).
  - When to use: any inference on a mean when the population shape is unknown or non-normal.
  - How: `σ_X̄=σ/√n` if σ is known; `s_X̄=s/√n` with `s²=Σ(Xᵢ−X̄)²/(n−1)` otherwise (almost always). Quadrupling n halves the standard error.
  - Failure mode: strongly skewed or fat-tailed populations need n well above 30; CLT needs finite variance and one population (see "mixed populations" below). For sampling without replacement from a finite population multiply the standard error by `√[(N−n)/(N−1)]` (finite population correction), ignorable when n < 5% of N.
- **Estimator quality checklist**: unbiased (expected value equals the parameter), efficient (smallest variance among unbiased estimators), consistent (sampling distribution collapses onto the parameter as n grows).
  - How to apply: the sample mean is unbiased, efficient and consistent for μ; `s²` with divisor n−1 is unbiased for σ² (divisor n is biased low). Unbiasedness and efficiency hold at any n; consistency is an asymptotic (large-n) property. Larger samples help only if the estimator is consistent.
- **Confidence interval (CI) recipe**: `point estimate ± reliability factor × standard error`, with confidence level 1−α.
  - Interpretation: probabilistic = in repeated sampling, 100(1−α)% of such intervals contain the parameter; practical = we are 100(1−α)% confident this interval contains it. It is not "95% probability that μ is in this particular interval" in the frequentist sense, and not a statement about individual observations.
  - Width drivers: confidence level (higher means wider: "the surer we want to be, the less we have to be sure of"), standard error (smaller with bigger n), and reliability factor (t > z at the same α).
- **Reliability factor selector (z vs t)**: see table in Formulas. Rule: unknown variance means use t with df=n−1 (the conservative, theoretically correct choice at any n); z is acceptable only when σ is known, or as the "z-alternative" with unknown variance and a large sample.
- **Sample-size trade-off**: more data narrows the CI, but (1) a longer window may mix two populations, (2) collecting costs money. Weigh precision, population homogeneity and cost. For a target half-width E, `n ≈ (t_{α/2}·s/E)²` (iterate because t depends on n).
- **Mixed-population check** (why pooling can mislead): two years of quarterly excess returns, a low-risk year (+5, −3, +5, −3: mean 1%, SD 4.62%, Sharpe 0.22) and a high-risk year (+20, −12, +20, −12: mean 4%, SD 18.48%, Sharpe 0.22), pool to mean 2.5%, SD 12.57%, Sharpe 0.199, below a 0.21 benchmark although each year beat it. Pooled data came from no single population, so the larger sample gave the wrong conclusion.
- **Four sampling biases**: a diagnostic checklist.
  - **Data-mining bias**: drilling the same data until something looks significant. Test 100 useless variables at 5% and expect about 5 "significant" ones (probability of at least one false positive is 1−0.95¹⁰⁰ ≈ 99.4%). Tells: *too much digging, too little confidence* (many variables tried, undisclosed) and *no story, no future* (no economic rationale; a butter-production series that "explained" 75% of S&P 500 variation is the classic example). Defences: out-of-sample tests, an economic rationale, disclosing the number of tests tried. Intergenerational data mining = later researchers inherit earlier researchers' data-snooping, so the effective number of tests is far larger than any one paper reports.
  - **Sample selection bias**: data availability excludes assets non-randomly. **Survivorship bias** is the key case: databases that list only existing funds/firms drop the failures, inflating average returns (hedge fund databases also suffer self-selection: only good track records volunteer to report).
  - **Look-ahead bias**: the test uses information not available on the decision date (year-end book value assumed known on 31 December, though published months later).
  - **Time-period bias**: results specific to the window; short windows are period-specific, long windows risk structural breaks (two different return distributions). Test anomalies across several business cycles.

## Key Concepts
- **Population / parameter**: all members of a group / a quantity describing it (μ, σ²).
- **Sample / statistic**: a subset / a quantity computed from it (X̄, s²).
- **Sampling plan**: the rules used to select the sample.
- **Sampling error**: difference between the observed statistic and the parameter it estimates (the price paid for sampling instead of surveying everyone).
- **Sampling distribution**: distribution of a statistic across all possible same-size samples; defined for a given n.
- **Standard error**: standard deviation of a sample statistic (for the mean, σ/√n or s/√n).
- **Estimator vs estimate**: the formula (random variable with a sampling distribution) vs the number it produces for one sample (a fixed number).
- **Time series vs cross-section**: observations of one unit at equally spaced times vs observations of many units at one date. **Panel data** = several units through time; **longitudinal data** = one unit through time.
- **Stationarity**: constant mean and variance through time; mixing regimes (fixed vs floating FX, tight vs loose policy) breaks it.
- **Degrees of freedom (df)**: number of independent observations left after estimating parameters; n−1 for a sample variance, because the sample mean pins down the last observation.
- **Student's t-distribution**: symmetric, mean 0, variance df/(df−2) (> 1), fatter tails than the normal, converges to the standard normal as df rises; one-parameter family indexed by df.
- **Reliability factor**: the z or t multiplier set by the confidence level (and df for t).
- **Out-of-sample test**: test on data that does not overlap the development sample; the main check for data mining.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Standard error, σ known | `σ_X̄ = σ/√n` |
| Standard error, σ unknown | `s_X̄ = s/√n`, `s² = Σ(Xᵢ−X̄)²/(n−1)` |
| Finite population correction | `√[(N−n)/(N−1)]` (use when sampling without replacement and n ≥ 5% of N) |
| CI, normal population, σ known | `X̄ ± z_{α/2}·σ/√n` |
| CI, σ unknown, large n (z-alternative) | `X̄ ± z_{α/2}·s/√n` |
| CI, σ unknown (t, df = n−1) | `X̄ ± t_{α/2}·s/√n` |
| t statistic | `t=(X̄−μ)/(s/√n)` ~ t with n−1 df |
| Variance of t | `df/(df−2)`, defined for df > 2 |
| Sample size for half-width E | `n ≈ (t_{α/2}·s/E)²` |

**z reliability factors (two-sided)**

| Confidence | α | z_{α/2} (curriculum 2-dp) | Exact |
|---|---|---|---|
| 90% | 0.10 | 1.65 | 1.645 |
| 95% | 0.05 | 1.96 | 1.960 |
| 99% | 0.01 | 2.58 | 2.576 (2.575 also quoted) |

**t critical values, two-sided (verified in Python)**

| df | 90% (t.05) | 95% (t.025) | 99% (t.005) |
|---|---|---|---|
| 9 | 1.833 | 2.262 | 3.250 |
| 23 | 1.714 | 2.069 | 2.807 |
| 29 | 1.699 | 2.045 | 2.756 |
| 49 | 1.677 | 2.010 | 2.680 |
| 99 | 1.660 | 1.984 | 2.626 |
| ∞ (z) | 1.645 | 1.960 | 2.576 |

**Which reliability factor** (Table 3 of the reading)

| Population | Variance | Small sample (n < 30) | Large sample (n ≥ 30) |
|---|---|---|---|
| Normal | known | z | z |
| Normal | unknown | t | t (z also acceptable) |
| Non-normal | known | not available | z |
| Non-normal | unknown | not available | t (z also acceptable) |

## Mental Models
- **Every statistic is a draw from a distribution.** Ask "how far could this be from the truth?" before "what is the number?". The answer is the standard error.
- **Use t whenever you had to estimate σ.** The extra fat-tail width is the price of not knowing σ; it vanishes as df grows, so t is never wrong, only occasionally unnecessary.
- **CI = estimate ± (confidence multiplier × noise).** To tighten it, you can lower confidence, collect more data (cost √n), or reduce noise; you cannot beat √n (4× data for half the width).
- **A bigger sample from a mixed population is worse than a small clean one.** Homogeneity first, then size.
- **A backtest is only as honest as its data availability.** Ask what was knowable on the date (look-ahead), who is missing (survivorship), how many ideas were tried (data mining), and which regime the window covers (time period).
- **Strategy that works in-sample + no story = noise until proven out-of-sample.**

## Worked Example
**z vs t (verified in Python).** Random sample of 100 US equity funds; mean Sharpe ratio 0.45, s = 0.30, standard error `0.30/√100=0.03`. 90% CI:
- z-alternative: `0.45 ± 1.65×0.03 = [0.4005, 0.4995]`.
- t with df = 99 (exact t.05 = 1.660; the book rounds to df=100, 1.66): `0.45 ± 1.660×0.03 = [0.4002, 0.4998]`.
Both round to 0.40 to 0.50; at n=100 the choice barely matters. At n=10 it does: for 95% confidence the t factor is 2.262 against 1.96 (15% wider).

**Net client flows (small-sample t, verified).** Weighted sample mean 5.5%, s = 10%, assumed normal, 95% CI:

| n | df | t.025 | s/√n | Half-width | Interval | Width vs n=10 |
|---|---|---|---|---|---|---|
| 10 | 9 | 2.262 | 3.162 | 7.15 | −1.65% to +12.65% | 100% |
| 20 | 19 | 2.093 | 2.236 | 4.68 | 0.82% to 10.18% | 65.5% |
| 30 | 29 | 2.045 | 1.826 | 3.73 | 1.77% to 9.23% | 52.2% |

Interpretation: at n = 10 the interval contains zero, so a net inflow is not established; at n = 20 and 30 it excludes zero. Width falls through both the standard error (√n) and the shrinking t factor.

**Known-variance CI.** σ = 20, n = 100, X̄ = 25: standard error 2, 95% CI `25 ± 1.96×2 = [21.08, 28.92]`.

**CLT check.** Uniform(0,100) is flat, yet means of n=100 draws cluster bell-shaped around 50 with standard error `28.87/√100=2.887` (σ = 100/√12 = 28.87). A 200-trial simulation in the reading gave 2.80, so close to theory.

**Sharpe pooling trap (verified).** Year 1 (+5, −3, +5, −3) and year 2 (+20, −12, +20, −12): pooled mean 2.5%, pooled SD 12.57%, Sharpe 0.199 (below the 0.21 benchmark) despite 0.22 in each year. Cause: two populations, not one.

## Anti-patterns
- **Reading a 95% CI as "95% of the data lie inside it"**: it brackets the parameter (the mean), not individual observations.
- **Using z with a small sample and unknown σ**: understates width; use t (needs approximate normality).
- **Using n instead of n−1 for the sample variance or for t degrees of freedom.**
- **Pooling regimes to "get more data"** (fixed + floating FX, low-risk + high-risk manager years, grocery + auto inventory turnover).
- **Presenting only the significant variables** from a large search, without reporting how many were tried.
- **Backtesting on today's index constituents or currently-live funds** (survivorship) or on year-end fundamentals assumed available at year-end (look-ahead).
- **Assuming "n ≥ 30" guarantees normality** of the sample mean for heavily skewed data.
- **Calling a non-random stratified bond sample a basis for population inference**: fine for index replication, not for parameter estimation.

## Exam Focus & Traps
- **Standard error of the mean is σ/√n, not σ/n and not the SD of the data.** Use s if σ is unknown.
- **Which statistic?** Known variance means z. Unknown variance means t (small sample needs normality). Non-normal + small sample + unknown variance = nothing available. Non-normal + large sample: z or t.
- **df = n−1** for a single-mean t interval and for the variance; the t-table's closest row may be used (df 99 ≈ 100).
- **t is wider than z for the same α**, and a higher confidence level or lower n widens the interval.
- **Estimator properties**: unbiased = E(estimator) = parameter; efficient = smallest variance among unbiased; consistent = concentrates as n→∞. s² with divisor n is biased.
- **Stratified sampling** gives greater precision than simple random sampling and guarantees subgroup representation; cell count = product of category counts (multiplication rule).
- **Bias labels**: "excludes failed funds" = survivorship (a form of sample selection bias); "uses data not yet published" = look-ahead; "tests many variables" = data mining; "short window" = time-period bias. Remedy for data mining = out-of-sample test.
- **Time series vs cross-sectional**: Quarterly returns of one fund = time series; P/B of all NYSE stocks at year-end = cross-section; Eurozone inflation over 5 years = panel.
- **Table rounding**: z.05 = 1.65 in this reading, 1.645 in hypothesis testing; 99% uses 2.58 here and 2.575 there. Pick the nearest answer option.

## Key Takeaways
1. Sample statistics are random variables; the standard error s/√n measures their noise, and the CLT makes X̄ approximately normal for n ≈ 30+ regardless of the population shape.
2. Confidence interval = point estimate ± reliability factor × standard error; wider for higher confidence, smaller n, or larger s.
3. Use z only if σ is known (or as the large-sample alternative); otherwise t with n−1 df, which converges to z as df grows.
4. A good estimator is unbiased, efficient and consistent; divisor n−1 makes the sample variance unbiased.
5. Stratified random sampling beats simple random sampling for precision and representation (bond-indexing cells).
6. More data helps only if it comes from one population; check homogeneity before pooling.
7. Four biases wreck inference before any test is run: data mining, sample selection (survivorship), look-ahead, time period; out-of-sample testing and an economic rationale are the defences.

## Connects To
- **ch 04**: normal and uniform distributions behind the CLT and z-factors; Monte Carlo as the simulation view of sampling distributions.
- **ch 02**: sample mean, variance, standard deviation and the Sharpe ratio are the statistics whose sampling error is quantified here.
- **ch 03**: expected value, variance and the multiplication rule (stratum counts).
- **ch 06**: the same standard errors and t/z factors turn into test statistics; a two-sided test at α equals a (1−α) confidence interval check; data-mining multiple testing builds on significance levels.
- **ch 07 / ch 08**: regression coefficient inference uses t with df = n−k−1 and the same interval structure.
- **ch 09**: stationarity and mixed regimes (time-series data).
- **`cfa-portfolio-management` ch 03**: market-efficiency anomalies are exactly what data mining, survivorship and look-ahead bias fabricate.
- **`cfa-portfolio-management` ch 14**: backtesting and simulation (L2) apply the out-of-sample discipline from this chapter.
