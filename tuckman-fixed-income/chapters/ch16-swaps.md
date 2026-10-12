# Chapter 16: Swaps
> **Source**: Tuckman & Serrat, *Fixed Income Securities* (3rd ed.), Chapter 16 (Selected Securities and Topics) | Bruce Tuckman, Angel Serrat

## Core Idea
A swap is a fixed-rate "bond" traded against a floating-rate "note" with no exchange of notional. The floating leg is worth par on every reset date (pre-crisis LIBOR logic), so all the risk and pricing subtlety sits in (a) the stub between resets, (b) the fixed leg, (c) what the discount curve really is (OIS post-2007, see ch17), and (d) counterparty, clearing, basis and convexity issues. Swap exposure is the NPV, never the notional.

## Frameworks Introduced
- **Fictional-notional valuation (fixed leg = bond, floating leg = FRN)**: add an equal notional payment at maturity to both legs; with default-free payments this changes nothing and lets you price each leg as a bond.
  - When to use: valuing or risking any vanilla fixed-vs-floating swap.
  - How: (1) build the fixed-leg cash flows (coupon = fixed rate × day-count fraction, + notional at T). (2) Floating leg: take par on the next reset/payment date plus the accrued known coupon. (3) Discount both with the swap discount curve. (4) NPV for the fixed receiver = PV(fixed) − PV(floating).
  - Failure mode: the notional trick hides counterparty risk (real exposure is NPV, not notional) and, post-crisis, "floating = par" only holds if the discount rate equals the index (LIBOR-OIS spread breaks it).
- **Roll-back proof that a floating leg is worth par at reset**: at T − .25 the leg is worth (100 + 100·L·d/360)/(1 + L·d/360) = 100 because the rate earned equals the rate discounted; repeat backward to t = 0.
  - When to use: pricing a swap at inception (NPV = PV(fixed) − 100) or between resets.
  - Between resets: floating leg = (100 + 100·L₀·d₀/360)/(1 + L·d/360), where L₀ is the last fix, d₀ the days in the current accrual period, d the days to the next payment and L the discount rate for d days. It behaves like a short bond with coupon L₀.
- **Reset risk**: the DV01 of the floating leg ≈ time to the next payment; it resets to about the accrual length right after a fixing and decays toward 0 just before payment.
  - When to use: hedging a swap book; hedge fixed and floating legs separately (fixed legs with Part Two methods, floating legs with short-rate derivatives, ch15) rather than netting DV01s into one long-dated hedge, which would add unneeded curve risk. Desks with very many swaps use partial/forward-bucket 01s (ch05).
- **CMS convexity correction**: fair fixed rate S of a constant-maturity swap payment exceeds the forward swap rate C(t,t+T); S − C ≈ Var[C_t(T)] · (1/C − T·(1+C/2)^(−2T−1)/(1−(1+C/2)^(−2T))) for semiannual compounding.
  - When to use: pricing any product paying a swap rate (CMS legs, CMS-linked notes, CMS spread options) at the wrong time/measure.
  - How: (1) per payment date, forward swap rate C(t,t+T); (2) variance of the swap rate to that date (from normal swaption vol, ch18, or a smile); (3) add the correction; (4) PV the corrections and divide by the annuity to get a running spread.
  - Why it works: the payoff C_t(T) is paid at t but swap-rate convexity (annuity A_t(T) moves inversely with the rate) makes a forward swap hedge gain whichever way rates move, so S > C(t,t+T) or an arbitrage exists.

## Key Concepts
- **Swap / notional**: exchange of fixed-rate interest for floating-rate interest on a notional that is only a calculation base and is never exchanged.
- **Payer / receiver**: the fixed payer receives floating; NPV is conventionally quoted for the receiver of fixed.
- **Settlement T+2 (GBP T+0)**: interest starts accruing two business days after trade date; LIBOR for a period is fixed two business days before the period starts.
- **Set in advance, paid in arrears**: each floating payment is known one period before it is paid.
- **Fixed-leg day count**: 30/360 semiannual (USD); payments falling on non-business days move (modified following), and the interest is adjusted for the extra days (unlike bonds).
- **Floating-leg day count**: actual/360 on quarterly 3M LIBOR; EUR swaps usually reference Euribor, not EUR LIBOR.
- **Reset risk**: DV01 of the floating leg, a sawtooth in time between resets.
- **NPV of a swap**: PV(fixed leg) − PV(floating leg) for the fixed receiver; the amount that changes hands on an unwind.
- **Unwind vs assignment**: tear up the swap by paying NPV to the counterparty, or novate to a third party with the counterparty's consent (normally granted unless there is a credit objection).
- **Counterparty risk vs index credit risk**: LIBOR's bank credit component (index) is distinct from the chance that the counterparty defaults (contract).
- **CSA (credit support annex)**: part of the ISDA Master Agreement governing collateral posting; the party with negative NPV posts.
- **CVA in the fixed rate**: uncollateralized swaps embed a credit-value adjustment so the weaker party pays more / receives less than market.
- **CCP (central counterparty) / clearing**: each side faces the clearinghouse; loss waterfall = defaulters' collateral, then CCP capital, then CCP failure. A CCP mutualizes rather than eliminates counterparty risk.
- **Basis swap**: floating index against another floating index plus a spread (3M LIBOR vs 1M LIBOR, 6M LIBOR or fed funds).
- **Constant maturity swap (CMS)**: one leg pays a fixed-tenor swap rate (e.g. 5y) on each date.
- **Convexity correction**: amount by which the CMS rate exceeds the forward swap rate.
- **ISDA Master Agreement**: standard legal contract for OTC swaps.

## Formulas & Reference Tables
Floating leg at a reset date (value per 100, d = days in period, L = 3M LIBOR fixed for the period):

`[100 + 100·L·d/360] / [1 + L·d/360] = 100`

Floating leg between resets (L₀ last fixing, d₀ days in the current period, d days to next payment, L discount rate):

`V_float = [100 + 100·L₀·d₀/360] / [1 + L·d/360]`

Payments:
- Fixed coupon: `Notional × K × (30/360 days)`; semiannual regular = `½ × K × N`.
- Floating: `Notional × L × (actual days)/360`.

Swap NPV for the fixed receiver: `NPV = PV(fixed leg incl. notional) − PV(floating leg incl. notional)`; at inception with par fixed rate the fixed leg = 100 and NPV = 0.

Receiver's exposure to default = NPV (payer's = −NPV if positive); a bond holder's = full PV.

DV01: `DV01(receive fixed) = DV01(fixed leg) − DV01(floating leg)`; `DV01(floating) ≈ time to next payment` just after a fix.

CMS convexity correction (n compounding periods per year, t = time to payment, T = tenor):

`S − C(t,t+T) ≈ Var[C_t(T)] · [ 1/C(t,t+T) − T·(1 + C(t,t+T)/n)^(−nT−1) / (1 − (1 + C(t,t+T)/n)^(−nT)) ]`   (n = 2 in (16.7))

Compact form: `S − C(t,t+T) ≈ ½ · Var[C_t(T)] · Cnvx(T, C) / D(T, C)` (yield-based convexity and duration of a T-year par bond; ch04).

Derivation skeleton: under the annuity measure `C(t,t+T) = E₀[C_t(T)]`, and the fair CMS rate solves `E₀[(C_t(T) − S)/A_t(T)] = 0`, so `S = C(t,t+T) + Cov[C_t(T), 1/A_t(T)] / E₀[1/A_t(T)]`. With a flat curve `C·A + Z(C) = 1`, giving `1/A = C/(1−Z(C))` and the covariance approximated by `E[H′]·Var` (exact for normal rates by Stein's lemma).

Running correction for a multi-date CMS: `ρ = Σ DF_i · corr_i / Σ DF_i`.

Basis swap convention: `party A pays 1M LIBOR (compounded) + spread s; receives 3M LIBOR`; s > 0 because 3M LIBOR carries more credit/liquidity premium and a stale panel.

Clearing waterfall: `defaulter collateral → CCP/member capital → CCP failure`.

## Mental Models
- **Swap = long one bond, short one FRN.** Risk and price follow from the two legs; the floating leg is a one-period bond that rebuilds itself each reset.
- **Floating leg as a sawtooth**: DV01 jumps to about the period length at each fixing then decays to zero; the swap's short-end exposure is mostly this.
- **Notional is a measuring stick, NPV is the exposure.** Always ask for the mark-to-market (and collateral) rather than the gross notional.
- **CCP = mutualization, not elimination.** It removes bilateral webs and adds margin discipline, at the cost of concentration and procyclical collateral.
- **Basis spread = price of credit/liquidity difference between two indices.** A zero basis would let one index be riskless and the other not, so the traditional "every floater is par" logic fails; ch17 fixes this by anchoring on OIS.
- **CMS convexity = long gamma in the hedge**: the annuity moves against the rate, so the forward-rate-hedged position profits both ways; the fair CMS rate is paid up for it.

## Worked Example
**1. Pricing an existing swap (Table 16.2 reconstruction).** Fixed rate 1.386% semiannual, matures 12/15/2011, valued 5/28/2010, previous 3M LIBOR fixing .257%, 92 days in the current period.
Discount factors for 6/15/10, 12/15/10, 6/15/11, 12/15/11: .999824, .996185, .990908, .983968.
- Fixed leg coupon = ½ × 1.386 = .693 per 100. PV = .693 × (.999824 + .996185 + .990908) + 100.693 × .983968 = 101.149.
- Floating leg = (100 + 92/360 × .257) × .999824 = 100.048 (next payment date treated as reset at par).
- NPV (fixed receiver) = 101.149 − 100.048 = **1.10** per 100. On a 5/28/2010 unwind, the fixed payer pays 1.10. Counterparty exposure of the fixed receiver is 1.10, versus 101.15 for a corporate bond holder with the same coupon.
Check of payment mechanics: 617,500 = ½ × 1.235% × 100mm; two extra days on a delayed date add 2/360 × 1.235% × 100mm = 6,861, for 624,361; floating 92 days at .50% pays 127,778.

**2. CMS rate on a flat 4% s.a. curve, vol 60 bp/yr, pays 5y swap rate annually in years 2–5.**
- Bracket term: 1/.04 − 5 × 1.02^(−11) / (1 − 1.02^(−10)) gives 2.616047 (multiplying variance in decimal²).
- Vol to each date = 60√t: 84.85, 103.92, 120.00, 134.16 bp. Corrections = 2.616 × var: 1.88, 2.83, 3.77, 4.71 bp.
- Discount factors (1.02^(−2t)): .9238, .8880, .8535, .8203; annuity 3.4857; PV corrections 1.74 + 2.51 + 3.22 + 3.86 = 11.33 bp.
- Running correction = 11.33/3.4857 = **3.25 bp**; fair CMS rate 4.0325%.
(Recomputed in Python; the book's table matches to rounding.)

## Anti-patterns
- **Quoting swap risk as notional**: real credit exposure is the NPV, usually a few percent of notional. Conversely, using notional-inclusive cash flows to reason about counterparty loss overstates the loss.
- **Hedging a swap with net DV01 in one long-dated instrument**: fixed-leg exposure is long-end, floating-leg exposure is very short-end; netting them leaves curve risk that looks hedged.
- **Discounting 3M-LIBOR flows at 1M LIBOR (or vice versa)**: different indices differ by the basis spread; "LIBOR of other terms cannot be used without adjustment."
- **Valuing the floating leg at par without a stub**: between fixings it is a bond with the last LIBOR coupon, not 100.
- **Taking the forward swap rate as the CMS rate**: ignores the convexity correction and underprices CMS receivers; the correction grows with variance (√t vol) and with tenor.
- **Believing a CCP eliminates counterparty risk**: it mutualizes it, and partial clearing can raise a firm's total counterparty risk by breaking netting.
- **Assuming a bond-style day-count**: swap payments on non-business days accrue extra days; bonds do not.
- **Post-2009 use of LIBOR-only pricing in wide LIBOR-OIS regimes**: fine when spreads are below about 10 bp (pre-crisis), wrong when they reach hundreds of bp.

## Practitioner Notes
- **Conventions (USD)**: fixed leg 30/360 semiannual; floating leg 3M LIBOR actual/360 quarterly; T+2 settle (GBP T+0); modified following.
- **Unwinds are expensive**: customised swaps are illiquid, so dealers quote an exit premium; customers and desks typically add an offsetting swap instead, leaving residual counterparty risk and a growing book. IMM-date swaps reduce schedule proliferation.
- **Corporate hedging uses**: (1) pay fixed (or forward-start) to lock in future bond issuance, with basis risk from bank-credit swap rates vs issuer credit; (2) issue fixed, receive fixed/pay floating to get synthetic floating funding at a spread to LIBOR; (3) hedge mortgage/MBS duration (GSEs, servicers); (4) lengthen asset duration for pensions and insurers by receiving fixed.
- **Mortgage hedging distorts swap spreads**: rising rates lengthen MBS duration, forcing fixed-payer hedging that can push swap rates below governments; homeowners (the natural short) do not hedge, so nothing offsets.
- **Credit terms**: collateralised swaps trade at market rates; uncollateralised ones carry CVA in the fixed rate and counterparty limits.
- **Regulatory context**: Dodd-Frank mandated central clearing; by the book's writing most dealer-dealer swaps and liquid CDS were cleared, dealer-customer trades still bilateral. LCH moving to OIS discounting in June 2010 was the watershed for the OIS-curve standard.
- **Numbers the authors commit to**: LIBOR-OIS was below 10 bp pre-crisis for years; 5y CMS example needs roughly 3 bp running convexity on 60 bp vol and a flat 4% curve.

## Key Takeaways
1. Price a swap as fixed-rate bond minus floating-rate note after adding notional to both legs; at inception with a par rate NPV = 0 and no cash changes hands.
2. The floating leg is worth par at each reset; between resets it is (100 + accrued-at-last-fix) discounted over the days left.
3. Only the discount curve matters beyond that: post-crisis use OIS discounting (ch17); LIBOR-only valuation is valid only when LIBOR-OIS is tiny.
4. Hedge fixed and floating legs separately; floating-leg DV01 ≈ time to next payment (reset risk).
5. Swap credit exposure is NPV, collateral (CSA) removes most of it, and uncollateralised trades embed CVA.
6. Clearing mutualizes risk through a margin/capital waterfall; it does not eliminate it.
7. Basis swaps trade at a positive spread for the longer/riskier index, which is why "every LIBOR floater = par" cannot hold simultaneously for all tenors.
8. CMS fair rates exceed forward swap rates by a convexity correction ≈ Var × (1/C − T·v^(2T+1)/(1−v^(2T))); get the variance from swaption vol.

## Connects To
- **ch02**: par, spot and forward swap rates, annuity factors used here.
- **ch04**: yield-based duration and convexity that shorten the CMS correction.
- **ch05**: partial/forward-bucket 01s that swap desks use.
- **ch13**: forward swap rates and forwards pricing.
- **ch15**: LIBOR-OIS spread, Eurodollar/fed funds hedges for floating legs, IMM dates.
- **ch17**: OIS discounting, collateral, and two-curve valuation that replace the floating-par result.
- **ch18**: swaptions, normal vol inputs to the CMS correction.
- **ch19**: CDS and asset swaps (up-front NPV on a non-par swap).
- **ch20**: mortgage hedging demand that moves swap rates.
- **ch21**: curve-fitting of discount factors for non-standard dates.
- **`hull-derivatives` ch07 / ch30 / ch34**: swap valuation and OIS discounting (ch07), CMS convexity adjustments (ch30), swaps revisited (ch34).
- **`cfa-derivatives` ch03**: swap pricing at exam level.
