# Chapter 13: Forwards and Futures: Preliminaries
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 13 · Part Four, Selected Securities and Topics

## Core Idea
A bond forward is a spot purchase financed in repo. The forward price is the future value of the full spot price less the future value of the coupons received before delivery. So `spot − forward` (the **forward drop**) equals **carry**: coupon income minus financing cost. Futures differ from forwards only by **daily settlement**. Under the risk-neutral measure a futures price is the *expected* terminal price, while a forward price is the *expected discounted* price divided by the discount factor. Because bond prices are high when rates are low, futures < forward. The **futures-forward difference** is negligible for 3-month bond futures, but for rate futures (Eurodollars) it grows with the square of maturity and adds to a Jensen **convexity effect**, so futures rates are above forward rates.

## Frameworks Introduced
- **Arbitrage forward price (cash-and-carry replication)**:
  - When to use: pricing any bond forward, TBA-like forward settlement, or the fair value of a futures before delivery options (ch14).
  - How: buy spot and sell the repo to the forward date, borrowing the full price. Accrue the loan at repo. Use any interim coupon to pay down the loan. At delivery, repay the loan and take back the bond. The repayment amount is the full forward price, and every quantity is known today.
  - Why it works: two strategies deliver the bond on the same date with no other cash flows, so they must cost the same. Failure mode: the repo rate used must be the *bond's own* term repo rate. If the bond trades special (ch12), using GC overprices the forward.
- **Forward drop = carry**:
  - When to use: explaining why forward < spot, and quoting carry on a basis or curve trade.
  - How: `p₀ − p₀(d) ≈ coupon accrual − financing cost = κ(d)`.
  - Why: with an upward-sloping curve, coupon rates exceed short repo rates, so spot holders earn positive carry and the forward must be cheaper. With an inverted curve the forward can exceed spot.
- **Forward swap rate by discounting**:
  - When to use: forward-starting swaps ("1yr2yr", "1×2", "1- into 2-year"), swaption underlyings.
  - How: set the PV of the forward fixed leg plus notional to par at the start date: `1 = [C/2 × Σ d(t+.5…t+T) + d(t+T)]/d(t)`.
  - Why it works: swaps exist in unlimited supply, so only cash flows matter and pure discounting prices them exactly.
- **Choosing the DV01 of a forward (spot vs forward yield shift)**:
  - Spot DV01 = forward DV01 + repo DV01. It assumes the repo rate moves 1:1 with long yields.
  - Forward DV01 assumes the repo rate is fixed.
  - Blended DV01 = forward DV01 + β × repo DV01, with β the fraction of the long-yield move passed through to repo (e.g. 40%).
  - **Best practice (two-factor)**: hedge the forward-yield exposure with the liquid 10-year bond and hedge the repo exposure separately with short-rate futures (ch15). Don't hedge overnight-rate risk with 10-year bonds.
- **Futures pricing in a term-structure model**:
  - `P₀ = E[Pₙ / Π(1 + rᵢ)]` (expected discounted value).
  - `d(n) = E[1/Π(1 + rᵢ)]`.
  - Forward = `P₀/d(n)`.
  - Futures `F₀ = E[Pₙ]`, from zero value after each daily settlement at every node.
  - **Futures-forward difference**: `F₀ = P₀(n) − Cov(Pₙ, 1/Π(1 + rᵢ)) / d(n)`.
- **Tailing the hedge**:
  - When to use: hedging a forward (basis trade, forward loan) with futures.
  - How: `N_fut = N_fwd / (1 + r·d/360)`. A futures gain arrives today while a forward gain arrives at delivery, so fewer futures are needed. Re-tail as d shrinks.

## Key Concepts
- **Forward contract**: agreement fixing today the price for settlement at a future date. It is worth 0 at inception. **Long** = buyer, **short** = seller. Also called the forward/delivery/expiration date.
- **Forward price vs forward contract value**: the price at which a *new* contract is struck at zero value, vs the mark-to-market of an *existing* contract.
- **Forward drop**: spot price minus forward price. It is usually positive because coupons exceed repo rates.
- **Carry (cash carry)**: coupon interest minus financing cost over the holding period. In bond forwards and futures, forward drop = carry.
- **Forward yield**: the single yield that discounts cash flows *after* the forward date back to the full forward price.
- **Forward (par) swap rate C(t, t+T)**: the fixed rate making a T-year swap starting at t worth par (zero NPV).
- **Daily settlement**: futures P&L is paid irrevocably each day and the contract is re-struck at the new settlement price. Contract value after settlement is 0.
- **Mark-to-market (strict sense)**: an accounting revaluation. It implies no cash exchange.
- **Variation margin (strict sense)**: an adjustment to collateral that is returnable and bears interest. Futures settlement payments are *not* collateral, even though they are often called variation margin.
- **Futures-forward effect (pure)**: futures < forward because settlement gains are reinvested at low rates and losses financed at high rates.
- **Convexity effect (rate futures)**: `E[1/(1+L/4)] > 1/(1 + E[L]/4)`. A future on a rate is not a future on a price.
- **Total futures-forward difference**: futures rate minus forward rate, the sum of both effects. It is always positive.
- **Tail**: `N_fwd − N_fut`, the reduction in futures needed because of daily settlement.

## Formulas & Reference Tables
Notation:
- p₀ = flat spot price for settlement at date 0, P₀ = full spot price = p₀ + AI(0).
- c = annual coupon rate (so 100c/2 is the semiannual coupon).
- r = term repo rate. d₁ = days from spot to the coupon date, d₂ = days from the coupon to delivery, d = d₁ + d₂.
- AI(·) = accrued interest function.

- Forward flat price (one interim coupon): `p₀(d) = [p₀ + AI(0)](1 + r·d₁/360) − 100c/2 − AI(d)`, compounded forward: `{[P₀(1 + r·d₁/360) − 100c/2](1 + r·d₂/360)} − AI(d)`.
- Full forward price: `P₀(d) = [P₀ − (100c/2)/(1 + r·d₁/360)] × (1 + r·d₁/360)(1 + r·d₂/360)`. Dropping interest-on-interest gives `P₀(d) ≈ [P₀ − (100c/2)/(1 + r·d₁/360)] × (1 + r·d/360)`. In words: the future value of the full spot price less the PV of the interim coupon. Several coupons: subtract the PV of each coupon. No coupon: `P₀(d) = P₀(1 + rd/360)`. At delivery d = 0, so forward = spot.
- Value of an existing long forward struck at P: `V = [P₀(d) − P]/(1 + rd/360)`.
- Carry: `κ(d) ≡ p₀ − p₀(d) ≈ 100c/2 + AI(d) − AI(0) − [p₀ + AI(0)]·r·d/360`.
- Forward swap price: `P(t, t+T; c) = {c/2 × [d(t+.5) + … + d(t+T)] + d(t+T)}/d(t)`. The par rate solves P = 1: `C(t, t+T) = 2[d(t) − d(t+T)]/Σ d(t+.5…t+T)`.
- Repo DV01 (short zero): ≈ `P × (d/360)/100` per 100.
- In a model: forward = `P₀/d(n)`, futures `F₀ = E[Pₙ]`, `F₀ = P₀(n) − Cov(Pₙ, 1/Π(1 + rᵢ))/d(n)`. Bond futures: Cov > 0, so `F₀ < P₀(n)`.
- Rough bond futures-forward size: `Cov ≈ σ_P × σ_disc × ρ`, with `σ_P = DV01 × σ_bp × √t` and `σ_disc = DV01_disc × σ_bp × √t`.
- Eurodollar-type rate futures: `F^R = 100 − 100L`, futures rate `r_fut = E[Lₙ]`. `1/(1 + 90r_fwd/360) = P₀(n) > F₀ > 1/(1 + 90r_fut/360)`, so `r_fut > r_fwd`.
- Normal model (drift λ, bp vol σ, t = expiry, β = deposit tenor, continuous compounding): `r_fut − r_fwd = σ²t²/2 + σ²βt/2`.
- Tail: `N_fut = N_fwd/(1 + rd/360)`.

**Table 13.2: total futures-forward difference, 3-month deposit (β = .25), σ = 100bp/yr**
| Expiry (yrs) | 0.25 | 0.5 | 1 | 2 | 5 | 10 |
|---|---|---|---|---|---|---|
| r_fut − r_fwd (bp) | 0.06 | 0.19 | 0.63 | 2.25 | 13.13 | 51.25 |

The difference scales with σ² and roughly with t². It is negligible in the first year and material beyond about 3 years. Scale the table by (σ/100bp)².

## Mental Models
- **Forward = spot + financing − coupons.** Every bond forward, futures fair value and implied repo calculation (ch14) is this identity rearranged.
- **Futures price = risk-neutral expectation; forward price = expectation under the delivery-date forward measure.** The gap is the covariance between the underlying and the realized discount factor over the life of the contract.
- **Daily settlement is a reinvestment bet you are forced into.** For bond futures, gains arrive when rates fall and are reinvested at low rates; losses arrive when rates rise and are financed at high rates. A long futures position is worse off than a long forward, so its price must be lower.
- **Rate futures double-penalize the long-price side.** Daily settlement plus Jensen's inequality both push the futures rate above the forward rate. Always convexity-adjust Eurodollar/SOFR strip rates before using them as forwards.
- **Separate the forward-yield risk from the repo risk.** A forward is a long bond plus a short repo. Hedge each leg with the instrument that matches its tenor.

## Worked Example
**1. Forward price of the UST 3⅝s of Aug 15, 2019 (trade May 28, 2010, spot settle Jun 1; delivery Sep 30, 2010 = 121 days; repo 0.30%).**
- Full spot = 102.8125 + 1.0615 = 103.8740, borrowed in repo.
- Aug 15 (75 days): loan = 103.8740 × (1 + 0.003 × 75/360) = 103.9389. Less the coupon 1.8125 gives 102.1264.
- Sep 30 (46 days): 102.1264 × (1 + 0.003 × 46/360) = **102.1656 full**. Less AI(Sep 30) = 0.4531 gives a **flat forward of 101.7125** (book: 101.7124).
- Forward drop = 102.8125 − 101.7125 ≈ 1.10 = carry: about 121 days of 3⅝% coupon vs 0.30% financing.
- Forward yield: solve 102.1656 = PV at y of the remaining cash flows (18 coupons, first one 138/184 of a period away), giving **y_fwd = 3.399%**. The spot yield is 3.268%.
- If the spot price jumps to 103.00, the new forward = 101.9002. The existing long gains 0.1878 at delivery, worth 0.1878/(1 + 0.003 × 121/360) = **0.1875** today.

**2. Which DV01 for the forward?**
- Forward DV01 (bump y_fwd 1bp) = 102.2424 − 102.1655 = **0.0769**.
- Spot DV01 (bump the spot yield 3.268% by 1bp) = **0.0803**.
- The difference, 0.0034, is the repo DV01 ≈ 100 × (121/360)/100.
- Blended (repo moves 40% of the long yield): 0.0769 + 0.4 × 0.0034 = **0.0783**.

**3. Forward par swap rate C(1, 2.5) (USD, May 28, 2010; Table 2.1 discount factors d(1) = .991306, d(1.5) = .984494, d(2) = .975616, d(2.5) = .964519).**
- C = 2 × (0.991306 − 0.964519)/(0.984494 + 0.975616 + 0.964519) = **1.832%**.

**4. Futures < forward on a 2-period tree** (illustrative: r₀ = 5%, r₁ᵤ = 6%, r₁d = 4%, p(up) = .6 then .5; date-2 prices 95/97/99).
- P₀ = 87.6495 and d(2) = 0.905384, so forward = **96.809**.
- Futures = 0.3 × 95 + 0.5 × 97 + 0.2 × 99 = **96.800**.
- Futures < forward by 0.9 cents, because low prices coincide with high rates.

**5. Size of the bond futures-forward difference (book's back-of-envelope).**
- Inputs: DV01 0.08, σ = 100bp, 3 months, ρ = 1.
- σ_price = 0.08 × 100 × 0.5 = 4. σ_disc = 0.0025% × 100 × 0.5 = 0.125%. Cov = 0.005.
- That is about ½ cent per 100, or **1/16 bp**, which is negligible.

**6. Tail.** Hedging 1,000 forwards 121 days out at 0.30% needs 1,000/1.001008 ≈ **999 futures**. At 4% for one year it would be ≈ 962.

## Anti-patterns
- **Pricing a forward with GC when the bond is special**: the forward is too low (more financing cost is subtracted), which misprices basis trades.
- **Confusing forward price with forward contract value**: the price is where a new trade prints. The value is the discounted difference between the market forward and the contract price.
- **Hedging a bond forward's repo exposure with 10-year bonds**: use short-rate futures (ch15) for the repo leg.
- **Using spot DV01 for a forward by default**: it assumes the repo rate moves 1:1 with long yields, which overstates the hedge.
- **Reading Eurodollar futures rates as forward rates**: the rates are biased upward by the total futures-forward difference (about 13bp at 5 years and 51bp at 10 years with 100bp vol).
- **Calling futures settlement "margin" and treating it as collateral**: settlement payments are irrevocable P&L with no interest paid on them. Margin is returnable, interest-bearing collateral.
- **Forgetting to tail a futures hedge of a forward**: small at low rates or short horizons, but it compounds on large notionals and long dates.

## Practitioner Notes
- Almost every "spot" bond trade actually settles T+1/T+2, so strictly it is a forward. Discount factors from regular-settlement prices are defined as spot by convention.
- Explicit bond forwards are rare, but **spot + repo = synthetic forward** is ubiquitous, and futures (ch14, ch15) are best understood as variants of forwards. Options on bonds are often modelled as options on the forward.
- In swaps, forward-starting trades are standard ("1yr2yr" / "1×2"). Because swaps are created on demand there is no "3-year swap for settlement in 1 year" language.
- For the actively traded bond futures (0–4 months to delivery) the futures-forward difference is a fraction of a basis point, so treat futures fair value = forward price adjusted for delivery options (ch14).
- The futures-forward effect is outside the fixed income logic for commodities such as oil: the sign of Cov(price, discount factor) is not obvious there.
- Counterparty-risk differences between OTC forwards and CCP-cleared futures are real but separate from daily settlement. The book treats them with swaps (ch16).

## Key Takeaways
1. Full forward price = FV of the full spot price at repo − FV of interim coupons. With no coupon, `P₀(d) = P₀(1 + rd/360)`.
2. Forward drop = carry = coupon income − financing cost. It is positive on an upward-sloping curve.
3. Forward swap rates follow from discount factors alone: `C(t, t+T) = 2[d(t) − d(t+T)]/Σd`.
4. Spot DV01 = forward DV01 + repo DV01. Hedge the two risks separately (long bond for the forward yield, short-rate futures for repo).
5. Futures = E[Pₙ] under risk-neutral pricing, forward = E[discounted Pₙ]/d(n). For bonds, futures < forward, but by only about 1/16bp for 3-month contracts.
6. For rate futures, the futures rate is above the forward rate: `r_fut − r_fwd = σ²t²/2 + σ²βt/2` in a normal model. Convexity-adjust long-dated strips.
7. Tail futures hedges of forwards: `N_fut = N_fwd/(1 + rd/360)`.

## Connects To
- **ch01 / ch02**: discount factors and the forward-rate logic used for forward swap rates. Table 2.1 data.
- **ch03**: carry and the return decomposition (expression 3.36). Yield conventions (Appendix A) used for forward yields.
- **ch04**: the DV01 of a short zero, used for repo DV01.
- **ch07–ch09**: risk-neutral trees and Jensen/convexity, which underpin `F₀ = E[Pₙ]` and the convexity effect.
- **ch12**: the repo rate (GC vs special) that goes into every forward price.
- **ch14**: bond futures, where forward price + delivery options gives the futures price and the implied repo rate reverses the forward formula.
- **ch15**: Eurodollar/SOFR futures, where the futures-forward convexity difference applies. Hedging repo risk with fed funds/ED futures.
- **ch16**: forward swaps and counterparty risk of forwards vs futures.
- **`hull-derivatives` ch05**: cost-of-carry forward pricing and the forward vs futures argument.
- **`hull-derivatives` ch06**: Eurodollar convexity adjustment and duration-based futures hedging.
- **`hull-derivatives` ch30**: convexity and timing adjustments.
- **`cfa-derivatives` ch03**: carry-arbitrage pricing and valuation of forwards, futures and swaps.
