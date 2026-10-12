# Chapter 6: Testing Framework and Evaluation Criteria (In/Out-of-Sample, Error Statistics)
> **Source**: ECB Statistics Paper No 27 (2018), §5 (5.1-5.4), Appendix 1 (error statistics), Box on statistical tests, Table 5 | Nymand-Andersen

## Core Idea
A yield-curve model must be judged by one common protocol: the same clean bond sample, an in-sample and a held-out out-of-sample population, several market regimes, and three separate criteria (flexibility and goodness of fit, robustness, smoothness). In-sample fit alone always flatters flexible models (splines fit "with arbitrary precision"), so out-of-sample accuracy, stress tests on prices and visual inspection are the referees.

## Frameworks Introduced
- **In-sample / out-of-sample split (1 bond in 10)**:
  - When to use: any model comparison or model validation of a curve estimator.
  - How: rank all bonds of the cleaned sample by ascending residual maturity (3 months to 30 years); put every 10th bond in the out-of-sample set; fit the curve on the rest; price the held-out bonds off the fitted curve and compare errors with in-sample errors.
  - Why it works: the held-out bonds cover every maturity bracket yet are too few to move the curve. ECB sample: about 286 in-sample and 32 out-of-sample bonds per day (318 total).
  - Weighting rule: emphasise flexibility, then weight in-sample statistics more; emphasise robustness, then weight out-of-sample more.
- **Five test periods (market regimes)**:
  1. Full two years (1 Apr 2003 to 31 Mar 2005, 502 days).
  2. 1-7 June 2003: strong rate-cut expectations (ECB cut 2.50% to 2.00% effective 6 June 2003).
  3. 15 Nov 2004 to 31 Jan 2005: euro rally, hawkish ECB talk, expected 25 bp hike that did not happen, flattening curve (expectations wrong).
  4. 1 Feb to 31 Mar 2005: credit-spread widening (GM/Ford downgrades), Stability and Growth Pact reform, French referendum.
  5. Five single days with the biggest day-on-day slope changes (12 Aug 2003, 9 Dec 2003, 22 Jun 2004, 21 Sep 2004, 15 Mar 2005).
  - When to use: models can behave asymmetrically in hike, cut, stable or high-volatility regimes; test each separately.
- **Three evaluation criteria** (all models face identical tests):
  1. **Flexibility and goodness of fit**: does the curve track short-end bends and price bonds not used in the fit? Measured by RMSE, MAE, WMAE and hit rate, in and out of sample.
  2. **Robustness**: perturb bond prices marginally and measure how the curve moves; a local shock at one maturity must not distort other maturities, a global shock must pass through proportionately.
  3. **Smoothness**: study spreads between maturities (e.g. 10y-2y, 10y-3m, 30y-10y) over time; abrupt breaks that the market slope cannot explain signal a non-smooth model.
- **Visual inspection as a mandatory step**: statistics (especially hit rate, which is binary) can hide odd long-end behaviour; animate daily curves over the sample.
- **Models in the contest (Table 5)**: Nelson-Siegel and Svensson (parsimonious; Bundesbank, Banque de France, Bank of Greece), Waggoner step-wise penalty (Bank of Greece, Bank of England), Waggoner with continuous variable roughness penalty VRP (Bank of England). Waggoner estimated by yield minimisation, VRP by price weighted by duration.

## Key Concepts
- **Residual**: observed yield minus fitted yield for a bond; consistent, small residuals mean an appropriate model.
- **Diagnostic check**: statistical test of how well a model predicts observed values (goodness of fit).
- **WMAE (weighted mean absolute error)**: mean absolute yield error with each term scaled by 1/√duration so that sparse long-maturity observations are deflated.
- **RMSE**: root of the mean squared yield error; always at least as large as MAE, penalises big misses.
- **Hit rate**: share of observed yields within a fixed band around the curve; binary, so blind to how far outside the band a miss is.
- **Out-of-sample test**: whether the curve prices bonds excluded from estimation.
- **Robust**: not sensitive to small data changes, outliers or small departures from assumptions.
- **Smooth**: no abrupt breaks in maturity spreads over time; variation in spreads reflects slope changes.
- **Hybrid model (Banque de France)**: Svensson when β₃ is inside its confidence interval, otherwise Nelson-Siegel.
- **Yield minimisation vs price minimisation**: objective function on yield errors versus price errors (price errors weighted by 1/duration² are approximately yield errors).
- **Knot placement rule**: equal number of bonds maturing between knots (Bank of Greece: a knot about every sixth bond), not every 3-4 bonds.
- **Over-parameterisation**: several parameter sets describe nearly the same curve.

## Formulas & Reference Tables
For day k, bonds i = 1..N, observed yield yᵢ,ₖ, fitted yield ŷᵢ,ₖ, duration Dᵢ,ₖ:
- `RMSEₖ = √[ Σᵢ (yᵢ − ŷᵢ)² / N ]`
- `MAEₖ = Σᵢ |yᵢ − ŷᵢ| / N`
- `WMAEₖ = Σᵢ ( |yᵢ − ŷᵢ| / √Dᵢ ) / N`
- `Hit rateₖ = #{ i : |yᵢ − ŷᵢ| ≤ band } / N`
- Daily model comparison spread: `Spreadₜ = RMSE[model A](t) − RMSE[model B](t)`; positive means B has the lower error that day.
- Spline objectives for reference: yield fit `min Σ(yᵢ−ŷᵢ)² + ∫λ(m)[f″(m)]²dm`; price/duration fit `min Σ((Pᵢ−Πᵢ)/Dᵢ)² + ∫λ(m)[f″(m)]²dm` (ch02).
- ⚠ Source inconsistency: the Appendix 1 hit-rate formula shows a threshold of 0.03 (percentage points, i.e. 3 bp), while the §6.1 text and the reported results use ±1.5 bp. Treat the band as a parameter you declare (the ECB reports 1.5, 3 and 5 bp variants). The appendix also writes the WMAE weight as dividing by √D; the footnote describes it as the "inverse of the square root of duration" as weighting factor, which is the same thing.

| Criterion | Question | Statistic | Pass signal |
|---|---|---|---|
| Flexibility / fit (in-sample) | Does the curve follow the data? | WMAE, RMSE, hit rate | Low errors, no systematic bracket bias |
| Flexibility / fit (out-of-sample) | Does it price unseen bonds? | Same, held-out bonds | Close to in-sample numbers |
| Robustness | Local shock stays local? | Curve before/after bump | Local effect small, global proportionate |
| Smoothness | Any unexplained breaks? | Spread time series (10y-2y, 30y-10y, 10y-3m) | No abrupt jumps unrelated to market |

## Mental Models
- **In-sample fit is a necessary, not sufficient, test**: more parameters always lower it; out-of-sample is the fair judge.
- **Hit rate answers "how many", RMSE answers "how far"**: use both; a model can have a poor hit rate yet small misses, or the reverse.
- **Weight by duration to deflate sparse zones**: 10-30 year data are thin, so yield errors there are scaled down by √D.
- **A curve is a time series**: plot spreads through time; a break that is not a market event is a model artefact.
- **Regime stress**: a model that passes only in quiet markets has not been tested.

## Worked Example
Five bonds on one day (illustrative, recomputed): observed vs fitted yields (%) 3.10/3.11, 3.12/3.115, 3.08/3.09, 3.15/3.14, 3.20/3.17; durations 0.5, 1.2, 3.8, 7.5, 15.0.
Errors (bp): −1, +0.5, −1, +1, +3.
- MAE = (1+0.5+1+1+3)/5 = 1.30 bp.
- RMSE = √((1+0.25+1+1+9)/5) = 1.57 bp.
- WMAE = (1/√0.5 + 0.5/√1.2 + 1/√3.8 + 1/√7.5 + 3/√15)/5 = 0.70 bp: the 3 bp miss on the 15-year bond counts for only 0.77 bp because of the duration weight.
- Hit rate at ±1.5 bp = 4/5 = 80%; at ±3 bp = 100%.
Interpretation: RMSE (1.57) exceeds MAE (1.30) because of the single large miss; the WMAE is the lowest because the miss sits at long duration. The hit rate tells you four fits were tight but not that the fifth was 3 bp away.

## Anti-patterns
- **Ranking models on in-sample RMSE only**: splines win by construction (Bliss 1996).
- **Using a hit-rate band without reporting it**: 1.5 bp gave 11-16% hits for N&S and Svensson while the same Svensson model reaches 72% at 3 bp and 98% at 5 bp.
- **Testing one calm period only**: the two-year sample had a single policy cut; results may not generalise (ch07).
- **Different samples or objectives across models**: comparisons then reflect data and implementation, not model quality.
- **Skipping the plot**: statistical tests said spline curves were fine while daily plots showed erratic 10-30 year behaviour.
- **Knot rule borrowed from small national samples**: clusters knots in a euro-area-sized sample.

## Practitioner Notes
- The ESCB team ran the identical sample and tests across five central banks (Greece, England, Italy, France, Germany); the same model differed between banks in curve type, objective, constraints, starting values and algorithm, so exact replication needs these documented.
- Robustness was illustrated on 15 June 2004 with three shocks: a 15 bp parallel shift ("brute"), a 3-standard-deviation shift on a single 1-year bond ("regional"), and +30 bp below one year / +20 bp above ("shift"). The hybrid model followed the global move and absorbed the local bump.
- Smoothness charts to build: 2y-3m, 10y-3m, 10y-2y, 10y-5y, 30y-10y, for both spot and forward. Spreads including the 3-month point are noisier for every model.
- Descriptive statistics of the sample come before any fitting (ch05).

## Key Takeaways
1. Hold out 1 bond in 10, ranked by maturity, and always report in- and out-of-sample errors.
2. Use three criteria: fit and flexibility, robustness, smoothness; same data and tests for every model.
3. Report WMAE, RMSE and a hit rate with its band stated.
4. Test across rate-cut, rate-hike, credit-stress and big-slope-move periods, not only the full sample.
5. Shock the data (global and local) and check that local shocks stay local.
6. Plot maturity spreads over time to spot breaks; always inspect daily curves visually.
7. Document objective, constraints, starting values, algorithm, knot rule.

## Connects To
- **ch05**: producing the clean sample these tests rely on.
- **ch02**, **ch03**: the models being tested.
- **ch07**: the numerical results of this protocol.
- **ch08**: how test evidence became the ECB's model choice.
- **`tuckman-fixed-income` ch21**: curve fitting and error measures in curve construction.
- **`cfa-fixed-income` ch07**: spot, forward curve concepts behind the fitted objects.
