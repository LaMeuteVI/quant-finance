# Chapter 10: Archived Trades and Lessons (Exemples et analyses d'anciens trades)
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 3 "Exemples et analyses d'anciens trades archivés sur mon blog" (charts 135–143, reconstructed as rule lists) | retail FX/CFD trader-educator

## Core Idea
Real trades by the author show how the rules bend and break: the range method often takes profit before the opposite bound, candlestick reversal structures can substitute for a soulèvement, plan-based breakouts run straight to the next barrier, and the one trade that went wrong was caused by an emotional stop (too tight), not by Ichimoku. The takeaway is that rules are applied adaptively but the ratio and the stop discipline are never negotiated.

## Frameworks Introduced
- **Retest after a first trade**
  - When to use: after a range or trend leg is closed.
  - How: price returns to test a Kijun that has laid flat on the old range boundary; enter in the trend direction on the close after a reversal structure (e.g. a second star), take profit at the channel bound (DowJones H4 short, 459 points).
- **Candlestick substitute for the soulèvement**
  - How: if no soulèvement occurred, an evening-star / dark-cloud structure under resistance (double doji, evening star on the 1-minute EURUSD) can trigger the range short; stop above the highest wick above the range.
- **Adaptive take profit in a range**
  - How: exit before the opposite bound if an intermediate support will probably bounce, if the move was brutal, or if the session ends and you do not hold overnight (NZDJPY H4 range: exited at an intermediate support at 19:00, still with a strong ratio). "There are no dogmas."
- **Scalping version**
  - How: same rules on M1 with a trend line over the range's sub-trend; stay in the trade until price breaks that line again; exit about 10 pips before target if the candlesticks lose conviction (57 pips on EURUSD M1); buy after a piercing pattern preceded by a ressaut with rising volume. Scalping requires staying at the screen.
- **Plan-based breakout**: a marubozu through resistance from a prepared plan goes straight to the next barrier found on higher TFs (EURAUD H1).
- **Wide stops for violent instruments**
  - How: CAD pairs (oil correlated), EURNZD, GBPNZD, gold and oil produce "killer wicks"; use wider stops, enter on the breakout only if R:R ≥ 2 after the wider stop, otherwise wait for the pullback or let it go.
- **Never move a stop (the author's mistake)**: GBPCAD H4: he entered the breakout out of fear of missing the move, put the stop under Tenkan (too tight), lost 48 pips, then saw the idea reach target. Cause: greed and emotion. He did not widen the stop afterwards, because moving it breaks the ratio and a later loss would need more than one win to repay; at most a 5 to 6 point adjustment, exceptionally.

## Key Concepts
- **Ratio over pattern**: the R:R decides entry, not how good the candle looks.
- **Killer wicks (mèches assassines)**: spikes through stops on volatile instruments.
- **Intermediate support exit**: partial target inside the range.
- **Evening star / dark cloud (couverture en nuage noir) / double doji**: reversal structures used for entry.
- **Piercing (pénétrante) / hammer / ressaut with volume**: buy structures at the lower bound.
- **Range frequency**: author estimates ranges 70% of the time, hence more range trades than trend trades.
- **Overnight risk**: avoided; he stops watching at 19:00.

## Formulas & Reference Tables
| Trade | TF | Setup | Outcome |
|---|---|---|---|
| Dow Jones | H4 | retest of Kijun on old range bound, short after second star | +459 points, exit at channel bound |
| NZDJPY | H4 | range short after dark cloud | exit at intermediate support, 19:00 |
| EURUSD | M1 | range short after double doji/evening star | +57 pips, exit about 10 pips before target |
| EURUSD | M1 | long after piercing and ressaut with volume | lower bound trade |
| DAX | M15 | ressaut closing as hammer/doji | easy trade, excellent ratio |
| Dow Jones | M5 | hammer ressaut with volume | loss (rules accept this) |
| EURAUD | H1 | plan breakout on marubozu | ran to next barrier |
| GBPCAD | H4 | breakout, stop under Tenkan | −48 pips, emotional error |

## Mental Models
- **A loss inside the plan is not a mistake**; a loss from an emotional shortcut is.
- **Teaching is not trading**: theory says bound to bound, practice adapts.
- **A fat ratio absorbs the losers** (ch02, ch07).

## Worked Example
**Why not widen the stop (python-verified)**: suppose the planned stop is 30 pips and the target 66 (R:R 2.2). Widening the stop to 55 pips to survive a wick makes R:R = 66 ÷ 55 = 1.2, below the threshold; the correct choices are to skip, wait for a pullback, or enter with the wider stop only if a farther target keeps R:R ≥ 2. A loss of 55 versus a win of 66 needs a win rate of 1/(1+1.2) = 45.5% to break even versus 31.3% at 2.2.

## Anti-patterns
- **Entering out of fear of missing the move** and then using a tight stop.
- **Ignoring killer wicks** on CAD/NZD/gold/oil.
- **Holding scalps while away** from the screen.
- **Treating a pattern as exempt from the ratio**.
- **Reducing the stop after entry** or widening it beyond a few points.

## Practitioner Notes
- The author publishes trades in real time on his blog and forum with a journal; the book shows only a sample.
- Typical stop references: above the highest wick, beyond the range bound, under Tenkan/Kijun flats (breakouts), but add margin in volatile pairs.
- Frames used range from M1 to H4; the system is the same.

## Key Takeaways
1. Rules are templates; ratio and stop discipline are not.
2. Take profit at an intermediate support when the move is brutal or you cannot hold overnight.
3. Reversal candle structures can replace a missing soulèvement/ressaut.
4. Violent instruments need wider stops, which can change the ratio.
5. Never loosen a stop after entry; skipping a trade is better than breaking the ratio.
6. Losses from the method are normal; losses from emotion are the real enemy (ch01).

## Connects To
- **ch01**: emotional errors and journaling.
- **ch02**: why the ratio cannot be broken.
- **ch07**, **ch08**: setups used in the examples.
- **ch09**: plans behind the breakout trades.
- **`cfa-portfolio-management` ch14**: backtesting and why anecdotes (single trades) are not evidence.
