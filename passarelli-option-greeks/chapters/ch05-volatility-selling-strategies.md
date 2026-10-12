# Chapter 5: An Introduction to Volatility-Selling Strategies
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 5

## Core Idea
Selling options is being paid theta to carry negative gamma and negative vega. The four basic volatility-selling structures (naked call, naked put, covered call, covered put) look like "income" trades, but they are managed like short-volatility risk: **decide the pain point in advance, translate it into a stock price with delta and gamma, and re-underwrite the trade daily with the "Would I Do It Now?" rule.** Holding to expiry makes the greeks irrelevant. Exiting early makes them the whole game.

## Frameworks Introduced
- **Volatility-seller's greek profile**: −Γ, −vega, +θ. The trader wants the stock quiet and IV flat or falling.
  - When to use: any short-premium trade, before sizing it.
  - How: check that the theta you collect per day pays for the gamma and vega you carry. Positions with larger |Γ| also carry larger |θ|, so the gamma-theta trade-off is the master constraint (higher theta is never free).
  - Failure mode: treating theta as "income" and ignoring the tail. Reward is capped at the premium, while risk sits in a move.
- **Pain-point conversion (delta-gamma stop distance)**: convert a premium stop into the stock move that triggers it.
  - How: (1) choose the exit option price. (2) Use the price you will actually pay: the offer when covering a short, the bid when selling a long. (3) Take the option-price change ΔV = exit − current. (4) Divide by the **average delta over the move**: `ΔS = ΔV ÷ (|Δ| + Γ/2)`. Delta alone understates how quickly a short option gets worse.
  - Why it works: a short option has negative gamma. When the stock moves against you, |Δ| grows by about Γ per $1, so the average delta over the move is roughly |Δ| + Γ/2.
  - Failure mode: ignoring vega. Adverse moves usually come with rising IV, so the stop is hit sooner than delta/gamma alone implies.
- **Would I Do It Now? rule**: "If I did not already have this position, would I open it at today's prices, given today's stock price and information?" If not, close.
  - How: compare the premium you would collect now, how far the stock is from the strike, days left, and theta received against gamma risk added. Then compare with your original thesis.
  - Example use: a short call whose stock rose 0.50 toward the strike now pays only $0.09 more premium for much more gamma. If you are no longer neutral or bearish, exit.
- **Theta as a decision tool for the losing short**: as the stock approaches the strike, theta rises (more reward) but gamma rises faster (more risk). Ask whether the reward per day compensates the risk of one more adverse day.
- **The double whammy** (short puts and any position long delta and short vega): a fall in the stock lowers value through delta and raises the option through IV (vega). The option therefore reaches your stop earlier than delta/gamma alone predicts, and a gap through the stop cannot be stopped at all.
- **Cash-secured put as a discounted-entry order**: sell the put, hold cash of `(K − premium) × 100` per contract. The effective purchase price if assigned is `K − premium`, which is also the expiry break-even.
- **Covered call decision grid (which month and strike)**: compare candidates on theta per day, IV term structure, net delta and the **indifference point** (`K + call premium`, the effective sale price if called away).
- **Covered put = naked call in disguise**: short stock + short put has the same payoff as a short call (synthetic equivalence, see ch06). It converts a limited-risk naked put into an unlimited-risk position, so "covered" is a misnomer.
- **Rolling**: when the short option is worth a nickel to a dime, stop waiting for the last few cents. Buy it back and sell the next month (a calendar or time spread if done as one order).

## Key Concepts
- **Naked (uncovered) call / put**: a short option with no stock or other option covering the risk. Naked call: limited reward, unlimited risk. Naked put: limited reward, risk to zero.
- **Volatility-selling / income-generating strategy**: a position with +θ, −Γ and −vega.
- **Slippage**: the gap between the assumed price and the actual fill, driven by the bid-ask spread. Wide spreads shrink the room between entry and stop.
- **Mental stop vs GTC stop**: a resting good-till-canceled buy-back order vs a price you watch and act on manually.
- **Whipsaw**: exiting at a stop only to see the market reverse.
- **Cash-secured put**: a short put backed by the cash to buy the shares if assigned.
- **Covered call (buy-write)**: long 100 shares plus a short call per contract. Stock adds delta only; the option's gamma, theta and vega are unchanged.
- **Indifference point (covered call)**: `K + premium`, the stock price at which stock-only and covered-call P&L at expiry are equal.
- **Covered put**: short stock plus short put. Same risk shape as a naked call.
- **Legging out**: closing one leg at a time. For a covered call you normally close the call first, because reducing risk is the goal.
- **Premium over parity**: option price minus intrinsic value. Below the strike, the time value is all that matters to a covered-put seller.
- **Roll / time spread**: buy back the near option and sell a later one against the same position.
- **Position delta in shares**: `option delta × 100 × contracts`, with sign flipped for a short.

## Formulas & Reference Tables
- Stock move for a given option-price change (delta only): `ΔS = ΔV ÷ |Δ|`
- Stock move including gamma (average-delta method): `ΔS = ΔV ÷ (|Δ| + Γ/2)`
- Option price change for a stock move ΔS (second-order): `ΔV ≈ (|Δ| ± Γ/2) × ΔS`. Use `+` when the move makes |Δ| larger (adverse move for a short option), `−` when it makes |Δ| smaller.
- Vega P&L: `vega × ΔIV(points) × 100 × contracts`
- Naked call: max profit = premium; break-even = `K + premium`.
- Naked put: max profit = premium; break-even = `K − premium`.
- Cash-secured put cash: `(K − premium) × 100 × contracts`; effective cost basis = `K − premium`.
- Covered call: max profit = `(K − S₀) + premium`; break-even = `S₀ − premium`; indifference point = `K + premium`; net delta = `1 − Δcall`.
- Covered put (short stock at S₀, short put): max profit = `(S₀ − K) + premium` at or below K; delta = `−1 + |Δput|`.
- Annualized static return: `(premium ÷ stock price) × (365 ÷ days)`.

**Greek signs by structure (per contract, at inception)**

| Structure | Delta | Gamma | Theta | Vega | Directional stance |
|---|---|---|---|---|---|
| Naked call | − | − | + | − | Not bullish (range or down) |
| Naked put | + | − | + | − | Not bearish (range or up) |
| Covered call | + (1 − Δcall) | − | + | − | Neutral to mildly bullish |
| Covered put | − (−1 + \|Δput\|) | − | + | − | Neutral to mildly bearish |

## Mental Models
- **You are the insurer, not the speculator.** Reward is bounded by the premium; sizing and the stop decide survival. Set the exit before entry.
- **Theta and gamma are one coin.** Higher theta means higher gamma. When the stock sits on your strike, you collect the most and are the most exposed.
- **Stock adds only delta.** A covered call has the identical gamma, theta and vega as the naked call. Only directional exposure and the tail change.
- **Convert everything to stock price.** A stop in option dollars is not a plan until you know which stock price triggers it.
- **The market reprices your stop.** Falling stocks bring rising IV and gaps. Treat the stop as a zone, not a line.

## Worked Example
Naked call (book's JNJ trade, recomputed). Stock 64, sell 10 Nov 65 calls at 0.66 (market 0.66/0.68). Per contract: Δ = 0.34, Γ = 0.15, θ = 0.018, vega 0.07. Stop: buy back at 1.10.

1. Max profit = 0.66 × 100 × 10 = $660. Break-even = 65.66.
2. Option move to the stop = 1.10 − 0.68 (the current offer) = 0.42.
3. Delta only: 0.42 ÷ 0.34 = 1.24. Delta plus gamma: 0.42 ÷ (0.34 + 0.15/2) = 1.01. The stop is hit about $1.01 higher, around 65.01 (near the strike, before any vega effect).
4. Theta check: at 64.50 with a few days gone, theta is about 0.018 per share = $18/day for 10 contracts. Would you sell these at 0.75 for $18/day with the stock 50 cents closer to the strike? That is the Would I Do It Now? test.

Covered call, HOG at 69, sell the March 70 call at 0.85 (Δ = 0.412): net delta = 1 − 0.412 = 0.588 (the book's table shows 0.591). Break-even 69 − 0.85 = 68.15. Max profit at or above 70 = 1 + 0.85 = 1.85. Indifference point 70.85. Static May 70 alternative: 2.80 ÷ 69 = 4.06% over 85 days, about 17.4% annualized. The March 70 was chosen anyway: higher theta (0.032 vs 0.022 for May), lower IV (19.2% vs 23%), and a neutral view that favors theta over delta.

## Anti-patterns
- **Using delta alone to set a stop on a short option**: understates the adverse move by the gamma term (1.24 vs 1.01 in the example).
- **Selling a naked option as a directional conviction trade**: it only says "not above/below". If you are bullish or bearish, buy a call or put.
- **Ignoring vega on a short put**: the fall that hurts through delta also raises IV. In the book's case, a gap to 63 with IV +5 points cost about $215 on vega alone (0.043 × 5 × 100 × 10), plus the delta/gamma loss.
- **Holding a covered call "for income" through a trend down**: the premium cushions only a few percent. The stock is the real risk.
- **Waiting for the last nickel**: with the short option at 0.05 and weeks to run, greeks and models no longer help. Roll instead.
- **Trading wide markets with tight stops**: a 0.70-wide spread means the stop price may never be offered.
- **Calling a covered put "covered"**: it is a naked call with unlimited upside risk.

## Practitioner Notes
- Sell before the next earnings date, and check for take-over or news catalysts before selling a naked call. The book's trader also used a trend filter (ADX/DMI) and range resistance to time the entry.
- Use different tactics for the delta profile: a short ITM put (Δ 0.65 ≈ long 650 shares for 10 lots) will take profits early and manage it like a stock position. A short OTM call is managed by gamma.
- For profits: "nobody ever went broke taking a profit." If the expected move has already happened and 28 days remain, the trade no longer matches the original thesis, so take the money.
- Cash-secured puts are a volatility trade too: the higher the IV, the bigger the purchase discount, but the more likely the stock moves through the break-even.
- Plan the exit at entry: a stock price level and a maximum loss per contract. In the book, Stacie risked 1.00 per contract.
- Assignment risk rises with IV and with ITM puts. Do not sell a put on a stock you would not own.
- ⚠ Correction (book, short put example): the book computes the put's gain on a $1 rise as `(0.65 + 0.15/2) × 1 = 0.73`. For the seller of the put, a rising stock makes the position delta smaller (short gamma), so the average delta is `0.65 − 0.075 = 0.575`, giving a gain of 0.575 (put offered near 1.225, profit about 0.525 at a 1.80 offer basis, not 0.68). The `+Γ/2` form applies to the adverse direction (stock falling for a short put; rising for a short call). The book's stated stop-loss stock price of "about 63.28" also does not reproduce: from a 1.80 offer to 2.75 is 0.95, and 0.95 ÷ 0.725 = 1.31, so the stop is about 62.7.

## Key Takeaways
1. Short options pay +θ and charge −Γ and −vega; every income trade is a short-volatility trade.
2. Convert your premium stop into a stock price using `ΔV ÷ (|Δ| + Γ/2)`, and use the offer (for shorts) as your price.
3. Apply "Would I Do It Now?" every time the stock, time or news changes.
4. Adding stock changes only delta: covered call has the naked call's gamma, theta and vega, and the covered put behaves like a naked call.
5. Cash-secured put: effective cost = K − premium; higher IV gives a bigger discount and a wider range of loss.
6. For short puts, expect delta and vega to hurt together (the double whammy) and to gap past stops.
7. Choose the covered-call month by theta, IV and indifference point, not by headline premium.
8. Roll when the remaining premium is a few cents and time remains; do not "collect the nickel".

## Connects To
- **ch04**: the mirror image, with volatility buyers paying theta for gamma and vega.
- **ch06**: covered call = short put; covered put = short call (synthetics).
- **ch09**: verticals cap the tail that naked selling leaves open.
- **ch11**: the roll described here is a calendar spread.
- **ch15**: short straddles and strangles are the two-sided version of these trades.
- **`hull-derivatives`**: payoff diagrams and put-call parity for covered positions.
