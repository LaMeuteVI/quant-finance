# Chapter 15: Straddles and Strangles
> **Source**: Dan Passarelli, *Trading Option Greeks* (2nd ed., Wiley/Bloomberg 2012), Ch. 15 · Advanced Option Trading

## Core Idea
Straddles and strangles are the purest instruments for buying or selling both realized and implied volatility at once. Long versions are active, gamma-scalped trades that need movement to beat theta and cheap-enough IV; short versions are monitored theta-harvesting trades where gamma losses are permanent while vega losses are temporary. The strangle trades lower nominal exposure for wider break-evens.

## Frameworks Introduced
- **Long straddle** (buy call + put, same class, expiry, strike): cost = both premiums; profit if the stock ends beyond `K ± debit`.
  - When to use: big move expected, direction unknown (breakout signals: CCI, Bollinger bands, pennants, or a fundamental catalyst), and IV not already inflated.
  - How: choose the expiry whose IV is cheapest and whose gamma/vega mix suits the plan (shorter expiry = more gamma, less vega); scalp gamma; exit when volatility appears to ebb.
  - Failure mode: buying just before earnings (after the rush, before the crush), or holding through stagnant theta.
- **Short straddle** (sell call + put, same strike): max profit = credit if the stock pins the strike; loss unlimited on both sides.
  - When to use: expect range-bound stock and IV too high vs RV and IV history.
  - How: actively monitor delta/gamma; hedge with stock or by buying back options; use a stop on delta; close before expiry to avoid pin risk.
  - Failure mode: 3+ standard-deviation gap (takeover, legal, political); every hedge locks in a loss.
- **Legging out (long straddle exit)**: instead of trading stock, sell calls when the stock rises (enough to flatten delta) and sell puts when it falls. Locks profit while shrinking risk.
- **Synthetic straddle**: `long call + long call + short 100 shares` (synthetic put) or `long put + long put + long stock`. Greeks nearly identical to a real straddle; only capital/margin differs (small under portfolio margining).
- **Long strangle** (buy OTM call + OTM put, different strikes): cheaper, wider break-evens, lower gamma/theta/vega; better percentage return, lower nominal return; vega rises as the stock approaches a strike. **Guts strangle** = ITM call + ITM put.
- **Short strangle** (sell OTM call + OTM put): more room for error, less premium; break-evens: put strike minus credit, call strike plus credit. Choose the month with the highest theta.
- **Limiting risk**: convert a short straddle/strangle into an iron butterfly/condor (buy farther OTM wings).
- **How cheap is too cheap**: do not sell strangles for a dime (e.g. 2-month 45/55 at 0.10) regardless of RV.

## Key Concepts
- **Straddle**: call and put at the same strike, expiry.
- **Strangle**: call and put at different strikes (usually both OTM).
- **Guts strangle**: both options ITM.
- **Break-even (straddle)**: `K ± net premium`.
- **Smiley/frown**: positive/negative gamma payoff shapes (long/short straddle before expiry).
- **Double vega**: two same-strike long options concentrate vega (about 0.05 each, roughly 10 cents per IV point per straddle in the example).
- **Gamma scalping**: buying and selling stock to lock in gains while long straddle (see ch13).
- **Pin risk**: uncertainty about assignment when the stock closes near the strike at expiry.
- **Realized/implied exposure go hand in hand**: a long straddle is long both; can't separate them.
- **Skew-of-IV-with-price**: IV tends to fall as the stock rallies and rise as it declines.
- **Synthetic put/call**: option plus stock replicating the other option type (ch06).

## Formulas & Reference Tables
- Straddle break-evens: `K − (C + P)` and `K + (C + P)`.
- Strangle break-evens (long): `K_put − debit` and `K_call + debit`; (short): `K_put − credit`, `K_call + credit`.
- Short-strangle profit region: between the two break-evens; max profit = credit between strikes.
- Daily theta cost for scalp break-even: `Θ$ per day` (Susan: theta -2.07 = $207/day for 20 lots).
- Vega profit: `ν × ΔIV`; IV gain needed to offset theta: `|Θ| · days / ν`.

| Feature | Long straddle | Long strangle |
|---|---|---|
| Cost (example) | 5.75 (75 straddle) | 2.35 (70/80) |
| Gamma / Theta / Vega (20-lot) | 2.16 / -2.07 / 3.35 | 1.70 / -1.71 / 2.80 |
| Break-evens | Nearer | Farther apart |
| Return profile | Higher nominal | Higher percentage |

| Feature | Short straddle (John, 105) | Short strangle (100/110) |
|---|---|---|
| Credit | 5.40 | 1.80 |
| Delta / Gamma / Theta / Vega | +0.26 / -1.18 / +1.20 / -2.09 | +0.13 / -0.91 / +0.92 / -1.61 |
| Break-evens | 99.60 / 110.40 | 98.20 / 111.80 |

Synthetic check ($40 stock, 60 days, IV 25, 4% rate): call delta 0.55, gamma 0.096, vega 0.064; put delta -0.46, gamma 0.099, vega 0.064. Straddle delta about +0.09, gamma 0.195, vega 0.128, versus synthetic straddle (two calls plus short 100 shares) delta about +0.10, gamma 0.192, vega 0.128.

## Mental Models
- **Straddle = movement race against theta; pay theta only as long as needed.**
- **Buy vol before the move is priced in**, same as buying a stock before news.
- **Strangle = a straddle with a deductible**: cheaper but you need more movement; better % returns when the stock moves modestly.
- **Vega losses are temporary, gamma losses are permanent** (for short vol).
- **Short strangle wiggle room vs short straddle premium**: pick based on which risk you'd rather have.
- **A short straddle's "risk of ruin" is about tail events, not average days.**

## Worked Example
Susan buys 20 Acme 75 straddles at 5.75 (stock 74.80, IV 36 equals RV 36): delta +0.85, gamma +2.16, theta -2.07 ($207/day), vega +3.35.
- Week 1: scalping +$1,100; straddle marked 5.10 bid = (5.10 - 5.75) × 20 × 100 = -$1,300; net -$200.
- Week 2: IV rises to 40 by Tuesday (straddle 5.20, essentially scratch); after FOMC stock jumps $4 and reverses, scalps +$5,200; IV falls to 30; straddle closed at 3.50: (3.50 - 5.10) × 20 × 100 = -$3,200; net +$2,000.
- Total about +$1,800 (1,100 - 1,300 + 5,200 - 3,200 = 1,800), earned by one or two big days; without them a certain loser.

John sells 10 XYZ 105 straddles at 5.40 (IV 26 vs RV 22, 12-month norm IV 20): vega -2.09, target IV 20: 6 × 2.09 = 12.54, i.e. $1,254 per 10-lot in $100 units. Stock rises to 106: delta ≈ 0.26 - 1.18 × 1.25 = -1.22. He waits (stop to cover at 107.50), stock retraces; on a $3.50 gap to 109 with straddle offered 4.75 he closes at profit (IV fell 1 point despite the rally).

## Anti-patterns
- **Buying a straddle right before earnings**: the move is already in the price.
- **Holding a long straddle without scalping**: waiting for a linear move wastes theta.
- **Ignoring IV when buying gamma**: a winning gamma trade can lose on IV.
- **Selling naked straddles without a hedge plan or wing**: unlimited-loss tail.
- **Carrying short options through expiry**: pin/assignment risk; buy them back for 0.05 to 0.10.
- **Selling "dime" strangles**: risking dollars to make dimes.
- **Selling vol when IV is below RV**: premium too cheap for movement.
- **Confusing straddle vs strangle vega**: strangle vega grows as the stock nears a strike; straddle vega shrinks as the stock leaves the strike.

## Practitioner Notes
- Ideal short-vol setup: IV above RV by 2 to 20 percent (perhaps more for speculators), plus a news check to play devil's advocate against the trade.
- Vol-selling in the example targets a return to the 12-month IV norm (20) and RV 15 to 20.
- IV commonly falls when the stock rallies; a gap up can help a short straddle's vega even as gamma hurts.
- Short straddle traders focus on the at-expiry diagram and time; long straddle traders focus on gamma vs theta each day.
- Pick expiry by theta (short) or by cheapest IV plus needed gamma (long).

## Key Takeaways
1. Long straddle: buy gamma and vega together, so check both RV and IV before buying.
2. Enter before the volatility trend starts; avoid paying the rush.
3. Manage actively: scalp stock or leg out; exit when volatility ebbs.
4. Break-evens: strike plus or minus premium (straddle), wider for strangles.
5. Short straddle/strangle: theta is the goal, gamma is the risk; monitor delta and hedge or leg out.
6. Strangles trade nominal for percentage return and margin for error.
7. Close shorts before expiry to avoid pin risk; wing them if tail risk is unacceptable.
8. Synthetics replicate straddles; portfolio margin makes them cheap to carry.

## Connects To
- **ch06**: put-call parity for synthetic straddles.
- **ch13**: gamma scalping and short-gamma hedging.
- **ch14**: reading vol charts to pick straddle buys/sells.
- **ch12**: earnings rush and crush.
- **ch10**: wing spreads (iron butterfly/condor) as capped-risk versions.
- **ch16**: ratio and complex spreads that extend these ideas.
- **`hull-derivatives`**: straddle payoffs and volatility trading.
