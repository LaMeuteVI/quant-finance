# Chapter 22: Value at Risk and Expected Shortfall

## Core Idea
- **VaR** is the loss we are X% sure not to exceed over N days.
- **Expected shortfall (ES)** is the mean loss beyond VaR. ES is coherent; VaR is not.
- Compute either one by historical simulation or by the model-building approach (linear, quadratic or Monte Carlo). Validate by back-testing.

## Frameworks Introduced
- **VaR / ES definitions**:
  - VaR is the X-percentile loss over N days.
  - ES = E[loss | loss > VaR].
  - Regulators moved from 99% 10-day VaR to **97.5% ES** under FRTB.
- **Square-root-of-time rule**: N-day VaR ≈ √N × 1-day VaR. This assumes daily changes are independent, identically distributed and normal.
- **Historical simulation**:
  - Apply each of the last ~500 days' percentage changes to today's portfolio.
  - VaR is the matching order statistic of the resulting losses. ES is the mean of the worst tail.
  - Extensions: weighting observations by age, volatility scaling, bootstrapping, stressed VaR (a stressed 12-month window), and extreme value theory for the tails.
- **Model-building approach (linear)**:
  - `ΔP = Σ δᵢΔxᵢ`, where δᵢ = Sᵢ·Δᵢ is the dollar delta.
  - `σ_P² = ΣΣ ρᵢⱼσᵢσⱼδᵢδⱼ` and VaR = z_X·σ_P·√N.
  - Normal ES = σ·e^{−z²/2}/(√(2π)(1 − X)).
  - Bonds are handled by cash-flow mapping onto standard maturities.
- **Quadratic (delta–gamma) model**: `ΔP = δΔS + ½γ(ΔS)²`. Options make ΔP skewed. Use Cornish–Fisher or Monte Carlo on this approximation.
- **Monte Carlo VaR**: simulate market moves, revalue fully (or use delta–gamma), then read off the percentiles.
- **Back-testing**:
  - Count exceptions: days when the loss exceeded VaR.
  - Formal check: the Kupiec test.
  - Basel traffic light, for 250 days at 99%: 0–4 exceptions green, 5–9 yellow, 10+ red.
- **Principal components analysis (PCA)**:
  - Correlated rates reduce to about 3 factors: shift (~80–90% of variance), twist and bow.
  - VaR is then computed from exposures to those factors.

## Key Concepts
- **Coherent risk measure**: satisfies monotonicity, translation invariance, homogeneity and **subadditivity**. VaR can fail subadditivity; ES satisfies all four.
- **Marginal, incremental and component VaR**: component VaRs add up to the total (Euler allocation).
- **Diversification benefit**: the sum of standalone VaRs minus the portfolio VaR.
- **Regulatory capital** (Basel II.5/III): multiplier × (VaR + stressed VaR). FRTB replaces this with ES and liquidity horizons.
- **Factor loadings**: sensitivities of rate moves to the principal components.

## Mental Models
- **VaR tells you a threshold; ES tells you how bad it gets beyond it.** Use ES when the tails matter (options, credit).
- **Historical simulation lets the data speak** (fat tails, non-linear correlations), but it assumes the past 500 days are representative.
- **Linear VaR fails for option books.** A short-gamma book loses more in the tails than its delta suggests.

## Anti-patterns
- **Using VaR as a limit that traders can game**: selling deep OTM options hides tail risk beyond the VaR level.
- **Scaling 1-day VaR by √N** when returns are autocorrelated or volatility clusters.
- **Ignoring model risk in back-tests**: zero exceptions can mean VaR is too conservative.

## Worked Example
**Two-stock linear VaR (Section 22.3).** $10m in Microsoft (daily σ = 2%), $5m in AT&T (1%), correlation ρ = 0.3.
- Daily standard deviations: 200,000 and 50,000.
- Portfolio: √(200k² + 50k² + 2 × 0.3 × 200k × 50k) = **220,200**.
- 1-day 99% VaR = 2.326 × 220,200 = $512,300. The 10-day VaR is **$1,620,100**.
- Standalone 10-day VaRs are $1,471,300 and $367,800, so the diversification benefit is **$219,000**.
- 10-day 99% ES (normal): Microsoft $1,687,000; AT&T $421,400; combined **$1,856,100**.

**Option book (Example 22.1).**
- Deltas: 1,000 on Microsoft options (S = 120) and 20,000 on AT&T options (S = 30).
- So ΔP = 120,000Δx₁ + 600,000Δx₂.
- With σ = 2% and 1% and ρ = 0.3, σ_ΔP = $7,099 per day.
- 5-day 95% VaR = 1.645 × √5 × 7,099 = **$26,100**.

## Key Takeaways
1. Linear, normal case: VaR = z·σ_P·√N and ES = σ·φ(z)/(1 − X).
2. ES is coherent (subadditive); VaR is not. Regulators now use 97.5% ES.
3. Historical simulation is model-free but backward-looking. Add stressed periods.
4. Option books need delta–gamma or full-revaluation Monte Carlo.
5. PCA reduces yield-curve risk to about 3 factors. Back-test VaR exceptions.

## Connects To
- **Ch 19**: deltas and gammas feed the linear and quadratic models.
- **Ch 23**: volatility and correlation inputs (EWMA/GARCH).
- **Ch 24**: credit VaR.
- **Ch 4 / Ch 6**: duration, the one-factor ancestor of PCA.
