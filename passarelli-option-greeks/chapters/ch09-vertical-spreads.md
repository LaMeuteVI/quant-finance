# Chapter 9: Vertical Spreads
> **Source**: Dan Passarelli, *Trading Option Greeks*, 2nd ed. (Bloomberg Press / Wiley, 2012), Chapter 9 · Part: Spreads

## Core Idea
A vertical spread (long one option, short another of the same type and expiry, different strikes) lets a trader **keep the Greek he wants (usually delta) and spread off the ones he does not want (theta, vega, gamma)**, at the price of capped profit. The spread's Greeks are driven by whichever strike is at-the-money: near the long strike it trades like a long-volatility position, near the short strike like a short-volatility, income position. Every vertical must finish at or through the **short strike**, and time must pass, to earn its maximum. Credit and debit verticals on the same strikes are synthetically the same trade (put-call parity), and a call vertical plus the opposite put vertical is a **box**.

## Frameworks Introduced
- **The four verticals** (same underlying, same expiry, same option type, two strikes; by convention the lower strike is quoted first, e.g. "the 75 80 put spread"):

  | Spread | Construction | Cash flow | Delta | Max profit | Max loss | Breakeven at expiry |
  |---|---|---|---|---|---|---|
  | Bull call | long K₁ call, short K₂ call (K₁<K₂) | debit D | + | (K₂−K₁) − D | D | K₁ + D |
  | Bear call | short K₁ call, long K₂ call | credit C | − | C | (K₂−K₁) − C | K₁ + C |
  | Bear put | long K₂ put, short K₁ put | debit D | − | (K₂−K₁) − D | D | K₂ − D |
  | Bull put | short K₂ put, long K₁ put | credit C | + | C | (K₂−K₁) − C | K₂ − C |

  - Three expiry regions (below both strikes, between, above both) instead of the two of a single option. Between the strikes the ITM leg leaves a stock position at an "effective price" equal to the breakeven.
- **Greek migration rule (the ATM strike dominates)**:
  - Underlying at the **long strike**: long gamma, long vega, short theta. The spread is a decaying asset that needs movement toward the short strike.
  - Underlying **midway between the strikes**: gamma, theta and vega of the two legs roughly cancel. The position is an almost **pure leveraged delta** play.
  - Underlying at the **short strike**: short gamma, short vega, long theta. The spread is now an income trade that wants the stock to sit still.
  - Delta keeps the same sign throughout (bullish or bearish by construction) and is largest between the strikes.
  - When the underlying moves from one strike to the other, the trade has changed character. Ask: *"If I didn't have this position on, would I want it now?"*
- **Vertical vs outright option (price and time trade-off)**:
  - Vertical always costs less than the outright long option and carries a disproportionately small theta/vega for its delta.
  - For moves **up to the short strike**, especially slow ones, the vertical wins; the vertical needs expiry (decay of the short leg) to realise its full value.
  - For **fast moves or moves far beyond the short strike**, the outright option wins: bigger delta, uncapped payoff.
- **Three volatility plays with verticals**:
  1. Speculate on IV with a roughly constant underlying: to be vega-short, sell the ATM strike and buy an OTM strike, choosing calls or puts to lean with your directional bias. Delta is the bigger risk (hedge with stock, delta-neutral trading, ch12–13).
  2. Profit from IV changes caused by the underlying's movement: bull spreads benefit from the equity "spot up / vol down" pattern (vega turns negative near the short strike as the stock rallies; vega turns positive near the long strike as the stock drops and IV firms). The benefit is paid for through the skew: the lower strike you buy carries a higher IV than the upper strike you sell.
  3. Special situations: rumored takeover. Buy an ITM/OTM call spread (e.g., 50 60 with the stock at $55) instead of calls whose IV is already bid. Near-zero vega at entry; if a cash deal at $60 is announced, the stock pins below $60, IV collapses and the short 60 call earns vega and theta: "win, win, win".
- **Credit/debit equivalence**:
  - Conventional use: credit spreads (short ATM/OTM, long further OTM) as income trades; debit spreads (long ATM/near-OTM, short further OTM) as delta bets. Both need the underlying to finish around the short strike and time to pass.
  - A credit call spread and a debit put spread on the same strikes/expiry share the same risk profile. **An ITM call (put) spread is synthetically equal to an OTM put (call) spread**, after interest.
  - Under Reg T margin, a credit vertical requires the max loss to be deposited, so in cash terms every vertical is a debit. Portfolio margining is more liberal.
- **Building a box**: long call vertical + long put vertical on the same strikes (or long synthetic stock at K₁ + short synthetic at K₂). Greeks nearly cancel; value = PV(K₂ − K₁) (American models add an early-exercise component).

## Key Concepts
- **Vertical spread**: long and short options of the same type, underlying and expiry, differing only in strike.
- **Debit spread**: the more expensive option (the lower-strike call or the higher-strike put) is bought; net premium paid.
- **Credit spread**: the more expensive option is sold; net premium received and kept if both expire OTM.
- **Short strike**: the strike of the sold leg; the target price for the underlying at expiry for every vertical.
- **Effective price**: the stock price implied by assignment/exercise net of the spread premium (e.g., K₁ + D for a bull call).
- **Negative scalp**: a stock round trip bought high/sold low created by assignment and exercise at expiry (e.g., short at 395, buy back at 405).
- **Pure leveraged delta**: the state of a vertical when the underlying sits between strikes and non-delta Greeks net to ≈0.
- **Selling future realized volatility**: using a credit vertical at the short strike to collect theta against short gamma.
- **Cash deal**: a takeover paid in cash; the target pins just below the offer price and IV collapses.
- **Box**: bull (bear) call spread + bear (bull) put spread, same strikes and expiry; a riskless (interest-rate) position.
- **Regulation T margining**: retail margin regime requiring the vertical's max loss in cash.
- **Portfolio margining**: risk-based margin regime available to professionals/qualifying retail, more liberal.

## Formulas & Reference Tables
- Width: `W = K₂ − K₁`.
- Debit vertical: `Max loss = D`, `Max profit = W − D`. Credit vertical: `Max profit = C`, `Max loss = W − C`.
- Breakevens: `BE_bull call = K₁ + D`, `BE_bear call = K₁ + C`, `BE_bear put = K₂ − D`, `BE_bull put = K₂ − C`.
- Spread Greeks: `Δ_spread = Δ_long − Δ_short` (same for Γ, Θ, vega), each measured per share; multiply by 100 per contract.
- P&L from delta over a move: `P&L ≈ Δ̄ × ΔS × 100` using the average delta over the move.
- Box value (European): `Box = (K₂ − K₁) × e^(−rT)`; the author approximates with simple interest `W − W × r × T` (1-year, r = 1%: 2.50 − 0.025 = 2.475).
- Box legs: `Box = (C(K₁) − C(K₂)) + (P(K₂) − P(K₁))`.

## Mental Models
- **"Move to the short strike, then wait."** The whole vertical family needs direction (toward the short strike) plus time (decay of the short leg). Debit and credit spreads only differ in where the underlying starts.
- **Think of a vertical as a delta instrument with its option-specific risk filtered out.** Use it when you have a directional view with a price target (the short strike) and no strong vol view.
- **Credit spread = naked short option with a stop built in.** The income trader is really selling the short leg and buying the wing as protection.
- **Where the stock is, relative to the strikes, decides whether you are long or short volatility**, not whether you paid or received a credit. A credit call spread sold with both calls ITM is a long-gamma, long-vega trade.
- **Prefer the vertical over the outright when you expect a slow or limited move; prefer the outright when you expect a fast, large move.**

## Worked Example
**1. AAPL bull call spread vs outright call** (AAPL ≈ $391, 40 days): buy Feb 395 call at 14.60, sell Feb 405 call at 10.20 → debit 4.40.

| Greek (per share) | Long 395 call | 395 405 call spread | Spread / outright |
|---|---|---|---|
| Delta | +0.484 | +0.100 | ≈ 21% |
| Gamma | +0.0097 | +0.0001 | ≈ 1% |
| Theta | −0.208 | −0.014 | ≈ 7% |
| Vega | +0.513 | +0.020 | ≈ 4% |

Max profit 10 − 4.40 = 5.60; BE 399.40. Spread Greeks as the stock rises (reconstructed signs; pdftotext dropped the minus signs): at $395 Γ +0.0002, Θ −0.009, vega +0.010; at $400 all ≈ 0 (Δ 0.101); at $405 Γ −0.0002, Θ +0.004, vega −0.035, Δ 0.097.

| Scenario (AAPL → $405) | 395 call | Return | 395 405 spread | Return |
|---|---|---|---|---|
| At expiry | 10.00 | −31.5% | 10.00 | +127% |
| After ~2 weeks (4 weeks left) | 19.85 | +36% | 5.70 | +30% |

Interpretation: the outright wins on a fast move, the spread wins when the move takes the full time.

**2. XOM bear put spread, then the move comes early** (XOM $80.55, 40 days): buy June 80 put 1.75, sell June 75 put 0.45 → debit 1.30; max profit 5 − 1.30 = 3.70; BE 78.70.

| Greek | 80 put | 75 80 put spread | Ratio |
|---|---|---|---|
| Delta | −0.445 | −0.300 | ≈ 2/3 |
| Gamma | +0.080 | +0.041 | ≈ 1/2 |
| Theta | −0.018 | −0.006 | ≈ 1/3 |
| Vega | +0.110 | +0.046 | ≈ 42% |

Spread Greeks as XOM falls (signs reconstructed): at $80 Δ −0.321, Γ +0.037, Θ −0.004, vega +0.040; at $77 Δ −0.388 (peak), Γ ≈ 0, Θ ≈ 0; at $75 Δ −0.364, Γ −0.026, Θ +0.016, vega −0.038. If XOM drops $5 in one day, average delta ≈ −0.36 → profit ≈ 0.36 × 5 = 1.80 (**$180 per spread, +138% on 1.30**), still well short of the 3.70 max, which only theta can deliver by expiry. Decision: bank the gain (the trade is now short gamma/vega) or hold only if you now want a pin at $75.

**3. The box (JNJ at $63.35, 38 days)**: Sam buys the 62.50 65 call spread (1.84 − 0.56 = 1.28; Δ +0.290); Isabel buys the 62.50 65 put spread (2.19 − 0.97 = 1.22; Δ −0.273). Together: 1.28 + 1.22 = 2.50 = width; interest on 2.50 over 38 days at 1% ≈ 0.003 (under a penny). Held to expiry the combined P&L is zero in every region.

## Anti-patterns
- **Using a covered call or naked short put for a "neutral to moderately bullish" view**: it carries full downside stock risk that serves no purpose for the forecast. A vertical expresses it with capped risk.
- **Buying outright calls for a slow, limited move**: traders can be right on direction and still lose to theta. Timing is everything.
- **Holding a debit spread after the move to the short strike without re-underwriting it**: the position has flipped to short gamma/vega. Re-evaluate as if putting it on fresh.
- **Paying commissions to close a far-OTM long wing for 0.05**: after a big favorable move, buy back the short leg (kills negative delta/gamma) and keep the wing as a free lottery ticket. A stock that fell $70 can rally $70.
- **Treating credit spreads and debit spreads as different species**: same strikes → same risk profile via synthetics. Choose on price, liquidity and margin, not ideology.
- **Chasing call IV in takeover rumors**: IV is already bid. Use the ITM/OTM call spread to neutralize vega.

## Practitioner Notes
- Theta per contract = theta per share × 100: the 395 405 bear call spread's −0.009 (for the buyer) is about **$0.90 a day** of decay for the seller near $395, and it accelerates into expiry.
- Early exit for credit spreads: after a large favorable move (AAPL falls to $325 with the 395s at 0.50/0.55 and 405s at 0.05/0.10), close only the short leg.
- The bull-spread player gets a structural tailwind from the negative spot/vol correlation in equities, but pays for it via the put/call skew (lower strikes carry higher IV).
- Large, low-cost traders (market makers) can trade vertical vega profitably despite its small size; retail traders should treat vertical vega as a secondary effect and delta as the primary risk.
- For income selling near the short strike with 40 days left, theta starts tiny (0.004/day on the 75 80 XOM spread at $80) and accelerates only in the final weeks, so the income vertical is a patience trade.
- Rule of thumb for strike selection: the **short strike is your price target**; the long strike is where your conviction starts.

## Key Takeaways
1. A vertical keeps delta and removes most of theta, vega and gamma; the price is capped profit.
2. Greeks are dominated by the ATM strike: long vol at the long strike, pure delta between the strikes, short vol at the short strike.
3. Every vertical needs the underlying to finish at/through the short strike and needs time to realise its max value.
4. Fast, big move → outright option; slow or limited move → vertical.
5. When the underlying travels from one strike to the other, re-underwrite the trade from scratch.
6. Credit and debit verticals on the same strikes are synthetically identical; ITM call spread ≡ OTM put spread.
7. Call vertical + opposite put vertical = box worth PV(width); a box is an interest-rate trade, not a directional one.

## Connects To
- **ch04**: basic single-leg strategies (long call/put, naked options) that verticals improve upon.
- **ch05**: covered calls and cash-secured puts that verticals replace for trading forecasts.
- **ch06**: put-call parity, synthetics and the box/conversion family underlying credit/debit equivalence.
- **ch10**: wing spreads (butterflies, condors) built by combining verticals.
- **ch12–13**: delta-neutral hedging of vertical vega and gamma.
- **ch16**: ratio spreads, which are unbalanced verticals.
- **`hull-derivatives` ch12**: bull/bear spreads and box spreads, payoff formalism.
- **`hull-derivatives` ch19**: Greeks of each leg and how they aggregate.
- **`cfa-derivatives` ch05**: L3 options strategies (bull/bear spreads, collars) in a portfolio context.
