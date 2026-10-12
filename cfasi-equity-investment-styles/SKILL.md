---
name: cfasi-equity-investment-styles
description: "CFA Society Italy x Advisor Private practitioner guides on equity investment styles (2018-2021, 25 chapters, translated from Italian): Value Investing, Factor Investing, Systematic Investments, Thematic Investments (robotics, healthcare, cyber, AI, climate, EV, hydrogen) and Emerging Markets (equity, EM debt, fund selection). Use when screening or judging value stocks, building factor or smart-beta portfolios, designing quant stock selection, assessing thematic funds, or sizing EM exposure. Terms: margin of safety, owner earnings, value trap, HML, P/B and ROE, smart beta, factor zoo, Markov-Switching regimes, Piotroski F-score, de-biasing, thematic ETF, MSCI EM, hard vs local currency debt."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Society Italy Equity Investment Styles Guides (Value, Factor, Systematic, Thematic, Emerging Markets)
**Source**: CFA Society Italy x Advisor Private practitioner guides: Factor Investing (2018), Systematic Investments (2019), Value Investing (2020), Thematic Investments (2021), Emerging Markets (2021), by Italian CFA charterholders and practitioners | **Domain**: Gestion de portefeuille | **Chapters**: 25 | **Generated**: 2026-10-08

## How to Use This Skill
- **Without arguments**: load the core frameworks below and the cheatsheet for decision rules.
- **With a topic**: ask about `<topic>` (for example "value trap" or "hydrogen"); I find it in the Topic Index and read the chapter before answering.
- **With a chapter**: ask for `ch12`.
- **Browse**: "what chapters do you have?"

When a topic is not covered in Core Frameworks, I read the relevant chapter file before answering. Chapter groups: ch01-ch05 Value Investing, ch06-ch08 Factor Investing, ch09-ch12 Systematic Investments, ch13-ch21 Thematic Investments, ch22-ch25 Emerging Markets. This is a book/guide skill: it carries practitioner decision rules and no exam content.

---

## Core Frameworks & Mental Models

**Value**
- **Investor vs speculator and margin of safety** (ch01, ch02): the investor values the business; buy only below V x (1 - MoS), `MoS = 1 - P/V`, rule of thumb 20-33%. A 10% earnings miss erases a 5% margin; the discount must not come from impaired assets.
- **Graham defensive screen** (ch01): P/E <= 15 on 3-year earnings, P/B <= 1.5 (combined P/E x P/B <= 22.5), assets >= 2x debt, 10 years of profits and dividends; guidelines, not cut-offs. Formula `V = E(8.5 + 2g) x 4.4/Y` is a sanity check only.
- **Multiples toolkit** (ch02, ch05): direct (yields) vs indirect (P/E, EV/EBITDA); triangulate with debt-aware multiples; choose the multiple per sector by backtest.
- **Justified P/B and value-trap test** (ch03): `P/B = (ROE - g)/(K - g)`. Low P/B with falling ROE is a trap; value x profitability (cheap and profitable) won in the US, developed ex-US and EM. Overprice should be absorbed by book growth plus dividends in about 8-10 years.
- **Owner earnings** (ch04): `NI + D&A +/- non-cash - maintenance capex +/- change in working capital`; rank on P/OE; do not trust P/B for banks.
- **Two-phase multifactor selection** (ch05): fundamental valuation, then composite z-score on Value, Growth, Momentum, Quality, rebalanced monthly; value needs a catalyst; value+momentum improves efficiency.

**Factor**
- **Factors, not labels** (ch06): return = macro exposure + style exposure + alpha; factor cross-correlation about 2% vs asset classes 39% (51% in turbulence). Five tests: persistent, pervasive, robust, economically sensible, investable; published premia fall about 58%.
- **Model ladder** (ch06): CAPM, APT, Fama-French three- and five-factor, Carhart; smart-beta weighting menu from equal weight to maximum Sharpe (more inputs, more estimation risk).
- **Four-regime map** (ch07): Heating Up, Goldilocks, Stagflation, Slowing Growth from growth and inflation acceleration; Goldilocks is the most persistent (6.6 quarters); expected duration `1/(1 - P_ii)`.
- **Purity vs investability** (ch08): academic long/short factors vs long-only indices; factor mix (Value, Quality, Momentum, Min Vol) beats timing; Five Pillars due diligence (Parent, Process, People, Price, Performance).

**Systematic**
- **Systematic vs discretionary grid** (ch09): process purity, portfolio breadth, relative risk; compare on information ratio and blend.
- **Quant families and hybrid tools** (ch10): factor, risk parity, macro, event arbitrage, stat arb, CTA; Magic Formula and Piotroski F-score (0-9); crowding (August 2007).
- **Bias map and ex-ante exits** (ch11): rules cure emotional bias at exit (disposition, regret); cognitive and social bias survive in rule design.
- **Four-step stock-selection build** (ch12): factors, metrics, scores, structure (long-only, long vs market, long/short).

**Thematic**
- **Theme taxonomy and EW basket** (ch13): sustainable (E, S, G), technology, emerging; read beta, correlation and drawdown dates together.
- **Enabler chains** (ch14, ch19, ch20): cost deflation (robotics, 5G), policy to cost to demand (EV, lithium), colour and electrolyser cost (hydrogen).
- **Segment mix over headline** (ch15, ch16): healthcare seven-segment map; cybersecurity growth hidden by +33% cloud vs -12.6% network hardware.
- **AI test and climate triad** (ch17, ch18): sense-understand-act-learn; physical, transition, liability risk; climate filter before climate theme.
- **Index-vs-label look-through** (ch21): methodology, replication, GICS, country, cap; dispersion within a theme can exceed 100 points.

**Emerging markets**
- **Weight vs economy** (ch22, ch23): EM is 13% of ACWI cap, 39% of GDP, 42% of revenues; China about 38% of MSCI EM; five advantages vs four disadvantages.
- **EM debt segments** (ch22, ch24): hard vs local currency, sovereign vs corporate; FX is the bond; ESG weights higher on governance.
- **Fund-selection funnel** (ch25): 700 to 100 to 6; verify mandate and documents; complementary combination.

---

## Chapter Index
| # | Title | Guide · Capitolo | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-value-investing-introduction.md) | Value Investing: An Introduction | Value · 1 | Margin of safety, Mr. Market, Graham screen |
| [ch02](chapters/ch02-a-story-of-value.md) | A Story of Value | Value · 2 | Two pillars, direct/indirect multiples, stress test |
| [ch03](chapters/ch03-value-investing-and-value-premium.md) | Value Investing and the Value Premium | Value · 3 | HML, P/B-ROE, overprice test, Perez cycle |
| [ch04](chapters/ch04-value-shareholders-owner-earnings.md) | Value Shareholders: Owner Earnings and Banks | Value · 4 | Owner earnings, P/OE screen, structured margin |
| [ch05](chapters/ch05-value-and-the-multifactor-approach.md) | Value and the Multifactor Approach | Value · 5 | Two-phase scoring, cycle table, catalyst |
| [ch06](chapters/ch06-factor-investing-new-asset-allocation.md) | Factor Investing: A New Asset Allocation | Factor · 1 | Factor tests, FF models, smart-beta weights, bond factors |
| [ch07](chapters/ch07-factor-investing-and-the-global-economic-cycle.md) | Factors and the Global Economic Cycle | Factor · 2 | Markov-Switching regimes, style behaviour |
| [ch08](chapters/ch08-factor-strategies-active-and-passive.md) | Factor Strategies: Active and Passive | Factor · 3 | Purity ladder, factor mix, Five Pillars |
| [ch09](chapters/ch09-systematic-origins-and-peculiarities.md) | Origins and Peculiarities of Systematic Investing | Systematic · 1 | Systematic vs discretionary grid, myths vs limits |
| [ch10](chapters/ch10-systematic-destination-quant.md) | Destination Quant | Systematic · 2 | Process taxonomy, quant families, Magic Formula, Piotroski |
| [ch11](chapters/ch11-systematic-behavioral-de-biasing.md) | Systematic Investing as De-biasing | Systematic · 3 | Bias map, ex-ante stops |
| [ch12](chapters/ch12-systematic-factor-investing-and-stock-selection.md) | Factor Investing and Stock Selection | Systematic · 4 | Four-step build, composite scores |
| [ch13](chapters/ch13-thematic-universe-analysis.md) | Analysis of the Thematic Universe | Thematic · 1 | Taxonomy, risk-return kit, EW basket |
| [ch14](chapters/ch14-thematic-robotics-automation-and-5g.md) | Robotics, Automation and 5G | Thematic · 2 | Enabler stack, Moore's Law, 5G specs |
| [ch15](chapters/ch15-thematic-healthcare-innovation.md) | Healthcare Innovation | Thematic · 3 | Seven-segment map, genome cost curve |
| [ch16](chapters/ch16-thematic-cybersecurity.md) | Cybersecurity | Thematic · 4 | Driver map, segment growth |
| [ch17](chapters/ch17-thematic-artificial-intelligence.md) | Artificial Intelligence | Thematic · 5 | Sense-understand-act-learn, three clusters, correlation test |
| [ch18](chapters/ch18-thematic-climate-change.md) | Climate Change: Risk to Opportunity | Thematic · 6 | Risk triad, transition scores, SDG screen |
| [ch19](chapters/ch19-thematic-electric-vehicles-battery-materials.md) | EV Growth and Battery Raw Materials | Thematic · 7 | Policy-cost-demand, cathode trade-off, lithium |
| [ch20](chapters/ch20-thematic-hydrogen.md) | The Potential of Hydrogen | Thematic · 8 | Hydrogen colours, value chain |
| [ch21](chapters/ch21-thematic-investable-universe-and-product-selection.md) | Investable Universe of Thematic Products | Thematic · 9 | Dispersion, methodology comparison, thematic as hedge |
| [ch22](chapters/ch22-em-definition-and-composition-of-emerging-markets.md) | Definition and Composition of Emerging Markets | EM · 1 | MSCI tests, weight vs GDP vs revenue, EM debt benchmarks |
| [ch23](chapters/ch23-em-equity-approach-and-differences-from-developed-markets.md) | EM Equity Approach | EM · 2 | Index history, five pros and four cons |
| [ch24](chapters/ch24-em-bonds-key-aspects-and-esg-sustainability.md) | EM Bonds and ESG | EM · 3 | Three EMD segments, PRI ESG lists |
| [ch25](chapters/ch25-em-equity-fund-selection-example.md) | EM Equity Fund-Selection Example | EM · 4 | Funnel, relative allocation, factor look-through |

## Topic Index
- **A-shares, Stock Connect** → ch23
- **Active vs passive factors** → ch08
- **AI, machine learning** → ch17
- **Benchmark and index methodology (thematic)** → ch21
- **Batteries, cobalt, lithium** → ch19
- **Behavioural biases** → ch11
- **Cheap multiples, EV/EBITDA, P/E** → ch02, ch05
- **Climate risk, SDG, transition scores** → ch18
- **Crowding, August 2007** → ch05, ch10
- **Cybersecurity** → ch16
- **Dispersion within themes** → ch21
- **Due diligence of factor funds** → ch08
- **EM bonds, hard vs local currency** → ch22, ch24
- **EM classification (MSCI)** → ch22
- **EM equity case** → ch23
- **ESG in sovereign credit** → ch24
- **Factor models (CAPM, APT, FF)** → ch06
- **Factor timing, regimes** → ch05, ch07, ch08
- **Factor zoo, data mining** → ch06
- **Fund selection funnel** → ch25
- **Graham, Dodd, Intelligent Investor** → ch01
- **Greenblatt Magic Formula** → ch10
- **Healthcare innovation** → ch15
- **HML, SMB, value premium** → ch03, ch06
- **Hybrid process** → ch10
- **Hydrogen** → ch20
- **Information ratio, tracking error** → ch08, ch09, ch25
- **Low volatility, minimum volatility** → ch06, ch07, ch08
- **Margin of safety** → ch01, ch02
- **Markov-Switching** → ch07
- **Momentum** → ch05, ch06, ch12
- **Mr. Market** → ch01
- **Owner earnings** → ch04
- **P/B and ROE** → ch03
- **Perez technological cycles** → ch03
- **Piotroski F-score** → ch05, ch10
- **Quant strategies (CTA, stat arb, risk parity)** → ch10
- **Robotics, 5G, Moore's Law** → ch14
- **Smart beta weighting** → ch06
- **Stop loss** → ch10, ch11
- **Systematic vs discretionary** → ch09
- **Thematic taxonomy and basket** → ch13
- **Thematic as hedge** → ch21
- **Value traps** → ch03, ch04, ch05
- **Value with catalyst** → ch05

## Supporting Files
- [glossary.md](glossary.md): key terms with definitions
- [patterns.md](patterns.md): techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md): decision rules, thresholds, tells

---

## Related Skills
- `cfa-equity-portfolio-management`: use for the CFA treatment of styles, smart beta and active-passive trade-offs.
- `cfa-equity-valuation`: use for DCF, multiples and residual income behind ch02, ch03.
- `cfa-portfolio-management`: use for factor models, behavioural finance and manager selection.
- `cfa-asset-allocation-cme`: use for capital-market expectations and cycle scenarios (ch07).
- `cfasi-portfolio-construction`: use for passive, fund selection and ESG guides that complement ch08, ch21, ch25.
- `cfasi-fixed-income-guides`: use for EM debt mechanics behind ch22, ch24.
- `cfa-financial-statement-analysis`: use for quality of earnings and cash-flow adjustments (ch04).
- `cfa-quantitative-methods`: use for regime switching, skewness and kurtosis.

## Scope & Limits
Covers five Italian practitioner guides published by CFA Society Italy with Advisor Private (2018-2021); the source is Italian and was translated to English, with named concepts kept. PDF tables were reconstructed from extracted text, and charts with illegible labels were used only where numbers were text-confirmed. Sponsor inserts (Invesco, GAM, Banor, CPR AM, Capital Group) are only briefly summarised and attributed as advocacy. Source errors found are flagged in the chapters (Margin-of-safety stress test in ch02, Sharpe in ch06, Piotroski scale and Magic Formula in ch10, Next Generation EU split in ch20, transition matrix orientation in ch07). Market data, index weights and country lists are dated 2018-2021 and illustrate mechanisms, not current levels. The guides are informational, not investment advice.
