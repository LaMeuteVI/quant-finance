# Chapter 14: Backtest Statistics

> **Source**: Marcos López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 14, pp. 195–210

## Core Idea

A backtest is a *single sample* from a stochastic process; the *statistics* you compute from it are estimators with bias, variance, and (worst) overfitting. The chapter introduces the four statistics that together form the institutional backtest report: the **Deflated Sharpe Ratio (DSR)** — corrects the Sharpe for the number of trials; the **Probability of Backtest Overfitting (PBO)** — measures the chance that the chosen strategy is the *worst* of all backtested strategies; the **Minimum Track Record Length (MinTRL)** — the number of bets needed to distinguish skill from luck; and the **out-of-sample (OOS) test** — the only honest assessment of skill.

These four statistics are what separate a research report from a sales pitch.

## Frameworks Introduced

- **The Deflated Sharpe Ratio (DSR)**:
  - The DSR adjusts the *in-sample* Sharpe for the number of trials `N_t` and the skew/kurtosis of the return distribution.
  - `DSR = (SR̂ − SR₀) × √(V[SR̂])^(-1)`, where `SR̂` is the backtest Sharpe, `SR₀ = E[max SR]` is the expected maximum Sharpe under the null (given `N_t` trials), and `V[SR̂]` is the variance of the SR estimator (Bailey & López de Prado 2014, formula 6).
  - `E[max SR | N_t] ≈ √(2 log N_t) − (γ / √(2 log N_t)) + (log log N_t + log(4π) − 2γ) / (2 (2 log N_t)^(3/2))`, where `γ ≈ 0.5772` is the Euler–Mascheroni constant.
  - The variance of the SR estimator (with skew `γ₃` and kurtosis `γ₄`):
    `V[SR̂] = 1 + γ₃ SR̂ − (γ₄ − 1)/4 × SR̂²` (in annualised units, divided by T).
  - *When to use*: every time a backtest SR is reported. The DSR tells the manager whether the SR is *surprising* given the number of trials.
  - *Why it works*: the multiple-testing correction is built into the SR threshold; a SR of 1.0 is impressive with N_t = 1, but it is *expected* with N_t = 100.
  - *Failure mode*: applying the DSR to a single trial "as a sanity check" — the DSR is most useful precisely when N_t is large.

- **The Probability of Backtest Overfitting (PBO)**:
  - PBO is the probability that the *best* of N_t backtested strategies is the *worst* out-of-sample.
  - Computed via **Combinatorially Symmetric Cross-Validation (CSCV)**:
    1. Compute the in-sample (IS) Sharpe for every strategy on every sub-sample.
    2. For each sub-sample split, compute the rank correlation between the IS ranks and the OOS ranks.
    3. The PBO is the fraction of splits where the best IS strategy is the worst OOS strategy.
  - *When to use*: after running N_t strategies; PBO is the institutional measure of whether your "best" strategy is actually a fluke.
  - *Why it works*: CSCV uses the OOS performance as a "ground truth" check on the IS ranking; the rank correlation tells you how much you can trust the IS ranking.
  - *Failure mode*: when the strategies are too similar (high correlation), CSCV cannot distinguish them; the PBO is meaningless.

- **The Minimum Track Record Length (MinTRL)**:
  - The MinTRL is the minimum number of bets needed to distinguish a true SR from 0 with statistical confidence.
  - `MinTRL ≈ 1 + (1 − γ₃ × SR + (γ₄ − 1)/4 × SR²) × (z_α / SR)²` (annualised, divided by periods per year).
  - For SR = 1, MinTRL ≈ 4 years of monthly data. For SR = 2, MinTRL ≈ 1 year.
  - *When to use*: before allocating capital to a strategy. The MinTRL is the answer to "how much data do I need before I can trust this backtest?".
  - *Why it works*: the formula is a power calculation; with a target SR and a target confidence, the formula gives the required sample size.

- **The Out-of-Sample (OOS) Test**:
  - The OOS test is the only honest assessment of a strategy's skill. The IS Sharpe is optimistically biased by construction; the OOS Sharpe is the real number.
  - *When to use*: always. The OOS test is not a *check*; it is the *test*.
  - *Failure mode*: peeking at the OOS performance and then changing the strategy; the OOS is no longer OOS if you have seen it.

## Key Concepts

1. **Deflated Sharpe Ratio (DSR)** — the Sharpe ratio corrected for the number of trials, skew, and kurtosis.
2. **Probability of Backtest Overfitting (PBO)** — the probability that the best IS strategy is the worst OOS strategy.
3. **Combinatorially Symmetric Cross-Validation (CSCV)** — the cross-validation scheme that supports PBO; uses the rank correlation between IS and OOS across many sub-sample splits.
4. **Minimum Track Record Length (MinTRL)** — the minimum number of bets needed to distinguish skill from luck with statistical confidence.
5. **Multiple testing haircut** — the correction for the number of trials; the central idea behind the DSR.
6. **Selection bias** — the bias introduced by choosing the best of N_t strategies; the DSR corrects for this.
7. **Effective number of bets** — `N_eff = T × ū`, where `T` is the number of time periods and `ū` is the average uniqueness of the bets.
8. **Out-of-sample (OOS) Sharpe** — the Sharpe computed on data not used in the IS optimisation; the honest measure.
9. **The "look-ahead" bias** — the bug where a strategy uses future data; the OOS test catches it.

## Formulas & Reference Tables

**Expected maximum SR under the null (for N_t iid strategies, normally distributed returns)**

`E[max SR | N_t] ≈ (1 − γ) Φ^(-1)(1 − 1/N_t) + γ Φ^(-1)(1 − 1/(N_t e))`, where `γ ≈ 0.5772` and `Φ^(-1)` is the inverse normal CDF.

For N_t = 100, this gives E[max SR] ≈ 2.51. **A backtest SR of 2.5 from 100 trials is *expected* under the null.**

**Deflated Sharpe Ratio (annualised)**

`DSR = (SR̂ × √(T − 1)) × Φ( (SR̂ × √(T − 1) − E[max SR] × √(T − 1)) / √(V[SR̂] × T) )`

Or, more compactly: the DSR is the probability that the true SR exceeds `E[max SR]`, under the distributional assumption.

**Variance of the SR estimator (annualised, with T observations)**

`V[SR̂] = (1 + γ₃ SR̂ − (γ₄ − 1)/4 × SR̂²) / T`

where `γ₃` is skewness and `γ₄` is kurtosis. For a normal return, `γ₃ = 0`, `γ₄ = 3`, so `V[SR̂] = (1 − 0.5 × SR̂²) / T`.

**Minimum Track Record Length (annualised, in years)**

`MinTRL = 1 + (1 − γ₃ SR + (γ₄ − 1)/4 × SR²) × (z_α / SR)²`

For `SR = 1`, `γ₃ = 0`, `γ₄ = 3`, `z_0.95 = 1.645`: `MinTRL = 1 + (1 − 0.5) × (1.645/1)² = 1 + 0.5 × 2.706 = 1 + 1.35 = 2.35 years`. (This is monthly data, annualised; for daily data the factor is different.)

**The PBO formula (via CSCV)**

`PBO = (1/M) × Σ_{m=1}^{M} I{r̂_c(IS_m) = best, r̂_c(OOS_m) = worst}`,

where `M` is the number of CSCV splits, `IS_m` is the IS sub-sample in split `m`, `OOS_m` is the OOS sub-sample, and `r̂_c` is the log-relative return rank.

**The logit transform for the PBO**

`logit(PBO) = log(PBO / (1 − PBO))`; the logit is approximately normally distributed and is the standard output of the `pbo` function in `mlfinlab`.

## Mental Models

- **A backtest is a single sample; treat it as such.** The DSR is the multiple-testing correction; the PBO is the overfitting test; the MinTRL is the sample-size check.
- **The OOS test is the only honest test.** Everything else is a *consistency check*.
- **Skew and kurtosis matter.** A strategy with high skew (e.g. lots of small losses and rare large gains) has a *negative* expected return at high confidence levels; the DSR captures this.
- **The "I'm in the 1% tail" trap.** A SR of 1 is impressive until you realise you ran 100 strategies and the expected max SR is 2.5.

## Worked Example (RECOMPUTED)

*Setup.* A quant researcher runs 50 strategies, picks the one with the best backtest Sharpe, and reports a SR of 2.8 (annualised) over 3 years of monthly data. The best strategy's monthly returns have skewness `γ₃ = −0.5` (left-tailed) and kurtosis `γ₄ = 4.5`. How surprised should we be?

*Step 1 — Expected max SR under the null (N_t = 50)*.
- `E[max SR | N_t=50] ≈ √(2 × ln 50) − γ / √(2 × ln 50)`
- `= √(7.824) − 0.5772 / √(7.824) = 2.797 − 0.206 = 2.591`
- So the expected max SR under the null is **2.59**. The researcher's 2.8 is *barely* above this.

*Step 2 — DSR*.
- First, the variance of the SR estimator: `V[SR̂] = (1 + γ₃ × SR̂ − (γ₄ − 1)/4 × SR̂²) / T`
- `= (1 + (−0.5) × 2.8 − (4.5 − 1)/4 × 2.8²) / 36`
- `= (1 − 1.4 − 0.875 × 7.84) / 36`
- `= (1 − 1.4 − 6.86) / 36`
- `= −7.26 / 36 = −0.20`
- **Negative variance is impossible**; the result means the data is so non-normal that the asymptotic SR estimator is invalid. The DSR is undefined or NaN; the report should refuse to compute a SR.
- *Lesson*: a strategy with high kurtosis and significant negative skew has a *negative* `V[SR̂]`; the agent must use HAC-robust estimators or bootstrap the SR distribution.

*Step 3 — PBO (via bootstrap if rank-correlation is computable)*.
- With 50 strategies and 36 monthly observations, the PBO is typically high (60–80%) for any single best strategy; the CSCV would assign high PBO to this portfolio.

*Step 4 — MinTRL*.
- `MinTRL = 1 + (1 − γ₃ × SR + (γ₄ − 1)/4 × SR²) × (z_α / SR)²`
- `= 1 + (1 − (−0.5) × 2.8 + (4.5 − 1)/4 × 2.8²) × (1.645 / 2.8)²`
- `= 1 + (1 + 1.4 + 0.875 × 7.84) × 0.345`
- `= 1 + (1 + 1.4 + 6.86) × 0.345`
- `= 1 + 9.26 × 0.345 = 1 + 3.19 = 4.19` years

So the strategy needs ~4.2 years of out-of-sample data to be confident the SR is real at 95% confidence — **longer than the 3 years of IS data used to fit it**.

*Step 5 — Interpretation*.
- The backtest SR of 2.8 is *not* impressive when corrected for the 50 trials, the negative skew, and the high kurtosis.
- The strategy needs 4+ years of OOS data to be statistically significant.
- The agent should not allocate capital until the OOS data is collected.

*Sanity check (Python).*
```python
import math
N_t, T, SR, gamma3, gamma4, z = 50, 36, 2.8, -0.5, 4.5, 1.645

# Step 1: expected max SR under the null
log_N = math.log(N_t)
E_max = math.sqrt(2*log_N) - 0.5772/math.sqrt(2*log_N)
print(f"E[max SR] = {E_max:.3f}")

# Step 2: variance of SR estimator
V = (1 + gamma3*SR - (gamma4-1)/4 * SR**2) / T
print(f"V[SRhat] = {V:.3f}  (negative => non-normal data; DSR undefined)")

# Step 4: MinTRL
MinTRL = 1 + (1 - gamma3*SR + (gamma4-1)/4 * SR**2) * (z/SR)**2
print(f"MinTRL (years) = {MinTRL:.2f}")
```

## Anti-patterns

- **Reporting a backtest Sharpe without a DSR correction.** A SR of 1.0 across 100 trials is expected under the null.
- **Trusting the in-sample Sharpe as the true Sharpe.** It is *always* optimistically biased.
- **Skipping the OOS test.** "I trust my backtest" is not a substitute for an OOS check.
- **Computing the DSR with a normal assumption when the returns are fat-tailed.** The DSR requires the correct `γ₃` and `γ₄`.
- **Computing the PBO with too few strategies.** The PBO requires `N_t ≥ 16` or so to be meaningful.
- **Stopping the OOS test when it confirms the backtest.** A confirmed OOS is great; a failing OOS means *stop*, not "iterate".

## Practitioner Notes

- **2026 update.** The DSR/PBO framework is now standard in institutional quant research; the `mlfinlab` Python library implements them. The companion papers (Bailey & López de Prado 2014 "DSR"; Bailey, Borwein, López de Prado & Zhu 2016 "PBO"; Bailey, Borwein, López de Prado & Zhu 2014 "Pseudo-Mathematics") are the canonical references.
- **The DSR is necessary but not sufficient.** A high DSR does not mean the strategy will work; it means the strategy is *not obviously* a fluke. The OOS test is the only sufficient test.
- **SPA (Hansen 2005) and Reality Check (White 2000)** are the alternative tests for many-strategies. The DSR/PBO is the López de Prado formulation; SPA is the academic standard. For a multi-strategy comparison, the agent should compute both.
- **The "live paper" test.** A useful additional check: a strategy's OOS performance in the *first 6–12 months of live paper trading* is the most informative single test. The agent should never skip this step.

## Key Takeaways

1. **The Deflated Sharpe Ratio (DSR)** is the institutional multiple-testing correction; a SR of 2.5 is *expected* under the null with 100 trials.
2. **The Probability of Backtest Overfitting (PBO)** is the institutional overfitting test; it is computed via CSCV.
3. **The Minimum Track Record Length (MinTRL)** is the institutional sample-size check; it tells you how much OOS data is needed.
4. **The OOS test is the only sufficient test** of a strategy's skill.
5. **Skew and kurtosis matter**; a strategy with high kurtosis and negative skew has a *negative* `V[SR̂]`, and the DSR is undefined until the variance estimator is corrected.

## Connects To

- **ch11** (Dangers of Backtesting): the framework is the response to the pathologies enumerated there.
- **ch12** (Backtesting through Cross-Validation): the cross-validation that supports the PBO and the DSR.
- **ch13** (Backtesting on Synthetic Data): the synthetic-data extension when the OOS sample is too small.
- **ch15** (Understanding Strategy Risk): the deeper look at the strategy-risk consequences of the DSR/PBO/MinTRL.
- **`hull-risk-management` ch12 (VaR and ES), ch25 (Model Risk)**: the institutional risk-management framing of backtest statistics.
- **`hull-risk-management` ch14 (Model-Building Approach)**: the backtest of a VaR model is the same discipline.
- **`diebold-mariano-forecast-accuracy` skill**: the forecast-comparison test that complements the strategy-comparison test.
