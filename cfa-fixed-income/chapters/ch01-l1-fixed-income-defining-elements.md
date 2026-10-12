# Chapter 1: Fixed-Income Securities: Defining Elements
> **Source**: CFA Program Curriculum 2020, Level I, Reading 42 · Fixed Income | Moorad Choudhry, PhD, FRM, FCSI, and Stephen E. Wilcox, PhD, CFA

## Core Idea
A bond is a contract, so analyze it in three layers: (1) the **basic features** (issuer, maturity, par, coupon rate and frequency, currency) that fix the *scheduled* cash flows; (2) the **legal, regulatory and tax** wrapper (indenture, collateral, credit enhancement, covenants, market of issue, tax status) that determines what those cash flows are worth when things go wrong; and (3) the **contingency provisions** (embedded call, put, conversion options) that can change the timing or nature of the cash flows. Every later valuation or risk tool (yields, duration, credit spreads, OAS) presupposes that you have correctly read these three layers from the term sheet and indenture.

## Learning Outcomes Covered
- Describe the basic features of a fixed-income security.
- Describe the content of a bond indenture.
- Compare affirmative and negative covenants and identify examples of each.
- Describe how legal, regulatory and tax considerations affect issuance and trading.
- Describe how the cash flows of fixed-income securities are structured (principal repayment and coupon structures).
- Describe contingency provisions affecting timing/nature of cash flows and say whether each benefits the borrower or the lender.

## Frameworks Introduced
- **Three elements of a bond investment**: features → legal/regulatory/tax considerations → contingency provisions.
  - When to use: first pass on any new issue, term sheet or prospectus.
  - How: (1) map the scheduled cash-flow diagram from the features; (2) read the indenture for issuer legal entity, source of repayment, collateral, credit enhancement, covenants; (3) list every embedded option, who holds it, and when it is exercisable.
- **Indenture review checklist** (beyond the basic features): legal identity and form of the issuer; source of repayment proceeds; asset/collateral backing; credit enhancements; covenants.
  - Why it works: credit risk depends on *which legal entity* owes you and *what you can seize*, not on the brand name of the group.
  - Failure mode: buying a holding-company bond as if it were an operating-company bond. The holdco may have few assets of its own and is **structurally subordinated** to creditors of the operating subsidiaries.
- **Source-of-repayment map by issuer type**:
  | Issuer | Primary source of repayment |
  |---|---|
  | Supranational (World Bank, EIB) | Repayment of previous loans made by the organization, or paid-in capital of members (can call on members) |
  | Sovereign | "Full faith and credit": taxing power and ability to print money (local-currency sovereigns are the safest credit) |
  | Non-sovereign government | (1) general taxing authority, (2) cash flows of the financed project, (3) special taxes or fees dedicated to the debt |
  | Corporate | Operating cash flows of the issuer |
  | ABS (via SPE/SPV) | Cash flows of the underlying pool of financial assets (mortgages, auto loans, card receivables) |
- **Credit enhancement taxonomy**:
  | Internal (structural) | External (third party) |
  |---|---|
  | Subordination (credit tranching, waterfall; losses allocated bottom-up) | Bank guarantee (bank) and surety bond (rated, regulated insurer, e.g. monoline); capped at the **penal sum** |
  | Overcollateralization (collateral > principal; e.g. $110m collateral for $100m issue = $10m OC) | Letter of credit (credit line to cover shortfalls) |
  | Reserve accounts: cash reserve fund; excess spread account (asset cash flow − bond interest), can be "turboed" to retire senior principal | Cash collateral account (issuer borrows and *invests* the enhancement amount now, e.g. in CP) |
  - Rule: guarantees, surety bonds and LOCs are *promises* and carry third-party (counterparty) risk. A cash collateral account is an *actual deposit*, so a downgrade of its provider need not downgrade the bond.
- **Covenant classification (affirmative vs negative)**:
  - Affirmative (positive) = what the issuer **must do**. Administrative, low cost, little constraint: use of proceeds, make contractual payments, comply with laws, maintain business lines, insure and maintain assets, pay taxes when due.
  - Negative = what the issuer **must not do**. Costly, materially constrain decisions. They protect against claim dilution, asset withdrawal/substitution and suboptimal investment:
    - Restrictions on debt (max leverage/gearing ratio, min interest coverage)
    - Negative pledges (no new debt senior to existing bonds)
    - Restrictions on prior claims (unencumbered assets may not be pledged)
    - Restrictions on distributions (dividends/buybacks capped at a % of cumulative earnings since a base date)
    - Restrictions on asset disposals (cumulative cap as % of gross assets; prevents break-up)
    - Restrictions on investments (no speculative investments; stay in current business)
    - Restrictions on M&A (only if company survives or acquirer assumes the indenture via a supplemental indenture)
  - Failure mode: over-tight covenants can *force* an avoidable default (e.g. block the asset sale or the takeover by a stronger firm that would have repaid bondholders).
- **Who benefits from each contingency provision** (the core exam decision table):
  | Provision | Holder of option | Price vs straight bond | Yield vs straight bond | Main risk shifted to investor |
  |---|---|---|---|---|
  | Call (incl. sinking-fund call at lowest of market/par/SF price) | Issuer | Lower | Higher | Reinvestment risk, capped upside |
  | Make-whole call | Issuer (but costly) | Close to straight | Close to straight | Little: investor compensated at PV of remaining flows at gov't yield + spread |
  | Put | Investor | Higher | Lower | None added; limits price-decline risk |
  | Conversion option | Investor | Higher | Lower | Dilution for existing shareholders (issuer side) |
  | Call on a convertible | Issuer | Lower than non-callable convertible | Higher | Forced conversion |
  | CoCo (contingent write-down/conversion) | Automatic on trigger | Lower | Higher | Loss absorption on the downside |
  | Cap on FRN | Issuer | Lower | Higher | Coupon capped in rising-rate world |
  | Floor on FRN | Investor | Higher | Lower | — |
  | Step-up coupon | Investor protection vs rising rates; incentive for issuer to call | — | — | Call risk if rates fall/stable |

## Key Concepts
- **Tenor**: time remaining to maturity (≠ original maturity).
- **Money market vs capital market securities**: original maturity ≤ 1 year vs > 1 year. Perpetual bonds (UK consols) have no maturity.
- **Par value** (principal, face, nominal, redemption, maturity value): amount repaid at maturity. Prices are quoted as % of par (95 = 95% of par); below 100 = discount, above 100 = premium.
- **Coupon rate (nominal rate)**: annual interest ÷ par; periodic payment = coupon rate × par ÷ frequency.
- **Floating-rate note (FRN)**: coupon = reference rate (Libor/Euribor/Hibor/Sibor or successor) + quoted margin fixed at issue; reset in advance, paid in arrears; mostly quarterly.
- **Inverse floater**: coupon moves opposite to the reference rate; favoured by investors expecting falling rates.
- **Zero-coupon (pure discount) bond**: issued at a discount, redeemed at par; interest is implied (par − price).
- **Dual-currency bond**: coupons in one currency, principal in another. **Currency option bond**: investor chooses the currency of each payment (straight bond + FX option).
- **Current (running) yield**: annual coupon ÷ price. **Yield to maturity (redemption yield)**: IRR of the bond's cash flows to maturity; inversely related to price.
- **Trust deed / indenture**: legal contract describing the bond, issuer obligations and bondholder rights; held by a **trustee** (appointed by issuer, fiduciary to bondholders) who monitors compliance, invoices the issuer, holds funds, and acts on default. The **principal paying agent** handles the mechanics of payments.
- **SPE / SPV / SPC**: thinly capitalized, bankruptcy-remote special legal entity used in securitization; the sponsor/originator's transfer of assets is a **true sale**.
- **Secured vs unsecured; senior vs subordinated (junior)**: ranking in bankruptcy. **Debenture**: unsecured in the US and many jurisdictions but usually *secured* in the UK and Commonwealth (e.g. India), so read the indenture.
- **Collateral trust bond** (secured by securities), **equipment trust certificate** (secured by physical equipment like aircraft, often for leasing tax benefits), **MBS** (mortgage pool), **covered bond** (dual recourse: issuer + on-balance-sheet cover pool, non-performing assets must be replaced).
- **Domestic / foreign / Eurobond / global bond**: see table below. Foreign-bond nicknames include Yankee (US), Samurai (Japan), Bulldog (UK), Panda (China), Maple (Canada), Kangaroo (Australia), Kimchi (Korea), Matador (Spain), Matryoshka (Russia).
- **Bearer vs registered bond**: owner unknown to trustee (only clearing system knows) vs ownership recorded by name/serial number. Eurobonds were historically bearer; today most bonds are registered.
- **Original issue discount (OID)**: par − original issue price; in OID-tax jurisdictions (e.g. US) a prorated part is taxed as interest each year and added to the cost basis.
- **Embedded option**: contingency provision in the indenture, not separable or tradable (vs a **warrant**, which is an *attached*, separately tradable option and a "sweetener").
- **Conversion ratio / price / value / premium / parity**: see formulas.
- **CoCo (contingent convertible)**: converts or is written down *automatically* on the *downside* (e.g. core Tier 1 ratio below the regulatory minimum), recapitalizing a bank and reducing systemic risk.

## Formulas & Reference Tables
- Periodic coupon: `C_period = (c × Par)/m`, with c the annual coupon rate and m payments per year.
- FRN coupon for period (t, t+1]: `c_t+1 = MRR_t + QM`, with MRR the reference rate observed at the start of the period (reset in advance) and QM the quoted margin.
- Current yield: `CY = Annual coupon / Price`.
- Level-payment (fully amortized) bond payment: `A = Par × r/[1 − (1 + r)⁻ᴺ]`.
- Partially amortized with balloon B: `A = [Par − B/(1 + r)ᴺ] × r/[1 − (1 + r)⁻ᴺ]`; final payment = A + B.
- Amortization split each period: `Interest_t = r × Balance_t−1`; `Principal_t = A − Interest_t`; `Balance_t = Balance_t−1 − Principal_t`.
- Sinking fund (x% of outstanding each year from year k): `Balance after n SF years = Par × (1 − x)ⁿ`; balloon = remaining balance at maturity.
- Capital-indexed linker: `Adjusted principal_t = Par × (Index_t/Index_0)`; `Coupon_t = (c × Adjusted principal_t)/m`.
- Interest-indexed: principal fixed; `Coupon_t = Coupon_0 × (Index_t/Index_0)`.
- Zero-coupon-indexed: `Principal at maturity = Par × (Index_T/Index_0)`, no coupons.
- Indexed-annuity: level annuity payment scaled by `Index_t/Index_0` (fully amortizing).
- Real rate (approx.): `real ≈ nominal − inflation`.
- Call premium: `Call price − Par`.
- Conversion ratio: `CR = Par / Conversion price`.
- Conversion value (parity value): `CV = Share price × CR`.
- Conversion premium: `Convertible price − CV` (positive premium = below parity: converting now would be worth less than selling the bond).
- Parity share price: `S* = Convertible price / CR` (share price at which CV = bond price).

**Market-of-issue classification**
| Type | Issuer | Currency | Market / regulator | Notes |
|---|---|---|---|---|
| Domestic | Incorporated locally | Local | National market | e.g. UK gilts issued by the DMO on behalf of HM Treasury |
| Foreign | Incorporated abroad | Local currency of market | National market, local regulator | Yankee, Samurai, Bulldog… |
| Eurobond | Any | Any (named by currency: Eurodollar, Euroyen; "euro-denominated Eurobond") | Outside any single jurisdiction; international syndicate | Less regulated, usually unsecured, often annual coupons; USD Eurobonds not SEC-registered so not sellable to US investors at issue |
| Global | Any | Any | Eurobond market **and** ≥1 domestic market simultaneously | Large issues, e.g. World Bank |

Rule: currency of denomination matters more for price than place of issue, because the relevant market interest rates are those of the currency.

**Inflation-linked structures**
| Structure | Coupon | Principal | Amortizing? | Examples |
|---|---|---|---|---|
| Zero-coupon-indexed | None | Indexed | No | Sweden |
| Interest-indexed | Indexed | Fixed nominal | No | Insurers, banks (not governments) |
| Capital-indexed | Fixed rate × indexed principal | Indexed | No | TIPS, UK/Aus/Can/NZ govts |
| Indexed-annuity | Level annuity, indexed | Included in annuity | Yes | Australian local govts |

**Callable exercise styles**: American (continuously callable from the first call date), European (one call date only), Bermudan (specified dates after the protection period, usually coupon dates). Putables are European (one-time put) or Bermudan (multiple put, more valuable); American-style puts are not observed in practice.

## Mental Models
- **Every embedded option has an owner, and the owner never gives it away for free.** If the issuer owns it (call, cap), the investor is paid through a lower price/higher yield. If the investor owns it (put, floor, conversion), the investor pays through a higher price/lower yield.
- **Think of credit enhancement as layers of loss absorption stacked below you.** Internal layers are part of the structure and do not depend on anyone's rating; external layers are only as good as the guarantor (monoline downgrades in 2007–09 proved it).
- **Negative covenants are the bondholder's option to stop value transfer to shareholders.** Read them as limits on leverage, priority, payouts and asset stripping. The tighter they are, the lower the spread should be, up to the point where they risk forcing a technical default.
- **FRN = low rate risk, full credit risk.** Price stays near par between resets unless the issuer's credit spread moves away from the fixed quoted margin.
- **Use the cash-flow diagram as the first sanity check.** Bullet: flat coupons plus a spike at maturity. Fully amortized: level payments. Partially amortized: level payments plus a balloon. Sinking fund: principal falls in steps.

## Worked Example
**Payment structures for a $1,000, 5-year, 6% annual bond priced at par (market rate 6%).**
- Bullet: $60 per year, $1,060 in year 5.
- Fully amortized: `A = 1,000 × 0.06/(1 − 1.06⁻⁵) = $237.40`.
  | Year | Interest | Principal | Balance |
  |---|---|---|---|
  | 1 | 60.00 | 177.40 | 822.60 |
  | 2 | 49.36 | 188.04 | 634.56 |
  | 3 | 38.07 | 199.32 | 435.24 |
  | 4 | 26.11 | 211.28 | 223.96 |
  | 5 | 13.44 | 223.96 | 0.00 |
- Partially amortized with a $200 balloon: `A = (1,000 − 200/1.06⁵) × 0.06/(1 − 1.06⁻⁵) = $201.92`; year-5 cash flow = 201.92 + 200 = **$401.92**.
- Interpretation: interest payments of the partially amortized bond are ≥ those of the fully amortized bond (equal only in year 1), because less principal is retired each year.

**Sinking fund.** £200m issue, 20 years, 5% of the *outstanding* balance retired in years 10–19: year-10 payment £10m, year-11 £9.50m…; balloon at year 20 = `200 × 0.95¹⁰ = £119.75m`.

**Inflation-linked (Lemurian bond, par L1,000, 4% semiannual, CPI +5%).**
- Zero-coupon-indexed: principal becomes L1,050.
- Interest-indexed: coupon L20 → L21; principal stays L1,000.
- Capital-indexed: principal L1,050; coupon = 0.04 × 1,050/2 = L21.
- Indexed-annuity (40 semiannual payments at 2%): `1,000 × 0.02/(1 − 1.02⁻⁴⁰) = L36.56` → × 1.05 = **L38.38**.

**Convertible.** Par €1,000, conversion price €20 → CR = 50. With a CR of 30, share at €33 → CV = €990; bond at €1,020 → conversion premium €30; parity share price = 1,020/30 = **€34**. Above €34 the bond is above parity.

**Call premium.** A bond callable in 2033 at 102.322 has a call premium of $23.22 per $1,000 par; issued 2019, first callable 2029 → 10-year call protection; callable every 15 August → Bermudan.

## Anti-patterns
- **Reading "debenture" as unsecured everywhere**: in the UK/Commonwealth it is typically secured; read the indenture.
- **Treating a subsidiary or holdco bond as a parent/opco obligation**: absent an explicit parent guarantee, only the issuing entity's credit and assets count.
- **Assuming an external guarantee is risk-free**: it transfers you to the guarantor's credit (monoline and bank downgrades in 2007–09).
- **Relying on overcollateralization without questioning collateral valuation**: inflated housing valuations were a core failure of MBS in the crisis.
- **Calling a warrant an embedded option**: warrants are attached and separately tradable.
- **Assuming an issuer *must* call a step-up bond**: calling is optional; it may keep the bond if refinancing is harder (crisis, credit deterioration), though failing to call can hurt its market reputation.
- **Ignoring that credit-linked coupons can be pro-cyclical**: the coupon step-up after a downgrade raises the debt burden and can accelerate default.

## Exam Focus & Traps
- **FRN reset timing**: the coupon paid on date t+1 uses the reference rate observed at the *previous* reset date t (e.g. Libor on 31 March sets the 30 June payment).
- **Nominal (coupon) rate is annual**: a 10% semiannual bond has a 10% nominal rate, not 5%. Tenor = remaining life, not original maturity. Price ≠ redemption value.
- **Which party benefits**: cap → issuer; floor → investor; step-up → investor (protection vs rising rates); inverse floater → investor who expects falling rates; FRN → investor who expects rising rates.
- **Most/least third-party risk**: cash collateral account has the least; surety bonds, bank guarantees and LOCs have more.
- **Internal vs external enhancement**: overcollateralization is *internal* (collateral is not provided by a third party); a surety bond is *external*.
- **Covenant classification**: "maintain min interest coverage" and "max D/E" are *negative* (restrictions on debt) even though phrased as "maintain". "Insure and maintain assets", "pay taxes", "comply with laws", "use of proceeds" are *affirmative*. Negative covenants are costlier; both kinds are legally enforceable and set at issue.
- **Market classification**: South African company, GBP bond sold in UK → foreign (Bulldog). USD bond by a Japanese company, not SEC-registered, sold in the Middle East → Eurobond.
- **Bearer vs registered**: the text says Eurobonds *used to be* bearer and most bonds are now registered, yet the official practice-problem answer still says Eurobonds are "typically issued as bearer bonds". On the exam, answer "bearer" when asked relative to domestic/foreign bonds.
- **OID taxation**: prorated OID taxed yearly (Z200/10 = Z20 per year), cost basis rises, no capital gain at maturity. Premium bonds: some jurisdictions allow a prorated deduction ($1,005 for 5 years → $1 per year) or a capital loss at maturity.
- **Covered bond vs ABS**: covered bond has dual recourse and replacement of non-performing assets → lower credit risk and lower yield than similar ABS.
- **TIPS = capital-indexed** (fixed real coupon on CPI-adjusted principal, deflation floor on principal at maturity).
- **Convertible condition**: CV < bond price → below parity; CV > bond price → above parity. Price floor of a convertible = straight-bond value.
- **Early conversion is rare**: coupons usually exceed dividends, which is why issuers add calls to force conversion.
- **Sinking-fund call**: issuer can usually buy back at the *lowest* of market, par or sinking-fund price; investor faces reinvestment risk and a possible loss when a premium bond is retired at par. A doubling option lets the issuer retire twice the required amount.

## Key Takeaways
1. Before pricing a bond, extract its features, its legal/tax wrapper, and every embedded option with its owner.
2. Credit risk depends on the legal issuer, source of repayment, seniority, collateral and credit enhancement, not on the group's name.
3. Internal enhancements (subordination, OC, reserve accounts) are structural. External ones (guarantees, surety, LOC) add counterparty risk, except a cash collateral account.
4. Affirmative covenants are administrative and cheap. Negative covenants are costly but protect against dilution, asset stripping and value transfer.
5. Principal can be repaid bullet, fully amortized, partially amortized with a balloon, or via a sinking fund. Every scheduled retirement reduces credit risk but adds reinvestment risk.
6. Coupon structures (FRN, capped/floored/collared, inverse floater, step-up, credit-linked, PIK, deferred, index-linked) exist to shift interest rate, credit, inflation or cash-flow timing risk between issuer and investor.
7. Issuer-owned options (calls, caps) lower price and raise yield; investor-owned options (puts, floors, conversion) raise price and lower yield.

## Connects To
- **ch02**: how these bonds are issued (primary market, underwriting, shelf) and traded, and the money-market and repo funding markets.
- **ch03**: pricing the cash flows defined here (YTM, flat/full price, FRN discount margin, money-market yields).
- **ch04**: securitization mechanics, SPVs, tranching and prepayment risk in ABS/MBS.
- **ch05**: duration and convexity of the structures introduced here (effective duration for callables).
- **ch06**: seniority ranking, recovery rates and covenant analysis in credit.
- **ch09**: valuation of callable, putable and convertible bonds (option-adjusted framework).
- **`tuckman-fixed-income` ch19**: corporate bonds and CDS from the practitioner side; **ch20**: mortgages and MBS; **ch00**: overview of global fixed-income markets.
- **`cfa-level1-curriculum` ch14**: personal revision notes on the same reading.
