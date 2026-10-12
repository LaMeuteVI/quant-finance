# Chapter 25: ESG and Value Investing
> **Source**: CFA Society Italy × Advisor Private (AP Advisor Private n. 13, Sep-Oct 2018), *Investimenti ESG*, Chapter 6 "ESG e Value Investing" | Angelo Meda, CFA, CIPM and Matteo Bonaventura, CFA (BANOR SIM; research with Politecnico di Milano)

## Core Idea
Value investing (Graham and Dodd, 1928; Buffett) buys securities trading below **intrinsic value** with a **margin of safety**. As intangible assets rose from 17% of market capitalization in 1975 to about 84% in 2015, balance-sheet analysis alone no longer explains durable earnings, so value investors need non-financial information on competitive advantage (**moat**) and externalities. ESG data are the proposed bridge, but face three problems: company-sourced and marketing-contaminated data (greenwashing), no accepted standards, and hard interpretation. SASB's **materiality** concept helps. A BANOR SIM / Politecnico di Milano study of the STOXX Europe 600 (2012-2017) found that high-ESG stocks outperformed through higher revenue growth, margin improvement and dividend yield, and that **combining a value factor (P/E) with ESG** beat either alone by about 1 percentage point a year.

## Frameworks Introduced
- **Value investing core**: (1) estimate intrinsic value (the value to which price should converge); (2) buy only when price is sufficiently below it; the gap is the **margin of safety**; wider margin gives higher probability of positive returns over a long horizon. Rejects strong market efficiency; relies on study of financial statements and fundamentals.
  - Evolution: Graham-Dodd net-net (current assets minus liabilities below price); 1960s onwards, Buffett: business model and **moat** (tangible sources: unique resources, location; intangible: patents, brands, trade secrets).
  - Failure mode: tangible-asset screens miss "capital light" companies (technology, services, internet, social media) whose value is intangible.
- **Intangible shift (Ocean Tomo)**: share of market cap in intangible assets: 1975 about 17%; 1985 about 32%; 1995 about 68%; 2005 about 80%; 2015 about 84% (complement tangible).
- **ESG as extension of fundamental analysis**: E, S, G capture externalities, reveal risks, and link to fundamentals: environmental performance maps to resource efficiency, social to effectiveness (workforce), governance to management alignment with company goals.
- **Three obstacles to using ESG data**
  1. **Source**: data come from sustainability reports, which are partly marketing; practice of showcasing marginal projects is **greenwashing**.
  2. **Standards**: no accepted reporting standard or calculation method comparable to financial reporting (which itself still struggles with IFRS/US GAAP convergence). GRI offers standard indicators for all firms but does not distinguish sector-specific topics. **SASB** (founded 2011) answers with **materiality**: report only ESG information whose trend and variability probably affect operating performance.
  3. **Interpretation**: mostly qualitative data; a simple average of ESG measures into one score can be limiting and misleading.
- **ESG approaches over time**: exclusion (1970s-80s), best-in-class (more recent: only firms above a threshold are investable), and, for a minority of managers, explicit inclusion of ESG in cash-flow forecasts or the cost of capital (growing).
- **Evidence on materiality**: Khan, Serafeim and Yoon (2016): best performance (1993-2013) from firms strong on **material** issues and weak on immaterial ones; worst from firms weak on material issues regardless of immaterial score. This is read as the first empirical proof that material non-financial information creates long-run investor value.
- **BANOR SIM-Politecnico di Milano study (STOXX Europe 600, 2012-2017)**
  - Sample: 882 firms; data: Datastream (prices), Worldscope (financials), Thomson Eikon (434 ESG variables).
  - Method: map the 434 variables to SASB's materiality map (30 categories of sector-specific indicators); keep sector-material variables; weight; final ESG score = weighted average of E, S, G by sector relevance. Each 30 June (2012-2017), rank firms into three portfolios (top quartile = high ESG, bottom quartile = low).
  - Results: (a) high-ESG portfolio outperformed the other two with a similar standard deviation; (b) single-pillar sorts (E, S or G alone) did **not** reproduce the result: strength in one pillar does not offset weakness in the others; (c) sources of outperformance: higher revenue growth, better operating-margin change (EBIT/sales), and higher average dividend yield; (d) among three stock-selection models - P/E value only, ESG only, combined - the **combined** model beat the others by about 1 percentage point a year.
  - Caveats: evidence on materiality is limited and recent; sample and period short; treat as supportive, not conclusive.

## Key Concepts
- **Intrinsic value**: estimated long-run fundamental value.
- **Margin of safety**: discount of price to intrinsic value.
- **Moat**: durable competitive advantage.
- **Net-net**: current assets net of liabilities below market price (Graham).
- **Capital-light business**: business model with few balance-sheet assets and mostly intangible value.
- **Externalities**: costs or benefits imposed on third parties and not priced by the company.
- **Greenwashing**: presenting marginal or cosmetic initiatives as sustainability performance.
- **Materiality (SASB)**: ESG information likely to affect operating performance in a given industry.
- **Material vs immaterial ESG issues**: issues that do or do not matter financially for the sector.
- **EBIT margin**: EBIT divided by sales.

## Formulas & Reference Tables
- Margin of safety `= (V_intrinsic - P) / V_intrinsic`.
- ESG score in the study `= sum_pillar w_pillar,sector * S_pillar`, where S_pillar is the weighted material-variable score of E, S or G and weights reflect sector relevance.

| Year | Tangible share of market cap | Intangible share |
|---|---|---|
| 1975 | 83% | 17% |
| 1985 | 68% | 32% |
| 1995 | 32% | 68% |
| 2005 | 20% | 80% |
| 2015 | 16% | 84% |

## Mental Models
- Use ESG as a moat detector: strong material-issue management is evidence of a durable advantage.
- Use sector materiality (SASB) to decide which ESG variables enter the score; ignore the rest.
- Use ESG as a quality overlay on cheap stocks: value alone catches traps; value plus ESG screens for sustainability of earnings.
- Use all three pillars: a high score in one pillar does not replace weakness elsewhere.

## Worked Example
**Margin of safety with an ESG adjustment (illustrative, not from the source).** A value analyst estimates intrinsic value at 100 for a firm priced at 70: margin of safety = 30%. Governance review reveals related-party dealings that the analyst judges to cut sustainable cash flows by 15%, so intrinsic value is 85 and margin of safety = (85 - 70)/85 = 17.6%.
- Interpretation: the ESG finding shrinks the cushion by 12 points; if the required margin is 25%, the stock fails the screen.

## Anti-patterns
- Using raw, self-reported ESG numbers without checking for greenwashing.
- Averaging E, S, G into one number for all sectors.
- Letting a strong environmental score offset poor governance.
- Treating tangible-asset multiples as sufficient for capital-light firms.
- Claiming causality from a short sample.

## Practitioner Notes
- The authors argue that managers who analyze non-financial information well and build ESG know-how will produce higher returns; the practical edge is in the quality of the process.
- Build sector materiality maps once and apply them consistently; keep a record of which variables drive each sector's score.
- Combine rankings: a value rank and a material-ESG rank, not only one of them.
- The white paper is freely available (BANOR SIM site) per the source.

## Key Takeaways
1. Value investing is price versus intrinsic value with a margin of safety.
2. Intangibles are now over 80% of market cap, so moat analysis and non-financial data matter.
3. ESG data carry greenwashing, standards and interpretation problems.
4. SASB materiality focuses the analysis on what moves operating performance.
5. Evidence (Khan-Serafeim-Yoon; BANOR-Polimi) links material ESG to outperformance.
6. High-ESG outperformance came from revenue growth, margin and dividends; no single pillar replicates it.
7. P/E plus ESG selection beat either alone by about 1 pp a year in the STOXX Europe 600 sample.

## Connects To
- **ch20**: ESG integration as a strategy.
- **ch23**: ratings and data sources.
- **ch24**: KPI problems and SASB/GRI context.
- **ch26**: how a small company can disclose material non-financial information.
- **`cfasi-equity-investment-styles` ch01-ch05 (value investing guide)**: value process and factor framing.
- **`cfa-equity-portfolio-management`**: active equity management and style.
