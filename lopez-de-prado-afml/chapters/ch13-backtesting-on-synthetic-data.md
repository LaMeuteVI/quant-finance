# Chapter 13: Backtesting on Synthetic Data

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 13, pp. 169–193

## Core Idea

A backtest on real data is limited by the available history. The chapter introduces **synthetic data** as a complementary tool: when the history is too short, the agent can generate synthetic data that *preserves* the statistical properties of the real data (returns distribution, autocorrelation, vol clustering) but is *longer* or has *different* regime structure. The two main uses are: (a) **stress testing** a strategy against data the strategy has not seen, and (b) **Monte Carlo** for risk metrics (e.g. the expected shortfall of a strategy over a long horizon).

## Frameworks Introduced

- **The Synthetic Data Generation Pipeline**:
  1. Estimate the parameters of the real data (returns distribution, autocorrelation, vol clustering).
  2. Generate a long synthetic series that preserves the parameters.
  3. Run the strategy on the synthetic data; measure the OOS performance.

- **The Two Main Uses**:
  - **Stress testing**: the synthetic data has regime changes that the real data does not; the strategy is tested against a worse regime.
  - **Monte Carlo**: the synthetic data is generated many times; the distribution of the OOS performance is the institutional measure of the strategy's risk.

- **The Synthetic Data Method (the "Generating Synthetic Data" recipe)**:
  1. Estimate the *unconditional* mean and standard deviation.
  2. Estimate the *autocorrelation* (ACF, PACF).
  3. Estimate the *volatility clustering* (GARCH, etc.).
  4. Estimate the *tail dependence* (copula, etc.).
  5. Generate a long series that preserves all of the above.

## Key Concepts

1. **Synthetic data** — artificially generated data that preserves the statistical properties of the real data.
2. **Stress testing** — running the strategy against a worse regime.
3. **Monte Carlo backtest** — running the strategy many times; the distribution of the OOS performance.
4. **Statistical properties** — the mean, standard deviation, autocorrelation, vol clustering, tail dependence.
5. **The "Generating Synthetic Data" recipe** — the chapter's framework for generating realistic synthetic data.

## Worked Example (RECOMPUTED)

*Setup.* A daily returns series with mean 0.05%, standard deviation 1%, autocorrelation 0.05, GARCH(1,1) parameters (0.05, 0.9).

*Step 1 — Estimate the parameters*.
- Mean: 0.0005. Std: 0.01. AR(1) coefficient: 0.05. GARCH(1,1): omega=0.0001, alpha=0.05, beta=0.9.

*Step 2 — Generate the synthetic series*.
- For t = 1, 2, ..., T:
  - `r_t = μ + φ × r_{t-1} + σ_t × ε_t`, where `ε_t ~ N(0, 1)`.
  - `σ_t² = ω + α × r_{t-1}² + β × σ_{t-1}²`.

*Step 3 — Run the strategy on the synthetic data*.

## Anti-patterns

- **Generating synthetic data that does not preserve the tail dependence.** The synthetic data should match the empirical *joint* distribution, not just the marginals.
- **Using synthetic data as a substitute for OOS testing.** Synthetic data is a *complement*, not a *substitute*.

## Key Takeaways

1. **Synthetic data is a complement to OOS testing**, not a substitute.
2. **The statistical properties** of the synthetic data should match the real data.
3. **The two main uses** are stress testing and Monte Carlo.

## Connects To

- **ch07** (Cross-Validation in Finance): the synthetic data is an alternative to the CPCV.
- **ch11** (Dangers of Backtesting): the synthetic data is a response to the data-snooping danger.
- **`hull-risk-management` ch13 (Historical Simulation and EVT)**: the synthetic data is a parametric alternative.
