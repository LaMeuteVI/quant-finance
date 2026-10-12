# Chapter 14: Note and Bond Futures
> **Source**: Tuckman & Serrat, *Fixed Income Securities* (3rd ed.), Chapter 14, "Note and Bond Futures" | Bruce Tuckman, Angel Serrat

## Core Idea
A U.S. Treasury futures contract has no single underlying: the short delivers any bond from a basket, priced through a **conversion factor**, and picks the **cheapest-to-deliver (CTD)**. The futures price is therefore the bond price/conversion-factor of the CTD (minimum over the basket) at delivery, and before delivery it sits *below* every bond's converted forward price by the value of the embedded **quality option** (plus the small timing and end-of-month options). Every hedge, basis trade and futures valuation reduces to understanding the net basis, which is the price of that optionality.

## Frameworks Introduced
- **Cost of delivery / CTD rule**: `CoD_i = P_i − cf_i × F` (accrued cancels). The short delivers the bond with the lowest cost of delivery.
  - When to use: identifying the CTD at delivery or when computing the final settlement price.
  - How: (1) list the basket with conversion factors; (2) compute `P_i/cf_i` for each bond (for a flat-accrued bond); (3) the minimum ratio is the CTD and equals the futures price at last delivery; (4) all other bonds have CoD ≥ 0.
  - Why it works: if F > min(P/cf) buy the CTD, sell futures, deliver for a riskless profit; if F < min(P/cf) sell the CTD, buy futures, and whichever bond the short delivers you re-buy the CTD and sell the delivered bond, again a riskless profit. So F_T = min_i(P_i/cf_i).
- **Conversion-factor approximation**: `cf ≈ price per 1 face of the bond at a yield equal to the notional coupon (6%)`, with maturity rounded down to the nearest quarter (CME rule for 10y notes).
  - When to use: to see which bonds are cheap or rich in the delivery ruling and to predict CTD drift.
  - Failure mode: exact only if the curve is flat at the notional coupon. Away from 6% the mismatch between the fixed cf and true prices creates the CTD switching.
- **CTD as a function of yield (duration rule)**: with yields above the notional coupon, the highest-duration bond becomes CTD; below the coupon, the lowest-duration bond becomes CTD. In addition, anything that cheapens a bond (steeper curve cheapens long bonds, flatter curve cheapens short bonds, idiosyncratic richening or cheapening) makes it more likely CTD.
  - Why: the slope of the converted price-yield curve `(1/cf) dP/dy` at 6% ≈ −duration of the bond. Conversion factors are fixed, so as yield rises the long-duration bond's price falls most and its P/cf drops below the others.
- **Gross basis / net basis**: `GB = P − cf·F`; `NB = P_fwd − cf·F = GB − carry`.
  - When to use: quoting (gross) and analysing (net) basis trades; NB is the price of the quality option for that bond.
  - How: long basis = long bond (financed in repo or forward) + short `cf × G` futures (tailed); short basis = the opposite.
  - P&L: delivery-date P&L of a properly tailed long basis = `G × (NB_end − NB_start)`.
- **Futures as lower envelope**: at delivery F is the lower envelope of converted price curves, hence negatively convex in yield; its DV01 looks like the long-duration bond at high rates and the short-duration bond at low rates.
- **Tree pricing of the quality option**: at delivery-date nodes compute `P_i/cf_i` for all bonds, set F = minimum, then roll back with the Chapter 13 futures recursion (futures price = expected next futures price under the risk-neutral measure). Calibrate by attaching an OAS to each bond so the model forward equals the market forward (bond forwards assumed fair).

## Key Concepts
- **Delivery basket**: set of eligible Treasuries defined by maturity rule (10y note: 6.5 to 10 years remaining at the first day of the delivery month; TYU0 basket had 16 bonds).
- **Conversion factor (cf)**: exchange-published factor that scales the delivery price of each bond; equals 1 for a 6% coupon bond, below 1 for lower coupons.
- **Delivery price / invoice price**: delivery price = `cf × F`; invoice = `cf × F + accrued interest`.
- **Quality option**: the short's right to choose which basket bond to deliver; the dominant embedded option.
- **Timing option**: the short's right to deliver any day in the delivery month (first delivery to last delivery date).
- **End-of-month option**: after the last trade date the final settlement price is fixed, but delivery can occur through month-end, so the short can switch bonds at a fixed F.
- **Cost of delivery**: `P_i − cf_i × F`; zero for the CTD on the last delivery date.
- **Cheapest-to-deliver (CTD)**: bond with minimum cost of delivery (equivalently minimum P/cf at delivery, minimum net basis before delivery).
- **Gross basis**: spot price minus cf-weighted futures price; quoted in 32nds.
- **Net basis (NB)**: forward price minus cf-weighted futures price; gross basis net of carry; the value of the switch option.
- **Carry (forward drop)**: `κ = spot − forward`; coupon income plus repo effects, usually positive for basket bonds.
- **Basis trade**: bond (via repo or forward) versus `cf`-weighted futures; buying the basis is a pure long of the quality option.
- **Tail**: reduction of the futures hedge by roughly `N × repo × days/360` contracts so futures P&L mimics forward P&L (Chapter 13). Distinct from the "tail" in the end-of-month hedge (a cf-weighted vs one-to-one hedge).
- **Squeeze**: buying a large fraction of a single deliverable plus futures; the basket makes it costly for a squeezer because the next-to-CTD costs only cents more.
- **Beta of a bond**: expected change in its yield for 1bp in a benchmark bond's yield; how futures desks parametrize idiosyncratic basket dynamics.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Delivery / invoice price | `cf_i × F_t`; `cf_i × F_t + AI_t^i` |
| Cost of delivery | `P_t^i − cf_i × F_t` (14.1) |
| CTD condition | `P^i − cf_i F ≥ P^CTD − cf_CTD F` (14.3) |
| Final settlement (last delivery date T) | `F_T = P_T^CTD / cf_CTD = min_i P_T^i / cf_i` (14.4, 14.9) |
| Conversion factor (approx.) | `cf ≈ (c/y)[1 − 1/(1+y/2)^{2n}] + 1/(1+y/2)^{2n}` with y = 6%, c = coupon, n = years (rounded down to a quarter) (14.10) |
| Gross basis | `GB = P_t^i − cf_i F_t` (14.12) |
| Net basis | `NB = P_t^i(T) − cf_i F_t = GB − κ^i(T)` (14.13, 14.15) |
| Forward price | `P^i(T) = P^i − κ^i(T)` (14.14) |
| Long-basis P&L at delivery (tailed) | `G × [NB_s − NB_t]` (14.17) |
| Implied repo (approx.) | `r_impl ≈ r_actual + NB/(P_dirty) × 360/d` (NB in price points, d = days to delivery) |
| Hedge ratio for a fixed CTD | `cf_CTD` futures per contract-size face of bond (one contract covers 1/cf of face) |
| Tail | `N_futures × r × d/360` contracts removed (14.22) |
| End-of-month switch P&L | `(P^i − P^CTD) + (cf_CTD − cf_i) × F_S` where i = currently held bond, CTD = new CTD, F_S = final settlement price (14.19) |
| Basis P&L in dollars (NB in ticks) | `Face × ΔNB/32/100` |

Mechanics constants: TYU0 contract size $100,000 face; tick = 1/32 (with half-tick "+"), 1 tick = $31.25 per contract; notional coupon 6%; last trade date about 7 business days before last delivery date.

TYU0 basket data (May 28, 2010; from the book): cf of 4.5s 5/15/17 = .9202, 3.25s 3/31/17 = .8538, 3.625s 8/15/19 = .8401, 3.5s 5/15/20 = .8210, 2.75s 2/15/19 = .7909.

CTD-by-yield (flat curve, at delivery): rates below about 5%: 4.5s 5/17 (shortest duration); near 6%: 2.75s 5/31/17 marginally; above about 6.15%: 3.5s 5/15/20 (longest duration).

## Mental Models
- **Futures = forward + short option to switch**: sell futures = sell one bond forward and buy the quality option; net basis is the option premium in price units (`NB = 0` means the option is worthless).
- **Lower envelope**: draw P/cf against yield for each bond; the futures price at expiry is the bottom line. Kinks are switch points; negative convexity comes from each kink.
- **Net basis as an option on rates**: the low-duration CTD (4.5s of 2017) has a net basis that rises with rates (like a call on rates, put on price); the long-duration bond's net basis rises as rates fall (put on rates); a middle-duration bond behaves like a straddle.
- **Conversion factor as a linearization**: cf equalises delivery prices only at a 6% flat curve; far from 6%, convexity of mismatch drives CTD switches. With rates at 2 to 3% the exchange has left the 6% notional unchanged, so the option is cheap (net bases near CTD of about a tick).
- **Squeeze insurance**: the basket works because next-to-CTD is only 1.3 cents worse than CTD in the example, capping what a squeezer can extract.

## Worked Example
**Conversion factor and gross basis (TYU0, 5/28/10).**
- 3.25s 3/31/17 mature 6.5 years after 9/30/10: `cf = 0.0325/0.06 × [1 − 1/(1.03)^13] + 1/(1.03)^13 = 0.8538` (checked).
- The 4.5s of 5/15/17 at 6y8m round down to 6.5 years: cf = 0.9202 (checked).
- Spot 111-22 (111.6875), futures 119-28 (119.875): `GB = 111.6875 − 0.9202 × 119.875 = 1.3785` = 44.1 ticks.
- Forward price 110.3207 → carry `= 111.6875 − 110.3207 = 1.3668` = 43.7 ticks; `NB = 44.1 − 43.7 = 0.4` ticks.
- Read: 0.4 tick of option value (about $12.50 per contract-size face) is what the market charges for switching away from the 4.5s. Implied repo ≈ 0.30% + 0.4/32/111.9 × 360/125 ≈ 0.33%, a hair above actual repo, so no material arbitrage.

**Cost of delivery at delivery (9/30/10, F = 121.2039).** 3.625s 8/15/19: `103.1007 − 0.8401 × 121.2039 = 1.277`. The 4.5s of 5/17: `111.5318 − 0.9202 × 121.2039 = 0.000`, so it is the CTD and `F = 111.5318/0.9202 = 121.2039`. Next to CTD (3.25s of 3/17) costs 0.013.

**Case study: selling the Nov '08 basis into TYM0 (Feb 28, 2000).** Sell USD 100mm of the 4.75s of 11/15/08 net basis at 7.45 ticks; hedge with 47 calls (strike 95, 1.516 each) on 4.7mm face.
- Modelled +20bp scenario: `100,000,000 × (7.45 − 0.9)/32/100 = $204,688` (checked).
- Actual path: 4/3: NB 11.06, loss `−$112,813` on basis, +$87,391 on options = −$25,422; 4/10: NB 22.0, basis loss −$455,000, options +$127,781 = **−$327,219**; horizon 5/19: NB 3.51, +$123,125 basis, −$57,281 options = **+$65,844** versus 153,532 predicted (checked).
- Tail: `920 × 5.55% × 122/360 ≈ 17` contracts, so buy 903 not 920 (920 = `100mm × 0.9195/100k`). Ignoring the tail would have cost about `1.5mm × 2.98/100 = $44,700`.

## Anti-patterns
- **Treating the horizon P&L table as the risk**: parallel-shift scenarios hid the curve-slope and futures-cheapness risk; the interim loss of $455k on the basis leg exceeded any modelled scenario and could have forced a stop-out.
- **Hedging bonds one-for-one with futures**: futures move like the CTD divided by cf; you need `cf_CTD` contracts per contract-size face, tailed for repo, and rebalanced as the CTD changes.
- **Calling a bond "the CTD" before the first delivery date**: strictly, only the lowest net basis is nearly CTD; the option value remains.
- **Single-factor CTD analysis**: curve steepeners and flatteners move the CTD without changing the level; use a two-factor model or slope sensitivity, plus per-bond yield sensitivities for idiosyncratic risk.
- **Using an option that expires before delivery to hedge net basis**: options on futures expire before the first delivery date, leaving a gap on a basis held to the last delivery date; hedge protection ends at option expiry.
- **Ignoring tails when computing basis P&L**: `G × ΔNB` is only true for a properly tailed position.

## Practitioner Notes
- Basis is quoted in 32nds of gross basis; desks trade packages of a bond plus its cf-weighted futures at the quoted gross basis, but manage on net basis.
- Carry on basket bonds is usually positive, so the short delays delivery (timing option rarely exercised early); early delivery only pays if carry is negative and outweighs remaining quality-option value.
- The end-of-month option is worth little: the window is under seven business days and any cheapening bond attracts shorts that switch into it, halting the cheapening.
- With low rates (2010) the option value is small: bonds near CTD had net bases below a tick even four months before delivery. When rates approach or exceed 6% the option becomes valuable; exchanges historically lowered the notional coupon to restore accuracy.
- Liquidation of short-basis positions (buy bonds, sell futures) cheapens futures; crowded basis trades can move the market against you in the interim.
- Model conventions: assume bond forwards fair (OAS attached to each bond), then price futures relative to bonds; a richer model gives each bond its own volatility (for 16 bonds, 120 correlations), which desks express through yield betas to a benchmark bond.
- European and Japanese contracts have essentially only the quality option.

## Key Takeaways
1. `F_T = min_i (P_i / cf_i)` at the last delivery date; the minimizer is the CTD.
2. Conversion factor is price at 6% yield; it equalises delivery only on a 6% flat curve, so the CTD is the long-duration bond when yields are above 6% and the short-duration bond when below, and drifts with slope.
3. Net basis = forward price − cf × F = price of the quality option; the long basis is a long option, the short basis is short it.
4. Basis P&L (tailed) = face × change in net basis; always compute the tail.
5. Futures DV01 and convexity shift with the CTD: hedge ratios need rebalancing and are negatively convex.
6. Basis trades must be stress-tested on curve slope, bond-specific richening, and futures cheapness, and on interim P&L, not just the horizon.
7. Delay delivery when carry is positive; the end-of-month option and squeezes are limited in practice.
8. Implied repo ≈ actual repo + NB/dirty price × 360/d; the highest implied repo identifies the CTD.

## Connects To
- **ch13**: forward vs futures, tail, carry and the futures pricing recursion used here.
- **ch12**: repo rates, specialness and financing that determine carry and cash-and-carry arbitrage.
- **ch18**: options on bond futures, the hedge used in the case study; also quality-option modelling ideas.
- **ch09 / ch10**: short-rate models (Vasicek-style) used to price the option in a tree.
- **ch04 / ch05**: one-factor versus multi-factor hedges, DV01 and slope risk.
- **`hull-derivatives` ch06**: Treasury bond futures, CTD and conversion factor mechanics from the derivatives side.
- **`cfa-derivatives` ch03**: futures pricing and basis concepts at exam level.
