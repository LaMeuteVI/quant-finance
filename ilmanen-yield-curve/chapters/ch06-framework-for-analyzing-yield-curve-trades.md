# Chapter 6: Framework for Analyzing Yield Curve Trades
> **Source**: Antti Ilmanen, *Understanding the Yield Curve, Part 6: Analyzing Yield Curve Trades*, Salomon Brothers U.S. Fixed-Income Research, Portfolio Strategies (November 1995). OCR source: figures and some numbers were reconstructed and recomputed.

## Core Idea
Every one-period forward rate splits into **rate expectations + bond risk premium + convexity bias**, and every government-bond position's near-term expected return splits into **yield income + rolldown + value of convexity + duration impact of your rate view**, plus a fifth **local rich/cheap** term for bonds that trade special. Relative value should be judged on total expected-return differentials, not yield spreads. That one framework covers the duration decision, sector and barbell-bullet positioning, and issue selection, and it links directly to scenario analysis.

## Frameworks Introduced
- **Forward-rate decomposition** (Equation 2): `f(n−1,n) = s₁ + Dur·E(Δs) + BRP + CB`.
  - When to use: to interpret a forward curve, or to back out the one component you cannot observe.
  - How: (1) take the observable forward rates. (2) Proxy two of the three unknowns: risk premia from historical average excess returns, or expectations from surveys (Blue Chip, WSJ). (3) Compute convexity bias `−½·Cx·σ²` with historical or implied volatility. (4) Back out the remainder: expected rate change × duration (if premia are proxied) or the risk premium (if surveys are used).
  - Failure mode: the residual is scaled by duration, so a couple of bp of error in the expectation proxy wrecks long-duration estimates. Use it beyond ~7 years of duration with great caution. The identity is exact bookkeeping, not an economic theory, so it cannot tell you the split by itself.
- **How each determinant shapes the curve** (the shape-reading table below).
- **Five-term expected-return measure**: `E[R] = yield income + rolldown + value of convexity + duration impact of the view + local rich/cheap (financing + spread to fitted curve + expected cheapening)`.
  - When to use: to rank any noncallable government positions (duration, sector, barbell-bullet, single issues) on one scale.
  - How: (1) yield income = coupon + accrual (use market-value-weighted portfolio yield over short horizons). (2) rolldown = rolldown yield change × horizon duration. (3) value of convexity = `½·Cx_h·σ²·(1 + RY/100)`, where h = horizon and σ = horizon basis-point volatility. (4) view = `−Dur_h·E(Δy)·(1 + RY/100)`. (5) local = special-repo advantage + on-the-run spread to model curve + expected cheapening. Portfolios: market-value-weight each component.
  - Why it works / failure mode: it captures all sources for noncallables. But components differ in reliability: yield is unambiguous, rolldown and local terms depend on curve fitting, convexity on the volatility input, and the view on forecasting skill. Noisy inputs can make it a worse signal than plain yield spreads, so backtest it against history before trusting it.
- **Stable-carry emphasis**: unless you are extremely confident in your view, lean on the parts of expected return that come from static market conditions (yield, rolldown, convexity, local effects). Their differentials are more reliable, and with a short horizon and strong view the duration term dominates everything.
- **Scenario analysis done properly**:
  - How: (1) define 3–5 curve scenarios (bear parallel, bull parallel, unchanged, bear-flattener, bull-steepener). (2) Compute each position's horizon return. (3) **Assign probabilities.** (4) Take the probability-weighted return. (5) Back out the implied mean view (mean yield change and reshaping), implied volatilities (dispersion across scenarios) and implied correlations.
  - Why: without probabilities you cannot see hidden biases: a bearish skew, or a very high or low implied volatility that makes convex positions look too good or too bad. A single scenario means zero volatility and biases positively convex positions downward.
- **Three interpretations of a forward rate** (all equivalent by construction): (a) **arbitrage** (price derivatives), (b) **break-even** (compare with your own view), (c) **rolling yield** (relative value with no view). None of them tells you how much of the forward is expectations vs premium.

## Key Concepts
- **Forward-spot premium (FSP)**: `f(n−1,n) − s₁`. It measures the steepness of the one-year forward curve.
- **Bond risk premium (BRP)**: the expected near-term holding return of a bond minus the short rate. Here it also absorbs liquidity, supply and sentiment effects.
- **Convexity bias (CB)**: the negative of the value of convexity; bigger with volatility and duration.
- **Rolling yield**: horizon return if the curve is unchanged. For a zero it equals the one-year forward for the segment (n−1, n).
- **Rolldown return**: the capital gain from rolling down an upward-sloping curve as maturity shortens.
- **Duration impact of the view**: expected change in the constant-maturity rate at the horizon maturity × (−horizon duration).
- **Local rich/cheap effect**: financing (special-repo) advantage, spread of the bond to the fitted curve, and expected cheapening as on-the-run status fades.
- **Concave / convex curve**: concave means steeper at short maturities (flattening expected, or high volatility or premia that level off with duration). Convex means steeper at long maturities (steepening expected).
- **Local expectations hypothesis (LEH)**: all bonds have the same near-term expected return (BRP = 0).
- **Unbiased expectations hypothesis**: forwards reflect only rate expectations (BRP and CB both zero).
- **Random walk assumption**: E(Δs) = 0, so the forward-spot premium equals BRP + CB.
- **Break-even yield spread change**: the flattening (bp) needed to offset a barbell's rolling-yield give-up.
- **Implied scenario statistics**: mean yield change, volatilities, correlations backed out of scenario probabilities.

## Formulas & Reference Tables
- Zero holding return: `h = rolling yield + [−Dur·Δs + ½·Cx·(Δs)²]·(1 + f/100)`, where Δs is the change in the (n−1)-year constant-maturity rate, and Dur, Cx are measured at the horizon. All rates in percent, annual compounding. The `(1 + f/100)` factor exists because capital grows to that value before the repricing at horizon.
- Zero rolling yield equals the forward rate: `1 + f(n−1,n)/100 = (1 + sₙ/100)ⁿ/(1 + sₙ₋₁/100)ⁿ⁻¹`. Worked: 5y at 10%, 4y at 9.5% → `1.10⁵/1.095⁴ − 1 = 12.02%`.
- Expected return: `E(h) = f + (1 + f/100)·[−Dur·E(Δs) + ½·Cx·E(Δs)²]`, with `E(Δs)² ≈ σ²`.
- Excess return: `BRP = E(h − s₁)`. Rearranging the expected return gives `FSP = f − s₁ = BRP + (1 + f/100)·[Dur·E(Δs) − ½·Cx·σ²]`. The `−½·Cx·σ²` term is the convexity bias: it pulls the forward below expected return, so forwards understate the expected returns of convex (long) bonds. ⚠ Correction: the convexity term carries a negative sign here (an earlier version of this line had it positive).
- Forward-rate form: `Forward = short rate + Dur·E(Δs) + BRP + CB`, with `CB ≈ −½·Cx·σ²`. (Here E(Δs) is the expected change in the constant-maturity rate; sign convention: a rise in expected rates raises the forward.)
- Forward from spot: `(1 + fₙ,ₘ/100)ⁿ⁻ᵐ = (1 + sₙ/100)ⁿ/(1 + sₘ/100)ᵐ`.
- Portfolio expected return: `Σ wᵢ·E(hᵢ)` component by component (market-value weights).
- Scenario expected return: `E(h) = Σ pᵢ·hᵢ`. Implied volatility = probability-weighted dispersion of scenario yield changes (or returns).
- Special cases of `FSP = BRP + view + CB`:

| Assumption | Forward-spot premium reflects | Terms set to zero |
|---|---|---|
| Random walk (E(Δs) = 0) | BRP + CB | view |
| Local expectations hypothesis | view + CB | BRP |
| Unbiased expectations hypothesis | view only | BRP and CB |

- How each determinant shapes the curve:

| Determinant | Effect on spot and forward curves |
|---|---|
| Expected parallel rise / fall in rates | linear upward / inverted |
| Expected curve flattening / steepening | concave / convex |
| Positive BRP (concave in duration, big at the front end, marginal after ~2y) | upward-sloping, concave on average |
| Convexity bias (negligible short, large at long end; rises with volatility) | inverted alone; humped with positive BRP |
| Long-run averages | slope from BRP; concavity from BRP concavity + convexity bias; expectations wash out |

- Sample decomposition, 3-month horizon, 26 Sep 1995 (%, semiannual par yields, Blue Chip view, implied volatility):

| | 3m bill | 3y | 10y | Barbell (bill + 10y) |
|---|---|---|---|---|
| Yield income | 1.349 | 1.474 | 1.568 | 1.425 |
| + rolldown | 0.000 | 0.065 | 0.108 | 0.038 |
| = rolling yield | 1.349 | 1.537 | 1.676 | 1.463 |
| + value of convexity | 0.000 | 0.014 | 0.082 | 0.029 |
| = convexity-adj. ER | 1.349 | 1.551 | 1.758 | 1.492 |
| + duration impact of view | 0.000 | −0.056 | −0.284 | −0.099 |
| = ER with view | 1.349 | 1.495 | 1.474 | 1.393 |
| + local rich/cheap | −0.015 | −0.039 | +0.025 | −0.002 |
| = total ER | 1.334 | 1.456 | 1.499 | 1.391 |

  Local effect for the 10y: financing +0.463, spread to curve −0.037, expected cheapening −0.401, total +0.025.
  ⚠ Correction: the OCR shows the bill's local effect as +0.015 and the barbell as 0.53/0.47 weights. The totals only reconcile with **−0.015** for the bill, and with a barbell weight of about **0.349** in the ten-year, computed as horizon duration ratio 2.500/7.168 (matching the 3y bullet's horizon duration), leaving 0.651 in bill. Both are recomputed here.

## Mental Models
- **Yield spread is one of five pieces.** Ask "what is the total expected return differential?" before you ask "what is the yield pick-up?".
- **Split every view into static vs. subjective.** Yield, rolldown, convexity, local effects are static; the duration term is your view. Size the trade to your confidence in the second part, and prefer trades whose edge sits in the first.
- **Horizon determines the mix.** Longer duration and shorter horizon mean the duration impact swamps everything; longer horizon lets slow carry and rolldown accrue.
- **Shape is a crowd of three votes.** A steep curve on one day is mostly expectations. Averaged over years it is mostly premium. Curvature carries all three, so a very concave curve is flattening expectations or high volatility.
- **Scenarios are hidden distributions.** Each set of scenarios and probabilities is a mean, a volatility and a correlation matrix. Back them out and challenge them.
- **Forward usefulness is not forecasting power.** Derivatives are priced with forwards by arbitrage even though forwards forecast spot rates poorly. Forwards forecast bond returns better than they forecast rate changes.

## Worked Example
**A. Five-scenario analysis (recomputed).** Portfolio: equal weights in 1- to 5-year zeros at yields 6.00, 6.25, 6.50, 6.75, 7.00% (annual compounding), one-year horizon (average maturity 3y to 2y). Scenarios: bear +100 bp; bull −100 bp; unchanged; bear-flattener (+100 bp at 1y down to +50 bp at 5y); bull-steepener (−50 bp at 1y to 0 at 5y).
- Portfolio one-year returns: 5.02, 9.06, 7.00, 5.51, 7.51%.
- Equal probabilities (0.2): E(h) = 0.2 × (5.02 + 9.06 + 7.00 + 5.51 + 7.51) = **6.82%**.
- Implied mean yield change is +10 bp for each rate (mild bearish bias), implied volatilities 80 to 66 bp (inverted volatility term structure), correlations ≥ 0.92.
- Decomposition: yield income 6.50%; rolldown 7.00 − 6.50 = 0.50%; value of convexity about 2 bp (viewless scenarios average 7.02% vs the neutral 7.00%); duration impact of the +10 bp view about −20 bp (6.82 vs 7.02). Check: 6.50 + 0.50 + 0.02 − 0.20 = 6.82. ✓
- Only the two parallel scenarios at 50/50 give 7.04%, 4 bp above the 7.00% unchanged-curve return. That gap is the value of convexity at 100 bp volatility, and a single scenario would miss it.

**B. Ranking a barbell vs bullet with the five-term table.** On 26 Sep 1995 the bill-plus-10y barbell earned 1.391% over three months vs 1.456% for the duration-matched 3y bullet: about −6.5 bp per quarter, roughly −26 bp annualised. The barbell lost on every measure. The 10y's big repo advantage (+46 bp per quarter) was largely offset by its expected cheapening (−40 bp), so financing alone did not rescue the trade.

## Anti-patterns
- **Reading forwards as pure expectations**: they also carry BRP and convexity bias; a steep curve is not automatically a forecast of rate rises.
- **Ranking by yield spread**: it omits rolldown, convexity, view and local effects; it can rank rich on-the-runs as cheap.
- **Single-scenario analysis**: it assumes zero volatility and undervalues convex positions.
- **Scenarios without probabilities**: you cannot see the implied mean view, volatility or correlations, so hidden biases survive.
- **Backing out the risk premium at long duration**: a 2 bp error in the expectation proxy is multiplied by ~10 in duration.
- **Ignoring financing and on-the-run effects**: special-repo income and expected cheapening can be as big as the yield differences you are trading on.
- **Trusting the fancier measure blindly**: theoretically better, but noisier inputs can make it a worse signal. Test against history.
- **Using one input source without checking it**: results shift with the curve-fitting technique, the raw material (bonds, STRIPS, swaps, Eurodeposit futures with futures-forward convexity adjustment) and the volatility estimate.

## Practitioner Notes
- The author's monitoring rule: track broad expected-return measures against their own history as cheapness indicators, in the way desks track yield spreads.
- The changing slope of the curve is driven as much by time-varying required premia as by shifting rate expectations. Individual rate views vary a lot, but risk aversion is highly correlated across investors, so it moves the aggregate more. The 1993–95 bill-curve snapshots showed forward-implied rises consistently above survey-expected rises; by end-1994 forwards implied about +200 bp in three-month rates in six months vs about +100 bp expected, an abnormally large premium.
- The 1995 rally was partly a collapse in the risk premium (lower inflation uncertainty, higher wealth) and not only easing expectations. The author cautions that the past two years' premia were strongly market-directional and may not always be.
- With horizon-appropriate inputs use implied volatilities from OTC options where possible, but historical volatilities gave nearly the same convexity bias on that date.
- The framework extends to currency-hedged cross-country positions and to spread positions against non-government assets. Unhedged FX is not covered.
- Realised returns decompose the same way, and the duration term dominates realised returns even more than expected returns.

## Key Takeaways
1. Forward rate = short rate + expectation term + BRP + convexity bias. It is an identity, so the split must come from proxies.
2. Total expected return = yield + rolldown + convexity + view (+ local effects). Use it, not yield spread, for relative value.
3. Static components are more reliable than the view. Prefer trades whose edge is in yield, rolldown, convexity and local cheapness.
4. Shape reading: expectations of parallel moves → slope; reshaping → curvature; premia → average slope and concavity; convexity → long-end sag.
5. In scenario analysis always assign probabilities and back out the implied view, volatility and correlations.
6. Use several scenarios to capture convexity: one scenario means zero volatility.
7. Beyond about seven years of duration the decomposition is fragile. Treat it as directional.
8. Validate any expected-return measure historically before trusting it as a cheapness signal.

## Connects To
- **ch01**: the three-determinant statement, rolling yield and break-even interpretation formalised here.
- **ch02**: forwards vs survey expectations and the evidence that forwards predict returns better than rates.
- **ch03**: why the risk premium curve is concave in duration.
- **ch04**: return-forecasting models for the "view" term and the time-varying premium.
- **ch05**: the value of convexity and barbell-bullet break-evens.
- **`tuckman-fixed-income`**: term-structure models, rolldown, and forward pricing.
- **`hull-derivatives`**: no-arbitrage pricing with forward rates.
