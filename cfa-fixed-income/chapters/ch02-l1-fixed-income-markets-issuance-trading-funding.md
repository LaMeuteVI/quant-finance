# Chapter 2: Fixed-Income Markets: Issuance, Trading, and Funding
> **Source**: CFA Program Curriculum 2020, Level I, Reading 43 · Fixed Income | Moorad Choudhry, PhD, FRM, FCSI, Steven V. Mann, PhD, and Lavone F. Whitmer, CFA

## Core Idea
Fixed-income markets are the plumbing of global capital allocation (about USD 247 trillion of debt at Q1 2018). To work in them you need four maps: **how markets are classified** (issuer, credit quality, maturity, currency, coupon type, geography), **how bonds get issued** (underwritten, best-efforts, shelf, auction, private placement), **how they trade** (mostly OTC, dealer-intermediated, liquidity measured by the bid–offer spread), and **how banks and dealers fund themselves** (deposits, central bank funds, interbank, CDs and, above all, repo). Every instrument's yield reflects its position on these maps: credit, liquidity, tax status, currency and funding cost.

## Learning Outcomes Covered
- Describe classifications of global fixed-income markets.
- Describe the use of interbank offered rates as reference rates in floating-rate debt.
- Describe mechanisms available for issuing bonds in primary markets.
- Describe secondary markets for bonds.
- Describe securities issued by sovereign governments.
- Describe securities issued by non-sovereign governments, quasi-government entities and supranational agencies.
- Describe types of debt issued by corporations.
- Describe structured financial instruments.
- Describe short-term funding alternatives available to banks.
- Describe repurchase agreements (repos) and the risks associated with them.

## Frameworks Introduced
- **Six classification criteria for fixed-income markets**: type of issuer (households, non-financial corporates, government, financial institutions; or, for bonds, government/government-related, corporate, structured finance), credit quality (investment grade ≥ Baa3/BBB−), original maturity (money market ≤ 1 year, capital market > 1 year), currency denomination, type of coupon (fixed vs floating), geography (domestic/foreign/Eurobond; developed vs emerging). Other lenses: inflation-linked and tax-exempt sectors.
  - When to use: to place any bond in a sector, pick a benchmark index, or explain yield differences.
  - Rule: currency drives which rates move the price (a USD bond by a British company moves with US rates).
- **Primary-market issuance mechanisms**:
  | Mechanism | Who bears placement risk | Typical users | Key features |
  |---|---|---|---|
  | Underwritten (firm commitment) | Underwriter/syndicate buys whole issue, resells | Corporates, US munis, some ABS/MBS | Revenue = spread between purchase and resale price; syndicated if large (lead underwriter) |
  | Best-efforts | Issuer (bank acts as broker for a commission) | Corporates | Less risk and less incentive for the bank |
  | Shelf registration | Issuer | Well-established, strong issuers (sometimes only to qualified institutional investors) | One master prospectus; each tranche needs only a short issue announcement confirming no material change |
  | Auction | Issuer; bidders compete | Sovereigns (US single-price; Canada, Germany multiple-price) | Price discovery and allocation |
  | Private placement | Negotiated | Smaller/new issuers, regular issuers wanting tailoring | Non-underwritten, unregistered; illiquid (US Rule 144A: tradable among qualified institutional buyers); customized, tighter covenants; bought by insurers and pension funds for extra yield |
- **Six phases of an underwritten offering**: (1) determine funding needs; (2) select underwriter/syndicate; (3) structure and announce (terms, prospectus/offering circular, trustee, press-release launch); (4) pricing (gauge demand through marketing, road shows, "anchor" investors, **grey market** = when-issued forward market; aim for small oversubscription); (5) issuing (offering day: underwriting agreement signed, syndicate buys whole issue and resells); (6) closing (~14 days later, bonds delivered; represented by a **global note** held by the paying agent).
  - Failure mode: price too high → undersubscribed, syndicate stuck with bonds. Price too low → large oversubscription, meaning the issuer left money on the table (could have paid a lower coupon).
- **US Treasury single-price (uniform, "Dutch") auction**: announcement → bidding (competitive bids state a yield; non-competitive bids accept the auction yield and are always filled) → issuance.
  - How allocation works: accept all non-competitive bids, then competitive bids in ascending yield order until the amount is filled. **Everyone receives the highest accepted yield (stop-out rate)**. Competitive bids above the stop-out yield get nothing.
  - Why it works: bidders can bid aggressively without "winner's curse" overpayment, which tends to lower the Treasury's funding cost. Multiple-price auctions give each winner their own bid price/yield.
- **Structured financial instrument taxonomy** (bond + ≥1 derivative; payoff linked by formula to an underlying, not to the issuer's cash flows):
  | Category | Example | Mechanics | Investor gets | Hidden risk |
  |---|---|---|---|---|
  | Capital protected | Guarantee certificate | Zero-coupon bond (principal floor) + call option bought with the remainder | Full (or partial) capital protection + upside; max loss = option premium | Protection only as good as the issuer's credit |
  | Yield enhancement | Credit-linked note (CLN) | Bond whose redemption falls by the reference asset's nominal if a credit event occurs; issuer = protection buyer, investor = protection seller | Higher coupon, usually bought at a discount | Credit event on the reference asset |
  | Participation | Floater; equity-index-linked notes (e.g. Italian 2005–2020 floater at 85% of 10y CMS) | Payoff tracks a fraction of an underlying | Indirect exposure (e.g. equity for investors barred from equities) | Usually no capital protection |
  | Leveraged | Inverse floater | `Coupon = C − L × R` | Magnified sensitivity to rates | Coupon falls L × 100bp per 100bp rise in R |
- **Repo rate drivers (what makes the repo rate lower)**: higher-quality collateral; shorter term (normal upward-sloping curve); delivery of collateral to the lender required; collateral in high demand (**special** collateral: cash lender accepts a below-market repo rate to get the security); lower rates on alternative money-market financing.
- **Repo margin (haircut) drivers (what makes the haircut higher)**: longer repo term; lower collateral quality; lower counterparty credit quality; collateral in ample supply or low demand (scarce/in-demand collateral → lower haircut). Haircuts are negotiated bilaterally.

## Key Concepts
- **Interbank offered rate (IBOR)**: set of rates (not a single rate) at which panel banks believe they could borrow *unsecured* from other banks, for maturities overnight to 1 year, per currency (Libor, Euribor, Tibor, Sibor, Hibor, Mibor, Koribor). Used for FRNs, loans, mortgages, swaps (~USD 350 trillion of contracts tied to Libor in 2018).
- **Libor phase-out**: trimmed-mean panel survey (top and bottom four submissions discarded); manipulation during 2007–09; administration moved from the BBA to ICE in 2014 (reduced to 5 currencies × 7 tenors; ⚠ Correction: ICE is Intercontinental Exchange, not "International Currency Exchange" as the source states); panel submissions no longer required after 2021. **SOFR** (secured overnight financing rate) is based on actual US repo transactions; first large SOFR FRN was Fannie Mae's USD 6bn in July 2018.
- **FRN reset convention**: rate set at the start of the period, paid at the end (in arrears); tenor of the reference rate matches the payment frequency (3M Libor for quarterly coupons).
- **Demand/supply of floating-rate debt**: banks funded short-term prefer floating-rate assets (asset-liability matching); investors expecting rising rates buy FRNs; consumer-finance firms and corporates wanting to avoid locking in fixed rates (or expecting falling rates) issue them.
- **Eurobond market**: outside the jurisdiction of the currency's country; less reporting, regulation and tax constraint; about 80% of issuers borrowing outside their home country use it.
- **Emerging-market bonds**: higher yields for weaker political stability, property rights and contract enforcement, but often lower debt/GDP and higher growth. Split into local-currency and hard-currency issues.
- **Fixed-income indexes**: Bloomberg Barclays Global Aggregate (US Agg + Pan-European Agg + Asian-Pacific Agg; IG fixed-rate), J.P. Morgan EMBI Global (USD Brady bonds, Eurobonds, loans of EM sovereigns and quasi-sovereigns), FTSE Global Bond Index Series.
- **Investors**: central banks (open market operations: buying bonds raises the monetary base; FX reserve management), institutions (pension funds, insurers, banks, hedge funds, endowments, sovereign wealth funds), retail (mostly indirect via mutual funds and ETFs because of informational barriers, large lot sizes and OTC trading).
- **Liquidity**: ability to trade quickly **at prices close to fair value**, on both the long and the short side. Proxy: bid–offer spread (≈5bp very liquid, e.g. World Bank; 10–12bp reasonable; >50bp illiquid; no quote = no liquidity).
- **Settlement**: government/quasi-government cash (T+0) or T+1; corporates T+2/T+3 (up to T+7 in some jurisdictions); Euroclear and Clearstream (linked by an electronic bridge), paperless book-entry.
- **Sovereign naming**: US T-bills (≤ 1y, discount), T-notes (>1 to 10y), T-bonds (>10y); JGBs, gilts, Bunds (annual coupons), OATs; Spain's letras (≤ 1y), bonos (1–5y), obligaciones (>5y). **On-the-run** = most recently issued, most liquid, used as the **benchmark issue**; older (off-the-run) issues trade less.
- **Sovereign credit**: usually unsecured, backed by taxing power; local-currency ratings typically above foreign-currency ratings (the state can tax and print its own currency, but earns foreign currency only through exports or markets). A strong domestic savings base lets the sovereign fund itself locally. Foreign-currency proceeds are usually swapped into local currency.
- **Non-sovereign bonds** (states, provinces, cities; US munis, UK local authority bonds, German Länder): repaid by general taxes, project revenues or dedicated fees; usually no national guarantee; trade at a higher yield than sovereigns (credit + liquidity).
- **Quasi-government (agency) bonds**: GSEs (Fannie Mae, Freddie Mac, FHLB), Hydro-Québec, JBIC (explicitly guaranteed by Japan); repaid from the entity's own cash flows; mostly only an *implicit* guarantee.
- **Supranational bonds** (World Bank/IBRD, IMF, EIB, ADB, AfDB): mostly plain vanilla, often used as benchmarks where no liquid sovereign exists.
- **Bilateral vs syndicated loans**: one lender vs a syndicate led by a lead bank; floating rate over Libor, a sovereign rate or the prime rate; syndicated loans increasingly securitized and traded. Europe/Japan ≈ 75–80% bank-funded; US ≈ 80% market-funded.
- **Commercial paper (CP)**: short-term unsecured promissory note for working capital, seasonal needs and **bridge financing**; typical maturity < 3 months; rolled over, so **rollover risk** is mitigated by **backup lines of credit** (usually 100%; subject to a material adverse change clause). Yields above T-bills (credit + liquidity) and, in the US, above tax-exempt munis.
- **CP ratings**: prime paper = P1/P2/P3 (Moody's), A1+/A1–A3 (S&P), F1+/F1–F3 (Fitch); below that is speculative.
- **Corporate maturity buckets (CFA convention)**: short ≤ 5y, intermediate >5–12y, long >12y; notes 1–12y, bonds >12y; century bonds (Disney 1993, Austria 2117).
- **Medium-term notes (MTNs)**: offered *continuously* by an agent of the issuer; any maturity (Disney's century bond came from an MTN programme); three segments: short-term fixed/floating, medium-to-long fixed, structured notes; tailored to buyers; cheaper registration/underwriting.
- **Serial vs term maturity**: serial = scheduled tranches mature each year (holders know which); term = bullet. A sinking fund on a term issue replicates serial retirement but bonds are chosen by lottery (random call at the sinking-fund price, usually par) or delivered after open-market purchase.
- **Bank funding**: retail deposits (demand/checking deposits pay little or no interest, savings accounts, money market accounts) and **wholesale funds** (central bank funds, interbank deposits, large-denomination negotiable CDs).
- **Central bank funds**: reserve surpluses lent to deficit banks; overnight or term (2 days–1 year); US **Fed funds effective rate** = volume-weighted average of broker-arranged trades.
- **Interbank deposits**: unsecured, need a credit line; dry up in stress (post-Lehman 2008).
- **CDs**: non-negotiable (early-withdrawal penalty) vs negotiable (tradable; large-denomination ≥ $1m in US = wholesale funding). Yield driven mainly by the bank's credit risk.
- **Repo / reverse repo**: sale of a security with agreement to repurchase at an agreed price and date = collateralized loan. Named from the **dealer's** perspective: dealer borrows cash = repo; dealer lends cash/borrows securities = reverse repo (used to cover shorts). Overnight, term, or repo-to-maturity. Coupons paid during the repo belong to the cash borrower (security seller). Interest paid at maturity of the repo.

## Formulas & Reference Tables
- FRN coupon: `Coupon rate_t+1 = Reference rate_t + Spread` (spread fixed at issue from issuer credit at issuance).
- Inverse floater: `Coupon = C − L × R` with C the coupon when R = 0, L the coupon leverage, R the reference rate at reset. `0 < L < 1` = deleveraged; `L > 1` = leveraged. Usually floored at 0.
  - ⚠ Correction (terminology): the source calls the Barclays 2010 note (7.50% − euro 3-month Libor from 2013, L = 1) a "leveraged inverse floater". Under its own definition (L > 1 is leveraged), L = 1 is the boundary case; treat it simply as an inverse floater with unit leverage.
- Money-market interest (discount basis, US CP/T-bill): `Interest = FV × r × (days/360)`; `Proceeds = FV − Interest`; holding-period return = `Interest/Proceeds`.
- Money-market interest (interest-bearing/add-on, ECP): `Proceeds = FV`; `Repayment = FV × (1 + r × days/360)`; return = `r × days/360`.
- T-bill price from a discount rate: `P = 100 × (1 − DR × days/360)`.
- Repo: `Loan = Collateral value × (1 − haircut)`; `Repo interest = Loan × Repo rate × (days/360)` (Act/365 in sterling); `Repurchase price = Loan + Repo interest`.

**USCP vs Eurocommercial paper (ECP)**
| Feature | USCP | ECP |
|---|---|---|
| Currency | USD | Any |
| Maturity | Overnight–270 days (>270 days needs SEC registration) | Overnight–364 days |
| Interest | Discount basis | Interest-bearing (add-on) or discount |
| Settlement | T+0 | T+2 |
| Negotiable | Yes | Yes |
| Size/liquidity | Larger, more liquid | Smaller tickets, less liquid, hard to place long tenors |

**Who can lose what in a repo**
| Defaulting party | Exposure of the other party | Protection |
|---|---|---|
| Cash borrower (dealer) fails to repurchase | Cash lender holds collateral worth less than the unpaid repurchase price if collateral price fell | Haircut (lender treated as the more vulnerable party) |
| Cash lender fails to return collateral | Dealer holds cash worth less than collateral if its price rose | Defaulting lender liable for the replacement cost above the repurchase price |

## Mental Models
- **Price a new issue like a market-maker, not like a seller.** A small oversubscription is optimal. A big one means the coupon was too generous for the issuer.
- **Liquidity is two-sided and price-conditional.** You can always trade fast at a bad price. A liquid bond is one you can trade fast *near fair value*, so read the bid–offer spread.
- **Repo is the funding engine of every liquid bond market.** Dealers hold inventory on repo, shorts are covered through reverse repo, and central banks run open market operations through it. When collateral goes "special", repo rates fall because the security itself is scarce, not because credit improved.
- **Think of CP as a daily credit vote.** Short maturity lets investors re-underwrite the issuer at every roll, which is why defaults are rare. It is also why rollover risk turns into a liquidity crisis when markets freeze, hence backup lines.
- **A structured note is a bond plus a derivative wrapped in the issuer's credit.** Decompose it (zero + call, bond + short CDS, floater × participation rate) before judging its value, and remember that "capital protection" is an unsecured promise.

## Worked Example
**1. Single-price T-bill auction (26-week, 23 July 2018).** Stop-out discount rate 2.140%; days = 182.
- Price = `100 × (1 − 0.0214 × 182/360) = 98.918111` → $9,891.81 per $10,000 par.
- Bids of $130.7bn for $45.0bn offered. All $0.79bn non-competitive bids filled; ~$43.2bn of $128.9bn competitive bids filled. The median competitive bid was 2.110%, yet every winner receives 2.140%.
- Interpretation: a bidder at 2.15% gets nothing; a bidder at 2.05% gets bonds at 2.140%.

**2. Discount vs interest-bearing CP.** $50m, 180 days, 5%.
- Interest = `50,000,000 × 0.05 × 180/360 = $1,250,000` in both cases.
- USCP (discount): proceeds $48,750,000, repay $50m → return `1.25/48.75 = 2.564%` for 180 days.
- ECP (add-on): proceeds $50m, repay $51.25m → return `2.50%`.
- Interpretation: same quoted rate, but the discount basis yields more to the investor because interest is earned on a smaller amount invested.

**3. Term repo (constructed example).** A dealer finances $50m market value of Treasuries for 30 days at a 2.00% repo rate with a 2% haircut (Act/360).
- Loan = `50,000,000 × 0.98 = $49,000,000`.
- Repo interest = `49,000,000 × 0.02 × 30/360 = $81,666.67`.
- Repurchase price = **$49,081,666.67**. Any coupon paid during the 30 days goes to the dealer.
- Interpretation: the $1m haircut is the cash lender's cushion against a fall in collateral value if the dealer defaults.

**4. Inverse floater reset.** Coupon = 7.50% − 3M rate (L = 1, floored at 0). With the reference at −0.32%, coupon = **7.82%**. A 5% − 0.5 × Libor note is a *deleveraged* inverse floater (coupon falls 50bp per 100bp rise in Libor).

## Anti-patterns
- **Treating an IBOR as one rate or as a secured rate**: it is a term structure of *unsecured* interbank rates up to 1 year. SOFR, by contrast, is secured and overnight, built from repo trades.
- **Assuming "capital protected" means riskless**: the zero-coupon leg is the issuer's unsecured debt. If the issuer fails, the protection disappears.
- **Relying on interbank or CP funding without a backup**: both markets dry up in systemic stress (2008). Backup lines carry MAC clauses that can be pulled exactly when needed.
- **Ignoring the haircut and counterparty in "safe" repo**: repo carries two-way credit risk even against AAA sovereign collateral.
- **Comparing CP and ECP yields without adjusting for discount vs add-on basis.**
- **Buying private placements for yield without pricing the illiquidity**: often no secondary market (or only 144A among QIBs).

## Exam Focus & Traps
- **Underwritten vs best-efforts**: underwriter *buys and resells* (bears risk, earns the spread); best-efforts bank is a *broker* (commission, less risk, less incentive).
- **Single-price auction**: competitive bid *above* the stop-out yield → nothing. Non-competitive bids are always filled. All winners get the *highest accepted* yield.
- **Grey market** = when-issued forward market for bonds about to be issued (not an unregulated market).
- **Shelf registration** = one master prospectus, short issue announcements; only for well-established issuers.
- **Settlement**: governments T+0/T+1, corporates T+2/T+3 (up to T+7), USCP T+0, ECP T+2.
- **Wholesale funds** = central bank funds, interbank funds, (large, negotiable) CDs. Retail deposits and, per the official answer key, **repos are not counted as "wholesale funds"** even though they are a major bank funding source.
- **Negotiable CD** can be sold before maturity; the **non-negotiable** CD carries the early-withdrawal penalty; large denominations (≥ $1m in the US) are the wholesale product.
- **Repo naming**: from the dealer's view, repo = collateralized *borrowing*, reverse repo = collateralized *lending* (and a way to borrow securities).
- **Haircut direction**: longer term, weaker collateral, weaker counterparty → *higher* haircut; scarce or in-demand collateral → *lower* haircut. **Repo rate direction**: special collateral → *lower* repo rate.
- **Sovereign ratings**: local-currency > foreign-currency; strong domestic savings base helps. Sovereigns are *unsecured*.
- **Lowest interest rate risk among sovereigns**: floaters.
- **Non-sovereign vs sovereign**: higher yield (credit + liquidity). **Agency bonds**: repaid first from the agency's own cash flows; mostly implicit guarantee (JBIC explicit).
- **Sinking fund ≈ serial maturity** for the issuer (both retire principal on schedule; sinking-fund bonds are chosen by lottery). Both reduce **credit** risk, not interest rate or inflation risk.
- **CP**: issued across the credit spectrum (only top names get low-cost CP); has a thin but existing secondary market; used for bridge financing.
- **Trap on market size**: the official practice-problem answer says the non-financial corporate sector has the *smallest* bonds outstanding in most countries, whereas Exhibit 1 (all debt, incl. loans) shows non-financial corporates as the *largest* global sector (29.7%). The difference is bonds vs total debt: corporates borrow heavily through loans.
- **CLN**: if no credit event, the investor gets all promised flows (coupons + par). The investor is the *protection seller*.

## Key Takeaways
1. Classify every bond on six axes (issuer, rating, original maturity, currency, coupon type, geography); currency determines which yield curve prices it.
2. IBORs are unsecured term interbank rates being replaced by transaction-based risk-free rates (SOFR in the US). FRNs reset in advance and pay in arrears.
3. Corporates mostly issue through underwritten syndicates or shelf programmes, sovereigns through auctions (US single-price), and smaller or tailored deals through private placements and MTNs.
4. Bonds trade mainly OTC through dealers. Liquidity = speed *at fair value*, measured by the bid–offer spread.
5. Sovereign > quasi-government ≈ supranational > non-sovereign in credit and liquidity for the same currency, and yields order accordingly.
6. Corporates fund short with loans and CP (rollover risk mitigated by backup lines) and long with notes/bonds structured through maturity type, coupon type, collateral and embedded options.
7. Structured notes repackage risk: capital protected, yield enhancement (CLN), participation, leveraged (inverse floater). Always decompose them into a bond plus a derivative.
8. Banks fund with deposits, central bank funds, interbank deposits, CDs and repo. In a repo, the haircut protects the cash lender and the repo rate falls for high-quality or special collateral.

## Connects To
- **ch01**: bond features, FRNs, covenants, sinking funds and embedded options referenced throughout.
- **ch03**: money-market yield conventions (discount vs add-on, 360 vs 365), FRN discount margins, flat vs full prices.
- **ch04**: securitization, ABS/MBS and CDOs (structured finance sector).
- **ch06**: credit analysis of corporate, sovereign and CP issuers; seniority rankings.
- **ch11**: CDS and credit-linked instruments (CLN = funded credit protection).
- **`tuckman-fixed-income` ch12**: repo, special collateral and financing in depth; **ch15**: short-term rates, SOFR and IBOR transition; **ch00**: overview of global fixed-income markets.
- **`cfa-portfolio-management` ch02**: construction of fixed-income indexes.
- **`cfa-level1-curriculum` ch15**: personal revision notes on the same reading.
