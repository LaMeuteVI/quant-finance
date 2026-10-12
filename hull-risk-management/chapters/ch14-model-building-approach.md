# Chapter 14: Model-Building Approach

> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed. (Wiley, 2012) | Chapter 14, pp. 299–323

## Core Idea

The model-building approach to VaR parametrizes the **joint distribution of market variables** and uses that distribution to compute the portfolio's loss distribution analytically or via simulation. The four building blocks are: (1) the **volatility model** for each variable, (2) the **correlation model** across variables, (3) the **simulation engine** (parametric closed-form, Monte Carlo, or historical), and (4) the **mapping** of the portfolio's payoffs to the market variables. Each block has its own failure modes, and the chapter devotes explicit attention to *which* assumptions are most exposed in tail events.

This chapter is the bridge between the *abstract* risk-measure theory of ch12 and the *practical* calculation pipelines that produce a daily VaR/ES number.

## Frameworks Introduced

- **The Model-Building VaR Pipeline**:
  1. Specify the model for each market variable's return (volatility, mean reversion, jumps).
  2. Specify the joint distribution (correlations, copulas).
  3. Map portfolio positions to the market variables (delta, gamma, vega for options).
  4. Generate scenarios (parametric or simulation).
  5. Revalue the portfolio under each scenario.
  6. Compute the loss distribution; report VaR / ES.

- **Variance-Covariance (parametric) VaR**:
  - For a linear portfolio of normal variables, `VaR_α = z_α × √(h' V h)`, where `h` is the position vector, `V` is the covariance matrix, and `z_α` is the standard normal quantile.
  - *When to use*: short-dated linear portfolios (equities, FX, linear rates).
  - *Why it works*: closed-form; trivially decomposable by risk factor.
  - *Failure mode*: understates tail risk; cannot handle non-linear payoffs (options).

- **The Cornish-Fisher expansion for non-normal VaR**:
  - Adjust the normal quantile for skew and kurtosis:
    `z_CF = z + (S/6)(z² − 1) + (K/24)(z³ − 3z) − (S²/36)(2z³ − 5z)`, where `S` is skew and `K` is excess kurtosis.
  - *When to use*: when returns are non-normal but a parametric form is needed.
  - *Why it works*: a third-order correction to the normal quantile; preserves tractability.

- **The Model-Building Approach for Options (the full revaluation vs. delta approximation)**:
  - Full revaluation under each scenario is the correct method for non-linear payoffs; the delta-only approximation understates tail risk.
  - The Hull chapter's worked example shows that a portfolio of long calls can have a 99% VaR *10× larger* than the delta-only VaR.

- **The Stressed VaR**:
  - Compute VaR using a 12-month window of stressed conditions (Basel III / FRTB requirement).
  - *Why it matters*: addresses the failure of the 1-year VaR to capture rare but persistent regime shifts (e.g. 2008).

- **The Incremental VaR and Component VaR**:
  - Incremental VaR for a position: `ΔVaR = VaR(P) − VaR(P − x_i)`. The marginal contribution of position `i` to portfolio VaR.
  - Component VaR: a linear decomposition such that `Σ CVaR_i = VaR(P)`, where the equality holds exactly for variance-covariance VaR.

- **The Conditional VaR (CVaR) approximation**:
  - For non-normal distributions, `CVaR_α ≈ VaR_α + (1/(1−α)) × E[(L − VaR_α)⁺]`. The Cornish-Fisher or Student-t form gives a tractable closed-form.

## Key Concepts

1. **Variance-covariance VaR** — closed-form VaR assuming normal joint distribution.
2. **Monte Carlo VaR** — simulation-based VaR; handles any payoff and distribution.
3. **Historical simulation VaR** — empirical VaR from past returns; non-parametric.
4. **Cornish-Fisher expansion** — a parametric correction for non-normality.
5. **Delta, Gamma, Vega** — the first-, second-, and volatility-sensitivity Greeks that map option positions to underlying risk factors.
6. **Stress VaR** — VaR computed over a 12-month stressed window; the FRTB requirement.
7. **Incremental VaR** — the change in portfolio VaR from adding or removing a position.
8. **Component VaR** — the linear decomposition of portfolio VaR into position contributions.
9. **Model risk** — the risk that the model is wrong; a first-order concern for any model-building approach.
10. **The mapping function** — the function that revalues the portfolio under each scenario.

## Formulas & Reference Tables

**Variance-Covariance VaR (linear, normal)**

`VaR_α = z_α × √(h' V h)` for a linear portfolio.

For multi-asset portfolio with covariance matrix `V` (NxN), the position vector `h` is Nx1.

**Delta-normal VaR (for option portfolios with linearisation)**

`VaR_α ≈ z_α × √(Δ' V_Δ Δ)`, where `Δ` is the position's vector of deltas to each underlying and `V_Δ` is the covariance of the underlyings.

**Cornish-Fisher-adjusted quantile**

`z_CF(α) = z_α + (1/6)(z_α² − 1)S + (1/24)(z_α³ − 3z_α)K − (1/36)(2z_α³ − 5z_α)S²`

where `S` is skew and `K` is excess kurtosis.

**ES (Cornish-Fisher, for skew and kurtosis)**

`ES_α ≈ VaR_CF + (1/(1−α)) × σ × [φ(z_CF) + S/6 × (z_CF² − 1) φ(z_CF) + ...]`

**Marginal VaR (gradient of VaR w.r.t. position)**

`∂VaR/∂h_i = z_α × (V h)_i / √(h' V h)`

**Component VaR (linear decomposition)**

`C_VaR_i = h_i × ∂VaR/∂h_i = z_α × h_i × (V h)_i / √(h' V h)`, with `Σ C_VaR_i = VaR`.

**Stressed VaR definition (Basel III)**

`SVaR_α = VaR_α (using a 12-month stressed period)`. Computed weekly; the regulatory capital uses the worst SVaR over the past 12 months.

## Mental Models

- **The model is the model; the world is not.** A parametric VaR is only as good as its distributional assumptions. Stress-test every input.
- **Delta-only VaR is an approximation.** For option-heavy portfolios, full revaluation is the only honest method.
- **Stressed VaR is the failure-mode-aware VaR.** A 99% VaR over a calm 1-year window is a lie; the 2008 episode showed that.

## Worked Example (RECOMPUTED)

*Setup.* A linear equity portfolio with three positions, `h = [100, 200, 150]` (in $thousands), covariance matrix

`V = [[0.04, 0.01, 0.005], [0.01, 0.04, 0.012], [0.005, 0.012, 0.0225]]`

(i.e. 20%, 20%, 15% annual vol, with correlations ~0.4, 0.2, 0.8 between (1,2), (1,3), (2,3)).

*Step 1 — Parametric VaR at 99%*.
- `V h = [0.04×100 + 0.01×200 + 0.005×150, 0.01×100 + 0.04×200 + 0.012×150, 0.005×100 + 0.012×200 + 0.0225×150]`
- `= [4 + 2 + 0.75, 1 + 8 + 1.8, 0.5 + 2.4 + 3.375]`
- `= [6.75, 10.8, 6.275]`
- `h' V h = 100×6.75 + 200×10.8 + 150×6.275 = 675 + 2160 + 941.25 = 3776.25` (in $(thousand)² of variance)
- `√(h' V h) = 61.45` (thousand $)
- `VaR_0.99 = 2.326 × 61.45 = $142.9 thousand`

*Step 2 — Component VaR*.
- `C_VaR_1 = 100 × 6.75 / 61.45 × VaR = 100 × 6.75 / 61.45 × $142.9k = $11.0k × (1/61.45) × ... let me redo.`
- More carefully: `C_VaR_i = h_i × (V h)_i / √(h' V h) × z_α`
  - `C_VaR_1 = 100 × 6.75 / 61.45 × 2.326 = 6.75/61.45 × 100 × 2.326 = 0.1098 × 232.6 = 25.55k`
  - `C_VaR_2 = 200 × 10.8 / 61.45 × 2.326 = 10.8/61.45 × 200 × 2.326 = 0.1758 × 465.2 = 81.78k`
  - `C_VaR_3 = 150 × 6.275 / 61.45 × 2.326 = 6.275/61.45 × 150 × 2.326 = 0.1021 × 348.9 = 35.62k`
- Sum = 25.55 + 81.78 + 35.62 = $142.95k ≈ VaR ✓

So the second position is contributing ~57% of the VaR, the third ~25%, the first ~18%. The decomposition tells the manager where the risk is concentrated.

*Sanity check (Python).*
```python
import numpy as np
from scipy.stats import norm

V = np.array([[0.04, 0.01, 0.005], [0.01, 0.04, 0.012], [0.005, 0.012, 0.0225]])
h = np.array([100, 200, 150])
alpha = 0.99
z = norm.ppf(alpha)
V_h = V @ h
port_var = h @ V_h
port_vol = np.sqrt(port_var)
VaR = z * port_vol
C_VaR = h * V_h / port_vol * z
print(f"Portfolio vol: {port_vol:.2f}")
print(f"VaR 99% (1-day, $k): {VaR:.2f}")
print(f"Component VaR: {C_VaR.round(2)}  sum: {C_VaR.sum():.2f}")
```

## Anti-patterns

- **Using delta-only VaR for option portfolios.** A long call can have delta-only VaR much smaller than full revaluation VaR; the convexity is in the tail.
- **Using a 1-year window of calm data.** The 99% VaR over 2017 is not a 99% VaR; the 99% VaR over 2008 is closer to a 99% VaR.
- **Reporting VaR without component decomposition.** The aggregate number hides the concentration of risk.
- **Ignoring the correlation breakdown in stress.** The correlations used in VaR (from the last year) are not the correlations in stress; in 2008, equity-bond correlations went from −0.3 to +0.6.

## Practitioner Notes

- **2026 update.** The FRTB (replacing the 2012 Basel's market risk framework that Hull 4e describes) is the binding standard. The IMA (Internal Models Approach) uses **ES at 97.5%** as the default measure, not 99% VaR; the IMA capital is `ES × m`, where `m` is a multiplier between 1.0 and 1.84 that depends on the backtest exception count and the P&L attribution test.
- **Stressed ES** under FRTB is computed over a 12-week stressed window. The Hull 4e's 12-month stressed VaR is broadly consistent with the FRTB approach but the metric is now ES, not VaR.
- **The risk-factor taxonomy** under FRTB is more granular than under the pre-FRTB framework. The Modellen Approach (FRTB SA) buckets risk factors by asset class, risk type (delta, vega, curvature), and a "bucket" classification. The Hull 4e does not cover this taxonomy.
- **Model risk management** (the next chapter in Hull) is the explicit response to the failure of any single model-building approach.

## Key Takeaways

1. **Variance-covariance, historical simulation, and Monte Carlo** are the three model-building approaches; the choice depends on portfolio non-linearity and data availability.
2. **Cornish-Fisher** is the parametric fix for non-normality when closed-form is required.
3. **Component VaR** decomposes the aggregate; the marginal contribution is `h_i × (V h)_i / √(h' V h) × z_α`.
4. **Stressed VaR (or stressed ES under FRTB)** is the failure-mode-aware risk measure; the 1-year calm-window VaR is not a 99% VaR.
5. **The mapping function** (revaluation logic) is the most under-appreciated source of model error; the wrong mapping produces a wrong VaR even with the right distribution.

## Connects To

- **ch09** (Interest Rate Risk): the duration-convexity mapping is the canonical mapping for linear rates products.
- **ch10** (Volatility): the volatility model is the input to the variance-covariance VaR.
- **ch11** (Correlations and Copulas): the correlation model is the input to the joint distribution.
- **ch12** (VaR and ES): the model-building approach produces the VaR/ES number.
- **ch13** (Historical Simulation and EVT): the non-parametric alternative to the parametric approach.
- **ch17** (Fundamental Review of the Trading Book): the regulatory framework that uses ES + stressed ES + backtest multiplier.
- **`frtb-market-risk-bcbs457` skill**: the binding source for FRTB's ES approach.
- **`lopez-de-prado-afml` ch14 (Backtest Statistics)**: the formal backtesting of the model.
