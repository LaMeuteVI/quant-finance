# Chapter 13: Binomial Trees

## Core Idea
In a binomial world, an option can be replicated by Δ shares plus borrowing, so its price follows from no-arbitrage alone. The same answer comes from **risk-neutral valuation**: expected payoff under probability p, discounted at r. Real-world probabilities never enter.

## Frameworks Introduced
- **One-step no-arbitrage portfolio**: long Δ shares, short 1 option. Choose `Δ = (f_u − f_d)/(S₀u − S₀d)` so the portfolio is riskless, then discount at r.
- **Risk-neutral valuation**:
  - `f = e^{−rΔt}[p·f_u + (1 − p)·f_d]` with `p = (e^{rΔt} − d)/(u − d)`.
  - The expected stock return under p is r.
- **Multi-step backward induction**: work from the final nodes back, one step at a time.
  - Two-step closed form: `f = e^{−2rΔt}[p²f_uu + 2p(1−p)f_ud + (1−p)²f_dd]`.
- **American options**: at each node, value = max(continuation value, intrinsic value).
- **Matching volatility (CRR)**: `u = e^{σ√Δt}`, `d = 1/u`, `p = (a − d)/(u − d)`.
  - a = e^{rΔt} for a non-dividend stock.
  - a = e^{(r−q)Δt} for an index with yield q.
  - a = e^{(r−r_f)Δt} for a currency.
  - a = 1 for futures.
- **Convergence**: as the number of steps increases, the tree converges to Black–Scholes–Merton (Ch 15). In practice 30+ steps are used, and 100+ for accuracy.

## Key Concepts
- **Delta (Δ)**: the ratio of the change in option price to the change in stock price. It changes node to node, which is why hedging is dynamic.
- **Risk-neutral world**: all assets earn r in expectation, and the discount rate is r.
- **Real-world vs risk-neutral**: under real-world p* the correct discount rate is unknown (it depends on the option's risk). The risk-neutral p avoids that problem.
- **Girsanov intuition**: changing the drift of S (μ → r) leaves σ unchanged. That is why volatility, not expected return, drives option prices.

## Mental Models
- Think "**replicate, then discount the riskless portfolio**". This is the root of all derivative pricing.
- **Expected return of the stock doesn't matter** for the option price given S₀. It is already embedded in S₀.
- For **American puts**, check early exercise at every node. Exercise tends to occur at low-S nodes when time is short.

## Anti-patterns
- **Discounting the real-world expected payoff at r**: this is wrong. Either use risk-neutral p with r, or real-world p* with a risk-adjusted (and unknown) rate.
- **Using too few steps** for American options near a boundary: the price oscillates and converges slowly.
- **Forgetting to change `a` for other underlyings** (q, r_f, futures).

## Code Examples
```python
import math
def crr(S, K, r, sigma, T, N, call=True, american=False, q=0.0):
    dt = T/N; u = math.exp(sigma*math.sqrt(dt)); d = 1/u
    p = (math.exp((r-q)*dt) - d)/(u - d); disc = math.exp(-r*dt)
    V = [max((S*u**j*d**(N-j) - K)*(1 if call else -1), 0) for j in range(N+1)]
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            cont = disc*(p*V[j+1] + (1-p)*V[j])
            ex = (S*u**j*d**(i-j) - K)*(1 if call else -1)
            V[j] = max(cont, ex) if american else cont
    return V[0]
# crr(50, 52, 0.05, 0.30, 2, 2, call=False, american=True) → ≈ 7.43 (Hull Fig 13.10)
```
- **What it demonstrates**: a CRR tree with early-exercise tests and support for dividend yield / FX / futures via q.

## Worked Example
**One step.** S₀ = 20 → 22 or 18 in 3 months. Call with K = 21, r = 4%.
- Δ = (1 − 0)/(22 − 18) = 0.25.
- p = (e^{0.04×0.25} − 0.9)/(1.1 − 0.9) = 0.5503.
- f = e^{−0.01}(0.5503 × 1) = **0.545**.

**Two-step American put.** S₀ = 50, K = 52, u = 1.2, d = 0.8, r = 5%, Δt = 1 → p = 0.6282.
- The European value is **4.1923**.
- American: at the low node (S = 40) the continuation value is 9.4636 < exercise value 12, so exercise early. The American value is e^{−0.05}(0.6282 × 1.4147 + 0.3718 × 12) = **5.0894**.
- With σ = 30% (u = 1.3499, d = 0.7408, p = 0.5097) the American put is worth **7.43**.

## Key Takeaways
1. Option price = discounted risk-neutral expected payoff. p = (a − d)/(u − d).
2. Delta hedging makes the portfolio riskless locally. Δ changes, so rebalance.
3. American options: take the max of continuation and exercise values at every node.
4. u = e^{σ√Δt}. Adapt a for dividends (q), currencies (r_f) and futures (a = 1).
5. Trees converge to BSM and remain the workhorse for American options.

## Connects To
- **Ch 11**: the early exercise logic proven by trees.
- **Ch 15**: the continuous-time limit (BSM).
- **Ch 19**: delta and gamma from tree nodes.
- **Ch 21**: trees in practice (control variates, dividends, trinomial trees).
- **Ch 28**: risk-neutral measures and martingales.
