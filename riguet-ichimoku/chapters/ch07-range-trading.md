# Chapter 7: Range Trading (Le trading range)
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 3 "Le trading range" (charts 72–97, reconstructed as rule lists) | retail FX/CFD trader-educator

## Core Idea
When the cloud (Kumo) is flat the market is in a range, the Ichimoku lines stop being support/resistance and become the equilibrium of the range, and the high-probability trade is to fade the bounds after a rejection candle on strong volume. The author considers it the easiest and most profitable method because the stop sits just beyond the rejection wick and the target just before the opposite bound, giving risk/reward far above 2:1 (ch02).

## Frameworks Introduced
- **Range detection and rectangle drawing**
  - When to use: the cloud is horizontal on the chosen TF (ch04).
  - How: (1) enclose price in a rectangle (rectangles preferred to triangles); (2) draw each bound like any S/R line: link as many contact points as possible, using candle closes/bodies rather than wicks; (3) if no clean alignment exists, link what the chart gives (e.g. one body and the last low wick); (4) wicks that poke through a bound are reassurance that the zone is real support/resistance.
  - Why it works / failure mode: ranges last longer on higher TFs; a M15 range breaks far faster than an H4 range. Failure: trading it as a trend or using Ichimoku lines inside as S/R.
- **Complete versus partial rotation**
  - How: price usually travels bound to bound (complete rotation, "rotation complète"). Sometimes it stalls and reverses at the equilibrium zone formed by the aligned flats of Kijun/SSB/SSA/Tenkan (partial rotation, "rotation partielle"). You cannot know in advance which one will occur; target the opposite bound but adapt at the equilibrium.
- **Rejection candles: soulèvement and ressaut**
  - When to use: entry filter at the bounds.
  - How: soulèvement (upthrust) = candle with a high wick above the upper bound that closes back below it → sell. Ressaut (spring) = candle with a low wick below the lower bound that closes back above it → buy. Require strong tick volume on the candle. The author enters only after these.
  - Why it works: the wick plus volume reflects a fight between sellers and buyers at a key level; the close decides who won. If the close is back inside the range, the losing camp exits and the move toward the opposite bound accelerates. If the close is outside, the bound is broken and a trend signal appears instead.
  - Failure mode: volumes in FX/CFD are only broker (tick) volume; the author knows this is contested and relies on his own observation, so treat it as a filter, not a proof.
- **Entry, stop, target (range rule set)**
  - How: (1) enter at the close of the soulèvement/ressaut candle (almost never wait for the next candle); (2) stop a few pips beyond the wick extreme; (3) take profit a few pips before the opposite bound; (4) compute R:R, which is normally well above 2:1.
  - Consequence: with R:R ≥ 4 a streak of three losses is repaid by one win (see Worked Example).
- **Equilibrium management**
  - How: when price reaches the equilibrium zone: no signal, wait (candle closes only). Reversal candles at the equilibrium (hammer, engulfing, wide-bodied reversal marubozu, after stagnation) → probable partial rotation: move stop to break even (BE) or cash in. Continuation candles (bearish continuation in a short) → probable complete rotation: stop to BE and let the trade run. Candlestick patterns are interpretable only at the bounds and the equilibrium, nowhere else in the range.
- **Anticipation on lower TFs (aggressive entry/exit)**
  - How: drop one or two TFs (e.g. H4 → M15, skipping H1) and draw the higher-TF level. Enter on the lower-TF close of the rejection candle instead of waiting for the higher-TF close, which improves the ratio because the higher-TF candle may close far below the best price. Exit early the same way (a reversal on M15 at the H4 equilibrium).
  - **Golden rule: "the higher TF close always prevails over the lower TF close."** If you entered on M5 and the M15 or H1 close returns beyond the trigger level (the bound), exit immediately, even if the stop has not been hit; the M5 sell signal has become a buy signal on the higher frame.
- **Recovering a missed range move**
  - How: (a) if price rose past the equilibrium after a rebound at the lower bound, it will probably reach the upper bound; mark the interim resistance (horizontal) and buy its break on a lower TF when the higher TF close would be too late; (b) trade the sub-trends inside the range (channels supported by Ichimoku lines whose start and end are known thanks to the rectangle).
- **Optional entry-filter variant**: many traders fade the bounds without rejection or volume; the author says his success rate is much higher with both.

## Key Concepts
- **Borne haute / borne basse**: upper / lower bound of the range rectangle.
- **Zone d'équilibre**: middle of the range where the flat lines sit; "equilibrium".
- **Rotation complète / partielle**: bound-to-bound versus reversal at equilibrium.
- **Soulèvement**: wick above resistance, close below it (upthrust).
- **Ressaut (ressort)**: wick below support, close above it (spring).
- **Tick volume**: transaction count from the broker, not capital flow (contested; author uses it).
- **Break even (BE)**: stop moved to entry.
- **Reversal / continuation candles**: doji, shooting star, hammer, piercing, engulfing, evening/morning star, dark cloud.
- **Higher-TF close prevails**: exit rule when lower and higher closes conflict.
- **Sub-trend inside the range**: tradeable channel with known endpoints.

## Formulas & Reference Tables
- `R:R = (entry − target) ÷ (stop − entry)` for a short; reverse for a long. Stop = wick extreme + a few pips; target = opposite bound − a few pips.
- Breakeven win rate at ratio R: `p* = 1 ÷ (1 + R)`.

| Situation at/in the range | Action |
|---|---|
| Upper bound, soulèvement, strong volume | sell at the candle close; stop above wick; target just above lower bound |
| Lower bound, ressaut, strong volume | buy at the close; stop below wick; target just under upper bound |
| Bound hit without rejection candle | no trade (author) |
| Close beyond the bound | range broken: trend rules (ch08) |
| Stagnation at equilibrium | wait; stop to BE |
| Reversal candle at equilibrium | cash in or BE (partial rotation) |
| Continuation candle at equilibrium | BE, hold toward the bound |
| Lower-TF entry, higher-TF close back through trigger | exit immediately |

## Mental Models
- **Share of the cake**: sellers who hit the top take their part; buyers at the bottom want theirs; the wick-and-volume battle shows who holds the key level.
- **Follow the winning camp**: the close of the rejection candle names the winner.
- **Ratio buys serenity**: a fat R:R makes losing streaks irrelevant.
- **Aggressive does not mean reckless**: better entries are safer because the ratio improves.
- **Range lines are equilibrium, not walls**.

## Worked Example
**Range sell (author's levels; pair not named in the extracted text)**: sell after a soulèvement at 1.5656; the lower bound ~1.5460 is 196 pips below (author says about 195). With the stop a few pips above the wick, e.g. 40 pips risk, R:R ≈ 196 ÷ 40 ≈ 4.9.

**Loss-streak arithmetic**: at R:R = 4 and risk of 1 unit per trade, three losses = −3, one win = +4, net +1. Breakeven win rate = 1/(1+4) = 20%.

**Entry-timing arithmetic (USDJPY, illustrative levels, python-checked)**: bound 125.10 wick high with stop 125.15, target 124.10. Entry at the M5 close 124.98 → R:R = (124.98−124.10)/(125.15−124.98) = 5.2; waiting for the H1 close at 124.85 → 2.5; if the H1 candle closes at 124.65 → 1.1 (trade no longer worth taking). The book's example: the lower-TF entry at 124.98 versus 124.85 on the H1 close.

**Nested exit**: short on M5 at 9:10; M15 closes 9:15, 9:30, 9:45 below the bound: hold. H1 close at 10:00 above the bound: exit with a small loss, do not wait for the stop.

## Anti-patterns
- **Using Ichimoku lines as S/R inside a range** (except the equilibrium zone).
- **Fading a bound without rejection candle and volume**.
- **Reading candlestick patterns mid-range** (useless there).
- **Holding a lower-TF entry against a higher-TF close**.
- **Waiting for the next candle's confirmation** and losing the ratio.
- **Predicting complete vs partial rotation** instead of reading the candles at equilibrium.
- **Drawing bounds through wicks only** instead of closes/bodies.

## Practitioner Notes
- Style/TF guide: short-term trading ranges on M15; day trading M15–H1; swing H4–daily; weekly/monthly ranges are multi-month investments.
- Author claims never losing three range trades in a row; treat as anecdote.
- Ranges are the market's main state in the author's view (about 70%, ch04).
- When the first move was missed, cash in on the interim breakout or the sub-trend rather than chasing.
- Lower-TF anticipation is accepted to cost occasional small losses; it is paid for by the better ratio and the money management of ch02.
- Combined with the higher-TF range logic of ch06 (a flat cloud on a higher frame creates a bound-to-bound target).

## Key Takeaways
1. Flat cloud = range; box it with closes; lines become equilibrium.
2. Trade only soulèvement/ressaut with strong volume, at the close.
3. Stop beyond the wick, target just before the opposite bound.
4. At the equilibrium, wait and read candles; BE or cash in on reversal, BE and hold on continuation.
5. Anticipating on lower TFs improves the ratio but obeys the rule that higher-TF close prevails.
6. If you missed the entry, trade the interim resistance break or the sub-trend inside the range.
7. A close beyond the bound ends the range logic; switch to ch08.

## Connects To
- **ch02**: ratio and risk cap.
- **ch04**: flat cloud detection and twists.
- **ch05**: lines and Chikou do not block in a range.
- **ch06**: higher-TF range and bounds as targets.
- **ch08**: what happens when the range breaks.
- **ch09**: planning range break scenarios.
- **`passarelli-option-greeks` ch05**: premium-selling mindset (selling after a rejection) is the options analogue of fading bounds.
