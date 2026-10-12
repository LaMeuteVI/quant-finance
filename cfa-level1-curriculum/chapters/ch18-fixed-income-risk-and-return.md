# Chapter 18: Understanding Fixed-Income Risk and Return (Fixed Income)

## Core Idea
Bond returns come from coupons, from reinvesting them, and from price changes at sale (plus the pull to par along the constant-yield trajectory). **Duration** gives the first-order price sensitivity to yield changes and **convexity** the second order. Whether *reinvestment risk* or *market price risk* dominates depends on the investment horizon relative to Macaulay duration.

## Frameworks Introduced
- **Sources of return**:
  1. Coupons and principal.
  2. Reinvestment of coupons.
  3. Capital gain or loss at sale, measured against the **carrying value** on the constant-yield trajectory (not the purchase price).
  - The **horizon yield** equals the YTM only if coupons are reinvested at the YTM and the bond is sold on the trajectory.
- **Two offsetting risks**:
  - Rates ↑ → the reinvestment value rises, the sale price falls.
  - Rates ↓ → the reverse.
  - A buy-and-hold investor faces only reinvestment risk.
- **Yield duration statistics**:
  - **Macaulay duration**: the PV-weighted average time to the cash flows.
  - **Modified duration**: `ModDur = MacDur/(1 + r)`, with r the yield per period. Then `%ΔPV_full ≈ −AnnModDur × ΔYield`.
  - **Approximate ModDur**: `(PV₋ − PV₊)/(2 × ΔYield × PV₀)`.
  - **Approximate MacDur** = ApproxModDur × (1 + r).
  - **Money duration** = AnnModDur × PV_full.
  - **PVBP (PV01)** = (PV₋ − PV₊)/2 for a 1bp shift.
- **Curve duration statistics**:
  - **Effective duration**: sensitivity to a parallel shift of the benchmark curve. Required for bonds with embedded options and MBS, where cash flows depend on rates.
  - **Key rate (partial) duration**: sensitivity to one maturity point, which captures non-parallel shifts.
- **Properties of duration**:
  - A zero-coupon bond's MacDur = its maturity.
  - A perpetuity's MacDur = (1 + r)/r.
  - Lower coupon or lower yield → higher duration.
  - Longer maturity → usually higher duration. For deep-discount bonds, duration can peak above (1 + r)/r and then fall.
  - Between coupon dates MacDur declines smoothly, then jumps up after each payment (a saw-tooth pattern).
- **Embedded options**:
  - **Callable**: the call caps the price when rates are low, so effective duration is *lower* than a straight bond's when rates fall. The bond shows **negative convexity**.
  - **Putable**: the put floors the price when rates are high, so effective duration is *lower* when rates rise.
- **Portfolio duration**: the weighted average of individual durations (practical, assumes parallel shifts) or the duration of the aggregate cash flows (theoretically correct).
- **Convexity**:
  - `%ΔPV_full ≈ −AnnModDur × Δy + ½ × AnnConvexity × (Δy)²`.
  - Approximate convexity = `(PV₋ + PV₊ − 2PV₀)/((Δy)² × PV₀)`.
  - **Effective convexity** is the same formula using benchmark-curve shifts.
  - **Money convexity** = convexity × PV_full.
  - Convexity is higher for longer maturity, lower coupon and lower yield.
  - Positive convexity helps both when yields fall and when they rise.
- **Investment horizon vs Macaulay duration (duration gap = MacDur − horizon)**:
  - Horizon > MacDur (negative gap): reinvestment risk dominates, so the investor fears **falling** rates.
  - Horizon = MacDur: the two risks offset. This is **immunization**.
  - Horizon < MacDur (positive gap): price risk dominates, so the investor fears **rising** rates.
- **Term structure of yield volatility**: short-term yields are usually more volatile.

## Key Concepts
- **Carrying value**: price on the constant-yield trajectory (amortized cost).
- **Yield vs curve duration**: sensitivity to the bond's own YTM vs to the benchmark curve.
- **OAS duration**: effective duration computed with an OAS model (as on Bloomberg).

## Mental Models
- **Duration = the time needed to be immunized.** Match the horizon to MacDur to lock in the YTM.
- **Convexity is the investor's friend and the issuer's call option is its enemy.**
- **Use effective duration whenever cash flows depend on rates** (callables, MBS).

## Anti-patterns
- **Using modified duration for callable bonds or MBS**: their cash flows change with rates.
- **Using duration alone for large yield moves**: add convexity.
- **Assuming parallel shifts in a portfolio**: use key-rate durations.

## Worked Example
**10-year 8% annual bond at a 10.40% YTM (from the notes, verified).**
- Price = **85.50**. MacDur = **7.0029**. ModDur = 7.0029/1.104 = **6.3432**. Approximate convexity ≈ 55.3.
- If the yield rises by 50bp:
  - Duration estimate: −6.3432 × 0.005 = −3.17%.
  - Convexity correction: +½ × 55.3 × 0.005² = +0.07%.
  - Total ≈ **−3.10%**.

**Treasury accrued interest (from the notes).** A 2.875% semiannual Treasury, 59 of 184 days into the coupon period:
- AI = 59/184 × 2.875/2 = 0.4609.
- Flat price 100-07 = 100.21875, so the full price = **100.6797**.

## Key Takeaways
1. Returns come from coupons, reinvestment and price change relative to the carrying value.
2. ModDur = MacDur/(1 + r). %ΔP ≈ −ModDur·Δy + ½·Convexity·Δy².
3. Effective and key-rate durations are needed for option-embedded bonds and non-parallel shifts.
4. Calls reduce duration when rates fall (negative convexity). Puts reduce duration when rates rise.
5. Horizon = MacDur immunizes: price risk and reinvestment risk offset each other.

## Connects To
- **Ch 16**: pricing and yields.
- **Ch 17**: MBS and negative convexity.
- **Ch 19**: spread duration and credit.
- **Hull Ch 4 / Ch 6** (`hull-derivatives`): duration hedging with futures.
