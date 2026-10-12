# Chapter 9: Hyper-Parameter Tuning with Cross-Validation

> López de Prado, AFML, Chapter 9, pp. 129–140.

## Core Idea

**Hyper-parameter tuning** is the optimisation of the meta-parameters of the model (regularisation strength, tree depth, learning rate) via CV. The chapter introduces the **grid search**, the **random search**, the **Bayesian optimisation**, and the **overfit of hyper-parameters** — a subtle but real danger. The institutional response: use **purged k-fold CV** for the hyper-parameter search, and **report the OOS performance** on a *third* set (the test set) that is *not* used in the search.

## Key Concepts

- **Grid search** — exhaustive search over a grid of hyper-parameters.
- **Random search** — random sampling of the hyper-parameter space; often more efficient than grid.
- **Bayesian optimisation** — the hyper-parameter space is modelled by a Gaussian process; the next sample is chosen to maximise the expected improvement.
- **Overfit of hyper-parameters** — the hyper-parameters are chosen to maximise the CV performance; the CV performance is optimistically biased.
- **The nested CV** — the inner loop selects the hyper-parameters; the outer loop estimates the OOS performance.
- **Purged k-fold for hyper-parameter search** — the inner loop uses purged k-fold.
- **Train/validation/test split** — the *test set* is held out for the final estimate.

## Formulas & Tables

- **Grid search**: iterate over all combinations of hyper-parameter values.
- **Random search**: sample `N` combinations uniformly from the hyper-parameter space.
- **Bayesian optimisation**: `θ_{n+1} = argmax_θ EI(θ) = argmax_θ (μ(θ) - f* - ξ) Φ((μ(θ) - f* - ξ) / σ(θ)) + σ(θ) φ(...)`, with `μ, σ` from the GP, `f*` the best value so far, `ξ` the exploration-exploitation trade-off.
- **Nested CV**: outer loop = purged k-fold for the OOS performance; inner loop = purged k-fold for the hyper-parameter selection.

## Key Takeaways

1. Random search is more efficient than grid for high-dimensional hyper-parameter spaces.
2. Bayesian optimisation is the state-of-the-art for expensive models.
3. The hyper-parameter search is itself prone to overfit; the nested CV is the institutional response.

## Connects To

- ch07 (CV in Finance), ch08 (Feature Importance), ch14 (Backtest Statistics).
