# Chapter 5: Understanding Fixed-Income Risk and Return
> **Source**: CFA Program Curriculum 2020, Level I, Reading 46 · Fixed Income | James F. Adams, PhD, CFA, and Donald J. Smith, PhD

## Core Idea
A fixed-rate bond's realized return comes from three sources: coupons and principal, reinvestment of coupons, and any gain or loss at sale measured against the constant-yield carrying value. Rate moves push two of these in opposite directions, so the **investment horizon relative to Macaulay duration** decides which risk dominates. **Duration** is the first-order price sensitivity and **convexity** the second-order one. Choose the right family: *yield* duration (Macaulay, modified, money, PVBP) for option-free bonds, *curve* duration (effective, key rate) when cash flows depend on rates or when you care about the shape of the curve.

## Learning Outcomes Covered
- Calculate and interpret the sources of return on a fixed-rate bond (horizon yield, carrying value).
- Define and calculate Macaulay, modified and effective duration. Explain why effective duration is required for bonds with embedded options.
- Define key rate duration and use it for shaping risk.
- Explain how maturity, coupon and yield affect interest rate risk.
- Calculate portfolio duration and state its limitations.
- Calculate money duration and PVBP.
- Calculate approximate convexity and distinguish it from effective convexity.
- Estimate %ΔP from duration and convexity.
- Describe the term structure of yield volatility.
- Relate holding-period return, duration and horizon (duration gap).
- Explain how changes in credit spread and liquidity move the YTM, and price their effect with duration and convexity.

## Frameworks Introduced
- **Three sources of return (plus the pull to par)**
  1. Promised coupon and principal, received on schedule.
  2. Reinvestment of coupons: the **interest-on-interest** gain.
  3. Capital gain or loss at sale, measured from the **carrying value** on the **constant-yield price trajectory** (amortized cost at the purchase YTM), never from the purchase price.
  - A discount (premium) bond's carrying value accretes (amortizes) to par. That accretion is **interest income**, not a capital gain.
  - **Interest income** = coupons + reinvestment + discount/premium amortization, i.e., the return from the passage of time. **Capital gain or loss** = the return from a change in YTM.
  - The **YTM equals the realized return** only if three conditions hold:
    1. The bond is held to maturity.
    2. There is no default.
    3. Coupons are reinvested at the YTM.
  - The **horizon yield** equals the YTM if coupons are reinvested at the YTM **and** the bond is sold on the trajectory.

- **Two offsetting interest rate risks**
  | Rates move | Coupon reinvestment (FV of coupons) | Market price at sale |
  |---|---|---|
  | Rates ↑ | Gain | Loss |
  | Rates ↓ | Loss | Gain |
  - Buy-and-hold to maturity: **only reinvestment risk**. Selling before the first coupon: **only price risk**.
  - Reinvestment risk grows with a **higher coupon** and a **longer reinvestment period**.

- **Duration gap rule** (`Duration gap = MacDur − Investment horizon`)
  | Situation | Gap | Dominant risk | Investor fears |
  |---|---|---|---|
  | Horizon > MacDur | Negative | Coupon reinvestment | **Lower** rates |
  | Horizon = MacDur | Zero | The two offset (immunized) | — |
  | Horizon < MacDur | Positive | Market price | **Higher** rates |
  - Assumption: a one-time, immediate, parallel shift that hits the YTM and reinvestment rates equally.
  - The gap is "current" only. MacDur and the horizon both change as time passes, so the hedge must be rebalanced.

- **Yield duration vs. curve duration**
  | Family | Measures sensitivity to | Statistics | Use for |
  |---|---|---|---|
  | **Yield duration** | The bond's own YTM | Macaulay, modified, money duration, PVBP, approximate convexity | Option-free fixed-rate bonds |
  | **Curve duration** | A parallel shift in the benchmark curve (usually the government par curve) | **Effective duration**, effective convexity, **key rate durations** | Callables, putables, MBS, floaters, liabilities (pensions); also useful as a supplement on option-free bonds |
  - Why effective duration for embedded options: the cash flows depend on future rates, so the bond has **no well-defined IRR**. Yield-to-worst duration is not the answer.
  - Effective duration requires a **pricing model** with these inputs, held fixed while the curve is shifted up and down:
    - The call protection period.
    - The call schedule.
    - The credit and liquidity spread.
    - Rate volatility.
  - Shrinking ΔCurve does **not** necessarily improve accuracy: refinancing and call decisions only react to moves above a threshold (transaction costs).
  - Even for an option-free bond, **ModDur ≠ EffDur** unless the curve is perfectly flat. Bloomberg example: ModDur 8.482 vs. "OAS duration" 8.510 on a 10y UST. The gap narrows with a flatter curve, a shorter maturity and a price near par.

- **Key rate (partial) duration**: sensitivity to a shift at **one maturity segment**, all else fixed. It captures **shaping risk** (steepening and flattening). `%ΔP ≈ −Σ KeyRateDurₖ × Δrₖ`. For a parallel shift, the sum of the key rate durations equals the effective duration.

- **Properties of Macaulay and modified duration** (option-free)
  | Driver ↑ | Effect on duration | Note |
  |---|---|---|
  | Coupon rate | ↓ | A zero has the highest duration for a given maturity |
  | Yield | ↓ | Heavier discounting puts more weight on near cash flows |
  | Time to maturity | Usually ↑ | **Always ↑ for par and premium bonds** (they approach (1 + r)/r from below). For long, low-coupon **discount** bonds, duration can exceed (1 + r)/r, peak and then decline |
  | Time within a coupon period | ↓ smoothly, jumps up after each coupon | The **saw-tooth** pattern |
  - A zero's MacDur = its time to maturity (N − t/T). A perpetuity's MacDur = (1 + r)/r.
  - **Convexity** rises with a longer maturity, a lower coupon, a lower yield and **greater dispersion of cash flows** (at equal duration).

- **Embedded options and effective duration and convexity**
  - **Callable**:
    - When rates are high, the call option is nearly worthless and the bond behaves like a straight bond.
    - When rates are low, the call caps price appreciation. EffDur falls (shorter expected life) and effective convexity turns **negative**.
    - Price(callable) = Price(straight) − Call value.
  - **Putable**:
    - When rates are high, the put floors the price, so EffDur falls.
    - Convexity is **always positive**.
    - Price(putable) = Price(straight) + Put value.
  - **Both options reduce effective duration** relative to the straight bond (with credit risk held constant).

- **Portfolio duration: two methods**
  1. **Cash-flow-yield method**: the duration of the aggregated cash flows, discounted at the portfolio's IRR (the **cash flow yield**). It is theoretically correct but impractical:
     - Cash flow yields are rarely computed.
     - Option-embedded bonds and floaters have uncertain cash flows.
     - Risk is quoted against benchmark moves, not cash-flow-yield moves.
     - ΔCFY ≠ ΔYTM of the components.
  2. **Market-value-weighted average** of individual durations. This is market practice. It can include **effective durations** of callables and floaters. It is exact only if the curve is flat. **Limitation: it assumes a parallel shift** (every YTM moves by the same amount).

- **Yield volatility × duration**: `%ΔP = (sensitivity per bp) × (number of bp)`. Duration and convexity supply the first factor, yield volatility the second.
  - The **term structure of yield volatility** is often **downward sloping**: short yields respond to monetary policy, long yields to more stable inflation and growth expectations.
  - A 30y bond with ModDur 18 is not necessarily 4× riskier than a 5y bond with ModDur 4.5 if its yield volatility is half as large.

- **Credit and liquidity through duration**: `YTM = benchmark (expected inflation + real rate) + spread (credit + liquidity)`. For an option-free bond the **same** duration and convexity apply to a move in any building block: "inflation duration" = "real rate duration" = "credit duration" = "liquidity duration".
  - In practice the components interact. A **flight to quality** lowers benchmark yields while widening spreads. A downgrade raises both credit risk and liquidity risk.

## Key Concepts
- **Carrying value**: the price on the constant-yield trajectory at the purchase YTM, i.e., the purchase price ± amortized discount/premium.
- **Horizon yield (holding-period rate of return)**: the IRR linking the purchase price to total return (FV of reinvested coupons + sale price or redemption).
- **Macaulay duration**: the PV-weighted average time to receipt of the cash flows, with weights = PV of each cash flow / full price. It is measured in periods, then annualized ÷ periodicity.
- **Modified duration**: MacDur/(1 + r). It gives the linear % change in the **full price** for a change in the annual YTM.
- **Approximate modified duration**: the central-difference slope of the price–yield curve. It converges to ModDur as ΔYield → 0.
- **Effective duration**: the central-difference sensitivity to a parallel shift in the benchmark curve (ΔCurve), from a pricing model.
- **Key rate duration**: sensitivity to a shift at a single maturity point. It measures shaping risk.
- **Money (dollar) duration**: AnnModDur × full price. It gives the price change in currency units.
- **PVBP / PV01 / DV01**: the price change for a 1bp YTM change. **BPV** = money duration × 0.0001. **Bloomberg "Risk"** = PVBP × 100.
- **Convexity**: the second-order term capturing curvature. It is positive for option-free bonds.
- **Effective convexity**: curve-based convexity from a model. It is **negative** for callables at low rates.
- **Money convexity**: AnnConvexity × full price.
- **Cash flow yield**: the IRR of a portfolio's or MBS's aggregated projected cash flows.
- **Term structure of yield volatility**: yield volatility as a function of maturity.
- **Duration gap**: MacDur − investment horizon.
- **Liquidity risk**: transaction cost of selling, visible in the bid–offer spread. It widens with thin trading.

## Formulas & Reference Tables
Notation: r = yield per period; c = coupon rate per period; N = periods to maturity (from the start of the current period); t/T = fraction of the current period elapsed; PMT = coupon per period; FV = par; PV₀, PV₊, PV₋ = full prices at the base, up-shifted and down-shifted yield or curve.
- **Full price**: `PV_Full = Σₖ₌₁ᴺ CFₖ/(1 + r)^(k − t/T)`
- **Macaulay duration (weighted-average form)**: `MacDur = Σₖ (k − t/T) × [CFₖ/(1 + r)^(k − t/T)] / PV_Full`
- **Macaulay duration (closed form)**: `MacDur = {(1 + r)/r − [1 + r + N(c − r)] / [c((1 + r)ᴺ − 1) + r]} − t/T` (in periods)
  - Zero-coupon: `MacDur = N − t/T`. Perpetuity: `MacDur = (1 + r)/r`.
- **Modified duration**: `ModDur = MacDur/(1 + r)`. Annualize: `AnnModDur = ModDur_periods / periodicity`.
- **Duration price estimate**: `%ΔPV_Full ≈ −AnnModDur × ΔYield`
- **Approximate modified duration**: `ApproxModDur = (PV₋ − PV₊) / (2 × ΔYield × PV₀)`. **Approximate MacDur** `= ApproxModDur × (1 + r)`.
- **Effective duration**: `EffDur = (PV₋ − PV₊) / (2 × ΔCurve × PV₀)`
- **Money duration**: `MoneyDur = AnnModDur × PV_Full`, with `ΔPV_Full ≈ −MoneyDur × ΔYield`
- **PVBP**: `PVBP = (PV₋ − PV₊)/2`, with ±1bp shifts
- **Convexity-adjusted estimate**: `%ΔPV_Full ≈ −AnnModDur × ΔYield + ½ × AnnConvexity × (ΔYield)²`
- **Approximate convexity**: `ApproxCon = (PV₋ + PV₊ − 2PV₀) / ((ΔYield)² × PV₀)`
- **Effective convexity**: `EffCon = (PV₋ + PV₊ − 2PV₀) / ((ΔCurve)² × PV₀) = [(PV₋ − PV₀) − (PV₀ − PV₊)] / ((ΔCurve)² × PV₀)`. It is negative when the price gain from a fall in rates is smaller than the loss from a rise.
- **Zero-coupon convexity** (in periods): `Convexity = (N − t/T)(N + 1 − t/T)/(1 + r)²`. Annualize by dividing by **periodicity²**.
- **Money convexity**: `MoneyCon = AnnConvexity × PV_Full`, with `ΔPV_Full ≈ −MoneyDur × ΔYield + ½ × MoneyCon × (ΔYield)²`
- **Portfolio duration (practice)**: `D_p = Σ wᵢ Dᵢ`, with wᵢ = market-value weights
- **Horizon yield**: `r_H = [(FV of reinvested coupons + Sale price)/Purchase price]^(1/H) − 1`
- **Implied spread change**: `ΔSpread ≈ −(%ΔP)/AnnModDur`, with the benchmark unchanged

**Which duration when**
| Question | Statistic |
|---|---|
| % price change for a YTM change, option-free bond | Modified duration (plus convexity for large moves) |
| Currency P&L per 1bp, hedge ratios | PVBP / DV01, or money duration × 0.0001 |
| Horizon that immunizes the YTM | Macaulay duration (the one case where "years" matters) |
| Callable, putable, MBS, liability streams | Effective duration and effective convexity |
| Steepener or flattener exposure | Key rate durations |
| Portfolio risk | Market-value-weighted durations (effective where options exist); assumes parallel shifts |

## Mental Models
- **Duration as a fulcrum in time**: after a one-off rate shock, the price effect (immediate) and the reinvestment effect (it builds over time) cross at the Macaulay duration. Hold for MacDur and the shock washes out.
- **Price change = sensitivity × shock size**: never rank bonds by duration alone. Multiply by the plausible yield move for that maturity (yield volatility), and add convexity when the moves are large.
- **Convexity is bought, not free**: a more convex bond beats a less convex one of equal duration in both rallies and sell-offs. The market prices that in through a lower yield. Negative convexity (callables, MBS) is a short option that is paid for with extra yield.
- **Options shorten duration from either side**: a call bites when rates fall, a put when rates rise. Either way, effective duration < straight-bond duration.
- **A spread is just another yield**: for an option-free bond, a 20bp credit widening and a 20bp Treasury sell-off cost the same. The difference lies in their correlation and liquidity, not in the math.

## Worked Example
**10-year 8% annual bond bought at 85.503075 (YTM 10.40%)**, verified in Python.
- **Duration and convexity**:
  - MacDur = **7.0029**. ModDur = 7.0029/1.104 = **6.3432**. ApproxCon (±1bp) ≈ **55.30**.
  - Money duration per US$1m par = 6.3432 × 855,031 ≈ **US$5.42m**. PVBP ≈ **0.0542** per 100.
- **+50bp shock**:
  - Duration: −6.3432 × 0.005 = −3.172%. Convexity: +½ × 55.30 × 0.005² = +0.069%.
  - Estimate **−3.102%**. Actual repricing at 10.90%: 82.8494, i.e., **−3.104%**.
- **Horizon analysis** after an immediate one-time shift (coupons reinvested at the new rate):
  | New rate | 4-year horizon: FV coupons / sale price / horizon yield | 7-year horizon: horizon yield | 10-year (buy-and-hold) horizon yield |
  |---|---|---|---|
  | 9.40% | 36.8014 / 93.7939 / **11.17%** | **10.408%** | 10.10% |
  | 10.40% | 37.3471 / 89.6688 / 10.40% | 10.400% | 10.40% |
  | 11.40% | 37.8997 / 85.7804 / **9.67%** | **10.407%** | 10.70% |
  - 4y < MacDur: price risk dominates, so higher rates hurt. At 11.40% the capital loss is 3.888, measured against the **carrying value** 89.6688, not the purchase price.
  - 7y ≈ MacDur: **immunized**.
  - 10y > MacDur: reinvestment risk dominates, so lower rates hurt.

**Callable bond, effective statistics** (model prices at ±25bp on the par curve):
- PV₀ = 101.060489, PV₊ = 99.050120, PV₋ = 102.890738.
- EffDur = (102.890738 − 99.050120)/(2 × 0.0025 × 101.060489) = **7.60**.
- EffCon = (102.890738 + 99.050120 − 202.120978)/(0.0025² × 101.060489) = **−285.2**.
- The gain from a 25bp fall (+1.830) is smaller than the loss from a 25bp rise (−2.010). That asymmetry is **negative convexity**.

**Portfolio duration: the two methods disagree** (two zeros, equal market value 9.8m each: a 1y zero at 2.0408% and a 30y zero at 8.0503%)
- Cash flow yield = **7.8611%**. MacDur = **16.28**, ModDur = **15.10**.
- Weighted average: MacDur = **15.50**, ModDur = **14.37**.
- The gap comes from the steep curve. A 10bp move in both YTMs moves the cash flow yield by only about 9.5bp.

## Anti-patterns
- **Measuring capital gains from the purchase price**: use the carrying value. Otherwise pull-to-par accretion gets misclassified as a gain.
- **Using modified or Macaulay duration (or yield-to-worst duration) for callables, putables or MBS**: the cash flows are rate-contingent. Use effective duration.
- **Ranking risk by duration alone**: ignores yield volatility (Example: a lower-duration bond with a bigger plausible yield shock can be the riskiest).
- **Treating portfolio duration as a full risk measure**: it assumes parallel shifts. Add key rate durations for curve reshaping.
- **Using the flat price**: duration and convexity are defined on the **full** price. Accrued interest does not change on the day of the shock, so it is the flat price that moves.
- **Shrinking ΔCurve to "improve" effective duration on option models**: refinancing thresholds make tiny shifts uninformative.
- **Assuming longer maturity always means more risk**: on deep-discount, low-coupon long bonds, duration can fall with maturity. EM example at a 20% YTM: ModDur 4.77 (10y), 5.17 (20y), 5.06 (30y).

## Exam Focus & Traps
- **Buy-and-hold investor**: no capital gain or loss at maturity. The **only** interest rate risk is **reinvestment**.
- **Duration gap sign**: gap = MacDur − horizon. **Positive gap: fears higher rates. Negative gap: fears lower rates.** Example: a 12y 8% par bond has MacDur 8.139, so a 10y horizon gives a gap of **−1.861** (fears lower rates).
- **ModDur < MacDur** whenever the yield is positive.
- **Annualize correctly**: durations ÷ periodicity. **Convexity ÷ periodicity²**. Approximation formulas already give annualized figures when you shift the *annual* yield.
- **Convexity term sign**: always **+½·C·(Δy)²** for option-free bonds, whatever the direction of Δy. Callables can have a negative C.
- **Put option reduces effective duration** (it does not increase it), especially when rates rise. **Putables are always positively convex.**
- **Key rate duration** is the answer for "shaping risk". Modified and effective durations cover parallel shifts only.
- **Pension liabilities**: effective duration from actuarial PVs at ±100bp. Example: (510.1 − 373.6)/(2 × 0.01 × 455.4) = **14.99**.
- **Downward-sloping volatility term structure** ⇒ long yields are more stable than short yields. It does **not** mean short bonds always move more in price.
- **Spread inference**: price 92.25 → 91.25 (−1.084%) with ModDur 7.24 gives a spread widening of ≈ **15bp**, not 100bp.
- **PVBP**: (PV₋ − PV₊)/2 for ±1bp. Money duration per 100 × 0.0001 gives the same thing. Scale by position/100.
- **⚠ Correction (source typos)**:
  - In the 2.875% UST PVBP example, PV₊ is printed once as "101.594327". The correct value is **100.594327** (PVBP = 0.08540).
  - In Example 12 the full price per 100 appears both as "104.495447" and as 104.954472. The consistent value is **104.954472** (USD 10,495,447 per USD 10m par). Money duration ≈ **675.9** per 100.
  - In the 7-year horizon at 9.40%, the reinvestment terms are printed "8 + (1.094)^k" and the total as "74.52177". They should read **8 × (1.094)^k** and **74.512177**.

## Key Takeaways
1. Realized return = coupons + reinvestment + (sale price − carrying value). The YTM is realized only under hold-to-maturity, no default and reinvestment at the YTM.
2. Horizon > MacDur means you fear falling rates. Horizon < MacDur means you fear rising rates. Horizon = MacDur immunizes against a one-off parallel shift.
3. `%ΔP ≈ −ModDur·Δy + ½·Convexity·Δy²`, on the full price, with annualized statistics.
4. Use effective duration and convexity (model-based, curve shifts) for anything with rate-contingent cash flows. Callables become negatively convex at low rates.
5. Duration falls with a higher coupon and a higher yield, and usually rises with maturity, except for long deep-discount bonds.
6. Portfolio duration as a weighted average is practical but assumes parallel shifts. Key rate durations capture shaping risk.
7. Risk = duration × yield volatility. Short-end yields are often more volatile.
8. One duration prices every building block of the yield (benchmark, credit, liquidity) for an option-free bond. Watch for interactions such as flight-to-quality.

## Connects To
- **ch03**: bond pricing, full vs. flat price, accrued interest, spreads (G-, I-, Z-spread, OAS).
- **ch04**: MBS prepayment risk. Why pass-throughs need effective duration and show negative convexity.
- **ch06**: credit spread risk. Spread duration × spread change as the credit return decomposition.
- **ch07**: term structure dynamics (level, slope, curvature) behind key rate and shaping risk.
- **ch09**: valuation of callable and putable bonds with binomial trees. Effective duration and convexity from models.
- **ch13**: immunization and liability-driven investing (duration and convexity matching, rebalancing the gap).
- **`tuckman-fixed-income` ch04**: one-factor risk metrics (DV01, duration, convexity) and hedging.
- **`tuckman-fixed-income` ch05**: multi-factor metrics (key rate and partial PV01s).
- **`cfa-level1-curriculum` ch18**: condensed revision notes on this reading.
