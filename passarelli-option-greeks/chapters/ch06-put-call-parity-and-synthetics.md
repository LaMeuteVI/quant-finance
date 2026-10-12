# Chapter 6: Put-Call Parity and Synthetics
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 6

## Core Idea
For one strike and expiry, a call and a put are the same instrument once stock and the carry "basis" (interest and dividends) are added. **Every option position has a synthetic twin; only delta changes when stock is added.** Learn the four synthetic identities and every later spread reduces to a handful of building blocks. Conversions, reversals, boxes and jelly rolls are the same identity used to isolate interest and dividend risk.

## Frameworks Introduced
- **Put-call parity (trader form)**: `Call + Strike − Interest + Dividend = Put + Stock`
  - When to use: to price one option from the other, to derive any synthetic, and to sanity-check IVs.
  - How: `Interest = Strike × rate × (days ÷ 365)` (simple interest, book convention). `Dividend` = dividends paid before expiry. Rearrange to isolate the leg you want (see the table).
  - Why it works / failure mode: arbitrage. If the call is too cheap versus the married put, buyers push it back. It is exact for **European** options; American exercise (deep ITM puts, calls before ex-date) can break it.
- **The basis**: the interest and dividend terms of parity. Interest favors the call (no capital tied up), dividends favor stock (calls do not receive them). Interest raises calls and lowers puts; dividends do the opposite.
- **Four synthetic identities** (after basis): long call = long put + long stock; short call = short put + short stock; long put = long call + short stock; short put = short call + long stock.
  - How: long options pair with long options plus stock; short options with short options plus stock. Gamma, theta and vega match and only delta differs.
- **Synthetic stock (combo)**: long call + short put (same strike, same expiry) = long stock. The effective purchase price is `K + (call − put)`, whichever option ends ITM. Reverse the signs for synthetic short stock.
- **Conversion / reversal**:
  - Conversion = long stock + long put + short call (same strike/expiry). Long stock offset by synthetic short stock. Flat delta, small gamma, theta and vega; **negative rho** (a bet that rates fall).
  - Reversal (reverse conversion) = short stock + short put + long call. **Positive rho** (short-stock rebate earns more when rates rise).
  - When to use: market makers flattening inventory and isolating interest and dividend exposure.
  - How: price the synthetic at `stock + interest − dividends`. Trade it only when the synthetic's price is better than fair by more than costs. Market makers try to leg in for a slightly better price than fair.
- **Box** = long synthetic at one strike + short synthetic at another (same expiry) = a zero-risk loan. Fair value = `strike difference − interest`. **Jelly roll** = the same strike across two months, long synthetic in one and short in the other: an interest-rate and pin-risk management tool.
- **Pin-risk control**: near expiry, market makers close conversions/reversals, or roll them (jelly roll), or box off strikes. Reason: at-the-strike outcome (which options are assigned or exercised) is unknown.
- **Which rate to use**: interest is personal. Price a conversion (you borrow to buy stock) at your **borrow rate**. Price a reversal (you earn a rebate) at your **short-stock rebate rate**.

## Key Concepts
- **Married put**: long stock plus long put per share; economically a long call.
- **Synthetic call / put / stock**: a combination of the other instruments with the same payoff and delta after the basis.
- **Combo**: another name for synthetic stock (call and put at the same strike).
- **Basis**: interest and dividend adjustment in parity.
- **Short-stock rebate**: interest professionals earn on short-sale proceeds.
- **Delta of a synthetic**: call Δ + stock Δ (+1 for long, −1 for short). Equals the put's delta (`Δput ≈ Δsynthetic put`, `Δcall ≈ Δsynthetic call`).
- **Delta rule of thumb**: for European, no-dividend options, `|Δcall| + |Δput| ≈ 1.00` at one strike.
- **Early exercise premium / anomaly**: deep ITM American puts can trade at parity while the call has time value, and ITM calls trade at parity before ex-dates.
- **Rho (of a conversion)**: change in value for a one-point rate move. The synthetic component carries the rate risk.
- **Pin risk**: uncertainty about assignment at a strike near expiry.
- **Flat the strike**: a market maker holding equal calls and puts (synthetically flat) at each strike.
- **Leg / legging in**: building a multi-leg position one leg at a time, accepting slippage risk.

## Formulas & Reference Tables
- Academic parity: `c + PV(K) = p + S` (European, no dividends)
- Trader parity: `Call + K − Interest + Dividend = Put + Stock`; `Interest = K × r × days/365`
- Synthetic identities (basis included):

| Position | Equals | Formula |
|---|---|---|
| Long call | Long put + long stock | `Call = Put + Stock − K + Interest − Div` |
| Long put | Long call + short stock | `Put = Call − Stock + K − Interest + Div` |
| Short put | Short call + long stock | `−Put = −Call + Stock − K + Interest − Div` (covered call) |
| Short call | Short put + short stock | `−Call = −Put − Stock + K − Interest + Div` |
| Long stock | Long call + short put | `Stock = Call − Put + K − Interest + Div` |
| Short stock | Short call + long put | `−Stock = −Call + Put − K + Interest − Div` |

- Synthetic price of stock: `K + Call − Put`; fair value `= Stock + Interest − Div`.
- Conversion edge = (synthetic price − stock price) − interest + dividends. Fair value 0.
- Box fair value: `(K₂ − K₁) − (K₂ − K₁) × r × days/360` (the book uses a 360 day basis in the box example, 365 elsewhere).
- Rho of a conversion ≈ `−(K × T)/100` per one rate point (T in years). Reversal is the opposite sign.
- Delta of the synthetic put: `Δcall − 1`. Of the synthetic call: `Δput + 1`.

**Exhibit summary (50-strike pair on a $50 stock, 66 days, American): call Δ 0.554, put Δ −0.457, Γ 0.075/0.078, θ 0.020/0.013, vega 0.084/0.084.** The vegas are equal (the IVs should match), and gammas nearly so. Call theta exceeds put theta because interest raises call time value.

## Mental Models
- **A call is a put, a put is a call.** Ask "which is cheaper to hold after carry?" not "which is right?". Both are the same trade with different capital.
- **Stock is the only greek-neutral ingredient**: adding it only shifts delta (`+1` for long, `−1` for short). So convert positions to whichever wrapper has the best margin, liquidity and dividend treatment.
- **A conversion is a loan**: you are long stock (a borrower) and synthetically short at a higher price (the lender's yield). You earn the interest built into the synthetic.
- **The interest sits in the call-put gap**: `call − put = stock − strike + interest`. At the money the gap equals the interest.
- **Put IV ≈ call IV**: a large gap is a dividend, borrow-cost or early-exercise story, not a free trade.

## Worked Example
Conversion on a 51.54 stock, 71 days, 5% rate, no dividend (the book's example).
- Buy 100 shares at 51.54. Sell 50 call at 3.50. Buy 50 put at 1.50.
- Synthetic short price = `K + call − put` = 50 + 3.50 − 1.50 = 52.00, which is 0.46 above the stock.
- Interest at the strike = 50 × 0.05 × 71/365 = 0.486. So the position "earns" 0.46 against 0.486 of carry: fair (gap 0.026 comes from rounding and the put's early-exercise value).
- Rho check: conversion rho −0.090. A 25bp move = 0.090 × 0.25 = 0.0225 per spread, or $11,250 on 5,000 spreads at $100 multiplier.
- Delta: +1.00 (stock) − 0.654 (short call, call Δ = +0.654) − 0.354 (long put, put Δ = −0.354) = −0.008. The book reports this small negative bias.
- Interpretation: the tiny negative delta is the early-exercise effect. If the stock falls sharply, the put goes to parity and can be exercised early, capturing the 0.46 before paying full interest.

Box: a 60/70 box (strikes differ by 10) for 90 days at 6%: interest = 10 × 0.06 × 90/360 = 0.15; fair value 9.85.

## Anti-patterns
- **Assuming parity holds exactly for American options**: it breaks for deep ITM puts and ITM calls before ex-dividend dates. Deltas can then sum to 1.07 to 1.08.
- **Ignoring the basis when comparing married puts and calls**: the married put costs more capital, and the call misses dividends.
- **Using one generic rate for every conversion/reversal**: the relevant rates differ (borrow vs rebate).
- **Holding conversions or reversals into expiry at a strike near the stock**: pin risk (unknown assignment, unwanted delta after expiry).
- **Treating a "flat" conversion as risk-free**: rho, early exercise and dividend changes remain.
- **Retail trading of boxes and conversions for "arbitrage"**: bid-ask costs exceed the tiny edge. Market makers, who buy bid and sell offer, can do it.

## Practitioner Notes
- Market makers hedge a call bought with short stock, then sell the put and sell more stock to make a reversal. They try to lock a small edge (for example buying a conversion at 0.50 over vs 0.46 fair, then legging out at 0.45 over).
- Boxes are used to clear inventory (conversion at one strike + reversal at another leaves four option legs, and the stock legs cancel) and to borrow or lend money at a rate.
- The rate a conversion or box implies is effectively the trader's own financing rate, so price it with the trader's actual borrow or rebate rate, not a textbook risk-free rate.
- Use parity to sanity-check quotes. If puts and calls at one strike imply different IVs, look at dividends, hard-to-borrow stock, or early-exercise value.
- For any complex spread, first convert every leg to calls (or puts) with a synthetic. Compare only after the basis.

## Key Takeaways
1. Parity: `Call + K − Interest + Dividend = Put + Stock`. Memorize it and its rearrangements.
2. Longs pair with longs; shorts pair with shorts. Adding stock changes only delta.
3. Synthetic stock is a long call plus a short put (same strike and expiry); fair price = stock + interest − dividends.
4. Conversion = long stock + long put + short call (rho negative). Reversal is the mirror (rho positive).
5. A box is a zero-risk loan valued at strike width minus interest.
6. Jelly rolls trade interest across months and are used to roll conversions before pin risk.
7. American exercise breaks parity when deep ITM puts or dividend-eve calls hit parity.
8. Choose the interest rate that matches the trade: borrow rate for conversions, rebate rate for reversals.

## Connects To
- **ch05**: covered call = short put; covered put = short call.
- **ch07**: rho and interest-rate sensitivity (the risk conversions isolate).
- **ch08**: dividends and early exercise (the other side of the basis).
- **ch09 to ch16**: every spread can be re-expressed with calls or puts by synthetics.
- **`hull-derivatives`**: put-call parity for European options with dividends; American bounds.
