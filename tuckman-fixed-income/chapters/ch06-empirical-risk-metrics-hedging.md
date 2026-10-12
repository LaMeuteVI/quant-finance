# Chapter 6: Empirical Approaches to Risk Metrics and Hedging
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 6 (Part Two: Measures of Interest Rate Risk and Hedging)

## Core Idea
DV01 hedges (ch04) and key-rate/multi-factor hedges (ch05) silently *assume* how rates at different points move relative to each other (typically one-for-one). This chapter replaces the assumption with **data**: regress yield changes on yield changes to get minimum-variance hedge ratios, or run **principal components analysis (PCA)** to get a small set of uncorrelated factors (level, slope, short rate) that describe the whole curve. The recurring warning is that empirical relationships are **not stable**. A hedge estimated in one regime can fail in the next, and handling that is an art, not a science. Even so, blindly assuming β = 1 (a plain DV01 hedge) is worse.

## Frameworks Introduced
- **Single-variable regression hedge (minimum-variance hedge)**:
  - When to use: hedging a position whose yield does not move one-for-one with the hedge instrument's yield (nominal vs TIPS, off-the-run vs on-the-run, cross-market, swap spread trades).
  - How:
    1. Collect daily **changes** in both yields over a relevant window.
    2. Regress the change in the yield of the position being hedged (dependent) on the change in the hedge yield (independent): `Δyᴺ = α + β·Δyᴿ + ε`.
    3. Hedge face `Fᴿ = −Fᴺ × (DV01ᴺ/DV01ᴿ) × β̂`, i.e. the DV01 hedge scaled by β̂.
    4. Read the hedged P&L volatility off the regression: `σ(P&L) ≈ |Fᴺ| × DV01ᴺ/100 × σ̂`, with σ̂ the standard error of the regression.
    5. Compare that volatility with the expected gain of the trade.
  - Why it works: the β̂ hedge minimizes the in-sample variance of the hedged P&L, because OLS gives `β̂ = Cov(Δyᴿ, Δyᴺ)/V(Δyᴿ)` (Appendix A).
  - Failure mode: β̂ drifts over time (regime changes), and in-sample fit overstates out-of-sample hedge quality.
- **Choice of dependent variable (economic, not cosmetic)**: OLS needs the independent variable to be uncorrelated with the error. Nominal = real + inflation, so in "nominal on real" the error contains inflation changes. The assumption that the real rate is uncorrelated with inflation is tolerable, though not ideal. In "real on nominal" the error (inflation) is certainly correlated with the regressor (the nominal rate), so OLS is biased and you would need instrumental variables. **Put the yield that contains the extra, unhedged component on the left-hand side.**
- **Two-variable regression hedge (10s/30s hedge of 20s)**:
  - When to use: a market maker receives fixed in an illiquid tenor (20-year EUR swaps) and hedges with liquid neighbours (10s and 30s) rather than crossing the bid-ask in the same tenor.
  - How:
    1. Regress `Δy²⁰ = α + β¹⁰Δy¹⁰ + β³⁰Δy³⁰ + ε`.
    2. Set `F¹⁰ = −F²⁰ × (DV01²⁰/DV01¹⁰) × β̂¹⁰` and `F³⁰ = −F²⁰ × (DV01²⁰/DV01³⁰) × β̂³⁰`.
    3. The β̂'s are the **risk weights**: the fraction of the 20-year DV01 put in each hedge.
  - Note: the risk weights need not sum to 100%. A minimum-variance hedge need not be DV01-neutral when rates do not move in parallel.
- **Level vs change regressions (and the AR(1)-error compromise)**:
  - A level regression `yₜ = α + βxₜ + εₜ` implicitly assumes errors are independent, i.e. a mispricing vanishes overnight. That is too fast.
  - A change regression `Δyₜ = βΔxₜ + Δεₜ` implicitly assumes errors are fully persistent, i.e. a mispricing never mean-reverts. That is too slow.
  - Both give unbiased, consistent but **inefficient** coefficients when errors are serially correlated.
  - The more sensible model is the level regression with `εₜ = ρεₜ₋₁ + νₜ`, ρ < 1. The spread then converges partially each day.
- **PCA hedging**:
  - When to use: large portfolios (one regression per security is impractical), butterflies, and any time you want a hedge or risk report in a few uncorrelated empirical factors.
  - How (same mechanics as ch05 multi-factor hedging):
    1. Reprice the portfolio after a one-standard-deviation shift of each PC.
    2. Compute an '01 per PC for the portfolio and for each candidate hedge.
    3. Solve a linear system that sets the net exposure to each hedged PC to zero, using one hedge instrument per PC.
- **Constructing PCs (Appendix B)**:
  - First PC `a` maximizes `a′Va` subject to `a′a = 1`.
  - Second PC `b` maximizes `b′Vb` subject to `b′b = 1` and `b′a = 0`, and so on. These are the eigenvectors of the covariance matrix V, ranked by eigenvalue.
  - Rescale each eigenvector by √(its eigenvalue) so that it reads as the **one-standard-deviation move, in bp, of each rate**.

## Key Concepts
- **Dependent / independent variable**: the yield being explained (the position) vs the explanatory yield (the hedge).
- **β̂ (regression coefficient)**: average bp change in the dependent yield per 1bp change in the independent yield. It is the hedge adjustment to the DV01 ratio.
- **Risk weight**: `−F_hedge × DV01_hedge / (F × DV01)`, the hedge DV01 as a % of the position DV01. For a regression hedge it equals β̂.
- **Standard error of the regression σ̂**: `√(Σε̂²/(n−2))`, the typical daily miss in bp. Multiplied by the position's dollar DV01 it gives the hedged daily P&L volatility.
- **R²**: share of the dependent variable's variance explained. In a one-variable regression R² = ρ², so R² = 56.3% implies a correlation of ≈ 75%.
- **Coefficient standard error / 95% CI**: `β̂ ± 2 × s.e.(β̂)`. If 1 is inside the interval, a DV01 hedge cannot be statistically rejected.
- **In-sample vs out-of-sample errors**: errors inside the estimation window are small by construction. Only out-of-sample errors test stability.
- **Rolling regression**: re-estimating β̂ on a moving window (e.g. 30 days) to see drift or a regime change.
- **Serial correlation**: errors correlated over time. Estimates stay unbiased and consistent but become inefficient.
- **Principal components (PCs)**: uncorrelated linear factors whose total variance equals the total variance of the rates, each chosen to explain the maximum remaining variance.
- **Level / Slope / Short-rate PC**: in USD swaps (2001–2008) the first three PCs. Level: all rates move the same way, humped with a peak near 5 years. Slope: short rates down, long rates up. Third PC: dominated by short-end moves (often mislabelled "curvature").
- **PC volatility vs total volatility**: `√(Σₖ PCₖ(τ)²)` vs the empirical volatility of rate τ. Their ratio (≈ 99%+) measures how much three PCs capture.
- **Butterfly**: receive the body (e.g. 5y) and pay the wings (2y, 10y), or the reverse, a bet on the body cheapening or richening relative to the wings.

## Formulas & Reference Tables
- DV01-neutral hedge: `Fᴿ × DV01ᴿ = −Fᴺ × DV01ᴺ`, so `Fᴿ = −Fᴺ × DV01ᴺ/DV01ᴿ`.
- Regression model: `Δyₜᴺ = α + βΔyₜᴿ + εₜ`. OLS minimizes `Σₜ(Δyₜᴺ − α̂ − β̂Δyₜᴿ)²`.
- OLS slope: `β̂ = Cov(Δyᴿ, Δyᴺ)/V(Δyᴿ)`. Fitted value: `Δŷᴺ = α̂ + β̂Δyᴿ`. Residual: `ε̂ₜ = Δyₜᴺ − Δŷₜᴺ`.
- Regression hedge: `Fᴿ = −Fᴺ × (DV01ᴺ/DV01ᴿ) × β̂`.
  - Risk weight: `−FᴿDV01ᴿ/(FᴺDV01ᴺ) = β̂`.
- Hedged P&L: `−Fᴿ(DV01ᴿ/100)Δyᴿ − Fᴺ(DV01ᴺ/100)Δyᴺ = −Fᴺ(DV01ᴺ/100)(Δyᴺ − β̂Δyᴿ)`.
  - Its volatility: `σ(P&L) ≈ |Fᴺ| × DV01ᴺ/100 × σ̂`.
- Minimum-variance proof (Appendix A): minimize `V = (FᴿDV01ᴿ/100)²V(Δyᴿ) + (FᴺDV01ᴺ/100)²V(Δyᴺ) + 2(FᴿDV01ᴿ/100)(FᴺDV01ᴺ/100)Cov`. Setting `∂V/∂Fᴿ = 0` gives `−FᴿDV01ᴿ = FᴺDV01ᴺ × Cov/V(Δyᴿ) = FᴺDV01ᴺβ̂`.
- Two-variable hedge: `Fᵏ = −F²⁰ × (DV01²⁰/DV01ᵏ) × β̂ᵏ` for k = 10, 30.
  - Derivation: substitute the fitted `Δŷ²⁰` into the P&L and zero the coefficients of Δy¹⁰ and Δy³⁰.
- AR(1) error: `εₜ = ρεₜ₋₁ + νₜ`, 0 ≤ ρ < 1.
  - ρ = 0 recovers the level regression. ρ = 1 recovers the change regression.
  - The expected fraction of a mispricing left after one day is ρ.
- Portfolio variance with DV01 weights w (bp moves): `σ²ₚ = w′Vw`, with `Vᵢⱼ = ρᵢⱼσᵢσⱼ`.
- PC construction: `max a′Va s.t. a′a = 1`, then orthogonality constraints for later PCs.
  - Variance of PC k = its eigenvalue λₖ.
  - Scaled PC: `ãₖ = √λₖ × aₖ`.
- Rate volatility from scaled PCs (uncorrelated): `σ(τ) = √(Σₖ ãₖ(τ)²)`.
  - `Σₖλₖ = Σᵢσᵢ² = trace(V)`.
- Portfolio volatility from PCs: `σₚ = √(Σₖ (w′ãₖ)²)`.

**USD swap PCs, Oct 2001–Oct 2008 (Table 6.5, bp per 1-s.d. move)**

| Term | Level | Slope | Short rate | PC vol | Total vol | % var Level | % var Slope | % var Short | PC/Total |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3.80 | −2.74 | 1.48 | 4.91 | 4.96 | 59.8 | 31.0 | 9.1 | 99.05% |
| 2 | 5.86 | −3.09 | 0.59 | 6.65 | 6.67 | 77.7 | 21.5 | 0.8 | 99.74% |
| 5 | 6.85 | −1.53 | −0.57 | 7.04 | 7.06 | 94.7 | 4.7 | 0.7 | 99.85% |
| 10 | 6.35 | 0.06 | −0.34 | 6.36 | 6.37 | 99.7 | 0.0 | 0.3 | 99.83% |
| 20 | 5.69 | 0.82 | 0.14 | 5.75 | 5.75 | 97.9 | 2.0 | 0.1 | 99.95% |
| 30 | 5.38 | 1.09 | 0.39 | 5.51 | 5.52 | 95.6 | 3.9 | 0.5 | 99.79% |
| All 30 rates | 32.47 | 6.74 | 2.28 | 33.25 | 33.29 | 95.4 | 4.1 | 0.5 | 99.87% |

**Regression results used in the chapter**

| Regression | Period | n | R² | σ̂ (bp) | α̂ (s.e.) | β̂ (s.e.) |
|---|---|---|---|---|---|---|
| UST 3⅝s Aug-19 on TIPS 1⅞s Jul-19 | Aug-09 to Jul-10 | 229 | 56.3% | 3.82 | .0503 (.2529) | 1.0189 (.0595) |
| UST 6½s Feb-10 on TIPS 4¼s Jan-10 | Feb-00 to Feb-02 | 519 | 43.0% | 4.70 | −.0267 (.2067) | 1.5618 (.0790) |
| EUR 20y on 10y & 30y swaps | Jul-01 to Jul-06 | 1281 | 99.8% | 0.14 | −.0014 (.0040) | β¹⁰ .2221 (.0034); β³⁰ .7765 (.0037) |

## Mental Models
- **Treat a regression hedge as a DV01 hedge with an empirically measured "beta" on the hedge leg.** Traders quote it as a risk weight ("101.89% of the DV01"). Remember that the whole point is that DV01 alone does *not* measure the relative risk.
- **σ̂ is the price tag of the trade.** A regression gives both the hedge ratio and the residual daily P&L volatility. Size the trade by comparing the expected convergence with `DV01 × σ̂`, not with the unhedged DV01.
- **Like-for-like rates regress tightly, cross-asset rates do not.** Swap on swap: R² ≈ 99.8%, σ̂ ≈ 0.14bp. Nominal on real: R² ≈ 56%, σ̂ ≈ 3.8bp. Expect cross-asset hedges to leave real risk behind.
- **Three factors cover the curve, and the short end needs more.** Three PCs explain > 99% of every tenor's variance, and the level PC alone explains 95% of total variance. At the 1-year point the level PC explains only 60%. Short-end books need more hedge instruments than long-end books.
- **PC shapes are a regime indicator.** A level PC humped at 5y reflects a central bank anchoring the front end with uncertainty over the path. When policy is credibly on hold for a long time (Japan, then USD/EUR/GBP after 2008), the level PC turns upward-sloping, peaking at 10y+.

## Worked Example
**A. Regression hedge, nominal vs TIPS (May 28, 2010).** Short $100mm UST 3⅝s of 8/15/2019 (yield 3.275%, DV01 .067). Buy TIPS 1⅞s of 7/15/2019 (yield 1.237%, DV01 .081).
- DV01 hedge: `Fᴿ = 100 × .067/.081 = $82.7mm`.
- Regression hedge (β̂ = 1.0189): `Fᴿ = 82.716 × 1.0189 = $84.28mm`. The risk weight is 101.89%.
- 95% CI for β: `1.0189 ± 2 × .0595 = (0.900, 1.138)`. It contains 1, so the DV01 hedge is not statistically rejected.
  - 95% CI for α: `(−0.456, 0.556)`, which contains 0.
- Hedged daily P&L volatility: `$100mm × .067/100 × 3.82 = $255,940`. The trade must promise enough widening of the breakeven spread to pay for this.
- Rolling 30-day β̂ ranged from 0.75 to 1.29 and was trending up at the end of the sample. In 2000–2002 the same kind of regression gave β̂ = 1.56. The hedge ratio is regime-dependent.

**B. Choosing between single-leg regression hedges (Exercise 6.3–6.5, recomputed).** You pay fixed on €100mm 20y (DV01 .1447). Regressions of Δy²⁰ on each hedge rate, Jul-09 to Jul-10:
- On the 10y: β̂ = 1.001, σ̂ = 1.105bp, DV01¹⁰ = .0864.
  - Receive `100 × .1447/.0864 × 1.001 = €167.6mm` of 10y.
  - Residual vol ≈ `100mm × .1447/100 × 1.105 = €159,894/day`.
- On the 30y: β̂ = 0.917, σ̂ = 0.666bp, DV01³⁰ = .1911.
  - Receive `100 × .1447/.1911 × .917 = €69.4mm` of 30y, a risk weight of 91.7%.
  - Residual vol ≈ `€96,370/day`.
- Decision: hedge with 30s. The residual risk is about 40% lower (higher R², 96.3% vs 89.9%).
- Check on the coefficients: the 30y slope CI `(0.895, 0.939)` excludes 1, so a DV01 hedge with 30s would be wrong.

**C. PCA-weighted 2s5s10s butterfly (USD, May 28, 2010).** Receive 100 notional of 5y (DV01 .0468). Pay F₂ of 2y (DV01 .0197) and F₁₀ of 10y (DV01 .0842). Neutralize the Level and Slope PCs from Table 6.5:
- Level: `F₂(.0197)(5.86) + F₁₀(.0842)(6.35) + 100(.0468)(6.85) = 0`.
- Slope: `F₂(.0197)(−3.09) + F₁₀(.0842)(.06) + 100(.0468)(−1.53) = 0`.
- Solution with the rounded table inputs: F₂ ≈ −120.4, F₁₀ ≈ −34.0. The book, at full precision, gets −120.26 and −34.06.
- Risk weights: **50.6% in 2s and 61.3% in 10s**, which sum to 112%, not 100%. The hedge is PC-neutral, not parallel-shift neutral.
- Residual risk: a 1-s.d. *fall* in the third PC costs ≈ **−0.031 per 100** of 5y notional.
  - A 2-s.d. move costs ≈ 0.062, i.e. only ≈ 1.3bp of 5y convergence (0.062/0.0468).
  - The trader may reasonably skip hedging PC3.
- Three-PC hedge (adding 30s): risk weights ≈ 28% (2y), 139% (10y), −67% (30y). Here you *receive* in 30s.

**D. Appendix B, three-rate PCA (verified with numpy).**
- Inputs: vols 4.25/4.20/4.15bp, correlations 10–20 .95, 10–30 .90, 20–30 .99.
- Eigenvalues 51.04, 1.867, 0.017 (96.4%, 3.5%, 0.03% of total variance 52.925).
- Scaled PCs: level (4.114, 4.191, 4.069), slope (−1.068, .260, .812), third (.032, −.103, .075).
- Portfolio with DV01 weights w = (.5, −1, .6): `w′Vw = 0.2156`, so **σₚ = 0.464bp**.
  - Per-PC exposures `w′ãₖ` = .3074, .3068, .1640.
  - `√(.3074² + .3068² + .1640²) = 0.464`.
- ⚠ Correction: the book labels 0.4642 as the portfolio *variance* in eq. (6.40) and labels .3074/.3068/.1640 as *squared* exposures in (6.47)–(6.49). In fact 0.464 is the volatility (variance 0.2156), and the three figures are unsquared exposures. The book's final answer, σ = 0.464, is right.

## Anti-patterns
- **Assuming β = 1 by default (a plain DV01 hedge across markets)**: for nominal vs real, or swaps vs Treasuries, the average relative move can be 1.5 in some regimes.
- **Treating the in-sample R² as hedge quality**: the EUR 10s/30s hedge had R² = 99.8% in 2001–06, yet out-of-sample daily errors reached −5.3bp in the 2008 crisis.
- **Regressing real on nominal (the wrong way round)**: the error then contains inflation, which is correlated with the regressor, so β̂ is biased.
- **Using level-on-level regressions to set hedges or signal convergence**: they assume a mispricing disappears overnight. Change regressions assume it never does. Model the persistence (ρ).
- **Forcing risk weights to sum to 100% or picking arbitrary 50/50 weights**: a minimum-variance or PC-neutral hedge is generally not DV01-neutral.
- **Calling the third PC "curvature" without looking at it**: in USD swaps it is dominated by short-end moves.
- **Using PCs estimated in one regime after a policy regime shift**: post-2008 the level PC's peak moved from ~5y to 10y+.

## Practitioner Notes
- The constant α in change-on-change regressions of comparable yields is almost always insignificant: one yield does not trend while its peer is flat. A significant α is a data or specification smell.
- Standard error of the regression uses n−2 degrees of freedom. The residual mean is zero by construction when a constant is included.
- Stability toolkit: rolling-window β̂ (30-day windows in the book), comparison across sub-periods (2000–02 vs 2009–10), and plots of out-of-sample residuals.
  - After a crisis there is no clean answer: you can re-estimate on crisis data, revert to a pre-crisis window, or shorten the window. Tuckman calls this the "art" of regression hedging.
- Market-maker logic for tenor hedging: hedging an illiquid 20y received from a client with liquid 10s and 30s preserves the client spread that paying 20s would give away. The regression tells you the split (≈ 22%/78% of DV01 in EUR 2001–06).
- The PCA sanity check: PC variance / total variance per tenor should be ≈ 99%+. If it falls well below, either there are more factors or the sample includes structural breaks.
- Butterfly weights: PCA (level + slope neutral) is the empirical alternative to the 50/50 DV01 butterfly and to the regression butterfly. Quote the result as risk weights on the body DV01.
- Level PC shape by market (2001–08): USD, EUR and GBP are humped with a ~5y peak. JPY rises monotonically and flattens out (zero-rate policy). Post-2008, all of them look like old JPY, and JPY is even steeper.

## Key Takeaways
1. Regression hedge = DV01 hedge × β̂, with `β̂ = Cov/Var`. It minimizes the in-sample variance of the hedged P&L.
2. The regression also prices the residual risk: `σ(P&L) ≈ |F| × DV01/100 × σ̂`. Use it to size trades and compare hedge candidates.
3. Put the yield containing the unhedged component (e.g. the nominal yield, which carries inflation) on the left-hand side, or OLS is biased.
4. Check β̂ stability (rolling windows, sub-periods, out-of-sample errors). Relationships break in crises and regimes.
5. Level vs change regressions are two extreme persistence assumptions. The sensible model is levels with AR(1) errors.
6. Three PCs (level, slope, short rate) explain > 99% of swap-curve variance. Level alone explains ~95%, but much less at the short end.
7. PCA hedges neutralize '01 exposures to each PC. The risk weights need not sum to 100%. Check the P&L from unhedged PCs before adding legs.
8. PC shapes are regime-dependent: prolonged policy anchoring pushes the level PC's peak to 10y+.

## Connects To
- **ch04**: DV01 and duration hedges, which regression hedging generalizes by the factor β̂.
- **ch05**: key-rate, partial '01 and forward-bucket hedges. PCA hedging uses the same "shift, reprice, solve" mechanics.
- **ch07–ch11**: term structure models replace empirical factors with modelled factors. Gauss+ (ch11) is calibrated partly to the empirical volatility/covariance structure of the curve.
- **ch14 / ch16**: futures and swap hedges where regression-based weights are common (e.g. swap spreads).
- **`cfa-fixed-income` ch07**: the level/slope/curvature factors of the yield curve and yield-curve factor models.
- **`cfa-fixed-income` ch14**: butterfly and yield-curve strategies that use these weights.
- **`ilmanen-yield-curve` ch06**: a framework for analyzing yield-curve trades, including duration-neutral and regression-weighted butterflies.
- **`hull-derivatives` ch03**: minimum-variance hedge ratio `h* = ρσ_S/σ_F`, the same OLS logic applied to futures hedging.
- **`hull-derivatives` ch22**: PCA as a risk-factor reduction tool for VaR.
