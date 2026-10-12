# Chapter 13: Delta-Neutral Trading: Trading Realized Volatility
> **Source**: Dan Passarelli, *Trading Option Greeks* (2nd ed., Wiley/Bloomberg 2012), Ch. 13 · Volatility

## Core Idea
Delta-neutral trading is really gamma trading. The long-gamma trader scalps stock (sells rallies, buys dips) to earn realized volatility and must out-earn theta every day; the short-gamma trader collects theta and must limit losses from adverse delta creep. Realized volatility (annualized standard deviation of daily moves), not net price change, drives both sides.

## Frameworks Introduced
- **Gamma scalping (long gamma)**: re-hedge deltas back to zero as the stock moves, locking profits on each swing.
  - When to use: you expect realized vol above what the options' IV/theta price in; the stock has been swinging intraday.
  - How: buy ATM calls, short stock delta-neutral. As price rises, position delta turns positive, sell stock to flatten; as it falls, delta turns negative, buy stock to flatten. Each hedge banks `Δ_created × move / 2` (average delta over the move). Compare the day's scalp profit with the day's theta.
  - Failure mode: quiet or trending-then-reverting tape; weekends and holidays (theta accrues, no scalping); covering too soon in a trend.
- **Gamma-vs-theta ledger**: daily P&L ≈ scalp profit (gamma) minus theta. A winning day means scalps exceed theta.
- **Going home flat**: at day end, cover residual deltas to be neutral so overnight risk stays volatility, not direction.
- **Gamma hedging (short gamma)**: hedge only enough to avoid runaway adverse deltas, not to "negative scalp" every wiggle.
  - Tools: partial hedges (cover half), over-hedging when a trend is expected, hedge triggers based on daily standard deviation from IV, market feel.
  - Trade-off: short-gamma traders always lock in a loss when hedging (buy after rises, sell after falls); long-gamma traders always lock in a gain.
- **25% IV benchmark**: gamma and theta come from the IV input. In the chapter's 25 IV example, if realized vol is below 25 the long-gamma trade is hard and the short-gamma trade is easier; above 25 the reverse.
- **Smiley and frown P&L diagrams**: positive gamma before expiry gives a "smile" (profit grows with movement in either direction, center sinks with time); negative gamma gives a "frown" (peak profit at zero at inception, center rises as time passes). Rising IV lifts the smile and lowers the frown, falling IV does the opposite.

## Key Concepts
- **Realized (statistical/historical) volatility**: annualized standard deviation of daily price changes; can be high with zero net price change.
- **Gamma scalping**: profitably re-hedging a long-gamma position on intraday swings.
- **Negative scalping**: re-hedging a short-gamma position; each hedge realizes a loss.
- **Position delta drift**: delta created by gamma = gamma × move.
- **Average-delta rule**: P&L on gamma-created delta over a move = ½ × created delta × move.
- **Going home flat**: neutralizing delta at the close.
- **Gap risk**: an overnight or opening jump leaves no chance to hedge along the way; it helps long gamma exponentially and hurts short gamma.
- **Theta as operating cost**: the daily expense of running the gamma-scalping business.
- **Smiley / frown**: shape of the pre-expiry P&L curve of long / short gamma.
- **Over-hedging**: hedging more than the net delta in anticipation of continued trend.
- **Not zero-sum**: two counterparties with mirror positions can both hedge differently and end with different dollar results.

## Formulas & Reference Tables
- Delta created by gamma: `ΔΔ = Γ × ΔS` (Γ in deltas per $1, position basis).
- Scalp profit for a hedged move: `≈ ½ × Γ × ΔS × ΔS` per unit (average delta = half the created delta).
- Position P&L with net delta Δ₀: `Δ₀·ΔS + ½Γ(ΔS)² + Θ·t`.
- Break-even daily move (long gamma, per 100-share units): `ΔS* ≈ √(2·Θ$ / (Γ·100))`. Example: Θ$ = 50, Γ = 2.80 gives 0.60, close to the 25%-vol daily 1σ move of about $0.63 on a $40 stock (40 × 0.25 / √252). This is the same idea as "IV is the market's break-even".
- Hedge size: `shares = |Δ_position| × 100`.

| 20-lot ATM call, $40 stock | 25 IV | 50 IV |
|---|---|---|
| Gamma | 2.80 | 1.40 |
| Theta | 0.50 ($50/day) | 0.90 ($90/day) |

## Mental Models
- **Long gamma is a business: revenue = scalps, expense = theta.** Track daily revenue vs cost, and remember weekends are expense-only days.
- **Delta hedge = profit lock for the long, loss lock for the short.**
- **Sell vol on quiet names, buy vol on names that move more than the option prices imply**; IV is the bar realized vol must clear.
- **Gaps are the long-gamma trader's jackpot and the short-gamma trader's nightmare**: the bigger the gap, the more the average-delta gain (or loss) grows, roughly quadratically.
- **Don't scalp what you shouldn't**: the best short-gamma trade is sometimes no trade (Mary on day one).

## Worked Example
Harry (long gamma): buys 20 ATM 40-strike calls, short 1,000 shares at $40. Γ = +2.80, Θ = -$50/day. First week:

| Day | Action | Scalp/gamma profit | Theta | Net |
|---|---|---|---|---|
| 1 | Stock 40 to 42: sell 560 at 42; back to 40: buy 560 | 560 × 2 = 1,120 | -50 | +1,070 |
| 2 | Drops 0.40: buy 112 at 39.60; sells 112 at 40 | 112 × 0.40 = 45 | -50 | -5 |
| 3 | Trends up in 0.50 steps: four sells of 140 | 4 × (140 × 0.50 / 2) = 140 | -50 | +90 |
| 4 | Gap down 4: buy 1,120 at 38 | 1,120 × 4 / 2 = 2,240 | -50 | +2,190 |
| 5-6 | Weekend | 0 | -100 | -100 |
| 7 | Up 0.25: sell 70 at 38.25 | 70 × 0.25 / 2 = 9 | -50 | -41 |

Week total about +$3,204: three winning days, four losing (weekend counted). One gap paid for the week. Recomputed: 1,070 - 5 + 90 + 2,190 - 100 - 41 = 3,204.

Mary (short gamma, mirror trade) over the same tape: day 1 no hedge, +50; day 2 no hedge, +50; day 3 hedged 280 at 41 and 280 at 42, -280 + 50 = -230; day 4 gap down, sold only 560 of the 1,120 to cover, -1,120 (locked) -1,120 (open) + 50 = -2,190; weekend +100; day 7 +181. Week about -$2,039 (Mary: 50+50-230-2,190+100+181). Lesson: selling vol on a stock that moved above the 25% benchmark.

## Anti-patterns
- **Buy-and-hold a gamma trade**: it needs active monitoring; it is a trading technique, not a position.
- **Ignoring the theta budget**: high-IV stocks have lower gamma and higher theta; volatile is not automatically profitable.
- **Covering deltas too early in a trend (day 3)**: gives up trend profit; too late risks giving back the swing.
- **Over-trading a short-gamma book**: every hedge realizes a loss; negative scalping bleeds.
- **Taking a directional lean unintentionally**: skipping the flat-at-close rule adds direction risk.
- **Assuming constant gamma in big moves**: the chapter examples hold gamma constant purely for simplicity.
- **Reading the seller's loss as the buyer's gain**: hedging discipline differs, so P&L is not zero-sum.

## Practitioner Notes
- Hedge-trigger methods named by the author: daily standard deviation, fixed percent of price, fixed dollar amount, time of day, market feel. No method dominates; test per stock.
- Short-gamma traders often hedge partially (cover half the delta) and may deliberately carry a delta bias over a weekend.
- Realized 25% or more is the break-even zone in the 25-IV setup, not a guarantee.
- Position P&L, not leg P&L, matters; monitor net delta and gamma. Use scenario graphs with days-to-expiry as a variable.
- Option-selling delta-neutral strategies work in low-vol regimes; small moves are fine, big moves blow you up.

## Key Takeaways
1. Delta-neutral with gamma is gamma trading: your delta changes every tick.
2. Long gamma: sell strength, buy weakness, and beat theta each day.
3. Break-even is set by the IV in the option price; compare with realized vol on the stock.
4. Weekends and holidays are pure theta cost for long gamma.
5. Gaps disproportionately reward long gamma and punish short gamma.
6. Short gamma: hedge selectively (partial or trend-based) instead of scalping every move.
7. Go home flat unless a directional lean is deliberate.
8. Smile vs frown diagrams show why: long gamma is hurt by time, short gamma by movement.

## Connects To
- **ch12**: the implied-volatility side of the same delta-neutral trades.
- **ch14**: volatility charts to compare IV with realized volatility.
- **ch15**: straddles and strangles as the purest gamma-scalping vehicles.
- **ch02**: gamma and theta definitions.
- **ch17**: how the greeks shape live trade decisions.
- **`hull-derivatives`**: dynamic delta hedging, gamma-theta relationship.
