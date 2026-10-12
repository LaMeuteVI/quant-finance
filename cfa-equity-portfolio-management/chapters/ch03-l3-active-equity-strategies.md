# Chapter 3: Active Equity Investing: Strategies
> **Source**: CFA Program Curriculum 2023, Level III, Reading 17 · Portfolio Management | Bing Li, PhD, CFA, Yin Luo, CPA, PStat, CFA, and Pranay Gupta, CFA

## Core Idea
Active equity management splits into fundamental (discretionary, judgment, depth on few stocks) and quantitative (systematic, factor models, breadth across many stocks). Within each, strategies are classed as bottom-up, top-down, factor-based, activist, statistical-arbitrage or event-driven. Value is added only if the investment thesis (what the opportunity is and why it exists) survives costs, behavioral biases (fundamental) or data-snooping, crowding and transaction costs (quantitative).

## Learning Outcomes Covered
- compare fundamental and quantitative approaches
- analyze bottom-up (value, growth, GARP), top-down (country, sector, style rotation, volatility, thematic), factor-based and activist strategies
- describe statistical arbitrage, market-microstructure and event-driven strategies
- describe how fundamental and quantitative strategies are created (process steps and pitfalls)
- discuss equity style classification (holdings-based, returns-based, self-identification)

## Frameworks Introduced
- **Fundamental vs quantitative comparison**: subjective/objective, discretionary/systematic, human judgment/statistical modeling, research/data, depth in a few names/breadth over many, forecasting future corporate parameters/pattern recognition on history, judgment sizing/optimizer.
  - When to use: classifying a manager in due diligence; deciding what risks to expect (company-level vs factor-level).
  - How: check number of holdings (~50 vs 400), rebalance trigger (continuous with target prices vs fixed calendar), who sizes positions (PM conviction vs optimizer), where risk is seen (stock vs portfolio).
  - Failure mode: labels are shorthand; hybrids exist (Asgard-type managers use quant tools and judgment). Fundamental managers' returns are often replicable by quant factors.
- **Seven-step fundamental process**: (1) define universe and investment thesis ("what is the opportunity and why is it there"); (2) prescreen; (3) industry and competitive analysis plus financial reports; (4) forecast cash flows/earnings; (5) convert to valuation (target price); (6) construct portfolio (over/underweights, sector stance); (7) rebalance with buy/sell discipline and stop-loss.
- **Quantitative process**: thesis, acquire and clean data, back-test (with IC), evaluate out-of-sample, portfolio construction with risk model and cost model, regular rebalancing.
- **Bottom-up taxonomy**: Value (relative value, contrarian, high-quality value, income, deep value, restructuring/distressed, special situations); Growth (growth, GARP).
- **Top-down taxonomy**: country/geographic allocation, sector/industry rotation, style (factor) rotation, volatility-based (VIX futures, straddles, variance swaps), thematic (structural vs short-term trends); implemented with futures, ETFs, swaps, baskets; also overlays to neutralise unintended macro bets.
- **Factor implementation methods**: hedged (quantile long/short) portfolio of Fama-French; factor-tilting long-only portfolio with controlled TE (enhanced-index-like); factor-mimicking portfolio (FMP: dollar-neutral, unit exposure to one factor, zero to others, theoretical).
- **Activist process**: identify target, buy stake (<10% typical), study structure and governance, submit proposals, threaten proxy contest, negotiate settlement or fight vote, exit or add.
- **Style analysis**: holdings-based (aggregate stock-level scores bottom-up), returns-based (Sharpe 1992 constrained regression on style indexes), manager self-identification; use both.

## Key Concepts
- **Rewarded vs unrewarded factors**: size, value, momentum, quality/profitability carry persistent premia; many others are used but unproven.
- **Value trap / growth trap**: cheap stock whose prospects keep deteriorating with no catalyst; growth stock whose growth arrives but price already discounts it (or fades after a low base).
- **Margin of safety (Graham and Dodd, 1934)**: buy at a significant discount to intrinsic value.
- **Contrarian**: relies on sentiment and price extremes (52-week lows) rather than fundamentals; targets depressed cyclicals.
- **High-quality value**: valuation plus consistent earnings power, above-average ROE, financial strength, good management (Buffett-style).
- **Deep value**: very low P/B in distress where information inefficiency is greatest; **restructuring/distressed**: counter-cyclical, aims at influence or control over discounted capital structures.
- **Special situations**: spin-offs, divestitures, mergers; needs legal and industry expertise.
- **GARP**: above-average growth at reasonable multiples; screen with PEG = (P/E) / (expected earnings growth in %).
- **Information coefficient (IC)**: correlation between factor scores (time t) and next-period returns across the cross-section; Pearson IC is outlier-sensitive, Spearman rank IC is robust; an average monthly IC of 5-6% is very strong for US equities.
- **Statistical arbitrage / pairs trading**: long the laggard, short the leader when the spread of two historically co-moving stocks is stretched, exit at mean reversion; main risk is a structural break.
- **Risk arbitrage (merger arbitrage)**: long target (cash deal), or long target and short acquirer at exchange ratio (share deal); profit is a deal spread, risk is deal failure; annualise the premium by deal duration.
- **Event-driven**: M&A, earnings and restructuring announcements, buybacks, special dividends, spin-offs.
- **Survivorship bias / look-ahead bias / data mining (overfitting)**: using only today's survivors; using data not yet published at the decision date; searching past data until a pattern fits.
- **Quant crowding**: many managers in the same trades (August 2007 "quant meltdown"); measured by short interest regressed on momentum (crowding coefficient).
- **Style classification dimensions**: characteristics-based (value/growth/core, size, volatility), membership-based (sector, country, developed/emerging), position-based (long/short, net long/short/neutral).
- **Morningstar Style Box**: 3x3 grid of size by value/core/growth; stocks are in exactly one box (1 or 0 membership); MSCI/FTSE Russell give fractional "value inclusion factors" (a stock with 0.6 value factor goes 60% to value, 40% to growth).
- **Activist defenses**: multi-class (multiple-vote) shares, poison pills, staggered boards, charter/bylaw provisions.

## Formulas & Reference Tables
`PEG = (P/E) / (expected EPS growth rate in %)`
`Normalized yield_t = Nominal yield_t − (1/12) Σ₁¹² Nominal yield_(t−i)` (12-month moving-average detrending of the rate variable)
`IC_Pearson = corr(factor score_t, return_(t→t+1))`; `IC_Spearman = Pearson corr of ranks`
`Returns-based style regression: rₜ = α + Σₛ βₛ Rₜˢ + εₜ, with Σβₛ = 1 and βₛ ≥ 0 for long-only`
`Covariance parameters to estimate = N(N+1)/2` (3,000 stocks → ~4.5 million, hence vendor risk models)
`Pairs spread = ln(P_A / P_B)`; entry at ±2σ from a rolling mean (130-day window in the example), exit at the mean.
`Value index membership: value score between 0 and 1; weight to value index = score × market cap`

| Fundamental | Quantitative |
|---|---|
| Subjective, discretionary | Objective, systematic |
| Research on company/industry/economy | Data and statistics |
| High conviction in few stocks (~50) | Many small factor bets (~400) |
| Forecast future earnings/cash flows | Mine historical patterns |
| Risk seen at company level | Risk seen at portfolio/factor level |
| Position sizing by judgment | Optimizer with risk and cost model |
| Continuous monitoring, target prices | Regular rebalancing (monthly, quarterly) |

| Strategy | Core signal | Typical holding/screen | Characteristic risk |
|---|---|---|---|
| Relative value | P/E, P/B vs sector peers | Discount to sector multiple | Discount is justified (sector multiples differ widely) |
| Contrarian | Sentiment, price lows | Depressed cyclicals | Catching a falling knife |
| Deep value | P/B far below 1, distress | Reorganisation candidates | Illiquid, legal complexity |
| Income | High dividend yield + growth | Dividend growers | Yield trap, rate sensitivity |
| GARP | Low PEG | Growth at reasonable multiple | Growth forecasts wrong |
| Growth | EPS, revenue growth, momentum | Tolerates high multiples | Growth trap, valuation compression |
| Activist | Underperformance, weak governance | Small-mid cap, <10% stake | Defenses, leverage rises after campaigns |
| Pairs/stat arb | Spread z-score | Same-industry pairs | Structural break (CNR vs CP example) |
| Merger arb | Deal spread | Announced deals | Deal failure, duration |

Factors and evidence in the source: value (Basu 1977, Fama-French 1993; premium either distress compensation or behavioral overreaction); momentum (Jegadeesh-Titman 1993; 12-month winners keep winning 2-12 months; short-term one-month reversal; momentum lost 56% in March-May 2009 long/short decile; sector-neutral version cuts downside); growth; quality/accruals (Sloan 1996); analyst sentiment (earnings revisions); news sentiment (NLP); alternative data (satellite, credit card, supply chain: signal = largest customer's trailing month return).
US 1988-2016: S&P 500 10.7% return, 14.4% vol, Sharpe 0.74; Russell 2000 11.1%, 18.7%, 0.59; R1000 Value 10.9%, 14.2%, 0.77; R1000 Growth 10.7%, 16.4%, 0.65.
Activism evidence: targets show slower growth, negative momentum, weaker governance; average +2% announcement-day return plus +0.6% next month (excess); fundamentals improve over 3 years but leverage rises; HFRX Activist Index Sharpe 0.56 vs S&P 500 0.54 (small sample).

## Mental Models
- **Depth vs breadth**: fundamental managers concentrate and own the company risk; quant managers diversify across hundreds of weak signals and own the factor risk.
- **Smell test before back-test**: a factor must make economic or behavioral sense; backtest performance alone is evidence of data mining.
- **Value is cheap for a reason until a catalyst appears**: always ask why the multiple is low and what changes perception; no catalyst means a trap.
- **Rank beats raw correlation**: use Spearman IC when outliers can flip Pearson (one extreme stock turned a good factor negative in the example).
- **Backtests live in a frictionless world**: a high-turnover signal (one-month reversal) can lose most of its return at 30 bp per trade while a slow signal (P/B) barely moves.
- **Pairs need an economic reason, not just correlation**: same-industry, same-valuation names; spurious correlation or a changed business (new management, new business lines) breaks the trade.

## Worked Example
**1. Matching stocks to disciplines (verified).** Using forward P/E = price / forward EPS and PEG = P/E / growth:
A: 50/5 = 10, growth 20%, PEG 0.5 (lowest) → GARP. B: 56/2 = 28 vs sector average 35 → relative value. C: 22/10 = 2.2, EPS growth −5% → deep value (check it is not a trap). D: 32/2 = 16 = sector average, yield 8%, growth 2% → income.
**2. Information coefficient (verified).** Nine stocks, factor scores from −1.45 to +1.45, next-month returns with Stock I (highest score) returning −8.5%. Pearson IC = −0.8% (factor looks useless), Spearman rank IC = +40% (factor works except one outlier). Long tercile (G, H, I) minus short tercile (A, B, C) = (3.02 + 3.05 − 8.5)/3 − (−3.0 − 0.6 − 0.5)/3 = −0.81% + 1.37% = +0.56% (56 bp). Decision: judge a factor on rank IC and quantile spread, not one Pearson number.
**3. Margin on quant data quality.** Satyam rule: a simulation at 31 Dec 2008 must include Satyam in the Nifty 50 and use the originally published (later proven fraudulent) accounts, because the fraud was unknown then; using restated data is look-ahead bias.

## Anti-patterns
- **Back-testing on today's index members or restated numbers**: survivorship and look-ahead bias inflate results.
- **Ignoring costs and short availability in a back-test**: reversal-type signals die at 30 bp per trade.
- **Hedged-portfolio factor test only**: top and bottom deciles ignore middle information (nonlinear payoffs, e.g. debt-change factor best in deciles 3-6), assume linearity, concentrate, need shorting and carry unintended factor exposures.
- **Running the same crowded factors as everyone else**: August 2007 shows forced exits compound losses; use differentiated signals and monitor crowding.
- **Letting stock picking create unintended sector/country bets**: fix with a top-down overlay (derivatives) or explicit sector-neutral construction.
- **Treating a low multiple as a margin of safety**: cheap relative to peers may be justified (value trap, HSBC example: fell 43.7% while looking cheap at 10.9x P/E, 0.9x P/B).
- **Behavioral biases in discretionary work**: confirmation (stock love), illusion of control (cognitive errors); loss aversion, overconfidence, regret aversion (emotional); counter with contrary views, written sell discipline, stop-loss, position reviews.
- **Interpreting a flat pairs spread as safe**: pairs trading carries open-ended loss if the divergence is structural.

## Exam Focus & Traps
- Fundamental = discretionary, forward-looking, depth, few stocks, risk at company level; quantitative = systematic, backward-looking data, breadth, optimizer, risk at portfolio level, regular rebalancing. A statement that quant emphasises forecasting company prospects is the wrong characteristic.
- Relative value (compare multiples within sector) vs contrarian (sentiment/price extremes) vs high-quality value (valuation + quality) vs deep value (distressed, asset-based): classify by what the stock/investor emphasises; a high P/B stock bought because it trades below intrinsic value relative to peers = relative value.
- Order of the fundamental process: after industry/competitive analysis comes forecasting and valuation, not rebalancing or back-testing. Quant process starts with the thesis (market opportunity), then data, back-test, evaluate.
- IC is the correlation of factor score at t with returns from t to t+1 (not return at t, not score at t+1).
- Using year-end financial data before publication = look-ahead bias (not survivorship, not data mining).
- Best pairs candidate: mean-reverting ratio and high correlation and a currently stretched spread. Not-significantly-different spread = no trade; low correlation or non-mean-reverting = reject.
- Style analysis: holdings-based = bottom-up aggregation of stock attributes, generally more accurate and shows current style; returns-based = regression on style indexes, shows average style over the window and can reveal drift or rotation, usable when holdings are not disclosed. Different vendors classify differently (Morningstar 0/1 vs MSCI/Russell fractional); adding a factor changes holdings-based style only if it changes holdings, but changes the returns-based analysis only through new returns.
- Activism: targets are underperformers with weak governance and under-used assets (an efficient company or one needing distressed restructuring is the wrong target); typical stake below 10%; long-term engaged owners (Asgard-like) engage rather than sue.
- Top-down tools: sector rotation suits global industries (IT, energy); local industries (real estate, consumer staples) suit within-country allocation. Long straddle = long volatility, max loss limited to premiums.

## Key Takeaways
1. Classify any manager on process: fundamental vs quant, bottom-up vs top-down, and see where risk is taken (company vs factor).
2. Write the investment thesis first: what the opportunity is, why it exists and why it persists after costs.
3. Value and growth each have a trap; require a catalyst and a view on why the multiple is what it is.
4. Quant strategies stand or fail on data hygiene (point-in-time, delisted names), out-of-sample tests, transaction costs and crowding.
5. Use Spearman rank IC and full-quantile analysis, then combine factors as assets (watch factor correlation).
6. Activism targets slow-growth, weakly governed, under-utilised-asset companies; expect positive announcement returns but rising leverage.
7. Overlays and sector-neutral construction control unintended macro exposures in stock-picking portfolios.
8. Use both holdings-based and returns-based style analysis, and check against self-declared style.

## Connects To
- **ch 01**: passive-active spectrum, costs and engagement basics.
- **ch 02**: factor-based passive strategies and smart beta as the low-cost version of these factors.
- **ch 04**: turns these strategies into portfolios (factor weights, sizing, active share, risk budgeting).
- **`cfa-portfolio-management` ch 12**: multifactor models; **ch 14**: back-testing and simulation; **ch 15**: analysis of active portfolio management.
- **`cfa-equity-valuation` ch 04-09**: DCF, multiples and residual-income valuation behind the fundamental process.
- **`cfasi-equity-investment-styles` ch 01-12**: value, factor and systematic investing guides.
- **`cfa-alternative-investments` ch 05**: hedge fund strategies (activist, event-driven, stat arb).
- **`pairs-trading-partial-cointegration`**: formal pairs trading.
- **`cfa-asset-allocation-cme` ch 01-02**: behavioral biases.
