# Chapter 15: Understanding Strategy Risk

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 15, pp. 211–219

## Core Idea

A strategy's *risk* is not just its *return* risk (the volatility of its returns); it is the *probability* that the strategy underperforms in the future, after accounting for the OOS uncertainty. The chapter formalises the *triangular relationship* between the Sharpe ratio, the statistical confidence, and the time horizon: a high IS Sharpe over a long history is *more* likely to be real than a moderate IS Sharpe over a short history.

## Frameworks Introduced

- **The Triangular Relationship**:
  - Given a target Sharpe `SR*` and a target confidence `α`, the minimum track record length is `MinTRL = 1 + (1 + (γ₄−1)/4 × SR²) × (z_α / SR)²`.
  - For SR* = 1, 95% confidence: MinTRL ≈ 2.4 years of monthly data.
  - The relationship is *non-linear*: doubling the SR reduces MinTRL by a factor of 4.

- **The Path Dependence of Strategy Risk**:
  - A strategy that has produced a high IR for 5 years is *less* risky than one that has produced the same IR for 1 year.
  - The risk of a strategy is a *function* of its history.

- **The Bayesian Update of Strategy Risk**:
  - Each day of OOS performance is a Bayesian update of the prior on the strategy's alpha.
  - A consistent string of positive days strengthens the belief; a string of negative days weakens it.

## Key Concepts

1. **Strategy risk** — the probability that the strategy underperforms in the future.
2. **Triangular relationship** — the SR, confidence, and horizon are linked.
3. **Path dependence** — the strategy's risk depends on its history.
4. **Bayesian update** — each day of performance updates the belief.

## Formulas & Reference Tables

**The MinTRL (annualised, in years)**

`MinTRL = 1 + (1 + (γ₄−1)/4 × SR²) × (z_α / SR)²`.

For `SR = 1, γ₄ = 3, z_0.95 = 1.645`: `MinTRL = 1 + (1 + 0.5) × (1.645)² = 1 + 1.5 × 2.706 = 1 + 4.06 = 5.06`. (Note: this depends on whether the formula is for monthly or annual data; LdP ch14 has both versions.)

**The Bayesian Sharpe Ratio update**

The posterior on the SR, given a sequence of OOS returns, is approximately normal with mean `(μ_OOS × N + μ_prior / σ²_prior) / (N + 1/σ²_prior)` and variance `1 / (N + 1/σ²_prior)`.

## Worked Example (RECOMPUTED)

*Setup.* A strategy with 5 years of monthly data, mean return 1%, standard deviation 3%, target SR 0.33, 95% confidence.

*Step 1 — Realised SR*:
- `SR_realised = (0.01 / 0.03) × √12 = 1.15` (annualised).

*Step 2 — MinTRL for SR* = 0.5, 95% confidence*:
- `MinTRL = 1 + (1 + 0.5) × (1.645 / 0.5)² = 1 + 1.5 × 10.83 = 1 + 16.24 = 17.24 years`. **17 years of monthly data is required** to confirm SR = 0.5 at 95% confidence.

*Step 3 — Implication*:
- The 5-year history is *not* enough to confirm the realised SR of 1.15 with confidence. The agent should report the *uncertainty* on the SR estimate.

## Anti-patterns

- **Treating the IS Sharpe as the true Sharpe.** Always report the MinTRL.
- **Confusing statistical confidence with practical significance.** A high-confidence low-SR is not better than a low-confidence high-SR.

## Key Takeaways

1. **Strategy risk is a function of the history**, not just the realised return.
2. **The MinTRL is the institutional measure** of the required history.
3. **The Bayesian update** is the correct way to combine prior with evidence.
4. **The triangular relationship** is the key tool.

## Connects To

- **ch14** (Backtest Statistics): the MinTRL is the central statistic.
- **`hull-risk-management` ch25 (Model Risk)**: the strategy risk is the model risk of the strategy.
- **`grinold-kahn-apm` ch17 (Performance Analysis)**: the skill/luck ratio is the equivalent in the active-management framework.
