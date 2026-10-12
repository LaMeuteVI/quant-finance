# Chapter 6: Multi-Timeframe Navigation (Navigation sur plusieurs unités de temps)
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 2 "La navigation sur plusieurs unités de temps" (charts 37–71, reconstructed as rule lists) | retail FX/CFD trader-educator

## Core Idea
Except in rare cases, Ichimoku is never read on one time frame. A signal detected on time frame X (UT, unité de temps) is validated or invalidated on the next higher frames, the same climb supplies the profit target, and lower frames refine entry timing. The method is a loop: detect, climb until obstacles appear, trace them, come back down, size the trade from the stop and the target (ch02).

## Frameworks Introduced
- **Validation climb (signal TF to higher TF)**
  - When to use: every candidate signal (breakout of a new high/low in a trend, pullback entry, range break).
  - How: (1) on the signal TF check cloud orientation and that nothing blocks price or Chikou (ch05); (2) move to the next higher TF and test the same two things: any flat Tenkan/Kijun/SSA/SSB, cloud edge, candle cluster or trend line in front of price, and in front of Chikou; (3) no obstacle on that TF: signal confirmed, but if the frame shows nothing at all (no lines in view) keep climbing; (4) obstacle present: signal invalid, wait until the obstacle clears on a candle close.
  - Why it works / failure mode: higher-TF levels carry more weight and the filter (Chikou) must be free there too. Failure: stopping the climb at a frame that is simply empty (no information is not confirmation).
- **Target search by climbing**
  - When to use: after the signal is validated, to find the take profit.
  - How: step up one TF at a time until Ichimoku lines show above price (long) or below (short). Trace each old flat as a horizontal extended to the right (plat en extension). Alignments of several flats at one price (Tenkan + Kijun + SSA + SSB) mark the strongest target; a line joining aligned flats on a monthly chart is the main objective, the first weekly flat the secondary. The target is then displayed on every lower TF.
  - Why it works / failure mode: the author states "the more flats aligned, the stronger the S/R". Failure: ignoring right-angle corners of Ichimoku lines ("pointes"), which he calls overlooked traps and strong levels.
- **Zoom-out limit rule**
  - When to use: deciding how far to look for flats on one frame.
  - How: zoom out while details stay legible; when they become too small, switch to the next higher TF instead of squinting.
- **TF ladder**: M15 → H1 → H4 → daily → weekly → monthly. The author skips M30, H2, H8 and similar intermediate frames, other traders do not.
- **Range-on-higher-TF logic**
  - When to use: the signal TF is trending but a higher TF shows a flat cloud (range).
  - How: box the range; prices tend to travel from one bound to the other; the bound is a strong S/R and only a candle close beyond it signals continuation. Take profit near the bound, or hold only if the bound breaks on a close and raise the stop to just under it. Equilibrium of the range (the flat Kijun of the higher TF) is the barrier for a partial rotation.
- **Descent for timing**: after validation and target, drop to a lower TF (e.g. M15) to draw the trigger level (recent highs/lows), enter on candle close, and verify R:R ≥ 2:1 (ch02).

## Key Concepts
- **Time frame (UT, unité de temps; TF)**: chart period.
- **Signal TF**: the frame where the trade idea appears.
- **Validation**: no obstacle for price and Chikou on higher frames.
- **Plat en extension**: a flat of an Ichimoku line projected horizontally to the right.
- **Alignment of flats**: several flats of different lines at the same price; the stronger the more lines.
- **Pointe / angle droit (corner)**: the corner where a flat meets the slope; strong S/R and trap zone (SSA corner, Tenkan corner).
- **Range on higher TF (rotation)**: flat cloud; partial rotation reverses at the equilibrium, complete rotation goes bound to bound (detail in ch07).
- **Candle-close confirmation**: always enter at the close, never during the candle.
- **Wick caution**: a breakout candle with a long wick below its body is a weak entry; prefer wickless or almost wickless breakout candles.
- **Reversal candles on lower TF**: used to cash profits near a higher-TF barrier or to fade a range bound in anticipation.
- **Elastic effect**: price far from a higher-TF Kijun invites a return (ch03), a reason to abstain after an extended move.

## Formulas & Reference Tables
| Question | Where to look | Decision |
|---|---|---|
| Is there a trend? | cloud orientation on each frame | oriented: trend; flat: range |
| Is the signal valid? | next higher TF: obstacles for price AND Chikou | none: valid; any: abstain |
| Target? | climb until lines appear; trace flats | nearest strong line or alignment |
| Entry timing? | lower TF break of recent extreme | at candle close |
| Is the trade worth it? | `R:R = (target − entry) ÷ (entry − stop)` | ≥ 2 (ch02) |

## Mental Models
- **Zoom ladder**: each TF is a lens; use the lowest one that shows structure.
- **Higher TF owns the obstacles, lower TF owns the timing**.
- **Empty is not clear**: a frame without lines tells nothing; go up.
- **Targets live on the frame where the lines are, not where you trade**.
- **Probabilities, never certainties**: the author stresses every statement as a probability.

## Worked Example
Reconstructed cases (author's reading):
1. **USDJPY long (M15)**: cloud up, candle closes above a recent high, nothing blocks price or Chikou. H1: free. H4: cloud flat, price near the top of a range, no line blocking. Decision: take the roughly 18 pips and exit, or keep the position only if the H4 candle closes above the bound, with the stop a few pips under the bound. Daily (also flat) shows price rising from the lower bound toward the upper bound, with two resistances on the way (an extended Tenkan flat and a price resistance), which become the targets after a break. Reversal candles under the H4 bound on M15 mean: cash in.
2. **AUDUSD short (H4)**: downtrend, price sitting on support. Daily: no obstacle (signal valid) but no target. Weekly: lines appear. Monthly: aligned Tenkan, Kijun and SSA flats joined by one line = objective, drawn back on H4. Entry would use M15 candle-close break with R:R ≥ 2.
3. **GBPUSD (H4 flat cloud)**: break of the H4 range upward is not tradable because on the daily Chikou still sits under old candles and an SSA/Tenkan corner lies ahead; wait for the daily highs to break.
4. **USDCAD long above 1.32 (daily)**: weekly shows nothing blocking above 1.32 and a first flat at about 1.3250; monthly main target 1.3360. Entering on the daily close above 1.32 cannot reach 2:1 toward 1.3250 (too late); a daily close above 1.3250 could target 1.3360, or enter on H4 for the ratio.
5. **NZDUSD short**: H4 breaks support; daily confirms downtrend without target; weekly SSB flat gives 0.6330; M15 break of lows at candle close gives entry for a minimum 2:1; target reached to the pip (author's account).

## Anti-patterns
- **Trading the signal TF alone**: you will not see the obstacle that is the real ceiling.
- **Treating an empty frame as confirmation**.
- **Entering during the candle**.
- **Buying after an extended move far from Kijun** because the TFs "agree".
- **Entering breakouts on candles with long wicks**.
- **Ignoring corners (angles) of the lines**.
- **Forgetting that Chikou must also be free on the higher TF**.

## Practitioner Notes
- The method is a checklist for every trade, not an optional extra: validation, then target, then timing.
- Targets are placed just before the strong line, not on it (stops and targets are detailed in ch07 and ch08).
- Ratio constraint decides the entry TF: if the ratio is not reachable at the signal TF after the close, move down a TF or wait for the next barrier break.
- Japanese candlestick reversal structures at S/R are the author's complement for exits and anticipations; he recommends Nison for the subject.

## Key Takeaways
1. Detect on one TF, validate on the next higher TF, climb until lines appear.
2. Validation means no obstacle for price and for Chikou on those frames.
3. Targets are old flats extended to the right; alignments mean strength.
4. A higher-TF flat cloud means treat that frame as a range with bounds as S/R.
5. Use lower TFs only for timing; enter on the close.
6. Require R:R ≥ 2:1; if not reachable, abstain or move TF.
7. Skip intermediate TFs (M30, H2, H8) in the ladder, per the author.

## Connects To
- **ch02**: R:R threshold used to accept or refuse the entry.
- **ch03**: flats and elastic effect that form obstacles.
- **ch04**: cloud orientation and twists on each TF.
- **ch05**: Chikou filter applied at every frame.
- **ch07**: what to do when a frame shows a range.
- **ch08**: executing validated trend signals.
- **`cfa-portfolio-management` ch09**: generic technical analysis concepts (support/resistance, trend).
