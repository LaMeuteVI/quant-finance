# Chapter 1: Overview of Forward Rate Analysis
> **Source**: Antti Ilmanen, *Understanding the Yield Curve, Part 1: Overview of Forward Rate Analysis*, Salomon Brothers U.S. Fixed-Income Research (1995)

## Core Idea
The Treasury curve shape has three drivers: **rate expectations**, **bond risk premia** and **convexity bias**. The one-year forward premium is roughly the sum of an expected rate change, a risk premium and a (negative) convexity term. You cannot decompose a real curve exactly, but one fact holds with no model at all: **forward rates are break-even rates**. If the forward-implied yields are realized, every bond and every self-financed curve position earns the riskless return. The rest of the series turns this into tools. Forwards serve as yardsticks for rate views, as detectors of cheap sectors, and as relative-value indicators for duration-neutral barbell/bullet trades.

## Frameworks Introduced
- **Three influences on the yield curve shape**:
  - **Rate expectations**: expected rises steepen the curve, and expected flattening makes it more concave (curved) as a function of duration.
  - **Bond risk premium (BRP)**: the expected one-period return of a long bond above the riskless one-period bond. Ilmanen uses it broadly, so it covers liquidity, institutional and supply/demand effects as well as pure risk compensation. A positive BRP steepens the curve.
  - **Convexity bias**: more convex (long) bonds can offer a given expected return at a lower yield. This depresses long yields and makes the curve concave at long durations.
  - The forward-spot premium decomposes (approximately) as `fₙ₋₁,ₙ − s₁ ≈ E(Δ rate) + BRP + CB`, with CB < 0.
  - When to use: to interpret any curve shape before trading it. For example, a steep curve means either expected hikes or high required premia, and a strong hump means expected flattening, high volatility, or a concave premium curve.
  - Failure mode: treating the decomposition as observable. All three components vary over time and must be estimated, using surveys (expectations), historical returns (premia) and option-implied volatility (convexity).
- **Forwards as break-even rates (model-free)**:
  - If forward-implied yield changes are realized, all government bonds earn the same holding-period return, and every self-financed position (for example long barbell / short bullet) earns 0.
  - If the curve is unchanged, the n-year zero earns the one-year forward rate fₙ₋₁,ₙ.
  - Rule: take a bearish position only if you expect rates to rise **by more than the forwards imply**. If you expect a smaller rise than the forwards imply, be long, because carry wins.
  - Failure mode: going short duration on a correct "rates will rise" call and still losing, because the rise was smaller than the forward-implied rise (the negative carry ate it).
- **Three practical uses of forwards in curve trades**:
  1. **Break-even yardstick for active views**. Compare your subjective curve scenario or yield path with the forward par curve at the horizon, or with the forward path of a constant-maturity rate (for example the implied 3-month rate path against your Fed view).
  2. **Indicator of cheap maturity sectors**. The forward curve magnifies local kinks, so abnormally high forwards flag cheap sectors. To exploit a high forward between 9y and 12y, buy the 12y and sell the 9y. Market-value weighting leaves you exposed to rising rates and steepening, so add a 15y short with weights that neutralize level and slope.
  3. **Relative-value tool for duration-neutral trades**. The implied spread change needed to offset the carry of a flattener or steepener is a cheapness indicator. When the implied flattening is historically wide, the flattener (barbell) is expensive and the bullet is cheap.
- **Cushion / rolling-yield logic for duration extension**:
  - On an upward-sloping curve, long bonds' yield advantage is a cushion against rising yields.
  - Their **rolling yield** advantage (yield + rolldown) is even larger than their yield advantage.
  - fₙ₋₁,ₙ equals the n-year zero's rolling yield. f₁,ₙ − sₙ₋₁ is the break-even shift that wipes out the advantage.
  - How: treat an unchanged curve as the base case (history supports this better than the forwards do), be long duration when the forward curve slopes up and short when it inverts, and resize dynamically.

## Key Concepts
- **Yield to maturity**: the single discount rate equating PV to price. It is problematic unless the curve is flat, because it discounts all flows at one rate and assumes a bond-specific reinvestment rate.
- **Par yield curve**: yields of hypothetical bonds priced at 100 (so coupon = yield). The on-the-run curve approximates it.
- **Spot rate sₙ**: the discount rate of a single cash flow at n (a zero's yield).
- **Forward rate f_m,n**: the rate for a loan from m to n contracted today. It can be locked in with zeros (buy one n-year zero, short Pₙ/Pₘ m-year zeros, zero net cost).
- **Implied spot curve one year forward** (f₁,₂, f₁,₃, …): the break-even curve next year. Do not confuse it with the **constant-maturity one-year forward curve** (f₁,₂, f₂,₃, f₃,₄, …).
- **Break-even yield change** Δfₙ₋₁ = f₁,ₙ − sₙ₋₁: the change in the (n−1)-year spot rate implied by the forwards.
- **Rolling yield**: horizon return if the curve is unchanged, equal to yield + rolldown return.
- **Rolldown return**: the capital gain from aging down an upward-sloping curve.
- **Forward-spot premium** FSPₙ = fₙ₋₁,ₙ − s₁.
- **Pure expectations hypothesis**: all bonds have the same near-term expected return because risk-neutral traders arbitrage away differentials.
- **Local expectations hypothesis (LEH)**: all bonds earn the same expected return over the next period.
- **Unbiased expectations hypothesis (UEH)**: forward rates equal expected future spot rates. LEH and UEH differ by the convexity bias, so both cannot hold exactly.
- **Liquidity premium hypothesis**: investors dislike short-term price swings, so the BRP is positive and rises with duration.
- **Preferred habitat hypothesis**: long-liability holders see long bonds as riskless, so the BRP can fall with duration.
- **Convexity**: `Cx = (d²P/dy²)/P`. For option-free bonds it grows roughly with duration². Among same-duration positions, the zero (bullet) has the least and a barbell has more.
- **Treasury Model spread**: a bond's rich/cheap spread against a fitted curve. Cheapness persists, so compare it with its own history.

## Formulas & Reference Tables
- Zero price: `Pₙ = 100/(1 + sₙ)ⁿ`
- Forward from spots: `(1 + f_m,n)ⁿ⁻ᵐ = (1 + sₙ)ⁿ/(1 + sₘ)ᵐ`. Special cases: sₙ = f₀,ₙ, and the one-year forward is fₙ₋₁,ₙ.
- Break-even selling rate: `(1 + s₂)²/(1 + f₁,₂) = 1 + s₁`. f₁,₂ is equally the break-even reinvestment rate for rolling one-year zeros.
- Coupon bond via YTM: `P = Σ C/(1+y)ᵗ + 100/(1+y)ⁿ`. Via spots: `P = Σ C/(1+sₜ)ᵗ + 100/(1+sₙ)ⁿ`.
- Bootstrap: solve `100 = C/(1+s₁) + … + (C+100)/(1+sₙ)ⁿ` for sₙ using the earlier spots.
- Linear approximation (exact under continuous compounding): `f_m,n ≈ (n·sₙ − m·sₘ)/(n − m)`
- One-year forward ≈ rolling yield: `fₙ₋₁,ₙ ≈ sₙ + (n−1)(sₙ − sₙ₋₁)`, i.e. yield + duration-at-horizon × rolldown.
- Realized one-year return of an n-year zero: `hₙ ≈ sₙ + (n−1)(sₙ − s*ₙ₋₁)`, where s*ₙ₋₁ is next year's (n−1)-year rate.
- Convexity bias: `CBₙ = −½ · Cxₙ · (σ of Δsₙ)²`
- Duration: `Dur = −(dP/dy)/P`.

**Ordering of the three curves**

| Spot curve shape | Ordering | Comment |
|---|---|---|
| Upward sloping | forward > spot > par | par is the flattest (an average of spots). Spots are geometric averages of forwards |
| Inverted | par > spot > forward | reversed |
| Humped (rise then fall) | forward crosses spot from above at the spot peak | |
| Steep then flattening | forwards can slope **down** while spots still slope up | rolldown shrinks |
| Flat | all identical | the only case where they coincide |

**Appendix A notation (used throughout the series)**

| Symbol | Meaning |
|---|---|
| f₁,ₙ | implied (n−1)-year spot rate one year forward |
| Δfₙ₋₁ = f₁,ₙ − sₙ₋₁ | break-even change of the (n−1)-year spot |
| Δfzₙ = f₁,ₙ − sₙ | implied yield change of the specific n-year zero |
| BRPₙ = E(hₙ − s₁) | bond risk premium. Realized BRPₙ = hₙ − s₁ (excess bond return) |
| PF | persistence factor: slope in a regression of realized BRPₙ on FSPₙ |
| Term spread | sₙ − s₁ |
| Real yield | long yield − recent year-on-year CPI inflation |
| Inverse wealth | `0.1·(Wₜ₋₁ + 0.9Wₜ₋₂ + 0.9²Wₜ₋₃ + …)/Wₜ`, with W = stock market level |

## Mental Models
- **Think of forwards as break-evens first and expectations last.** The break-even property needs no assumption, while "forwards = expected rates" needs zero risk premia and negligible convexity bias. The data reject that.
- **Think of the one-year forward curve as a map of rolling yields.** Given an unchanged curve, fₙ₋₁,ₙ is the n-year zero's expected one-year return, so the forward curve is a near-term expected-return curve (biased down by convexity).
- **Use the forward curve as a magnifying glass.** Spot and par rates are averages of forwards, so local cheapness shows up much more in forwards. In January 1990 the par curve spanned about 25bp while the 3-month forwards spanned about 200bp.
- **Level expectations shape the slope, and slope expectations shape the curvature.** Expected parallel rises give a linearly rising curve against duration. Expected rises plus flattening give a rising, concave curve.
- **Prefer "unchanged curve" over "forwards realized" as a base case.** Historically, current spots forecast future spots better than forwards do.

## Worked Example
**Bootstrapping and the break-even (Ilmanen's Figure 9, recomputed).** Par rates are 6% (1y) and 8% (2y), annual coupons.
- s₁ = 6%. Solve `100 = 8/1.06 + 108/(1+s₂)²`, which gives **s₂ = 8.08%**.
- `1 + f₁,₂ = 1.0808²/1.06`, so **f₁,₂ = 10.20%**.
- Two-year zero today: 100/1.0808² = **85.61**. If f₁,₂ is realized next year, its price is 100/1.1020 = **90.74**. The return is 90.74/85.61 − 1 = **6.00%**, which equals s₁.
- Interpretation: the one-year rate must rise by **more than 420bp** (10.20 − 6.00) before the two-year zero underperforms the one-year zero.

Full table (par → spot → one-year forward), recomputed:

| n | Par | Spot | Fwd fₙ₋₁,ₙ | Rolling-yield approx `sₙ + (n−1)(sₙ−sₙ₋₁)` |
|---|---|---|---|---|
| 1 | 6.00 | 6.00 | 6.00 | — |
| 2 | 8.00 | 8.08 | 10.20 | 10.16 |
| 3 | 9.50 | 9.72 | 13.07 | 13.00 |
| 4 | 10.50 | 10.86 | 14.36 | 14.28 |
| 5 | 11.00 | 11.44 | 13.77 | 13.76 |
| 6 | 11.25 | 11.71 | 13.10 | — |

The forward curve peaks at 4 years and then inverts, even though spots keep rising, because the spot slope flattens. The linear rolling-yield approximation is within about 8bp. (Recomputing from the 2-decimal par rates reproduces the source table to within 1bp through year 6. Years 7–10 differ by up to about 10bp because the par inputs are rounded.)

**Implied curve change.** With the same curve, f₁,₃ = √(1.0972³/1.06) − 1 ≈ 11.63%. So the forwards imply that next year's 2-year spot rises about 355bp from today's 8.08% (Δf₂). The specific 3-year zero's yield rises about 191bp (Δfz₃ = 11.63 − 9.72).

## Anti-patterns
- **"Forwards show the market's expected rates"**: only true with zero BRP and tiny convexity bias. At short maturities the BRP is material, so raw forwards give a strongly **upward-biased** estimate of expected near-term rates. Subtract a premium estimate.
- **"Unequal expected returns would mean arbitrage"**: false. Arbitrage ties forwards to zero prices, but it says nothing about what drives zero prices (expectations vs premia). 1994 showed that long bonds with higher expected returns are not riskless.
- **Trading a direction view without the forwards**: ignoring carry turns correct forecasts into losses.
- **Reading very low long-end forwards as cheapness signals**: these reflect convexity bias, so forwards understate expected returns at long maturities.
- **Using YTM to compare bonds on a sloped curve**: it mixes discount rates and assumes bond-specific reinvestment rates. Work with spots and forwards.

## Practitioner Notes
- In recent decades the U.S. Treasury curve sloped up about **90%** of the time, which is consistent with positive premia.
- Empirical premia (1970–94, excess over the 1-month bill) are **concave in duration**. They rise steeply up to about 2 years and then slowly. Geometric averages are roughly flat beyond 2 years. The theoretical linear-in-duration line overstates long-end premia.
- Premia are **countercyclical**: high after poor economic conditions and low after strong ones, because risk aversion rises when wealth is low.
- Steeper curves have been followed on average by small **declines** in long yields, not by the rises the pure expectations hypothesis predicts. Steeper curve means higher expected BRP.
- Many one-factor models assume the same expected return for the same duration, so convexity is priced exactly. Empirically, barbells **marginally underperform** duration-matched bullets in the long run, which means investors pay for convexity as insurance.
- **December 1994 case**: 3m–2y was about 200bp steep and 2y–30y about 20bp flat. The high curvature meant forwards implied a 2s30s inversion by March, so the barbell (30y + 3m bill) versus the duration-matched 2y bullet was very expensive. The 2y bullet then outperformed. By March 1995 the front end had flattened by 108bp and the long end steepened by 45bp.
- **January 1990 case**: the par curve was nearly flat (within 25bp), but 3-month forwards ranged about 200bp. High forwards flagged the 6y and 12y sectors as cheap, and low forwards flagged 4y and 9y as rich. The cheap sectors richened over the next quarter.
- A bond-level rich/cheap spread (for example against a fitted "Treasury Model" curve) is best judged against its own history, because cheapness persists.

## Key Takeaways
1. Decompose every forward premium into expected rate change + risk premium + convexity bias (negative) before interpreting the curve.
2. Forwards are model-free break-evens. Every directional or curve trade should be sized against the forward-implied move, not against zero change.
3. fₙ₋₁,ₙ = the n-year zero's rolling yield ≈ its expected return if the curve stays put. An upward-sloping forward curve therefore favors duration extension.
4. The forward curve magnifies sector cheapness. Trade bumps with level- and slope-neutral butterflies.
5. High curve concavity means expensive flatteners (barbells) and cheap bullets, unless you expect more flattening or a volatility spike.
6. Raw forwards overstate expected near-term rates. Strip out a premium estimate before inferring what the Fed or market "expects".
7. An unchanged curve is historically a better base case than forwards being realized.

## Connects To
- **ch02**: the break-even and expectations views of forwards in depth, including the four views of forward rates.
- **ch03**: long-run average risk premia against duration (the empirical Figure 3 curve).
- **ch04**: time-varying premia and the predictors (steepness, real yield, inverse wealth, momentum).
- **ch05**: the convexity bias formula and the value of convexity.
- **ch06**: the full framework for barbell/bullet and curve trades.
- **`tuckman-fixed-income` ch02**: spot, forward and par rate mechanics and bootstrapping.
- **`tuckman-fixed-income` ch03**: returns, carry and roll-down decomposition.
- **`cfa-fixed-income` ch07**: term structure theories (expectations, liquidity, preferred habitat).
- **`cfa-fixed-income` ch14**: yield-curve strategies (riding the curve, barbell vs bullet).
