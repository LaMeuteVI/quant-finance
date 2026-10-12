# Chapter 3: Returns, Spreads, and Yields
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 3 (Part One: The Relative Pricing of Securities with Fixed Cash Flows) · Examples: US Treasury 4½s of 30-Nov-2011 and ¾s of 30-Nov-2011, priced 28-May-2010

## Core Idea
Spot, forward and par rates (ch02) describe the curve; **returns, spreads and yields** are how a desk judges an individual security. A realized return is P&L divided by the *initial price* (even when financed). A spread is the parallel shift to a benchmark forward curve that reproduces the market price, and it expresses cheap/rich in bp instead of cents. Yield is a convenient *quote* of price, not a measure of relative value (the coupon effect). Total P&L splits exactly into cash carry, carry-roll-down, rate change and spread change, and "no change" scenarios for carry-roll-down each carry a hidden assumption about risk premia.

## Frameworks Introduced
- **Gross and net realized return (one period)**:
  - When to use: ex-post performance of a bond over a holding period equal to a coupon period.
  - How: gross `R = (P₁ + c − P₀)/P₀`; net = gross − financing cost, where the financing cost is `r/2` (semiannual) applied to the borrowed price. Divide by the initial *price*, not by the investor's equity, because leverage varies by investor and a 100% financed trade has zero equity.
  - Failure mode: dividing by capital produces investor-specific "returns on capital" that cannot be compared across securities.
- **Multi-period return with reinvestment**: coupons received early must be reinvested at an assumed rate, and financed positions also need the future financing rates. The return is unknowable ex-ante beyond the first period.
- **Spread to a curve (bond-specific, eq. 3.8)**:
  - When to use: quantifying how cheap or rich a bond is against a benchmark (swaps, Treasuries), or quoting a sector spread.
  - How: 1) compute the forward rates f(1)…f(T) from the benchmark curve; 2) find `s` such that discounting each cash flow with `1 + f(t) + s` per period (semiannual: `f/2 + s/2`) gives the market price; 3) quote `s` in bp. For a sector (e.g. corporates), use a **spread curve** s(1)…s(T), a different forward spread per period.
  - Why it works: `P ≡ P(R) + ε` and the same information is re-expressed as a shift in rate space, which is portable across bonds of different maturity and duration.
- **Yield-to-maturity (YTM)**: the single rate y with `P = Σ (c/2)/(1+y/2)ᵗ + 1/(1+y/2)²ᵀ`. Solve numerically. It bundles the term structure and the bond's spread into one number, and prices only that one bond.
- **P&L decomposition (exact, additive)**: total price appreciation `= Pₜ₊₁(Rₜ₊₁,sₜ₊₁) − Pₜ(Rₜ,sₜ)` split into:
  1. **Carry-roll-down** `= Pₜ₊₁(Rᵉₜ₊₁, sₜ) − Pₜ(Rₜ, sₜ)`: price change from time passing with rates moving "as expected" and no spread change;
  2. **Rate change** `= Pₜ₊₁(Rₜ₊₁, sₜ) − Pₜ₊₁(Rᵉₜ₊₁, sₜ)`;
  3. **Spread change** `= Pₜ₊₁(Rₜ₊₁, sₜ₊₁) − Pₜ₊₁(Rₜ₊₁, sₜ)`;
  then add **cash carry** (coupon − financing cost). Divide every line by P₀ for return components.
  - When to use: P&L attribution, catching booking errors, scenario tables.
  - Caveat: the order of the steps changes the split slightly (only materially for very nonlinear securities).
- **Carry-roll-down "no change" scenarios**: choose Rᵉ as (a) **realized forwards**, (b) **unchanged term structure**, (c) **unchanged yield**, or (d) expectations of short rates realized (conceptually best, rarely used; needs ch08's framework). No choice clearly dominates.
- **Appendix A (settlement between coupons)**: use the full (dirty) price and the market convention that the next coupon is discounted by `(1+y/2)^τ`, where τ = fraction of the semiannual period until the next coupon.

## Key Concepts
- **Gross realized return**: end value (price + coupons + reinvestment) minus start value, over start value.
- **Net realized return**: gross return minus financing cost, still divided by the initial price.
- **Spread (s)**: the shift to every forward rate of a benchmark curve that equates model price to market price; positive means cheap.
- **Spread curve**: a term-dependent forward spread s(t); the natural description of a corporate issuer vs swaps.
- **Yield-to-maturity**: single discount rate reproducing the market price; a quoting convention.
- **Pull to par**: with fixed yield, premium bonds fall and discount bonds rise toward 100 as maturity nears.
- **Coupon effect**: fairly priced bonds of equal maturity but different coupons have different YTMs.
- **Cash carry**: coupon income minus financing cost (explicit cash flows only); what drives forward and futures pricing (ch13-14).
- **Carry (broad sense)**: P&L from passage of time with everything else constant, including pull-to-par.
- **Roll-down**: P&L because a maturing security's cash flows are priced at earlier, different points on the curve.
- **Carry-roll-down (Tuckman)**: all time-decay P&L *excluding* cash carry; mixes carry and roll-down on purpose.
- **Realized forwards**: scenario where today's forward rates become tomorrow's spot/forward rates.
- **Unchanged term structure**: scenario where each forward rate for a given calendar term stays put.
- **Simple yield (Japan)**: JGB convention `c/p + (1/T)(1−p)/p`, no compounding.
- **Annuity factor A(T)**: PV of 1 per year (semiannual 1/2) for T years; the PV factor of coupons, swap fixed legs and mortgage payments.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Gross return (3.1) | `R = (P₁ + c − P₀)/P₀` |
| Net return (3.5) | `R − r/2` for a six-month holding period, e.g. 1.317% − 0.2%/2 = 1.217% |
| Price in forwards (3.7) | `P = c/(1+f(1)) + c/[(1+f(1))(1+f(2))] + … + (1+c)/[(1+f(1))…(1+f(T))]` |
| Price with spread (3.8) | same with each `f(t)` replaced by `f(t) + s` |
| Price with spread curve (3.10) | each `f(t)` replaced by `f(t) + s(t)` |
| Yield, coupon date (3.13) | `P = (c/2) Σₜ₌₁²ᵀ 1/(1+y/2)ᵗ + 1/(1+y/2)²ᵀ` |
| Closed form (3.14) | `P = (c/y)[1 − 1/(1+y/2)²ᵀ] + 1/(1+y/2)²ᵀ` |
| Annuity (3.15) | `A(T) = (1/y)[1 − 1/(1+y/2)²ᵀ]` |
| Perpetuity | `c/y` |
| Yield, mid-period (3.31) | `P = (c/2)Σₜ₌₀²ᵀ⁻¹ 1/(1+y/2)^(τ+t) + 1/(1+y/2)^(τ+2T−1)` (full price) |
| Yield, mid-period closed form (3.32) | `P = (1+y/2)^(1−τ) · { (c/y)[1 − 1/(1+y/2)²ᵀ] + 1/(1+y/2)²ᵀ }` |
| Japanese simple yield | `y = c/p + (1/T)(1−p)/p` |
| Realized forwards, one period (3.18) | `[P₁(R₁)+c−P₀(R₀)]/P₀ = f(1)`; with spread curve `f(1)+s(1)` |
| Realized forwards, to maturity (3.19) | total return `= (1+f(1))(1+f(2))…(1+f(T)) − 1` |
| Unchanged TS, one period (3.22) | `[(f(T) − c)/((1+f(1))…(1+f(T))) + c]/P₀`; with spread use `f(T)+s(T)−c` |
| Unchanged yield, one period (3.25) | `[P₁+c−P₀]/P₀ = y` |
| Unchanged yield, to maturity (3.26) | total return `= (1+y)ᵀ − 1`, only if coupons reinvested at y |
| P&L off coupon date (3.35) | `Δp(carry-roll-down) + Δp(rates) + Δp(spread) + [AI(t+1)−AI(t) − Pₜ·r·d/360]` |
| P&L with coupon in between (3.36) | cash-carry term becomes `c/2 + AI(t+1) − AI(t) − Pₜ·r·d/360` |

Price-yield facts from (3.14): `c = y` → par; `c > y` → premium; `c < y` → discount; a flat curve makes every bond's YTM equal the flat rate. On a sloped curve the coupon effect appears: with an **upward** sloping curve, `y(zero) > y(par) > y(9%)` at each maturity; reversed if downward.

## Mental Models
- **A spread is a price expressed in rate units.** "Cheap 6.5 cents" and "cheap 4.4bp" are the same statement; use cents to size the arbitrage P&L, bp to compare bonds and read charts.
- **Yield is a weighted average of spot rates, weighted by PV of each cash flow.** Heavy coupons pull weight to short rates, so on an upward curve high-coupon bonds show lower yields for zero credit or liquidity difference.
- **Carry-roll-down is a scenario, not a forecast.** Under realized forwards every bond earns the short rate (net return 0 after financing); under an unchanged curve return depends on `f(T) − c`; the two extremes correspond to "no risk premium" and "term premium explains all the slope".
- **Decompose before you explain.** Attribute P&L to carry, rates, spread, and only then debate views; unexplained residual = booking or model error.
- **Roll vs buy-and-hold** is a forward-vs-forecast bet: rolling short paper wins if realized forwards exceed the forwards priced into the bond, and buying long wins if they come in lower.

## Worked Example
Bond: ¾s (coupon 0.375 per half-year on face 100) of 30-Nov-2011, priced 28-May-2010 on base forwards f = 0.149%, 0.556%, 1.036% (semiannual-compounded), market price 100.190.
1. **Base price** with s = 0: 100.255. Market is 0.065 cheap.
2. **Spread**: solve 100.190 = Σ CF/Π(1 + f/2 + s/2) → s ≈ 0.044% = **4.4bp** (checked numerically: 4.36bp).
3. **Six-month holding period** under realized forwards (curve becomes 0.556%, 1.036%, spread unchanged): price 99.911, carry-roll-down = **−0.279** (recomputed −0.278 before rounding of s).
4. **Parallel −10bp**: price 100.011, rate change = **+0.100** (recomputed +0.099).
5. **Spread converges to 0**: price 100.054, spread change = **+0.043** (+0.044).
6. **Cash carry**: coupon 0.375, unfinanced financing 0 → 0.375.
7. **Total P&L = −0.136 + 0.375 = +0.239 per 100** (0.24%). The bond lost value from roll-down (a short bond with above-forward coupon shrinking) yet the trade made money because of the coupon, the rate fall and spread convergence.

Cross-checks: 4½s of 30-Nov-2011 at 105.856, coupon 2.25: six-month gross return with price 105 = 1.317%; financed at 0.2% for six months net = 1.217% (= 1.317% − 0.1%); one-year return with November coupon reinvested at 0.60% and price 105 = 3.449%; YTM ≈ 0.574%. JGB: p = 101.45, c = 2%, T = 20 → simple yield 1.90%.

## Anti-patterns
- **Comparing yields of bonds with different coupons or cash-flow shapes**: the coupon effect makes a higher YTM meaningless as cheapness evidence. Compare spreads to a common curve.
- **Dividing financed P&L by the equity invested** when reporting security returns: use the initial price convention or state leverage.
- **Believing "a bond earns its yield"** without the conditions: yield must not change and every coupon must be reinvested at that yield; a term structure makes both false.
- **Treating carry-roll-down as an expected return**: the expected return of a bond is short rate plus a risk premium; the price at expected rates is not the expected price (convexity, Jensen).
- **Assuming realized forwards for a long bond and pocketing "roll-down" as free money**: it is only free if the curve is unchanged and premia are fixed.
- **Mixing accrued interest into quoted-price P&L**: off coupon dates use full price for financing and separate `AI(t+1) − AI(t)`.

## Practitioner Notes
- Quote in the market's language: Greece's 7-year issue in March 2010 was reported as +310bp to mid-swaps, equal to +334bp over Bunds, versus roughly +61bp Spain, +114bp Portugal, +45bp Italy. Spreads travel across benchmarks, yields do not.
- Bond traders bid in price or yield, never in spot/forward rates.
- Scenario tables usually show two carry-roll-down columns (realized forwards and unchanged curve); large gap between them signals an unusually steep or humped curve.
- The sequence rates then spread is convention; keep it fixed so P&L reports are comparable across days.
- Cash carry, not carry-roll-down, is the term that enters forward and futures fair value (ch13-14).

## Key Takeaways
1. Realized return = (end value + coupons + reinvestment − start) / **initial price**; net return subtracts financing (0.2% annual for six months = 0.1%).
2. A spread `s` added to every benchmark forward reproduces market price; 6.5 cents cheap ≈ 4.4bp for the ¾s.
3. YTM is a quoting device; fairly priced bonds of the same maturity differ in yield by coupon (zero > par > high coupon on an upward curve).
4. Price-yield algebra gives premium/discount/par, pull to par, annuity `A(T)` and perpetuity `c/y`.
5. P&L = cash carry + carry-roll-down + rate change + spread change, exact by construction.
6. Realized forwards: every bond returns f(1) (+ s(1)) for one period and net return is zero after financing; unchanged curve: return driven by `f(T) − c`; unchanged yield: return = yield.
7. Roll short bonds beats holding long bonds only when realized forwards exceed the initial forwards.
8. Off-coupon-date calculations use full price, dirty-price discounting `(1+y/2)^τ`, and accrued interest in cash carry.

## Connects To
- **ch01**: discount factors and full-vs-quoted price (accrued interest) underlie every formula here.
- **ch02**: spot/forward/par rates are the curve R and forwards f(t) used in spreads and scenarios.
- **ch04**: replaces "rates change" in the decomposition by DV01, duration and convexity.
- **ch05**: rate-change P&L broken down across key rates and forward buckets.
- **ch08**: expectations, risk premium and convexity; the "expectations realized" scenario.
- **ch12-14**: repo financing and cash carry in forwards/futures pricing.
- **ch19**: spread curves for corporate bonds and CDS.
- **`cfa-level1-curriculum` ch18**: CFA treatment of yield measures, return decomposition and rolling yield.
