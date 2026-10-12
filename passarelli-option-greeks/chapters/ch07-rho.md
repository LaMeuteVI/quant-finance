# Chapter 7: Rho
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 7

## Core Idea
Rho is the "quiet greek": the change in option value per one-percentage-point change in the interest rate. It is positive for calls, negative for puts, and grows with strike and time to expiry. For short-dated options it is noise. For LEAPS, conversions, reversals, boxes and jelly rolls it matters. **Rho is important to understand but rarely practical to trade for anyone without market-maker costs.**

## Frameworks Introduced
- **Rho from put-call parity**: interest sits in `Call + K − Interest = Put + Stock`. If rates rise, calls must rise and puts must fall by the same amount to keep parity. Hence call rho > 0, put rho < 0, and at a strike the call rho and put rho are roughly equal in size.
  - When to use: to reason about direction and magnitude of rate exposure without a model.
  - How: `Interest = K × r × days/365`; rho depends on the three drivers (strike, rate level, time). A synthetic stock at a strike has rho of about `K × T / 100` per rate point.
- **Rho scales with time**: rho is roughly proportional to `T`. Rate changes early in the life of a long option matter more than rate changes late in its life.
  - How: compute the rho at each future date, not today's. A 25 bp cut today costs `0.25 × rho_today`; a cut six months later costs `0.25 × rho_then`, which is smaller.
- **Rho in LEAPS trade planning**: for a long-dated option, add rho to the usual delta/gamma/theta/vega checklist. Compare rho as a percent of option value (typically 5–8% for two-year options).
  - When to use: choosing between a near-term option and LEAPS for a directional view when a rate decision is expected.
- **Backing out the interest rate priced into the market** (implied rate curve): when model values for ATM calls and puts across months don't fall between the call and put markets, adjust the interest input by month until the theoretical values sit in the middle of both markets.
  - How: fix stock, strike, IV and dividend. Solve the interest rate so calls and puts both fit. Longer months that need a higher rate imply the market expects rate hikes; lower rates imply cuts.
  - Failure mode: attributing the discrepancy to volatility. A call-high, put-low pattern that grows with maturity is rate expectations (or borrow/dividend effects), not IV.
- **How to trade rho purely**: rho can be isolated only by removing other greeks with conversions, reversals, boxes or jelly rolls (ch06). Conversion: long stock, long put, short call = negative rho (profits if rates fall). Reversal: positive rho. Jelly roll: rho long one month, short another.
  - Failure mode: bid-ask cost. For non-market makers, the spread exceeds the expected rho profit.

## Key Concepts
- **Rho**: `∂V/∂r`, quoted per +1 percentage point (100 bp).
- **Positive rho (calls, reversals)**: gains when rates rise. **Negative rho (puts, conversions)**: gains when rates fall.
- **Quiet greek**: rho is small next to delta, theta and vega, especially for short-term options.
- **Long-term option (LEAPS)**: rho grows with `T`, so it becomes material at 1 to 2 years.
- **Interest variable in parity**: `K × r × T`; the carrying cost avoided by owning a call instead of stock.
- **Priced-in rates**: expected rate changes are embedded in option prices for months after the anticipated move.
- **Snapshot nature**: rho is measured at a given price, IV, rate and date; it changes as time passes.
- **Rho as percent of value**: the practical way to judge importance (5 to 8% for two-year ATM options).
- **Rate that matters**: the trader's own financing rate, not "the" risk-free rate.
- **Bid-ask hurdle**: LEAPS spreads are often more than 0.40 wide, exceeding typical rho gains.
- **Interest-rate uncertainty**: when the direction of rates is unclear, long-dated options carry real risk. Short-dated options are the safer choice.

## Formulas & Reference Tables
- Interest variable: `Interest = K × r × (days/365)`
- Rho definition: call ρ > 0, put ρ < 0; `ΔV ≈ ρ × Δr(in points)`
- European BS (no dividend): `ρ_call = K T e^(−rT) N(d₂) / 100`, `ρ_put = −K T e^(−rT) N(−d₂) / 100`
- Call rho minus put rho at one strike ≈ `K T e^(−rT) / 100` (from parity), i.e. about `K×T/100`
- Rho as a fraction of value: `ρ / V`
- Rate-cut path for a LEAPS: rho declines as `T` shrinks. Use the rho at the date of each expected move.

**Rho by expiry (120-strike ATM calls, 5.5% rate, book figures)**

| Expiry | Days | Rho | Gain for +25 bp |
|---|---|---|---|
| July | 38 | 0.068 | 0.017 |
| October | 130 | 0.226 | 0.057 |
| January | 221 | 0.385 | 0.096 |

**Short-term vs LEAPS ATM calls (stock 59.95, strike 60)**

| | 44-day call (1.60) | 639-day LEAPS (7.60) |
|---|---|---|
| Delta | 0.55 | 0.71 |
| Gamma | 0.115 | 0.03 |
| Theta | about −0.02 | about −0.01 |
| Vega | 0.08 | 0.27 |
| Rho | 0.039 | 0.638 |

## Mental Models
- **Rho ≈ strike × time**: big strike and long time means big rho. Ignore it for a 30-day $20 stock option, respect it for a two-year $150 strike.
- **Rho is a slow-burn greek**: rate paths are stretched over months, and each cut hurts less than the last because the option's life is shrinking.
- **Buy LEAPS for time and vega, then check rho**: you trade lower theta and higher vega for interest exposure. A long call is long rates; a long put is short rates.
- **The rate is in the forward curve**: if the Fed is expected to move, longer options already include it. Surprise (relative to expectation) creates P&L.
- **Rho trades are conversion trades**: only a flat book of conversions and rolls isolates rates, and only cheap-execution firms profit.

## Worked Example
Which greek moves the LEAPS call P&L? (book's 2-year 70-strike call: stock 70, IV 20%, rate 8%, price 13.60, Δ 0.760, θ −0.013, vega 0.308, rho 0.793.)

1. Rho gain from a 25 bp hike: 0.793 × 0.25 = 0.198 (about 0.20), which is about 1.5% of the 13.60 price. Rho itself is 0.793 ÷ 13.60 = 5.8% of value.
2. Six weeks pass (42 days) before the next Fed meeting. Stock falls just 0.60: delta loss = 0.760 × 0.60 = 0.456. Theta: 0.013 × 42 = 0.546.
3. Net before vega: +0.198 (rho) + 0.198 (second hike, at most) − 0.456 − 0.546 is negative. A 1.5-point IV drop costs 1.5 × 0.308 = 0.46 on its own.
4. Interpretation: delta, theta or vega swamps rho. Add a wide bid-ask (often above 0.40) and buying LEAPS to trade rates is not practical.

LEAPS rho decay (639-day call): rho 0.638 today: a 25 bp cut costs 0.160. After six months rho about 0.46: the next cut costs 0.115. After another six months rho about 0.26: 0.065.

Implied-rate example (ABC, 70 strike, IV 20%, no dividend, August one month out): with an 8% rate the model shows calls too low and puts too high for Sep to Mar. Use 8.25%, 8.50%, 8.75% for Sep, Dec, Mar and the theoretical values fall inside the markets: the market prices rate hikes.

## Anti-patterns
- **Ignoring rho on LEAPS**: two-year options carry 5 to 8% of value in rho, and it is compounded by wide markets.
- **Using today's rho for a multi-meeting rate view**: rho shrinks as expiry approaches, so later moves matter less.
- **Buying LEAPS purely as an interest-rate bet**: delta, theta and vega dominate and spreads eat the profit.
- **Blaming IV for a call/put pricing gap that grows with maturity**: check the rate (and borrow and dividends) first.
- **Trading conversions or boxes as a retail account for rho**: bid-ask costs cancel the edge.
- **Forgetting the sign**: a put buyer is short rates, a conversion holder is short rates, a reversal holder is long rates.

## Practitioner Notes
- Rule of thumb: `rho/price` around 5 to 8% for two-year ATM options; under 1% for options of one to two months.
- Market makers care about rho on large conversion books (0.090 rho × 0.25 = $2.25 per 1-lot for a 25 bp move, $11,250 for 5,000 lots).
- For a directional LEAPS buyer: quantify rho as part of the plan, especially around FOMC meetings with real uncertainty. If IV is at a yearly low, LEAPS vega usually dominates the case for buying.
- If the market has a consensus about rate direction it is priced in. Uncertainty about that consensus gives the risk.
- In short-dated trades, rho is ignored by nearly everyone, including the trader who is right.
- Near-zero rates (as in 2009 to 2015) compress rho and interest effects in parity; higher-rate regimes (2022 onward) restore them. The formula scales with the rate level of the moment.

## Key Takeaways
1. Call rho > 0, put rho < 0; rho comes from the interest term in put-call parity.
2. Rho rises with strike and time; ATM rho ≈ `K×T/100` per point for the synthetic.
3. Short-dated options: ignore. LEAPS: rho is 5 to 8% of value and belongs in the trade plan.
4. Use rho at the date of each expected rate move, because it declines as expiry nears.
5. Rates are priced into options by month; back out the implied rate to see the market's expectation.
6. To trade rates alone, isolate rho using conversions, reversals, boxes or jelly rolls; that is a market-maker business.
7. Bid-ask spreads and other greeks dominate any LEAPS-based interest-rate bet.

## Connects To
- **ch06**: conversions, reversals, boxes and jelly rolls (the instruments that isolate rho).
- **ch04**: LEAPS as a strike/expiry choice and the price-time trade-off.
- **ch08**: the other part of the basis (dividends) and its effect on calls and puts.
- **ch11**: calendar and diagonal spreads (rho across months).
- **`hull-derivatives`**: derivation of rho and the effect of the rate in Black-Scholes.
