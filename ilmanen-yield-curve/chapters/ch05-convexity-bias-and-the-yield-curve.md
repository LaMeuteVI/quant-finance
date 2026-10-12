# Chapter 5: Convexity Bias and the Yield Curve
> **Source**: Antti Ilmanen, *Understanding the Yield Curve, Part 5: Convexity Bias and the Yield Curve*, Salomon Brothers U.S. Fixed-Income Research (September 1995)

## Core Idea
Positive convexity is valuable, and its value grows with yield volatility. So investors accept lower yields on highly convex (long) bonds and still earn the same near-term expected return. This **convexity bias** pushes the curve toward an inverted or humped shape, mostly at the long end. Yield-based tools (yield, rolling yield) give convexity no value. The fix is **convexity-adjusted expected return = rolling yield + value of convexity**, which is the right single number for judging duration-neutral barbell-bullet trades. In practice a barbell-bullet trade is mostly a curve-flattening bet, and convexity is a secondary, though real, component.

## Frameworks Introduced
- **Convexity-adjusted expected return** (Equation 2):
  - When to use: to compare expected near-term returns across bonds or across barbell-bullet structures when the base case is an unchanged curve.
  - How: (1) Compute the rolling yield (yield + rolldown return, i.e. the return if the curve does not move). (2) Estimate the expected basis-point yield volatility over the horizon. (3) Add `½ · Cx · σ²` (annualised for a one-year horizon). (4) Compare the sums, not the yields.
  - Why it works / failure mode: the rolling yield assumes zero volatility, so it is biased downward for any positively convex bond. Any base-case proxy can be used instead of "unchanged curve" and the convexity term still gets added; if you hold curve-reshaping views, add them as a third term. It is only as good as the volatility forecast (the value of convexity for the 30-year bond was several hundred bp in the early 1980s and rarely above 100 bp in the 1990s).
- **Convexity bias decomposition of the curve shape** (the "pure convexity" thought experiment):
  - When to use: to isolate what part of the curve's shape is compensation for convexity rather than expectations or risk premia.
  - How: (1) Assume every zero has the same expected return (8%) and short rates are expected flat. (2) Back out each zero's rolling yield = 8% − value of convexity. (3) The rolling yield equals the one-year forward rate between n−1 and n, so you get the forward curve. (4) Chain forwards into the spot curve. Result: both curves slope down at an increasing pace, and convexity bias = −½·Cx·σ².
  - Failure mode: real curves rarely invert like this, because positive bond risk premia offset the bias at the front end. At the long end the bias can dominate, giving a **humped** curve. Even convexity-adjusted returns invert beyond ~25 years, which the author attributes to a liquidity and financing advantage of long zeros.
- **Barbell-bullet break-even analysis** (two questions):
  - When to use: to see whether a duration- and cash-neutral barbell is a curve trade or a convexity trade.
  - How: (1) Weight the barbell so duration at horizon matches the bullet (long-bond weight = bullet duration / long duration at horizon; the rest in cash). (2) Compute the rolling-yield give-up. (3) Solve the **flattening break-even**: how many bp the bullet-to-long spread must narrow, with no parallel shift, to offset the give-up. (4) Solve the **parallel-shift break-even**: how large a parallel move is needed for convexity alone to offset it. (5) Compare both with historical frequencies.
  - Why: the payoff versus parallel shifts is U-shaped like a **long straddle**, with the give-up as the premium and maximum loss at zero yield change.
- **Implied volatility of a barbell-bullet trade**: back out the volatility at which the rolling-yield spread equals the convexity pick-up, assuming the barbell and the bullet have equal expected returns. High curve concavity means high implied volatility. A convex (dished) curve gives negative implied volatility, which signals expected steepening. Very noisy, because reshaping expectations pollute it. Better: subtract the value of convexity (at option-implied volatility) from the rolling-yield spread to extract flattening expectations.
- **Return decomposition** (Equation 3): `Return ≈ yield − Dur·Δy + ½·Cx·(Δy)²`, plus a small residual. Use it to attribute realised returns.

## Key Concepts
- **Convexity (Cx)**: the curvature of the price-yield curve, `(100/P)·d²P/dy²` with yields in percent. A positively convex price rises more for a yield fall than it falls for an equal rise.
- **Value of convexity**: `≈ ½·Cx·σ²`, the expected gain from convexity when yields move up or down by about σ. It is zero if volatility is zero.
- **Convexity bias**: the negative of the value of convexity. It is the wedge between the forward curve and the expected-return curve, and it tilts the curve down.
- **Rolling yield**: the one-year holding return if the curve is unchanged. For an n-year zero it equals the one-year forward rate from n−1 to n.
- **Convexity-adjusted expected return**: rolling yield + value of convexity.
- **Cash-flow dispersion**: the standard deviation of a portfolio's cash-flow maturities around its Macaulay duration. More dispersion gives more convexity at a given duration. A zero has none and hence the minimum convexity for its duration.
- **Barbell / bullet**: a barbell is short plus long bonds (and possibly cash). A bullet is a single intermediate bond of the same duration.
- **Yield volatility, σ = Vol(Δy)**: the annualised standard deviation of basis-point yield changes. This differs from relative volatility Vol(Δy/y), which is the option-market quote. Convert: `σ_bp = Vol(Δy/y) · y`.
- **Term structure of volatility**: volatility by duration. Inverted in the early 1980s (money-supply targeting), flat or humped in the 1990s. Zeros are more volatile than coupon bonds of equal duration.
- **Rolling-yield give-up**: the yield a barbell loses versus the bullet, because the curve is concave in duration.
- **Long straddle analogy**: the barbell-bullet payoff vs parallel shifts is U-shaped like a long straddle, but held over a static horizon (no dynamic delta hedging).
- **Dispersion term** (Kogelman 1986): the extra convexity of a coupon bond or portfolio beyond a duration-matched zero.

## Formulas & Reference Tables
- Price approximation: `100·ΔP/P ≈ −Dur·Δy + ½·Cx·(Δy)²`, with `Dur = −(100/P)·dP/dy` and yields in %.
- Zero price: `P = 100/(1 + y/100)ⁿ`. Modified duration `Dur = n/(1 + y/100)`, and Macaulay duration T = n.
- Zero convexity: `Cx = (n² + n)/[100·(1 + y/100)²] = [Dur² + Dur/(1 + y/100)]/100`. Rule of thumb: `Cx ≈ Dur²/100` (a 15-duration zero has Cx ≈ 2.25).
- Portfolio convexity: `Cx = (T² + T)/[100(1 + y/100)²] + Dispersion/[100(1 + y/100)²]`, where T = Macaulay duration.
- Value of convexity: `½·Cx·σ²` (σ in %, per year). For a horizon h in years scale σ by √h, so the value scales with h (a quarter gives roughly ¼ of the annual figure).
- Convexity bias `≈ −½·Cx·σ²` (adjusted because price changes happen at the end of the horizon, not instantly).
- Expected return: `E[R] ≈ rolling yield + ½·Cx·σ²`. Value of convexity for zeros `≈ Var(h)/200`, where h = holding-period return.
- Return vs yield volatility: `Vol(h) ≈ Dur·σ ≈ Dur·Vol(Δy/y)·y`. Variance link: `Var(h) ≈ 100·Cx·σ²`.
- Arithmetic vs geometric mean: `GM ≈ AM − Var(h)/200`. Duration extension raises arithmetic expected return through convexity, but the added volatility drags the geometric mean down by the same amount.
- Barbell weights: `w_long = Dur_bullet(at horizon)/Dur_long(at horizon)`, `w_cash = 1 − w_long`. Barbell convexity = market-value-weighted average of component convexities. Barbell yield volatility uses market value × duration weights.
- Sample expected one-year returns, 1 Sep 1995 (yield, rolling yield, value of convexity, convexity-adjusted return, all %):

| Bond | Dur | Cx | σ (bp) | Yield | Rolling yield | Value of Cx | Conv-adj ER |
|---|---|---|---|---|---|---|---|
| 1y par | 0.95 | 0.02 | 98 | 5.73 | 5.73 | 0.00 | 5.73 |
| 5y par | 4.20 | 0.23 | 104 | 6.13 | 6.31 | 0.09 | 6.40 |
| 10y par | 7.20 | 0.67 | 95 | 6.47 | 6.94 | 0.27 | 7.21 |
| 30y par | 12.66 | 2.57 | 82 | 6.81 | 6.67 | 0.88 | 7.55 |
| 20y zero | 18.68 | 3.66 | 83 | 7.07 | 7.49 | 1.22 | 8.71 |
| 30y zero | 28.07 | 8.14 | 79 | 6.88 | 5.93 | 2.53 | 8.46 |
| 1y+30y barbell | 7.18 | 1.38 | 82 | 6.30 | 6.23 | 0.47 | 6.70 |

- Historical decomposition, 30-year on-the-run 1980–94 (average annualised return 10.34%): yield 9.41%, duration −0.49%, convexity +1.48%, residual −0.06%. Duration drives 99% of monthly volatility but washes out over time. Convexity was about half as large in the 1990s.
- Barbell-bullet (5y bullet vs 30y + 1-month bill barbell) 1980–94: total −1.05%/yr = yield −0.95, reshaping (duration) −0.36, convexity +0.30, residual −0.04. The bullet won in four of five three-year subperiods.

## Mental Models
- **Convexity is an option you pay for in yield.** Think of the barbell as a long straddle: the rolling-yield give-up is the premium and large moves either way repay it. Ask whether implied volatility (from the curve) exceeds what you expect.
- **Yield ≠ expected return.** Yield ignores rolldown, rolling yield ignores volatility, and convexity-adjusted return ignores your reshaping views. Move down that ladder as far as your information allows.
- **Convexity is a volatility bet, curve shape a level bet.** Around the 10s-30s trade, flattening is about 2.5 times more plausible than a giant parallel move. Do not sell a barbell as a "convexity trade" unless you expect an extreme shock.
- **Convexity is priced at the long end and nearly free at the front end.** Below about 5 years the bias is negligible, so curvature there reflects flattening expectations. Beyond 10 years it reflects volatility as well.
- **Expect an inverted curve when volatility is high.** High volatility makes the curve more humped and raises the barbell-bullet and coupon-zero spreads.

## Worked Example
**A. Value of convexity with two scenarios (annual compounding, recomputed).** A 30-year zero yields 8%: P = 100/1.08³⁰ = 9.94. Yields jump to 10% or 6% with equal probability: prices 5.73 and 17.41, so E(P) = 11.57. The expected gain from pure volatility is 11.57 − 9.94 = 1.63 (16%) with no directional view. (The source's semi-annual figures give 5.40, 17.00, 9.50 and a $1.70 gain. The point is unchanged.)

**B. Backing out a rolling yield.** Set expected return 8%, σ = 100 bp, long zero Cx ≈ 15²/100 = 2.25. Value of convexity = 0.5 × 2.25 × 1² = 1.125%. Rolling yield must be 8 − 1.125 = 6.875%, i.e. the forward rate for that segment sits 112.5 bp below the expected return.

**C. 1s-30s barbell vs 10-year bullet (Sep 1995).** Weights 0.53 in the 30-year (6.67% rolling) and 0.47 in the 1-year (5.73%) against the 10-year at 6.94%.
- Rolling-yield give-up: 0.53 × 6.67 + 0.47 × 5.73 − 6.94 = −0.71% (71 bp).
- Convexity pick-up in value terms: barbell 0.47% (0.5 × 1.38 × 0.82²) vs bullet 0.27%, but the book quotes the full adjusted returns: 6.70 − 7.21 = −51 bp. The barbell is still expensive.
- Break-evens: about 11 bp of 10s-30s flattening (this happened by at least 11 bp in about 30% of years) or a 138 bp parallel shift (more than 138 bp only about 17% of years).
- Read: the trade needs flattening, not convexity. It is a curve trade with a small convexity kicker.

## Anti-patterns
- **Ranking bonds by yield or rolling yield alone**: this gives convexity no value and penalises long zeros. Use convexity-adjusted expected return.
- **Ignoring the volatility input**: convexity's value can double with 1980s volatility and vanishes in calm markets. Use a current forecast, not a stale sample. Do not lean on implied volatility just because it is available, since it does not predict better than history.
- **Confusing basis-point and relative volatility**: option quotes are relative. A 13% quote at a 7% yield equals 91 bp, and mixing them gives errors of a factor of 10 or more.
- **Extrapolating a wide-barbell result to narrow barbells**: the 5s vs cash-and-30s result (yield give-up of about 100 bp/yr) does not carry to 2s-5s-10s, where curvature and convexity are far smaller.
- **Assuming a duration-neutral barbell is parallel-shift proof**: it is neutral only to small parallel shifts, and nonparallel shifts dominate (99% of monthly return volatility is duration impact, which for the trade is reshaping).
- **Treating convexity as free money**: if it were, flat curves plus parallel shifts would give arbitrage. The market prices it through concave yield curves.

## Practitioner Notes
- The approximation in Equation (1) is very accurate within about 300 bp, even for a 30-year zero. Quarterly horizon: scale value by ¼.
- Convexity of a coupon bond exceeds a duration-matched zero's only through dispersion; zeros are the least convex for their duration.
- Historically more convex positions earned somewhat lower long-run returns (the bullet beat the barbell by about 105 bp/yr), consistent with convexity being partly priced or with income-seekers dominating. The author says the jury is still out.
- The rolling-yield curve is typically concave in duration, so a duration-neutral barbell almost always gives up rolling yield. Time variation in coupon-sector curvature (below 10 years) reflects expected flattening more than volatility expectations.
- Typical inputs he used: horizon of one year; σ from 1990–95 weekly data (all-period estimates ranged widely). 1979–82 (money-supply targeting) is an outlier regime.
- Two straddle styles map to two barbell styles: a static horizon-matched barbell (profit depends on the end yield) and a frequently rebalanced barbell (profit depends on realised volatility).
- On-the-run yield series mislead because of liquidity roll effects. Use a clean single-bond series when measuring yield changes.

## Key Takeaways
1. Value of convexity ≈ ½·Cx·σ². It is proportional to volatility squared and, for zeros, to duration squared.
2. Convexity bias tilts the curve down, and only visibly at long maturities. With positive risk premia the result is humped.
3. Always use convexity-adjusted expected return (rolling yield + ½·Cx·σ²) for relative value across duration, not yield.
4. A duration-neutral barbell loses rolling yield and gains convexity. Compare both with the two break-evens (flattening in bp, parallel shift in bp).
5. Most barbell-bullet trades are curve-flattening trades. The 10s-30s example needed only 11 bp of flattening versus a 138 bp parallel move.
6. Use a volatility forecast appropriate to the regime (1983–95 or 1990–95, not 1979–82), and mind bp versus relative volatility.
7. Extract expectations from curvature by subtracting the convexity value at option-implied volatility.
8. Historically, long-run returns of more convex positions were not higher: the bullet beat the barbell.

## Connects To
- **ch01**: the rolling yield, forward curve, and the three-influence decomposition (expectations, risk premium, convexity) that this chapter completes.
- **ch02**: forward rates as the base case and the "unchanged curve" as a forecast.
- **ch03**: the concave average-return curve, which explains why bullets beat barbells.
- **ch04**: risk-premium predictors that offset the convexity bias.
- **ch06**: uses convexity-adjusted returns and break-evens inside the trade-selection framework.
- **`tuckman-fixed-income` / `cfa-level1-curriculum` ch 18**: duration, convexity and effective duration mechanics.
- **`hull-derivatives`**: the straddle and volatility analogy.
