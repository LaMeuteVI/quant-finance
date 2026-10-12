# Chapter 2: Statistical Concepts and Market Returns
> **Source**: CFA Program Curriculum 2020, Level I, Reading 7 · Quantitative Methods | DeFusco, McLeavey, Pinto, Runkle

## Core Idea
Descriptive statistics compress a return history into four properties: where it is centered (mean, median, mode), how dispersed it is (variance, standard deviation, MAD), whether it is lopsided (skewness) and whether the tails are fat (kurtosis). Choosing the right statistic matters: geometric mean for past compound performance, arithmetic mean for a one-period forward-looking estimate, median for skewed or outlier-prone data, and Chebyshev's bound when the distribution shape is unknown.

## Learning Outcomes Covered
- distinguish descriptive vs inferential statistics, population vs sample, and the four measurement scales
- define parameter, sample statistic, frequency distribution; compute relative and cumulative relative frequencies
- describe histogram and frequency polygon properties
- calculate and interpret arithmetic, weighted, geometric and harmonic means, median and mode
- calculate quartiles, quintiles, deciles, percentiles
- calculate range, MAD, population and sample variance and standard deviation
- apply Chebyshev's inequality; calculate the coefficient of variation
- explain skewness; locate mean, median, mode in skewed unimodal distributions
- explain sample skewness and kurtosis; compare arithmetic and geometric means for returns

## Frameworks Introduced
- **Four measurement scales (weakest to strongest)**: nominal (categories, no order), ordinal (ordered, gaps unequal), interval (equal gaps, no true zero), ratio (true zero, ratios meaningful).
  - When to use: to decide which statistic is legitimate. The mode is the only central-tendency measure valid for nominal data; credit ratings and star ratings are ordinal; returns, prices, dividends, maturities are ratio.
- **Frequency distribution construction (7 steps)**: sort ascending; range = max − min; choose k intervals; width = range/k (round up); build interval endpoints from the minimum; count observations; tabulate.
  - How: intervals are non-overlapping, lower limit inclusive and upper limit exclusive except the last. Too few intervals hides the tails, too many leaves empty bins; a risk manager keeps a large k to see tail detail.
  - Derived columns: absolute frequency, relative frequency (frequency/total), cumulative relative frequency (fraction below each upper limit).
- **Choosing a measure of central tendency**:
  - Arithmetic mean: use all data, symmetric data without outliers, one-period expected return.
  - Median: skewed data or outliers (e.g. P/E of a portfolio, industry multiples).
  - Mode: nominal data, or to name the modal interval of a histogram.
  - Weighted mean: portfolios and indexes (weights sum to 1; a short position has a negative weight; equal weights give the arithmetic mean).
  - Geometric mean: compounded growth or multi-period historical return.
  - Harmonic mean: a fixed amount of money repeatedly invested at varying prices per unit (cost averaging).
  - Ordering when observations are not all equal: `harmonic < geometric < arithmetic`.
- **Percentile location and interpolation**: position `L_y = (n + 1) × y/100`; if L_y is an integer take that observation; otherwise interpolate linearly between the two bracketing sorted values.
- **Dispersion toolkit**: range (two points only), MAD (all points, not tractable), variance and standard deviation (tractable, enter the Sharpe ratio, beta, portfolio variance), semivariance and target semivariance (downside only, no clean portfolio algebra).
- **Chebyshev's inequality**: for any distribution with finite variance, at least `1 − 1/k²` of observations lie within k standard deviations of the mean, for k > 1.
  - When to use: shape unknown or non-normal. It gives only a minimum; it never gives a maximum.
- **Coefficient of variation**: relative dispersion, scale-free; use to compare variability across series with different means or units. For returns it is risk per unit of mean return.
- **Normal vs non-normal check**: skewness near 0 and excess kurtosis near 0 are consistent with normal. Rule of thumb for n ≥ 100: skewness beyond ±0.5 or excess kurtosis above 1.0 is unusually large. Jarque-Bera: `JB = n[SK²/6 + KE²/24]`; JB ≥ 6 (n ≥ 30) rejects normality at about the 5% level.
- **Geometric vs arithmetic use rule**: historical multi-period performance, use geometric; expected one-period return and discounting uncertain flows, use arithmetic; graph past performance on a semilogarithmic scale (constant compound growth plots as a straight line).

## Key Concepts
- **Descriptive vs inferential statistics**: summarizing observed data vs making estimates about a larger group from a sample.
- **Population / parameter**: all members of a group / a descriptive measure of that population (μ, σ²).
- **Sample / statistic**: a subset of a population / a measure computed from a sample (X̄, s²).
- **Holding period return**: `(P_t − P_{t−1} + D_t)/P_{t−1}`; carries a time unit but no currency unit.
- **Cross-sectional vs time-series mean**: average across units at one date vs average of one unit over time.
- **Trimmed mean / Winsorized mean**: mean after dropping, or capping at percentile values, a stated tail share of the data.
- **Modal interval**: the highest bar of a histogram of continuous data; unimodal, bimodal, trimodal describe the number of modes.
- **Quantile**: a value below which a stated fraction of data lies (quartile, quintile, decile, percentile); Q1 = P25, Q2 = median = P50, Q3 = P75.
- **Interquartile range (IQR)**: `Q3 − Q1`, the span of the middle 50% of observations.
- **Degrees of freedom (n − 1)**: after the sample mean is fixed only n − 1 deviations are free; dividing by n − 1 makes s² an unbiased estimator of σ².
- **Semideviation**: square root of the average squared shortfall below the mean (or target B), divided by n − 1.
- **Skewness**: standardized average cubed deviation; positive = long right tail (frequent small losses, rare big gains), negative = long left tail.
- **Kurtosis / excess kurtosis**: tail weight; normal = 3, excess = kurtosis − 3; leptokurtic (> 0, fat tails), mesokurtic (= 0), platykurtic (< 0).
- **Frequency polygon / cumulative frequency distribution**: line graph of interval midpoints vs frequency / graph of cumulative counts whose slope tracks interval frequency.
- **Compound return**: another name for the geometric mean return.

## Formulas & Reference Tables
Symbols: Xᵢ observation, n sample size, N population size, μ population mean, X̄ sample mean, s sample standard deviation, R_t holding period return, B target.

| Statistic | Formula |
|---|---|
| Holding period return | `R_t = (P_t − P_{t−1} + D_t)/P_{t−1}` |
| Population mean | `μ = ΣXᵢ/N` |
| Sample mean | `X̄ = ΣXᵢ/n` (deviations always sum to 0) |
| Weighted mean | `X̄_w = Σwᵢ Xᵢ`, `Σwᵢ = 1` |
| Geometric mean (Xᵢ ≥ 0) | `G = (X₁X₂…Xₙ)^(1/n)` |
| Geometric mean return | `R_G = [Π(1 + R_t)]^(1/T) − 1` |
| Harmonic mean (Xᵢ > 0) | `X̄_H = n / Σ(1/Xᵢ)` |
| Percentile position | `L_y = (n + 1)·y/100` |
| Interpolation | `P_y ≈ X_i + (L_y − i)(X_{i+1} − X_i)`, i = integer part of L_y |
| Median position | odd n: `(n + 1)/2`; even n: mean of items n/2 and (n + 2)/2 |
| Range | `max − min` |
| MAD | `Σ|Xᵢ − X̄|/n` |
| Population variance / SD | `σ² = Σ(Xᵢ − μ)²/N`, `σ = √σ²` |
| Sample variance / SD | `s² = Σ(Xᵢ − X̄)²/(n − 1)`, `s = √s²` |
| Semivariance (approx.) | `Σ_{Xᵢ ≤ X̄}(Xᵢ − X̄)²/(n − 1)` |
| Target semivariance | `Σ_{Xᵢ ≤ B}(Xᵢ − B)²/(n − 1)` |
| Chebyshev | share within `X̄ ± ks` ≥ `1 − 1/k²` |
| Coefficient of variation | `CV = s/X̄` |
| Sample skewness | `SK = [n/((n−1)(n−2))] · Σ(Xᵢ − X̄)³/s³` ; large n: `≈ (1/n)Σ(Xᵢ − X̄)³/s³` |
| Sample excess kurtosis | `K_E = [n(n+1)/((n−1)(n−2)(n−3))]·Σ(Xᵢ − X̄)⁴/s⁴ − 3(n−1)²/((n−2)(n−3))` ; large n: `≈ (1/n)Σ(Xᵢ−X̄)⁴/s⁴ − 3` |
| Geometric ≈ arithmetic | `R_G ≈ R_A − σ²/2` |
| Pearson skewness (footnote) | `3(mean − median)/s` |

Chebyshev table (minimum share within k standard deviations):

| k | 1.25 | 1.5 | 2 | 2.5 | 3 | 4 |
|---|---|---|---|---|---|---|
| Minimum share | 36% | 56% | 75% | 84% | 89% | 94% |

Normal distribution: mean = median, fully described by mean and variance, about 68% / 95% / 99% within ±1 / ±2 / ±3 standard deviations (more precisely 68.3% / 95.5% / 99.7%).

Relative location in unimodal skewed distributions: positive skew, `mode < median < mean`; negative skew, `mean < median < mode` (dictionary-order mnemonic).

S&P 500, 1926-2017 (nominal): annual geometric 10.16%, arithmetic 12.06%, SD 19.79%, skewness −0.40, excess kurtosis 0.10; monthly geometric 0.81%, arithmetic 0.95%, SD about 5.4%, skewness +0.34, excess kurtosis 9.77. The normal fits annual returns far better than monthly ones, and skewness and kurtosis depend on the holding period.

## Mental Models
- **Mean = reward, dispersion = risk, skewness and kurtosis = the shape of the surprise.** Mean and SD alone are blind to whether the big deviations are gains or losses and whether they are frequent.
- **Mean follows the outliers, median ignores them.** One P/E of 143 in a seven-stock book moves the mean to 36.6 while the median stays at 22.95; analysts therefore characterize industry multiples by medians.
- **Arithmetic mean answers "what will a typical single year be?"; geometric mean answers "what did my money compound at?"** Volatility drag: `R_G ≈ R_A − σ²/2`, so more volatility widens the gap between them.
- **Chebyshev is the distribution-free safety net.** It is loose (75% within 2 SD) compared with the normal (95%), so use the normal only when it is justified.
- **Fat tails make normal models underestimate extremes.** Positive excess kurtosis means very bad outcomes occur more often than the bell curve says (October 1987 was about 20 daily standard deviations away).
- **Harmonic mean is for "fixed amount per period" averaging.** Investing a constant 1,000 at prices 10 and 15 buys at an average price of 12, below the 12.5 arithmetic average.

## Worked Example
**A. Mean, geometric mean, dispersion for two funds (annual returns, %).** Fund A: 34.90, 6.13, 2.69, 11.66, 21.77. Fund B: 31.69, 7.75, −7.56, 18.25, 16.18.
- Arithmetic mean: A 15.43, B 13.26.
- Geometric mean: A `(1.3490·1.0613·1.0269·1.1166·1.2177)^(1/5) − 1 = 14.86%`; B 12.50%. Gap 0.57 vs 0.76 points; B is more volatile so its gap is larger.
- Sample SD: A 13.06 (variance 170.57), B 14.46 (variance 209.23). MAD: A 10.32, B 10.53. Range: A 32.21, B 39.25. MAD < SD always.
- CV (SD/mean): A 0.85, B 1.09. B bears more risk per unit of return.
- Semideviation of A about its mean: below-mean returns 2.69, 6.13, 11.66; semivariance `(162.31 + 86.49 + 14.21)/4 = 65.75`, semideviation 8.1% (vs SD 13.1%). Target semideviation at 11.5%: `(77.6 + 28.8)/4 = 26.61`, giving 5.2%.
Interpretation: B ranks riskier on every measure; downside-only measures say A's risk is lower than its SD suggests because its dispersion is dominated by upside.

**B. Skewness and kurtosis of a 10-year fund record.** Returns: −35.75, 25.62, 15.15, −0.72, 17.25, 31.69, 7.75, −7.76, 18.25, 16.18. Mean 8.77, s 19.47. `SK = [10/(9·8)]·(−74,659.5)/19.47³ = −1.40` (large negative: 2008 crash). `K_E = [110/(9·8·7)]·(4,385,716/19.47⁴) − 3(81)/(8·7) = 6.66 − 4.34 = 2.32`, leptokurtic. Negative skew with fat tails: Jarque-Bera not applicable here (n < 30), but treat the normal as a poor fit.

**C. Chebyshev on monthly S&P 500.** Mean 0.95%, SD 5.39%, n = 1,104. At least 75% lie in `0.95 ± 10.78 = [−9.83%, 11.73%]`, so at least 828 observations; the actual count in the nearby intervals is about 96%, consistent with the bound.

**D. Percentile.** Sorted European returns, n = 15; P60 position `16 × 0.60 = 9.6`, between 6.81 and 7.20: `6.81 + 0.6 × 0.39 = 7.04`.

## Anti-patterns
- **Reporting the arithmetic mean as the compound return**: a +100% year then −50% averages +25% but earns 0%; always report the geometric mean for realized multi-period performance.
- **Using mean P/E of a portfolio or sector**: outliers distort it; use the median or a harmonic mean of multiples.
- **Dividing by n for a sample variance**: use n − 1, or s² is biased low. Use σ² (divide by N) only for a genuine full population.
- **Applying normal-distribution intervals to fat-tailed data**: monthly equity returns have excess kurtosis near 10; use Chebyshev or a fat-tailed model.
- **Comparing standard deviations across series with different means**: use CV (CV is meaningless when the mean is near zero or negative).
- **Treating ordinal data (ratings) as interval**: averaging star ratings or credit ratings assumes equal gaps that do not exist; use the median or mode.
- **Reading "75% within 2 SD" as the exact share**: Chebyshev is a minimum, not an expectation.
- **Using excess kurtosis and raw kurtosis interchangeably**: Excel and some packages label excess kurtosis as "kurtosis"; check the definition (normal = 3 vs 0).
- **Averaging growth over different horizons**: monthly and annual return distributions are not comparable (monthly values are smaller on average).

## Exam Focus & Traps
- Always `harmonic ≤ geometric ≤ arithmetic`; equality only when all observations are identical.
- Geometric mean needs `1 + R` (never raw returns); the final answer subtracts 1.
- Mean, median, mode order: positive skew mode < median < mean; negative skew mean < median < mode.
- Positive skew: frequent small losses, rare large gains. Negative skew: frequent small gains, rare large losses.
- Sample SD uses n − 1 (calculator "sx"); population SD uses N ("σx"). Check which the question describes.
- Median of an even sample is the average of the two middle items; the percentile formula uses (n + 1), not n.
- Quintile count: there are four cut points (P20, P40, P60, P80) defining five groups; similarly three quartile cut points.
- Chebyshev gives a lower bound valid for any shape, with k > 1; it does not state a maximum.
- Weighted average of returns requires weights summing to 1; if a portfolio is rebalanced to constant weights, compute each period's weighted return, not the arithmetic mean of fund returns.
- Sample skewness and excess kurtosis have small-sample correction factors; large-n shortcuts are approximations.
- Forward-looking return (expected single-period) uses the arithmetic mean; long-horizon wealth uses the geometric. Equity risk premium forecasts use arithmetic means.
- Population mean is a parameter; sample mean is a statistic (a classic definitional question).

## Key Takeaways
1. Match the average to the question: geometric for past compound growth, arithmetic for expected one-period return, median for skewed data, harmonic for equal-money averaging.
2. Report mean together with dispersion; add CV when means differ, semideviation when downside matters.
3. Use `n − 1` for sample variance, and remember MAD ≤ SD.
4. Chebyshev's `1 − 1/k²` holds for any distribution; the normal's 68/95/99 only for normal data.
5. Skewness sign shows which tail is long; excess kurtosis > 0 means fat tails and underestimated extremes under normal assumptions.
6. `R_G ≈ R_A − σ²/2`: volatility erodes compound growth.
7. Percentiles need the (n + 1)y/100 rule plus linear interpolation; frequency tables should balance detail and clarity, with extra tail detail for risk work.
8. Check the measurement scale before computing any statistic.

## Connects To
- **ch 01**: the compound growth rate there is a geometric mean; TVM uses the same compounding logic.
- **ch 03**: expected value is a probability-weighted mean; portfolio variance requires covariance and correlation.
- **ch 04**: the normal and lognormal distributions formalize the 68/95/99 rule and skew in returns.
- **ch 05**: sample mean, standard error, and the use of n − 1 in estimation and confidence intervals.
- **ch 06**: tests on mean and variance build on the sample statistics defined here.
- **`cfa-portfolio-management` ch 05**: portfolio return and risk, Sharpe ratio `(R_p − R_f)/σ_p` (e.g. (12% − 3%)/20% = 0.45), and the mean-variance framework.
- **`cfa-portfolio-management` ch 13**: VaR depends on the fat-tail and skew issues described here.
