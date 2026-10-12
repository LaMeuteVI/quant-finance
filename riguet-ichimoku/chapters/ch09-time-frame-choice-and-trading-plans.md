# Chapter 9: Choosing Time Frames and Building Trading Plans (Allons plus loin dans le process)
> **Source**: Patrick Riguet, *Ichimoku Kinko Hyo — La formation totale* (French), Part 3 "Quelles UT utiliser si l'on préfère…" and "Allons plus loin dans le process" (charts 115–134, reconstructed as rule lists) | retail FX/CFD trader-educator

## Core Idea
Ichimoku works on every time frame, so style (scalping, day trading, swing) does not dictate which frame you analyse: climb from any frame until levels appear, and a weekly chart can produce an intraday plan just as an M15 chart can reveal a swing plan. In practice there are two workflows: scan for a signal "here and now" (and abstain if none is valid) or, better, pre-build bullish and bearish trading plans with triggers, stops and targets, then wait for one to fire.

## Frameworks Introduced
- **TF-by-style defaults (the simple answer, which the author qualifies)**
  - Very short term / scalping: M1, M5, M15 (M15 main screen, H1 to validate and set the target, M5 for timing). Intraday: M15, H1, H4. Swing trading: H4, daily, weekly. He nevertheless says all roads lead to Rome and starts almost always from H4.
- **Key question on every chart**: "Is there free space in which to trade?" Orientation of the cloud first; then obstacles for price and Chikou; then a target.
- **Top-down plan extraction (weekly to intraday)**
  - How: (1) on the weekly, trace all important flats (extended right) under and above price; (2) copy them to the daily; delete the levels that sit inside a range; (3) on H4, spot sub-ranges (a flat, twisting cloud); (4) build a plan combining: a range-fade after a ressaut with volume, a Chikou break of a trend line to go long toward the range top, and a break of the range bottom to go short toward the next extended flat (e.g. SSB); (5) refine on H1 and M15 for entries.
- **Workflow 1: signal search "here and now"**
  - How: open the chart, read cloud orientation, look for an entry (breakout or pullback), validate by climbing (ch06), require R:R ≥ 2:1 (ch02), enter; if the signal is not validated, change asset. The author watches 20 to 25 assets, not to trade more but to raise the odds of finding one valid signal. Often there is nothing: patience and abstention are the strategy.
  - Overbought/oversold filter (from ch03): if price is far from Tenkan, do not buy a new-high breakout (or sell a new-low breakout). Wait for a pullback on Kijun (flat, no close beyond it) or for Tenkan to catch up. After a range break, price often returns to retest the bound, which also coincides with the flat Kijun (50% retracement).
- **Workflow 2: prepared trading plan (best option)**
  - How: (1) analyse top-down to identify a trigger level, a stop, and a chain of targets (flats and alignments on higher TFs); (2) prepare both a bullish and a bearish scenario for the same asset; (3) wait, possibly days or weeks, for a scenario to trigger; (4) on trigger, if price breaks close to the trigger the ratio allows a breakout entry; if far, wait for a pullback on Ichimoku lines which will have risen; (5) execute without opinion.
  - Why it works / failure mode: removes conviction and political/macro bias; the author says nobody knows which way the market will go, it is mass psychology, so the job is to read probabilities. Failure: impatience, or forgetting the plan (he cites a plan re-used a month later).

## Key Concepts
- **Scalping / day trading / swing trading**: M1–M15, M15–H4, H4–weekly (author's defaults).
- **Plan de trading**: pre-analysed scenario with trigger, stop and target.
- **Seuil de déclenchement**: trigger level of a plan.
- **Bullish and bearish scenarios**: both prepared, none favoured.
- **Space to trade (espace libre)**: distance between entry and the next barrier.
- **Equilibrium alignment**: Kijun flat + SSB flat marking a strong level.
- **Retest**: price returns to the broken bound or line (pullback).
- **Overbought/oversold vs Tenkan**: wait when price is stretched.
- **Abstention**: valid outcome of a scan.
- **Journal / forum / blog posts**: the author publishes trades in real time (not a source for numbers here).

## Formulas & Reference Tables
| Style | Main screen | Validate/target | Timing |
|---|---|---|---|
| Scalping | M1, M5, M15 | up to H1 | M1/M5 |
| Day trading | M15 | H1, H4 | M5 |
| Swing | H4, daily | weekly, monthly | H1/M15 |

| Plan element | Source |
|---|---|
| Trigger | break of range bound / swing extreme on candle close |
| Stop | beyond Kijun flats and prior swing (ch08) or beyond wick (ch07) |
| Target 1…n | extended flats and alignments on higher TFs |
| Skip if | R:R < 2 or obstacle for Chikou before target 1 |

## Mental Models
- **Plan the trade, then trade the plan**: analysis happens before the market moves, execution happens without opinion.
- **Many charts, few trades**: scanning widens the opportunity set, discipline narrows entries.
- **All roads lead to Rome**: frames are lenses; style governs the holding period, not the analysis TF.
- **Stretch = wait**: price far from Tenkan means pause or pullback is coming.

## Worked Example
1. **SP500 H4 (here and now)**: cloud up, but price far from Tenkan on H4 and daily (overbought). A buy on a new high is premature. A pullback to the H4 flat Kijun (an old resistance now support) could allow a long, but the weekly shows obstacles for price and Chikou between entry and the first target: probability very uncertain, abstain and look elsewhere.
2. **EURUSD M15 (here and now)**: after a range break, a sell signal; Tenkan accompanies the fall (no oversold) but price is far from the flat Kijun (50% retracement) and the broken bound. Wait for a pullback; the H1 shows strong oversold: do not enter and do not look higher.
3. **GBPUSD H4 (range)**: doji soulèvement above the upper bound, sell, stop above the wick, target 1 equilibrium, target 2 range bottom: very large ratio.
4. **USDJPY plan**: monthly chart shows Chikou at the SSB level; a H4 break of 105.50 targets 110 (aligned Kijun/SSB flats), then 112 (aligned SSA/mini SSB). Distance: 4.5 points to 110 and 6.5 to 112 (python-checked). The first trigger fired on a marubozu at 15:00, stop under Kijun flats and old lows, trade ran to 110; the second trigger fired a month later, to 112.
5. **USDCAD plan**: monthly retest of an old wick resistance turned support; if H4 breaks above 1.35, targets 1.37 and 1.39 (200 pips each); if the break is far from the trigger, wait for pullback on rising Ichimoku lines.
6. **EURUSD daily range plan**: price rejected at the top and dropped, now hits a horizontal support inside the range with many touches; on H1 a break leaves about 180 pips; plan for the next week, not on Friday 19:00.

## Anti-patterns
- **Forcing a trade on a chart because you opened it**.
- **Building a single directional conviction** from macro/news.
- **Chasing a stretched move away from Tenkan**.
- **Entering before checking weekly obstacles**.
- **Forgetting a plan** or trading it without rechecking the ratio at trigger time.
- **Trading late on a Friday evening** when you cannot watch.

## Practitioner Notes
- The author monitors 20–25 instruments; he does not monitor markets after 19:00 and avoids overnight positions.
- Plans commonly have multiple targets taken from aligned flats; after a target is reached, the plan for the next one may fire weeks later.
- Cloud, Chikou, flats and candle structures are the whole toolkit; no oscillators.
- Weekly or monthly analysis is also used for plan building even if the entry is on H4.

## Key Takeaways
1. Any time frame can start the analysis; climb until structure appears.
2. Always ask: is there free space between entry and the next obstacle?
3. Prepare bullish and bearish plans; execute on trigger without opinion.
4. Scan many assets; abstain when nothing validates.
5. Do not chase stretched moves; wait for Kijun pullbacks.
6. Targets come from aligned flats on higher TFs.
7. Skip when R:R < 2 or obstacles precede the first target.

## Connects To
- **ch01**: cold execution, abstention, plans against emotion.
- **ch02**: R:R and sizing for plans.
- **ch03**: overbought/oversold via Tenkan, elastic Kijun.
- **ch06**: climbing frames for validation/targets.
- **ch07**, **ch08**: execution rules for range and trend plans.
- **ch10**: archived real trades illustrating plans and errors.
- **`passarelli-option-greeks` ch17**: risk management mindset (trade only with an edge and defined risk).
