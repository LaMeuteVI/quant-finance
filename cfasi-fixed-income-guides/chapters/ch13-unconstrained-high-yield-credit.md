# Chapter 13: The High Yield Credit Market
> **Source**: CFA Society Italy × Advisor Private, "Unconstrained Fixed Income" guide (Sept–Oct 2019), Chapter 2 (Il mercato del credito High Yield) | Emanuele Gerletti, CFA and Francesco Vicino

## Core Idea
High yield (HY, speculative grade) is the part of the credit market where credit spread, not the risk-free rate, is the main component of expected return. The spread is explained by three drivers: loss given default (1 minus recovery value), probability of default and an excess spread for unexpected losses and liquidity. Practitioners manage HY through credit analysis (cash generation, leverage ratios), spread duration with mean-reversion rules, technical factors (liquidity, central bank distortions), derivatives (CDS, indices) and relative value trades (horizontal, vertical, curve, basis, rating compression, sovereign vs quasi-sovereign). Hard-currency EM credit is a major sub-market driven by China, commodities and the Fed.

## Frameworks Introduced
- **Rating boundary**: below Baa3 (Moody's) or BBB- (S&P, Fitch) is HY. Not all HY is "junk": solid cash-generating names penalised by geography or governance, and "Rising Stars" about to be upgraded to IG. Instruments of the same issuer can carry different ratings by seniority. Expected yields of B and CCC names can reach about 10% in EUR.
- **Credit analysis pairs**: (1) cash-generation measures: cash flow from operations, from investing, from financing, free cash flow; (2) credit position ratios: Gross debt / EBITDA, Net debt / EBITDA, Cash flow from operations / Gross debt. Interpret by sector and country (utilities sustain higher leverage than metals and mining) and consider non-core assets or stakes that can be sold. In HY, credit analysis is "more art than science".
- **Yield decomposition**: risk-free rate (policy, growth, inflation) + swap spread (interbank risk) + credit spread. In HY the credit spread dominates.
- **Credit spread formula**
  `Credit spread = Probability of default × (1 − Recovery value) + Excess spread`
  - Recovery value: depends on seniority, collateral, business sustainability, region, sector. 2018 recovery about 40% for the whole market, from 27% (Latin America) to 44% (Asia); it varies widely by year (EM global 49% in 2015, 28% in 2016, 46% in 2017, 39% in 2018, with distressed exchanges).
  - Probability of default: cash generation, financial and operating leverage, economic cycle, jurisdiction. EM HY default rate from 2011 to 2018: between 0.6% and 5.1%, and double digits possible in recession (Latin America 10.6% in 2013).
  - Excess spread: compensation for unexpected loss and illiquidity; rises in stress.
  - Use to check whether an index's spread is consistent with expected defaults.
- **Spread duration**: price change `ΔP ≈ −Spread duration × ΔCredit spread`. Larger spread duration means larger price impact for a given spread move.
  - **Mean-reversion rule**: HY spread excursions beyond two standard deviations are rare and brief. When spreads are above +1 or +2 standard deviations, raise spread duration to harvest mean reversion; when below −1 or −2 standard deviations, reduce spread duration to avoid a larger correction.
  - **Callable trap**: in tight markets callable bonds are priced to the call, which shortens spread duration; when spreads widen, pricing switches to the original maturity, spread duration jumps and prices fall more than expected. In stress, prices along the curve converge to the recovery level, so longer maturities do not simply fall more.
  - **Floater**: do not confuse interest rate duration (low, because of coupon resets) with spread duration (high and the key risk).
- **Technical factors / liquidity**: bond size, bid-offer (wider in HY, sometimes quoted in points), currency premium for non-home-currency issues, and QE side effects (IG scarcity pushes investors to HY, more generalists in the segment, amplifying moves in both directions).
- **CDS toolkit**: a CDS pays a periodic premium (standard coupon 500 bp for HY, upfront payment depends on whether the traded spread is below or above the coupon) to the protection seller who covers losses on a credit event. Protection buyer = seller of risk, gains when spreads widen; protection seller = buyer of risk, replicates a bond's credit exposure without the risk-free/swap component. Indices: iTraxx Crossover (XOVER, 75 European HY names) and CDX (US, 100 names), semiannual roll. Typical tenors 6 months to 10 years; 5-year most liquid.
- **Trade types**
  | Trade | Structure |
  |---|---|
  | Long credit risk | Buy a bond, ETF, long-only fund, or sell CDS protection |
  | Short credit risk | Short bond, buy CDS protection, short ETF (institutional or limited retail access) |
  | Horizontal pair | Long one issuer / short another |
  | Vertical pair | Same issuer, different seniority (senior vs sub) |
  | Curve trade | Same issuer, different maturities |
  | Basis trade | `Basis = CDS spread − Z-spread`; arbitrage when it deviates from zero because of technical factors |
  | Rating compression/decompression | Long low-rating, short high-rating at extreme spread differentials (e.g. MAIN (IG) vs XOVER (HY) in Europe) |
  | Sovereign vs quasi-sovereign | Petrobras 2023 vs Brazil 2023 (gap about 140 bp, to over 600 bp in 2015-16, normal about 135 bp); Pemex 2024 vs Mexico 2023 (average gap about 145 bp, peaked about 300 bp, trough about 100 bp); Pemex stand-alone CCC (Fitch) but government support lifts the rating to BB+ (6 notches) |
  - Risk: "too big to fail" is a bet, not a guarantee (Venezuela and PDVSA).
- **Hard currency EM credit market (CEMBI)**: about USD 2.1 trillion; Asia about 52% (China 31%), Latin America 25% (Brazil and Mexico 8% each), EM Europe and Middle East & Africa about 11% each. Drivers: China (GDP growth, debt levels, CNY, trade war), commodities (Brazil, Russia, some African and Middle Eastern issuers are exporters; Turkey and China are importers), Fed policy and USD strength (USD-denominated issues with local revenues: telecoms, utilities), local legislation risk (creditor protection in distress).
- **Rate vs spread example**: summer 2013 US 10-year yield rose from 1.64% to nearly 3%, the ICE BofA EM HY index lost about 5.67%, mostly from the risk-free leg while spreads were little changed. Normally rising yields on growth hopes come with tightening spreads, but the correlation is not stable.

## Key Concepts
- **High yield / speculative grade** — below IG.
- **Rising star / fallen angel** — HY about to become IG / IG cut to HY.
- **Gross / Net debt to EBITDA** — leverage ratios.
- **Free cash flow** — cash from operations less capital expenditure.
- **Swap spread** — interbank risk component.
- **Excess spread** — risk premium beyond expected loss.
- **Spread duration** — sensitivity to credit spread.
- **CDS, protection buyer / seller** — credit insurance contract.
- **XOVER / MAIN / CDX** — CDS indices (European HY / European IG / US).
- **Basis** — CDS spread minus Z-spread.
- **Quasi-sovereign** — state-controlled company.
- **Distressed exchange** — default through bond exchange; recovery stats show "with" and "ex" distressed exchanges.
- **CEMBI** — JP Morgan Corporate EM Bond Index.

## Formulas & Reference Tables
- `Credit spread ≈ PD × (1 − RR) + Excess spread`
- `ΔP ≈ −SpreadDuration × ΔSpread`
- `Basis = CDS spread − Z-spread`
- CDS upfront: positive or negative amount reflects traded spread above/below the standard 500 bp coupon.
- EM HY default rates (J.P. Morgan): 2011 0.6%, 2012 3.5%, 2013 4.3%, 2014 3.8%, 2015 3.8%, 2016 5.1%, 2017 2.3%, 2018 1.6%.
- Rating table in the source mislabels Baa2 as BBB+ and B2 twice; correct mapping Baa1 BBB+, Baa2 BBB, Baa3 BBB-; B1 B+, B2 B, B3 B-. **⚠ Correction**. The source also defines spread duration as the time to repay the capital, which is wrong: spread duration is the price sensitivity to spread changes.

## Mental Models
- Use the spread decomposition to ask: is the market spread above expected loss plus a fair excess spread?
- Use spread duration actively with a mean-reversion band (±1 to ±2 standard deviations).
- Use CDS indices for liquid expression of views and for hedging a cash HY portfolio.
- Use pair trades to isolate credit views from rate views; check that the legs have equal spread duration.
- Use the callable-bond trap as a reason to look at spread duration to worst, and stress at original maturity.

## Worked Example
Check an HY index spread against expected loss.
Inputs (using the guide's 2018 numbers where available, the rest the writer's): EM HY default rate 1.6% (2018), recovery 40%, observed index spread 400 bp.
1. Expected loss `= 1.6% × (1 − 0.40) = 0.96%`, i.e. 96 bp.
2. Excess spread `= 400 − 96 = 304 bp` is what the market pays above expected loss.
3. Stress view: default rate 5.1% (2016 peak) and recovery 28% (2016): loss `= 5.1% × 0.72 = 3.67%` (367 bp), leaving only 33 bp of excess spread.
4. With spread duration 4.0, a 100 bp widening costs `4.0 × 1.0% = 4.0%` of price, about the entire year's carry (spread 4% plus risk-free).
Interpretation: HY spreads cover expected loss in normal years with a wide margin but nearly vanish in a 2016-type year; position sizing should be done on spread duration, not maturity.

## Anti-patterns
- Judging HY solely by rating, ignoring cash flows, leverage and sector norms.
- Buying callable HY at a tight spread and counting on call-based duration.
- Hedging floaters with interest rate duration only.
- Running a basis or pair trade without matching spread duration.
- Assuming sovereign support (quasi-sovereigns) is guaranteed.
- Buying a passive EM credit ETF without knowing it is about half Asia, one-third China.

## Practitioner Notes
- Liquidity in HY is worse than IG; QE crowded generalists into HY, which can exaggerate moves.
- Retail access to credit shorts is limited to some ETFs; single bond shorts and CDS are institutional.
- Rating agencies' stand-alone vs supported ratings (Pemex) tell you how much a quasi-sovereign's spread depends on state support.

## Key Takeaways
1. HY starts below BBB-/Baa3 and includes rising stars and fallen angels.
2. Credit analysis: cash generation plus leverage ratios, read by sector and country.
3. Credit spread = default probability x loss given default + excess spread.
4. Spread duration, not maturity, measures HY price risk; use mean reversion bands.
5. Callable and floating-rate structures distort duration signals.
6. CDS and indices (XOVER, CDX) allow long or short credit exposure.
7. Pair trade families: horizontal, vertical, curve, basis, rating compression, sovereign vs quasi-sovereign.
8. Hard-currency EM credit is dominated by China, commodities and the Fed.

## Connects To
- **ch12**: IG corporates and spread vs rate returns.
- **ch14**: convertible bonds, an equity-linked credit alternative.
- **ch15**: bank subordinated and hybrid instruments.
- **ch16**: local currency EM.
- **ch03** (`cfasi-fixed-income-guides`): HY issuer types and covenants.
- **`cfa-fixed-income` ch07**: credit analysis and CDS in the CFA curriculum.
