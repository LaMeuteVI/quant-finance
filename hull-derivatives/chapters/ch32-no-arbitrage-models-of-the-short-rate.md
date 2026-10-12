# Chapter 32: No-Arbitrage Models of the Short Rate

## Core Idea
No-arbitrage short-rate models take today's zero curve as an input and fit it exactly through a time-dependent drift θ(t). Ho–Lee and Hull–White (extended Vasicek) remain analytically tractable. Lognormal models (BDT, Black–Karasinski) avoid negative rates. All are implemented on trinomial trees and calibrated to caps or swaptions.

## Frameworks Introduced
- **Ho–Lee**: `dr = θ(t)dt + σdz`.
  - θ(t) = F_t(0,t) + σ²t, where F(0,t) is the instantaneous forward rate.
  - Normal rates with no mean reversion. All rates are equally volatile.
- **Hull–White (one-factor)**: `dr = [θ(t) − ar]dt + σdz`.
  - θ(t) = F_t(0,t) + aF(0,t) + (σ²/2a)(1 − e^{−2at}).
  - Bond prices are affine: `P(t,T) = A(t,T)e^{−B(t,T)r}` with `B = (1 − e^{−a(T−t)})/a`.
  - European bond options have closed forms (Jamshidian's decomposition handles coupon bonds and hence swaptions).
- **BDT / Black–Karasinski**: `d ln r = [θ(t) − a ln r]dt + σdz`.
  - Lognormal, so r > 0. There is no analytic bond price, so use trees.
- **Hull–White two-factor**: adds a stochastic factor to the reversion level, which allows curve twists.
- **Volatility structures**:
  - Ho–Lee: flat forward-rate volatility.
  - Hull–White: the volatility of the T-maturity forward decays as σe^{−a(T−t)}.
- **Trinomial tree procedure (Hull–White)**:
  1. Build a tree for x (dx = −ax dt + σdz), with Δx = σ√(3Δt) and branching that switches at j_max ≈ 0.184/(aΔt).
  2. Shift each level by α_i so the tree reprices P(0, (i+1)Δt), using **Arrow–Debreu prices** Q_{i,j} and forward induction.
  3. Roll back to value derivatives. American and Bermudan features are handled naturally.
- **Calibration**:
  - Choose a and σ (or σ(t)) to minimize pricing errors on caps or swaptions.
  - Prefer calibrating to instruments similar to the product being priced.
- **Hedging with one-factor models**: use the model's delta/gamma to r, or zero-curve bucket deltas computed by bumping and refitting.

## Key Concepts
- **Arrow–Debreu (state) prices Q_{i,j}**: the PV of $1 paid if node (i, j) is reached.
- **θ(t)**: the time-dependent drift that fits the initial curve.
- **Negative rates**: possible in normal models (Ho–Lee, Hull–White), impossible in lognormal models (BDT, BK).
- **Jamshidian decomposition**: an option on a coupon bond = a portfolio of options on zero-coupon bonds, each struck at the value implied by the critical r*.

## Mental Models
- **The fit to today's curve is free; the volatility structure is the modeling choice.** Mean reversion a controls how forward-rate volatility decays with maturity.
- **Calibrate locally**: parameters fitted to 1y×5y swaptions will not necessarily price 10y×20y swaptions well.
- **Trinomial trees + forward induction = exact curve fit** at every time step.

## Anti-patterns
- **Using Ho–Lee for long-dated products**: without mean reversion, long rates are as volatile as short rates, which is unrealistic.
- **Recalibrating daily and treating parameter changes as P&L noise**: this is model risk hiding in the parameters.
- **Using a one-factor model for spread options between rates**: all rates are perfectly correlated in it.

## Worked Example
**Hull–White tree (Example 32.1).**
- Product: a 3-year European put on a 9-year zero-coupon bond (face 100), strike 63.
- Model: a = 0.1, σ = 0.01, with the zero curve of Table 32.2 (e.g., 3-month rate 4.96%), interpolated linearly.
- Build the x-tree with Δx = 0.01·√(3Δt). Shift it level by level so that it reprices the market discount factors.
- At the 3-year nodes, compute 9-year bond prices analytically with P = A·e^{−Br}. Roll back the put payoff.
- The tree price converges to the **analytic Hull–White price** as the number of steps grows (Table 32.3). This validates the construction.

## Key Takeaways
1. No-arbitrage models fit today's curve exactly via θ(t).
2. Hull–White = extended Vasicek: tractable, mean-reverting, with a closed form for European bond options.
3. Lognormal models (BDT, BK) keep rates positive but need trees.
4. Trinomial trees + Arrow–Debreu forward induction calibrate α_i step by step.
5. Calibrate a and σ to instruments that resemble the product being priced.

## Connects To
- **Ch 31**: equilibrium versions.
- **Ch 29**: caps and swaptions used for calibration.
- **Ch 21**: trinomial trees.
- **Ch 33**: HJM (Ho–Lee and Hull–White are special cases).
- **Ch 34**: Bermudan and cancelable swaps valued on these trees.
