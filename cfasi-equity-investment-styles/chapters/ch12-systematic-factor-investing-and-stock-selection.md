# Chapter 12: Factor Investing and Systematic Stock Selection
> **Source**: CFA Society Italy × Advisor Private, *Systematic Investments* guide (2019), Ch. 4 "Factor investing e stock selection" | Andrea Nocifora, CFA; plus GAM insert "Gli investimenti sistematici e dinamici nei mercati del credito" (sponsor content, attributed)

## Core Idea
A systematic equity stock-picking model gets exposure to factors such as **Value, Momentum and Quality** not passively but by **scoring individual companies** on fundamental metrics. Designing it needs four decisions: which factors, how each is defined (metrics), how stocks are ranked or scored, and what portfolio structure (long-only, long vs market, long/short). Statistical factor definitions (Fama-French) and investment styles (Graham value, Lynch growth) are not the same thing; their stock lists can differ completely.

## Frameworks Introduced
- **Statistical factor vs investment style**
  - What: Fama-French treat markets as efficient; excess return over the market portfolio is compensation for extra risk (Value and Size exposure). A Graham-type system searches for mispricing, a gap between intrinsic and market value.
  - When: before building a model or comparing two "value" funds.
  - How: ask which definition is used (P/B decile? composite of cash-flow, earnings, dividends?).
  - Failure mode: two portfolios both labelled Value can hold very different stocks and have different factor exposures.
- **Systematic stock-selection process (4 steps)**
  1. **Choose factors**: judge attractiveness statistically (risk-adjusted historical performance, correlation structure among factors) and discretionarily (economic rationale for the premium). Account for time variation tied to the business cycle, market structure and who participates, and investor sentiment/behavioural biases.
  2. **Define each factor with several metrics** and rank or score stocks (composite definition, Morgan Stanley European Quantitative Strategy 2018):
     | Factor | Example metrics |
     |---|---|
     | Value | 12M forward P/E, FCF yield, price-to-book, dividend yield |
     | Growth | long-term growth, internal growth |
     | Momentum | price momentum, earnings momentum |
     | Quality | accruals, debt/equity, capex-to-sales, return on equity |
     | Risk | 12M return volatility |
     | Size | market capitalisation |
  3. **Pick the portfolio structure**: long-only (top scores only); long vs market (long the factor basket, short the benchmark, e.g. S&P 500 for a US universe, or Stoxx Europe 600); long/short (long top basket, short inverse-exposed names, e.g. cheap vs expensive). Differences: implementation difficulty (shorting can be costly or impossible), risk profile and equity-market beta.
  4. **Score and rebalance**: see illustrative model below.
- **Illustrative model in the guide** (European universe, Stoxx Europe 600): Value (P/E, P/B, EV/EBITDA, dividend yield), Momentum (price momentum, forward EPS momentum), Quality (EBIT margin, ROIC, gap between net income and operating cash flow). Each metric is converted to a 1-100 score that accounts for the distance between companies (not just rank), rewarding clear leaders and penalising the worst. The final score is the **equal-weighted sum of factor scores**. Rescored **monthly**; at each rebalance the **top 50** form the long leg and the **bottom 50** the short leg. The guide shows back-tested illustrations for long-only, long vs market, and long/short (Figures 7-9; sourced Datastream, Bloomberg).
- **Evidence summary** (JP Morgan US factor reference book 2018; Asness-Moskowitz-Pedersen 2013 "Value and Momentum Everywhere"; Asness-Frazzini 2013 "The Devil in HML's Details"):
  - Pre-GFC (US): Value, Quality and Low Volatility showed significantly positive risk-adjusted returns; post-GFC Value weakened, Quality and Low Vol slightly improved, Income emerged as a distinct factor.
  - Long/short Value had the best risk-adjusted returns 1985-2008 and deteriorated after the crisis (still at historically depressed levels per the 2018 source).
  - Value outperformed over multi-decade horizons in the US and globally; Momentum (long winners, short losers) was very persistent over long horizons but very volatile.
- **Sponsor insert (GAM) on credit**: systematic, dynamic credit via three sub-strategies, combined dynamically between risk-on and risk-off: **Tactical credit** (rotates between credit markets and safe instruments; "credit trader"; captures risk-appetite shifts), **Directional credit** (long/short credit market and sectors; "credit strategist"; captures credit-condition changes), **Market-neutral credit** (portfolio of single-name corporate CDS; "credit analyst"; relative value in spreads). Uses CDS/CDX for liquidity and transparency. Marketing claims (participate in upside, protect downside) are not evidence.

## Key Concepts
- **Factor**: a systematic return driver (Value, Size, Momentum, Quality, Low Vol, Income, Growth).
- **Ranking vs scoring**: rank uses order only; score also uses distance between companies.
- **Composite factor definition**: several metrics per factor to reduce idiosyncratic metric noise.
- **Equal-weighted score**: simple aggregation of factor scores into a final composite.
- **Long-only / Long vs Market / Long-short**: three structures with increasing market-beta neutrality and implementation cost.
- **Pre/post GFC regime**: factor premia unstable across periods.
- **Time variation**: factor returns depend on the cycle, technical flows and sentiment.
- **Fama-French factors**: statistical Value (HML) and Size (SMB) premia in an efficient-market framework.
- **Graham value system**: intrinsic-value gap screening; unlike HML.
- **Earnings momentum**: revision-based drift; **price momentum**: past winners continue.
- **Accruals**: gap between earnings and cash flow; high accruals flag low earnings quality.
- **CDS / CDX**: credit derivatives used for liquid credit exposure (sponsor insert).

## Formulas & Reference Tables
- Composite score: `S_i = Σ_f w_f · S_i,f` with `w_f = 1/F` in the guide's equal-weighted model; `S_i,f` itself an average of metric scores, each scaled to 1-100.
- One scaling choice consistent with "distance-aware" scoring: min-max `S = 1 + 99 · (x - x_min)/(x_max - x_min)` (sign flipped for metrics where lower is better, such as P/E); the guide does not specify the exact method. Z-scores with winsorisation are the common alternative.
- Long/short return: `R_LS = R_top50 - R_bottom50`; long vs market: `R_LvM = R_top50 - R_benchmark`.
- Beta of structures: long-only about 1; long vs market about 0 (if the long basket beta is about 1); long/short about 0 if both legs have similar beta.

## Mental Models
- Use **"define the factor before you buy the factor"**: two Value funds can be opposite bets.
- Use **composite metrics** to avoid single-ratio traps (low P/B alone catches distressed firms; add Quality).
- Use **long-only for access, long/short for purity**: long/short isolates the factor but needs shorting capacity and costs.
- Use **monthly rescoring with turnover cost awareness**: signal freshness vs trading cost.
- Use **post-GFC caution**: do not extrapolate the 1985-2008 Value premium to the next decade.

## Worked Example
Distance-aware scoring of three stocks on forward P/E (lower is better), illustrative: A 10x, B 15x, C 30x.
- Min-max with inversion: `S = 1 + 99 · (30 - x)/(30 - 10)`.
- A = 1 + 99 · 20/20 = **100**; B = 1 + 99 · 15/20 = **75.25**; C = **1**.
- Rank alone gives 1, 2, 3 (equal gaps); score shows B is much closer to A than C is, which is the point of "distance" scoring.
- Add Momentum scores A 40, B 80, C 90 and Quality scores A 70, B 60, C 20: equal-weighted composite A = (100+40+70)/3 = **70.0**; B = (75.25+80+60)/3 = **71.8**; C = (1+90+20)/3 = **37.0**. B ranks first and C last, although C is the best momentum name.

## Anti-patterns
- Calling any single-metric portfolio "the Value factor".
- Assuming back-tests shown (April 2006 to March 2009 in the caption) are reliable. **⚠ Correction**: the captions of Figures 7-9 say "April 2006 to March 2009", but the charts run to 2018, so the caption period is a typo; ask for the true sample and out-of-sample split.
- Ignoring factor crowding and decay after publication.
- Equal-weighting factors without testing correlations and cycle exposure.
- Long/short backtests without borrow cost, shorting limits and slippage.

## Practitioner Notes
- The guide's author is a portfolio manager of both discretionary and quant global equity strategies; the model is "illustrative", not a track record.
- Build checklist: universe and point-in-time data (avoid look-ahead), sector/country neutralisation, winsorisation, turnover cap, capacity, borrow cost.
- Compare against factor ETFs for the cost of passive access (see ch06-ch08 of this skill).

## Key Takeaways
1. Stock-picking by factor exposure scores companies on fundamentals rather than buying a factor index.
2. Statistical factors and investment styles are different objects.
3. Four design choices: factors, metrics, scoring, portfolio structure.
4. Illustrative model: V, M, Q, equal-weighted, monthly rescoring, top 50 long and bottom 50 short.
5. Factor performance varies with the cycle; Value long/short weakened after 2008, Momentum is persistent but volatile.
6. Sponsor credit strategy: three complementary sub-strategies (tactical, directional, market neutral CDS), marketing claims unverified.

## Connects To
- **ch09**: why the same ideas look different in discretionary and systematic language.
- **ch10**: other quant families, Magic Formula and Piotroski as scoring models, crowding in 2007.
- **ch11**: rule-based discipline.
- **ch06-ch08**: factor definitions and evidence (Factor Investing guide).
- **`cfa-equity-portfolio-management`**: active, passive and smart-beta equity portfolio construction.
