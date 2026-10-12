# Chapter 10: Destination Quant: Types of Quantitative Strategies, Performance and Crowding Risk
> **Source**: CFA Society Italy × Advisor Private, *Systematic Investments* guide (2019), Ch. 2 "Destinazione quant" | Marianna Longo, CFA; plus sponsor insert "Irrazionalità prevedibile o disciplina negli investimenti" (GAM, attributed where used)

## Core Idea
A **quant** manager starts from historical data, tests a rule repeatedly and automates it to generate excess return; a **fundamental** manager starts from an idea and builds the portfolio name by name. Quant strategies are many (factor, risk parity, systematic macro, arbitrage, CTA), so "quant" is a method, not one risk exposure. The chapter's practical message: quant funds delivered lower volatility than hedge funds on average but are exposed to **model decay and crowding** (the 6-10 August 2007 episode, a weak 2018), and fundamental managers can borrow quant tools to form a **hybrid process**.

## Frameworks Introduced
- **Fabozzi-Focardi-Jonas (2008) process taxonomy**
  - What: classifies a process as *fundamental* (judgement and intuition), *quantitative* (fixed rules) or *hybrid* (mix).
  - When: first step of any due diligence on how decisions are made.
  - How: ask "who or what takes the final decision, and can it be written as a rule?". A fundamental manager running an Excel screen to shrink the universe is hybrid.
  - Failure mode: labelling by marketing; many "fundamental" funds are hybrid and many "quant" funds have discretionary overrides.
  - Metaphor from the source: fundamental managers are snipers, quants fire bursts where history says to fire.
- **Quant strategy map** (the guide's list, after Bloomberg):
  | Strategy | Logic | Typical holding / note |
  |---|---|---|
  | Factor model | Independent variable (P/E, inflation, unemployment change, momentum, sentiment, put/call open interest, revisions) explains a dependent variable (index, currency, bond index, commodity, VIX) | Most common hedge-fund quant approach |
  | Risk parity | Equal risk, not equal capital, per asset class (equity, bonds, inflation-linked); weight inversely to volatility; recompute vol and rebalance monthly | Diversification against market swings |
  | Systematic global macro | Inflation, unemployment, consumption linked to market moves; e.g. carry trade (short low-yield currency, long high-yield currency) | Macro data, rule-based |
  | Event-driven arbitrage | Mispricing around events (analyst estimate cuts, buybacks, bankruptcies, pre-earnings run-up) | Days to weeks, shortest of the group |
  | Statistical arbitrage | Pairs or baskets that normally co-move; sell the one that rose, buy the one that fell, wait for realignment (guide's example: Coca-Cola vs PepsiCo) | Bets on overreaction then mean reversion |
  | CTA (trend following) | Buy futures near the 50-day high, sell near the 50-day low (guide's example) on equity index, currency, commodity | Days to weeks; one of the most volatile quant styles; only 30-50% of trades profitable but winners are large |
- **Factor-model inputs by asset class**: equity (value multiples such as P/E, EV/EBITDA; size; sector; volatility; momentum), bonds (industrial production, employment growth, inflation vs trend; maturity; rating; leverage ratios such as interest coverage and net debt/EBITDA), cross-asset (sentiment, revisions to analyst or economist estimates).
- **Hybrid-process toolkit** (how fundamental managers borrow quant steps): (1) speed up analysis with a quantitative first screen (drop the most indebted, most expensive, smallest names); (2) support the decision with technicals or stop-loss/take-profit rules; (3) apply several criteria at once with a composite score.
  - **Greenblatt "Magic Formula"**: rank the universe on earnings yield and on return on capital, sum the two ranks, buy the best aggregate (30 stocks from the 2,500 largest by market cap). Guide-reported result: about +24% a year vs about +12% for the S&P 500, 1987-2004 (back-test reported by the author, not an independent out-of-sample result). **⚠ Correction**: the guide calls the quality leg "ROE"; Greenblatt's original uses return on capital (EBIT / (net working capital + net fixed assets)) and earnings yield = EBIT / enterprise value.
  - **Piotroski F-score** (2000): 9 binary tests, one point each. Profitability (4): ROA > 0, operating cash flow > 0, ROA up vs prior year, operating cash flow > net income. Leverage/liquidity/source of funds (3): leverage down, current ratio up, no new shares issued. Operating efficiency (2): gross margin up, asset turnover up. Buy high scores (8-9), short low scores (0-1) among cheap (high book-to-market) stocks; guide reports about +23% a year market-adjusted for the long-short, 1976-1996. **⚠ Correction**: the guide's text first describes a 1-100 score where "the lowest" is chosen; this contradicts the 0-9 scale it states a few lines later. The F-score is 0-9 and higher is better.
  - **Stop loss** (Klement, 2013 evidence): cuts volatility reliably and counters the disposition effect (selling winners early, keeping losers) and loss aversion; raised performance vs buy-and-hold for MSCI US, MSCI UK and US REITs, but not for commodities, gold or emerging equities. Gains depend on re-entry rules and market regime.

## Key Concepts
- **Quant (quantitative) process**: decisions follow fixed rules derived from tested data; less supervision, no emotions, no tiredness, no occasional errors (only systematic ones).
- **Factor model**: regression-style link between explanatory variables and an asset's return or risk.
- **Risk parity**: allocation by contribution to risk instead of capital; low-vol assets receive higher weight.
- **Carry trade**: fund in a low-rate currency, buy higher-rate currency assets.
- **Statistical arbitrage**: market-neutral convergence bet on temporarily dislocated related securities.
- **CTA / trend following**: position taken after a price trend is observed (breakout rule).
- **Crowding**: too many models concentrated on few anomalies, so exits are correlated.
- **Death spiral (Khandani-Lo hypothesis)**: forced deleveraging of similar positions causes losses that force more selling.
- **Market-neutral**: beta of zero by construction, which does not make the fund immune to common-factor liquidation.
- **Model decay**: historical factor-return relationships may stop, be nonlinear or miss new events.
- **Disposition effect / loss aversion**: behavioural reasons a stop-loss rule helps.
- **Hybrid process**: fundamental process with quantitative screens or scores.

## Formulas & Reference Tables
- Magic Formula score for stock *i* among *N*: `Score_i = Rank_EY,i + Rank_ROC,i` (rank 1 = best; lowest sum wins). `EY = EBIT / EV`, `ROC = EBIT / (NWC + net fixed assets)`.
- Piotroski: `F = Σ (9 binary signals)`, `0 <= F <= 9`.
- Risk parity weight (simple inverse-volatility form): `w_i = (1/σ_i) / Σ_j (1/σ_j)`. Full risk parity uses equal risk contributions and needs the covariance matrix; inverse-vol is exact only if correlations are equal.
- Guide performance data (HFR via Financial Times): ten-year average annual return quant hedge funds +2.0% vs all hedge funds +2.8%; annualised volatility 3.9% vs 6.0%; quant hedge fund assets about USD 950bn (2018, chart scale to USD 1,000bn); 2018 return -3.5% vs -3.9% in 2008; possible first outflow since 2009, over USD 8bn. 2007: month-to-date losses of quant funds ranged from -5% to -30%; the S&P 500 was -3% on 9 August, followed by a strong rebound on 10 August.

## Mental Models
- Use **"burst vs sniper"** to explain the trade-off: many small, rule-driven bets vs few researched ones.
- Use **"same label, different risk"** to split a quant allocation: trend followers, stat-arb and risk parity respond to opposite market conditions.
- Use **crowding as a correlation test**: if all your quant funds hold the same anomaly, their drawdowns will line up even when they claim market neutrality.
- Use **hybrid first** when a team has no quant capacity: an Excel-level screen plus a composite score already removes the worst names.
- Use **stop loss as risk control first, return enhancer second**.

## Worked Example
Inverse-volatility weights for three assets with volatilities equity 16%, bonds 4%, inflation-linked 8% (illustrative).
- `1/σ`: 6.25, 25.0, 12.5; sum = 43.75.
- Weights: equity **14.3%**, bonds **57.1%**, inflation-linked **28.6%** (sum 100%).
- Interpretation: capital is bond-heavy but each leg contributes similar risk if correlations are comparable. This is why risk parity often uses leverage to reach a target return, and why a rise in bond vol forces monthly de-risking.

Magic Formula toy ranking: stock A (EY rank 10, ROC rank 40) = 50; stock B (EY 30, ROC 15) = 45. B is selected despite being worse on earnings yield; the combined rank rewards cheap AND profitable.

## Anti-patterns
- Reading the ten-year average (+2.0% vs +2.8%) as proof quants "underperform": the figure is for hedge-fund quant indices with lower volatility (3.9% vs 6.0%), so risk-adjusted they were not worse.
- Treating "market neutral" as "no common risk": August 2007 showed shared factor risk.
- Using a static factor set without monitoring decay.
- Quoting the Magic Formula or Piotroski back-tests as expected live returns (period-specific, pre-cost, publication effects).
- Adding a stop loss to any asset class on faith; evidence is asset-specific.

## Practitioner Notes
- Due-diligence list: signal family, holding period, turnover, capacity, overlap with peer strategies, behaviour 6-10 Aug 2007 and 2018, exit/liquidity plan.
- Sponsor insert (GAM): argues humans are 25% finance and 75% psychology (a popular claim presented by the sponsor without a rigorous source; treat as a motivational statement). Its credible content is the bias list: loss aversion (Kahneman-Tversky 1979), recency, herding (value managers buying technology in the late 1990s), overconfidence, confirmation bias. Chapter 11 develops these.
- Some quants (Man Numeric, 2018) test replicating private-equity-like returns with listed small caps at lower cost; a listed proxy shares liquidity risk of small caps and does not replicate PE illiquidity premium.

## Key Takeaways
1. Fabozzi-Focardi-Jonas: fundamental, quantitative, hybrid; classify first.
2. Six main quant families with very different holding periods and risk drivers.
3. Quant hedge funds: about USD 950bn, lower volatility than hedge funds overall, weaker 2018.
4. August 2007: a common-factor deleveraging spiral hit market-neutral and long-only funds; correlations between quant and other hedge-fund styles rose.
5. Risks: relationships may not persist, nonlinearities are missed, static factor sets fail in new regimes.
6. Fundamental managers can borrow quant tools (screens, composite scores, Piotroski, stop loss) without becoming systematic.

## Connects To
- **ch09**: definitions and myths about systematic investing.
- **ch11**: behavioural biases that rules aim to remove.
- **ch12**: how a factor model for stock selection is built.
- **ch01-ch05** (Value Investing guide): Greenblatt and Piotroski as quantitative value screens; ch05 covers Piotroski quality in value.
- **`cfa-equity-portfolio-management`**: quantitative and active equity strategies.
