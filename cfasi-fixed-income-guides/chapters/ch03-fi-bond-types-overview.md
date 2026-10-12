# Chapter 3: Overview of the Types of Fixed Income Securities
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 3 (Una panoramica sulle diverse tipologie di titoli a reddito fisso) | Giancarlo Pavia, CFA

## Core Idea
The bond universe is best organized by issuer type, because the issuer determines the dominant risk, the seniority, the investor base and the liquidity. Sovereigns and supranationals carry mostly rate risk; corporates carry credit risk; high yield adds default and covenant negotiation; hybrids and bank capital instruments trade structural complexity (subordination, deferral, extension, write-down) for extra spread. Secured structures (ABS, covered bonds) rely on asset pools. Learn the capital stack of a bank and the hybrid trigger mechanics before buying any subordinated paper.

## Frameworks Introduced
- **Issuer-type classification**
  | Segment | Dominant risk | Notes |
  |---|---|---|
  | Government, agencies, supranationals (e.g. EIB) | Rate, inflation, FX; credit only for weak sovereigns | Maturities from 1 month to 100 years; small minimums (about EUR 1,000); used as "risk-free" reference |
  | Inflation-linked sovereign (TIPS, UK linkers, OATei, BTPei) | Real-rate risk | Fixed real coupon, indexed principal; deflation floor at 100 only for primary buyers of some issues |
  | Emerging market sovereign | Macro, credit, FX | Higher yield, diversification (see ch11) |
  | Investment grade corporate | Credit spread | Benchmark size at least EUR 500m; senior unsecured bullet, 3/5-15/20 years; minimum about EUR 100,000 (qualified investors) |
  | Mid-cap and private placement | Credit, liquidity | EUR 50-350m; unrated; covenants negotiated; held to maturity by insurers |
  | High yield (BB+ to CC) | Default, price volatility | Restrictive covenants; distressed specialists take over near default |
  | Hybrid corporate | Subordination, deferral, extension | Yield premium to senior of issuer; rated 2-3 notches below senior |
  | Financials (banks, insurers) | Structure-dependent | Senior, subordinated, secured (ABS, covered) |
  | Green / Social | Same as issuer's credit | Use of proceeds certified by a second opinion provider |
- **Rating-change impact rule**: for a given rating move, the price change is larger when the move crosses IG to HY, and at equal rating, lower-rated bonds are more price volatile (BBB more than AA).
- **Fallen angel logic**: an IG issuer cut to BB pays mostly in spread concessions, not new covenants, since the market expects a return to IG.
- **HY protection toolkit (negotiated)**: early redemption options, change-of-control put, make-whole call, dividend limits, asset-sale and M&A limits, debt limits tied to financial ratios, pledges on shares or assets.
- **Hybrid deferral taxonomy**: optional (management discretion), mandatory (automatic trigger on financial ratios), cumulative (deferred coupons accrue and must be paid), non-cumulative (lost), cash-cumulative (paid in cash later).
- **Hybrid replacement language**: Intentional Replacement Language (issuer states intent to refinance with equity-credit securities) versus Replacement Capital Covenant (binding commitment).
- **Bank capital stack (loss absorption order)**: shareholders (CET1) first, then AT1, then Tier 2, then senior non-preferred, then senior preferred / other unsecured via bail-in. Excluded from bail-in: deposits up to EUR 100,000, covered bonds, employee claims.
- **Covered bond vs ABS**: both are asset-backed, but the covered bond has dual recourse (cover pool plus the originating bank's credit) and the pool is credit enhancement, not the investment; ABS investors take the pool's credit risk, in tranches (senior, mezzanine, junior/equity).

## Key Concepts
- **Fallen angel** — issuer downgraded from IG to HY (here, to BB).
- **Mini-bond** — small (under EUR 50m), unrated bond of Italian SMEs, bullet or amortizing, often unlisted on regulated markets, bought by private debt funds.
- **Private placement / club deal** — issue subscribed by one or a few investors with tailored covenants and lower liquidity.
- **Hybrid bond** — perpetual or very long, subordinated, with call schedule and step-up (typically 25-75 bp) if not called; issuers gain partial "equity credit" from rating agencies.
- **Equity credit** — share of a hybrid that rating agencies treat as equity, relieving the issuer's ratios.
- **AT1 (Additional Tier 1)** — perpetual, discretionary non-cumulative coupons, loss absorbing on a going concern; coupon cancellable when the Maximum Distributable Amount (CRD IV) limit is hit.
- **CoCo (contingent convertible)** — AT1 that converts or writes down when capital versus risk-weighted assets falls below a trigger.
- **Tier 2** — dated subordinated debt (minimum 5 years), absorbs losses on a gone-concern basis (at the point of non-viability); regulatory credit amortizes over the last 5 years, hence the 10-year bond callable in year 5.
- **First call date** — AT1/Tier 2 call at par needs supervisor approval, replacement with equal or better capital, and proof of ample capital post-call; if not called, coupon resets to reference rate plus pre-set spread.
- **Bail-in / BRRD** — Bank Recovery and Resolution Directive framework by which unsecured creditors absorb bank losses.
- **TLAC** — Total Loss Absorbing Capacity; from 2022 equal to 18% of RWA.
- **Senior non-preferred** — Italian "second-level" senior debt (introduced December 2017): senior to AT1/Tier 2 but junior to senior preferred; counts towards TLAC.
- **Covered bond (OBG in Italy)** — bank bond secured by a segregated, bankruptcy-remote cover pool (e.g. loan-to-value at most 80%), top ratings, used to take rate risk rather than credit risk.
- **Green / Social bond** — ordinary bond whose proceeds fund certified environmental or social projects (Climate Bond Initiative criteria).
- **Basel I / II / III** — capital accords: minimum capital; three pillars with rating-based risk weights; higher-quality capital, leverage and liquidity (LCR) limits, with Basel 4 planned for 2022.

## Formulas & Reference Tables
- Hybrid pricing logic: `Yield(hybrid) ≈ Yield(senior of same issuer) + premium for subordination, deferral and extension`; premium varies with risk appetite.
- Tier 2 regulatory credit: straight-line amortization over the last 5 years to maturity (`1/5` per year).
- TLAC floor: `TLAC ≥ 18% × RWA` (from 2022).
- 2017 issuance quoted in the guide: about EUR 2.25 trillion of bonds, about EUR 1.2 trillion in EUR, about EUR 370 billion by corporates; green/social about USD 125bn (2016: about USD 80bn). Treat these as dated data points.

## Mental Models
- Use "issuer type first" to decide which risk to analyse: rates for sovereigns, spread and covenants for corporates, structure for banks.
- Use "who is the natural holder" to anticipate liquidity: insurers hold private placements to maturity, so secondary liquidity is thin.
- Use the capital-stack ladder to read a bank bond: the lower the rung, the more the investor behaves like an equity holder with a capped upside.
- Use covered bonds as a government-bond substitute when you want spread over Bunds without taking bank credit risk.
- Use the 10NC5 Tier 2 pattern as a prior: the market treats the first call as the effective maturity.

## Worked Example
Tier 2 callable: bank issues a 10-year Tier 2, callable at par in year 5, 5-year mid-swap reference 1.0% at issue with spread 3.5%, so coupon 4.5% for years 1-5.
1. At year 5, if not called, the coupon resets to the then 5-year mid-swap rate plus 3.5%. If mid-swap is 2.0%, new coupon 5.5%.
2. If mid-swap fell to 0.2%, new coupon would be 3.7%, below the original: the issuer is unlikely to call only if replacement debt costs more than 3.7% plus its call costs; the investor faces extension risk to year 10.
3. Regulatory amortization: in years 6-10 the bond's capital credit declines by 20% a year, so the issuer's incentive to call at year 5 is strong.
Interpretation: value the bond to the first call date, then stress the extension case at the reset spread.

## Anti-patterns
- Treating a rated Tier 2 or AT1 like a senior bank bond because the issuer rating is high; the instrument rating is 2-3 notches lower and coupons can be cancelled (AT1).
- Assuming inflation-linked bonds always protect from deflation; check the issue-specific floor.
- Buying "frequent issuer" benchmark paper as if mid-cap private placements had the same liquidity.
- Assuming a covered bond is a credit-risk-on-the-pool investment; it is a dual-recourse structure.
- Overlooking that the green label does not change the issuer's credit risk.

## Practitioner Notes
- In HY, covenant negotiation is a core part of selection; in IG, it is mostly the spread over the issuer's senior curve.
- AT1 call extension was the 2010s market convention, but treat it as a custom, not a contract.
- Bail-in hierarchy matters when judging the cushion in front of your tranche; senior non-preferred was created to lift this cushion for senior preferred holders.

## Key Takeaways
1. Classify by issuer: government and agencies, corporate IG, HY, financials, secured.
2. Sovereigns are not risk-free outside reference markets; 2011 Italy and 100-year issues are reminders.
3. IG to HY downgrade is a discontinuity in price and in the eligible investor base.
4. Hybrids pay for subordination, deferral and extension; check cumulative versus non-cumulative.
5. Bank loss absorption order: CET1, AT1, Tier 2, senior non-preferred, senior preferred.
6. Covered bonds have dual recourse and bankruptcy-remote pools; ABS tranche the pool risk.
7. Tier 2 and AT1 calls need regulatory approval and capital replacement.

## Connects To
- **ch01**: the contract features behind these instruments (call, subordination, CoCo).
- **ch02**: risks (credit, downgrade, call) specific to these issuer types.
- **ch05**: spreads and curves used to price corporate and sovereign bonds.
- **ch11**: emerging market sovereign and corporate bonds.
- **`cfa-fixed-income` ch07**: credit analysis, covered bonds and securitization in the CFA curriculum.
