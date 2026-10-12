# Chapter 0: An Overview of Global Fixed Income Markets
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Overview + Part One introduction | Data as of 2009–2010 (BIS, Fed Flow of Funds, ECB, BoJ)

## Core Idea
Fixed income markets are balance sheets talking to each other. Households save (directly or via pension funds, insurers, deposits), and governments, businesses and home buyers borrow, with banks, broker-dealers, securitization vehicles and central banks in between. To read today's prices you need to know **who holds what, how they are funded and which constraints they face**. Long-dated demand from pensions and insurers, bank funding fragility and central bank balance sheets move curves as much as macro expectations do. The chapter also sets the book's key convention: **swaps, not government bonds, are the benchmark curve** against which almost everything is priced.

## Frameworks Introduced
- **Three bank risks (credit, interest rate, financing)**: banks earn spreads only by taking risk.
  - *Credit risk*: borrowers may not repay (the book covers it in ch19).
  - *Interest rate risk*: funding short at low rates and lending long at fixed rates. When short funding costs rise relative to fixed lending rates, the spread narrows or turns negative (the subject of Part Two, ch04–ch06).
  - *Financing risk*: deposits (insured) and long-term bonds are stable funding. Fed funds, repo and commercial paper can vanish in days, and assets cannot be liquidated as fast, which forces fire sales. That is a **run**.
  - When to use: any time you assess an intermediary (bank, broker-dealer, SPV, levered fund). Ask "what is the maturity mismatch of assets against the *stability* of liabilities?"
  - Failure mode: judging a bank on its capital ratio alone. The 2007–2009 failures came from runs on short-term secured and unsecured funding, not only from asset losses.
- **Leverage arithmetic**: `equity cushion / assets` is the percentage asset decline that wipes out equity.
  - The asset-to-liability ratio was 4.9× for households, 1.9× for nonfinancial businesses and only **1.1× for commercial banks**. So an **11.1%** fall in bank financial assets erases sector equity.
  - How: loss in capital = (share of risky assets) × (price drop) / (capital ratio).
  - Any entity more levered than its sector average loses proportionally more equity.
- **On- vs off-balance-sheet securitization**:
  - *On-balance-sheet*: the institution buys the assets and recovers funds when it sells the securities.
  - *Off-balance-sheet*: an **SPV/SIV** buys the assets, funded by short- and long-term debt.
  - Why banks preferred the off-balance-sheet route pre-crisis: they wanted the "moving" rather than the "storage" business, and sponsor guarantees were penalized less by capital rules than on-balance-sheet assets.
  - Failure mode: an SPV funded with commercial paper has financing risk. When asset quality is doubted, CP stops rolling and the SPV is put back on the sponsor's balance sheet.
  - Numbers: SPV assets were $4.2tn at end-2006 (74.3% mortgage-related, 19.9% of liabilities in CP) and fell to $2.8tn by March 2010, with CP down to 4.4% of liabilities.
- **Pension architecture (the three-pillar system)**:
  - Pillar 1 is public, mostly **PAYG** (pay-as-you-go). It comes in *Bismarckian* form (benefits linked to earnings: Austria, Belgium, France, Germany, Italy, Spain) or *anti-poverty* form (Ireland, Netherlands, UK).
  - Pillar 2 is occupational. Pillar 3 is private and always defined contribution.
  - **Defined benefit (DB)**: the sponsor bears the investment risk. **Defined contribution (DC)**: the beneficiary does. **Hybrid**: returns-based with some sponsor guarantee, such as guaranteed paid-in principal (Germany) or a minimum return (Switzerland, 2.75%).
  - The global trend is DB → DC/hybrid, which shifts risk from employers to employees.
  - Rule: the more generous the public replacement rate, the less households save through private pensions and insurance (Figure O.7 trend, which also fits the US and Japan).
- **Liability-driven demand (LDI)**: once regulation requires marking liabilities at market rates, sponsors hedge rate risk. The UK Pensions Act 2004, Dutch discounting at swap rates (formerly a static 4%) and Solvency II for insurers all push this way. Sponsors either lengthen bond portfolios or **receive fixed in long-dated swaps**. This structural receiving flow is a key explanatory factor for long-end EUR and GBP swap and bond pricing (see the ch02 trading case study).
- **Benchmark choice (swaps vs government bonds)**: price everything relative to the most liquid curve that carries common rate information.
  - Government bonds are **not fungible**: each issue is in fixed supply with idiosyncratic liquidity and financing (repo specialness). On-the-run Treasuries trade rich to a curve fitted on "similar" off-the-run bonds.
  - A swap is a **commodity**: a 10-year 4% swap can never be in short supply, because anyone can write a new one.
  - Hence bond traders price bond by bond, while swap traders "strike a curve" that prices the whole book. Swaps are now the base curve in the EUR, USD and JPY markets, and other curves are built as spreads on top. Even Treasury relative value is assessed as spread to the USD swap curve.

## Key Concepts
- **T-bills / notes / bonds**: US Treasury discount securities (≤1 year), coupon securities with original maturity ≤10 years, and >10 years. The note/bond split is a historical artifact of a statutory rate cap removed in 1988.
- **TIPS**: principal indexed to the CPI. The maturing principal is **floored at the original face**, which is a deflation floor. By contrast, **JGBi** principal is *not* floored, so its nominal return can be negative in deflation.
- **Reopening**: selling more of an existing issue at later auctions. For example, the UST 2.625% Aug-2020 was issued at $24bn, then reopened twice at $21bn each.
- **Agency- and GSE-backed securities**: agency debt, GSE debt (FNMA, FHLMC, FHLB) and agency MBS (FNMA, FHLMC, GNMA). They benefit from an *implicit* guarantee. The CBO estimated the funding advantage at 41bp on debt and 30bp on MBS.
- **Munis**: GO bonds (full faith and credit) vs revenue bonds (project cash flows). Interest is mostly federally tax-exempt, so top-bracket investors earn more after tax than on comparable taxables, especially at long maturities. **BABs** were taxable munis with a 35% federal interest rebate.
- **Commercial paper**: unsecured and short-term. US CP maturities run up to 270 days (longer would trigger SEC registration) and average about 30 days.
- **Federal funds / EONIA / TONAR**: uncollateralized overnight interbank rates in the US, the Eurozone and Japan.
- **Repo**: a short-term loan secured by high-quality collateral (a sale plus agreement to repurchase). It is the main tool of central bank operations: Fed repo, ECB MRO (≤1 week) and LTRO (3–6 months), BoJ *Gensaki*.
- **Tier 1 capital ratio**: common plus preferred equity over risk-weighted assets. The Basel II minimum was 4% (the BIS called for 6% by 2015). The market's comfort level is closer to 10%.
- **Solvency ratio (pensions)**: assets / PV(liabilities). Dutch funds went from 150% to 107% between 2008 and 2010.
- **Rinban**: BoJ outright JGB purchase auctions.
- **Quantitative easing (BoJ 2001–2006)**: expanding bank reserves via 25-day repo and Rinban. It largely failed, because banks hoarded liquidity and corporates kept deleveraging.
- **Security Market Program (ECB)**: outright purchases of peripheral sovereign bonds in 2010, about €47bn Greece, €15bn Ireland and €12bn Portugal.

## Formulas & Reference Tables
- `Leverage (asset/liability) = A / L`. Break-even asset loss that wipes out equity = `(A − L)/A`.
- `Capital hit (% of capital) = w_risky × Δp / k`, where w_risky is the share of assets hit, Δp the price drop and k the capital/assets ratio.
- `Debt-to-GDP` is the standard sovereign credit indicator. It is only comparable within reason, because some economies can sustain higher ratios.

| Maturity structure of govt debt | <2y | 2–5y | 5–10y | >10y |
|---|---|---|---|---|
| US Treasuries (Mar-2010) | 45% | 25% | 20% | 10% |
| Germany (Dec-2010) | 28% | 27% | 27% | 17% |
| France | 20% | 27% | 28% | 25% |
| Italy | 23% | 25% | 24% | 27% |
| JGBs (Jul-2010) | 27% | 26% | 28% | 19% |

US borrowing is short-heavy, which means more **refinancing (rollover) risk**. Europe's maturity profile is spread out.

| Market snapshot (2009–2010) | Key numbers |
|---|---|
| US credit market debt | Mortgages $14.2tn · Corp & foreign bonds $11.4tn · Treasuries $8.3tn · Agency/GSE $7.8tn · Loans $4.1tn · Munis $2.8tn · Consumer credit $2.4tn · CP $1.1tn |
| US public debt / GDP | 88% (65% at end-2006) |
| Fed balance sheet | $908bn (2006) → $2.3tn (Mar-2010). About 53% agency/GSE MBS, meaning 16% of the whole market |
| ECB balance sheet | €570bn (2002) → €1,135bn (Sep-2009). LTROs €635bn, deposit facility €140bn |
| European banks' holdings | 32% of European govt bonds, 44% of other govt loans (vs 2.4% of UST held by US banks) |
| Japan | Gross govt debt 188% of GDP. About 94% of JGBs held domestically, 55.6% by the public sector. Postal system holds about ⅓ of JGBs |
| Japanese households | 54.9% cash and deposits, 27% insurance and pensions, 2.9% bonds |
| European insurers' credit mix | AAA 3%, AA 20%, A 47%, BBB 30%. Equities only 7% of assets |

## Mental Models
- **Follow the balance sheet, then the price.** Before judging a curve segment rich or cheap, ask who is the structural buyer or receiver: pensions and insurers at the long end, banks and central banks at the front, the Japanese postal system in JGBs.
- **Funding stability > asset quality in a crisis.** A sound asset book funded overnight can fail faster than a weaker book funded with deposits and term debt.
- **Think of central banks as the lender of last resort to the whole system.** Post-2008 the ECB and BoJ shifted from managing reserves to *financing bank securities portfolios* via long-term repo. The ECB also took over interbank intermediation (the deposit facility on one side, LTROs on the other).
- **Use swaps as the base curve, government bonds as spreads to it.** A bond issue can be squeezed and a swap cannot.
- **Prefer "moving" to "storage" only if the moving stays off your book.** Implicit sponsor guarantees make off-balance-sheet vehicles economically on-balance-sheet in stress.

## Worked Example
**Bank leverage and mortgage losses (verified).**
- Inputs:
  - Commercial banking financial assets were $14.4tn and liabilities $12.8tn (March 2010).
  - At end-2006, 41.9% of bank assets were mortgage-related. Assume bank capital = 10% of assets.
- Step 1, equity cushion: 14.4 − 12.8 = $1.6tn, i.e. 1.6/14.4 = **11.1%** of assets. An 11.1% asset decline wipes out the sector's equity. The A/L ratio is 1.125, vs 4.9 for households and 1.9 for nonfinancial business.
- Step 2, mortgage shock: a 12% drop in mortgage-related assets costs 0.419 × 12% = **5.03%** of total assets.
- Step 3, capital impact: 5.03% / 10% ≈ **50%** of capital lost.
- Interpretation: a moderate fall in *one* asset class halves the capital of a 10×-levered bank. The real losses were larger for banks with above-average real estate exposure. Smaller US banks had 54% of assets real-estate-related, vs 43% for the 25 largest.

## Anti-patterns
- **Treating government bonds as fungible benchmarks**: on-the-runs carry liquidity and financing premia, so a curve fitted to off-the-runs will underprice them.
- **Reading sector averages as individual balance sheets**: averages hide the life cycle (friends and family → bank loans → private placement → public bonds) and the dispersion (bank deposit/liability ratio: 69% for the largest 25 US banks vs 84% for smaller ones).
- **Counting only marketable debt as "government debt"**: US Treasuries ($8.3tn) are not the full public debt ($12.8tn), which includes intragovernmental holdings such as the Social Security trust funds. In Japan, public-sector-held JGBs *should* be counted because they back third-party claims. BoJ holdings should not.
- **Assuming a debt ceiling caps issuance**: the statutory US limit ($14.294tn in Feb-2010) has been raised many times.
- **Assuming inflation-linked bonds always floor principal**: TIPS do and JGBi do not.

## Practitioner Notes
- **The long end is technical.** In EUR and GBP, pension and insurer receiving in long swaps, forced by mark-to-market liability rules, can invert the long forward curve independently of macro views. UK statutory inflation-linking of pension benefits is why the UK linker market is the most developed.
- **Funding runs follow a sequence**: fed funds and repo erode in days, then CP over months, then uninsured deposits leave, and customers draw committed credit lines at the worst moment.
- **Post-2008 institutional responses to remember**:
  - All surviving major US investment banks became bank holding companies to access the Fed discount window.
  - Broker-dealers cut their reliance on overnight repo.
  - The ECB held about €400bn of Greek, Irish and Portuguese bonds (outright plus repo) by end-2010, about 65% of their combined public debt.
- **The European sovereign–bank loop**: European banks hold about ⅓ of their governments' bonds, so sovereign stress and bank stress are the same trade.
- **Japan**: a domestic-savings-funded, JGB-centric market. Foreigners own only about 6% of JGBs but account for 15–25% of cash volume and 25–40% of JGB futures volume. The postal savings system, with ¥177tn of deposits, is the largest savings institution in the world.
- **US Treasury auction calendar** (as of 2010):
  - Bills: 4-, 13- and 26-week bills weekly, 52-week bills every 4 weeks.
  - Notes: 2-, 3-, 5- and 7-year notes monthly.
  - 10-year notes and 30-year bonds: quarterly new issues plus reopenings.
  - TIPS: 5- and 30-year issued annually and reopened twice; 10-year issued semiannually and reopened four times.

## Key Takeaways
1. The US, the Eurozone, Japan and the UK dominate debt issuance. EUR and USD dominate OTC rate derivatives, and Europe and North America dominate listed ones.
2. Banks run three risks (credit, rate and financing), and financing risk is what kills them fastest.
3. Bank leverage of about 10× means a 12% drop in about 40% of assets halves capital. Always compute the break-even loss `(A − L)/A`.
4. Mark-to-market liability regulation turns pensions and insurers into structural receivers of long swaps and buyers of long bonds. That is a price-setting technical.
5. Swaps are the benchmark curve because they are fungible. Government bonds carry issue-specific liquidity and repo effects.
6. Central bank balance sheets (Fed MBS purchases, ECB LTROs and SMP, BoJ Rinban) became major holders and financiers of fixed income after 2008.
7. Instrument details matter: the TIPS deflation floor vs the JGBi's absence of one, muni tax exemption, CP ≤270 days.

## Connects To
- **ch01**: arbitrage pricing and discount factors, the method behind "relative pricing to benchmarks".
- **ch02**: the EUR forward swap curve trading case, driven by the pension and insurer technicals described here.
- **ch03**: spreads of bonds to swap and government curves.
- **ch04–ch05**: interest rate risk of maturity-mismatched balance sheets (DV01, key-rate hedging for LDI).
- **ch12**: repo and financing risk during the 2007–2009 crisis.
- **ch15**: fed funds, EONIA and short-term rate markets.
- **ch19 / ch20**: corporate bonds and CDS; mortgages and MBS.
- **`cfa-fixed-income` ch02**: fixed income markets, issuance, trading and funding.
- **`cfa-fixed-income` ch13**: liability-driven investing.
- **`hull-derivatives` ch08**: securitization and the 2007 crisis.
