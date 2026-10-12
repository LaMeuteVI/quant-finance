# Chapter 16: Machine Learning Asset Allocation

> **Source**: López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 16, pp. 221–235

## Core Idea

The chapter applies ML to the *asset allocation* problem: given a set of asset returns, the goal is to find a portfolio that maximises a risk-adjusted return. The traditional approach (mean-variance) is dominated by estimation error in the means. The chapter introduces the **Hierarchical Risk Parity (HRP)** algorithm, which uses the correlation matrix (not the covariance) and a hierarchical clustering to produce a portfolio that is more robust to estimation error than the mean-variance portfolio.

## Frameworks Introduced

- **The Hierarchical Risk Parity (HRP) Algorithm**:
  1. Compute the correlation matrix of returns.
  2. Compute the distance matrix `D_ij = √(0.5 × (1 − ρ_ij))`.
  3. Hierarchical clustering (single-linkage) on the distance matrix.
  4. Quasi-diagonalisation: re-order the rows and columns of the covariance matrix according to the dendrogram.
  5. Recursive bisection: split the portfolio into two halves, allocate inverse-variance weights, recurse.

- **The Comparison with Mean-Variance**:
  - Mean-Variance (Markowitz): `h* = V^(-1) μ`. Dominated by estimation error in `μ`.
  - HRP: `h` from the recursive bisection. More robust; the out-of-sample Sharpe is typically higher.
  - The minimum-variance portfolio (no `μ`): `h* = V^(-1) 1 / (1' V^(-1) 1)`. More robust than mean-variance but still depends on `V`.

- **The "Nested Clustered Optimisation" (NCO) Algorithm**:
  1. Cluster the assets by correlation.
  2. Allocate weights *between* clusters by inverse-variance.
  3. Allocate weights *within* clusters by inverse-variance (or mean-variance if there is enough data).
  4. The result is a hierarchical portfolio that respects the correlation structure.

## Key Concepts

1. **HRP (Hierarchical Risk Parity)** — the algorithm of the chapter.
2. **Hierarchical clustering** — single-linkage, complete-linkage, average-linkage.
3. **Quasi-diagonalisation** — re-ordering the covariance matrix to match the dendrogram.
4. **Recursive bisection** — the weight allocation step.
5. **NCO (Nested Clustered Optimisation)** — the generalisation.
6. **Minimum-variance portfolio** — the special case with no `μ`.
7. **Estimation error** — the dominant source of error in the mean-variance portfolio.

## Formulas & Reference Tables

**The distance matrix**

`D_ij = √(0.5 × (1 − ρ_ij))`.

**The single-linkage clustering**

`D(C_a ∪ C_b, C_c) = min(D(C_a, C_c), D(C_b, C_c))`.

**The recursive bisection allocation**

`w_L = 1 − w_R`, where `w_L / w_R = (1 / V_L²) / (1 / V_R²)`, with `V_L²` and `V_R²` the variances of the two halves.

## Worked Example (RECOMPUTED)

*Setup.* 5 assets, with covariance matrix
```
V = [[0.04, 0.01, 0.005, 0.002, 0.001],
     [0.01, 0.04, 0.012, 0.003, 0.002],
     [0.005, 0.012, 0.0225, 0.001, 0.001],
     [0.002, 0.003, 0.001, 0.02, 0.01],
     [0.001, 0.002, 0.001, 0.01, 0.025]]
```

*Step 1 — Compute the distance matrix*.

*Step 2 — Cluster*.

*Step 3 — Quasi-diagonalise and bisect*.

*Step 4 — Compare HRP to mean-variance and min-variance*.

## Anti-patterns

- **Using mean-variance without shrinkage.** The raw sample covariance is unfit for production.
- **Using the equal-weight portfolio as the default.** The HRP is a better default; the equal-weight is only appropriate when the correlation is low and the volatilities are similar.
- **Trusting the in-sample Sharpe of an HRP portfolio.** The HRP is more robust than mean-variance but not robust to overfitting.

## Key Takeaways

1. **HRP is more robust than mean-variance** in the presence of estimation error.
2. **The hierarchical clustering** of the correlation matrix is the key step.
3. **The recursive bisection** allocates inverse-variance weights.
4. **NCO is the generalisation** that allows mean-variance within clusters.

## Connects To

- **ch14** (Backtest Statistics): the backtest of an HRP portfolio uses the same statistics.
- **`grinold-kahn-apm` ch14 (Portfolio Construction)**: the HRP is a more robust alternative to the Grinold–Kahn construction.
- **`hull-risk-management` ch14 (Model-Building Approach)**: the portfolio VaR is the risk metric for the HRP.
