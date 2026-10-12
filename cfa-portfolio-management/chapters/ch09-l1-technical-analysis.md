# Chapter 9: Technical Analysis
> **Source**: CFA Program Curriculum 2020, Level I, Reading 56 · Alternative Investments & Portfolio Management | Barry M. Sine and Robert A. Strong, PhD, CFA

## Core Idea
Technical analysis infers future price direction from price and volume data (charts, trend, patterns, indicators, cycles, intermarket ratios) on the premise that prices reflect supply and demand, and that collective investor psychology repeats. It works only in freely traded, liquid markets and only when a trend exists: a pattern or oscillator reading without a prior trend or without regard to the normal range of the security has little predictive value. Indicators are tools to be combined and confirmed, never mechanically followed at default settings.

## Learning Outcomes Covered
- explain principles, applications and assumptions of technical analysis
- construct and interpret line, bar, candlestick and point-and-figure charts
- explain trend, support, resistance and change in polarity
- describe reversal and continuation chart patterns
- describe price-based, momentum oscillator, sentiment and flow-of-funds indicators
- explain how technicians use cycles
- describe Elliott Wave Theory and the role of Fibonacci numbers
- describe intermarket analysis and its use in asset allocation

## Frameworks Introduced
- **Technical vs fundamental analysis**: technical = price/volume only, objective data, projects where price *will* trade; fundamental = intrinsic value, external data, where price *should* trade.
  - When to use: technical for assets with no cash flows (commodities, currencies, futures), short horizons, timing entries and exits for fundamentally selected names, and in cases of accounting fraud (Enron, WorldCom). Fundamentals for assets with income streams and long horizons.
  - Failure mode: late in confirming trends; unusable in manipulated (central-bank-intervened FX), illiquid, or restructuring-to-zero situations (short covering creates fake uptrends); both are subjective at the interpretation stage.
- **Trend, support and resistance, change in polarity**: uptrend = higher highs and higher lows (trendline connects lows); downtrend = lower highs and lower lows (trendline connects highs). A breach of 5-10% beyond the line, held for time, signals trend end. Once support is broken it becomes resistance; once resistance is broken it becomes support (e.g., DJIA 1,000 resistance until 1982, support in 1984).
- **Chart pattern method**: (1) confirm a clear prior trend; (2) identify the pattern; (3) wait for a confirmed breakout (filter 3-5% and/or several days); (4) set the measured price target; (5) check volume (confirm or diverge). Without a prior trend the pattern has no predictive value.
- **Oscillator method**: use oscillators (a) to gauge trend strength, (b) to spot reversals at extremes or zero/100 crossings, (c) in non-trending markets to sell overbought and buy oversold. Always read in the context of the trend and the security's own historical range; look for convergence vs divergence with price.
- **Elliott Wave Theory** (R. N. Elliott, 1938, *The Wave Principle*): markets move in 5 impulse waves (1-5) in the trend direction followed by 3 corrective waves (a-b-c); each wave subdivides; wave relationships are Fibonacci ratios.
- **Intermarket analysis** (John Murphy, 1991): stocks, bonds, currencies and commodities are linked; use relative strength ratios to detect inflections and rotate allocations.

## Key Concepts
- **Freely traded market**: willing buyers and sellers, no external intervention; precondition of technical analysis.
- **Line chart**: closing prices connected over time (one data point per period).
- **Bar chart**: open, high, low, close (OHLC) per period: vertical high-low line, left tick = open, right tick = close.
- **Candlestick chart**: OHLC with body (open-close) and wick/shadow (high-low); **white/clear body = close > open, dark/filled = close < open**; origin Japan (rice markets, 1700s); a **doji** (open = close) signals balance and, after a long trend, a probable reversal.
- **Point and figure chart**: columns of X (rising) and O (falling) on a grid with **box size** and **reversal size** (commonly 1 unit and 3 boxes); no time or volume axis; a new column starts only after a reversal of at least the reversal size; larger reversal size = fewer columns, fewer signals.
- **Scale**: linear (arithmetic) for narrow ranges, logarithmic (equal % moves = equal distance) for ranges spanning orders of magnitude (e.g., gold or DJIA over 100 years).
- **Volume**: conviction measure; rising price with rising volume confirms; rising price with falling volume diverges (warning).
- **Relative strength analysis**: line chart of asset price / benchmark (or other asset) price; rising = outperformance. Not the same as the **relative strength index (RSI)**.
- **Reversal patterns**: head and shoulders, inverse head and shoulders, double/triple tops and bottoms. **Continuation patterns**: triangles (ascending, descending, symmetrical), rectangles, flags, pennants.
- **Moving average (SMA/EMA)**, **golden cross** (short MA crosses above long MA, bullish), **death cross** (crosses below, bearish).
- **Bollinger Bands**: moving average ± k standard deviations (same window); widen with volatility.
- **Momentum oscillators**: ROC/momentum, RSI, stochastic (%K, %D), MACD; **overbought/oversold**, **convergence/divergence**.
- **Sentiment indicators**: opinion polls (Investors Intelligence, AAII, Market Vane, etc.), put/call ratio, VIX, margin debt, short interest ratio; mostly contrarian.
- **Flow-of-funds indicators**: Arms index (TRIN), margin debt, mutual fund cash position, IPOs, secondary offerings.
- **Cycles**: Kondratieff wave (54-year), 18-year, decennial, US presidential cycle.
- **Fibonacci sequence/ratios**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...; key ratios 0.382/0.50/0.618 (retracements) and 1.618 (extensions).

## Formulas & Reference Tables
- **Head and shoulders target** (bearish, prior uptrend): `Target = Neckline − (Head − Neckline)`
- **Inverse head and shoulders target** (bullish, prior downtrend): `Target = Neckline + (Neckline − Head)`
- **Double top target**: `Target = Valley low − (Top − Valley low)`; **double bottom**: `Target = Peak between bottoms + (Peak − Bottom)`
- **Triangle measuring implication**: height of the triangle at its widest (start); after breakout price expected to move at least that amount. Breakouts usually occur one half to three-quarters of the way to the apex.
- **Flag/pennant target**: `Target = End of pattern + (price change from trend start to pattern start)` (pole length)
- **Simple moving average**: `SMAₙ = (P₁ + P₂ + … + Pₙ)/n`; common windows 20 (month), 60 (quarter); exponential MA weights recent prices more.
- **Bollinger Bands**: `Upper = MAₙ + k·σₙ`, `Lower = MAₙ − k·σₙ` (typical k = 2, same n for MA and σ).
- **Momentum / ROC (centered on 0)**: `M = (V − Vₓ) × 100` (V = latest close, Vₓ = close x days ago, typically 10). **Centered on 100**: `M = (V/Vₓ) × 100`. ⚠ Correction: the common practitioner ROC is `(V/Vₓ − 1) × 100` (percentage); the curriculum's first form is a price-difference scaled by 100. Know both for the exam.
- **RSI**: `RSI = 100 − 100/(1 + RS)`, `RS = Σ(up changes)/Σ(down changes, absolute)` over the window (Wilder's default 14 periods). Bounded 0-100; >70 overbought, <30 oversold. ⚠ Note: the curriculum uses the simple-sum version; Wilder's original smooths up/down averages after the first window, which gives slightly different values.
- **Stochastic**: `%K = 100 × (C − L_n)/(H_n − L_n)` (C latest close, L_n/H_n lowest/highest over n = 14 periods); `%D` = 3-period average of %K (signal line); overbought >80, oversold <20; %K crossing above %D = bullish (short-term).
- **MACD**: `MACD line = EMA₁₂ − EMA₂₆`; `Signal line = EMA₉(MACD line)`; oscillates around 0, no bounds; compare with the security's own history.
- **Put/call ratio** = put volume ÷ call volume (normally < 1; contrarian: extreme high = bullish, extreme low = bearish).
- **Short interest ratio** = short interest ÷ average daily trading volume (days to cover).
- **Arms index (TRIN)** = `(Advancing issues ÷ Declining issues) ÷ (Volume of advancing ÷ Volume of declining)`; ≈ 1.0 balanced; **> 1.0 = more volume in decliners (bearish)**; **< 1.0 = more volume in advancers (bullish)**.
- **Fibonacci ratios**: `1/2 = 0.50, 2/3 = 0.667, 3/5 = 0.60, 5/8 = 0.625, 8/13 = 0.615`; `2/1 = 2, 3/2 = 1.5, 5/3 = 1.667, 8/5 = 1.60, 13/8 = 1.625 → 1.618 (golden ratio)`.

**Indicator summary**

| Indicator | Type | Bullish / bearish reading | Key caveat |
|---|---|---|---|
| Moving average cross | Price-based | Golden cross bullish; death cross bearish | Lag; optimization does not transfer across securities or regimes |
| Bollinger Bands | Price-based (not an oscillator) | Contrarian: sell at upper, buy at lower; trend: buy breakout > 5-10% above | Contrarian approach loses in regime change |
| ROC/momentum | Oscillator | Zero (or 100) crossing in trend direction = signal; extremes = overbought/oversold | Ignore counter-trend crossings |
| RSI | Oscillator | >70 overbought, <30 oversold; range 40-80 in uptrend, 20-60 in downtrend | Overbought can persist in strong trends (Ford, Mar 2009) |
| Stochastic | Oscillator | >80/<20; %K/%D crosses | "Stochastics default club"; shorter windows = more false signals |
| MACD | Oscillator | Line/signal cross, unusual level, divergence | No fixed OB/OS levels |
| Put/call, VIX | Sentiment | Contrarian extremes | Normal range differs by security |
| Margin debt | Sentiment/flow | Rising with prices, peaks near tops (corr ≈ 80% with S&P 500 in the source sample) | Late-cycle |
| Short interest ratio | Sentiment | High = bearish sentiment, but also future buying demand | Two readings |
| TRIN | Flow of funds | Above 1 bearish, below 1 bullish | Day-to-day noise |
| Mutual fund cash | Flow of funds | Contrarian: high cash = bullish (future buying power); low = bearish (average 5.9% 1984-2017) | Adjust for interest-rate level |
| IPOs / secondary offerings | Flow of funds | Surge = bearish (supply, issuers sell near tops) | |

**Elliott waves (bull market)**

| Wave | Direction | Sub-waves | Characteristics |
|---|---|---|---|
| 1 | Up | 5 | Basing; rising price, volume, breadth |
| 2 | Down | 3 | Retraces much (often 50% or 62%) but never all of wave 1 |
| 3 | Up | 5 | Above wave 1 high; strongest (often 1.618 × wave 1); most of the move |
| 4 | Down | 3 | Often retraces ~38% of wave 3 |
| 5 | Up | 5 | Usually weaker than 3 unless extended (euphoria) |
| a | Down | 3 | Correction begins |
| b | Up | 5 | False rally, "bull trap" |
| c | Down | 3 | Final correction; does not fall below start of wave 1 |

Bear market: impulse waves labeled A-E downward, counter-waves 1-3 upward. Waves in trend direction = 5 sub-waves; counter-trend waves = 3. Nine degrees: Grand supercycle (centuries), supercycle, cycle, primary, intermediate, minor, minute, minuette, subminuette.

**Cycles**

| Cycle | Length / pattern | Evidence and caveats |
|---|---|---|
| Kondratieff wave | 54 years (1780s onward; also Phelps Brown and Hopkins 50-52 years; van Gelderen and de Wolff 50-60 years, 1913) | Only about 4 completed cycles |
| 18-year | 3 per K wave; mainly real estate | |
| Decennial | Years ending in 5 best, years ending in 0 worst (DJIA up every year ending in 5 from 1885 to 1995, but −0.6% in 2005, −2.2% in 2015) | Weak sample |
| US presidential | Pre-election (third) year best (positive 1943-2011 until 2015's −2.2%); post-election and midterm weakest | 58 elections only |

**Intermarket links**: bond prices up (rates down) → stocks up; bond prices down (rates up, inflation expectations) → commodities up; strong USD → commodity prices down. Sectors: early-cycle leaders = utilities, financials, consumer non-durables, transportation; recovery = retailers, manufacturers, health care, consumer durables; laggards = energy, basic materials, technology. Commodity-linked equity markets: Australia, Canada, South Africa.

## Mental Models
- **Price is the vote count**: the chart shows what people did, not why; technicians do not need to know the security's name.
- **A pattern needs a trend to reverse or continue**: always ask "what was the prior trend?" before naming any pattern.
- **Use the oscillator relative to the security's own range**: 70/30 and 80/20 are defaults, not laws; utilities oscillate narrowly, small-cap tech widely; in an uptrend RSI tends to range 40-80.
- **Trend first, oscillator second**: an RSI above 70 in a strong uptrend is a sign of strength, not an automatic sell; trade oscillator crossings only in the direction of the trend.
- **Divergence is an early warning, not a signal**: price new high without oscillator (or volume) new high flags fading demand; wait for confirmation (trendline break, crossover, neckline break).
- **Sentiment indicators are contrarian at extremes**: crowds buy near tops (margin debt, IPO surge, low put/call) and sell near bottoms (VIX spike, high put/call).
- **Strategies tuned to one security, one period do not travel**: optimized moving-average lengths fit the participants of that security; re-test as the participant mix changes.
- **Use technicals for timing and fundamentals for selection**: where fundamentals are slow or fraudulent, technical charts may move first (market leads the economy by about 6 months).

## Worked Example
**Head and shoulders target (LPA Petroleum case).** Head peak US$108, neckline US$79, shares at US$78 (just through the neckline).
1. Head-to-neckline height = 108 − 79 = 29.
2. Target = 79 − 29 = **US$50**.
3. Trade: short at 78, cover at 50: gross gain US$28 per share, before costs. Filter: many technicians wait for 3-5% below the neckline or several days of close; expect a rebound to the neckline (now resistance) before the decline.

**RSI (Ford, June 2009).** 21 daily changes: 11 up summing 1.45, 9 down summing 1.51 (1 unchanged).
- `RS = 1.45/1.51 = 0.960`; `RSI = 100 − 100/1.960 = 48.99` (curriculum rounds to 48.98).
- Neutral reading (between 30 and 70). By contrast RSI above 70 on 23 March 2009 was not a sell because the stock was in an uptrend.

**Other recomputed checks**: Inverse H&S (DJIA): `9,050 + (9,050 − 7,197) = 10,903`. Pennant: A = 65.10, B = 71.90, pole = 6.80, C = 69.75 → target `69.75 + 6.80 = 76.55`. Double top (Eurodollar futures): tops 97.00/97.02, valley 96.42 → `96.42 − (97.02 − 96.42) = 95.82`. Short interest ratio: TD Bank `20,420,166/1,183,558 = 17.25 days` vs Goldman `10,936,467/9,086,174 = 1.2 days`. TRIN NYSE `(850/1,982)/(76,921,200/185,461,042) = 1.03`; NASDAQ `1.80` (both bearish, NASDAQ much worse). Stochastic illustration: close 46, 14-day low 40, high 50 → `%K = 100 × 6/10 = 60`.

## Anti-patterns
- **Forcing a conclusion from a chart with no trend**: sideways or trendless charts carry little forecasting information (options strategies may suit).
- **Labelling a pattern without a prior trend**: no predictive value.
- **Trading oscillator defaults**: the stochastics default club; others front-run the default crowd; shorter windows create more false signals.
- **Selling every RSI > 70 or buying every < 30**: in trends the oscillator stays extreme.
- **Acting on the first pierce of a trendline or neckline**: use 5-10% and time filters (trendline) or 3-5% and days (neckline).
- **Assuming a double top/bottom will form**: there is no theory predicting whether a low repeats once or twice; it is known only after the fact.
- **Over-optimizing moving-average or oscillator parameters** and extrapolating to other securities or regimes.
- **Using technical analysis in managed, illiquid or zero-value-restructuring securities**: central-bank-intervened FX, thin ADRs (analyze the local line), bankrupt equities.
- **Treating long cycles as laws**: tiny samples (4 K-waves, 58 elections) and recent failures (2005, 2015 decennial; 2015 presidential).
- **Counting Elliott waves rigidly**: counts are routinely renumbered; use with Dow theory, trend and oscillators.
- **Reading volume or sentiment in isolation**: use confirmation across tools.

## Exam Focus & Traps
- Not an assumption: **markets are efficient**. Assumptions: freely traded, supply/demand sets price, trends/patterns repeat, behavior is partly irrational.
- Drawback: identifies changes in trend after the fact (lag). Useful for commodities/currencies because **no valuation model** exists.
- Bar chart = OHLC with left tick open, right tick close; candlestick = body shaded when **close < open** (dark) and clear when close > open; X's and O's belong to point and figure, whose horizontal axis is **changes in price, not time**.
- Log scale suits long, wide-ranging data (gold over 100 years), not one month of a stock or 5-year Treasury yields.
- Downtrend line connects **highs**; uptrend line connects **lows**.
- Change in polarity: breached **resistance becomes support** (and vice versa), not "broken uptrend becomes downtrend".
- Volume increasing with the trend **confirms**; price up with volume down = divergence.
- Reversal: head and shoulders (prior uptrend), inverse (prior downtrend), double/triple tops/bottoms; **continuation**: triangles, rectangles, flags, pennants. Triple top is reversal; pennant, rectangle are continuation. Inverse H&S: target = neckline + (neckline − head): neckline 100, head 75 → 125.
- H&S: volume lower on head and right shoulder; neckline once breached becomes **resistance** (not support).
- Bollinger Bands are **price-based, not a momentum oscillator**; MACD, stochastic, RSI, ROC are oscillators.
- TRIN < 1 = more volume in advancing issues = bullish; > 1 bearish (the reverse of what many expect).
- Mutual fund cash and short interest (squeeze demand argument) are contrarian; IPO surge bearish; rising margin debt below its average still bullish in the curriculum's logic.
- Decennial pattern: years ending in 5 beat years ending in 0 (2015 would be better than 2020 per theory); presidential cycle: **third year (pre-election)** best.
- Kondratieff = 54 years; 3 × 18-year cycles; main problem of cycle theories = small sample size.
- Elliott: 5 waves with, 3 correction; wave 2 never erases all of wave 1; wave 3 often longest; wave 4 ~38% retracement; presidential is not an Elliott degree (supercycle and grand supercycle are).
- Relative strength **analysis** (ratio of prices) vs relative strength **index** (momentum oscillator): distinct.
- ⚠ Source inconsistency: curriculum Example 5 states a 7.0% mutual fund cash position but the solution refers to "6.0%"; either way it is near the 5.9% average and neutral.

## Key Takeaways
1. Technical analysis is price/volume-based, objective in data but subjective in interpretation; best for timing, short horizons and assets without cash flows.
2. Start every analysis with the long-time-frame trend and its support/resistance, then drill down; trend defined by higher highs/lows or lower highs/lows.
3. Use patterns only when a prior trend exists, wait for filtered breakouts, set measured targets (neckline ± head distance, triangle height, pole), and check volume.
4. Choose chart type by purpose: line (overview), bar/candlestick (daily range and sentiment, doji), point and figure (entry/exit levels, no time), log scale for wide ranges.
5. Treat RSI/stochastic/MACD/ROC as sentiment gauges with security-specific ranges; combine with trend, look for divergence, use crossovers in trend direction.
6. Read sentiment and flow-of-funds data as contrarian at extremes (VIX, put/call, margin debt, mutual fund cash, IPOs, short interest, TRIN).
7. Respect the limits: small-sample cycles, subjective Elliott counts, parameter optimization that does not generalize, unusable in intervened or illiquid markets.
8. Apply intermarket relative strength (bonds/stocks/commodities/dollar, sectors, countries) to guide asset allocation rotation and inflection warnings.

## Connects To
- **ch03**: market efficiency; technical analysis assumes inefficiency/behavioral patterns (semi-strong form tension).
- **ch02**: security market indexes underpin relative strength and breadth data (Dow Theory, DJIA).
- **ch04** and **ch07**: where technical timing sits in the portfolio management process (TAA tilts within the IPS policy).
- **ch14**: backtesting and simulation, the discipline needed to test oscillator and moving-average rules (data snooping, overfitting).
- **`riguet-ichimoku`**: Ichimoku Kinko Hyo, the Japanese all-in-one trend, momentum and support/resistance system (candlestick heritage).
- **`cfa-economics` ch04**: business cycle context for intermarket and sector rotation.
- **`cfa-ethics-gips`**: Standard V (diligence and a reasonable basis) applies when basing recommendations on technical signals.
