# Chapter 28: Martingales and Measures

## Core Idea
Every traded derivative satisfies `(μ − r)/σ = λ`, the market price of risk of the underlying variable. Risk-neutral valuation generalizes to the **equivalent martingale measure** theorem: for any numeraire g, f/g is a martingale. Choosing the numeraire cleverly (money-market account, zero-coupon bond, annuity) simplifies stochastic-rate pricing and justifies Black's model for rates.

## Frameworks Introduced
- **Market price of risk λ**: for any derivative on θ, `μ_f − r = λσ_f`. With several variables, `μ − r = Σλᵢσᵢ`.
- **Risk-neutral world**: λ = 0. Other worlds use λ = σ_g, the volatility of the numeraire.
- **Martingale**: a zero-drift process, so E[θ_T] = θ₀.
- **Equivalent martingale measure**:
  - If f and g are traded securities and the world is "forward risk-neutral with respect to g", then `f₀ = g₀·E_g[f_T/g_T]`.
- **Numeraire choices**:
  - **Money-market account**: `f₀ = E[e^{−∫r dt}f_T]`. This is the traditional risk-neutral measure.
  - **Zero-coupon bond P(t,T)** (T-forward measure): `f₀ = P(0,T)·E_T[f_T]`. The forward price of any asset for maturity T is a martingale.
  - **Annuity A(t)** (swap measure): `f₀ = A(0)·E_A[f_T/A(T)]`. The forward swap rate is a martingale.
- **Black's model revisited (stochastic rates)**:
  - Under the T-forward measure, `c = P(0,T)[F₀N(d₁) − KN(d₂)]`.
  - F₀ is the *forward* price. σ is the volatility of the forward.
  - The model is exact if F_T is lognormal.
- **Exchange option via numeraire U**: `f₀ = U₀·E_U[max(V_T/U_T − 1, 0)]`. This gives Margrabe with σ² = σ_U² + σ_V² − 2ρσ_Uσ_V.
- **Change of numeraire (drift adjustment)**:
  - Switching from numeraire g to h increases the drift of a variable v by `ρσ_v(σ_h − σ_g)`.
  - This is the engine behind convexity, timing and quanto adjustments.

## Key Concepts
- **Numeraire**: the unit in which prices are measured.
- **Forward risk-neutral world**: the world defined by a zero-coupon bond numeraire.
- **Girsanov theorem**: changing measure changes drifts but not volatilities.
- **Traded vs non-traded variables**: only traded securities earn r in a risk-neutral world. For non-traded variables (interest rates, commodity consumption prices), λ must be estimated.

## Mental Models
- **Pick the numeraire that makes the payoff's underlying a martingale**:
  - bond option → T-forward measure,
  - caplet → forward measure of the payment date,
  - swaption → annuity measure.
- **λ is the "Sharpe ratio" of a source of risk.** Every derivative on that variable shares it.
- **Drifts change with measure; volatilities do not.** That is why implied volatilities transfer across measures.

## Anti-patterns
- **Using the risk-neutral drift of a non-traded variable as r**: it is r only for traded assets.
- **Discounting forward expectations taken under the wrong measure**: expectations under the T-forward measure must be discounted with P(0,T), not with the money-market account.
- **Mixing numeraires within one pricing formula**.

## Worked Example
**Market price of risk (Example 28.1).** A derivative linked to the oil price has expected return 12% and volatility 20%. r = 8%.
- λ_oil = (0.12 − 0.08)/0.20 = **0.2**.
- Any other oil derivative with volatility 30% must earn 8% + 0.2 × 30% = **14%**.
- Oil itself is a consumption asset, so λ cannot be computed from oil's own return.

**Why caplets use Black.** Under the measure defined by the zero-coupon bond maturing at payment date t_{k+1}, the forward rate F_k is a martingale. So:
- the expected payoff is computed with E[R_k] = F_k,
- the result is discounted with P(0, t_{k+1}),
- and assuming F_k is lognormal yields Black's caplet formula exactly.

## Key Takeaways
1. μ − r = λσ for every derivative on the same variable. λ = the market price of risk.
2. For any numeraire g: f₀ = g₀ E_g[f_T/g_T].
3. T-forward measure: forward prices are martingales. Discount with P(0,T).
4. Annuity measure: forward swap rates are martingales, which gives the swaption Black model.
5. A change of numeraire shifts drifts by ρσ_v(σ_h − σ_g). This is the source of convexity and quanto adjustments.

## Connects To
- **Ch 13 / Ch 15**: basic risk-neutral valuation.
- **Ch 26**: exchange options.
- **Ch 29**: standard market models for bond options, caps and swaptions.
- **Ch 30**: convexity, timing and quanto adjustments.
- **Ch 33**: LMM measures.
