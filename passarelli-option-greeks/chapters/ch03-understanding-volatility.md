# Chapter 3: Understanding Volatility
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 3

## Core Idea
"Volatility" has three distinct meanings for an option trader. **Historical (realized) volatility** is how much the stock *has* moved. **Implied volatility** is the price of options expressed as a volatility, set by supply and demand, "fear and greed". **Expected volatility** is the trader's own forecast of both. Most option positions are exposed to realized volatility (through gamma) *and* to implied volatility (through vega). So buying options is buying volatility and selling options is selling volatility. The edge comes from forecasting IV (mean reversion, event cycles, skew) and from converting annual volatility into the daily and monthly moves you actually trade.

## Frameworks Introduced
- **The three volatilities**:

  | Type | What it measures | Source | Exposure in a position |
  |---|---|---|---|
  | Historical volatility (HV, realized, statistical) | Annualized std. dev. of past daily returns | Closing prices, usually a 30-trading-day window | Gamma/theta P&L from actual movement |
  | Implied volatility (IV) | The volatility input that reprices the option to the market | Option prices (mid, bid or ask) | Vega P&L from repricing |
  | Expected volatility | The trader's forecast of future HV and future IV | Analysis, event calendar, vol charts | Drives trade selection |

- **De-annualizing IV (the "rule of 16")**:
  - How: 1-day σ ≈ IV/√256 = IV/16. For a period of n trading days, σ ≈ (IV/16)·√n. The move in dollars ≈ S × σ, and there is roughly a 68% chance of finishing within ±1σ.
  - When to use: to size strikes, stops and hedges, and to ask whether the option is pricing a move you believe.
  - Why 256: √256 = 16 is a convenient round number close to the actual count of about 252 trading days.
- **HV–IV divergence around scheduled events**: before an earnings release (especially with no analyst consensus), the stock goes quiet, so HV falls, while options get bid, so IV rises. After the news the stock moves (or doesn't), IV collapses and the two converge. Trade the *convergence*, and remember that IV rising before the last 15 reports does not guarantee it rises this time.
- **Mean reversion of IV, with regime awareness**:
  - How: establish the normal IV range from the last **6 months** (use **12 months** if IV changed a lot in that window). Fade breakouts outside the range, expecting a return to it.
  - Failure mode: a *regime change*, where fundamentals shift and a new mean forms. Examples from the book: SPX IV was about 20–30 in 1998–2003 and about 10–13 in late 2006. It traded about 12–20 from fall 2010 to mid-2011, then about 24–40 after August 2011 during the European debt crisis.
- **Fundamental analysis of IV**: ask where the fear is, where the complacency is, which events are scheduled and how important they are. The underlying question is always: what is the potential for the stock to move?
- **Two dimensions of skew**:
  - **Term structure (horizontal, monthly skew)**: IV by expiry at the same strike. When volatility is falling, the front month trades below the back months (upward term structure). When it is rising, the front month trades above them. Event months (earnings, a lawsuit verdict) carry their own premium.
  - **Vertical (strike) skew**: IV by strike within one expiry. In equities, downside strikes ("puts") trade at higher IV than ATM and upside strikes ("calls") at lower IV. The put side also has a steeper *slope* (IV points per strike). Grain options typically show the reverse (calls richer).

## Key Concepts
- **Historical volatility (HV)**: the annualized standard deviation of daily returns. It is computed close-to-close, over a rolling window of usually 30 trading days (weekends and holidays excluded).
- **Standard deviation (σ)**: dispersion around the mean. For a normal distribution, ±1σ covers about 68%, ±2σ about 95% and ±3σ about 99.7%.
- **Lognormal distribution**: the price distribution assumed by standard pricing models. Returns are normal and prices cannot go below zero.
- **Implied volatility (IV)**: the volatility that makes the model value equal the option's market price (usually the mid).
- **Vol trader's quote**: bids and offers expressed in IV, for example "30 bid at 31 offer", not in dollars.
- **Vol chart**: a time series of IV together with HV. It is the "technical analysis" tool for options (ch14). Using IV from mid-market theos removes bid-ask noise from last-trade prices.
- **Reversion to the mean**: IV's tendency to return to its typical range after a breakout.
- **VIX (CBOE Volatility Index)**: the IV of a hypothetical 30-day SPX option, interpolated from the two nearest expiries.
- **Volatility–price inverse relationship**: IV usually rises when the market or stock falls and falls when it rallies. When prices fall, investors buy puts. When they rally, they sell back protection and write calls.
- **Term structure of volatility**: IV across expiries for the same strike.
- **Vertical (strike) skew**: IV across strikes for the same expiry.
- **Skew slope**: the change in IV per strike. Models let you set separate upside and downside slopes, either linear or exponential.
- **Smile / sneer**: names for the shape of the IV-vs-strike curve.
- **Front month / back months**: the nearest expiry vs. the later ones.

## Formulas & Reference Tables
- Daily log return: `rᵢ = ln(Sᵢ/Sᵢ₋₁)`
- Historical volatility: `HV = √[Σ(rᵢ − r̄)²/(n − 1)] × √252`. ⚠ Correction: the book describes σ as dispersion around "the average stock price". HV is the dispersion of *returns*, not of price levels.
- 1-day expected move: `σ₁d = IV/√256 = IV/16`
- n-day expected move: `σₙ = (IV/16) × √n`, with n = trading days in the period
- Dollar range (≈68%): `S × (1 ± σₙ)` (normal approximation). The lognormal version is `S·e^{±σₙ}`, which is asymmetric. For IV = 32% over 1 year: normal 68–132, lognormal 72.6–137.7.
- IV change needed for a given dollar move in the option: `ΔIV (pts) = ΔPrice / Vega`

**GM 32.5 calls, S = 31.96 (Exhibits 3.3–3.4)**: term structure and vega

| Expiry | Days | Theo | IV | Vega | IV points for +$0.10 |
|---|---|---|---|---|---|
| Feb | 21 | 0.80 | 32.0% | 0.031 | 3.2 |
| Mar | 51 | 1.30 | 32.7% | 0.046 | 2.2 |
| Jun | 142 | 2.50 | 34.1% | 0.076 | 1.3 |
| Sep | 240 | 3.40 | 34.6% | 0.098 | 1.0 |
| (7 days) | 7 | — | — | ≈ 0.014–0.017 | ≈ 6–7 |

Front-month IV is the most volatile for two reasons: it has the most trading activity, and its vega is the smallest, so the same dollar move in the option means a larger IV move. (A BS check reproduces these vegas within about 0.005.)

**Citigroup 84-day vertical skew (Exhibit 3.5), S = 34.16**: IV by strike 31: 49.6 | 32: 47.6 | 33: 45.8 | 34: 44.2 | 35: 42.6 | 36: 41.2 | 37: 40.1 | 38: 39.0. The downside slope is about 2.0 and 1.8 pts per strike, the upside slope about 1.1. That is a >10-point gap across 7 strikes.

## Mental Models
- **Think of IV as the option's price and of dollars as the currency it is quoted in.** A vol trader compares 30 bid / 31 offer across strikes and months. Dollar prices are secondary.
- **HV is the rearview mirror, IV is the windshield.** When they diverge, ask which event the market is pricing.
- **Use the rule of 16 as a sanity check on every trade.** 32 IV means a 2% daily move. If you don't believe the stock will move 2% a day, the options are expensive *for you*.
- **Treat IV as a mean-reverting asset with regime breaks.** Fade extremes, but first check whether the fundamentals have changed.
- **Stock down, IV up.** Long puts and downside skew gain in a selloff from both delta and vega. Upside calls get hurt by vega in a rally.

## Worked Example
**1. Expected-move ladder** ($100 stock, ATM IV = 32%)

| Horizon | Calculation | 1σ | 68% range (normal approx.) |
|---|---|---|---|
| 1 day | 0.32/16 | 2.00% | 98.00–102.00 |
| 1 week (5 days) | 0.02 × √5 | 4.47% | 95.53–104.47 |
| 1 month (22 days) | 0.02 × √22 | 9.38% | 90.62–109.38 |
| 1 year | 0.32 | 32% | 68–132 (lognormal: 72.6–137.7) |

A trader short a 110 call for one month is about 1σ out of the money. Under the normal approximation, the stock ends above about +1σ roughly 16% of the time.

**2. Computing HV** (illustrative closes: 100, 101.5, 100.8, 102.3, 101.1, 103.0)
Log returns (%) are +1.489, −0.692, +1.477, −1.180, +1.862. The sample σ is 1.413% per day, so HV ≈ 1.413% × √252 ≈ **22.4%** (×16 gives 22.6%). If the ATM options trade at 30 IV, the market prices about 33% more movement than the stock has recently delivered. Before selling, check for an upcoming event.

**3. Vega-to-IV conversion**: a 45-strike call on a $44.22 stock, 60 days, 18% IV, is worth 1.10 with vega ≈ 0.07. If IV goes from 18 to 20, the call goes to 1.24 without the stock moving. A buyer who "got the direction right" can still lose if IV drops from 20 back to 18 after an event.

## Anti-patterns
- **Blaming market makers when an option price moves "wrongly"**: it is usually an IV change the trader did not track.
- **Charting raw option prices**: trades alternating between a 0.80 bid and a 0.90 offer look like a 12.5% "move" that is pure noise. Chart IV computed from mid-market theos.
- **Trusting displayed IVs without knowing whether they were computed from the bid, the ask, the last trade or a stale quote**: compute your own.
- **Comparing IV with HV over mismatched windows** (a 5-day HV vs. a 60-day option): the window changes the answer.
- **Using annualized IV as a forecast for a 1-month horizon without scaling by √time.**
- **Assuming mean reversion across a regime change**, for example SPX in August 2011.
- **Assuming the event pattern will repeat**: 15 prior pre-earnings IV run-ups do not guarantee the 16th.

## Practitioner Notes
- Compute IV at the price you would actually trade: a long-vol trader looking to exit should solve IV at the **bid** to see what level he can sell.
- Front-month IV needs a much bigger point move for the same dollar change. Expect front-month IV to swing wildly near expiry and don't over-interpret it.
- In quiet regimes the term structure slopes upward (front < back). In stress it inverts (front > back). The shape tells you whether the market expects volatility to fall or rise.
- Individual-stock IV tends to move with the VIX, because of systematic (market) risk. A VIX spike lifts most single-name IVs.
- Put skew exists because hedgers keep demanding downside protection. Skew itself is a tradable market with its own specialists.
- Buying a call rather than stock when you expect high volatility caps the dollars at risk while keeping similar upside. This extra demand is itself one reason IV rises in fearful markets.

## Key Takeaways
1. Separate HV (what happened), IV (what is priced) and expected volatility (your forecast), and know which one each position is exposed to.
2. De-annualize with the rule of 16: daily σ = IV/16, n-day σ = IV/16 × √n.
3. Before earnings and similar events, HV tends to fall and IV to rise. They converge after the news.
4. IV mean-reverts within a 6–12-month range, until the regime changes.
5. IV usually moves inversely to price in equities, and put skew is steeper than call skew.
6. Short-dated IV is the most volatile because vega is smallest there. Convert dollar moves into IV points with ΔIV = ΔPrice/Vega.
7. Generate your own IVs. Screen-displayed IVs are unreliable.

## Connects To
- **ch02**: vega and the model calibration loop.
- **ch04**: vega risk and gamma/theta, i.e. trading realized against implied volatility.
- **ch05**: volatility-selling strategies that monetize high IV.
- **ch12–ch13**: delta-neutral trading of implied vs. realized volatility.
- **ch14**: reading vol charts (HV vs. IV patterns).
- **`hull-derivatives` ch15**: estimating volatility from historical data, and implied volatility.
- **`hull-derivatives` ch20**: volatility smiles, skew and surfaces.
- **`hull-derivatives` ch23**: EWMA/GARCH volatility estimation.
- **`cfa-derivatives` ch05**: implied volatility, skew and the VIX in options strategy.
