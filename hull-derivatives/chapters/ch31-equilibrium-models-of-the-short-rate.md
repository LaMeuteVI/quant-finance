# Chapter 31: Equilibrium Models of the Short Rate

## Core Idea
A Markov model for the instantaneous short rate r determines the whole term structure as a function of today's r. Vasicek and CIR are the classic mean-reverting equilibrium models. They are tractable (affine bond prices) but do **not** fit today's curve exactly. Use them for simulation and intuition; for pricing, use the no-arbitrage models of Ch 32.

## Frameworks Introduced
- **Short-rate valuation**: `P(t,T) = Ê[e^{−∫_t^T r dτ}]` in the traditional risk-neutral world.
  - The zero rate is `R(t,T) = −ln P(t,T)/(T − t)`.
- **Vasicek**: `dr = a(b − r)dt + σdz`.
  - Mean-reverting at speed a toward level b, with normally distributed rates (they can go negative).
  - `P(t,T) = A(t,T)e^{−B(t,T)r}` with `B = (1 − e^{−a(T−t)})/a`.
- **CIR**: `dr = a(b − r)dt + σ√r dz`.
  - The volatility scales with √r, so rates stay non-negative when 2ab ≥ σ².
  - It also has the affine form A·e^{−Br}, with different A and B.
- **Duration in affine models**: the sensitivity of P to r is B(t,T), which is less than T − t. The effective duration of a zero-coupon bond is B, not its maturity.
- **Real world vs risk-neutral**:
  - Real-world drift = risk-neutral drift + λσ(r).
  - The market price of interest rate risk λ is **negative**.
  - Vasicek with constant λ: same process, but the risk-neutral reversion level is higher (so the real-world level is lower).
  - CIR with λ ∝ √r: the real-world process has a higher reversion speed and a lower level.
- **Parameter estimation**:
  - Regress Δr on r (discretized AR(1)) using a short-term rate proxy.
  - Or use maximum likelihood.
  - Or calibrate to the term structure and options.
- **Richer models**: two-factor (Longstaff–Schwartz, with stochastic volatility), and equilibrium models with time-varying parameters.

## Key Concepts
- **Instantaneous short rate r**: the rate applicable to an infinitesimal period.
- **Mean reversion**: high rates tend to fall and low rates tend to rise. Half-life = ln 2 / a.
- **Affine term-structure model**: log bond prices are linear in r.
- **One-factor limitation**: all rates are perfectly correlated instantaneously, so the curve cannot twist.

## Mental Models
- **Mean reversion dampens long-rate volatility**: long rates move less than short rates, consistent with data.
- **Vasicek = a normal, tractable, possibly negative model; CIR = a square-root, positive model.** Choose by whether negative rates are acceptable or desirable.
- **Equilibrium models produce the curve; no-arbitrage models take the curve as input.**

## Anti-patterns
- **Pricing derivatives with Vasicek/CIR without refitting**: model bond prices will not match market bond prices, so the derivative prices are off by construction.
- **Using maturity as the duration in mean-reverting models**: the effective duration is B(T) < T.
- **Estimating a from noisy daily data without accounting for the measure** (real-world vs risk-neutral).

## Worked Example
**Mean-reversion duration (Example 31.1).** A 4-year zero-coupon bond.
- Yield-based duration D = 4: +10bp in the yield → price −0.4%.
- In Vasicek with a = 0.1: B(0,4) = (1 − e^{−0.4})/0.1 = **3.30**.
- So +10bp in the *short rate* → price −0.33%. Mean reversion makes the long end less sensitive to short-rate shocks.

## Key Takeaways
1. One-factor short-rate models: P = A·e^{−Br}. The whole curve is driven by r.
2. Vasicek: normal rates, which can be negative. CIR: √r volatility, non-negative rates.
3. Mean reversion makes B(T) < T and dampens long-rate volatility.
4. The market price of interest rate risk is negative. Real-world and risk-neutral processes differ in their drift.
5. Equilibrium models don't fit today's curve. For pricing, move to Ho–Lee or Hull–White.

## Connects To
- **Ch 4**: duration and the term structure.
- **Ch 28**: market price of risk.
- **Ch 32**: no-arbitrage extensions (Hull–White = extended Vasicek).
- **Ch 33**: HJM/LMM.
