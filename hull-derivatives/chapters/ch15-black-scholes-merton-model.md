# Chapter 15: The Black–Scholes–Merton Model

## Core Idea
With GBM stock prices, a portfolio of the option and Δ shares is instantaneously riskless, so it must earn r. This yields the BSM PDE, in which μ is absent, and the closed-form prices of European calls and puts. Traders quote *implied* volatility rather than price.

## Frameworks Introduced
- **Lognormal property**: `ln S_T ~ N(ln S₀ + (μ − σ²/2)T, σ²T)`. The continuously compounded return x ~ N(μ − σ²/2, σ²/T).
- **Volatility estimation**:
  - `u_i = ln(S_i/S_{i−1})` and σ̂ = stdev(u)/√τ, where τ is the interval length in years.
  - Count **trading days** (≈252/yr). Volatility is mostly caused by trading itself, not by calendar time.
- **BSM PDE**: `∂f/∂t + rS∂f/∂S + ½σ²S²∂²f/∂S² = rf`.
- **BSM formulas**:
  - `c = S₀N(d₁) − Ke^{−rT}N(d₂)`.
  - `p = Ke^{−rT}N(−d₂) − S₀N(−d₁)`.
  - `d₁ = [ln(S₀/K) + (r + σ²/2)T]/(σ√T)` and `d₂ = d₁ − σ√T`.
  - N(d₂) = the risk-neutral probability of exercise. S₀N(d₁)e^{rT} = the expected value of S_T·1{S_T > K} under risk-neutrality.
- **Risk-neutral valuation**: set μ = r, take the expected payoff and discount at r.
- **Dividends**:
  - European: replace S₀ by S₀ − PV(dividends).
  - American calls: **Black's approximation** = max(European to T, European to just before the final ex-dividend date).
  - Early exercise is optimal only just before an ex-dividend date, and only if `D_n > K[1 − e^{−r(T−t_n)}]`.
- **Warrants / ESOs with dilution**: value = N/(N + M) × a BSM call on the adjusted stock price (N shares, M warrants).

## Key Concepts
- **Implied volatility**: the σ that equates the BSM price to the market price. It is found by iteration (Newton–Raphson or bisection).
- **VIX**: a model-free 30-day implied volatility index on the S&P 500 (from a strip of options).
- **Expected return trap**: arithmetic vs geometric means differ by σ²/2. Mutual fund "average returns" can mislead.
- **Trading-day convention**: T is measured in trading days / 252 for volatility purposes.

## Mental Models
- **The option price doesn't depend on μ**, because μ is already embedded in S₀ and the riskless hedge removes it.
- Read **BSM as**: (PV of the stock received if exercised) − (PV of the strike paid × probability of exercise).
- **Implied volatility is the market's price language**: quote options in σ, not in dollars.

## Anti-patterns
- **Using calendar days for historical volatility** without adjusting. Returns over weekends are not three times as volatile.
- **Forgetting dividends**: overstates calls and understates puts.
- **Treating BSM σ as constant across strikes**: see the smile (Ch 20).

## Code Examples
```python
from math import log, sqrt, exp, erf
N = lambda x: 0.5*(1+erf(x/sqrt(2)))
def bsm(S, K, r, sigma, T, q=0.0):
    d1 = (log(S/K)+(r-q+0.5*sigma**2)*T)/(sigma*sqrt(T)); d2 = d1 - sigma*sqrt(T)
    c = S*exp(-q*T)*N(d1) - K*exp(-r*T)*N(d2)
    p = K*exp(-r*T)*N(-d2) - S*exp(-q*T)*N(-d1)
    return c, p
def implied_vol(price, S, K, r, T, q=0.0, call=True, lo=1e-4, hi=5.0):
    for _ in range(100):
        mid = (lo+hi)/2; v = bsm(S,K,r,mid,T,q)[0 if call else 1]
        lo, hi = (mid, hi) if v < price else (lo, mid)
    return mid
# bsm(42, 40, 0.10, 0.20, 0.5) → (4.76, 0.81)
```

## Worked Example
**Example 15.6.** S₀ = 42, K = 40, r = 10%, σ = 20%, T = 0.5.
- d₁ = 0.7693 and d₂ = 0.6278. Ke^{−rT} = 38.049.
- c = 42N(0.7693) − 38.049N(0.6278) = **4.76**.
- p = 38.049N(−0.6278) − 42N(−0.7693) = **0.81**.
- The stock must rise by 2.76 for the call buyer to break even.

## Key Takeaways
1. BSM: c = S₀N(d₁) − Ke^{−rT}N(d₂). Parity gives p.
2. μ does not enter. Price in a risk-neutral world and discount at r.
3. Estimate σ from log-returns over trading days, and annualize with √(252).
4. Dividends: use S₀ − PV(D). American calls use Black's approximation.
5. Traders quote implied volatility. Deviations across K and T form the smile or surface.

## Connects To
- **Ch 13**: trees converge to BSM.
- **Ch 14**: Itô's lemma is used in the derivation.
- **Ch 17–18**: extensions for q, r_f and futures (Black).
- **Ch 19**: Greeks are BSM derivatives.
- **Ch 20**: smiles, as departures from BSM.
- **Ch 27**: alternative models.
