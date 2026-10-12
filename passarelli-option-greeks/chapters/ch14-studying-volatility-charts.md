# Chapter 14: Studying Volatility Charts
> **Source**: Dan Passarelli, *Trading Option Greeks* (2nd ed., Wiley/Bloomberg 2012), Ch. 14 · Volatility (charts courtesy of iVolatility.com: gray = 30-day realized, black = IV)

## Core Idea
A volatility chart overlays implied volatility (IV) and 30-day realized volatility (RV) so you can see whether options are cheap or rich relative to (a) the stock's own movement and (b) their own history. The relationship between the two lines, in nine combinations of "rises / constant / falls", tells you whether the gamma-to-theta bargain favors buyers or sellers and whether the move is event-driven or noise.

## Frameworks Introduced
- **What a vol chart answers**: (1) Was the past 30 days more or less volatile than usual? (2) What is the stock's typical RV range? (3) How much RV did the stock show around recurring events? Also: is IV high or low vs its own past?
- **The Nine Volatility Chart Patterns** (RV move, IV move):
  1. **RV rises, IV rises**: active, news-heavy stocks (tech-bubble names, story stocks, panic markets like summer 2011). Three variants: IV up more, RV up more, equal. Example: IV 50, RV 35 in late July. Buy only if RV likely to catch up (news pending); if no news, IV outrunning RV signals exuberance and a possible short-vol trade (wild ride, negative gamma dangerous). Sharp temporary IV jump = **spike**; one-day RV surge that persists 30 days then drops = **realized volatility mesa**.
  2. **RV rises, IV constant**: a one-off move already priced in, or RV catching up to a stable IV (IV 25, RV lagging then rising through 25 in May). Early long-vol buyers bled theta; sellers just before the rise lose on gamma with no IV crush to help.
  3. **RV rises, IV falls**: two cases. Slow crossover (IV drifting lower to cross RV, IV at 35 near bottom of its 4-month range) = buy value (favorable gamma/theta and cheap vs history). Sharp version = earnings crush: buying delta-neutral the day before loses about 10 vega points but positive gamma can more than compensate (RV nearly doubled, 28 to 53 in one day).
  4. **RV constant, IV rises**: atypical (usually RV fades pre-event). With no news, sell IV 5 to 10 points above RV (RV 20 to 24, IV from 24 to over 30) for theta and IV fall convergence.
  5. **RV constant, IV constant**: boring stock; IV often trades slightly above RV for long stretches (example IV high teens, RV low teens). Favors option sellers by gamma/theta: short call plus long stock delta-neutral, time spreads, iron condors. Not a guarantee: negative scalping and trending moves hurt; pair with a price chart.
  6. **RV constant, IV falls**: classic convergence, driven by arbitrage. Gaps of 1 to 3 points persist; 7 to 10 points (IV 33 collapsing to 22) cannot. Slow versions come from market makers capitulating on long vol and lowering offers.
  7. **RV falls, IV rises**: the classic IV rush (earnings; FDA binary events for small biotechs, where the IV-RV gap can reach hundreds of points). Predictable but hard to trade: vega and gamma pull opposite ways as they converge; many traders skip earnings.
  8. **RV falls, IV constant**: crossover ambiguity. Options market reacts to stock volatility, not vice versa. When IV rises or falls, look to the underlying for the reason. Falling vol usually means lack of news. Hard to sell when IV is cheap vs history, hard to buy when IV above RV. Adjust hedge intervals as vol ebbs (e.g. from $0.50 to $0.40).
  9. **RV falls, IV falls**: end of a highly volatile period (IV 75 to 55, RV from low 50s to under 25); reversion to the mean, IV stays a bit above. If the stock has changed fundamentally (spin-off, merger) and history is unreliable, benchmark against similar stocks in the same industry.
- **Gamma/theta edge rule**: buy vol when IV is below RV (and not at the top of its own range); sell when IV is above RV for no news reason. Edge is statistical, not certain.
- **Hedge-interval calibration by chart**: IV-based one-day standard deviation can cause early covering when RV > IV and late covering when RV < IV.

## Key Concepts
- **Implied volatility (IV)**: market's price of future volatility.
- **Realized (historical, statistical) volatility**: annualized standard deviation of recent price changes (here 30 business days).
- **Spike**: sharp temporary IV jump.
- **Realized volatility mesa**: one-day RV step that stays elevated for 30 days then drops equally fast when the shock leaves the window.
- **Convergence / divergence / crossover**: lines approaching, separating, or swapping order; a crossover can signal cheap or rich IV.
- **Rush and crush**: event-driven IV up then collapse.
- **Reversion to the mean**: IV and RV drift back to a typical band.
- **Gamma/theta ratio**: how much gamma you get per unit of theta; favors sellers when IV >> RV.
- **Peer benchmarking**: substitutable stocks in the same industry trade at similar volatilities.
- **Negative scalping**: paying to hedge short gamma on oscillating stock.
- **Options follow the stock**: IV reacts to stock volatility, not the other way.

## Formulas & Reference Tables
- One-day 1σ move: `S × IV / √252` (IV-implied) vs the actual daily standard deviation from realized vol.
- Long-vol break-even: gamma scalps must cover theta; IV < RV tilts odds to the buyer.

| RV \ IV | IV rises | IV constant | IV falls |
|---|---|---|---|
| **RV rises** | 1: news/active; buy only if RV catches up, else consider selling | 2: RV catching up; buyer wins late, early buyers bleed | 3: value buy or earnings crush (gamma beats vega) |
| **RV constant** | 4: sell IV 5-10 pts above RV if no news | 5: sellers' gamma/theta edge | 6: arbitrage convergence |
| **RV falls** | 7: earnings/FDA rush; hard to trade | 8: ambiguous crossover; watch history | 9: end of volatile period; reversion |

## Mental Models
- **Read the pair, not one line**: cheapness is relative to RV now and to IV history.
- **RV moves first, IV follows**: search the underlying for the reason when IV moves.
- **Big IV-RV gaps get arbitraged**: 1 to 3 points can persist, 7 to 10 will not.
- **A 30-day RV line is a moving window**: a single big day sits in the calculation for 30 days and then vanishes (mesa).
- **Every ship on the bottom of the ocean has a chart**: use the chart plus a price chart plus news, then hedge accordingly.

## Worked Example
Pattern 3 (earnings crush), from the chapter's numbers: RV jumps from about 28 to 53 in a day, IV falls about 10 points. A delta-neutral long with vega +1.20 loses `10 × 1.20 = 12.0` (about $1,200 per 20-lot in 100-share units) on vega, but if the stock moves enough that `½·Γ·(ΔS)²` exceeds 12.0 plus theta, the trade still wins. With Γ = 1.80 that needs `ΔS ≈ √(2 × 12.0 / 1.80) ≈ 3.65`, about a $3.65 move. Recomputed: 2 × 12 / 1.8 = 13.33, square root 3.65. Interpretation: an earnings long-vol trade needs a bigger move than the IV crush implies, which is why pattern 7 is "hard to trade".

Example for pattern 4: RV 22, IV 30. Sell a delta-neutral ATM call; gain from theta and IV convergence if IV falls 6 points; with vega -1.15, expected vega gain about 6.9 (about $690 per 20-lot).

## Anti-patterns
- **Buying vol early on a pattern-2 chart**: theta kills before RV catches up.
- **Selling vol just because IV > RV on a stock with news pending**: patterns 1 and 7 punish short gamma.
- **Treating a mesa drop as calming**: the RV decline is just a shock leaving the window.
- **Using one hedge interval regardless of regime**: adjust to current RV.
- **Trading crossovers mechanically (pattern 8)**: check IV vs its own history first.
- **Ignoring peers when a stock has changed fundamentally**: history may not define its mean.
- **Trading earnings just because the pattern is "predictable"**: vega and gamma offset.

## Practitioner Notes
- Standard iVolatility-style charts: black IV, gray 30-day RV; study 6 to 12 months for range.
- IV usually sits 1 to 3 points above RV for extended periods in normal names; sell/buy triggers need a gap well beyond that.
- Combine the vol chart with a stock price chart to time hedges and to see whether volatility came from trending or oscillating price.
- Many traders avoid earnings altogether for the simpler patterns (5, 6, 4).
- Rising IV without news and constant RV is one of the cleaner "sell" tells; RV crossing above steady IV after a long lag is a "buy" tell.

## Key Takeaways
1. Read IV against both RV and IV's own history.
2. Nine patterns: RV (up, flat, down) x IV (up, flat, down).
3. IV above RV with no news favors selling; IV below RV and cheap vs history favors buying.
4. Big IV-RV gaps close via arbitrage; expect convergence.
5. Earnings patterns (3 and 7) pit vega against gamma; sizing matters more than direction.
6. RV mesas are artifacts of a 30-day window.
7. Adapt hedge spacing to the current RV regime.
8. Use industry peers as a volatility benchmark when history is unreliable.

## Connects To
- **ch03**: definitions of IV, HV, reversion to the mean, one-day standard deviation.
- **ch12**: rush and crush trades on the pattern 3 and 7 charts.
- **ch13**: gamma scalping and short-gamma hedging under these regimes.
- **ch15**: straddles and strangles in each pattern.
- **ch17**: how volatility signals feed into live decisions.
