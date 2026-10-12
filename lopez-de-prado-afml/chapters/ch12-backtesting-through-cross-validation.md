# Chapter 12: Backtesting through Cross-Validation

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 12, pp. 161–168

## Core Idea

The standard k-fold CV is *not* a backtest; it is a model-selection tool. To turn CV into a *backtest*, you need (a) purged k-fold or CPCV (ch07), and (b) a clear *backtest path* — a single train-test combination that produces a single OOS performance number. The chapter introduces the **CPCV backtest path** as a sequence of OOS predictions, the **CPCV Sharpe ratio** as the per-path performance metric, and the **probability of OOS Sharpe exceeding a threshold** as the institutional summary statistic.

## Frameworks Introduced

- **The CPCV Backtest Path**:
  - A path is a sequence of OOS predictions, one per test fold in the CPCV.
  - The OOS predictions are concatenated to form a single OOS time series.
  - The path's Sharpe is `SR_path = μ(OOS returns) / σ(OOS returns) × √(periods per year)`.

- **The Distribution of Backtest Sharpes**:
  - With `N_paths = C(N, k)` paths, the distribution of `SR_path` is the institutional measure of the strategy's OOS performance.
  - The mean `μ(SR_path)` is the expected OOS Sharpe; the standard deviation `σ(SR_path)` is the variability of the OOS performance.

- **The Probability of Outperforming**:
  - `P(SR > target) = P(Z > (target − μ) / σ)`, where `Z` is standard normal.
  - The "Probability of Backtest Overfitting" (PBO) is `P(SR_OOS < 0)` — the probability that the OOS performance is *negative* despite a positive IS performance.

## Key Concepts

1. **CPCV backtest path** — a sequence of OOS predictions from one CPCV split.
2. **OOS Sharpe** — the Sharpe of the OOS predictions.
3. **The distribution of backtest Sharpes** — the institutional measure of the strategy's OOS performance.
4. **The Probability of Backtest Overfitting (PBO)** — the probability that the OOS performance is negative.
5. **The Sharpe threshold** — the target OOS Sharpe the strategy must beat.

## Formulas & Reference Tables

**The path Sharpe**

`SR_path = (μ_path / σ_path) × √(periods per year)`.

**The mean and standard deviation of the path Sharpe**

`μ(SR) = (1/N_paths) × Σ_p SR_p`, `σ(SR) = √(1/(N_paths−1) × Σ_p (SR_p − μ(SR))²)`.

**The probability of OOS outperformance**

`P(SR > target) = 1 − Φ((target − μ(SR)) / σ(SR))`.

## Worked Example (RECOMPUTED)

*Setup.* CPCV with N=6, k=3, 20 paths. The 20 path Sharpes are `SR_p ∈ [0.1, 1.2]` with mean 0.5 and standard deviation 0.3.

*Step 1 — Mean and standard deviation*:
- `μ(SR) = 0.5`, `σ(SR) = 0.3`.

*Step 2 — Probability of OOS outperformance (target = 0.5)*:
- `P(SR > 0.5) = 1 − Φ(0 / 0.3) = 0.5`. **50% chance** of OOS Sharpe exceeding 0.5.

*Step 3 — Probability of OOS Sharpe > 0*:
- `P(SR > 0) = 1 − Φ((0 − 0.5) / 0.3) = 1 − Φ(−1.67) = 1 − 0.0475 = 0.9525`. **95% chance** of OOS Sharpe > 0.

## Anti-patterns

- **Using standard k-fold as a backtest.** It is a model-selection tool, not a backtest.
- **Reporting a single backtest Sharpe.** The distribution of Sharpes is the institutional measure.
- **Ignoring the PBO.** A high IS Sharpe with high PBO is a fluke.

## Key Takeaways

1. **CPCV is the institutional backtest**; standard k-fold is wrong.
2. **The distribution of OOS Sharpes** is the institutional measure; a single Sharpe is not enough.
3. **The PBO** is the probability that the OOS Sharpe is *negative* despite a positive IS performance.
4. **The mean and standard deviation of the path Sharpes** are the inputs to the DSR and PBO.

## Connects To

- **ch07** (Cross-Validation in Finance): the CPCV is the basis for the backtest paths.
- **ch11** (Dangers of Backtesting): the framework is the response to the dangers.
- **ch14** (Backtest Statistics): the DSR and PBO are the institutional statistics.
