# Chapter 13: Historical Simulation and Extreme Value Theory

> Hull 4e, pp. 277–297. The non-parametric approach to VaR: from past P&L to tail quantiles.

## Core Idea

**Historical simulation (HS)** uses the empirical distribution of past P&L: `VaR_α` is the `(1-α)`-th percentile of the empirical distribution. HS is non-parametric and respects the actual tail shape; it has no model error (the data is the data). The drawbacks: with 250 daily observations, the 99% VaR is the 2nd- or 3rd-worst loss (extremely noisy); the 99.9% VaR is impossible. **Extreme Value Theory (EVT)** extends the tail: the **Generalised Pareto Distribution (GPD)** fits the tail beyond a threshold; the **Generalised Extreme Value (GEV)** distribution fits the block maxima.

## Key Concepts

- **Historical simulation (HS)** — empirical quantiles of past P&L.
- **Brute force HS** — use all past observations.
- **Weighted HS** — apply exponentially decaying weights; emphasise recent observations.
- **Volatility-adjusted HS** — scale past P&L by current volatility.
- **Generalised Pareto Distribution (GPD)** — the limit distribution of excess losses over a threshold.
- **Generalised Extreme Value (GEV)** — the limit distribution of block maxima.
- **The Peak-Over-Threshold (POT) method** — fit the GPD to losses above a high threshold.
- **The Hill estimator** — a non-parametric estimator of the tail index.
- **The shape parameter (ξ)** — `ξ > 0`: heavy-tailed (Student-t, Pareto); `ξ = 0`: thin-tailed (normal, exponential); `ξ < 0`: bounded.
- **The VaR and ES from EVT**: `VaR_α = u + (σ_u / ξ) × ((α_u / N_u)^(-ξ) − 1)`, where `u` is the threshold, `α_u` is the expected number of exceedances, `N_u` is the total.

## Formulas & Tables

- **HS VaR**: `VaR_α = Q_{1-α}(L_1, L_2, ..., L_N)` where `L_i` are past losses.
- **Volatility-adjusted HS**: `L_adjusted(t) = L(t) × σ_t / σ_T`, where `σ_T` is the realised vol on day `T`.
- **GPD**: `P(X - u > x | X > u) = (1 + ξ × x / σ_u)^{-1/ξ}`.
- **VaR from POT**: `VaR_α = u + (σ_u / ξ) × ((N_u × (1-α) / N)^(-ξ) - 1)`.
- **Hill estimator**: `H = (1/k) × Σ_{i=1}^{k} log(X_{(N-i+1)} / X_{(N-k)})`, where `X_{(i)}` is the i-th order statistic.

## Key Takeaways

1. HS is the non-parametric default; volatility-adjusted HS is the modern standard.
2. EVT (GPD, POT) extends HS into the deep tail.
3. The shape parameter ξ determines the tail behaviour: heavy (ξ > 0) vs thin (ξ < 0).

## Connects To

- ch12 (VaR), ch14 (Model-Building), `hull-derivatives` ch15 (Volatility Smiles — fat tails).
