# Chapter 19: The Greek Letters

## Core Idea
Dealers manage option books by neutralizing sensitivities: delta daily (with the underlying), gamma and vega occasionally (with traded options), and monitor theta and rho. The cost of delta hedging converges to the BSM price as rebalancing becomes frequent.

## Frameworks Introduced
- **Naked / covered / stop-loss**: all are poor hedges. The stop-loss strategy fails because of transaction costs and because you cannot buy or sell exactly at K.
- **Greeks (European call, no dividends)**:
  - Δ = N(d₁). A put has Δ = N(d₁) − 1.
  - Γ = N′(d₁)/(S₀σ√T). It is the same for calls and puts.
  - Vega = S₀√T·N′(d₁). It is the same for calls and puts.
  - Θ_call = −S₀N′(d₁)σ/(2√T) − rKe^{−rT}N(d₂).
  - ρ_call = KTe^{−rT}N(d₂) and ρ_put = −KTe^{−rT}N(−d₂).
  - With yield q: multiply the S terms by e^{−qT}, Δ_call = e^{−qT}N(d₁), and add a qS term to theta.
- **Delta hedging**: hold −Δ units of the underlying per long option. Rebalance as Δ drifts. The hedge cost ≈ the BSM price, and the error shrinks as rebalancing frequency increases.
- **Gamma-neutral then delta-neutral**:
  1. Neutralize gamma with a traded option: w_T = −Γ/Γ_T.
  2. Re-neutralize delta with the underlying.
- **Gamma + vega neutral**: this needs **two traded options**. Solve the 2×2 linear system, then fix delta with the underlying.
- **BSM identity**: `Θ + rSΔ + ½σ²S²Γ = rΠ`. For a delta-neutral book, Θ + ½σ²S²Γ = rΠ, so **positive gamma ⇒ negative theta**.
- **Taylor expansion**: `ΔΠ ≈ ΘΔt + ½Γ(ΔS)² + Vega·Δσ` for a delta-neutral portfolio.
- **Portfolio insurance**: create a synthetic put by trading stock and bonds or index futures (dynamic hedging).
  - With futures: short `e^{−qT}e^{−(r−q)T*}[1 − N(d₁)]·A/A_F` contracts.
  - It failed on 19 Oct 1987, when the market gapped and liquidity vanished.

## Key Concepts
- **Delta of the underlying** = 1. **Delta of a forward** = e^{−qT}. **Delta of futures** = e^{(r−q)T}.
- **Scenario analysis**: a grid of P&L across S and σ. It captures non-linearities the Greeks miss.
- **Realities of hedging**: rebalance delta daily. Gamma and vega are hard to hedge, so they are monitored with limits. Bid–ask costs dominate for small books.
- **Machine learning (deep hedging)**: learn a hedging policy that minimizes a risk measure, including transaction costs.

## Mental Models
- **Long gamma = rent paid in theta** in exchange for profits from large moves. Short gamma = collect theta, lose on big moves.
- **ATM, short-dated options have the highest gamma**. Long-dated options have the highest vega.
- **Delta-hedging P&L ≈ ½Γ S²(σ²_realized − σ²_implied)Δt**. You profit when realized volatility beats implied (long gamma).

## Anti-patterns
- **Relying on stop-loss "covered when ITM" hedging**: it is path dependent and leaks cost at every crossing of K.
- **Hedging gamma with the underlying**: it has zero gamma, so you need options.
- **Assuming dynamic hedging works in gaps**: 1987 portfolio insurance, jumps and illiquidity.

## Reference Tables
| Greek | Call (no div) | Put (no div) | Sign intuition |
|---|---|---|---|
| Δ | N(d₁) | N(d₁) − 1 | call + / put − |
| Γ | N′(d₁)/(Sσ√T) | same | long option + |
| Vega | S√T N′(d₁) | same | long option + |
| Θ | −SN′(d₁)σ/(2√T) − rKe^{−rT}N(d₂) | −SN′(d₁)σ/(2√T) + rKe^{−rT}N(−d₂) | usually − |
| ρ | KTe^{−rT}N(d₂) | −KTe^{−rT}N(−d₂) | call + / put − |

## Worked Example
**The bank's 100,000-call book (Examples 19.1–19.6).** S₀ = 49, K = 50, r = 5%, σ = 20%, T = 20 weeks (0.3846). The bank sold the calls for $300,000. The BSM value is ≈ $240,000 ($2.40 each).
- **Δ = 0.522** → the position delta is −52,200, so buy 52,200 shares to hedge.
- **Γ = 0.066** per option. **Vega = 12.1** per option: +1 vol pt ⇒ +$0.121.
- **Θ ≈ −4.31/yr** per option: about −$0.0118/calendar day.
- **Gamma/vega neutralization.** A delta-neutral book has Γ = −5,000 and vega = −8,000. Traded option 1 has (Δ, Γ, vega) = (0.6, 0.5, 2.0) and option 2 has (0.5, 0.8, 1.2).
  - Solve −5,000 + 0.5w₁ + 0.8w₂ = 0 and −8,000 + 2w₁ + 1.2w₂ = 0 → **w₁ = 400, w₂ = 6,000**.
  - The new delta is 0.6 × 400 + 0.5 × 6,000 = 3,240, so sell 3,240 units of the underlying.

## Key Takeaways
1. Delta-hedge daily. The cost of hedging converges to the theoretical option value.
2. Gamma and vega require traded options. Two instruments are needed to hit both.
3. Θ + ½σ²S²Γ = rΠ for delta-neutral books: theta and gamma are two sides of one trade.
4. Use scenario grids (S × σ) for non-linear books, not only Greeks.
5. Dynamic replication breaks in gaps and illiquidity (1987).

## Connects To
- **Ch 15**: BSM formulas behind the Greeks.
- **Ch 20**: vega by bucket and sticky-strike vs sticky-delta.
- **Ch 21**: Greeks from trees and Monte Carlo (finite differences, pathwise).
- **Ch 22**: delta–gamma VaR.
- **Ch 26**: Greeks of exotics (discontinuous barrier deltas).
