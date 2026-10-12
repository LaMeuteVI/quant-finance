# Chapter 14: Yield Curve Strategies
> **Source**: CFA Program Curriculum 2023, Level III, Reading 13 · Fixed-Income Portfolio Management | Robert W. Kopprasch, PhD, CFA, and Steven V. Mann, PhD. Supplemented by the **2020 L3 refresher reading "Yield Curve Strategies"** (same authors; carry-trade, inter-market and parts of the evaluation-framework sections by Christopher D. Piros, PhD, CFA). Material found only in the refresher is marked **(2020 refresher)**.

## Core Idea
Active rate management means taking deliberate positions against the benchmark in the three yield-curve factors: **level** (≈82% of US Treasury curve moves), **slope** (≈12%) and **curvature** (≈4%). You can also trade **volatility** and cross-currency curve differences.
- Workflow: forecast the curve and compare the forecast with the **forward curve**, which is the market's break-even. Then pick the instrument (cash bonds, leverage/repo, futures, swaps, options) and the structure (duration shift, bullet/barbell, steepener/flattener, butterfly/condor). Measure the exposure with **key rate durations**, and estimate the payoff with the return decomposition plus scenario analysis.
- Duration dominates the outcome, but equal-duration portfolios can perform very differently. Convexity helps only if yields actually move, because its price is a lower yield.

## Learning Outcomes Covered
- Describe the drivers of return from benchmark-yield changes (level, slope, curvature; duration and convexity).
- Position a portfolio when the rate view **coincides** with the market (static curve: buy-and-hold, rolldown, repo carry, sell convexity, receive-fixed swaps, long futures).
- Position when the view **diverges** from the forwards in level, slope or shape (duration management, steepeners/flatteners, butterflies, condors).
- Position for expected changes in **rate volatility** (callable/putable bonds, MBS, bond options, swaptions, options on futures).
- Evaluate portfolio vs benchmark sensitivity with **key rate durations**.
- Discuss yield-curve strategies **across currencies** (hedged/unhedged, carry trades, cross-currency swaps and basis).
- Evaluate the expected return and risk of a yield-curve strategy (return decomposition, scenario analysis, PCA factor scenarios).

## Frameworks Introduced
- **Expected return decomposition (2023, Eq. 1)**:
  `E(R) ≈ Coupon income ± Rolldown return ± E(ΔPrice from benchmark-yield view) ± E(ΔPrice from spread view) ± E(ΔPrice from currency view)`
  - The 2020 refresher version adds `− E(credit losses)`.
  - **Rolling yield** = coupon income + rolldown return. Both are known in advance and contribute *no* risk. Risk comes only from deviations from your curve, spread and FX views.
- **Static-curve strategies (view = forwards, or a stable curve)**:

| Strategy | Return source | Needs | Risk |
|---|---|---|---|
| Buy-and-hold (duration > benchmark, possibly off-the-runs) | Higher coupon from extra duration | Upward slope | Level rise, liquidity (off-the-runs) |
| Roll down / ride the curve | Coupon + price gain as yield falls with maturity | Steep, stable segment | Curve moves to or above the forwards |
| Repo carry trade | (Coupon ± rolldown) − repo financing | Positive carry | Leverage, curve flattening or inversion (negative carry) |
| Long futures | Price appreciation − margin cost (implicit carry) | — | Rates up, margin calls |
| Receive-fixed swap | "Swap carry" (fixed − MRR) + MTM | — | Swap rates up, MRR up, collateral |
| **Sell convexity (2020 refresher)** | Option premium or the extra yield of callables/MBS | Realized vol < implied vol | Large moves in either direction |

- **Carry trade implementation (2020 refresher)**:
  - **Intra-market** (one currency, exploits an upward slope):
    - (a) buy a bond and repo-finance it;
    - (b) receive fixed / pay floating on a swap;
    - (c) buy bond futures. A long futures position *is* a carry trade: by cash-and-carry arbitrage it implicitly earns accrued interest and pays the financing rate.
  - **Inter-market, currency unhedged** (borrow low-rate, lend high-rate):
    - (1) borrow low-rate currency → spot FX → buy the high-yield bond;
    - (2) currency swap: receive high-rate currency, pay low-rate currency;
    - (3) buy the high-yield bond, repo-finance it in its own currency, and buy that currency forward. This synthetically borrows in the low-rate currency, often more cheaply because repo < unsecured.
    - It profits because uncovered interest parity fails empirically. But the return distribution is **fat-tailed and negatively skewed**: crowded exits such as the AUD/JPY unwind in 2008 (AUD fell almost 50%) and the mid-1990s EM carry.
  - **Inter-market, currency hedged**: you must borrow *and* lend in each currency. The trade exploits the **difference in slopes**: receive fixed (or buy futures) on the steeper curve, pay fixed (or sell futures) on the flatter one.
- **Divergent level view (duration management)**:
  - Expect lower yields → lengthen duration (buy long cash bonds, receive-fixed swaps, long futures, long calls or receiver swaptions).
  - Expect higher yields → shorten (sell or switch to short bonds, pay-fixed swaps, short futures, long puts or payer swaptions).
  - Derivatives are preferred for shortening: short-selling bonds has uncertain borrow cost and availability, and derivatives keep duration separate from security selection.
  - **How you add duration matters (2020 refresher)**: two portfolios with the same duration (for example, drop cash vs switch into 6- and 12-year bonds) respond differently to non-parallel moves.
- **Three ways to add duration, sized on PVBP (2020 refresher)**. Target ΔPVBP = (target Dur − current Dur) × MV/10,000.
  1. **Futures**: `N = ΔPVBP / PVBP_fut`, with `PVBP_fut ≈ PVBP_CTD/CF_CTD`.
  2. **Leverage**: buy bonds worth `ΔPVBP × 10,000 / Dur_bond`, funded overnight. Then `Effective duration ≈ (Notional/Equity) × Dur_assets`. With term funding, net out the liability duration. Leverage amplifies credit and liquidity risk.
  3. **Receive-fixed swaps**: `Notional = ΔPVBP / (net swap PVBP per unit notional)`, where net PVBP = PVBP(fixed leg) − PVBP(floating leg). Swaps and futures have no well-defined % duration (their MV ≈ 0), so always work in PVBP.
  - The tenor choice changes the curve exposure. A 5-year swap needs about 2× the notional of a 10-year swap and about 3.6× that of a 20-year swap for the same PVBP.
- **Slope strategies (money-duration-weighted long/short pairs)**:

| View | Structure | Net duration | Wins if | Loses if |
|---|---|---|---|---|
| Duration-neutral steepener | Long short-end, short long-end (BPV-matched) | 0 | Slope ↑ | Flattening |
| Bear steepener | Steepener, net short duration | < 0 | Slope ↑ and/or yields ↑ | Flattening, yields ↓ |
| Bull steepener | Steepener, net long duration | > 0 | Slope ↑ and/or yields ↓ | Flattening, yields ↑ |
| Duration-neutral flattener | Short short-end, long long-end | 0 | Slope ↓ | Steepening |
| Bear / bull flattener | Flattener with net short / long duration | < 0 / > 0 | Slope ↓ and yields ↑ / ↓ | Steepening, opposite level move |

  - Macro mapping:
    - **Bull steepening**: central bank cuts in a recession (e.g., UK 2008).
    - **Bear steepening**: long yields jump on growth and inflation.
    - **Bear flattening**: tightening follows inflation fears.
    - **Bull flattening**: flight to quality.
  - Long-only version (2020 refresher and Exhibit 67): positioned for a **flattener = barbelled** vs the benchmark. Positioned for a **steepener = bulleted**.
- **Curvature strategies (butterflies and condors)**: the butterfly spread is `2 × medium − short − long`. It is usually positive (humped curve).

| Expected scenario (2023 naming) | Yields | Butterfly spread | Position |
|---|---|---|---|
| **Negative butterfly** | Wings ↓, body ↑ | Rises (more curvature) | **Long barbell (wings) / short bullet (body)**. Positive convexity. Also profits if vol is higher than priced. |
| **Positive butterfly** | Wings ↑, body ↓ | Falls (less curvature) | **Long bullet / short barbell**. Short convexity. Earns yield if rates are stable. |

  - **Wing-weighting methods (2020 refresher)**:
    - *Duration-neutral*: equal market value and equal duration, hence money-duration neutral.
    - *50/50*: half the body's money duration to each wing, as used by leveraged dealers. It is cash-neutral only by coincidence and expresses "the body is rich" without a view on how the mispricing resolves.
    - *Regression-weighted*: adjusts for the different yield volatility of the wings, estimated on a short 30–45 day look-back.
  - **Condor (2020 refresher)**: four legs, two duration-neutral pairs. Long 2s/short 5s (profits if the front end steepens) plus short 10s/long 30s (profits if the back end flattens) → profits from *more* curvature. Reverse all legs for less curvature. Pair weights and leverage are discretionary.
- **Volatility strategies**: a bond with an embedded option = option-free bond ± the option.
  - Expect **higher realized vol than implied** → be **long convexity**: putable bonds, long calls/puts on bonds or bond futures, long swaptions, barbells.
  - Expect **low vol** → **sell convexity**: callables, MBS (an implicit short call held by homeowners), written options, bullets.
  - Direction plus vol: long call on bond or futures and long **receiver** swaption add duration and convexity. Long put and long **payer** swaption cut duration and add convexity.
  - Liquidity rule: take pure level views with option-free bonds (more liquid). Use option-embedded bonds only when the view is on volatility.
  - **Buying convexity with options (2020 refresher)**: sell part of the long bond to buy near-the-money calls on bond futures, sized by the PVBP ratio (option par = bond par × PVBP_bond/PVBP_option), and keep money duration constant.
    - The option convexity was about 826 vs about 6 for the 30-year bond.
    - Result: +0.83% at −75bp and +0.95% at +75bp, but −0.23% if rates are unchanged. You win whenever |Δy| > ~25bp before expiry.
    - Mirror image: switching a 5-year Treasury into 30-year FNMA 3% MBS (similar duration) *sells* convexity. It wins about +0.17% if rates are flat and loses about 1.1% at −75bp.
- **Key rate duration (KRD) framework**:
  - Definition: `KRD_k = −(1/PV) × ∂PV/∂r_k`, and `Σ KRD_k = effective duration`.
  - Use active KRD = portfolio KRD − benchmark KRD to spot "shaping risk" that total duration hides.
  - Estimated P&L: `ΔV ≈ −Σ_k (partial PVBP_k × Par) × Δy_k (bp)`.
  - Map a KRD profile to derivatives: negative active KRD at a tenor = pay-fixed swap or short futures there; positive = receive-fixed or long futures.
  - **(2020 refresher)**: partials are computed by moving one curve point and interpolating neighbours (Yield Book: 1, 2, 3, 5, 10, 20, 30y). A 7-year bond is captured by interpolating the 5y and 10y points. **Partial PVBP (PDV01)** = price change for ±10bp at one point ÷ 20.
- **Cross-currency framework**:
  - Domestic return: `R_DC = (1 + R_FC)(1 + R_FX) − 1`. For a portfolio, `R_DC = Σ ωᵢ(1 + R_FC,i)(1 + R_FX,i) − 1`.
  - Fully hedged with forwards → earn the **domestic** risk-free rate (covered interest parity). A higher-yielding currency trades at a forward discount.
  - Unhedged carry profits when the **forward-rate bias** persists (UIP fails).
  - A **fixed-fixed cross-currency swap** = receive-fixed domestic IRS + cross-currency basis swap (floating vs floating ± basis) + pay-fixed foreign IRS. Dropping one leg isolates a view. For example, skip the pay-fixed USD swap to keep the USD rate view while the FX stays hedged.
  - Three risks of a cross-currency curve trade: the overweight currency's curve, the underweight currency's curve, and FX.
  - **Cross-currency basis**: persistently negative for JPY and EUR after 2008 (a CIP violation). Du, Tepper and Verdelhan explain it by (1) balance-sheet and regulatory costs of arbitrage and (2) supply–demand imbalances between high-rate and low-rate currencies.
- **Inter-market strategy rules (2020 refresher)**:
  - Two markets share one yield curve only with (1) perfect capital mobility **and** (2) an exchange rate credibly fixed *forever*. So "it's really all about the currency", even when hedged.
  - Always compare markets on **hedged returns** (forward FX), never on local or spot-converted returns. Once hedged, the base currency is irrelevant: the best assets are the best for everyone.
  - Take currency exposure only if you expect the currency to beat its *forward* rate, not merely to appreciate.
  - A bond hedged with rolling 3-month forwards = long the foreign curve out to maturity + short foreign 3-month rate + long domestic 3-month rate. You carry a residual bet on the **short-end rate spread**.
  - **Convergence trade** (Greek vs German/EUR, 2020 refresher): pair the long bond with a pay-fixed **asset swap** to separate spread duration from overall duration. It wins if Greek yields fall *or* EUR swap rates rise, at the cost of lower running cash flow (Euribor + spread < coupon).
- **Scenario and risk framework**:
  - Risk = deviations from the view. Rolling yield carries none.
  - Use a few pertinent scenarios, including the one where **the trade thesis breaks down entirely**. Use many scenarios only to compute summary statistics.
  - **(2020 refresher)** Use ±1σ PCA shocks to **shift** (non-parallel level), **twist** (slope) and **butterfly** (curvature). They are uncorrelated, so the 2³ = 8 composite scenarios are simple sums of the single-factor impacts.
  - Leveraged investors should also stress for the rate or FX move that triggers a margin call or forced unwind.

## Key Concepts
- **Level / slope / curvature**:
  - Level: a parallel shift.
  - Slope: e.g., **2s30s** = 30y − 2y yield (127bp in July 2020). A negative slope means an inverted curve.
  - Curvature: the butterfly spread. Positive = humped (concave) curve, negative = saucer (convex) curve.
- **Constant-maturity yield**: an interpolated yield for an exact tenor. Model-dependent. Including off-the-runs "pulls" the curve up, and spot and forward curves amplify model differences.
- **Bullet / barbell / ladder**:
  - Bullet: maturities concentrated around one point (low dispersion, low convexity).
  - Barbell: maturities at both ends (high convexity).
  - Ladder: evenly spread.
- **Rolldown return**: price change as a bond ages along an unchanged upward-sloping curve. It turns *negative* for zeros with negative yields (premium amortization).
- **Repo carry / swap carry**: repo carry = asset yield − repo rate. Swap carry = fixed rate − MRR (receive-fixed).
- **Basis point value (BPV/PVBP)**: `ModDur × MV × 0.0001`. Futures: `BPV_CTD/CF_CTD`. Swap: `ModDur_swap × Notional/10,000`.
- **Implicit leverage of derivatives**: MTM moves are large relative to the margin or collateral posted. CCP clearing extends margining to OTC swaps, so you must hold cash or eligible collateral.
- **Key rate (partial) duration**: sensitivity to one tenor's yield with the others held constant. Sums to effective duration.
- **Shaping risk**: exposure to changes in curve shape that are invisible in total duration.
- **Payer / receiver swaption**: the right to pay fixed (short duration) / receive fixed (long duration).
- **Cross-currency basis**: the gap between the direct USD rate and the synthetic USD rate obtained by swapping another currency. Negative means synthetic USD is more expensive.
- **Forward-rate bias**: forwards are empirically biased predictors of future spot FX. This is the basis of carry.
- **Condor (2020 refresher)**: a four-leg curvature trade made of two duration-neutral pairs.
- **Structured notes (2020 refresher)**: inverse floaters (levered), deleveraged floaters, range accruals, extinguishing accruals, rate-differential notes, ratchet floaters, dual-currency / power-reverse duals. They give customized front-end curve bets but are illiquid and complex. Orange County (1994) lost USD 1.5bn of 7.5bn with repo-levered inverse-floater-type notes as the Fed hiked.

## Formulas & Reference Tables
- **Price change**: `%ΔPV_Full ≈ −ModDur × Δy + ½ × Convexity × (Δy)²`. This uses "raw" convexity. Vendors often report convexity ÷ 100. A zero's raw convexity ≈ duration².
- **Portfolio statistics**: `AvgModDur = Σ ModDur_j × MV_j/MV` and `AvgConvexity = Σ Convexity_j × MV_j/MV`. With short positions, MV_j < 0 and the denominator is the *net* MV.
- **Butterfly spread**: `= −y_short + 2y_medium − y_long`.
- **Effective duration and convexity**:
  - `EffDur = (PV₋ − PV₊)/(2 × ΔCurve × PV₀)`.
  - `EffCon = (PV₋ + PV₊ − 2PV₀)/(ΔCurve² × PV₀)`.
- **Key rates**: `KRD_k = −(1/PV)(ΔPV/Δr_k)`, and `Σ KRD_k = EffDur`.
- **Futures BPV**: `≈ BPV_CTD / CF_CTD`. For a fixed-basket contract (e.g., Australian bond futures), it equals the basket's BPV.
- **Swap BPV**: `= ModDur_swap × Notional / 10,000`.
- **Hedge or extension sizing**:
  - Futures: `N_f = ΔBPV_target / BPV_fut`.
  - Swap: `Notional = ΔBPV_target / BPV per unit notional`.
  - Leverage: `ΔMV = ΔBPV × 10,000 / Dur` and `EffDur ≈ (Notional/Equity) × Dur_assets` (2020 refresher).
- **Duration-neutral barbell weights (2020 refresher)**: `D_body = w·D_short + (1 − w)·D_long`, so `w = (D_long − D_body)/(D_long − D_short)`.
  - Convexity gain = Σ w·C (wings) − C_body.
  - Yield give-up = Σ w·y (wings) − y_body.
- **Forward vs forecast rule (2020 refresher)**: a bond beats the one-period rate if its forecast horizon yield is **below** its implied forward yield.
  - `Excess ≈ −Dur_horizon × (forecast yield − forward yield)`. Pick the bond with the largest product of that yield gap and horizon duration.
  - Total return ≈ −Dur_end × (y_end − y_begin) + y_begin (annual par bond, one-year horizon). Use the *ending* duration because the price change is taken at the horizon.
- **Currency**:
  - `R_DC = (1 + R_FC)(1 + R_FX) − 1`.
  - Covered interest parity: `F(DC/FC) = S₀(DC/FC) × (1 + r_DC)ᵀ/(1 + r_FC)ᵀ`.
  - Hedged foreign return ≈ local return + (F/S − 1), with the quote in base currency per unit of foreign currency (2020 refresher).
- **Money-market carry (MXN example)**: `Return = Π(1 + r_MXN,q/4) × S₀/S₁ − (1 + r_USD)`, with S quoted as MXN per USD.
- **Relative performance of structures vs a ladder or benchmark at equal duration (2020 refresher, Exhibit 67)**:

| Scenario | Barbell | Bullet |
|---|---|---|
| Parallel shift (either direction) | Outperforms (convexity; small, ≈25bp per ±100bp) | Underperforms |
| Flattening | Outperforms | Underperforms |
| Steepening | Underperforms | Outperforms |
| Less curvature | Underperforms | Outperforms |
| More curvature | Outperforms | Underperforms |
| Lower rate volatility | Underperforms | Outperforms |
| Higher rate volatility | Outperforms | Underperforms |

  - Magnitudes on USD 60m at duration 7.6, Dec-2015 curve:
    - An *extreme* 2s/30s barbell (convexity 1.578 vs 1.134, yield −29bp): +1.12% if flatter, −1.00% if steeper, −1.04% with less curvature, +1.02% with more.
    - An extreme 7s/10s bullet mirrors this (≈ −1.24%, +1.10%, +1.44%, −1.41%).
    - A *less extreme* four-bond barbell deviates only ±14bp.
    - Lesson: convexity pays only if you add a meaningful amount, and doing so is a slope and curvature bet.

## Mental Models
- **Forwards are the market's break-even.** A static curve and the forwards are different forecasts. If the curve rolls exactly to the forwards, *every* tenor earns the short rate. Any position is a bet that the realized curve differs from the forwards (2020 refresher).
- **Convexity is an option: it costs yield (theta) and pays on movement (gamma).** Buy it before large, fast moves or rising vol. Sell it (callables, MBS, written options, bullets) when you expect realized vol below implied vol.
- **Think in money duration and KRD buckets, not average duration.** Two portfolios with duration 5.3 can have opposite curve bets. Read the active KRD vector like a list of swap and futures positions.
- **Every curve trade is a sum of a level bet and shape bets.** Neutralize the ones you don't want: BPV-match the legs for pure slope, and use 3–4 legs for curvature. Add net duration deliberately (bull/bear variants).
- **Across borders, compare on hedged returns, then decide separately whether to own the currency relative to its forward.** Covered parity makes a hedge a short-rate spread trade, not a free lunch.

## Worked Example
**1) Duration-neutral steepener, then a butterfly (2023; recomputed).**
- Bonds at par: 2y (ModDur 1.994, convexity 5.0), 5y (4.88, 26.5), 10y (9.023, 90.8).
- **Steepener**: long USD 163.8m 2y, short USD 36.2m 10y. Net MV = 127.6m.
  - Duration = (1.994×163.8 − 9.023×36.2)/127.6 ≈ **0**. Convexity = (5×163.8 − 90.8×36.2)/127.6 = **−19.34** (short the convex leg).
  - +25bp parallel: −0.5 × 19.34 × 0.0025² × 127.6m ≈ **−USD 7.7k** (convexity cost only).
  - Slope +50bp (2y −25bp, 10y +25bp):
    - 2y leg = 163.8m × (1.994×0.0025 + ½×5×0.0025²) = +819,102.
    - 10y leg = −36.2m × (−9.023×0.0025 + ½×90.8×0.0025²) = +806,310.
    - Total **+USD 1.63m**.
- **Bull steepener variant**: raise the 2y to 213.8m. Duration = 0.561 and BPV ≈ USD 9,969, so a 25bp larger fall in 2y yields adds ≈ USD 249k.
- **Negative-butterfly trade**: long 110m 2y, short 248.3m 5y, long 110m 10y.
  - BPVs: +21,934, −121,170, +99,253. The sum is ≈ 0, so the trade is duration-neutral. Convexity = −139.9 on the net short MV of −28.3m, which is *positive* convexity exposure in money terms.
  - Scenario: 2y and 10y −25bp, 5y +50bp. BPV estimate = 25×21,934 + 50×121,170 + 25×99,253 = **USD 9.09m**. With convexity = **USD 9.04m**.
  - Why lower: the 5y moves twice as much, so the short body's convexity term dominates.

**2) Forward-vs-forecast bond selection and the return decomposition (2020 refresher, AusBank; figures as given).**
- Setup: benchmark duration 2.00 ± 0.30, and the manager is highly confident of **+60bp** parallel within 12 months. The annual par curve is 1y 1.50%, 2y 1.91%, 3y 2.23%, 4y 2.50%, 5y 2.74%, 6y 2.95%.
- Stable-curve (rolldown) returns rise with maturity (6y: 3.92%). Under the +60bp forecast, compare each bond's forecast yield with its implied forward:

| Bond | Implied forward (1y ahead) | Implied change | Forecast | Holding return |
|---|---|---|---|---|
| 2y | 2.33% | +83bp | 2.10% (+60bp) | **1.72%** (best) |
| 5y | 3.27% | +53bp | 3.34% | 1.41% |
| 6y | 3.46% | +51bp | 3.55% | 1.18% |

  - Rule: the 2y's forecast yield is 23bp below its forward. At a horizon duration of 0.98 this adds about 22bp over the 1.50% one-year rate: `−0.98 × (2.10 − 1.91) + 1.91 ≈ 1.72%`.
  - Bonds whose forecast yield exceeds their forward (5y, 6y) return less than the one-year rate.
- Decision: go 100% into the 2y (duration 1.944, inside the band).
- Decomposition vs keeping the initial six-bond portfolio (+60bp):
  - Yield income: 1.91% vs 2.01% (−10bp).
  - Rolldown: 0.404% vs 0.463% (−6bp).
  - Price effect from the view: −0.584% vs −0.777% (+19bp).
  - Net: **1.73% vs 1.70%**, +3bp.
- Caveat: held for the full year, the 2y would drift below the lower duration bound (1.70) within 3–4 months, so the position needs rebalancing.

**3) Barbell vs bullet with a currency overlay (2023, AUD zeros; recomputed).**
- The view is AUD zero yields −60bp and AUD +0.25% vs USD. Both portfolios have horizon duration 3.95. Start price 98.
- Rolldown: bullet 99.75 → +1.786%. Barbell 100.00 → +2.041%.
- Rate effect: −3.95 × (−0.006) + ½ × C × 0.006² gives 2.405% (C = 19.5) and 2.431% (C = 34).
- USD return: bullet `(1 + 0.017857 + 0.024051)(1.0025) − 1 = 4.451%`. Barbell = **4.733%**.
- The barbell wins by 28bp: about 25.5bp from rolldown (its long zero rides a steeper segment) and about 2.6bp from convexity.
- Same pattern in the USD case with +50bp: bullet −0.369% vs barbell −0.105%.

**4) Cross-currency carry (2023 MXN example; recomputed).**
- Borrow USD for one year at 1.85%. Roll 90-day MXN bills at 7.70% → 7.85% → 8.15% → 8.20%. The spot MXN/USD moves from 19.15 to 19.65.
- Return = (1.01925)(1.019625)(1.020375)(1.0205) × 19.15/19.65 − 1.0185 = **+3.61%**.
- That is well below the 6.08% expected with stable rates and FX. A 2.6% peso depreciation erased more than the rise in MXN rates added. (In Q1 2020 the MXN fell about 25% in roughly a month.)

## Anti-patterns
- **Reading average duration as the whole story**: equal durations hide opposite slope and curvature bets. Compare KRD vectors against the benchmark.
- **Buying convexity for a slow-moving view**: the yield give-up accrues every day. In the options example, returns were negative if |Δy| < ~25bp. In the Brazil example, a 60/40 3y/30y barbell against the 10y gained 0.528 convexity (scaled) for **−127bp** of yield.
- **Treating a static curve as "rates unchanged = forwards realized"**: rolldown profits require the curve to stay put, *not* to roll to the forwards.
- **Comparing foreign bonds on local or spot-converted returns**: use forward-hedged returns, then decide on currency separately (2020 refresher).
- **Sizing swaps and futures on notional or "duration %"**: they have ≈ 0 MV. Size on PVBP, and use the CTD for futures.
- **Short-selling cash bonds to cut duration**: borrow costs and availability are uncertain. Use pay-fixed swaps or short futures.
- **Crowded carry trades**: negative skew and forced unwinds (yen carry). Unwind before rate or FX moves exceed the accumulated carry.
- **Leveraged structured-note bets on a static front end**: Orange County (2020 refresher).
- **Extreme barbells or bullets on a weak slope/curvature conviction**: they swing about ±100bp vs a ladder. A less extreme structure caps the deviation at about ±14bp.

## Exam Focus & Traps
- **Callable vs putable vs option-free**:
  - Yields ↓: option-free > callable (short call, gains capped).
  - Yields ↑, least to most decline: **putable < callable < option-free** (the long put gains value; the short call loses value, which cushions the callable).
  - A long callable is *short* vol. A long putable is *long* vol.
- **Swaption direction**: expect higher rates → **long payer** swaption or **long put on bond futures**. A short payer is wrong: it loses when rates rise.
- **KRD → derivatives mapping** (Example 11): active KRDs −2.82 (5y), −0.29 (10y), +2.93 (30y) → **pay-fixed 5y swap, short 10y futures, receive-fixed 30y swap**.
- **Butterfly naming**:
  - In the 2023 reading, a *negative butterfly* = the butterfly spread rises (wings ↓, body ↑) → long wings / short body.
  - The 2020 refresher's PCA labels are arbitrary. There, a "positive butterfly" factor = ends ↓ and middle ↑. **Always reason from the yield moves, not the label.**
- **Bullet vs barbell and slope**: flattening → barbell. Steepening → bullet. More curvature or more vol → barbell. Less curvature or low vol → bullet. The refresher Example 3 wording: in a steepener with low vol, the bullet wins *and* picks up yield (+32bp) by giving up convexity.
- **Condor for less curvature**: short 2s, long 5s, long 10s, short 30s, all legs with equal |money duration|. With 30s capped at USD 100m and PVBP per USD 1m of 198/480/880/1,972, the position is **short 996m 2s, long 411m 5s, long 224m 10s, short 100m 30s**.
- **Pay-fixed overlay** (Example 6): the USD 100m index (ModDur 5.299) plus a USD 50m pay-fixed 5y swap (ModDur 4.32) → duration 3.139. BPV falls by 21,600, which saves ≈ USD 540k on +25bp.
- **Replicating a cash position with futures**: 10y BPV USD 18,524 ÷ (88.40/0.684 = 129.24) = **≈143 contracts**.
- **Bond vs receive-fixed swap** (Example 3, £100m, −50bp, 6 months):
  - Bond: coupon £1.125m + price £4.338m (of which rolldown £0.262m).
  - Swap: carry £1.1305m + MTM £4.234m. The duration approximation 8.318 × 100m × 0.005 = £4.159m.
  - The swap uses only collateral, not the full price.
- **Inverted-curve trap** (Example 4): long-duration buy-and-hold *gains* when long yields fall. The repo carry turns negative. Coupons reinvest at the higher short rates.
- **Hedged foreign zero** (2023): a German investor in a 2y UST zero hedged at F = 1.1870 vs S = 1.1218 earns **−0.60%** a year, which is the German 2y yield, as CIP requires. Unhedged over one year: R_FC 4.57%, R_FX 1.70%, **R_DC 6.34%**.
- **Bear flattening abroad with a stable, upward domestic curve**: the best carry is **receive floating foreign / pay floating domestic**. Foreign short rates rise most, and the domestic short end is the cheapest funding.
- **PCA scenario risk (2020 refresher Ex. 8)**:
  - With equal duration (7.01), the bullet is hit hardest by the empirical *shift*, which is humped: the belly moves most. Duration understates the bullet's level risk.
  - σ over the 8 composite scenarios: ladder 0.860%, barbell 0.843%, bullet 0.901%.
  - The ladder is the most immune to twist and butterfly moves (range ±0.18% vs about ±0.29% for the barbell and bullet).

## Key Takeaways
1. Start from `E(R) ≈ coupon + rolldown ± rate view ± spread view ± FX view`. Only the "view" terms carry risk.
2. With a static view, add duration or leverage: buy-and-hold, rolldown, repo carry, receive-fixed swaps, long futures, sell convexity. With a divergent view, trade level, slope or curvature explicitly.
3. Size every overlay on PVBP: `BPV_fut ≈ BPV_CTD/CF`, `BPV_swap = ModDur × N/10,000`, and leverage ≈ (Notional/Equity) × Dur.
4. Flattener or more curvature or more vol → barbell / long wings. Steepener or less curvature or calm markets → bullet / long body. Add net duration for bull or bear variants.
5. Convexity costs yield and pays only on large, timely moves. Check the break-even move (about ±25bp in the option example).
6. Use KRDs against the benchmark to find and express shaping bets. The partials sum to effective duration.
7. Across currencies, compare hedged returns, treat the hedge as a short-rate spread bet, and take FX exposure only against the forward. Carry trades earn in calm markets and crash in crowded exits.
8. Evaluate strategies with scenario analysis: the thesis-failure scenario plus ±1σ shift/twist/butterfly composites (2020 refresher).

## Connects To
- **ch05**: duration, convexity and the price approximation used throughout.
- **ch07**: term structure, forward rates, rolling down the curve, PCA of level/slope/curvature.
- **ch09**: embedded options, effective duration and convexity, callable/putable behaviour.
- **ch12**: the return-decomposition model and the leverage and repo tools.
- **ch13**: bullet/barbell/ladder in immunization, futures BPV and the CTD, swaps as duration tools.
- **ch15**: the credit-spread terms of the return decomposition.
- **`ilmanen-yield-curve` ch05**: convexity bias, i.e. why convex long bonds yield less (the "price" of convexity here).
- **`ilmanen-yield-curve` ch06**: framework for analyzing curve trades, including duration-neutral flatteners and barbell vs bullet break-evens.
- **`tuckman-fixed-income` ch04–05**: DV01 and key-rate/multi-factor hedging. **ch14**: note and bond futures, CTD and conversion factors. **ch16**: swaps.
- **`cfa-derivatives` ch06**: swap, futures and forward strategies. **ch07**: currency management (hedging, forward-rate bias, carry).
- **`cfasi-fixed-income-guides`**: practitioner implementation of duration, curve and unconstrained bond strategies.
