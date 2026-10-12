# Chapter 17: Structural Breaks

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 17, pp. 249–261

## Core Idea

A *structural break* is a sudden change in the data distribution. Financial time series are *full* of structural breaks: regime changes (2008 crisis, COVID 2020), corporate actions (M&A, splits), and market-microstructure changes. The chapter introduces the **CUSUM test** for detecting a break in the mean, the **Chow test** for testing a *known* break, and the **supF test** for testing for an *unknown* break.

## Frameworks Introduced

- **The CUSUM Test**:
  - For a series `X_t`, the CUSUM is `S_t = Σ_{i=1}^{t} (X_i − μ̄)`, where `μ̄` is the sample mean.
  - The null is no break; the test statistic is `max |S_t| / σ̂`.
  - Critical values are tabulated.

- **The Chow Test (Known Break)**:
  - H0: no break at `t = t_0`. H1: break at `t_0`.
  - The test statistic is `F = (RSS_0 − RSS_1) / k / (RSS_1 / (N − 2k))`, where `RSS_0` is the residual sum of squares with no break, `RSS_1` is the sum of the two sub-sample RSS, and `k` is the number of parameters.
  - Under H0, `F ~ F(k, N−2k)`.

- **The SupF Test (Unknown Break)**:
  - H0: no break. H1: a break at some `t_0`.
  - The test statistic is `sup_{t_0} F(t_0)`, where `F(t_0)` is the Chow test at each candidate break.
  - Critical values are non-standard (Andrews 1993, 2003).

- **The Bai–Perron Test (Multiple Breaks)**:
  - H0: `m` breaks. H1: `m+1` breaks.
  - The test statistic is `F(m | m+1)`.
  - The procedure is to test sequentially: `m=0 vs m=1, m=1 vs m=2, ...`, until the test fails.

## Key Concepts

1. **Structural break** — a sudden change in the data distribution.
2. **CUSUM test** — for a single unknown break in the mean.
3. **Chow test** — for a known break.
4. **SupF test** — for an unknown break (Andrews 1993).
5. **Bai–Perron test** — for multiple breaks.

## Formulas & Reference Tables

**The CUSUM statistic**

`S_t = Σ_{i=1}^{t} (X_i − μ̄)`.

**The Chow F-statistic**

`F = ((RSS_0 − RSS_1) / k) / (RSS_1 / (N − 2k))`.

**The SupF statistic**

`SupF = sup_{t_0 ∈ [π_0, 1−π_0]} F(t_0)`, where `π_0` is the trimming parameter (typically 0.15).

## Worked Example (RECOMPUTED)

*Setup.* 500 days of returns. The first 250 have mean 0% and std 1%; the second 250 have mean 0.05% and std 1.5%.

*Step 1 — CUSUM test*:
- The CUSUM should detect a break at `t = 250`.

*Step 2 — SupF test**:
- The SupF should also detect a break.

*Step 3 — Bai–Perron (multiple breaks)*:
- If there are 2 breaks, the Bai–Perron should detect both.

## Anti-patterns

- **Ignoring structural breaks.** Every backtest should test for breaks.
- **Using a Chow test with a known break but no power analysis.** The test may have low power.
- **Using a SupF test without the trimming parameter.** The SupF is sensitive to the trimming.

## Key Takeaways

1. **CUSUM, Chow, SupF, Bai–Perron** are the institutional tests.
2. **Structural breaks are pervasive in finance.**
3. **Every backtest should test for breaks.**

## Connects To

- **`tsay-analysis-financial-time-series` ch09 (Nonlinear Models and Breaks)**: the Bai–Perron test is a standard time-series tool.
