# Chapter 7: Empirical Results on Euro Area Government Bonds
> **Source**: ECB Statistics Paper No 27 (2018), §6 (6.1-6.5), Tables 6-8, Charts 14-19, Appendix 4 summary | Nymand-Andersen

## Core Idea
On a clean sample of about 318 euro area government bonds per day (April 2003 to March 2005), all four models (Nelson-Siegel, Svensson, Waggoner step penalty, VRP) fit within a few basis points, in and out of sample. Differences appear only at the extremes: Svensson is slightly better than Nelson-Siegel, splines fit marginally closer but become erratic and volatile at 10-30 years, and parsimonious models are sensitive to starting values. The very good results partly reflect data quality and a calm period.

## Frameworks Introduced
- **Four-model scorecard** (same sample, same tests; see ch06 for the protocol):
  - When to use: as the benchmark of what "good" looks like for a government curve fit.
  - How: compare WMAE, RMSE, hit rate by maturity bracket, then robustness and smoothness plots.
  - Failure mode: reading the ranking as general; it comes from a stable two-year window with one rate cut.
- **Error profile by maturity**: errors are lowest in the medium bracket (about 2.3 bp WMAE) and rise at short and especially long maturities.
- **Hybrid selection statistic**: Banque de France chose Svensson on 405 of 502 days (above 80%), i.e. a second hump was statistically justified most of the time, yet N&S and Svensson fits were almost identical.
- **Spread-volatility diagnostic**: spreads that include the 3-month point or the 30-year point are more volatile in every model; VRP shows abrupt breaks above 10 years.
- **Visual-inspection check**: animated daily curves revealed spline 30-year yields swinging between about 6% and 5% in opposite directions on dates where the data did not support it.

## Key Concepts
- **In-sample WMAE ranges**: parsimonious models 1.8-5.3 bp for all maturities (N&S 4.1-5.3, Svensson 3.7-4.1); splines 3.3-4.5 bp (RMSE 6.1-9.0 bp).
- **Out-of-sample ranges (Table 8)**: WMAE 3.4-5.4 bp, RMSE 5.0-7.2 bp, slight rise in the 20-30 year bracket (except hybrid).
- **Hit rates at ±1.5 bp**: N&S and Svensson 11-16% overall; hybrid about 40% (above 90% for 3m-1y); Waggoner about 13%; VRP about 29%, but only 4-5% above 10 years because of heavy smoothing.
- **Hit rate vs band**: Svensson 72% at ±3 bp and 98% at ±5 bp.
- **Parameter similarity**: N&S and Svensson parameters differ only at the third decimal (Table 6, ch03).
- **Sensitivity to rates**: Svensson reacts more to interest-rate changes than N&S in the literature; not visible in this calm sample.
- **Over-parameterisation**: several parameter sets give nearly the same curve.
- **Starting-value and algorithm sensitivity**: observed for both parsimonious models.
- **Minimum support**: B-spline locality makes Waggoner more stable to small price changes.
- **Smoothing-parameter optimum**: L = 100,000, S = 0.1, μ = 1 for VRP.
- **Maximum maturity drift**: the longest bond maturity often fell below 30 years, offered as a reason for long-end instability.
- **Spline model-factor list**: optimisation algorithm, smoothing parameters, penalty function, knot points.

## Formulas & Reference Tables
| Result (ECB sample) | N&S | Svensson | Hybrid (BdF) | Waggoner | VRP |
|---|---|---|---|---|---|
| In-sample WMAE, all maturities (bp) | 4.1-5.3 | 3.7-4.1 | lowest | 3.3-4.5 (both splines) | 3.3-4.5 |
| Hit rate overall (±1.5 bp) | 11-16% | 11-16% | about 40% | about 13% | about 29% |
| Hit rate above 10y | n/a | n/a | above 10% | n/a | 4-5% |
| Long-end smoothness | volatile spreads incl. 3m and 30y | same | n/a | smoother | most volatile with 30y |
| Sensitivity | starting values, algorithm | starting values, algorithm | rule on β₃ | knots, penalty, algorithm | same, plus L, S, μ |

| Maturity bracket | Typical error pattern |
|---|---|
| 3m-1y | Highest dispersion of yields; hybrid hit rate above 90% |
| 1-10y | Lowest errors (WMAE about 2.3 bp) |
| 10-30y | Errors rise; spline curves erratic |

- Daily comparison statistic: `Spread(t) = RMSE[N&S](t) − RMSE[Svensson](t)`; mostly positive across the two years, but values are tiny and not conclusive.
- Dataset: 502 TARGET days, 286 in-sample + 32 out-of-sample bonds on average.

## Mental Models
- **Quality of data explains the quality of fit**: a large, filtered sample gave better statistics than the literature; do not credit the model alone.
- **Calm sample, weak discrimination**: with one rate cut in two years, models could not be separated; stress periods are where Svensson's extra flexibility would show.
- **Ends are where models differ**: below 1 year and above 10 years.
- **Splines win the in-sample lap, lose the credibility lap**: tiny extra accuracy bought with erratic long maturities.

## Worked Example
Hit-rate sensitivity to the band (reported ECB numbers for Svensson): ±1.5 bp gives 11-16%; ±3 bp gives 72%; ±5 bp gives 98%.
Reading: yield dispersion around the curve is a few bp, so a 1.5 bp band is simply tighter than the data's noise (WMAE of 3.7-4.1 bp). A reasonable operating band is 3-5 bp. Check: with WMAE around 4 bp and errors roughly bell-shaped, a ±1.5 bp band should capture on the order of a quarter or less of observations, consistent with 11-16%.
Model comparison logic: N&S WMAE 4.1-5.3 bp versus Svensson 3.7-4.1 bp is a gap of roughly 0.4-1.2 bp: statistically small, so the decision rests on robustness and communication (ch08).

## Anti-patterns
- **Declaring a winner from insignificant gaps**: differences of 0.5-1 bp WMAE are not conclusive.
- **Generalising a calm two-year result to turbulent regimes** or to the zero lower bound (not tested; flagged for research).
- **Trusting hit rate at long maturities**: low hit rate says nothing about how far the miss is, and visual plots disagree.
- **Fitting 3-month to 30-year spreads and treating volatility as signal**: it is mostly edge-of-sample noise.
- **Optimising smoothing parameters on the evaluation data without noting it**: the VRP combination was chosen as best on this same dataset.

## Practitioner Notes
- Svensson was consistently (but insignificantly) better than N&S, in and out of sample and in each sub-period; the hybrid had the best goodness of fit.
- Parsimonious models were reasonably robust; Waggoner is likely more stable to small price changes than VRP thanks to minimum support.
- Spline long-end behaviour was unexpected and not confirmed by similar studies; the paper offers a time-varying maximum maturity as a possible reason.
- Further research asked for: effect of starting values and algorithm on parsimonious models; calibration of knots, penalty and smoothing parameters; zero lower bound performance.
- Volatility of 10y-3m spreads: yields of the shortest maturities are noisy, so many practitioners lower-bound the sample at 3 months (ch05).

## Key Takeaways
1. All four models fit euro area government bonds to a few bp, in and out of sample.
2. Svensson slightly beats N&S; the hybrid does best on fit statistics.
3. Splines fit slightly closer in sample but are volatile and erratic at 10-30 years (VRP worst).
4. Parsimonious models are robust to local shocks but sensitive to starting values and algorithm.
5. Spline results depend heavily on algorithm, smoothing parameters, penalty and knots.
6. Data quality and a calm sample likely drive the exceptional statistics.
7. Always read hit rates with their band and cross-check visually.

## Connects To
- **ch06**: the protocol and formulas behind these numbers.
- **ch02**, **ch03**: model mechanics (penalties, N&S/Svensson forms).
- **ch05**: data quality that drove the fit.
- **ch08**: how the evidence became a model choice and ECB settings.
- **`tuckman-fixed-income` ch21**: fitting error versus smoothness in curve construction.
- **`ilmanen-yield-curve`**: interpreting slope and forward-curve changes.
