# Chapter 8: Alternative Indexing: Smart Beta, Thematic and ESG Instruments (Alternative Indexing: strumenti smart beta e tematici)
> **Source**: CFA Society Italy x Advisor Private, "Passive Investments" guide (Advisor Private no. 26, 2020), Chapter 4 | Alessandro Stella, CFA, CESGA (market data: Morningstar, DWS, MSCI, Borsa Italiana)

## Core Idea
Smart beta (factor ETFs) is the hybrid between active and passive: rules-based, transparent, cheap, but with a deliberate tilt away from market-cap weights to harvest persistent risk premia (value, size, momentum, low volatility, quality, dividend yield). It exists because (a) cap-weighted indices concentrate in the largest or most indebted issuers, (b) most active alpha turns out to be factor premia (Ang, Goetzmann, Schaefer 2012 for the Norwegian pension fund), and (c) 2008 showed asset-class correlations converge in crises. The same toolbox extends to bonds, to thematic mega-trend ETFs and to ESG indices.

## Frameworks Introduced
- **Alpha decomposition**: active "alpha (gross)" = smart-beta factor exposure (macro, region, style) + factor timing + security selection; only the remainder is "true (net) alpha". Passive factor tools replace the first two cheaply. Active large-cap US funds: about 85% trailed the S&P 500 over ten years to end 2018 (S&P Dow Jones Indices, as cited).
- **Factor theory lineage**: CAPM (Sharpe 1964: market beta); APT (Ross 1976: several macro factors, unnamed); Fama-French three-factor (1992-93: market, size SMB, value HML); Carhart (1997) adds momentum (MOM). Today's common set (MSCI table): **value** (book/price, earnings/price, cash flow, dividends), **size** (low market cap), **momentum** (3-12 month relative return), **low volatility** (standard deviation, beta, idiosyncratic risk), **dividend yield**, **quality** (ROE, earnings stability, leverage, accruals). "Factor zoo" warning (Cochrane 2011): separate factors with economic rationale and a risk premium from mere anomalies.
- **Test for a genuine, investable factor**: (Miller 2006 and Ang 2013 criteria) persistent over time, strong explanatory power across many securities, academically grounded, historical and expected excess return, track record covering at least a full market cycle, and implementable in a liquid, capacity-sufficient strategy. Academic factor portfolios ignore transaction costs, liquidity, capacity; real implementation differs.
- **Smart beta positioning**: between passive (market return, rules-based, transparent) and active (active return, discretionary implementation). Names: alternative beta, fundamental indexing, alternative indexing, factor-tilted, style investing. 17% of global ETP assets were in factor strategies at end 2019 (ETFGI/Morningstar). Why use it: (1) lower cost than active for the same premia; (2) targeted, tactical or strategic exposure to a specific risk (and diversification by factor rather than asset class: private equity, hedge funds, real estate correlate with equity through shared macro factors); (3) transparency and full look-through, protecting against style drift; (4) risk management (low-vol/low-beta tilts for lower drawdowns; adjusting effective market exposure, Baker 2011); (5) fits specific needs (dividend ETFs for income investors).
- **Morningstar Factor Profile** (adds yield, momentum, quality, volatility, liquidity, size to the 1992 Style Box): compare a fund's current factor loadings to its 5-year history and category average to detect drift and to explain performance gaps among similar products. January-May 2020: dividend ETFs tilted to quality, size and momentum beat ETFs focused purely on yield.
- **Factor ETFs in bonds**: after 2008, risk-factor ideas moved to credit and rates. Cap-weighted bond indices overweight the most indebted issuers (Greece weight in Euro-sovereign indices rose from 3% to over 4.5% between 2002 and its 2010 downgrade to sub-investment grade). Alternatives: quality-weighted sovereign indices (DWS/Markit tested 18 fundamental variables on EM hard-currency debt: debt/GDP, debt/exports, external debt, reserves, fiscal and current-account balances, GDP per capita and growth, inflation, openness, unemployment, competitiveness, education, old-age dependency, corruption perception, political rights, default history, developed/emerging status) and duration-hedged credit ETFs (hold IG or HY corporates, hedge rates with futures or short government bonds, to earn spread with minimal rate sensitivity). Houweling and van Zundert (2014): factors (size, low risk, value, momentum) in corporate bonds lift Sharpe and alpha over market-cap; added to an equity factor portfolio, up to +1% return and +0.1 Sharpe.
- **Factor cyclicality and timing vs mixing**: factors behave differently across the cycle: value and size lead early in bull markets, momentum follows, low volatility/dividend/quality suit contraction. Each factor typically had 2-3 years of underperformance vs the market (MSCI factor histories 1988-2013). Timing is hard. Dichtl, Drobetz, Lohre, Rother, Vosskamp (FAJ 2019): timing and tilting added about 95 bp a year gross over 20 years vs equal-weighted factors, but turnover of 4.8 vs 0.26 erased it net: net excess return 2.25% vs 2.21%, net Sharpe 0.79 vs 0.81, information ratio 0.04. **Factor mixing** (multi-factor ETFs combining complementary cycles) is the practical answer. Correlations of excess returns (Deutsche Bank, Jan 2000-Feb 2019): value-quality -35%, value-momentum -19%, quality-momentum +2%, min-vol vs value -0.2%, vs quality 15%, vs momentum 21%. Bottom-up multi-factor construction (stock-level exposure to several factors) beats merely stacking single-factor portfolios. Many providers equal-weight factors; alternatives are risk-contribution weights.
- **Smart-beta market (Morningstar, end 2019)**: 1,422 strategic-beta ETPs with about 1.09 trn USD (USA 960.6 bn, 88.1%; Europe 79.1 bn, 7.2% of global smart-beta assets, 36.6% growth; Asia-Pacific 34.5 bn); 2019 flows 93.2 bn (organic growth 11.6%); 406 launches in three years. Europe: dividend ETFs 30.1 bn about 40% of assets; 2018 flows favored risk-oriented (min vol) and multifactor; value saw 1.2 bn outflows in 2018 as value lagged growth for 8 years; 2019 flows into yield (2.7 bn), min vol (1.6), size (1.5), multifactor (1.5). Costs: asset-weighted average fee of all ETPs 0.25%; strategic-beta ETPs 0.36% (equal-weighted 0.43%); European smart-beta management fee fell from 0.40% (2017) to 0.34% (2019), a 15% cut (verified).
- **Thematic investing**: selects mega-trends (e-commerce, 5G, robotics, mobility, smart cities, energy efficiency, digitalization, cybersecurity, AI) rather than past winners. Checks: is the driver investable; structural change; economic sustainability; growth potential; profitability of exposed firms. Construction: revenue-based classification (e.g. FactSet RBICS) is sector-like and often too rigid; a bottom-up company-level (qualitative and quantitative) approach better picks firms best positioned, including those whose revenues have not yet appeared. Young market: Borsa Italiana ETFplus 116 thematic ETFs end 2019 (43 new, +58%), assets 2.38 bn EUR; costs above broad-beta ETFs but expected to fall.
- **ESG ETFs and passive ESG approaches**: (1) exclusion (negative screen on controversial sectors and business-activity revenues; most traditional), (2) best-in-class (select top ESG-rated companies within sector; e.g. MSCI ESG Leaders, MSCI SRI), (3) thematic (e.g. impact). MSCI's rating model scores 37 issues under environmental (climate change, natural capital, pollution and waste, environmental opportunities), social (human capital, product liability, stakeholder opposition, social opportunities) and governance (corporate governance, corporate behavior) pillars. Evidence quoted: DWS and Hamburg University 2015: in about 90% of studies ESG integration was not worse than conventional; MSCI AC World Sustainable Impact +13.0% vs MSCI AC World -1.3% year to 31 July 2020 (net return, USD). ESG as a separate equity factor is debated; alpha is largely explained by size, value etc. Market data: global ESG assets 30.7 trn USD end 2018 (+34% in two years, GSIA); European ESG ETFs about 17.3 bn USD end 2019 (2.1% share, 6.0 bn flows; SRI ETFs 14.4 bn, ex-controversial weapons 1.1, low carbon 0.9, ESG 0.7, thematic 0.2); about 13 bn new money in H1 2020 (over 36% of ETP flows); Italy: 57 new ESG instruments in 2019, record 1.5 bn EUR inflows, 109 ETFs with 2.65 bn EUR. EU taxonomy action plan is expected to define sustainable activities; the lack of unified criteria complicates ESG verification.

## Key Concepts
- **Smart / strategic beta**: rules-based non-cap-weighted index strategies.
- **Factor**: persistent characteristic explaining cross-sectional returns, with risk-premium rationale.
- **SMB / HML / MOM**: size, value and momentum factor returns.
- **Factor zoo**: proliferation of weak or data-mined factors.
- **Style drift**: manager deviating from stated style.
- **Cap-weighted concentration**: over-weight of the largest or most indebted issuers.
- **Quality-weighted bond index**: weights by fundamentals instead of debt outstanding.
- **Factor mixing / multi-factor**: combining factors with complementary cycles.
- **Factor timing**: rotating factors by regime; erodes alpha by turnover.
- **Look-through**: transparency of underlying exposures.
- **Best-in-class / exclusion / thematic ESG**: three passive ESG approaches.
- **Mega-trend**: structural change used as thematic driver.
- **RBICS**: FactSet revenue-based industry classification.

## Formulas & Reference Tables
- `Excess return(factor) = R(factor portfolio) - R(market)` (long-only factor ETF measured vs cap-weighted parent).
- `Sharpe = excess return / standard deviation`; `IR = (R_timing - R_equal) / TE`.
- Factor timing table (FAJ 2019, % per year):

| | Equal-weight gross | Equal-weight net | Timing gross | Timing net |
|---|---|---|---|---|
| Excess return | 3.22 | 2.21 | 4.17 | 2.25 |
| Std dev | 3.73 (see note) | 2.72 | 2.83 | 2.85 |
| Sharpe | 1.18 | 0.81 | 1.47 | 0.79 |
| Tracking error | - | - | 1.13 | 1.13 |
| IR | - | - | 0.84 | 0.04 |
| Turnover | 0.26 | 0.26 | 4.80 | 4.80 |

  **⚠ Correction**: 3.22 / 3.73 = 0.86, whereas the stated Sharpe is 1.18 = 3.22 / 2.73; the standard deviation printed as 3.73 for the equal-weight gross column is most likely a typo for 2.73. Other cells verify (net 2.21/2.72 = 0.81; timing 4.17/2.83 = 1.47; net 2.25/2.85 = 0.79; IR 0.95/1.13 = 0.84 and 0.04/1.13 = 0.04).
- Factor-correlation grid: see framework above.

## Mental Models
- Use smart beta when you want a known factor premium at index cost; use active only for alpha beyond factors.
- Use multi-factor, not single-factor timing, unless you can trade at near-zero cost.
- Use quality-weighted or duration-hedged bond ETFs to avoid cap-weighting's bias toward the biggest debtors.
- Use the Morningstar Factor Profile (or holdings look-through) before buying: does it actually deliver the factor claimed?
- Use exclusion for values, best-in-class for ESG tilt with sector neutrality, thematic for conviction; know which one you are buying.
- Use thematic ETFs as satellite positions: young, concentrated, costlier.

## Worked Example
Net value of factor timing. Inputs: equal-weight factor mix net excess 2.21%, Sharpe 0.81; timing strategy gross excess 4.17% with turnover 4.80; net 2.25%. Steps: gross improvement = 4.17 - 3.22 = 0.95 pt (about 95 bp a year); net improvement = 2.25 - 2.21 = 0.04 pt; cost absorbed = 0.95 - 0.04 = 0.91 pt (about 96% of the gain). Information ratio net = 0.04 / 1.13 = 0.035. Interpretation: turnover of 4.8x makes the cost ~19 bp per unit of turnover on this arithmetic; the gain from timing is real on paper but untradable, hence factor mixing.

## Anti-patterns
- Treating any back-tested anomaly as a factor.
- Buying a dividend ETF as "value" without checking yield/quality/size loadings.
- Chasing last year's factor winner (value outflows before a rotation) or rotating factors with high turnover.
- Assuming "ESG" means the same thing across ETFs (exclusion vs best-in-class vs impact).
- Using thematic ETFs as core holdings without analyzing concentration, revenue purity, and fees.
- Ignoring that factors can lag the market for 2-3 years.

## Practitioner Notes
- Request: index rules (selection, weights, rebalance), turnover, factor exposures, capacity, TER, tracking vs parent, look-through.
- Combine factors with different cycles (value/size early, momentum mid, low volatility/quality/dividend late), accepting 2-3 year dry spells.
- For income clients, check payout sustainability (quality) not just yield.
- Bond factor ETFs complement equity factor portfolios: more diversification of risk sources.
- For ESG: check the underlying rating methodology, data coverage, and fund manager's voting (see ch07).
- Fee compression is ongoing; compare to plain cap-weighted ETFs, which remain much cheaper.

## Key Takeaways
- Most of the "alpha" in active funds is factor premium that can be bought passively.
- A factor needs persistence, economic rationale, breadth and investability; many published factors fail.
- Smart beta sits between active and passive: cheaper than active, rules-based, transparent, but still a tilt that can underperform for years.
- Factor timing alpha disappears net of turnover; multi-factor mixing exploits low or negative factor correlations.
- Cap-weighted bond indices reward heavy borrowers; quality-weighted and duration-hedged factor approaches address that.
- Thematic and ESG ETFs are growing quickly but young, costlier and defined very differently from one provider to the next.
- Smart beta was 17% of global ETP assets and about 1.09 trn USD at end 2019.

## Connects To
- **ch02**: passive/active, factor risk in institutional allocation.
- **ch03**: performance attribution and factor analysis.
- **ch05-ch07**: passive vehicles, costs and replication.
- **ch06**: climate benchmarks (CTB/PAB) and ESG index mechanics.
- **ch06-ch07 sponsored inserts**: ESG engagement myths.
- **Factor chapters ch06-ch08 of `cfasi-equity-investment-styles`**: factor investing in depth.
- **ch09-ch14**: ETF/fund selection for smart beta and ESG.
- **ch20-ch30**: ESG investing guide.
