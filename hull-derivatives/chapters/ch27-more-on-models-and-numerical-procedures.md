# Chapter 27: More on Models and Numerical Procedures

## Core Idea
Fitting the smile requires departing from GBM. The main alternatives are CEV, jump-diffusion, variance-gamma, stochastic volatility and the IVF (local volatility) model. Hard products need specialized numerics:
- convertible bonds with default,
- path-dependent trees,
- barrier-aligned grids,
- two-asset trees,
- Longstaff–Schwartz Monte Carlo for American options.

## Frameworks Introduced
- **CEV model**: `dS = (r − q)S dt + σS^α dz`.
  - α < 1 means volatility rises as S falls, which produces an equity-like skew.
  - α = 1 is GBM.
- **Merton jump-diffusion**: `dS/S = (r − q − λk)dt + σdz + dp`. Jumps arrive as a Poisson process with lognormal sizes.
  - The price is a Poisson-weighted sum of BSM prices.
  - It produces FX-like smiles, and short-dated smiles are stronger.
- **Variance-gamma**: time runs on a gamma-distributed clock. The skew and kurtosis parameters give flexibility.
- **Stochastic volatility**:
  - Hull–White: `dV = a(V_L − V)dt + ξV^α dz_V`, with correlation ρ to the price.
  - Heston: α = 0.5.
  - ρ < 0 gives the equity skew; ρ = 0 gives a symmetric smile.
  - When ρ = 0, the price is the BSM price averaged over the distribution of average variance.
- **IVF / local volatility (Dupire, Derman–Kani)**: σ(S, t) is chosen to fit *all* European prices exactly. Its forward smile dynamics are unrealistic, which matters for compound and barrier options.
- **Convertible bonds**: trees with an extra default branch (hazard λ, recovery R). At each node, take the max of holding, conversion and (issuer's) call.
- **Path-dependent trees**: carry representative values of the path function (e.g., the running average) at each node and interpolate during rollback. Used for Asians and lookbacks.
- **Barrier options on trees**: convergence is slow when the barrier falls between nodes. Fixes:
  - position the nodes on the barrier,
  - interpolate between the inner and outer barrier,
  - use an adaptive mesh.
- **Two correlated assets**: transform to uncorrelated variables, or adjust the probabilities of a 3-D tree.
- **Monte Carlo for American options**:
  - **Longstaff–Schwartz**: work back from maturity. On ITM paths, regress the discounted continuation value on basis functions of S. Exercise wherever intrinsic > fitted continuation.
  - **Parametrized exercise boundary** (Andersen): optimize the boundary iteratively.

## Key Concepts
- **Smile-consistent models**: models calibrated to fit the vanilla surface.
- **Forward smile**: the smile the model implies for the future. It drives exotic prices.
- **Mixed jump-diffusion / stochastic volatility**: models combining both, used in practice.
- **Credit-risky convertible**: its value depends on hazard rates and on the issuer's call policy.

## Mental Models
- **Short-maturity smile ≈ jumps; long-maturity smile ≈ stochastic volatility.**
- **Two models that fit today's vanillas can price exotics very differently.** Model risk lives in the forward dynamics.
- **Longstaff–Schwartz = backward induction with regression**: the continuation value is estimated, not computed exactly.

## Anti-patterns
- **Pricing forward-start or cliquet exotics with local volatility**: it flattens forward smiles and misprices them.
- **Using too few basis functions or including OTM paths in the regression** of Longstaff–Schwartz. The resulting estimate is biased.
- **Trees whose nodes miss the barrier**: they produce oscillating, biased barrier prices.

## Worked Example
**Convertible bond (Example 27.1).**
- Terms: 9-month zero-coupon bond, face $100, convertible into 2 shares (S₀ = 50). The issuer can call at $113.
- Inputs: σ = 30%, λ = 1%, R = 40%, r = 5%. Use a 3-step tree with Δt = 0.25.
- Tree parameters: u = 1.1618, d = 0.8607, p_u = 0.5115, p_d = 0.4860, p_default = 0.0025. The bond is worth 40 at the default nodes.
- At each node the value is `max(conversion value, min(holding value, call price))`.
- **Node E** (S = 50): holding value = (0.5115 × 116.18 + 0.4860 × 100 + 0.0025 × 40)e^{−0.0125} = 106.78. This is above the conversion value of 100, and the issuer will not call at 113.
- **Node B** (S = 58.09): holding value 119.54 > call price 113. The issuer calls, and the holder then converts for 116.18.
- Rolling back to the root gives **$107.44**.

## Key Takeaways
1. CEV → equity skew; jumps → FX smile; stochastic volatility with ρ < 0 → equity skew.
2. IVF/local volatility fits every European price but distorts the forward smile.
3. Convertibles: trees with a default branch plus conversion and call decisions at each node.
4. Barrier trees: align nodes with the barrier or interpolate.
5. American Monte Carlo: Longstaff–Schwartz regression on ITM paths.

## Connects To
- **Ch 20**: smiles that these models explain.
- **Ch 21**: base numerics.
- **Ch 26**: exotics valued with these methods.
- **Ch 24**: hazard rates in convertibles.
