# Chapter 21: Basic Numerical Procedures

## Core Idea
When no closed form exists, value derivatives with one of three methods:
- **Trees**: American options with few underlying variables.
- **Monte Carlo**: path-dependent or many-variable, European-style payoffs.
- **Finite differences**: PDE-based, handles American exercise.

Accuracy comes from variance reduction, control variates and convergence checks.

## Frameworks Introduced
- **Binomial trees in practice (CRR)**:
  - `u = e^{σ√Δt}`, `d = 1/u`, `p = (a − d)/(u − d)`, with `a = e^{(r−q)Δt}`.
  - For FX use q = r_f. For futures use a = 1.
  - **Greeks from the tree**: Δ from the first-step nodes, Γ from the second-step nodes, `Θ = (f₂,₁ − f₀)/(2Δt)`. Vega and rho by bumping the input and rebuilding.
- **Discrete dividends**:
  - Known dividend *yield* at time t: shift the tree down by (1 − δ). It stays recombining.
  - Known *cash* dividend: build the tree on `S* = S − PV(D)`, then add PV(D) back at each node. It stays recombining.
- **Control variate technique (trees)**: `f_A(est) = f_A(tree) + [f_E(BSM) − f_E(tree)]`. The error the tree makes on the European option is used to correct the American value.
- **Alternative trees**:
  - Equal probabilities (p = ½).
  - **Trinomial**: `u = e^{σ√(3Δt)}`, with probabilities p_u, p_m = 2/3, p_d.
  - **Adaptive mesh**: finer grid near the strike and near expiry.
- **Time-dependent parameters**: vary Δt or p to fit term structures of r and σ.
- **Monte Carlo**:
  - Simulate risk-neutral paths: `ln S(t+Δt) = ln S(t) + (r − q − σ²/2)Δt + σε√Δt`.
  - Average the discounted payoffs. Standard error = ω/√M.
  - For several variables, correlate the ε values with a Cholesky decomposition.
- **Variance reduction**:
  - Antithetic variables (ε and −ε).
  - Control variates (a similar derivative with a known value).
  - Importance sampling (sample where the payoff is nonzero).
  - Stratified sampling.
  - Moment matching.
  - Quasi-random (Sobol) sequences: error ~1/M instead of 1/√M.
- **Finite difference methods**: discretize the BSM PDE on an (S, t) grid and solve backward.
  - **Implicit**: always stable. Needs a tridiagonal solve at each step.
  - **Explicit**: equivalent to a trinomial tree. Can be unstable; using ln S as the variable helps.
  - **Crank–Nicolson**: the average of the two. Second-order accurate.

## Key Concepts
- **Convergence**: tree prices oscillate as N changes. Average N and N+1, or use smoothing and Richardson extrapolation.
- **Standard error**: MC price ± 1.96·ω/√M is a 95% confidence interval.
- **Cholesky**: correlated normals via ε = Lz, with LLᵀ = Σ.
- **Monte Carlo Greeks**: pathwise or likelihood-ratio methods, or bump-and-revalue with the **same random numbers**.
- **American options with MC**: need regression-based methods such as Longstaff–Schwartz (Ch 27).

## Mental Models
- **Choose by structure**:
  - American with ≤2 factors → tree or finite differences.
  - Path-dependent or ≥3 factors, European → Monte Carlo.
  - Barriers → adaptive grids or trees whose nodes sit on the barrier.
- **Monte Carlo cost grows linearly with the number of variables.** Trees and grids grow exponentially (the curse of dimensionality).
- **Always report the MC standard error** next to the price.

## Anti-patterns
- **Bumping with fresh random numbers** to get MC Greeks: the noise swamps the signal.
- **Explicit finite differences with too large a Δt**: unstable, oscillating values.
- **Too few tree steps for American options with dividends**, without a control variate.

## Code Examples
```python
import numpy as np
def mc_euro_call(S0, K, r, q, sigma, T, M=200_000, seed=1, antithetic=True):
    rng = np.random.default_rng(seed); z = rng.standard_normal(M)
    if antithetic: z = np.concatenate([z, -z])
    ST = S0*np.exp((r-q-0.5*sigma**2)*T + sigma*np.sqrt(T)*z)
    disc = np.exp(-r*T)*np.maximum(ST-K, 0)
    return disc.mean(), disc.std(ddof=1)/np.sqrt(len(disc))   # price, standard error
```
- **What it demonstrates**: exact-GBM Monte Carlo with antithetic variates and a reported standard error.

## Worked Example
**American put (Example 21.1).**
- Inputs: S₀ = K = 50, r = 10%, σ = 40%, T = 5 months, 5 steps of 1 month (Δt = 0.0833).
- Tree parameters: u = 1.1224, d = 0.8909, a = 1.0084, p = 0.5073.
- The 5-step tree gives **$4.49**. With more steps it converges to ≈ **$4.28** (4.272, 4.278, 4.283 at larger N).
- **Control variate**: price the European put on the same 5-step tree and compare it with BSM. Correcting the American estimate by that European error removes most of the discretization error.

## Key Takeaways
1. Trees for low-dimensional American options. MC for path dependence and high dimensions. Finite differences for PDE-based American pricing.
2. Handle cash dividends with the S* = S − PV(D) tree so it stays recombining.
3. Use control variates and antithetic variables. Always quote the MC standard error.
4. Implicit and Crank–Nicolson FD are stable. Explicit FD is a trinomial tree and can go unstable.
5. Compute Greeks with common random numbers or differences between tree nodes.

## Connects To
- **Ch 13**: binomial basics.
- **Ch 19**: Greeks.
- **Ch 26**: exotics valued numerically (Asians, lookbacks, barriers).
- **Ch 27**: path-dependent trees, Longstaff–Schwartz, the barrier grid problem.
- **Ch 32**: interest rate trees (Hull–White trinomial).
