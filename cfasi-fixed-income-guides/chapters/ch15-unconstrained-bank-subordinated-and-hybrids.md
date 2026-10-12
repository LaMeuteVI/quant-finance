# Chapter 15: Bank Subordinated Debt and Non-Financial Hybrids
> **Source**: CFA Society Italy × Advisor Private, "Unconstrained Fixed Income" guide (Sept–Oct 2019), Chapter 4 (Subordinati bancari e ibridi non finanziari) | Luigi Pedone, CFA

## Core Idea
Bank Tier 2 and Additional Tier 1 (AT1) bonds and corporate hybrids pay a large yield premium over the same issuer's senior debt because they are subordinated, complex and, for AT1 and hybrids, coupon-discretionary. The premium is tied to specific, nameable risks: extension, bail-in, conversion/write-down and coupon cancellation. The 2016 Deutsche Bank AT1 sell-off and the 2019 Santander non-call show these are real, not theoretical. These instruments suit institutional or professional investors.

## Frameworks Introduced
- **Yield pick-up illustration (Bloomberg, 5 Aug 2019)**
  | Instrument | Ranking | Yield to maturity | Yield to call |
  |---|---|---|---|
  | Enel 1.5% 2025 | Senior unsecured | 0.13% | 0.07% |
  | Enel 3.5% 2080, callable 2025 | Hybrid | 3.05% | 2.42% |
  | Intesa 4% 2023 | Senior unsecured | 0.52% | n/a |
  | Intesa 6.625% 2023 | Tier 2 | 1.48% | n/a |
  | Intesa 6.25% perpetual, callable May 2024 | AT1 | 5.51% | 5.59% |
  Reading: Enel hybrid yield to maturity is about 23 times the senior; Intesa Tier 2 about 3 times and AT1 about 11 times the senior yield (ratios of low-yield numbers, so read as spread pick-up in absolute bp: about 292 bp, 96 bp and 499 bp).
- **Bank capital stack (CRR IV)**: from senior down: deposits/secured debt, senior preferred, senior non-preferred, Tier 2 (about 2% of RWA, minimum 5-year maturity, no step-up clauses), AT1 (about 1.5% of RWA, perpetual, minimum loss-absorption trigger 5.125% CET1), CET1 (common equity). Specific risks: bail-in risk (non-preferred, T2, AT1), extension risk (T2, AT1), coupon cancellation and conversion risk (AT1 only).
- **Tier 2 features**: minimum 5 years; callable not before 5 years and only with regulator approval and replacement with equal or better capital; no incentive to redeem (no step-up, whereas earlier structures had coupon increases); coupons are mandatory (except when resolution triggered). Risks: **extension** (if not called or if regulation changes qualification, timing is uncertain), **bail-in** (principal written down or converted, coupon and maturity altered by the resolution authority even before formal insolvency).
- **AT1 features**: perpetual, callable after 5 years; fully discretionary non-cumulative coupons; junior to Tier 2; contractual loss absorption (conversion into shares or principal write-down) when CET1 falls below the trigger: 5.125% ("low trigger") or 7% ("high trigger"). Risks:
  1. Conversion/write-down risk.
  2. **Coupon risk**: cancellation (discretionary), imposed by regulator, or partial when capital falls below a regulatory level (MDA, above the contractual trigger).
  3. Extension risk: if not called at first call date, the coupon resets to a swap rate plus the initial spread ("reset spread" or back-end) for another period.
  4. Bail-in.
- **Non-financial hybrid features**: long maturity (30-50 years) or perpetual; subordination to senior unsecured; issuer call (typically 5-10 years) with step-up if not called (often capped near 100 bp so the issuer is not forced to call); optional coupon deferral. Equity credit (a percentage counted as equity by rating agencies) reduces cost relative to equity, avoids dilution and voting rights, improves ratings. Growth since 2007 has been rapid.
- **Deferral clause taxonomy**: dividend stopper (no dividends until hybrid interest paid), dividend pusher (mandatory interest if dividends are paid; may impair equity credit), mandatory deferral (triggered by financial ratio breach), cumulative vs non-cumulative deferral, cash cumulative (deferred coupons settled in cash) vs non-cash cumulative (settled through new shares).
- **Event case 1: Deutsche Bank AT1 coupon risk (February 2016)**: AT1 prices fell and yields above 10% (Unicredit and Deutsche) on doubts about ability to pay coupons amid oil collapse, macro fears and bail-in (in force from 1 January 2016). Investors focused on distributable reserves available for AT1 coupons and on the effect of a large annual loss on capital ratios; Deutsche responded with a statement of about EUR 1 billion of distributable reserves; later the regulator clarified how the capital level triggering coupon suspension is calculated.
- **Event case 2: Santander AT1 non-call (2019)**: AT1 issued with a 6.0% coupon (5-year euro swap plus 620 bp reset spread). At the first call date the issuer decided not to redeem because the reset coupon (swap at that time plus 620 bp) was lower than the cost of a refinancing at market conditions. The price barely moved, and the bond began to trade on a call within the following 12 months. Lesson: first-call redemption is an economic and regulatory decision, not a convention.

## Key Concepts
- **Tier 2 / AT1 / CET1** — layers of regulatory capital.
- **MDA (Maximum Distributable Amount)** — regulatory limit on distributions when capital buffers are breached.
- **Trigger (5.125% / 7% CET1)** — contractual level where AT1 converts or is written down.
- **Reset spread (back-end)** — spread added to the swap rate for the new coupon period after a missed call.
- **Bail-in** — loss absorption by creditors under resolution.
- **Resolution Authority** — body with power to write down, convert, amend maturity and coupon.
- **Equity credit** — share of a hybrid treated as equity by agencies.
- **Dividend pusher / stopper** — linkage between hybrid coupons and dividends.
- **Step-up cap** — maximum coupon increase (here about 100 bp).
- **Cumulative / non-cumulative deferral** — whether missed coupons accrue.

## Formulas & Reference Tables
- AT1 reset coupon: `Coupon_new = Swap_5y(t_reset) + Reset spread`.
- Call economics for the issuer: call if `Coupon_new > Cost of replacement capital` (including costs); do not call otherwise.
- Pick-up: `Pick-up (bp) = (Yield hybrid − Yield senior) × 100`.
- Rating gap rule from ch03: hybrid ratings typically 2-3 notches below the issuer's senior rating.
- 2019 hybrid issuance sample (Bloomberg): EnBW 2079 (NR), Accor perpetual (BB), Enel 2080 (BBB-), Merck 2079 (BBB), Telefonica perpetual (BB), Total perpetual (A-), LeasePlan perpetual (B+), Orange perpetual (BBB-); sizes EUR 300m to 1.5bn.

## Mental Models
- Use the stack to locate the risk: lower ranking implies more equity-like behaviour; the premium is the price of structure.
- Use yield to the first call as a base case, but stress to the reset coupon: if the reset coupon is below the issuer's replacement cost, plan for extension.
- Use coupon-source analysis (distributable reserves, MDA distance) for AT1, not just rating.
- Use the investor's profile: these are institutional instruments; retail suitability is weak given complexity.
- Use diversification across issuers and legal regimes; contractual details differ by bank.

## Worked Example
Santander-style AT1 reset decision.
1. Original coupon 6.0% = 5y swap `−0.20%` + 620 bp at issue.
2. At the first call date (5 years later), assume 5-year swap `= −0.30%`. Reset coupon `= −0.30% + 6.20% = 5.90%`.
3. Issuer's cost of issuing a new AT1 at that time: assume 6.5% (an illustrative figure).
4. Since 5.90% < 6.5%, keeping the old bond is cheaper: do not call. The investor now holds a 5.90% bond for another 5 years.
5. Price effect: if the market now values the bond to a call in 12 months at a required yield of 6.3%, the one-year carry shortfall is about `6.3% − 5.9% = 0.4` points, so the price drifts only a few tenths of a point below par. In the guide the observed move was brief and small because the market had already priced the uncertainty.
Interpretation: always compare the reset coupon with the issuer's replacement cost; never assume a first-call redemption.

## Anti-patterns
- Equating Tier 2 and AT1 risk because both are "bank subordinated".
- Buying AT1 on yield to call without stressing extension and coupon cancellation.
- Ignoring distance to MDA and distributable items.
- Assuming a step-up forces redemption; step-ups are capped and often limited.
- Treating hybrid corporate ratings as equal to the issuer's senior rating.
- Selling to retail clients without suitability checks.

## Practitioner Notes
- Rating agencies' equity credit explains why corporates issue hybrids: less expensive than equity, improves ratios.
- After 2016, regulators clarified MDA computation, which reduced one uncertainty; the 2019 Santander non-call caused only a brief dip, showing investors had learned the structure.
- Differences between banks (trigger levels, call practices) require instrument-level reading.

## Key Takeaways
1. Subordinates pay a large pick-up for structure: roughly 100 to 500 bp over senior in the August 2019 sample.
2. Tier 2: dated, mandatory coupons, bail-in and extension risks.
3. AT1: perpetual, discretionary non-cumulative coupons, contractual CET1 trigger (5.125% or 7%), conversion or write-down risk.
4. Coupon risk can come from issuer choice, regulator, or MDA constraints.
5. First call is an economic decision; reset spread governs extension economics.
6. Corporate hybrids offer equity credit to issuers and deferral to issuers; step-ups are capped.
7. Suitable mainly for institutional or professional investors.

## Connects To
- **ch03** (`cfasi-fixed-income-guides`): capital structure and TLAC, introduction to AT1, Tier 2 and hybrids.
- **ch12**: IG corporate bond spread analysis.
- **ch14**: convertibles as another hybrid.
- **ch13**: HY credit analysis for lower-rated hybrids.
- **`cfa-fixed-income` ch07**: bank capital and securitization context.
- **`cfa-financial-statement-analysis`**: capital ratios and bank regulatory analysis.
