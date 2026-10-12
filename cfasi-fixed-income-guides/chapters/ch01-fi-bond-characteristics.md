# Chapter 1: Main Characteristics of Fixed Income Securities
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 1 (Le principali caratteristiche dei titoli a reddito fisso) | Denis Manzi, CFA

## Core Idea
A bond is a contract: who pays what, when, in which currency, ranked where in the creditor queue, and with which options for either party. Every later risk and valuation question (duration, spread, call risk, recovery) is a function of a handful of contract terms. Read the **indenture** first; the term sheet headline (coupon, maturity) hides the features that decide the outcome.

## Frameworks Introduced
- **Bond contract decomposition** (par, coupon type, maturity, amortization, currency, seniority, embedded options)
  - When to use: before pricing or comparing any bond.
  - How: (1) par and quote convention (price as % of par); (2) coupon formula (fixed, zero, floating, reverse floating, step, mixed, inflation-linked); (3) principal schedule (bullet vs amortizing); (4) currency of coupons vs principal; (5) seniority; (6) options (call, put, conversion, write-down); (7) covenants.
  - Why it works: price = PV of contractual cash flows plus or minus the value of options; each feature maps to one valuation term.
- **Coupon-formula taxonomy**
  | Type | Coupon | Wants | Typical protection |
  |---|---|---|---|
  | Fixed | c × par | Falling rates | none |
  | Zero | none; return = redemption minus price | Falling rates (highest sensitivity) | none |
  | Floater | reference rate + margin | Rising rates | cap (max), floor (min) |
  | Reverse floater | X − Leverage × reference | Falling rates | floor at 0% |
  | Step-up / step-down | pre-set rising / falling schedule | known path | n/a |
  | Mixed | fixed then floating (or reverse) | depends on phase | n/a |
  | Inflation-linked | fixed real rate × index ratio, principal also indexed | Higher inflation than breakeven | n/a |
- **Breakeven inflation read-through**: breakeven = nominal yield minus real (inflation-linked) yield at the same maturity. Buy the linker if you expect inflation above the breakeven.
- **Call-price structures**: (1) fixed and constant; (2) variable by date (a call schedule, e.g. 105 / 102.5 / 100 after years 5 / 6 / 7+); (3) make-whole (price = PV of remaining cash flows at benchmark yield + fixed spread).
- **Clean vs dirty price**: dirty = clean + accrued interest (rateo). The buyer pays the seller the accrued coupon.

## Key Concepts
- **Indenture (regolamento di emissione)** — the legal document stating holders' rights, issuer duties and bond terms; normally names a trustee.
- **Trustee** — the representative of bondholders who monitors the issuer's compliance.
- **Covenant** — clause binding the issuer; affirmative (pay interest and principal on time) or negative (no debt above a set level).
- **Par / face / redemption value** — the amount repaid at maturity; prices are quoted as % of par (above 100 = premium, below 100 = discount).
- **Maturity buckets (market convention)** — short term 1–5 years, medium 5–12, long above 12.
- **Zero-coupon bond** — pays no coupons; interest is the gap between purchase and redemption price.
- **Cap / floor on a floater** — maximum / minimum coupon regardless of the reference rate.
- **Index ratio** — inflation-capitalization factor applied to both coupon and principal of a linker, rebased at issue.
- **Convertible bond** — holder may swap into shares at a fixed conversion ratio; the issuer has implicitly sold an equity option, so the coupon is lower than on a plain bond.
- **Contingent convertible / write-down (CoCo)** — bank paper that automatically converts to shares or has its par cut when capital ratios fall below a trigger (detail in ch03).
- **Bullet vs amortizing** — 100% of principal at maturity vs pre-set instalments (reduces credit risk).
- **Dual-currency bond** — coupons in one currency, principal in another.
- **Callable (issuer put-back right)** — issuer may redeem early at the call price from the first call date; exercised when it can refinance more cheaply.
- **Putable** — holder may demand early repayment; exercised when market rates rise above the bond's.
- **Seniority** — priority in liquidation: senior secured > senior unsecured > subordinated.
- **Accrued interest (rateo)** — coupon earned since the last coupon date.

## Formulas & Reference Tables
- Coupon cash amount per period: `C = (coupon rate / m) × par` (m = payments per year). EUR 100,000 at 2% semiannual: `(2%/2) × 100,000 = 1,000`.
- Zero-coupon simple annual return: `[(Pr/Pa) − 1] / N`; compound: `(Pr/Pa)^(1/N) − 1` (Pr = redemption price, Pa = purchase price, N = years).
- Floater: `Coupon = reference rate + margin` (margin rises with issuer risk); with cap/floor: `min(cap, max(floor, ref + margin))`.
- Reverse floater: `Coupon = X − L × ref`; with floor `max(0, X − L × ref)`.
- Linker coupon: `C = VN × IRF × CF` (VN = par, IRF = index ratio at payment date, CF = fixed real coupon rate); principal repaid = `VN × IRF`.
- Breakeven inflation: `BEI = y_nominal − y_real`.
- Convertible: parity per share = par / shares per bond; convert when share price > par / conversion ratio.
- Make-whole call price: PV of remaining coupons and principal discounted at `benchmark yield + make-whole spread`.
- Dirty price: `Dirty = Clean + Accrued`; `Accrued = coupon × (days since last coupon / days in period)`.

## Mental Models
- Use the **coupon formula** to infer which rate view the instrument expresses: floater = long rates up, reverse floater = leveraged long rates down.
- Use **breakeven** as a market-implied inflation forecast, not a certainty: the linker wins only if realized inflation exceeds it.
- Use **"embedded option = who owns it"**: issuer-owned options (call, CoCo conversion) are paid for with a higher coupon; holder-owned options (put, convert) with a lower coupon.
- Use **seniority plus covenants** as the credit-protection layer: same issuer, different tranche, very different loss given default.

## Worked Example
Make-whole call. 10-year, 3% annual-coupon bond issued at 100; five years after issue the issuer calls make-whole at benchmark + 50 bp; the 5-year benchmark yields 1.0%.
1. Discount rate = 1.0% + 0.50% = 1.5%.
2. Remaining cash flows: four coupons of 3 and a final 103.
3. Price = `3/1.015 + 3/1.015² + 3/1.015³ + 3/1.015⁴ + 103/1.015⁵ = 107.17` (recomputed: 107.174).
4. Interpretation: the holder is repaid above par, so the make-whole call compensates for lost coupons; the issuer has little incentive to call unless it can refinance far cheaper.

Linker coupon: par 100, fixed 2%, index ratio rebased to 100 at issue, 2% inflation in year 1: `C = 100 × 1.02 × 2% = 2.04`. If the final index ratio is 120%, principal repaid is 120 per 100 of par.

Zero coupon bought at 90, redeemed at 100 in 5 years: simple 2.22% per year, compound 2.13% per year (recomputed). Quote the compound figure for comparisons.

## Anti-patterns
- Comparing the simple annual return of a zero with the yield of a coupon bond.
- Buying a floater "for the coupon" without checking the cap (the cap makes it behave like a fixed bond when rates rise) or the floor.
- Treating a convertible as "bond plus free upside": the lower coupon is the price of the option.
- Ignoring the call schedule and first call date when judging yield.
- Quoting a price without saying clean or dirty.

## Practitioner Notes
- The guide mixes a sponsor insert ("Le 5 variabili da monitorare", 2018 outlook on inflation, politics, credit, emerging markets, income) that is date-bound market commentary; the only lasting point is that with low coupons, total return depends on capital gains, so selectivity matters. It is not reproduced.
- Reverse floaters typically carry a 0% coupon floor; check it, because the leverage `L` multiplies duration.
- Rule of thumb: the higher the issuer's credit risk, the larger the floater margin.

## Key Takeaways
1. A bond is defined by its indenture; read covenants, trustee, seniority and options.
2. Prices are quoted as % of par; clean vs dirty differs by accrued interest.
3. Coupon type encodes the rate view: fixed and reverse floaters gain when rates fall, floaters when rates rise.
4. Cap and floor turn a floater into a bond with embedded options.
5. Linkers pay a real coupon on an indexed principal; breakeven = nominal yield minus real yield.
6. Callable bonds are paid for with extra yield; convertibles and puts are paid for with lower coupons.
7. Amortizing structures reduce credit risk; bullets concentrate repayment at maturity.
8. Make-whole calls price at benchmark + spread, so they protect the investor's yield.

## Connects To
- **ch02**: how each feature changes interest-rate, call, credit and liquidity risk.
- **ch03**: detail on subordinated, CoCo and structured bond types.
- **ch06**: price and yield calculations.
- **`cfa-fixed-income` ch01–ch03**: CFA treatment of bond features, indenture, covenants and markets.
