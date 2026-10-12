# Chapter 2: Greek Philosophy
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 2

## Core Idea
A pricing model does not tell you what an option is *worth*. The market sets the price, and the trader tunes the inputs (mostly volatility) until the theoretical value sits between the bid and the offer. The model's real use is its **partial derivatives**: delta, gamma, theta, vega and rho. They tell you how the option's value will move when each of the five changeable inputs (stock price, time, volatility, interest and dividends) moves. "Thinking Greek" means watching and trading these sensitivities with at least as much care as the option price itself.

## Frameworks Introduced
- **Price vs. value (the model-calibration loop)**:
  - A pricing model has six inputs: stock price, strike, time, interest rate, dividends and volatility. Only the strike is fixed. The other five are dynamic.
  - How: take the market price as given → back out the implied volatility → the model's theoretical value (the "theo" or fair value) now lies inside the bid-ask spread → read the greeks off that calibrated model.
  - Why it works: it turns one observable price into a multi-dimensional risk description. Failure mode: stale inputs (the day not taken out, an old rate or dividend) produce theos outside the market and wrong greeks.
- **The four definitions of delta**, each used for a different job:
  1. Rate of change of the option value per $1 move in the underlying. Use it for P&L forecasts.
  2. Slope (first derivative) of the value-vs-price curve. Use it for intuition.
  3. **Share equivalent**: `position delta = contracts × Δ × 100`. Use it for hedging and sizing.
  4. **Trader's probability**: Δ ≈ the chance of finishing ITM. This is a rule of thumb only. The mathematically closer proxy is N(d₂), which is below the call's N(d₁).
- **Gamma-adjusted (average-delta) repricing**: over a move of ΔS, the option changes by about the *average* of the starting and ending deltas times ΔS. This equals `Δ·ΔS + ½Γ·ΔS²`. Use it whenever a move is more than a few cents.
- **Greek sign rules for positions**:

  | Position | Delta | Gamma | Theta | Vega | Rho |
  |---|---|---|---|---|---|
  | Long call | + | + | − | + | + |
  | Short call | − | − | + | − | − |
  | Long put | − | + | − | + | − |
  | Short put | + | − | + | − | + |

  Long options are long gamma and vega and short theta. Short options are the mirror image. Every option trade is a choice between **gamma/vega and theta**.
- **"Taking the day out"**: the market marks tomorrow's decay into prices *during* today's session, usually midday once the stock has settled. By Friday afternoon, desks value options with Monday's days-to-expiry. Do not mistake a routine intraday cheapening for an IV collapse.

## Key Concepts
- **Theoretical value (theo, fair value)**: the model output, calibrated so it falls inside the bid-ask spread.
- **Delta (Δ)**: `∂V/∂S`. A call is between 0 and +1, a put between −1 and 0, and stock is exactly 1. It is quoted either as a decimal (0.50) or as a whole number (50).
- **Position delta**: the share equivalent of an option position. Being long 5 calls with a 0.43 delta means being long 215 deltas.
- **Gamma (Γ, curvature)**: `∂Δ/∂S`, quoted in deltas per $1. Long options are +Γ and short options are −Γ.
- **Theta (θ, time decay, erosion)**: the change in value for one unit of time. The book's convention is **one calendar day, based on a 7-day week**, because news can arrive on weekends.
- **Vega**: the change in value for a **1-percentage-point** change in implied volatility. It is the same for the call and the put at the same strike and expiry.
- **Implied volatility (IV)**: the volatility input that makes the model theo equal the market price. It is the "sixth variable" that explains why two $40 stocks can have 40-strike calls priced at 0.50 and 2.00.
- **Rho (ρ)**: the change in value for a **1-percentage-point** change in the interest rate. Calls are +ρ and puts are −ρ.
- **Time value (extrinsic value)**: premium above intrinsic value. Only time value is exposed to theta and vega.
- **Put-call parity**: the no-arbitrage identity that links a call, a put, the stock and the carry on the strike. "A put is a call, a call is a put."
- **Short-stock rebate**: the interest a professional earns on the cash proceeds of a short sale. This is why higher rates make puts cheaper.
- **Moneyness**: how far ITM or OTM an option is, measured *proportionally*. A strike $5 ITM on a $20 stock is "deeper" than one $5 ITM on a $200 stock.

## Formulas & Reference Tables
- Delta P&L (first order): `ΔV ≈ Δ·ΔS`
- Delta + gamma: `ΔV ≈ Δ·ΔS + ½Γ·ΔS² = ((Δ₀ + Δ₁)/2)·ΔS`, with `Δ₁ = Δ₀ + Γ·ΔS`
- Full daily P&L attribution (per share): `ΔV ≈ Δ·ΔS + ½Γ·ΔS² + θ·Δt(days) + Vega·ΔIV(pts) + ρ·Δr(pts)`
- Position greek: `Σ (contracts × greek × 100)`, with the sign of the position (short = negative)
- Put-call parity, European, no dividend: `c + PV(K) = p + S`
- Trader's form, American equity, simple interest: `Stock = Call + Strike − Put − Interest + Dividend`, i.e. `C − P = S − K + Interest − Dividend`
  - `Interest ≈ K × r × (days/360)`. Traders use simple interest (360 here, 365 in ch06 and ch07; the choice shifts the figure by about 1.4% and desks follow their own convention). Models compound.
  - Synthetics: `Call = Stock + Put + Interest − Dividend − Strike` and `Put = Call + Strike − Interest + Dividend − Stock`
- Rho effect: when r rises, calls gain ρ_c per point and puts lose |ρ_p| per point. A 25 bp move ≈ ρ/4.
- **Scaling (price homogeneity)**: multiplying S and K by λ multiplies value, theta, vega and rho by λ, divides gamma by λ, and leaves delta unchanged. For example, a $30 stock's ATM vega of 0.085 becomes 0.850 on a $300 stock.

**How the greeks change with the other inputs** (summary of Exhibits 2.3–2.16)

| Greek | Moneyness | Less time to expiry | Higher IV |
|---|---|---|---|
| Delta | ITM → 1, OTM → 0, ATM ≈ 0.50 (call slightly > 0.50 because of interest) | ITM → 1 and OTM → 0 faster | ITM and OTM deltas are pulled toward 0.50 |
| Gamma | Peaks ATM (often at a slightly higher strike) | ATM gamma explodes, ITM/OTM gamma goes to 0 | Flattens the curve: ATM gamma falls, wings rise |
| Theta | Peaks ATM (most time value) | ATM decay accelerates non-linearly. OTM decays steadily | Higher theta (more premium to lose) |
| Vega | Peaks ATM | Falls (roughly with √T) | ATM vega is almost unchanged. Wing vegas rise |
| Rho | Larger ITM | Falls sharply (a 22-day ATM rho of 0.015 vs. 0.858 for a 750-day LEAPS) | Minor |

**Delta of a 50-strike call vs. time** (extract of Exhibit 2.3): with S = 46, delta is 0 at expiry, 0.15 at 1 month, 0.31 at 3 months and 0.42 at 7 months. With S = 54 it is 1.00, 0.87, 0.77 and 0.73. More time pulls deltas toward 0.50.

**ATM theta in the final 10 days** (Exhibit 2.12, $70 stock): 10d 0.075 → 5d 0.106 → 2d 0.171 → 1d 0.443. The whole remaining time value (about 0.44) disappears on the last day. A BS check at about 30% IV reproduces a 1-day value of 0.44.

## Mental Models
- **The model is a mirror, not an oracle.** It reflects the market. If several theos in a chain sit outside bid/ask, suspect an input (rate, dividend, days), not the market.
- **Think of delta as "shares I'm effectively long."** Summing contracts × Δ × 100 across the book gives a single number you can hedge with stock.
- **Gamma is the option buyer's friend on the move and the seller's enemy.** Long gamma makes winners accelerate and losers decelerate. Short gamma does the reverse.
- **Theta is the rent on gamma.** The ATM options with the most gamma also pay the most theta, especially close to expiry.
- **Vega lives where time value lives.** No time value (deep ITM or far OTM, or near expiry) means little vega.
- **Rho is a carry argument.** A deep ITM call at parity costs $40 instead of $100 for the stock. The $60 saved earns interest, so higher rates make calls richer. The short-stock rebate is the reason higher rates make puts cheaper.

## Worked Example
**1. Average-delta repricing** (call: S = 60, value 3.00, Δ = 0.50, Γ = 0.04)

| Stock | Delta | Average delta over the $1 step | Call value |
|---|---|---|---|
| 58 | 0.42 | 0.44 | 2.08 |
| 59 | 0.46 | 0.48 | 2.52 |
| **60** | **0.50** | — | **3.00** |
| 61 | 0.54 | 0.52 | 3.52 |
| 62 | 0.58 | 0.56 | 4.08 |

A put with Δ = −0.40 and value 2.25 works the same way: 1.87 at 61 and 1.53 at 62, or 2.67 at 59 and 3.13 at 58. The gains get bigger and the losses get smaller, which is long gamma at work.

**2. Greek-by-Greek daily P&L attribution** (checked with Black-Scholes)
Long 10 ATM calls: S = K = 60, 60 days, r = 1%, IV = 25%. BS gives value 2.473, Δ = 0.527, Γ = 0.0655, θ = −0.0210/day and vega = 0.0968. Overnight the stock rises to 61.50 (+1.50), one day passes and IV drops to 24% (−1 pt). Multiplier = 10 × 100 = 1,000.

| Source | Calculation (per share) | P&L ($) |
|---|---|---|
| Delta | 0.527 × 1.50 | +790 |
| Gamma | ½ × 0.0655 × 1.50² | +74 |
| Theta | −0.0210 × 1 | −21 |
| Vega | 0.0968 × (−1) | −97 |
| **Greek estimate** | | **+746** |
| Full BS revaluation (3.2205 − 2.4728) | | **+748** |

Interpretation: the greeks explain the day to within $2. The directional view paid (delta plus gamma), and the IV crush cost almost five days of theta.

**3. Put-call parity check** (S = 80, 3-month 80 strike, r = 5%, $0.25 dividend): `Interest = 80 × 0.05 × 90/360 = 1.00`. `C − P = S − K + Interest − Dividend = 0 + 1.00 − 0.25 = 0.75`, so a call at 3.75 against a put at 3.00 is consistent. A 25 bp rate rise adds 80 × 0.0025 × 0.25 = 0.05 of carry, widening C − P to 0.80. Over one year the same 25 bp would add 0.20.

## Anti-patterns
- **Treating theo as a price target**: a model value outside bid/ask points to a bad input, not a free trade.
- **Using delta alone for large moves**: it ignores gamma and understates gains for long options (and losses for short ones).
- **Reading delta as an exact probability**: it is a rough guide. The ITM probability under the model is N(d₂), which is below the call delta.
- **Comparing thetas from different vendors without checking the unit**: 1 trading day, 1 calendar day and 7 days are all used.
- **Reading a Friday intraday cheapening as an IV drop**: the desk may simply be taking the weekend out.
- **Ignoring rho on LEAPS**: it is negligible for short-dated options but material for long-dated ones.
- **Trusting one-click online greeks**: professionals use greeks from inputs they set themselves.

## Practitioner Notes
- Put-call deltas should add up to about 1.00 in absolute value. Deviations tell you something. An ITM American put with |Δ| above 1 − Δ_call (for example 0.14 + 0.89 = 1.03) is behaving like short stock because of early-exercise potential. An ITM call on a dividend payer near the ex-date gets extra delta for the same reason.
- ATM calls usually have Δ slightly above 0.50 and are worth more than the ATM put when rates are positive. The longer the expiry, the bigger the gap. Calls also show a higher theta than puts at the same strike, because the call starts with extra carry value that must decay to zero.
- Short-dated, low-IV ATM options have the highest gamma. Expect position delta to swing violently in expiration week.
- For American options, rho across a put-call pair shrinks as the put goes deep ITM (it becomes an exercise candidate). The combined rho can reach zero.
- Platform stress tests (±1, 2 or 3 standard deviations, IV and time shifts) are the practical way to see second-order effects the point greeks miss.
- Parity arbitrage belongs to professionals trading size for pennies. Retail traders use parity to buy or sell the *cheaper synthetic* instead of the listed option.

## Key Takeaways
1. Calibrate the model to the market (IV) first, then trust the greeks it produces.
2. Summarize every position as delta, gamma, theta, vega and rho. Long options are +Γ, +vega and −θ, short options the reverse.
3. Reprice with the average delta (Δ + ½ΓΔS) for any meaningful move.
4. Gamma, theta and vega all peak ATM. Near expiry, ATM gamma and theta explode while vega fades.
5. Higher IV pulls deltas toward 0.50, flattens gamma and raises theta.
6. Put-call parity ties calls and puts together. Rho is its carry term: calls gain and puts lose when rates rise.
7. A daily Greek-by-Greek P&L attribution is the core habit of an options trader.

## Connects To
- **ch03**: how implied and realized volatility are defined and traded.
- **ch04**: the gamma-theta trade-off and vega risk in depth.
- **ch06**: put-call parity, synthetics, conversions and reversals.
- **ch07**: rho in depth, including LEAPS and rate changes.
- **ch08**: dividends, early exercise and delta anomalies.
- **`hull-derivatives` ch15**: the Black-Scholes-Merton model behind the greeks.
- **`hull-derivatives` ch19**: the formal definitions of the Greek letters and the Taylor-series P&L.
- **`hull-derivatives` ch11**: put-call parity and bounds for American options.
- **`cfa-derivatives` ch04**: BSM greeks and delta hedging in the CFA framework.
