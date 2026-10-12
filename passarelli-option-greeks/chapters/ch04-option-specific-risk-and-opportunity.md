# Chapter 4: Option-Specific Risk and Opportunity
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 4

## Core Idea
Buying a call or a put "for direction" also buys gamma, theta, vega and rho exposure you did not ask for. **Strike choice is greek choice.** An ITM option is almost pure delta. An ATM option carries the most gamma, theta and vega. An OTM option is really a bet on **gamma, time and the size of the move**, with a low probability of payoff. Under the directional wrapper, every option trade is a volatility trade. Strategies sort into volatility buyers (+Γ, +vega) and volatility sellers (−Γ, −vega). With an efficient IV market, neither side has a built-in statistical edge.

## Frameworks Introduced
- **Greek priority ranking for a directional long option** (the Kim / Disney case):
  1. **Delta**: the reason for the trade.
  2. **Theta**: the price of waiting. Budget it for the planned holding period.
  3. **Vega**: about the whole premium is time value, so all of it is exposed to IV.
  4. **Gamma**: secondary. Use it mainly to predict how delta will evolve.
  5. **Rho**: negligible for short-dated options unless an FOMC decision is inside the holding window.
  - How: rank the greeks *by your thesis*, then choose the strike and expiry that maximize the greeks you want per unit of the ones you don't.
- **Strike-selection matrix** (44-day Disney calls, S = 35.10, IV ≈ 19%):

  | Greek | 32.50 ITM (3.00) | 35 ATM (1.10) | 37.50 OTM (0.20) |
  |---|---|---|---|
  | Delta | 0.862 | 0.570 | 0.185 |
  | Gamma | 0.079 | 0.166 | 0.119 |
  | Theta/day | −0.010 | −0.013 | −0.007 |
  | Vega | 0.026 | 0.048 | 0.032 |
  | Rho | 0.033 | 0.023 | 0.007 |
  | Time value | 0.40 | 1.00 | 0.20 |
  | Character | Stock substitute, "pure delta" | Balanced. Maximum theta and vega | Gamma/magnitude lottery |

  - Use **ITM** when you want leveraged delta with little exposure to decay and IV.
  - Use **ATM** when you want the biggest reaction to a timely move and accept the highest theta and vega.
  - Use **OTM** when you expect a *large, fast* move. It gives a better gamma/theta ratio but a low probability of payoff.
- **The gamma/theta relationship ("rent vs. reward")**: an option buyer pays theta to own gamma. OTM strikes can improve the ratio (for the 37.50 call, gamma is ≈ 72% of the ATM gamma for ≈ half the theta). The ideal path is for the stock to rally *through* the high-gamma strike and continue into the low-theta ITM zone.
- **Average daily theta (amortized decay budget)**: `(Premium now − Premium expected at exit, same S) ÷ days held`. Plan the exit before expiry acceleration eats the remaining time value.
- **Tweaking greeks**: there are three ways to reshape exposure. (1) Change the quantity, which scales all greeks proportionally. (2) Change the strike or expiry, which is the simplest. (3) Add stock or options to build a spread (ch09 onward). Every choice is a trade-off. There is no free greek.
- **Volatility buyers vs. volatility sellers**: long premium means +Γ and +vega, short premium means −Γ and −vega. Verticals, butterflies, condors, calendars and collars fall on either side depending on the strikes' position relative to the stock and on whether you bought or sold them.
- **Direction neutral vs. direction biased vs. direction indifferent**: volatility-selling strategies are typically *neutral* (they want a range). Volatility-buying strategies are either *biased* (long call or put, i.e. delta trades) or *indifferent* (straddles and strangles that profit from movement either way).

## Key Concepts
- **Immediate directional exposure**: the current delta, which gamma changes as the stock moves.
- **Theta risk**: the loss in value from the passage of time. It is the one input that changes with certainty.
- **Price-time matrix**: a grid of option value (or delta, gamma, vega) by stock price and by days to expiry. It is the practical tool for planning an exit.
- **Future realized volatility**: the stock movement that long-option positions monetize through gamma.
- **Positive vs. negative gamma position**: +Γ makes moves in your favor accelerate and moves against you decelerate. −Γ does the opposite.
- **Dynamic greeks**: an ITM option can become ATM tomorrow, so gamma, theta and vega can "come back into play" at any time.
- **Leverage**: an option controls 100 shares for a fraction of the price. Percentage swings are large, while nominal exposure is smaller than the stock.
- **Teenie buyers / teenie sellers**: floor-trading archetypes from the 1/16 tick era. Buyers pay a teenie to close or own far-OTM options as cheap lottery tickets or insurance. Sellers pocket a teenie, betting the option expires worthless.
- **Babe Ruth style**: the buyer's profile of many small losses and a few large wins.
- **Fair game**: a price at which the expected payoff equals the cost. Here IV is the entry fee.
- **Surprise dividend risk**: an unexpected large dividend (for example $3) makes the stock more valuable to hold than the call and cuts the call's value.

## Formulas & Reference Tables
- Average daily theta: `θ̄ = (V_t₀ − V_t₁)/(t₀ − t₁)`, with S and IV held constant
- Gamma/theta efficiency: `|Γ/θ|` (higher means more convexity per dollar of daily decay). BS values: 32.50 ≈ 8.5, 35 ≈ 12.7, 37.50 ≈ 14.2.
- Put delta ≈ `Call delta − 1` (European, no dividend), with the same gamma and vega at a given strike
- Expected value of a game: `E = Σ pᵢ × payoffᵢ`. Die paying $1 on 1, 2 or 3: E = $0.50. Die paying $1 on a 1 only: E = $0.1667.
- Leverage return: `(V_exit − V_entry)/V_entry`

**Scenario grid after 21 days (23 days left), from the book's price-time matrices**

| DIS at day 21 | 35 call (paid 1.10) | 37.50 call (paid 0.20) | 32.50 call (paid 3.00) | 35 put (paid 0.80) |
|---|---|---|---|---|
| 38 | 3.14 (+185%) | 1.04 (+420%) | 5.61 (+87%) | 0.03 (−96%) |
| 37 | 2.21 (+101%) | 0.50 (+150%) | 4.61 (+54%) | 0.09 (−89%) |
| 35 | 0.73 (−34%) | 0.05 (−75%) | 2.68 (−11%) | 0.62 (−23%) |
| 33 | 0.10 (−91%) | 0.00 (−100%) | 1.09 (−64%) | 2.03 (+154%) |

(Matrix rows are at whole-dollar stock prices, so the 35 row is 0.10 below the entry price of 35.10.)

## Mental Models
- **An option buyer races the clock.** The only certain input change is time, so decide in advance how many days of decay you are paying for.
- **Deep ITM options are stock with a small insurance policy.** The deeper ITM, the more they act like stock and the less the greeks matter. The greeks are still dynamic, though.
- **OTM options are magnitude bets.** The 0.185 delta says the option expires ITM about 1 time in 5 or 6, so the wins must be several times the losses.
- **Gamma always changes delta in the long option holder's favor.** It adds delta when you are right and removes it when you are wrong.
- **Every option trade is a volatility trade.** A long call is long *upward* volatility. Adverse volatility costs you, but less than the stock would.
- **No free lunch in aggregate.** IV is the fair-game entry fee. Individual options can be mispriced, but neither always buying nor always selling carries a structural edge.

## Worked Example
**Choosing the strike for a 3-week bullish view** (DIS 35.10, 44 days, r = 5.25%, no dividend). A Black-Scholes check with IV ≈ 19.2% reproduces the ATM call at 1.10 with Δ = 0.568, Γ = 0.168, θ = −0.0132 and vega = 0.048. The book's 37.50 call at 0.20 back-solves to ≈ 17.9% IV and the 32.50 call at 3.00 to ≈ 22.6% IV, so normal downside skew is already in these prices.

1. *Stock flat for 3 weeks*: the ATM call decays from 1.04 to 0.73 in the matrix (≈ −30% of premium, i.e. theta). The ITM call loses only 0.23, but it tied up 3.00.
2. *+$2 move (to 37)*: ATM +101%, OTM +150%, ITM +54%. At that point the ATM call has vega 0.018, so even a 5-point IV drop costs less than 0.10, under 5% of its value.
3. *+$3 move (to 38)*: OTM +420% on an ≈ 8% stock move. It still has only ≈ 18.5% odds of expiring ITM.
4. *Put buyer (Mick, 35 put at 0.80)*: θ goes from −0.009 at 44 days to −0.013 at 23 days, −0.021 at 9 days and −0.049 at 2 days. With the stock unchanged, the put is worth 0.35 after 35 days. Average daily theta = (0.80 − 0.35)/35 = **0.0129/day**, which delta must earn back every day to break even. Holding only 21 days costs (0.80 − 0.57)/21 ≈ 0.011/day.

Interpretation: choose ATM for a timely move of moderate size, OTM only when you expect a large and fast move, and ITM when you want a stock replacement. Exit before the last 2–3 weeks unless the move has already come.

## Anti-patterns
- **Thinking a long call is "just bullish"**: it is also short theta and long vega. A correct direction that arrives too slowly, or with an IV crush, can still lose.
- **Buying cheap OTM options because the percentage payoff looks huge**: the probability-weighted payoff is fair at best (fair-game logic).
- **Holding long ATM options into the final weeks without a plan**: theta accelerates non-linearly (0.049/day at 2 days on a 0.80 put).
- **Judging an OTM option's theta as "small"**: measured against a 0.20 premium, 0.007/day is 3.5% a day.
- **Believing either option buying or option selling is structurally superior**: it is a matter of preference and skill in finding specific mispricings.
- **Ignoring corporate-action risk**: a surprise special dividend reprices calls down and puts up.

## Practitioner Notes
- The author's rule: follow "cut losses, let profits run" *with respect to theta*. Exit decaying longs before expiration week if the forecast has not played out. When to cut is personal and depends on the trade.
- Budget decay explicitly. If you plan to hold for 3 weeks, price the option at the exit date with an unchanged stock (the matrix) and treat that loss as the cost of the trade.
- If the move comes early, you pay less decay. If it comes late, the option may have decayed to nothing. The timing of the forecast matters as much as its direction.
- Rho: since the Greenspan and Bernanke eras, rate moves are mostly announced at scheduled FOMC meetings. If none falls inside the option's life, ignore rho on short-dated options (0.023 at 44 days, 0.011 at 23 days).
- Volatility sellers' income strategies "win more often than they lose, but lose more than they win" when they do lose (iron condors, for example). Buyers accept many strikeouts for a few home runs. Pick the profile you can execute consistently.
- Most strategies change category (volatility buyer or seller) as the stock moves relative to the strikes. Re-evaluate the category, not only the P&L.

## Key Takeaways
1. Strike choice sets your greek mix: ITM ≈ delta, ATM = maximum Γ, θ and vega, OTM = a leveraged bet on magnitude.
2. Rank the greeks by your thesis. For a directional long, the order is delta, then theta, vega, gamma and rho.
3. Compute the average daily theta over your planned holding period and exit before decay accelerates.
4. OTM calls or puts need a big move soon. Their delta (≈ probability) warns you that most will expire worthless.
5. Long options are long realized volatility (gamma) and long implied volatility (vega). Short options are the reverse.
6. Volatility-selling strategies are direction neutral. Volatility-buying strategies are direction biased or direction indifferent.
7. With IV as the fair entry price, no systematic edge comes from always buying or always selling options.

## Connects To
- **ch02**: definitions and behavior of each greek.
- **ch03**: IV, skew and why the 37.50 and 32.50 strikes carry different IVs.
- **ch05**: volatility-selling strategies (the other side of this chapter).
- **ch09–ch11**: using spreads to reshape greeks (verticals, wings, calendars).
- **ch13**: gamma scalping, where long gamma is monetized through delta hedging.
- **ch15**: straddles and strangles, the direction-indifferent volatility buyers.
- **`hull-derivatives` ch19**: theta–gamma relationship and greek profiles by moneyness.
- **`hull-derivatives` ch12**: option trading strategies catalog.
- **`cfa-derivatives` ch05**: long option strategies and their greek exposures.
