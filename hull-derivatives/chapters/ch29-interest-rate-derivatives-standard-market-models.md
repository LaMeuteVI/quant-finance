# Chapter 29: Interest Rate Derivatives: The Standard Market Models

## Core Idea
European bond options, caps/floors and swaptions are priced with versions of Black's model. Each assumes a different variable is lognormal:
- the forward bond price (bond options),
- each forward rate (caplets),
- the forward swap rate (swaptions).

The models are mutually inconsistent but market-standard. More general term-structure models are needed for American or path-dependent products.

## Frameworks Introduced
- **European bond option (Black)**: `c = P(0,T)[F_B N(d₁) − KN(d₂)]`.
  - Forward bond price: `F_B = (B₀ − I)/P(0,T)`, where I is the PV of coupons paid during the option's life.
  - σ_B is the volatility of the forward bond price.
  - Yield volatility converts to price volatility via `σ_B ≈ D·y₀·σ_y`.
  - Watch whether the strike is a **cash** or a **quoted** price (accrued interest).
- **Caps and floors**:
  - A cap is a portfolio of caplets. A caplet pays `L·δ_k·max(R_k − R_K, 0)` at t_{k+1}.
  - Each caplet is priced as `L·δ_k·P(0,t_{k+1})[F_k N(d₁) − R_K N(d₂)]`, with σ_k the volatility of F_k.
  - A floor is a portfolio of floorlets.
  - **Cap − floor = swap** (pay fixed R_K): put–call parity for caps.
  - A collar = long cap + short floor.
  - A caplet is equivalent to a put on a zero-coupon bond.
- **Quotes**:
  - **Flat volatilities**: one volatility for all caplets of a given cap.
  - **Spot volatilities**: a volatility per caplet.
  - The volatility **hump**: spot volatilities peak around 2–3 years.
- **Post-LIBOR caps**: they are based on backward-looking compounded SOFR, so the accrual period is part of the option's life. The Black model is adjusted accordingly.
- **European swaption (Black)**:
  - Payer swaption: `L·A·[s_F N(d₁) − s_K N(d₂)]`.
  - Annuity: `A = (1/m)ΣP(0, T_i)`.
  - s_F is the forward swap rate, with volatility σ.
  - A receiver swaption is the equivalent put.
- **Swaptions as bond options**: a payer swaption = a put on a coupon bond (coupon s_K) with strike = par.
- **Volatility cube**: swaption volatility by (option expiry, swap tenor, strike).
- **Hedging**:
  - **Delta**: bump zero-curve buckets or instruments (partial durations), or use PCA factors.
  - **Vega**: bump volatilities by bucket.

## Key Concepts
- **Caplet / floorlet**, **reset date / payment date**, **tenor δ**.
- **Payer vs receiver swaption**: the right to pay fixed vs to receive fixed.
- **Forward swap rate**: `s_F = [P(0,T₀) − P(0,T_n)]/A`.
- **Normal (Bachelier) model**: used when rates are low or negative. Lognormal models fail at r ≤ 0.

## Mental Models
- **Black for rates = discount the forward-measure expectation.** The rate or price is lognormal under the right numeraire (Ch 28).
- **A cap hedges a floating-rate borrower against rising rates; a floor protects a floating-rate lender.**
- **Swaptions price correlation between forward rates; caps don't.** A cap is a sum of independent caplets.

## Anti-patterns
- **Quoting a cap with spot volatilities and then pricing it with flat volatilities** (or vice versa).
- **Applying lognormal Black when rates are near zero or negative**: use the normal model or shifted-lognormal Black.
- **Valuing Bermudan swaptions with Black**: they need a term-structure model.

## Worked Example
**Caplet (Example 29.3).**
- Contract: cap $10m at 8% (quarterly compounding) for 3 months starting in 1 year.
- Inputs: F = 7%, σ = 20%, flat zero rate 6.5%, so P(0, 1.25) = 0.9220.
- d₁ = [ln(0.07/0.08) + 0.02 × 1]/(0.20 × 1) = −0.5677 and d₂ = −0.7677.
- Caplet = 0.25 × 10 × 0.9220 × [0.07N(−0.5677) − 0.08N(−0.7677)] = **$0.00519m ≈ $5,190**.

**Payer swaption (Example 29.4).**
- Contract: right to pay 6.2% on a 3-year semiannual swap starting in 5 years, $100m notional.
- Inputs: flat zero rate 6%, forward swap rate 6.194% (s.a.), σ = 20%.
- A = ½ × Σ e^{−0.06t} for t = 5.5…8, which gives 2.0035.
- d₁ = 0.2214 and d₂ = −0.2258.
- Value = 100 × 2.0035 × [0.06194N(0.2214) − 0.062N(−0.2258)] = **$2.19m**.

**Bond option (Example 29.1).**
- Contract: 10-month call on a 9.75-year 10% bond. B₀ = 960 (cash price), K = 1,000.
- PV of coupons = 95.45, so F_B = (960 − 95.45)e^{0.1 × 0.8333} = 939.68.
- With σ_B = 9% and a cash strike, the call is worth **$9.49**.

## Key Takeaways
1. Bond option, caplet and swaption are all Black-type formulas, each lognormal in a different variable.
2. Cap − floor = swap. A caplet = a put on a zero-coupon bond.
3. The swaption formula uses the annuity A as the discount factor and s_F as the forward.
4. Know whether volatilities are flat or spot, and lognormal or normal.
5. Hedge by bucketed delta and vega (partial durations, PCA).

## Connects To
- **Ch 18**: Black's model.
- **Ch 28**: numeraires justify each model.
- **Ch 30**: payoffs where the "forward = expected" assumption fails.
- **Ch 31–33**: short-rate and LMM models for American and path-dependent products.
- **Ch 34**: nonstandard swaps.
