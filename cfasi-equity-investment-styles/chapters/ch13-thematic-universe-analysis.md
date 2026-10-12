# Chapter 13: Analysis of the Thematic Universe: Taxonomy, Risk-Return and Multi-Theme Portfolios
> **Source**: CFA Society Italy × Advisor Private, *Thematic Investments* guide (2021), Ch. 1 "Analisi dell'universo tematico" | Francesco Mastroberardino; preface by Vafa Ahmadi (CPR AM, sponsor content, attributed)

## Core Idea
**Thematic investing** buys companies exposed to a structural, long-term growth trend (climate, ageing, digitalisation) rather than to a sector, region or style. The chapter maps about 26 themes, splits them into **sustainable** (ESG-linked), **non-sustainable (technology)** and **emerging** themes, and measures 5-year risk/return, correlation to MSCI World and tail risk using theme indices. Result: most themes beat the global equity index on risk-adjusted terms, behaviours differ strongly by group, and a **diversified equally weighted basket of themes** is the best default unless you have deep knowledge of a specific business.

## Frameworks Introduced
- **Theme taxonomy (by ESG link)**
  | Group | Themes (index logic) | ESG factor |
  |---|---|---|
  | Sustainable, E | Climate Change (large/mid-cap developed, CO2-weighted); Water (50 global water firms); Battery (battery makers plus metal miners); Circular Economy (50 largest circular-economy names); Blue Economy (50 ocean-related, e.g. offshore wind); Smart Cities (equal weight across sub-themes: mobility, security, health, connectivity, waste, e-commerce); Sustainable Food (revenue majority from theme); Clean Energy (clean generation plus equipment) | Environmental |
  | Sustainable, S | Ageing Population (at least 50% of revenue linked, ESG and liquidity filters); Wellness (equal weight across health-related sectors); Human Development (companies with social, environmental or governance practices) | Social |
  | Sustainable, G | Gender Equality (weighted by a score on 19 gender-equality criteria) | Governance |
  | Non-sustainable (tech/consumption) | Artificial Intelligence; Cloud; Digital Security (at least 50% revenue, liquidity filter); Gaming (at least 50% revenue); Robotics; Big Data; Healthcare Innovation; Blockchain (committee-based discretionary inclusion); Digital Economy; E-commerce; Millennials; Smart Factory | none by design |
  | Emerging | Hydrogen (production, storage, distribution, transport, use); 5G | none (short track record) |
  - How to use: before comparing two "thematic" funds, identify the index logic (revenue threshold, equal vs score-weighted, committee), because exposures differ.
- **Risk-return analysis kit** (assumptions): risk-free = 200-day moving average of the 10-year Bund yield, -0.51%; downside-deviation target = Italian 10-year inflation breakeven 1.05% a year; benchmark for beta and correlation = MSCI World; 5-year window; VaR 95% parametric on a quarterly horizon; max drawdown with start/end dates and rebound from the low; 3-year rolling correlation of monthly returns (1-year for emerging themes).
- **Four-quadrant map** (return vs volatility relative to MSCI World): Q1 higher return and higher vol; Q2 higher return and lower vol (ideal); Q3 lower return and lower vol; Q4 lower return and higher vol (worst).
- **Multi-theme portfolio test**: equally weighted (1/n), monthly rebalanced baskets: all themes (ex emerging), non-sustainable, sustainable, environmental (E), social and governance (SG).

## Key Concepts
- **Theme**: investable structural growth trend cutting across sectors and countries.
- **Sustainable vs non-sustainable theme**: whether the theme has natural E, S or G content.
- **Equal-weighted index**: sub-themes weighted equally so each part of the theme is represented.
- **Revenue-threshold theme**: constituents must derive at least 50% of revenue from the theme (pure-play filter).
- **Sharpe ratio**: `(R - Rf)/σ`.
- **Downside deviation**: dispersion of returns below a target (here 1.05%).
- **Sortino ratio**: excess return over downside deviation; the guide's table uses `(R - Rf)/DD`, not target-based. **⚠ Correction (method note)**: the textbook Sortino uses `(R - MAR)/DD` with the same target as in DD; the table numerators use the risk-free rate (e.g. Climate Change 1.48 = (12.40+0.51)/8.72, while with MAR 1.05% it would be 1.30). Rank orderings are similar but levels are overstated.
- **Beta vs correlation**: beta near 1 can hide low correlation (Cloud, Healthcare Innovation); read both together.
- **Parametric VaR (95%, quarterly)**: loss threshold under normality; underestimates real tail in March 2020.
- **Max drawdown / rebound from low**: realised worst loss and recovery.
- **Rolling correlation**: 3-year window moved monthly.
- **Structural break**: the 5G history (negative to Dec 2018, strong 2019-2020) makes full-sample metrics unreliable.

## Formulas & Reference Tables
- `Sharpe = (R_ann - Rf) / σ_ann`; with Rf = -0.51%, Battery = (22.01 + 0.51)/19.78 = 1.14 (matches table).
- `Downside deviation = sqrt( mean( min(R_t - target, 0)^2 ) )`, target 1.05% a year.
- `VaR_95 (parametric) = -(μ - 1.645 σ)` over the horizon.
- **Sustainable themes, 5Y (Table 1)**: return / vol / Sharpe / beta / Sortino
  | Theme | Ret | Vol | Sharpe | Beta | Sortino |
  |---|---|---|---|---|---|
  | Climate Change | 12.40% | 13.56% | 0.95 | 1.00 | 1.48 |
  | Water | 9.95% | 12.12% | 0.86 | 0.78 | 1.21 |
  | Battery | 22.01% | 19.78% | 1.14 | 1.24 | 2.07 |
  | Circular Economy | 12.61% | 13.08% | 1.00 | 0.91 | 1.63 |
  | Blue Economy | 14.02% | 12.90% | 1.13 | 0.72 | 1.93 |
  | Smart Cities | 12.93% | 15.12% | 0.89 | 1.05 | 1.31 |
  | Sustainable Food | 7.17% | 11.11% | 0.69 | 0.67 | 1.01 |
  | Clean Energy | 25.97% | 23.16% | 1.14 | 1.04 | 2.02 |
  | Ageing Population | 8.01% | 15.46% | 0.55 | 1.07 | 0.77 |
  | Wellness | 15.17% | 10.63% | 1.47 | 0.58 | 2.61 |
  | Human Development | 5.16% | 11.91% | 0.48 | 0.76 | 0.70 |
  | Gender Equality | 10.01% | 14.19% | 0.74 | 1.01 | 1.10 |
  | MSCI World | 11.02% | 13.52% | 0.85 | 1.00 | 1.28 |
- **Technology themes, 5Y (Table 3)**: AI 28.92% / 19.78% / 1.49; Cloud 29.92% / 18.24% / 1.67; Digital Security 15.04% / 14.97% / 1.04; Gaming 38.61% / 16.57% / 2.36 (beta 0.68); Robotics 21.82% / 19.47% / 1.15; Big Data 28.01% / 25.32% / 1.13 (beta 1.39); Healthcare Innovation 36.88% / 18.89% / 1.98; Blockchain 31.90% / 20.34% / 1.59; Digital Economy 26.22% / 18.73% / 1.43; E-commerce 16.30% / 15.44% / 1.09; Millennials 23.32% / 16.64% / 1.43; Smart Factory 21.57% / 17.13% / 1.29. All sit in Q1.
- **Emerging (since index launch)**: 5G 14.73% / 16.88% / Sharpe 0.90 / beta 0.94; Hydrogen 73.59% / 36.25% / 2.04 / beta 1.46 (index starts Nov 2018; not a normal 5Y sample).
- **Tail risk (VaR 95% quarterly / max drawdown)**: MSCI World -8.47% / -19.78% (Jan-Mar 2020). Sustainable: Wellness -5.15% / -13.53% (best); Clean Energy -13.10% / -22.69%; Battery -11.17% / -21.21%; Ageing -10.77% / -25.81% (worst drawdown). Tech: most had worst loss in Q4 2018 (AI, Gaming, Robotics, Healthcare Innovation, Blockchain, Digital Economy, E-commerce) rather than Q1 2020. Rebounds from March 2020 low: Clean Energy +180%, Battery +111%, Hydrogen +222%, 5G +53%.
- **Equal-weighted baskets (Table 7)**: all themes 19.88% / 14.16% / Sharpe 1.44 / beta 1.00 / Sortino 2.45; non-sustainable 26.81% / 16.44% / 1.66 / 1.10 / 3.10; sustainable 13.14% / 12.68% / 1.08 / 0.90 / 1.68; E only 14.86% / 13.30% / 1.16 / 0.93; SG only 9.70% / 11.98% / 0.85 / 0.86 / 1.28 (equal to MSCI World on risk-adjusted terms). VaR of all baskets better than the index (-7.0% to -7.5% vs -8.47%).

## Mental Models
- Use **index logic first**: revenue threshold, weighting scheme and discretionary committees determine what you actually own.
- Use **beta plus correlation plus drawdown dates** together: Cloud and Healthcare Innovation show beta about 1 but low correlation and drawdowns on different dates.
- Use **Sortino/downside deviation for positively skewed themes** (Gaming: downside deviation under half of volatility) because standard deviation penalises up moves.
- Use **EW basket as default** for thematic sleeve when you cannot pick the winning theme: it ranked above most components (18 of 24 had a lower Sharpe).
- Use **short-history caution** for Hydrogen and 5G: annualised returns of 74% are not forecasts.

## Worked Example
Sharpe and Sortino check for Wellness: return 15.17%, vol 10.63%, downside deviation 6.01%, Rf -0.51%.
- Sharpe = (15.17 + 0.51)/10.63 = **1.475**, table 1.47 (matches).
- Sortino (table method) = 15.68/6.01 = **2.61**; with MAR 1.05% = 14.12/6.01 = **2.35**.
- Interpretation: Wellness is the most defensive theme (beta 0.58, best VaR), so it is attractive for smoothing a thematic sleeve, but its beta crept toward the market after 2020 (correlation rose).

## Anti-patterns
- Reading 5-year outperformance as a persistent edge: the window is dominated by 2019-2021 growth, ultra-low rates and a technology boom.
- Treating an emerging-theme backtest (Hydrogen from Nov 2018) as a risk estimate.
- Using parametric VaR as a tail guardrail: March 2020 realised losses were far above estimates.
- Assuming "sustainable theme" means low risk: Clean Energy and Battery are among the most volatile and deepest-drawdown themes; the S and G themes underperformed in the sample.
- Counting themes as diversifiers without checking correlation drift (rose in 2020 even for historically low-correlation themes).
- Index survivorship and look-ahead: theme indices are built after the theme became popular.

## Practitioner Notes
- Source includes a preface by CPR AM (sponsor) arguing growth factors are labour efficiency (education, ageing), technological progress, and risk factors (climate, inequality, food security, demography); this is advocacy, useful as a theme-selection grid (growth driver vs risk factor).
- The guide counts "24 themes" in the basket section and mentions "19 themes" in one drawdown comparison; treat the exact count as inconsistent in the source (the table-based universe is 12 sustainable plus 12 technology/consumption).
- Practical use: allocate thematic exposure as a satellite sleeve, EW across themes, rebalance monthly or quarterly, and cap single theme concentration.

## Key Takeaways
1. Themes cluster into sustainable (mostly environmental), technology/consumption, and emerging groups with different risk profiles.
2. Technology themes: higher return and higher volatility, low correlation, more drawdown in Q4 2018; sustainable themes: moderate excess return, high correlation, drawdown Q1 2020.
3. Social and governance themes underperformed; Wellness is the defensive exception.
4. VaR was optimistic in March 2020; correlations rose across themes.
5. A diversified EW theme basket beat most single themes on Sharpe and tail risk.
6. Use more than one metric and confirm with concept (Cloud and Healthcare Innovation: beta misleads).
7. Emerging themes (Hydrogen, 5G) have too little history for firm conclusions.

## Connects To
- **ch14-ch20**: single-theme deep dives (robotics, healthcare, cyber, AI, climate, EV/batteries, hydrogen).
- **ch21**: investable universe of thematic products (ETFs, funds).
- **`cfasi-portfolio-construction` ch20-ch30 (ESG guide)**: ESG integration behind sustainable themes.
- **ch06-ch08**: factor exposures that thematic indices implicitly carry (growth, momentum).
