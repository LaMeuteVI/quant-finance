# Patterns — Equity Investment Styles Recipes

## Margin-of-Safety Purchase Test
**When to use**: deciding whether a cheap stock is a buy.
**How**: 1. Estimate V conservatively (several multiples, DCF with normalised rates). 2. Require price below V x (1 - MoS), MoS 20-33%, larger when visibility is poor. 3. Stress V by 10% (earnings miss) and check the discount survives. 4. Ask whether the price fall reflects impaired assets (then no margin exists). 5. Re-analyse losers case by case; sell when price clearly exceeds V.
**Trade-offs**: V is an estimate; a 5% margin disappears with a 10% miss. (ch 01, 02)

## Value Trap Diagnosis
**When to use**: low P/B or P/E on a stock or whole sector (banks, energy).
**How**: 1. Compute justified P/B = (ROE - g)/(K - g); if ROE or K moved, the discount may be fair. 2. Check ROE trend, dividend cuts, leverage and industry share loss. 3. Place the sector on the Perez cycle: installation-phase incumbents are traps, mature leaders become value. 4. Add a profitability or Piotroski filter. 5. For banks, reclassify the balance sheet; do not trust P/B.
**Trade-offs**: filters shrink the universe and can exclude true turnarounds. (ch 03, 04, 05)

## Owner-Earnings Screen
**When to use**: comparing firms with different capex needs (non-financials).
**How**: OE = NI + D&A +/- non-cash - average maintenance capex +/- working capital; rank on P/OE; use sector long/short or sector-neutral baskets; judge management by dollar of value created per dollar retained.
**Trade-offs**: maintenance capex is an estimate; the guide's test was simple and cost-free. (ch 04)

## Overprice Recovery Test
**When to use**: paying above book value.
**How**: split price into book and overprice; project book growth plus dividends; accept if the overprice is absorbed in about 8-10 years (equity cash-flow duration 8-12 years).
**Trade-offs**: needs stable ROE; ignores intangibles that understate book. (ch 03)

## Two-Phase Multifactor Stock Selection
**When to use**: building a value-core book without value traps.
**How**: 1. Value each name with fundamental methods. 2. Score sector-relative z-scores on Value, Growth, Momentum, Quality (weights equal or cycle-driven). 3. Buy best composite, equal-weighted, monthly rebalance. 4. Neutralise country and size bets. 5. Choose the valuation multiple per sector by backtest.
**Trade-offs**: crowding and decay of public factors; weights by cycle phase are backtests. (ch 05, 12)

## Systematic Stock-Selection Build (4 steps)
**When to use**: designing or auditing a quant equity model.
**How**: 1. Pick factors with economic rationale and low mutual correlation. 2. Define each with several metrics (Value: forward P/E, FCF yield, P/B, dividend yield). 3. Convert metrics to distance-aware scores (min-max or winsorised z) and average equally. 4. Choose structure: long-only, long vs market, long/short. Monthly rescoring, top 50 / bottom 50. Use point-in-time data and cost-aware turnover.
**Trade-offs**: shorting cost and capacity; the premium varies after 2008. (ch 12)

## Five Tests of a Genuine Factor
**When to use**: before adding any factor to a portfolio.
**How**: persistent, pervasive across countries, robust to definitions, economically sensible, investable after costs; demand low correlation to existing factors; haircut by about 58% for post-publication decay; use higher t-ratio hurdles after data mining.
**Trade-offs**: strict tests reject genuine but young factors. (ch 06)

## Smart-Beta Weighting Choice
**When to use**: selecting or building a factor index.
**How**: equal weight when inputs are untrustworthy; DRW w ~ 1/sigma with equal correlations; ERC for risk parity; Maximum Decorrelation for identical volatilities; Efficient Min Vol for defensiveness; Max Sharpe only with reliable expected returns. Set rebalancing frequency between drift and cost.
**Trade-offs**: more inputs, more estimation risk. (ch 06)

## Regime-Aware Factor Tilt
**When to use**: setting small tactical factor tilts around a neutral mix.
**How**: classify with growth (CLI) and inflation acceleration into Heating Up, Goldilocks, Stagflation, Slowing Growth; hold the market in Heating Up, Quality and Value-Weighted in Goldilocks, Minimum Volatility in Stagflation, Quality, Momentum and Min Vol in Slowing Growth; use expected regime duration 1/(1 - P_ii) and transition probabilities; tilt on forecasts.
**Trade-offs**: regime is known late; most alphas are insignificant; style correlations 0.60-0.95. (ch 05, 07, 08)

## Factor Mix Core-Satellite
**When to use**: implementing factors with a fund budget.
**How**: passive factor mix (Value, Quality, Momentum, Min Vol, equal weight) for the directional core; active multi-factor long/short multi-asset funds as diversifying satellite; neutral risk-parity factor weights with limited tilts.
**Trade-offs**: long-only factors carry market beta; the 60/40 vs combined test (0.48 vs 1.02 return/risk) is a flattering 2000-2017 window. (ch 08)

## Factor Fund Due Diligence (Five Pillars)
**When to use**: selecting active factor or quant funds.
**How**: Parent (history in systematic investing, not back-test launches); Process (global, cost-net evidence, few indicators per factor); People (research function); Price (turnover, netting, direct execution vs swap fees above 50 bps); Performance (correlation to equity and hedge-fund indices, skew, kurtosis, drawdown in 2007 and 2018).
**Trade-offs**: qualitative judgement needed. (ch 08, 10)

## Systematic vs Discretionary Classification
**When to use**: comparing funds or blending managers.
**How**: classify on process (flexible vs pure), breadth (concentrated vs diversified), relative risk; compare on information ratio, not return; use Fabozzi-Focardi-Jonas labels (fundamental, quantitative, hybrid); blend for low correlation.
**Trade-offs**: mixed data sets give conflicting studies. (ch 09, 10)

## Hybrid Quant Toolkit
**When to use**: a fundamental team with limited quant capacity.
**How**: screen out the most indebted, expensive and smallest names; rank on composite criteria (Magic Formula rank sum of EY and ROC; Piotroski F-score 8-9 long, 0-1 short); add stop-loss and take-profit rules.
**Trade-offs**: back-tests are period-specific and pre-cost. (ch 10)

## Pre-Committed Exit Rules
**When to use**: self-directed or advised clients prone to disposition effect.
**How**: map bias to phase (entry: selection rules; exit: orders). Fix stop `P <= P_entry x (1 - s)` and target `P >= P_entry x (1 + g)` as working orders; add rebalancing bands; combine with education.
**Trade-offs**: whipsaws in ranges; rule design inherits designer bias; evidence is asset-specific. (ch 10, 11)

## Index-vs-Label Look-Through
**When to use**: any factor or thematic product.
**How**: read the rulebook (revenue threshold at 50%, weighting, committee), replication type, top-10 weight, GICS, country and cap mix, correlation to the tech index, swap counterparty; compare two ETFs on methodology before cost.
**Trade-offs**: effort; index changes. (ch 08, 12, 13, 21)

## Thematic Sleeve Construction
**When to use**: adding a thematic satellite.
**How**: default to an equal-weight basket of themes rebalanced monthly or quarterly; cap single-theme and overlapping themes (AI, robotics, cloud, Digital Economy); read beta, correlation and drawdown dates together; use Sortino for skewed themes; treat emerging-theme history as non-statistical.
**Trade-offs**: 5-year windows reflect the 2019-2021 boom; correlations rose in 2020. (ch 13, 14, 17, 21)

## Enabler-Chain Theme Analysis
**When to use**: judging a technology or energy-transition theme.
**How**: map the chain (cost deflation, platforms, application; or policy, cost, demand, bottleneck). Robotics: talent, compute, sensors. EV: regulation to battery cost to lithium. Hydrogen: colour, electrolyser, electricity, carbon price. Choose the low-regret layer (lithium across chemistries) or picks-and-shovels. Run sensitivity of end cost to raw-material price.
**Trade-offs**: policy dependence and execution risk for juniors. (ch 14, 19, 20)

## Climate Filter then Theme
**When to use**: integrating climate in a portfolio.
**How**: 1. Score transition risk with forward-looking scores (laggard below 50, opportunity above 75). 2. Tilt the whole book. 3. Add a revenue-based SDG 13 or climate theme. 4. Engage on disclosure (TCFD).
**Trade-offs**: vendor scores disagree; strict SDG screens keep about 10% of the universe. (ch 18)

## EM Exposure Decomposition
**When to use**: sizing EM equity or debt.
**How**: compare market-cap weight (13%) with GDP (39%) and revenue (42%) weights; decide hard vs local currency before countries; compute FX volatility as sqrt(unhedged vol^2 - hedged vol^2); check China (about 38%) and sector concentration; budget for -65% drawdown risk.
**Trade-offs**: classification lists are dated; hedging costs. (ch 22, 23, 24)

## EM Sovereign ESG Overlay
**When to use**: country selection in EM debt.
**How**: start from macro-financial ratios, add PRI factor lists with higher weights on governance and social factors; test against CDS spreads; do not average rating agencies without checking methodology.
**Trade-offs**: ratings diverge; reporting gaps. (ch 24)

## Fund-Selection Funnel
**When to use**: choosing among many funds in one category (EM equity example).
**How**: universe (about 700) → quantitative screen on currency, UCITS, age, AUM (about 100) → short list by simple rule (6) → verify mandate, KIID, factsheet geography → relative country, sector and factor tables → correlations and attribution → qualitative review → complementary combination of low-correlation funds (about 0.8 is good).
**Trade-offs**: "beat the benchmark three years" is naive; one outlier year can drive the information ratio. (ch 25)
