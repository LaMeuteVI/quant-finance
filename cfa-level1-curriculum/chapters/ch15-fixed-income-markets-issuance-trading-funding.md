# Chapter 15: Fixed-Income Markets — Issuance, Trading and Funding (Fixed Income)

## Core Idea
Bond markets are segmented by issuer, credit quality, maturity, currency, coupon type and geography. They are dominated by institutions and trade mostly OTC. Bonds are issued by public offering (underwritten, best-efforts, auction, shelf registration) or by private placement. Governments, agencies, supranationals, corporates and structured products each have distinct features. Banks fund themselves with deposits plus short-term wholesale funding (reserves, interbank loans, CDs, repo).

## Frameworks Introduced
- **Market classification**:
  - Issuer: households, non-financial corporates, financials, governments.
  - Credit: investment grade vs high yield. Regulated investors are limited to investment grade, which makes IG more liquid.
  - Maturity: money market vs capital market.
  - Currency: local vs foreign.
  - Coupon: fixed vs floating. Banks prefer floating to match their liabilities.
  - Geography: domestic, foreign, Eurobond; developed vs emerging.
- **Reference rates**: Libor (legacy; panel-based, unsecured interbank) → replaced by overnight risk-free rates (SOFR, €STR, SONIA). FRN coupon = reference rate + margin.
- **Investors**: central banks (open-market operations, FX reserves), institutions (pension funds, insurers, banks, SWFs), retail (mostly via funds and ETFs).
- **Primary market**:
  - **Underwritten offering**, in six steps:
    1. Determine funding needs.
    2. Select the underwriter or syndicate.
    3. Structure the deal and appoint a trustee.
    4. Announce, with the prospectus.
    5. Pricing day.
    6. Closing day (≈ T+14).
    - A **grey market** (forward trading) exists before issuance.
  - **Best-efforts**: the bank acts as agent only.
  - **Auctions** (sovereigns):
    - Single-price (US Treasury) or multiple-price.
    - **Competitive** bids state a yield. **Non-competitive** bids accept the result and are always filled.
    - Competitive bids are filled from the lowest yield up until the amount is covered.
  - **Shelf registration**: one disclosure document, multiple tranches over time. Reserved for well-established issuers.
  - **Private placement**: unregistered, sold to a few qualified investors, often with customized covenants. Little secondary trading.
- **Secondary market**: mostly **OTC dealer** markets with quotes and bid–ask spreads; some exchanges.
  - Settlement: T+1 for governments (sometimes T+0), T+2/T+3 for corporates.
- **Sovereign bonds**:
  - Names: Treasuries, gilts, Bunds, OATs, JGBs.
  - T-bills ≤ 1y, T-notes 1–10y, T-bonds > 10y.
  - The **on-the-run** issue (the latest for a maturity) is the benchmark and the most liquid.
  - Credit: unsecured, backed by taxing power. Local-currency debt is safer than foreign-currency debt, because the sovereign can print its own currency.
- **Non-sovereign** (states, cities): general obligation vs revenue bonds.
- **Quasi-government / agencies**: no explicit sovereign guarantee.
- **Supranational**: World Bank/IBRD, IMF, EIB.
- **Corporate debt**:
  - **Bilateral** and **syndicated loans**: mostly floating rate. Europe relies more on banks; the US more on capital markets.
  - **Commercial paper (CP)**:
    - Unsecured, ≤ 1y (US CP ≤ 270 days).
    - Funds working capital and provides **bridge financing**.
    - Usually rolled over, so there is **rollover risk**. Backup credit lines are required.
    - **USCP** is issued at a discount. **ECP** may be discount- or yield-based.
  - **Notes and bonds**: **serial** maturity (staggered) vs **term** maturity (bullet); sinking funds.
- **Structured instruments**:
  - **Capital protected**: zero-coupon + call, e.g., a guarantee certificate.
  - **Yield enhancement**: credit-linked notes (CLNs).
  - **Participation**: e.g., floaters, index participation.
  - **Leveraged**: inverse floaters.
- **Bank funding**:
  - **Retail deposits**: demand (checking), savings, money market accounts.
  - **Wholesale**:
    - central bank reserves (Fed funds market),
    - interbank deposits,
    - **CDs** (non-negotiable, with a withdrawal penalty, vs negotiable, which can be sold),
    - **repo**.
- **Repo mechanics**:
  - Sell a security today and agree to buy it back later at a higher price.
  - Economically, a **collateralized loan**. The **repo rate** is the implied interest.
  - The cash borrower does a repo; the **cash lender** does a **reverse repo**.
  - Overnight vs term repo.
  - **Haircut (repo margin)** = collateral value − loan amount.
  - The repo rate is **lower** for high-quality, liquid collateral, shorter terms, and collateral in high demand ("special" vs general collateral). It is also higher when alternative money-market rates are higher.

## Key Concepts
- **On-the-run vs off-the-run**.
- **Grey market**: forward trading of bonds before their issue.
- **Backup lines of credit** for CP.

## Mental Models
- **Liquidity follows regulation and benchmarks**: IG, on-the-run and sovereign bonds are the most liquid.
- **Repo is secured lending**: price it by collateral quality, term and scarcity.
- **CP is cheap until the rollover fails** (2008). Always check the backup lines.

## Anti-patterns
- ⚠ **Correction vs the notes**: in a repo, the party that **lends cash** (buys the security) does the *reverse* repo. The notes say "borrows the cash".
- **Relying on short-term wholesale funding for long-term assets** (bank runs, Northern Rock).
- **Assuming quasi-government bonds carry an explicit government guarantee**.

## Worked Example
**Repo cost.** A dealer repos $10m of Treasuries overnight at a 2% repo rate (360-day basis) with a 2% haircut.
- Cash received = 10m × (1 − 0.02) = **$9.8m**.
- Interest = 9.8m × 0.02 × 1/360 = **$544.44**.
- The repurchase price is $9,800,544.44.

**T-bill auction (from the notes).** The high rate at auction was 2.140% (median 2.110%). Bidders paid 98.9181% of par. Bids totaled $130bn for $45bn issued, a **bid-to-cover ratio of ≈ 2.9**.

## Key Takeaways
1. Markets are segmented by issuer, credit, maturity, currency, coupon and geography, and are mostly OTC.
2. Issuance: underwritten, best-efforts, auction (competitive vs non-competitive), shelf, private placement.
3. Sovereign: on-the-run benchmark. Local-currency sovereign debt is safer than foreign-currency.
4. CP funds working capital and carries rollover risk. Loans are floating. Serial vs term maturities.
5. Bank funding = deposits + reserves, interbank, CDs, repo (collateralized, with a haircut).

## Connects To
- **Ch 14**: bond features.
- **Ch 16**: pricing, money-market yields.
- **Ch 5**: open-market operations and the policy rate.
- **Ch 8**: primary and secondary market mechanics.
