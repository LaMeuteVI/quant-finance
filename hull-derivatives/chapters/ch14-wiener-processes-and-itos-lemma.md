# Chapter 14: Wiener Processes and Itô's Lemma

## Core Idea
Stock prices are modeled as Markov processes driven by a Wiener process. Geometric Brownian motion (GBM) gives lognormal prices, and Itô's lemma gives the process followed by any function of S. Because the derivative and the stock share the same dz, they can hedge each other.

## Frameworks Introduced
- **Markov property**: only the current value matters for predicting the future. This is consistent with weak-form market efficiency.
- **Wiener process dz**: `Δz = ε√Δt`, ε ~ N(0,1), with independent increments. Over T, z(T) − z(0) ~ N(0, T). Variance adds and standard deviation scales with √T.
- **Generalized Wiener process**: `dx = a dt + b dz`. Over T, x ~ N(x₀ + aT, b²T).
- **Itô process**: `dx = a(x,t)dt + b(x,t)dz`.
- **GBM for stocks**: `dS = μS dt + σS dz`. The return over Δt is `ΔS/S ~ N(μΔt, σ²Δt)`.
- **Itô's lemma**: for G(S,t),
  `dG = (∂G/∂S·μS + ∂G/∂t + ½·∂²G/∂S²·σ²S²)dt + ∂G/∂S·σS dz`.
- **Applications**:
  - Forward price F = Se^{r(T−t)} gives `dF = (μ − r)F dt + σF dz`.
  - ln S gives `d ln S = (μ − σ²/2)dt + σ dz`.
  - So `ln S_T ~ N(ln S₀ + (μ − σ²/2)T, σ²T)`, which makes S_T lognormal.
- **Correlated processes**: `ε₂ = ρε₁ + √(1−ρ²)·η` generates correlated Wiener increments.

## Key Concepts
- **Drift μ**: the expected return per year (continuously compounded, arithmetic).
- **Volatility σ**: the standard deviation of returns per year. The standard deviation over Δt is σ√Δt.
- **Variance rate**: b² per unit time.
- **Quadratic variation**: `(dz)² = dt`. This is the source of the ½σ² term.
- **Lognormal property**: E(S_T) = S₀e^{μT}. The median is S₀e^{(μ−σ²/2)T}.
- **Monte Carlo simulation**: discretize, sample ε and build paths.
- **Fractional Brownian motion**: Hurst exponent H ≠ 0.5 means increments are correlated (rough volatility uses H < 0.5).

## Mental Models
- **Uncertainty scales with √T**, not T. That is why short-dated options have small time value and why volatility is quoted annually.
- **μ − σ²/2 vs μ**: the expected *arithmetic* return is μ, while the expected *log* (geometric) return is μ − σ²/2. Volatility drags compound growth.
- **Same dz for S and f(S)** is what makes a riskless hedge possible (Ch 15).

## Anti-patterns
- **Treating dz like dt in calculus**: forgetting the ½G_SS σ²S² term. Ordinary chain rules fail for stochastic calculus.
- **Confusing μ with the expected continuously compounded return** (that is μ − σ²/2).
- **Scaling volatility linearly with time** instead of with √time.

## Code Examples
```python
import numpy as np
def gbm_paths(S0, mu, sigma, T, steps, n, seed=0):
    rng = np.random.default_rng(seed); dt = T/steps
    z = rng.standard_normal((n, steps))
    return S0*np.exp(np.cumsum((mu-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z, axis=1))
```
- **What it demonstrates**: exact GBM simulation via ln S (no discretization bias).

## Worked Example
**Weekly stock move (Example 14.3).** μ = 15%, σ = 30% and Δt = 1 week = 0.0192.
- ΔS/S = 0.15 × 0.0192 + 0.30 × √0.0192·ε = 0.00288 + 0.0416ε.
- For S = $100: ΔS = 0.288 + 4.16ε. The weekly change is ~N(0.288, 4.16²).

**Itô on ln S.** With G = ln S: ∂G/∂S = 1/S, ∂²G/∂S² = −1/S², ∂G/∂t = 0.
- So dG = (μ − σ²/2)dt + σ dz: a generalized Wiener process with constant drift and volatility.

## Key Takeaways
1. Stock prices follow GBM: dS/S = μdt + σdz. They are lognormal at any horizon.
2. Standard deviation grows with √T. Variance grows linearly.
3. Itô's lemma: add ½G_SS σ²S² to the drift. The dz term is G_S σS dz.
4. ln S drifts at μ − σ²/2, the volatility drag.
5. The derivative and the underlying share one source of risk, which is the basis for the BSM hedge.

## Connects To
- **Ch 15**: the BSM PDE derived with Itô's lemma.
- **Ch 21**: Monte Carlo simulation.
- **Ch 27**: jumps, stochastic volatility and other processes.
- **Ch 28**: martingales, change of numeraire and Girsanov.
- **Ch 31–32**: short-rate processes (Itô processes for r).
