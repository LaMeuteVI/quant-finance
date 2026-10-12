# Chapter 23: Estimating Volatilities and Correlations

## Core Idea
Volatility is stochastic and it clusters. Weight recent squared returns more heavily (EWMA), or also allow mean reversion to a long-run level (GARCH(1,1)). Fit the parameters by maximum likelihood, forecast the term structure of volatility, and update covariances with the same scheme so they stay consistent.

## Frameworks Introduced
- **Simple variance**:
  - σ²ₙ = (1/m)Σu²ₙ₋ᵢ, where uᵢ = (Sᵢ − Sᵢ₋₁)/Sᵢ₋₁.
  - For daily data, assume a zero mean and divide by m.
- **ARCH(m)**: σ²ₙ = γV_L + Σαᵢu²ₙ₋ᵢ.
- **EWMA**: `σ²ₙ = λσ²ₙ₋₁ + (1 − λ)u²ₙ₋₁`.
  - RiskMetrics uses λ = 0.94 for daily data.
  - Weights decline geometrically.
  - Only the current σ² and the latest u need to be stored.
- **GARCH(1,1)**: `σ²ₙ = ω + αu²ₙ₋₁ + βσ²ₙ₋₁`.
  - The weights satisfy γ + α + β = 1, with ω = γV_L, so V_L = ω/(1 − α − β).
  - The model is stable only if α + β < 1.
  - EWMA is the special case ω = 0, α + β = 1.
- **Forecasting with GARCH**:
  - `E[σ²ₙ₊ₜ] = V_L + (α + β)^t(σ²ₙ − V_L)`.
  - Term structure for an option of maturity T (in days): `σ(T)² = 252[V_L + (1 − e^{−aT})/(aT)·(V(0) − V_L)]`, with a = ln[1/(α + β)].
- **Maximum likelihood**:
  - Maximize `Σ[−ln vᵢ − u²ᵢ/vᵢ]` over the parameters.
  - Diagnose the fit with a Ljung–Box test on u²ᵢ/σ²ᵢ: it should show no remaining autocorrelation.
- **Correlations and covariances**:
  - EWMA: covₙ = λcovₙ₋₁ + (1 − λ)xₙ₋₁yₙ₋₁. GARCH has analogous versions.
  - Keep the matrix **positive semidefinite**: use the same λ for every variance and covariance.

## Key Concepts
- **Volatility clustering**: big moves follow big moves.
- **Mean reversion**: GARCH pulls the variance toward V_L at rate 1 − α − β per day.
- **Persistence**: α + β close to 1 means shocks decay slowly. Half-life = ln 0.5 / ln(α + β).
- **Consistency condition** for three variables: ρ₁₂² + ρ₁₃² + ρ₂₃² − 2ρ₁₂ρ₁₃ρ₂₃ ≤ 1.
- **Implied vs historical volatility**: implied is forward-looking but contains risk premia.

## Mental Models
- Use **EWMA for tracking** (simple, fast) and **GARCH for forecasting** (it mean-reverts to a long-run level).
- Think of **λ as memory**: a high λ gives a smooth, slow estimate; a low λ reacts fast.
- **GARCH term-structure forecasts** predict that implied volatilities of long-dated options move less than those of short-dated options.

## Anti-patterns
- **Estimating each correlation with a different weighting scheme**: the matrix becomes inconsistent (not PSD) and can produce a negative portfolio variance.
- **Using equal-weight historical volatility right after a crisis**: it reacts slowly, then drops abruptly when the crisis days leave the window.
- **Accepting a GARCH fit with α + β ≥ 1**: there is no mean reversion (IGARCH).

## Code Examples
```python
import numpy as np
def ewma_vol(returns, lam=0.94, init=None):
    v = init if init is not None else np.var(returns[:30])
    out = []
    for u in returns:
        out.append(np.sqrt(v)); v = lam*v + (1-lam)*u*u
    return np.array(out)
def garch_forecast(v0, omega, alpha, beta, t):
    VL = omega/(1-alpha-beta); return VL + (alpha+beta)**t*(v0-VL)
```

## Worked Example
**EWMA update (Example 23.1).** λ = 0.90. Yesterday's volatility estimate was 1% per day (σ² = 0.0001). Yesterday the variable moved 2% (u² = 0.0004).
- σ²ₙ = 0.9 × 0.0001 + 0.1 × 0.0004 = 0.00013.
- σₙ = **1.14% per day**. The move was bigger than expected, so the estimate rises.

**GARCH(1,1) (Example 23.2).** σ²ₙ = 0.000002 + 0.13u² + 0.86σ².
- γ = 1 − 0.13 − 0.86 = 0.01, so V_L = 0.000002/0.01 = 0.0002.
- Long-run volatility = √0.0002 = **1.4% per day** (≈ 22% per year).
- Suppose yesterday's estimate was 1.6% (σ² = 0.000256) and the variable fell 1% (u² = 0.0001).
- Then σ²ₙ = 0.000002 + 0.13 × 0.0001 + 0.86 × 0.000256 = 0.00023516, so σ = **1.53%**.

## Key Takeaways
1. EWMA: σ²ₙ = λσ²ₙ₋₁ + (1 − λ)u²ₙ₋₁, with λ ≈ 0.94 for daily data.
2. GARCH(1,1) adds mean reversion toward V_L = ω/(1 − α − β).
3. Fit by maximum likelihood, then check that residual autocorrelation is gone.
4. GARCH forecasts give a volatility term structure for pricing and for VaR.
5. Update covariances with the same scheme so the matrix stays PSD.

## Connects To
- **Ch 15**: historical volatility.
- **Ch 22**: inputs to VaR.
- **Ch 27**: stochastic-volatility option models.
- **Ch 20**: volatility term structure versus implied volatility.
