# Chapter 5: Chikou Span, the Filter, and the Global Reading
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 2 "Chikou-span — le filtre du système" and "Ichimoku Kinko Hyo — vue globale" | retail FX/CFD trader-educator

## Core Idea
Chikou span (lagging span), the close plotted 26 periods back, is the filter of the system: a price signal is valid only if Chikou is free of obstacles at the same moment. The author calls this an absolute rule and says he almost always lost trades when he ignored it. Combined with cloud orientation it gives the global reading: trend up, trend down, or range.

## Frameworks Introduced
- **Chikou filter rule (validation of every signal)**
  - When to use: for every candidate entry, on the signal time frame and on the higher ones.
  - How: (1) detect a price signal (breakout, pullback entry); (2) look at where Chikou sits: is there anything in the way in the direction of the trade? Obstacles: flats of Tenkan, Kijun, SSA, SSB and their extensions, the cloud itself, candle bodies and wicks of the old price, chartist trend lines and channel bounds; (3) if Chikou is free → signal valid; if blocked → abstain; wait for Chikou to break the obstacle.
  - Why it works / failure mode: Chikou is a piece of market memory; it meets the same support/resistance that price would face over the coming 26 bars. Failure: in a range almost nothing blocks Chikou (and nothing blocks price), so the filter must be read together with the regime.
- **Global reading table** (see below): cloud orientation + lines + Chikou.
  - When to use: the routine first look.
  - How: oriented cloud → trend; buy (or sell) new extremes or pullbacks using the lines as S/R; flat cloud → the lines become the equilibrium of the range, not S/R; range: abstain or trade the range.
- **"Wait for Chikou to break the obstacle"**
  - When to use: price has already broken a line but Chikou has not.
  - How: do not enter on price alone; the entry time is when Chikou clears (e.g. breaks the trend line) and price follows; entering earlier usually gets the immediate pullback.

## Key Concepts
- **Chikou span (遅行スパン)**: closing price shifted back 26 periods; built from closes only, wicks are ignored (it touches the wick extreme while the candle is open, then reverts to the close).
- **Filter (filtre)**: Chikou validates or invalidates price signals.
- **Obstacle**: anything in Chikou's path: flats (Tenkan, Kijun, SSA, SSB), cloud, candles, oblique trend lines, horizontals.
- **Market memory**: Chikou reveals where past price acted as barrier; same levels as for price.
- **Free Chikou (libre de tout obstacle)**: no obstacle on the side of the trade.
- **Range exception**: lines stop being S/R both for price and Chikou.
- **Channel bound / oblique**: a chartist line that Chikou can "surf" along as an obstacle.
- **Confirmation on candle close**: signals are confirmed only at the close of the candle.
- **Global view**: cloud orientation plus price position relative to lines and Chikou.

## Formulas & Reference Tables
- `Chikou plotted at t−26 = Close_t`; it is computed only from closes.
- Comparing Chikou at bar t−26 with price: Chikou is above price 26 bars ago → bullish filter; below → bearish filter (implied by the obstacle logic; the book frames it as "free of obstacle").

| Situation | Reading | Action |
|---|---|---|
| Signal long, Chikou free above | valid | proceed to ch06 checks and R:R |
| Signal long, Chikou under a flat/cloud/candle cluster | invalid | abstain, wait for Chikou break |
| Signal short, Chikou blocked by a trend line | invalid | wait for Chikou to break the line |
| Range (flat cloud) | lines not S/R | range logic (ch07) |
| Oriented cloud, price above, flats holding | trend up | longs on new highs/pullbacks, stops under flats |

## Mental Models
- **Chikou as a scout**: it tests the same terrain as price will, 26 bars earlier than price reaches it on the right.
- **Price proposes, Chikou disposes**: entry = price signal AND free Chikou.
- **Everything is an obstacle**: not only Ichimoku lines but trend lines and candles count.
- **Regime switch**: apply the filter strictly in trends, read lines as equilibrium in ranges.

## Worked Example
Author's cases (scenarios reconstructed as rule lists):
1. Price attempts to break a resistance with a strong marubozu but Chikou sits under SSB: signal rejected; price fails to cross.
2. Price breaks a bearish trend line but stalls; at the same time Chikou faces that same oblique: no short until Chikou breaks it (1-minute chart). Entering on the candles that broke price first would have met the immediate retracement and likely the stop.
3. Daily GBPUSD: price breaks a range on H4 above a line; on the daily Chikou would still be under price candles → no entry; wait for the daily highs to break, letting Chikou clear (checks higher TF, ch06).
4. Monthly USDJPY: long flat SSB aligned with Kijun flat blocks price and Chikou at the same time; months of stall.

## Anti-patterns
- **Entering without checking Chikou** ("I can skip it this once").
- **Reading wicks into Chikou**: only closes.
- **Applying flats as obstacles in a range** (they are not).
- **Ignoring non-Ichimoku obstacles** (trend lines, candles, horizontals).
- **Entering on the price break when Chikou is still blocked**.

## Practitioner Notes
- The rule is called "absolute and fundamental" by the author; he admits violating it in the past and "almost always" losing.
- Chikou is checked on the signal TF and again on higher TFs (ch06).
- The author combines Ichimoku with basic chartism (horizontals, oblique lines, channels) and candlesticks; he says Ichimoku can be used alone but is stronger with them.
- The system works on all timeframes; a 1-minute example is used to show the filter.
- Global reading examples: SP500 weekly (oriented up, Kijun supports; when Kijun failed SSA took over), EURUSD daily (down; Kijun repeatedly overrun so check reactions), DowJones H4 (flat cloud → range, lines unreliable).

## Key Takeaways
1. Chikou = close shifted 26 bars back; only closes count.
2. A price signal is valid only if Chikou is free of obstacles in the trade direction.
3. Anything blocks Chikou: flats, cloud, candles, trend lines.
4. If Chikou is blocked, abstain and wait for it to break the obstacle.
5. In a range the lines no longer block price or Chikou.
6. Global view: cloud orientation first, then lines, then Chikou.
7. Do not assume Kijun always holds in trends; verify reactions.

## Connects To
- **ch03**: the flats that block Chikou.
- **ch04**: the cloud edges that block Chikou.
- **ch06**: apply the filter on the signal and higher TFs.
- **ch07**: range exception.
- **ch08**: use the filter in trend entries.
- **`cfa-portfolio-management` ch09**: confirmation with independent technical evidence.
