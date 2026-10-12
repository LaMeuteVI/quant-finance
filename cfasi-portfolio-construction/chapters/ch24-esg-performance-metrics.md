# Chapter 24: ESG Investing - Performance Metrics for ESG Investments
> **Source**: CFA Society Italy × Advisor Private (AP Advisor Private n. 13, Sep-Oct 2018), *Investimenti ESG*, Chapter 5 "Metriche di Performance per gli Investimenti ESG" | Antonella Puca, CFA (CFA Institute)

## Core Idea
Measuring an ESG fund means measuring two things: **ESG performance** (how sustainable the holdings are) and **financial risk-adjusted performance**. ESG performance starts from **materiality indicators** and **KPIs** reported by companies under standards such as GRI, IIRC, SASB, UN Global Compact, CDP and CDSB; agencies convert them into **company ESG ratings** and then **portfolio ratings** (Morningstar's sustainability score). The big obstacle is the absence of a single global standard: even a KPI as simple as "percentage of women in the workforce" can be computed in incompatible ways. On financial results, large meta-studies find a mostly non-negative relation between ESG and performance, and index evidence shows ESG leaders broadly in line with the parent index.

## Frameworks Introduced
- **Barriers to ESG adoption (AIMA 2018 hedge-fund survey)**: inadequate methodologies for measuring sustainability risk (45.1% of managers), lack of relevant corporate disclosure (44%); ESG analysis needs skills different from financial analysis; benefits take time and no single standard exists to measure a company's or fund's ESG performance. Swiss Sustainable Finance (2017) adds performance concerns and ESG data-analysis difficulty.
- **Regulatory and governance backdrop in Italy/EU**: Legislative Decree 32/2007 (implementing Directive 2003/51/EC) requires management reports to include financial and non-financial KPIs; **Non-Financial Reporting Directive 2014/95/EU**, implemented by Legislative Decree 254/2016 (30 December 2016, effective 25 January 2017), imposes minimum ESG disclosure on large companies, either inside the annual report or as a separate document subject to external audit review; Borsa Italiana's Corporate Governance Code (2015) asks boards to consider all risks material to medium-long-term sustainability and large FTSE MIB companies to consider a sustainability committee.
- **Materiality indicators (Oxford / Arabesque 2015)**: E - biodiversity/land use, carbon emissions, climate-change risks, energy use, raw material sourcing, regulatory and legal risks, supply-chain management, waste and recycling, water management, weather events. S - community relations, controversial activities, products and consumer relations, diversity, labour relations, health and safety, human-resource management, human rights, responsible marketing and R&D, union relationships. G - accountability mechanisms, anti-takeover measures, board structure and size, bribery and corruption, CEO duality, executive compensation, control structure, shareholder rights, transparency, voting procedures. Relevance varies by company and sector.
- **KPI definition problem**: each indicator breaks down into qualitative and quantitative KPIs; definitions vary by sector and firm (PwC's Damian Regan). Diversity example: percentage of women - of what population (full time only or part time too, all levels or non-managers, excluded peripheral workers)? Other S KPIs: training participation in safety programmes, workplace incidents, donations to non-profits, legal disputes, voluntary turnover.
- **Corporate ESG reporting standards**: **GRI** (Global Reporting Initiative; estimated adopted by over 80% of the largest global companies), **IIRC** (Integrated Reporting Framework: connectivity of financial and non-financial capital over short, medium, long term), **SASB** (US, industry-specific standards for listed companies), **UN Global Compact**, **CDP** (climate, water and raw-material reporting; per LSEG 2015, 93% of FTSE 100, 64% of FTSE 350 and 45% of the 100 largest Borsa Italiana companies reported environmental data to CDP), **CDSB** (environmental disclosure standards). Assurance: auditors such as PwC can attest to KPIs, which verifies that the calculation follows the company's own stated method, **not** that the KPI is better than another firm's.
  - Direction: industry moving to standardization but still far from the comparability of IFRS or US GAAP financial data.
- **Company and portfolio ratings**: agencies turn KPIs into ratings (MSCI: AAA-CCC scale for over 6,000 companies). **Morningstar sustainability rating of funds**: asset-weighted average of normalized company ESG scores from Sustainalytics, excluding unrated securities and derivatives such as options/futures and short-sale rights; the fund needs at least 50% of net assets in covered securities (rescaled to 100%); the score is reduced by a **portfolio controversy deduction** reflecting the holdings' involvement in ESG incidents, giving the **Portfolio Sustainability Score (PSS)**; funds are ranked within their category.
  - Distribution (Morningstar Table 2): top 10% receive 5 (high), next 22.5% score 4 (above average), next 35% score 3, next 22.5% score 2, bottom 10% score 1. (The source prints the second bucket as 25%, which would sum to 102.5%; **Correction**: 22.5%.) Fewer than 5% of 300+ open-end funds available in Italy at 31 March 2018 got the top score.
- **Fiduciary standard for ESG financial performance**: US Department of Labor (ERISA ETI Bulletin 2015, FAB 2018-01): ESG factors may enter primary analysis, but fiduciaries cannot sacrifice return or accept more risk to promote collateral policy goals. UK Law Commission (2014): no obstacle to considering ESG factors that are or may be financially material.
- **Evidence on ESG and financial performance**: Friede, Busch and Bassen (2015) aggregate over 2,000 empirical studies: about 90% find a non-negative ESG-performance relation, a majority positive. Zanker (CFA, 2017) review: ESG investments performed at least as well on a risk-adjusted basis as conventional ones.
- **Index evidence (MSCI World ESG Leaders versus MSCI World, to May 2018)**: net annualized returns 7.07% / 8.79% / 5.28% over 3 / 5 / 10 years versus 7.65% / 9.40% / 5.38%; 10-year annualized volatility 16.23% versus 16.21%; 10-year Sharpe ratio 0.37 for both. The Leaders index is a best-in-class, asset-weighted index built on MSCI World excluding alcohol, tobacco, gambling, nuclear and weapons.
  - Hypothesized channels: neglecting sustainability raises long-run and tail risk; leaders in strategic products and workforce attraction often have better ESG profiles; lower legal-litigation risk and expenses help operating performance. Use a medium-long horizon for comparison.

## Key Concepts
- **Materiality indicator**: ESG dimension likely to affect a company's financial performance.
- **KPI (key performance indicator)**: quantitative or qualitative measure of an ESG indicator.
- **Non-financial reporting**: ESG disclosure required of large EU companies.
- **GRI / IIRC / SASB / CDP / CDSB / UN Global Compact**: reporting standards and initiatives (see above).
- **Assurance**: independent verification of the calculation method for a reported KPI.
- **ESG rating**: agency score assigned to an issuer or portfolio.
- **Portfolio Sustainability Score (PSS)**: Morningstar's controversy-adjusted asset-weighted ESG score.
- **Portfolio controversy deduction**: penalty applied for ESG incidents.
- **ETI Bulletin**: US DOL guidance on economically targeted investments.
- **Sharpe ratio**: excess return per unit of volatility: `(R - Rf) / sigma`.

## Formulas & Reference Tables
- Fund ESG score (Morningstar-type): `ESG_fund = sum_i w_i * ESG_i^norm` over covered holdings, with `w_i` rescaled to sum to 100% of covered assets; `PSS = ESG_fund - controversy deduction`.
- Sharpe ratio: `(R_p - R_f) / sigma_p`.
- Difference in annualized return (ESG Leaders minus parent): -0.58 pp (3y), -0.61 pp (5y), -0.10 pp (10y); volatility difference +0.02 pp.

Morningstar rating buckets: 5 globes (top 10%), 4 (next 22.5%), 3 (next 35%), 2 (next 22.5%), 1 (bottom 10%).

## Mental Models
- Use "ESG performance is two numbers: how sustainable and how profitable".
- Use sector-specific materiality to decide which KPIs matter before comparing ratings.
- Use assurance as a check on consistency of method, not on quality of the KPI.
- Use a 3-to-10-year window when comparing ESG indices with parents; short windows confuse style and sector effects.
- Use a fiduciary frame: ESG consideration is acceptable if financially material and not at the cost of return or risk.

## Worked Example
**ESG Leaders versus parent (recomputed from the source figures).**
- Inputs: Returns to May 2018 (ESG Leaders / parent): 3y 7.07 / 7.65; 5y 8.79 / 9.40; 10y 5.28 / 5.38. Volatility 10y 16.23 / 16.21. Sharpe 10y 0.37 / 0.37.
- Steps: differences are -0.58, -0.61, -0.10 pp. Over 10 years the gap is 0.10 pp a year, and the Sharpe ratio is identical to two decimals.
- Interpretation: ESG integration via a best-in-class index cost a small shortfall over recent windows and none over ten years on a risk-adjusted basis; the result supports "no material penalty", not "automatic outperformance".

## Anti-patterns
- Comparing ESG ratings across agencies as if they measured the same thing.
- Interpreting an aggregate ESG score as a simple average of E, S and G without regard to sector materiality.
- Reading "assured" as "good".
- Claiming ESG outperformance from one short-window comparison.
- Counting derivatives and unrated holdings as covered when computing a fund's ESG coverage.

## Practitioner Notes
- Ask for the KPI definition and boundary (population, scope) before using any reported number.
- Check fund coverage: a fund rated on 50% of its assets differs from one rated on 95%.
- Standardization is advancing (GRI, SASB, CDP), but comparability remains weaker than financial statements.

## Key Takeaways
1. ESG performance measurement is hampered by missing global standards and KPI definition differences.
2. Materiality indicators across E, S, G are the starting point; relevance varies by sector.
3. GRI, IIRC, SASB, UN Global Compact, CDP and CDSB are the main reporting frameworks.
4. Morningstar's PSS combines asset-weighted ESG scores with a controversy deduction.
5. Meta-evidence: about 90% of 2,000+ studies show non-negative ESG-performance links.
6. MSCI World ESG Leaders tracked the parent closely on return, volatility and Sharpe ratio.
7. Fiduciaries may consider ESG when financially material but cannot sacrifice return.

## Connects To
- **ch20**: why investors adopt ESG and the types of strategies measured here.
- **ch21**: data quality and standard-setting background (SASB, EFFAS).
- **ch23**: index and rating-agency choices behind ESG scores.
- **ch25**: SASB materiality applied to European equities.
- **ch26**: non-financial statement (Legislative Decree 254/2016) in practice.
- **`cfa-ethics-gips`**: fiduciary duty and GIPS context.
