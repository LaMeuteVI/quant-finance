# Chapter 5: The Value Investment Style and the Multifactor Approach
> **Source**: CFA Society Italy × Advisor Private, *Value Investing* guide (2020), Ch. 5 "Lo stile di investimento Value e l'approccio multifattoriale" | Alessandro Capeccia (Azimut). Data as of end 2019 / early 2020; sources credited in the guide to SG Cross Asset Research, UBS, Exane, BofA and J.P. Morgan.

## Core Idea
Pure value, measured by a single multiple, has delivered good long-run returns but with poor efficiency (large drawdowns, sector concentration, quality problems) and has not worked reliably in the decade after 2008. The practical answer is the **multifactor approach**: keep value as the core but combine it with momentum, quality, profitability and earnings revisions, weight the factors by the economic cycle, and choose the valuation metric by sector. The result is a "new value" that behaves like a quant-fundamental ("quantamental") process.

## Frameworks Introduced
- **Two-phase multifactor process (Capeccia, Azimut)**
  - Phase 1: value each company with traditional fundamental methods: P/E, P/FCF, P/B, DCF, EVA (return on adjusted capital), Gordon model, sum of the parts.
  - Phase 2: rank stocks on pre-selected performance drivers (Value, Growth, Momentum, Quality), assign weights (subjective or cycle-dependent), compute each stock's composite score and build the portfolio from the best scores; typically equal-weighted unless benchmark or tracking-error constraints bind.
  - Cadence: rebalance monthly, more often during quarterly reporting season to capture momentum and estimate revisions.
  - Controls: avoid unintended country and size (small-cap) bets.
- **Core factor definitions (SG Cross Asset Research)**
  - Value: book-to-price, earnings-to-price, 1-year-forward earnings-to-price, EBITDA/EV, free-cash-flow yield (financials excluded where inappropriate; all relative to sector).
  - Quality: Merton distance to default, Piotroski financial quality score, price volatility, beta.
  - Momentum: 12-month residual momentum lagged one month.
  - Profitability: gross profitability, ROA, ROE, ROIC (relative to sector).
- **UBS value metrics**: book/price, trailing dividend yield, earnings yield, EBIT/EV, free-cash-flow yield, sales yield (core sales/EV), PEG (earnings yield relative to forecast EPS growth).
- **Sector-specific multiple choice**
  - Rule: backtest which multiple works per sector; one multiple used across sectors gives divergent results.
  - Reported 10-year backtest: P/B failed except in telecoms and oil; dividend yield was the only working metric in utilities. EV-based multiples are less sensitive to capital structure, accounting policy and non-core assets, hence better for cash-generation analysis; price multiples are simpler but more distorted.
- **Value with catalyst**
  - A cheap valuation alone is not enough; a trigger that forces the market to re-rate is needed (Mario Gabelli's motto).
- **Cycle-aware factor rotation (J.P. Morgan, 1994-2014 backtests)**
  - Use: map factor returns to four cycle phases and overweight accordingly (table below).
  - Reading: in the early recovery and in expansion, value (high beta, cyclical) leads; as the cycle matures, move to growth with lower risk; in slowdown and contraction, rotate to quality and low volatility.
  - Limits: breaks down when the market's view of the cycle shifts abruptly (Q4 2018).
- **Value plus momentum combination**
  - Since 1990 (SG data to end 2019): value earned the best single-factor annual return (11.2%) and positive months about 62% of the time; value + momentum earned 11.8% with 63.6% positive months and stronger efficiency.

## Key Concepts
- **Quantamental**: fundamental analysis augmented with large-scale quantitative data processing.
- **Multifactor approach**: ranking stocks on several drivers and combining scores into one portfolio.
- **Deep value**: strict classical criteria (Graham, Piotroski) giving few stocks, concentrated by sector and country.
- **Value trap / low quality**: cheap stocks with balance-sheet, governance or product problems that need a catalyst.
- **Relative drawdown**: maximum peak-to-trough loss of the long-short value strategy; the guide cites over 60% and volatility around 19%, versus 52% and 15% for the broad index.
- **ZIRP**: zero interest rate policy; removed the positive risk-free anchor for valuation.
- **Passive-flow effect**: ETF and index flows buy by market cap regardless of fundamentals, boosting large caps, hurting equal-weighted portfolios and the size factor.
- **Factor crowding**: proliferation of factor indices and swaps sold by investment banks (J.P. Morgan and BofA equity risk premia indices) causes abrupt reversals and lower alpha.
- **Equity risk premia (ERP) indices**: bank-created long-short factor indices tradable as swaps or certificates.
- **EPS momentum/revisions**: earnings-estimate changes as a signal.
- **Alternative data**: web semantics, big data, geolocation to predict reported figures.

## Formulas & Reference Tables
- `Composite score_i = sum_k (w_k x z_ik)` with `z_ik` the sector-relative rank/z-score of stock i on factor k (Value, Growth, Momentum, Quality) and `w_k` factor weights (equal by default or cycle-driven).
- Yields as inverses: `earnings yield = 1/(P/E)`, `book/price = 1/(P/B)`, `FCF yield = FCF/market cap`, `sales yield = core sales/EV`.

**Average monthly excess return of long-short factors by cycle phase, % (J.P. Morgan, Jan 1994-Dec 2014)**

| Phase | Value | Growth | Momentum | Quality | Risk (high-low) | Size (large-small) |
|---|---|---|---|---|---|---|
| Expansion | 0.85 | 0.44 | 1.11 | -0.85 | 0.99 | -0.32 |
| Slowdown | -0.07 | 0.33 | 1.41 | 0.71 | -1.24 | 0.67 (**⚠** Fig. 14 shows -0.67) |
| Contraction | 0.06 | -0.44 | 0.84 | 0.89 | -1.36 | 0.33 |
| Recovery | 1.65 | 0.57 | -0.64 | -0.08 | 1.62 | -2.27 |

**Factor performance to Dec 2019 (SG Global Quantitative Research)**

| Style | Last 5 years, annual % | Since 1990, annual % | % positive months since 1990 |
|---|---|---|---|
| Value | -1.4 | 11.2 | 62.2 |
| Momentum | 1.7 | 6.1 | 61.9 |
| Quality | 2.7 | -0.6 | 54.2 |
| Growth | 1.6 | 0.4 | 53.6 |
| Profitability | 2.3 | 4.5 | 57.2 |
| Value + Momentum | 0.3 | 11.8 | 63.6 |

**Multiples most used by institutional investors (UBS survey of about 270 analysts)**: P/E 31%, EV/EBITDA 23%, FCF yield 16%, P/B 9%, others (dividend yield 5%, EV/sales 4%, PEG 3%, P/NAV 2%, P/NPV 1%, other 6%).

**Europe factor performance Jan 2003-Jan 2020 (BofA)**: value vs growth -16.5% in 12 months, -44.9% over 5 years; rising vs falling momentum +23.5% (12m) and +65.9% (5y); low vs high quality negative. The "since inception" column in the source (values such as -224.6) is a cumulative series, not comparable to the others.

## Mental Models
- **Use sector-specific valuation when screening a global universe**: a multiple that works in utilities (dividend yield) may fail in tech.
- **Use value + quality/profitability to filter value traps**: leave out cheap names with weak financial strength scores.
- **Use the cycle phase to set factor weights**: more value early in recovery/expansion, quality and low volatility when growth is slowing.
- **Use momentum or revisions as a timing overlay for value**: it improves efficiency without abandoning cheapness.
- **Use less crowded factors**: when a classic factor is widely traded through indices and swaps, expect sharp reversals and lower alpha.

## Worked Example
Composite-score construction (illustrative, recomputed).
- Inputs: three stocks scored by sector-relative z-scores on Value, Momentum and Quality, equal weights of one-third each.
- A: Value 1.5, Momentum -0.5, Quality 0.5 -> (1.5 - 0.5 + 0.5)/3 = 0.50.
- B: Value 1.0, Momentum 1.0, Quality 0.5 -> 2.5/3 = 0.83.
- C: Value 2.0, Momentum -1.5, Quality -1.0 -> -0.5/3 = -0.17.
- Result: rank B > A > C. C is the cheapest stock but is excluded because weak momentum and quality flag a likely trap.
- Interpretation: a pure value ranking would put C first; the multifactor score demotes it.

Value efficiency (guide data, recomputed).
- Long-short value drawdown over 60% and volatility 19% vs broad index drawdown 52% and volatility 15%: ratio of volatilities 19/15 = 1.27x; deep-value screens narrow diversification further.
- Interpretation: strong long-run returns came with return-to-risk too poor for many mandates or clients with short patience.

## Anti-patterns
- Running a portfolio on one multiple (P/B notably) across all sectors; a study cited in the guide found P/B positive only in 1963-1981 over a long history from 1926.
- Deep-value screens that produce a handful of names concentrated by country and sector.
- Overweighting low-quality balance sheets because they look cheapest.
- Ignoring the client time horizon: a long-term strategy fails if the client redeems before the payoff.
- Overweighting a country or small caps by accident when ranking globally.
- Reading the cycle table as a trading rule: it is a backtest, and phases are identified with delay.
- Assuming ex-ante that value must rebound after a bad year; in 2019 it did not.

## Practitioner Notes
- Since 2003 many indices changed methodology to include fundamental and technical style criteria (the guide cites the MSCI World example).
- Structural reasons given for value's weakness after 2008: post-Lehman risk aversion, ZIRP (valuation no longer anchored on positive risk-free rates), passive flows into cap-weighted indices (favouring large caps and quality/momentum, hurting size and equal weighting), and factor crowding through tradable indices. Evidence: strongest drawdowns of value in 2008-09 and no catch-up after the 2019 rebound.
- Lessons from Q4 2018 / 2019: markets priced a slowdown (low volatility factor surged), then reversed with Fed easing; value underperformed even in a bull market with average gains above 20%.
- Research direction: less common factors, better estimate quality (EPS revisions), alternative data (web semantics, geolocation to track restaurant visits, used by large asset managers' quant teams) and AI; any resulting alpha is likely temporary.
- J.P. Morgan and BofA publish European equity risk premia indices with positioning views (value overweight, momentum, quality, low beta underweight, as of early 2020), which shows factors are now traded like single stocks.

## Key Takeaways
1. Value alone, especially deep value, shows high drawdowns (over 60%), volatility and sector/country concentration.
2. Best performer since 1990 (11.2% a year), but negative over 2015-2019 (-1.4%).
3. Combining value with momentum lifts annual return to 11.8% and raises efficiency.
4. Use sector-specific valuation metrics; backtests show wide differences.
5. Add quality, profitability and earnings revisions to avoid value traps and adapt to low rates.
6. Factor rotation by cycle phase: value in recovery and expansion, quality and low volatility in slowdown and contraction (note the source overstates the weakness; table values are near zero).
7. Passive flows and factor-index trading reduced classic factor efficacy; innovation shifts to data quality and uncorrelated signals.
8. A catalyst is as important as cheapness.

## Connects To
- **ch01**: Graham's criteria, the origin of classical value.
- **ch03**: value premium, profitability and value traps in detail.
- **ch04**: owner earnings as a cash-based value metric.
- **ch06-ch08**: factor investing theory, factor cycles and implementation.
- **ch09-ch12**: systematic investing as the fully rules-based version of this process.
- **`cfa-equity-portfolio-management`**: style, factor models and active-passive trade-offs.
