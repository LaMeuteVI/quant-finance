# Chapter 8: Dividends and Option Pricing
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Part I, Chapter 8

## Core Idea
Dividends have no greek, but they move option prices, create exercise decisions, distort deltas and corrupt implied volatility if the model input is wrong. Treat the dividend stream (amounts **and** ex-dates) as a pricing input to monitor like delta, vega or rho. The money is lost or made in three places: forgetting to exercise ITM calls before the ex-date, feeding the model a wrong date or amount, and being long or short calls/puts when the dividend policy changes.

## Frameworks Introduced
- **The four dividend dates**: declaration date (amount and dates announced), ex-dividend date (first day the stock trades without the dividend), record date (holders of record collect; shorts owe), payable date (cash arrives, weeks later).
  - When to use: to know which overnight you must hold stock or exercise calls.
  - How: settlement takes time, so the record date is effectively irrelevant; what counts is the **ex-date**. To receive the dividend you must own the stock at the *open* of the ex-date, i.e. buy before the prior day's close. Options holders never receive dividends; only exercised (stock) positions do.
  - Failure mode: the "buy the close, sell the open" dividend capture. The stock opens roughly lower by the dividend (a $50 close opens near $49.75 for a $0.25 dividend) and overnight gap risk remains, so it is neither riskless nor profitable.
- **Conversion/reversal across the ex-date (neutrality test)**: a dividend changes the stock-to-synthetic spread but not the P&L of a hedged position.
  - How: synthetic stock = `K + Call − Put`. Before the ex-date, the synthetic-vs-stock gap = interest − dividend. After the ex-date the gap = interest only, because the dividend has left the model. The stock falls by D, the gap widens by D, and the dividend received offsets it. Net P&L = 0 (apart from theta).
  - Why it works: the stock leg drops by D but the owner holds stock-plus-dividend, so total assets are unchanged.
- **Early-exercise decision rule for ITM calls (the day before the ex-date)**: compare the dividend benefit of exercising with what you can get for the put.
  - When to use: every ex-date, for every ITM call you are long (outright, in a reversal, in a spread).
  - How: exercise value = `Dividend − Interest` (the price at which exercising effectively sells the put synthetically). Then:
    - `Dividend − Interest > Put Bid` → exercise (you are selling the put for more than the market pays).
    - `Dividend − Interest < Put Bid` → do not exercise; sell the put instead if you want out.
    - `Dividend − Interest = Put Bid` → indifferent on value.
  - Use the put **bid** because that is the price at which you can actually sell it.
  - Why exercise rather than leg out: selling the call at the bid and buying back stock at the offer costs spread and slippage. Exercising closes both legs at parity in one step.
  - Failure mode: forgetting. Not exercising is a costly, fully controllable error.
- **Short-side edge ("skating")**: a trader long stock and short ITM calls at parity gains if some long-call holders forget to exercise. Stock remaining on the ex-date collects the dividend. If `Dividend > interest on the stock`, this is a small arbitrage.
  - How: dividend plays use ITM call spreads the afternoon before the ex-date, preferably in high open-interest names and the front month, where forgetting is most likely. Both calls must be deep ITM with puts worth less than `Dividend − Interest`.
  - Trade-off: only viable with very low transaction costs (professionals and large retail).
- **Dividend input discipline (model inputs)**: price the option off the expected **schedule** (date and amount for each dividend through expiration), not one flat number.
  - How: (1) stable payer: enter the regular amount; (2) grower: project the usual raise on the usual date (GE raised near December for years, so options expiring after December used the higher amount); (3) uncertain payer: estimate from history, then update at each declaration; (4) correct the date immediately when declared.

## Key Concepts
- **Declaration date**: announcement of amount, record and payable dates.
- **Ex-dividend date (ex-date)**: the date the stock trades without the dividend; the open price is lower by about D.
- **Record date**: shareholder-of-record date; effectively the ex-date plus settlement lag.
- **Payable date**: date cash is paid.
- **Gap open**: overnight price change; why dividend capture is not riskless.
- **Synthetic stock gap (before ex-date)**: `Synthetic − Stock = Interest − Dividend`.
- **Synthetic stock gap (after ex-date)**: `= Interest` only.
- **Early exercise (American calls)**: ITM calls may trade at parity before an ex-date because exercise captures the dividend.
- **Exercising as selling the put**: exercising an ITM call in a reversal equals synthetically selling the put at `Dividend − Interest`.
- **Skating**: surviving a day without assignment on a short ITM call.
- **Strange deltas**: call delta ≈ 1.00 at parity plus a residual put delta of 0.05 or more gives a synthetic delta above 1.00 (absolute call + put deltas of 1.07–1.08 are common).
- **Special dividend**: unscheduled lump payment that resets option values overnight (Microsoft paid $3 in 2004).
- **Bad date**: a model ex-date later than the real one keeps the dividend in the theo, understating calls and overstating IV.

## Formulas & Reference Tables
- Put-call parity after the dividend has left the model (European-style approximation): `Call = Put + Stock − Strike + Interest`, where `Interest = K × r × days/365`.
- With dividends before expiry: `Call − Put = Stock − Strike + Interest − PV(Dividends)`. Higher dividends lower calls and raise puts.
- Exercise threshold (ITM call in a reversal): `Dividend − Interest` versus `Put Bid`.
- Ex-date open (unchanged market): `S_open ≈ S_close − D`.
- Implied-vol distortion from a bad date: `ΔIV ≈ (Theo_right − Theo_wrong) / Vega` (in vol points, with vega per 1 vol point).

| Situation | Calls | Puts |
|---|---|---|
| Dividend raised / special dividend | Fall (long loses, short gains) | Rise (long gains, short loses) |
| Dividend cut / omitted | Rise | Fall |
| Ex-date passes, stock unchanged | Rise slightly vs. stock (dividend removed) | Fall slightly |
| Longer expiry | More dividends embedded, larger effect | Same |

| Dividend-rule outcome | Action |
|---|---|
| `D − Int > Put Bid` | Exercise the ITM call the day before the ex-date |
| `D − Int < Put Bid` | Keep the call, sell the put if desired |
| `D − Int = Put Bid` | Indifferent |

## Mental Models
- **Dividends are a negative-carry-on-calls, positive-carry-on-puts input**: the stock owner receives the dividend, the option holder does not. So dividends depress calls and lift puts, like negative interest.
- **Treat the ex-date as a scheduled repricing event**: the model removes the dividend and values step even with the stock unchanged. Expect the option market to reprice with it, and be alert for wrong-date artefacts.
- **Exercising = selling the put**: reduces the exercise choice to a price comparison you can do in your head.
- **Computer deltas near ex-dates are suspect**: override them with common sense; ITM calls behave like stock, but the synthetic can exceed 1.00 delta.
- **Dividend exposure grows with time to expiry**: a two-year option holds many dividends. A small per-share change compounds (six dividends in the XYZ example).

## Worked Example
**1. Conversion across the ex-date** (D = 0.25, stock 50, 50 strike): before the ex-date, put 2.34, call 2.48. Long stock at 50, long put, short call = synthetic short at `50 + 2.48 − 2.34 = 50.14`, gap to stock 0.14 (interest minus dividend). The stock opens at 49.75 and options lose 0.02 each to theta (put 2.32, call 2.46). Synthetic short remains at 50.14 (`50 + 2.46 − 2.32`). Gap to stock is 0.39 = 0.14 + 0.25 (all interest). Position value: before, stock 50; after, stock 49.75 + 0.25 dividend = 50. P&L from the dividend mechanics: zero.

**2. Reversal and early exercise** (stock 70, D = 0.40, 60 call at 10.00, 60 put at 0.05, 24 days, 5%, interest on the strike ≈ 0.20). Short stock at 70, long call, short put. If held through the ex-date with the stock unchanged: stock 69.60, parity call = `0.05 + 69.60 − 60 + 0.20 = 9.85`, i.e. a gain of 0.25 above parity, but the short stock owes 0.40. Net `0.25 − 0.40 = −0.15`. Exercising the call the day before the ex-date avoids that loss. Exercising is equivalent to selling the put at `0.40 − 0.25 = 0.15` (dividend avoided minus call time value gained), and the source's rule-of-thumb threshold is `Dividend − Interest = 0.40 − 0.20 = 0.20` versus a put bid of 0.05, so exercise. All figures verified in Python.

**3. Bad ex-date** (30-day 75 call, stock 76, vol 20%, 5.25%, D = 0.25): correct theo after the ex-date is 2.43; with the dividend wrongly kept one day later, the theo is 2.27 (theta ≈ 0.03 plus dividend effect). Gap 0.16 ÷ vega 0.08 = **2 IV points**; the trader would mistake the call for 2 vol points richer than it is.

**4. Dividend-size shock** (XYZ, 528 days, 60 strike, stock 61, 25.5% vol, 5%): quarterly dividend 0.10 → 0.50 (six dividends). Call 9.65 → 8.13 (−1.52); put 5.42 → 6.08 (+0.66). A Black-Scholes escrowed-dividend check (PV of the extra dividends ≈ 2.31) gives call −1.47, close to the book; the book's put move (+0.66) is smaller than the European model's (+0.84) because the puts are American and carry an early-exercise premium. Use the book's figures as the quoted reference.

## Anti-patterns
- **Forgetting to exercise ITM calls before the ex-date**: the dividend, not direction, decides P&L; the loss is entirely avoidable.
- **Legging out instead of exercising**: pays bid/offer twice and risks slippage between legs.
- **Buying the close and selling the open for "free" dividends**: the open is lower by D and the gap risk is real.
- **Entering a flat dividend or wrong ex-date**: produces a wrong theo and a wrong implied vol, most damaging near expiration and in LEAPS.
- **Trusting model deltas near the ex-date**: synthetic deltas above 1.00 confuse delta-neutral books.
- **Holding long-dated calls through a dividend policy risk (special dividends, hikes) unaware**: the loss sits in every remaining dividend, not just the next.
- **Ignoring dividend risk in names with erratic payouts**: the more uncertainty, the more hidden risk.

## Practitioner Notes
- **Volume spike the day before the ex-date is mechanical**: heavy ITM call trading (tens of thousands of contracts in names averaging a couple of thousand) reflects dividend arbitrage and exercise, not a directional view. Do not read it as a signal.
- **Do the math before every ex-date** for every option class traded; it takes a minute (`D − Interest` vs put bid).
- **Exercise rather than leg out**: one action, parity price.
- **Where "skating" works**: front month, high open interest, deep ITM, and low transaction costs; the edge is other people's oversights.
- **Dividend data sources**: news services, company investor-relations pages and phone lines; update the model at each declaration.
- **Case study, GE**: for decades its dividend rose by a few cents each December; traders projected the raise into options expiring after December. It then held flat in December 2008, then was cut from 0.31 to 0.10 (ex-date 06/18/09), its first cut in over three decades. Cuts help calls and hurt puts. Predictable patterns break; carry a range of dividend scenarios on LEAPS.
- **Stable payer (Exelon, 0.525 quarterly)**: little dividend risk, enter the regular amount.
- **Long-dated options carry the most dividend risk**: a 0.40 change on six dividends moved the call by 1.52 (≈ 16% of its 9.65 value).

## Key Takeaways
1. Only the ex-date matters; you must hold the stock at the open of that day to be paid, and the stock opens lower by about the dividend.
2. Before the ex-date a synthetic's spread to stock is interest minus dividend; afterward it is interest alone; hedged positions have zero net P&L from this.
3. Long ITM calls near an ex-date: exercise if `Dividend − Interest > Put Bid`; do the calculation daily around ex-dates.
4. Exercising beats legging out because it avoids bid/offer and slippage.
5. Higher dividends hurt calls and help puts; cuts do the reverse; the effect scales with the number of dividends before expiry.
6. A wrong ex-date or dividend amount shows up as a false IV reading (two vol points in the example).
7. Model deltas (synthetic above 1.00) near the ex-date are unreliable; apply judgment.
8. Project dividends as a schedule and update it with each declaration; erratic payers need scenario thinking.

## Connects To
- **ch06**: conversions, reversals and put-call parity are the framework for every dividend calculation here.
- **ch07**: interest (rho) and dividends both enter the parity gap; dividends are the opposite-sign carry.
- **ch03**: bad dividend data corrupts implied volatility.
- **ch04**: time decay (theta) accounts for small option changes across the ex-date.
- **ch12**: delta-neutral books need clean deltas; be careful near ex-dates.
- **`hull-derivatives`**: European/American option pricing with known dividends, put-call parity with income.
