# Chapter 5: High-Frequency Data Analysis

> Tsay, Chapter 5. Realised volatility, bipower variation, microstructure noise.

## Core Idea

**High-frequency data** (intraday ticks) allows direct estimation of the **realised variance** `RV_t = Σ r_{i,t}²` where `r_{i,t}` is the i-th intraday return. The **bipower variation** `BV_t = (π/2) × Σ |r_{i,t}| × |r_{i-1,t}|` is a robust alternative. **Microstructure noise** (bid-ask bounce, price discreteness) biases the realised variance upward; the **two-scale realised variance (TSRV)** corrects for this.

## Key Concepts

- **Realised variance (RV)** — `RV_t = Σ r_{i,t}²`; consistent estimator of integrated variance.
- **Bipower variation (BV)** — robust to jumps; `BV_t = (π/2) × Σ |r_{i,t}| × |r_{i-1,t}|`.
- **Jump detection** — `RV_t - BV_t > threshold` indicates jumps.
- **Two-scale realised variance (TSRV)** — corrects for microstructure noise.
- **Realised kernel (RK)** — Barndorff-Nielsen, Hansen, Lunde, Shephard 2008; a robust alternative.
- **Multi-power variation** — `MP(p) = μ_p^{-1} × Σ |r_{i,t}|^p` for `μ_p = E[|Z|^p]`; the basis for jump-robust estimators.
- **Microstructure noise** — the bid-ask bounce; biases RV upward.
- **Subsampling** — averaging over different sampling frequencies; the basis of the multi-scale estimators.

## Formulas & Tables

- **RV**: `RV_t = Σ r_{i,t}²`.
- **BV**: `BV_t = (π/2) × Σ |r_{i,t}| × |r_{i-1,t}|`.
- **TSRV**: `TSRV = RV̄ - (n̄ / n) × RV`, where `RV̄` is the average of subsampled RVs and `n̄` is the average number of observations.
- **Jump test statistic**: `J = (RV - BV) / √(θ × (Σ |r|^4))`; `~N(0,1)` under no jumps.

## Key Takeaways

1. RV is the direct estimator of integrated variance.
2. BV is robust to jumps; the difference RV - BV detects jumps.
3. TSRV and RK correct for microstructure noise.

## Connects To

- ch03 (GARCH), ch07 (Multivariate), `hull-risk-management` ch10 (Volatility), `lopez-de-prado-afml` ch02 (Information-driven bars).
