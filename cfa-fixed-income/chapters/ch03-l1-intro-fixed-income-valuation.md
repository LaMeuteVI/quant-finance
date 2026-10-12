# Chapter 3: Introduction to Fixed-Income Valuation
> **Source**: CFA Program Curriculum 2020, Level I, Reading 44 · Fixed Income | James F. Adams, PhD, CFA, and Donald J. Smith, PhD

## Core Idea
A bond is a stream of promised cash flows, and its price is the present value of that stream. Discount everything at one rate (the yield-to-maturity) for a quick quote, or discount each flow at its own spot rate for the no-arbitrage value. Every other tool in the reading (accrued interest, matrix pricing, money-market yields, forwards, spreads) exists to translate quotes and conventions into that one DCF identity.

## Learning Outcomes Covered
- Calculate a bond price from a market discount rate; relate price to coupon, maturity and yield
- Define spot rates and price a bond with spot rates (no-arbitrage value)
- Calculate flat price, accrued interest, full price; describe matrix pricing
- Convert annual yields across compounding periodicities
- Compute and interpret yield measures for fixed-rate bonds, FRNs (discount margin) and money market instruments (discount rate, add-on rate, BEY)
- Compare spot curve, coupon-bond yield curve, par curve, forward curve
- Compute forward rates from spot rates, spot from forward, and price a bond with forwards
- Compare G-spread, I-spread, Z-spread, OAS

## Frameworks Introduced
- **Market discount rate pricing (Equation 1)**: `PV = PMT/(1+r) + … + (PMT+FV)/(1+r)ᴺ`, r per period
  - When to use: option-free fixed-rate bond priced on a coupon date; also to back out yield-to-maturity (IRR of the flows).
  - How: (1) set N = years × frequency; (2) r = stated annual yield ÷ frequency; (3) PMT = coupon rate × par ÷ frequency; (4) solve PV.
  - Failure mode: single-rate pricing hides the term structure; two very different spot curves can give the same price and YTM (see Worked Example 2).
- **Premium/discount by "deficiency or excess" decomposition**: price = 100 ± PV of (coupon rate − r) × 100 per period over N periods.
  - When to use: to sanity-check a price and see why it sits away from par (coupon below r is deficient, so discount; coupon above r is excessive, so premium; equal, so par on a coupon date at any maturity).
- **Four price-yield relationships**: inverse, convexity, coupon effect, maturity effect (with the low-coupon discount-bond exception).
  - When to use: rank bonds by rate sensitivity without computing durations.
  - How: lower coupon means larger % price change; longer maturity means larger % change; drops in yield lift price more than equal rises cut it.
  - Failure mode: the maturity effect can fail for low-coupon (not zero-coupon), long-maturity bonds trading at a discount (e.g., 10% coupon at 20% yield: 20-year moves more than 30-year).
- **Spot-rate (no-arbitrage) valuation (Equation 2)**: `PV = PMT/(1+Z₁) + PMT/(1+Z₂)² + … + (PMT+FV)/(1+Z_N)ᴺ`
  - When to use: relative value, arbitrage checks, stripping and reconstituting bonds. If market price differs from this value, there is an arbitrage in the absence of transaction costs.
- **Full-price / flat-price / accrued-interest system (Equations 3–6)**: dirty = clean + AI; full price `PV_Full = PV × (1+r)^(t/T)`.
  - When to use: any trade between coupon dates.
  - How: (1) get t, T under the day-count; (2) AI = (t/T) × PMT; (3) compute PV as if on the last coupon date with N remaining periods; (4) compound forward by t/T; (5) flat = full − AI.
- **Matrix pricing**: estimate the required yield of an illiquid or unissued bond from comparable, liquid bonds of similar credit quality, interpolating on maturity (and coupon).
  - When to use: illiquid bond marks, new-issue spread estimates.
  - How: (1) YTM of each comp; (2) average yields at each maturity bucket; (3) linearly interpolate to target maturity; (4) price with that yield.
  - Failure mode: comps must share credit quality; coupon differences matter for coupon-bond yields.
- **Periodicity conversion (Equation 7)**: `[1 + APR_m/m]^m = [1 + APR_n/n]^n`. Compare yields only at the same periodicity.
- **Yield-to-worst**: minimum of YTM and every yield-to-call; the conservative yield for callable bonds. Option-adjusted yield/OAS replace it when an option model and volatility assumption are available.
- **FRN discount-margin model (Equation 8)**: like Equation 1 with `(Index+QM)/m` as coupon and `(Index+DM)/m` as discount rate.
- **Money-market rate toolkit (Equations 9–12)**: discount-rate vs add-on-rate pricing; convert everything to a bond-equivalent yield (BEY, add-on for a 365-day year) before comparing.
- **Curve family**: spot (zero) curve, coupon-bond yield curve, par curve, forward curve; each derivable from the others.
- **Forward-rate identity (Equation 14)**: `(1+z_A)^A × (1+IFR_{A,B−A})^(B−A) = (1+z_B)^B`.
- **Spread ladder**: G-spread (over interpolated government YTM), I-spread (over interpolated swap rate), Z-spread (constant spread over the whole spot curve), OAS = Z-spread − option value.

## Key Concepts
- **Market discount rate (required yield)**: rate of return investors require given the bond's risk; used to discount cash flows.
- **Yield-to-maturity (YTM)**: IRR of the promised flows; assumes hold to maturity, no default, reinvestment of coupons at the YTM itself.
- **Discount / par / premium bond**: price below / equal to / above par, driven by coupon rate versus market discount rate.
- **Pull to par**: with constant yield, flat price converges to par as maturity nears (constant-yield price trajectory).
- **Spot rate (zero rate)**: YTM on a zero-coupon bond for a given maturity; also called strip rate; "spot" here is not the cash-market sense.
- **Flat (clean, quoted) price / full (dirty, invoice) price**: full = flat + accrued interest; dealers quote flat to avoid a saw-tooth price pattern.
- **Accrued interest**: `(t/T) × PMT`, independent of yield; ignores time value of money, so flat price is slightly low relative to theory.
- **Day-count conventions**: actual/actual (typical for government bonds), 30/360 (typical for corporates), actual/360 and actual/365 (typical for FRNs and money market).
- **Street convention vs true yield vs government equivalent yield**: street ignores weekends and holidays; true uses the actual calendar (never higher than street, usually 1-2 bp lower); government equivalent restates a 30/360 yield to actual/actual.
- **Current (running) yield**: annual coupon ÷ flat price; ignores gain or loss to par and reinvestment. **Simple yield** adds straight-line amortization of the discount or premium (quoted mostly on JGBs).
- **Yield-to-call / yield-to-worst / option-adjusted yield**: yield measures for callable bonds; call price replaces FV and call date replaces maturity.
- **Quoted margin vs required margin (discount margin)**: fixed spread in the FRN contract vs spread investors currently demand to price at par on a reset date.
- **Discount rate (money market) vs add-on rate**: discount rate divides interest by FV (understates return); add-on rate divides by PV.
- **Bond equivalent yield (BEY)**: add-on rate for a 365-day year; the common denominator for money market comparisons.
- **Par curve**: YTMs at which bonds of each maturity price at exactly par; derived from spot rates.
- **Implied forward rate (forward yield)**: breakeven reinvestment rate linking two zero-coupon investments; notation "2y5y" = 5-year tenor starting in 2 years.
- **On-the-run / off-the-run**: newest, most liquid benchmark issue vs seasoned issues (off-the-run yield slightly higher).
- **Yield spread building blocks**: benchmark (expected real rate + expected inflation) plus spread (credit, liquidity, taxation).

## Formulas & Reference Tables
Notation: r = market discount rate per period; N = periods; PMT = coupon per period; FV = par (or call price); t = days since last coupon; T = days in coupon period; Zₖ = spot rate for period k; m, n = periodicities.

| # | Formula | Notes |
|---|---|---|
| 1 | `PV = Σₖ PMT/(1+r)ᵏ + FV/(1+r)ᴺ` | price on a coupon date; YTM solves this for r |
| 2 | `PV = Σₖ PMT/(1+Zₖ)ᵏ + FV/(1+Z_N)ᴺ` | no-arbitrage value |
| 3 | `PV_Full = PV_Flat + AI` | full = invoice price |
| 4 | `AI = (t/T) × PMT` | yield-independent |
| 5 | `PV_Full = PMT/(1+r)^(1−t/T) + PMT/(1+r)^(2−t/T) + … + (PMT+FV)/(1+r)^(N−t/T)` | between coupon dates |
| 6 | `PV_Full = [PMT/(1+r) + … + (PMT+FV)/(1+r)ᴺ] × (1+r)^(t/T)` | bracket = Equation 1 (N periods from last coupon), calculator-friendly |
| 7 | `(1 + APR_m/m)^m = (1 + APR_n/n)^n`, so `APR_n = n[(1+APR_m/m)^(m/n) − 1]` | fewer compounding periods gives higher APR |
| 8 | `PV = Σₖ [(Index+QM)·FV/m] / [1+(Index+DM)/m]ᵏ + FV/[1+(Index+DM)/m]ᴺ` | simplified FRN model on a reset date, 30/360 |
| 9 | `PV = FV × [1 − (Days/Year) × DR]` | discount-rate instruments (T-bills, CP, BAs) |
| 10 | `DR = (Year/Days) × (FV−PV)/FV` | denominator is FV, so DR understates return |
| 11 | `PV = FV / [1 + (Days/Year) × AOR]` | add-on instruments (CDs, repo, time deposits, Libor/Euribor) |
| 12 | `AOR = (Year/Days) × (FV−PV)/PV` | proper simple-interest yield |
| 13 | par rate (per period) `= (1 − d_N) / Σₖ dₖ`, `dₖ = 1/(1+Zₖ)ᵏ` | par curve from spot curve (PV = FV = 100 in Equation 2, solve PMT) |
| 14 | `(1+z_A)^A × (1+IFR_{A,B−A})^(B−A) = (1+z_B)^B` | forward from spots; periods must match the rate's periodicity |
| 15 | `PV = Σₖ PMT/(1+Zₖ+Z)ᵏ + FV/(1+Z_N+Z)ᴺ` | Z-spread Z is constant, solved numerically |

Other identities:
- Spot from forwards (annual): `(1+z_N)ᴺ = (1+f₀,₁)(1+f₁,₁)…(1+f_{N−1,1})`; a bond can equally be valued by discounting with cumulative products of forward rates.
- Percentage price change: `(New − Old)/Old`.
- Current yield `= annual coupon / flat price`.
- Yield-to-worst `= min(YTM, YTC₁, YTC₂, …)`.
- `OAS = Z-spread − option value (bp per year)`; option value `= price(option-free) − price(callable)`.
- Yield spread `= YTM − benchmark`; 1 bp = 0.01%.
- BEY from a 360-day add-on: multiply by 365/360.
- Discount-rate to add-on: (1) price via Eq. 9, (2) AOR via Eq. 12 with Year = 365.

Yield-curve taxonomy:

| Curve | Built from | Reinvestment risk? | Use |
|---|---|---|---|
| Spot (zero, strip) | zero-coupon YTMs | none | discounting; term structure analysis |
| Yield curve on coupon bonds | on-the-run YTMs, interpolated | yes | quoting, benchmarks |
| Par curve | YTMs of par-priced bonds | yes | coupon-setting for new par bonds |
| Forward curve | forward rates of constant tenor | n/a | breakeven reinvestment, derivatives |

Money-market quoting conventions:

| Instrument | Quote basis | Year |
|---|---|---|
| T-bills, commercial paper, BAs | discount rate (often) | 360 (USD) |
| CDs, repo, time deposits, Libor/Euribor | add-on rate | 360 or 365 by market |
| Standardized comparison | BEY | 365 |

## Mental Models
- **Price = 100 ± PV of the coupon gap**: a bond is a par bond plus an annuity of (coupon − yield) × 100. Discounts and premiums are just annuities of deficiency or excess.
- **Spot rates are the truth; YTM is an average**: the YTM is the single rate that reproduces the price the spot curve already set. Two bonds can share a YTM while their curves differ.
- **Forward rate = breakeven reinvestment rate**: buy the longer zero if you expect the future short rate below the forward; roll shorter zeros if you expect it above.
- **Clean price for talking, dirty price for paying**: quote comparisons use flat prices; cash settlement always uses full price.
- **Compare like with like**: always align periodicity, day-count and quote basis (discount vs add-on) before calling any yield difference "compensation".
- **Benchmark plus spread**: decompose YTM into macro (benchmark) and micro (credit, liquidity, tax) so that shifts in curve level and shifts in spread are diagnosed separately.
- **FRN = fixed-rate bond in credit, near-cash in rates**: a reset-date FRN prices at par unless required margin differs from quoted margin, so its price risk is credit risk only.

## Worked Example
**1. Full price, accrued interest, flat price (actual/actual).** 5% semiannual government bond maturing 15 Feb 2028; settlement 14 May 2019; t = 88, T = 181; stated YTM 4.80% (r = 2.40% per period); 18 periods at the last coupon date (15 Feb 2019).
- Step 1: `PV = 2.5·[1−1.024⁻¹⁸]/0.024 + 100·1.024⁻¹⁸ = 101.44779`.
- Step 2: `PV_Full = 101.44779 × 1.024^(88/181) = 102.62432`.
- Step 3: `AI = (88/181) × 2.5 = 1.21547`.
- Step 4: `PV_Flat = 102.62432 − 1.21547 = 101.40885`.
- Interpretation: AI does not depend on the yield, so all yield sensitivity sits in the flat price.

**2. Same YTM from different spot curves.** 4-year 3% annual bond.
- Spot curve A: 0.39%, 1.40%, 2.50%, 3.60%. Price = 3/1.0039 + 3/1.014² + 3/1.025³ + 103/1.036⁴ = 98.104.
- Spot curve B: 4.08%, 4.01%, 3.70%, 3.50% gives 98.104 as well (the source's rounded rates reproduce it to about 0.0001).
- YTM (solve Equation 1 on 98.104) = 3.516% for both.
- Interpretation: one number cannot identify a curve; use spot rates when the curve shape matters (e.g., stripping, relative value).

**3. Forward rate and breakeven.** 3-year and 4-year zeros at 3.65% and 4.18% (semiannual basis). A = 6, B = 8: `(1.01825)⁶ × (1+f)² = (1.0209)⁸`, so f = 2.8891% per period and the "3y1y" forward = 5.778% annualized (×2).
- Interpretation: buying the 4-year rather than the 3-year earns 5.778% on the incremental year; if you expect the 1-year rate in 3 years to be below 5.778%, prefer the 4-year zero.

**4. Money-market comparison (90 days).** Commercial paper at 5.76% discount rate (360): price = 100 × (1 − 0.0576 × 90/360) = 98.560; AOR (365) = (365/90) × (1.44/98.56) = 5.925%. A time deposit quoted at 5.90% BEY is worse by 2.5 bp despite the higher-looking add-on.

**5. Discount margin.** 5-year FRN, 3M Libor 1.10%, QM 0.75%, price 95.50. Periodic coupon = (0.011+0.0075)×100/4 = 0.4625; solve N = 20 for r = 0.7045% per period; DM = 4r − Index = 2.818% − 1.10% = 1.718%. Required margin rose from 75 bp to about 172 bp (credit downgrade), hence the discount.

## Anti-patterns
- **Comparing YTMs with different periodicities**: a 10.696% quarterly-compounded bond is not 6.6 bp above a 10.630% semiannual one; converted to the same basis the gap is about 20.9 bp.
- **Comparing a discount rate to an add-on rate**: the discount rate divides by FV and understates return; a 5.76% CP discount rate is a 5.925% BEY.
- **Quoting or comparing full prices as "price trend"**: AI ramps daily and drops at each coupon; use flat prices.
- **Equating YTM with realized return**: it holds only with hold-to-maturity, no default, and reinvestment at the YTM itself.
- **Using YTM for a callable bond**: quote yield-to-worst, or option-adjusted yield/OAS if you have a volatility view.
- **Applying the maturity effect blindly**: fails for long-dated, low-coupon discount bonds (not zero-coupons).
- **Reading current yield as total return**: it ignores pull to par and reinvestment; for a 2% 10-year at 95 it gives 2.105% vs a YTM near 2.5%.
- **Matrix-pricing with comps of different credit quality**: the interpolated yield then embeds a hidden spread error.
- **Treating "discount rate" as one thing**: in the money market it is a specific quoting convention, not a present-value rate.

## Exam Focus & Traps
- **Flat price vs par**: at YTM = coupon rate between coupon dates the flat price is slightly below par (30/360 example: 99.989), because AI ignores time value; full price is still correct.
- **Periodicity conversion direction**: lower compounding frequency requires a higher APR (semiannual 4.96% becomes 5.02% effective annual; quarterly 4.93%). Negative yields flip intuition: more frequent compounding gives a more negative APR.
- **Spot vs forward notation**: "2y5y" = 5-year rate starting in 2 years (a 7-year maturity today), not a 2-year rate in 5 years. Use per-period rates when plugging into Equation 14: A, B in periods, z = annual/2 for semiannual quotes.
- **Yield-to-worst is the lowest of all yields, including YTM**: the sequence is computed with call prices as FV and call dates as N; in the source example (call 102/101/100) the worst was the yield-to-third-call (6.953%) versus YTM 7.070%.
- **FRN discount margin logic**: if quoted margin > required margin, price above par at the next reset (premium); if QM < DM, discount. QM = DM means par.
- **Money market**: discount-rate instruments price with `1 − DR × Days/Year`; add-on with `1/(1 + AOR × Days/Year)`. Convert 360-day add-on to BEY by multiplying by 365/360; discount rate must be converted to price first, then to an add-on rate.
- **Bond vs money market yields**: bond YTMs are compounded with a fixed periodicity; money-market yields are simple and their periodicity = Year/Days (differs by tenor).
- **Spreads**: G-spread uses a single-YTM benchmark; Z-spread uses the whole spot curve (constant across all cash flows); I-spread uses the interpolated swap rate; OAS = Z-spread − option value, so it is smaller than the Z-spread for a callable bond.
- **Which benchmark**: government YTM for USD, GBP, JPY; EUR swap "mid-swaps" for euro corporates; century bonds priced over the 30-year Treasury.
- **Calculator traps**: N must be periods (years × frequency); solve PV first at the last coupon date, then multiply by (1+r)^(t/T); take the day-count consistent with the bond (actual/actual government, 30/360 corporate).
- **Convexity effect statement**: percentage price rise for a yield fall is larger than the percentage price drop for an equal rise; do not confuse with the coupon effect.
- **Errata**: no correction listed for Reading 44 in the CFA errata file (the errata entry labelled Reading 44 belongs to a different volume). The 2y5y example (5.8372%) is a semiannual-basis rate, equal to 2 × [(100/75)^(1/10) − 1].

## Key Takeaways
1. Price any option-free bond as the PV of flows: per-period r, N periods, price = par ± PV of the coupon gap; on a coupon date a coupon equal to the yield gives par at any maturity.
2. Use spot rates for the no-arbitrage value; YTM is only an IRR and can hide very different curves that price identically.
3. Quote in flat price, settle in full price; AI = (t/T) × PMT, independent of yield, with the day-count (actual/actual vs 30/360) chosen per market.
4. Rank rate sensitivity quickly: low coupon and long maturity means high % price change, and yield drops help more than yield rises hurt (convexity).
5. Always convert to a common periodicity before comparing yields; fewer compounding periods needs a higher APR.
6. For callables use yield-to-worst; for FRNs use discount margin against quoted margin; for money-market paper convert to BEY before comparing.
7. Build matrix-pricing estimates from comps of equal credit quality by averaging yields per maturity and interpolating linearly; then price with the interpolated yield.
8. A forward rate is the breakeven reinvestment rate: extend maturity if you expect future rates below the forward, roll if above.
9. Choose the spread by purpose: G-spread for quick government comparison, I-spread for swap-based comparison, Z-spread for full-curve credit compensation, OAS to strip out embedded-option value.

## Connects To
- **ch01**: bond features (coupon types, embedded options) that determine which yield measure applies (YTC for callables, discount margin for FRNs).
- **ch02**: market structure, day counts and money-market instruments (T-bills, CP, repo) whose quoting conventions are priced here.
- **ch04**: pass-through and ABS valuation extends this DCF logic to uncertain cash flows (prepayment, spreads like nominal or Z-spread).
- **ch05**: duration and convexity quantify the price-yield relationships (coupon, maturity, convexity effects) introduced qualitatively here.
- **ch06**: credit analysis explains what the yield spread (G, I, Z) is compensating for.
- **ch07**: term structure dynamics builds on spot, par and forward curves defined here.
- **ch08**: arbitrage-free valuation formalizes spot-rate pricing and binomial trees, and Z-spread and OAS reappear there.
- **ch09**: OAS and option-adjusted yield for bonds with embedded options.
- **`tuckman-fixed-income` ch01**: discount factors and no-arbitrage pricing (law of one price, stripping) behind Equation 2.
- **`tuckman-fixed-income` ch02**: spot, forward and par rates in continuous and discrete compounding, the deeper treatment of Equations 13 and 14.
- **`tuckman-fixed-income` ch03**: returns, spreads and yields, including the limits of YTM and yield-spread measures.
