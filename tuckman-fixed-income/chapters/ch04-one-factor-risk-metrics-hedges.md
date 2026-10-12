# Chapter 4: One-Factor Risk Metrics and Hedges
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 4 (Part Two: Measures of Interest Rate Risk and Hedging), plus the Part Two introduction · Examples: 4½s of 5/15/2017, TYU0 10-year note future, TYU0C 120 call, 2⅛s of 5/31/2015, priced 28-May-2010

## Core Idea
Interest rate risk is the slope (DV01), the slope per unit of value (duration) and the change of slope (convexity) of the price-rate function P(y), where y is *one* factor that fixes the whole curve. The definitions are model-free: y can be a yield, a spot or forward rate, or a model factor. DV01-matching hedges are local, so they need rebalancing, and a hedged book can still be short convexity, which is short volatility. The popular yield-based versions are closed-form and give great intuition, but they secretly assume parallel yield shifts.

## Frameworks Introduced
- **General (effective) DV01**: `DV01 ≡ −ΔP/(10,000·Δy) = −(1/10,000)·dP/dy`.
  - When to use: any security with a price-rate function, including options and futures; trading and hedging in dollars.
  - How: reprice at y ± 0.5bp or ± 5bp (bump both sides, do not use the base price), divide the price difference by the rate difference in bp; sign so that DV01 > 0 when price rises as rates fall.
  - Failure mode: a value that depends on which factor is bumped (yield, forward, spot: DVDF/DVDZ naming). State the shift.
- **DV01 hedge ratio (4.7)**: `F_B = −F_A × DV01_A / DV01_B` (DV01s per 100 face, same units).
  - When to use: one hedge instrument, one risk factor.
  - How: 1) compute both DV01s per 100 face; 2) apply the formula; 3) sanity-check the signs; 4) re-hedge as DV01s drift.
  - Sign rules: long A means short B (if both DV01 positive); the larger-DV01 security is traded in smaller size; a negative-DV01 security (mortgages, ch20) flips the direction.
- **Duration (effective)**: `D ≡ −(1/P)·dP/dy`, quoted per 100bp. Use it for investing (compares percent risk of different assets); use DV01 for trading (dollar amounts differ across legs).
- **Convexity**: `C ≡ (1/P)·d²P/dy²`. Numerical estimate: first derivatives on the two half-intervals, then second derivative = change in the first derivative over the rate gap, then divide by P.
- **Second-order Taylor approximation**: `ΔP ≈ (dP/dy)Δy + ½(d²P/dy²)Δy²`; in percent, `ΔP/P ≈ −D·Δy + ½·C·Δy²`.
  - When to use: quick estimates and mental P&L; the duration term normally dominates (for hedged books built to zero duration, the convexity term can dominate).
  - Failure mode: breaks for very large moves or highly nonlinear payoffs.
- **Portfolio aggregation rules**: `DV01 = Σ DV01ⁱ`; `D = Σ (Pⁱ/P)·Dⁱ`; `C = Σ (Pⁱ/P)·Cⁱ`. Compute security-level sensitivities once and add, valid because all securities share the same single factor.
- **Yield-based DV01, duration, convexity**: special case where y is the security's own yield (modified/adjusted duration). Closed forms below.
  - Two weaknesses: only for fixed cash-flow securities (no options) and implicit parallel yield shifts, so a hedge matching yield-DV01 works only if the two yields move by the same amount.
- **Bullet vs barbell decision**:
  1. Fix the bullet's value and duration; 2. build the barbell from a short and a long bond with `V_S + V_L = V` and `V_S·D_S/V + V_L·D_L/V = D_bullet`; 3. compute portfolio convexity and yield; 4. choose the barbell if you expect volatility above the level that pays for the yield give-up, the bullet if you expect a quiet market.
  - Why it works: duration is linear in maturity, convexity roughly quadratic, so spreading cash flows at constant duration raises convexity and lowers yield.
- **Convexity-aware ALM**: match assets and liabilities on duration and convexity, so the sensitivities stay matched after small moves and rebalancing is rarer.

## Key Concepts
- **Price-rate function P(y)**: price as a function of the single interest rate factor.
- **DV01 (dollar value of an 01)**: price gain for a one-bp fall in rates; positive for standard bonds.
- **Duration**: percent price change per unit rate change, quoted per 100bp; interpretable as PV-weighted average time to receipt for yield-based duration.
- **Modified (adjusted) duration**: Tuckman's yield-based duration = Macaulay duration/(1 + y/2).
- **Effective duration**: general definition, valid for any curve shift and any security.
- **Convexity**: second derivative over price; positive means price-rate curve bows upward and DV01 falls as rates rise.
- **Short convexity position**: hedged book that loses whichever way rates move, e.g. short options, DV01-hedged with futures.
- **Long volatility ≡ long convexity**: gains grow with the square of the rate move.
- **Barbell / bullet**: two-maturity vs single-maturity portfolios with the same duration.
- **Local hedge**: DV01 matches only near the current rate; the P&L curves are tangent, not identical.
- **Curve risk**: exposure to slope changes that a one-factor hedge cannot see.
- **Adjusted notional (conversion-factor notional)**: bond amount comparable to a futures contract, 100/CF (ch14).
- **Pull-in time-weighted PV**: the PV × term column of Table 4.6, whose share of the total is each flow's contribution to risk.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| DV01 (4.1/4.2) | `−ΔP/(10,000Δy)`, `−(1/10,000)dP/dy` |
| Duration (4.10/4.11) | `−(1/P)dP/dy`; `ΔP/P = −D·Δy` |
| Convexity (4.14) | `(1/P)d²P/dy²` |
| Taylor (4.18–4.21) | `P(y+Δy) ≈ P + P′Δy + ½P″Δy²`; `ΔP/P ≈ −DΔy + ½CΔy²` |
| Hedge ratio (4.7) | `F_B = −F_A·DV01_A/DV01_B` |
| DV01 from duration (4.48) | `DV01 = P·D/10,000` |
| Portfolio | `DV01 = ΣDV01ⁱ`, `D = Σ(Pⁱ/P)Dⁱ`, `C = Σ(Pⁱ/P)Cⁱ` |
| Yield-based DV01 (4.34) | `(1/10,000)(1/(1+y/2))[Σₜ₌₁²ᵀ (100c/2)(t/2)/(1+y/2)ᵗ + T·100/(1+y/2)²ᵀ]` |
| Yield-based duration (4.36) | same bracket `÷ P`: PV-weighted times `t/2`, divided by `1+y/2` |
| Closed form duration (4.37) | `D = (1/P)[(100c/y²)(1 − 1/(1+y/2)²ᵀ) + T·100(1 − c/y)/(1+y/2)²ᵀ⁺¹]` |
| Yield-based convexity (4.49) | `C = (1/P)(1/(1+y/2)²)[Σ (100c/2)(t/2)((t+1)/2)/(1+y/2)ᵗ + T(T+.5)·100/(1+y/2)²ᵀ]` |
| Zero coupon | `D = T/(1+y/2)`; `DV01 = T·P/(10,000(1+y/2))`; `C = T(T+.5)/(1+y/2)²` |
| Par bond (c = y) | `D = (1/y)[1 − 1/(1+y/2)²ᵀ]`; `DV01 = D/100` |
| Par convexity (4.52) | `C = (2/y²)[1 − 1/(1+y/2)²ᵀ] − 2T/(y(1+y/2)²ᵀ⁺¹)` (verified numerically; source OCR is garbled) |
| Perpetuity | `D = 1/y`; `DV01 = c/(100y²)` per 100 face with c a decimal rate |

Comparative statics (fixed yield): duration rises with maturity for zeros and par bonds (par duration tends to the perpetuity's 1/y); duration **falls** as coupon rises; duration **falls** as yield rises; DV01 rises with coupon and falls with yield; DV01 of a zero eventually falls back to zero at very long maturity (price effect beats duration effect); very-low-coupon long bonds can have duration above the perpetuity's and then decline toward it. Convexity of a zero grows with T²; a coupon bond is less convex than a zero of equal maturity and yield.

## Mental Models
- **DV01 is a tangent, convexity is how fast the tangent tilts.** Two positions with equal DV01 look identical for tiny moves and diverge by ½·ΔDV01-rate·Δy².
- **Convexity is a bet on volatility.** ½CΔy² is positive for any move if C > 0; if the hedged book is short convexity, you are short vol and must collect enough premium.
- **Duration is trading-desk dollars vs investor percent.** Legs of a hedge have different market values, so hedge in DV01.
- **A coupon bond is a portfolio of zeros**, and each flow contributes PV × time to risk: at 2.1% yield, the last cash flow of a 5-year note is 95.3% of its DV01.
- **Cost of carrying convexity is yield.** The barbell buys convexity by giving up yield (2.663% vs 3.288%); pick it only if expected volatility beats that give-up.

## Worked Example
**1. Hedging a short option with futures.** Short $100mm TYU0C 120; DV01 (per 100) of option 0.03505, of TYU0 0.07442.
- `F = 100,000,000 × 0.03505/0.07442 = $47.098mm` futures bought (recomputed 47.0976mm).
- Value at 2.77%: −100mm × 1.7383/100 + 47.098mm × 119.7061/100 = $54,640,879. After a 5bp fall (prices 1.9194 and 120.0780): $54,634,936. The hedge holds locally (≈ $5.9k drift).
- At ±25bp the hedge is off by ≈ $150k whichever way rates go, versus ≈ $15,625 collected (half a 1/32 tick on the option): the position is **short convexity**. Re-hedge: sell futures if rates rise, buy if they fall.

**2. Yield-based DV01/duration of the 2⅛s of 5/31/2015** at y = 2.092%: price 100.1559, Σ PV × time = 477.7621. DV01 = 477.7621/(1.01046 × 10,000) = 0.04728. D = 477.7621/(1.01046 × 100.1559) = **4.7208**. Convexity: Σ = 2,586 → C = 25.29. A five-year zero at the same yield has C = 5 × 5.5/1.01046² = 26.93, higher, as expected.

**3. Barbell vs bullet** (3⅜s of 11/15/2019: D = 8.033, C = 74.8, yield 3.288%; 5-year 2½s: D = 4.520, C = 23.4, yield 2.025%; 30-year 4⅜s: D = 16.611, C = 389.7, yield 4.221%).
- V₅ + V₃₀ = 100.859mm; duration match gives V₃₀ = 100.859 × (8.033 − 4.520)/(16.611 − 4.520) = **$29.304mm (29.05%)**, V₅ = $71.555mm (70.95%).
- Barbell convexity = 0.7095 × 23.4 + 0.2905 × 389.7 = **129.8** vs 74.8; yield = **2.663%** vs 3.288%.
- Interpretation: barbell wins if rates move a lot, bullet if yields stay put.

**4. Taylor check** on TYU0C 120 for a move to 2.50%: 1.738 + 0.946 + 0.170 = 2.854 (P′ = −350.5, P″ = 46,682.7, Δy = −0.27%); duration term dominates, convexity term fixes the curvature.

## Anti-patterns
- **Hedging with equal DV01s and walking away**: DV01 is local and blind to convexity mismatch; a short-option/futures hedge loses on every large move.
- **Treating yield-DV01 equality as a complete hedge across different bonds**: it presumes both yields move by the same bp; use regression or multi-factor hedges (ch05, ch06) when they do not.
- **Comparing convexity numbers across securities without normalising**: option convexity is thousands of times larger simply because price is small in the denominator; use dollar convexity.
- **Concluding a convex position is "better"**: markets price convexity; long convexity loses to carry if rates stay still.
- **Using duration for hedge sizing between legs of unequal value**: equal durations do not offset dollars.
- **Bumping only one side or from the base price** for numerical derivatives: use symmetric bumps and adequate precision, since second derivatives divide twice by a tiny gap.
- ⚠ **Correction (source arithmetic)**: the book states that the 2⅛s of 5/31/2015 has duration 3.8375 at a 6% yield. Recomputing with (4.36) gives **≈ 4.60**. The direction of the statement (duration falls when yield rises) is right; use 4.60.

## Practitioner Notes
- Traders say "DV01" and mean yield-DV01; check whether a system quotes DVDF (forward-parallel) or DVDZ (zero-parallel) before comparing.
- Investors quote duration; desks quote DV01 in dollars per bp per 100 face or per position.
- Near-par approximation: DV01 (per 100) ≈ D/100 with D from the par formula; a par 5-year at 3.5% has D ≈ 4.55, a 10-year 8.38, a 30-year 18.48; the perpetuity limit at 3.5% is 28.6.
- Half-tick edge on 1/32 (0.015625) for $100mm is $15,625: the payment for making the market and managing the hedge, which convexity losses can exceed in one 25bp move.
- Long convexity is long volatility: expect it to bleed carry (barbell yield 63bp lower than bullet here) in quiet markets.
- Convexity reads: ordinary coupon bonds ≈ 25–400 (5-year to 30-year); the Tuckman futures TYU0 shows a *negative* convexity region at current rates (−14.3 at 2.77%) because of the cheapest-to-deliver switch (ch14).

## Key Takeaways
1. DV01 = −ΔP/(10,000Δy); duration = −(1/P)dP/dy; convexity = (1/P)d²P/dy².
2. Hedge ratio `F_B = −F_A·DV01_A/DV01_B`: opposite sides, smaller size in the higher-DV01 asset.
3. DV01 hedges are local; equal DV01 with unequal convexity means short (or long) volatility and rebalancing needs.
4. ΔP/P ≈ −DΔy + ½CΔy²; the duration term usually dominates.
5. Portfolio DV01 adds; duration and convexity are value-weighted.
6. Yield-based metrics assume parallel yield moves and exclude options; bonds are PV × time bundles, with the final payment dominating.
7. Duration falls with coupon and yield; zero-coupon convexity = T(T+0.5)/(1+y/2)².
8. At equal duration a barbell has more convexity and less yield than a bullet: it is a volatility trade.

## Connects To
- **ch03**: DV01 replaces the "rate change" component of P&L decomposition; yield formulas reused.
- **ch05**: key-rate durations and partial PV01s remove the parallel-shift assumption.
- **ch06**: regression and PCA hedges replace the β = 1 assumption.
- **ch08**: convexity vs drift and volatility, why convex assets have lower yield.
- **ch14**: conversion-factor adjusted notional, futures DV01 and negative convexity regions.
- **ch18**: option delta and gamma as the DV01 and convexity of options.
- **`cfa-level1-curriculum` ch18**: modified/effective duration and convexity on the CFA curriculum.
