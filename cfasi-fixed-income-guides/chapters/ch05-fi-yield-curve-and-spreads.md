# Chapter 5: The Yield Curve and the Types of Spread
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 5 (La curva dei tassi di interesse e le varie tipologie di spread) | Francesco Spadaccia, CFA

## Core Idea
The yield curve (term structure) maps yield against maturity for bonds of equal credit quality. Its level reflects monetary policy; its slope reflects expectations about growth, inflation and policy, plus a risk premium. Spreads measure what the market pays for the extra risks of a bond over the risk-free curve, and the choice of spread (nominal, Z-spread, OAS, asset swap) determines which risks are included or removed. Use Z-spread for option-free bonds, OAS for bonds with options, and remember that option cost is the gap between the two.

## Frameworks Introduced
- **Level and slope reading of the curve**
  | Shape | Slope | Typical reading |
  |---|---|---|
  | Normal (upward) | Long yield > short yield | Normal compensation for volatility, inflation and default risk at long maturities; growth expected |
  | Flat | Roughly equal | Slowdown expected; usually a transition state |
  | Inverted | Long yield < short yield | Expected rate cuts, recession or deflation; rarely lasts |
  - Steepening = long-short gap widens (market expects higher short rates and better growth); flattening = gap narrows (expects cuts and slowing).
- **Three theories of the term structure**
  | Theory | Claim | Implication | Weakness |
  |---|---|---|---|
  | Expectations | Maturities are perfect substitutes; long rate = geometric average of expected short rates; forward rates are unbiased predictors | Upward slope = rising short rates expected; flat = unchanged | Ignores risk: price at future date is not certain |
  | Liquidity preference | Long bonds must pay a premium for price volatility and default exposure; forwards are biased upward estimates | Curve normally upward-sloping; any shape = expectations + premium | The premium is unobservable |
  | Market segmentation (preferred habitat) | Investor groups (banks, insurers, pension funds) have fixed maturity needs and do not leave them; each segment clears on its own supply and demand | Slope reflects relative demand for long vs short | Implies no arbitrage across maturities, which arbitrageurs contest |
- **Spot-forward indifference condition** (basis of the expectations theory): an investor with a 1-year horizon is indifferent between a 1-year bond and rolling a 6-month bond at the forward rate.
- **Spread ladder (what each spread captures)**
  | Spread | Definition | Fixes | Still ignores |
  |---|---|---|---|
  | Nominal spread | Bond YTM minus YTM of same-maturity government bond | Nothing; simple | Curve shape and future rate volatility |
  | Z-spread (zero-volatility) | Constant spread added to every spot rate of the risk-free curve so PV of cash flows equals market price | Term structure | Option exercise driven by rate volatility |
  | OAS (option-adjusted) | Constant spread to the spot curve that equates the model fair value (with option exercise under assumed volatility) to market price | Term structure and embedded options | Model dependence (volatility, curve) |
  | ASW spread | Fixed spread over Euribor/Libor on an asset swap with zero initial NPV | Converts to floating-rate basis | Like Z-spread: credit, option and liquidity are priced together |
  - Nominal, Z and ASW spreads all embed credit risk, option risk and liquidity risk. OAS strips out the option.
- **Option-cost identity**: `Option cost = Z-spread − OAS`. Positive: investor sold an option to the issuer (callable). Negative: investor owns an option (putable).
- **When nominal and Z-spread diverge**: they differ more with a steep curve, a long maturity, and amortizing principal; they coincide for a flat curve (and are very close for short maturities).

## Key Concepts
- **Term structure / yield curve** — yield as a function of maturity for equal credit quality; government bonds (and interbank rates for the short end up to 12 months) are used.
- **Level vs slope** — level is driven by central bank policy (e.g. QE shifted it down); slope is the long-short yield difference and is among the most reliable cycle indicators.
- **Spot rate** — discount rate for a single cash flow at a given maturity.
- **Forward rate** — rate for a future period implied by today's curve.
- **Bootstrapping** — building spot (zero-coupon) rates from market prices of coupon bonds.
- **Risk premium** — extra yield for long-maturity risk (volatility, inflation, default).
- **Nominal spread** — simple yield difference over the same-maturity risk-free bond.
- **Z-spread** — see above; usable only for held-to-maturity valuation without option exercise.
- **OAS** — decreases when assumed volatility is higher (for a callable bond), because the option is worth more.
- **Asset swap** — derivative exchanging the bond's fixed coupons for floating (Euribor/Libor) plus the fixed ASW spread.
- **Spread duration/credit cycle outlook** — the guide's sponsored insert favours securitized credit, US and European HY, AT1 and local-currency EM bonds, while underweighting long-duration, tight-spread sectors in a rising-rate world (attributable to the sponsor, dated 2018).

## Formulas & Reference Tables
- Expectations theory, two periods: `(1 + R2)^2 = (1 + r1) × (1 + f)` where `R2` is the 2-year spot rate, `r1` the current 1-year rate and `f` the expected 1-year rate starting in one year. **⚠ Correction**: the guide writes `(1 + r_n) = (1 + r_1)(1 + r_2)`, where `r_n` is the two-year compounded return; as a per-year rate the left side must be squared (or use the 2-period total return).
- Implied forward: `f = (1 + R2)^2 / (1 + R1) − 1`.
- Z-spread: find `z` such that `P = Σ C_t / (1 + r_t + z)^t + (F) / (1 + r_n + z)^n`, with `C_t` coupons, `F` redemption, `r_t` risk-free spot rates.
- Nominal spread: `YTM(bond) − YTM(government bond of equal maturity)`; example: 6% − 4% = 200 bp.
- Option cost: `Z-spread − OAS`.
- Asset swap: the ASW spread is the fixed amount that makes the swap's initial NPV zero.

## Mental Models
- Use the curve slope as a cycle gauge: steepening for recovery, flattening or inversion for slowdown.
- Use Z-spread for corporate relative value among straight bonds; switch to OAS as soon as a call or put is present.
- Use `Z-spread − OAS` to price an embedded option implied by the market, and compare it with your own volatility view.
- Use the three theories together: expectations set the base path, liquidity premium adds the positive tilt, segmentation explains local distortions (e.g. pension demand for long bonds).
- Use ASW spread when comparing a fixed bond to floating-rate funding or to bonds in other currencies swapped to a common base.

## Worked Example
Two-year 5% annual bond, risk-free spot curve R1 = 2%, R2 = 3%, market price 98.00 (inputs chosen by the writer).
1. Risk-free value: `5/1.02 + 105/1.03^2 = 4.902 + 98.972 = 103.87`.
2. Z-spread: solve `5/(1.02+z) + 105/(1.03+z)^2 = 98.00`. Result `z = 3.117%` (about 312 bp).
3. YTM of the bond at 98.00: 6.092%. The 2-year risk-free par yield from the spot curve: `(1 − 1/1.03^2) / (1/1.02 + 1/1.03^2) = 2.985%`. Nominal spread = 6.092% − 2.985% = 3.107% (about 311 bp).
4. Forward rate: `f = 1.03^2/1.02 − 1 = 4.010%`.
Interpretation: nominal and Z-spreads differ by only about 1 bp here (short maturity, mild slope); they would diverge on a 10-year bond on a steep curve. If the bond were callable with OAS of 2.60%, the embedded option cost would be 3.117% − 2.60% = 0.52 pp.

## Anti-patterns
- Reading an inverted curve as an immediate sell signal without dating the lead time.
- Quoting a spread to a "benchmark" of mismatched maturity.
- Using Z-spread to compare callable bonds; it overstates the compensation for credit.
- Treating OAS as model-free; a different volatility assumption changes it.
- Believing forwards are forecasts; under liquidity preference they contain a premium.
- Comparing ASW spreads across different swap curves (Euribor vs Libor) without adjustment.

## Practitioner Notes
- The guide's 2018 context: QE depressed the level; steepening was expected as support ended.
- Higher assumed volatility lowers the OAS of a callable (option is worth more), a standard sanity check on vendor OAS.
- ASW spread is a quote convention in European credit trading desks; consistent curve choice matters more than the level.

## Key Takeaways
1. Curve level follows policy; slope signals growth and inflation expectations.
2. Expectations, liquidity preference and segmentation are complementary explanations of the shape.
3. Spot rates discount a single cash flow; forward rates are implied future spot rates.
4. Nominal spread ignores curve shape and options; Z-spread fixes the curve; OAS fixes options too.
5. `Z-spread − OAS` equals the option's cost to the holder.
6. OAS depends on the model and on assumed rate volatility.
7. ASW spread translates a fixed-rate bond into a floating-rate spread with zero initial NPV.

## Connects To
- **ch02**: curve risk and credit spread risk.
- **ch03**: callable, hybrid and subordinated bonds where OAS matters.
- **ch06**: pricing from spot rates, duration and spread duration.
- **ch09**: unconstrained funds expressing curve views.
- **`cfa-fixed-income` ch09 / `tuckman-fixed-income`**: spot, forward and term-structure models in depth.
- **`ilmanen-yield-curve`**: empirical term premium and curve behavior.
