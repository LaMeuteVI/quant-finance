# Chapter 12: Delta-Neutral Trading: Trading Implied Volatility
> **Source**: Dan Passarelli, *Trading Option Greeks* (2nd ed., Wiley/Bloomberg 2012), Ch. 12 · Volatility

## Core Idea
Delta-neutral trading is not a strategy but a way to strip direction out of any option position by adding or shorting stock, so that what remains is a bet on volatility (gamma/theta for realized vol, vega for implied vol). The canonical implied-vol play is the earnings "rush and crush": IV rises into a known event and collapses after it, and the trade is judged (and post-mortemed) by greek P&L attribution, not by leg-by-leg prices.

## Frameworks Introduced
- **Direction neutral vs direction indifferent**: two non-directional views.
  - Direction neutral: expects no trend; deltas near zero; movement hurts (short iron condors, long time spreads, OTM credit spreads). Negative gamma is the enemy.
  - Direction indifferent: wants movement but not its sign (long gamma), or trades IV itself, or harvests carry (conversions, reversals, boxes, dividend plays).
- **Delta-neutral construction**: net option deltas to zero with stock.
  - How: position delta = Σ(contracts × delta × 100) ± shares. Buy 20 calls of 0.50 delta = +1,000 deltas, short 1,000 shares. Stock changes only delta, not gamma/theta/vega.
  - Why it works: with delta flat, the position's P&L is driven by gamma (realized vol), theta (time) and vega (IV). Long calls + short stock has a V-shaped expiry payoff: profit needs a move big enough to recoup the premium.
- **Rush and crush**: IV climbs before a widely anticipated binary event (earnings, FDA) as insurance demand rises, then collapses 10-20+ points within minutes of the news.
  - Seller variant (Susie): sell ATM options delta-neutral right before the announcement, exit next morning. The prize is vega; theta is irrelevant (<1 day held); the risk is negative gamma on a big gap.
  - Buyer variant (Bobby): buy delta-neutral options a few days before the event, sell before the announcement. Needs IV to rise enough to cover theta; gamma is nearly irrelevant because the exit is before the move.
- **Reversion to the mean of IV**: IV trades in a stock-specific band (tides, not lines); stretched IV snaps back like a rubber band. Estimate the "normal" non-event IV from the chart between events (chip stock example: about 25%).
- **Volatility inertia**: absent a catalyst, IV should sit near realized vol (like an object in motion). Divergences between IV and realized vol are the tradable conditions. Always study both series together.
- **P&L attribution by greek**: `P&L ≈ Δ·ΔS + ½·Γ·(ΔS)² + Θ·days + ν·ΔIV`. Use it forecasting and post-trade; it explains why you made what you made.
  - Failure mode: estimate only. Gamma is not constant (falls fast then slowly as options go OTM), greeks are model values, slippage and IV rounding are ignored.

## Key Concepts
- **Delta neutral**: net position delta of zero; no immediate gain from a small move in either direction.
- **Direction neutral**: belief the underlying will not trend; typically negative gamma.
- **Direction indifferent**: does not care about the sign of the move; often long gamma or an IV/carry trade.
- **Rush**: pre-event IV bid-up by buyers seeking insurance.
- **Crush / "whacked"**: sudden post-event IV drop of 10 to 20+ points.
- **Reversion to the mean**: tendency of IV to return to its stock-specific range.
- **Marks**: prices at which the securities trade in the market, used to compute open P&L.
- **Portfolio margining**: margin based on the "up and down risk" of the whole portfolio, letting correlated products (SPX vs SPY) offset; replaced strategy-based Reg. T margin (post-2007), making delta-neutral trading affordable for retail. Eligibility needs a minimum balance and broker approval.
- **Reg. T (strategy-based) margin**: fixed-rule margin that can exceed the maximum possible loss (e.g. protective put: 50% of stock value plus up to 100% of put premium).
- **Position greeks**: per-contract greek × contracts (in 100-share units), e.g. vega -1.15 means -$115 per IV point.
- **Break-even IV move**: vega × ΔIV = theta × days held.
- **Caveat venditor**: the mean IV reverts to is itself not fixed and can reset higher after bad news.

## Formulas & Reference Tables
- `Position delta = Σ(nᵢ · Δᵢ · 100) + shares`
- `P&L(Δ) = Δ₀ · ΔS` (initial position delta × move)
- `P&L(Γ) ≈ ½ · Γ · (ΔS)²`, equivalent to (Γ·ΔS) × ΔS ÷ 2 (average delta gained over the move)
- `P&L(Θ) = Θ_day × days held`
- `P&L(ν) = ν × ΔIV points`
- Break-even IV rise for a long-vega trade: `ΔIV* = |Θ| · days / ν`.

| Greek | Susie (short 20 calls, long 1,100 sh) | Bobby (long 20 calls, short 1,000 sh) |
|---|---|---|
| Delta | +0.20 | +0.20 |
| Gamma | -1.60 | +1.80 |
| Theta | +0.75 | -0.64 |
| Vega | -1.15 | +1.20 |

## Mental Models
- **Delta-neutral means volatility is the position**: stock is only the hedge; ignore which leg made money.
- **IV is a rubber band with a moving anchor**: fade extremes vs the stock's own range, but re-anchor after fundamentals change.
- **Vega is the prize, gamma is the toll, theta is the clock**: in a <1-day event trade, only vega and gamma matter; in a multi-day long-vega trade, theta becomes the cost of waiting.
- **Every ship on the bottom of the ocean has a chart**: a clean historical pattern never removes tail risk.
- **Buy vol later, not sooner**: buying 4 points cheaper two weeks earlier (gain 4 x 1.20 = $480) would have cost 14 days x $64 theta = $896.

## Worked Example
Susie (sell the crush): stock $50, sell 20 one-month 50 calls at 2.10 (35 IV), buy 1,100 shares. Next morning stock is $52, IV 25, she buys the calls at 2.80 and sells the stock.
- Actual P&L: calls 20 x (2.10 - 2.80) x 100 = -$1,400; stock 1,100 x $2 = +$2,200; net +$800.
- Greek estimate (in $/100-share units): delta 0.20 x 2 = 0.40; gamma -1.6 x 2 x 2 / 2 = -3.20; theta +0.75; vega -1.15 x -10 = +11.50; total 9.45 = $945.
- Interpretation: $1,150 of vega was eroded by about $320 of gamma loss from the $2 rally; the $145 gap to actual reflects gamma nonconstancy, model values and rounding (25 IV theoretical was 2.796 vs 2.80 paid).

Bobby (buy the rush): stock $49.70, buy 20 33-day 50 calls at 1.75 (30 IV), short 1,000 shares. Three days later, IV 35, stock $50.00, sells calls at 2.10 and covers stock.
- Actual: calls +$700, stock -$300, net +$400. Greeks: 0.06 + 0.08 - 1.92 + 6.00 = 4.22 = $422.
- Break-even: needs 1.92 / 1.20 = 1.6 IV points just to pay three days of theta.

## Anti-patterns
- **Reading P&L leg by leg**: in a hedged position the option and stock legs offset; only net and greek attribution explain the result.
- **Holding a crush-sell through the event's tail**: theta is trivial on a one-day hold, so holding extra days only adds gamma risk.
- **Selling the rush on a stock that gaps hard on earnings**: history of realized-vol jumps (see October in the example) signals negative gamma will eat the vega.
- **Buying pre-event vol without a theta budget**: if IV does not rise by `|Θ|·days/ν` you lose.
- **Treating the mean IV as a constant**: a shocking result can reset the band higher.
- **Trusting greek attribution as exact**: constant-gamma assumption fails on big moves.

## Practitioner Notes
- Portfolio margin (post-2007) plus cheap commissions removed the retail barrier to delta-neutral trading; still, many accounts remain on Reg. T, so check margin before sizing.
- Odd-lot rounding means "neutral" is rarely exactly zero: Susie and Bobby both stayed +0.20 (about 20 shares long). Accept small residual delta.
- Judge the trade by the IV level you can exit at, versus the residual gamma loss, not by the option price.
- Typical crush magnitudes in the example: about 10 points after Oct and Jan earnings, 8 to 9 after April; the rush took IV from about 25 baseline to 35.
- Compare realized (30-day historical) with implied on the chart: realized often quiets just before the event, which helps the seller's gamma.

## Key Takeaways
1. Delta-neutral is a construction technique; the strategy is the volatility view behind it.
2. Choose direction neutral (movement hurts) vs direction indifferent (movement or IV helps) before choosing structure.
3. Estimate the stock's non-event IV band from the chart and fade deviations, but expect the band to shift after fundamentals change.
4. Sell the crush: short vega and negative gamma, hold under a day, exit as IV drops; size for the gap risk.
5. Buy the rush: long vega, positive gamma, exit before the event; require ΔIV ≥ |Θ|·days/ν.
6. Attribute P&L with Δ, Γ, Θ, ν before and after every trade.
7. Greek attribution is an approximation; expect 10 to 20% error on sizable moves.
8. Portfolio margin lowers cost of carrying hedged books.

## Connects To
- **ch03**: reversion to the mean of volatility, IV vs HV definitions.
- **ch05**: volatility-selling strategies (theta trades; this chapter is the vega/crush version).
- **ch13**: the realized-volatility (gamma) side of delta-neutral trading.
- **ch14**: reading the volatility charts used to find rush-and-crush setups.
- **ch17**: applying the greek P&L attribution in live positions.
- **`hull-derivatives`**: delta hedging and greeks mathematics.
