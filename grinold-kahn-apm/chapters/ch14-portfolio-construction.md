# Chapter 14: Portfolio Construction

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 14, pp. 377–418 (Part Four: Implementation)

## Core Idea

Given a **forecast of residual alpha** `α` and a **covariance matrix** `V` of residual returns, the optimal active portfolio is the one that **maximises value-added** `VA = α' h − (λ/2) h' V h`, where `h` is the active weight vector. The classical mean-variance solution `h* = (1/λ) V^(-1) α` is the **unconstrained** optimum; the chapter develops the *residual* formulation, the *fundamental law* connection, the impact of *forecast uncertainty*, and the **residual alpha** as the lever that connects forecasting to construction.

The chapter's most important practical point: the optimal `h` is the *single* vector that maximises the value-added; the `α` comes from forecasting, the `V` from the risk model, and the `λ` from the investor's risk aversion. Get any of the three wrong, and the construction is wrong.

## Frameworks Introduced

- **The Mean-Variance Active Portfolio (the basic formula)**:
  `h* = (1/λ) V^(-1) α`, where:
  - `h` = active weights (deviation from benchmark)
  - `α` = forecast of residual alpha (per asset)
  - `V` = covariance matrix of residual returns
  - `λ` = risk aversion (typically 2 for a quadratic investor with a 50/50 mean-variance mix)
  - *When to use*: the textbook unconstrained active portfolio. The starting point for every implementation.
  - *Why it works*: the KKT conditions of the value-added maximisation give this closed form.
  - *Failure mode*: `V` is singular or ill-conditioned; `V^(-1) α` is dominated by estimation error. **In practice, shrink `V` toward a structured prior.**

- **The Residual Formulation (the full Grinold–Kahn form)**:
  - Decompose the total alpha into a **common-factor** component and a **residual** component.
  - The optimal *common-factor* exposure comes from a separate optimisation (the asset allocation problem; ch18).
  - The optimal *residual* exposure is the mean-variance solution above.
  - *Why it works*: separates two decisions: the manager's view on **which factor premia to harvest** and the manager's view on **which individual assets to overweight** within the chosen factor exposures.

- **The Fundamental Law of Active Management in Construction**:
  - `IR² = α' V^(-1) α`. The squared IR is the value-added of the optimal portfolio per unit of variance.
  - *Why it matters*: gives a clean target for the construction — the IR of the constructed portfolio is the sqrt of the value-added divided by the variance.

- **Forecast Uncertainty (the alpha risk problem)**:
  - The realised alpha is `α_realised = α_forecast + ε`, where `ε` is the *forecast error* with covariance `P` (the covariance of the forecast error).
  - The optimal portfolio under uncertainty is `h* = (1/λ) (V + P)^(-1) α_forecast` — the *certainty-equivalent* version. Adding `P` to `V` shrinks the weights toward the benchmark.
  - *When to use*: always in practice. The naïve `V^(-1) α` formula overweights assets with the most uncertain forecasts.
  - *Failure mode*: under-estimating `P` (the most common error in real-world systems).

- **The Bayesian View of Portfolio Construction**:
  - The Black–Litterman model combines the *equilibrium* view (from market capitalisation weights) with the *manager's* view (from forecasting). It is the formal Bayesian version of the Grinold–Kahn framework.
  - *When to use*: when the manager's α has low confidence and the benchmark has the right structure.

## Key Concepts

1. **Active weight `h`** — deviation from benchmark weights; the decision variable in construction.
2. **Residual alpha `α`** — the forecast of the return *in excess of the benchmark*, on a residual basis.
3. **Risk aversion `λ`** — the multiplier on variance in the mean-variance objective; the inverse of the investor's tolerance.
4. **Value-added (VA)** — `α' h − (λ/2) h' V h`; the mean-variance objective in active space.
5. **Tracking error (TE)** — `√(h' V h)`; the standard deviation of the active return.
6. **Information ratio (IR)** — `α' h / √(h' V h)`; the per-unit-of-TE alpha.
7. **Forecast uncertainty covariance `P`** — the covariance of the *forecast error*; a measure of how much the manager does not trust their own alpha.
8. **Bayesian shrinkage** — combining a prior (e.g. zero alpha) with the observed alpha; reduces the impact of noisy estimates.
9. **Black–Litterman** — the institutional implementation of the Bayesian view; combines equilibrium returns with the manager's views.
10. **Residualisation** — removing the common-factor component from the alpha; the *pure* stock-specific view.

## Formulas & Reference Tables

**The unconstrained optimal active portfolio**

`h* = (1/λ) V^(-1) α`

**Value-added at the optimum**

`VA* = (1 / (2λ)) α' V^(-1) α`

**IR² of the optimal portfolio**

`IR² = α' V^(-1) α` (this is also the maximum information ratio, achieved by `h*`).

**Optimal portfolio under forecast uncertainty**

`h*_CE = (1/λ) (V + P)^(-1) α`

**TE constraint formulation (target TE = TE\*)**

`h*_TE = (TE* / √(α' V^(-1) α)) V^(-1) α`

**Bayesian (Black–Litterman) expected return**

`E[R_BL] = [(τ Σ)^(-1) + P^(-1)]^(-1) [(τ Σ)^(-1) Π + P^(-1) Q]`

where `Π` is the equilibrium excess return, `Q` is the manager's view, `P` is the uncertainty of the view, `Σ` is the covariance, and `τ` is a scalar (typically 0.05) controlling the strength of the equilibrium prior.

**Tracking-error budget allocation across alpha sources**

`TE_i / TE_total = (h_i' V h_i) / Σ_j (h_j' V h_j)` if the alphas are uncorrelated; otherwise the more general formula uses the Cholesky decomposition.

## Mental Models

- **Construction is the solution of a mean-variance problem.** The only inputs are alpha, V, and lambda. The skill of the manager is in producing the right alpha and the right V.
- **V must be shrunk.** The raw sample covariance is dominated by estimation error; the optimal construction uses a *structured* prior (factor model, Ledoit–Wolf shrinkage, etc.).
- **Forecast uncertainty shrinks toward the benchmark.** When the manager is unsure, the optimal is to stay close to the benchmark.

## Worked Example (RECOMPUTED)

*Setup.* Two-asset portfolio, with covariance matrix `V = [[0.04, 0.01], [0.01, 0.04]]` (40% per-asset residual vol, 25% correlation). Forecast `α = [0.02, 0.01]` (2% and 1% expected residual return). Risk aversion `λ = 4`.

*Step 1 — Unconstrained optimal*:
- `V^(-1) = (1/(0.04² − 0.01²)) × [[0.04, −0.01], [−0.01, 0.04]]`
- `det = 0.0016 − 0.0001 = 0.0015`
- `V^(-1) = (1/0.0015) × [[0.04, −0.01], [−0.01, 0.04]] ≈ [[26.67, −6.67], [−6.67, 26.67]]`
- `h* = (1/4) × V^(-1) × α = 0.25 × [[26.67, −6.67], [−6.67, 26.67]] × [0.02, 0.01]`
- `h* = 0.25 × [26.67×0.02 − 6.67×0.01, −6.67×0.02 + 26.67×0.01]`
- `h* = 0.25 × [0.5334 − 0.0667, −0.1334 + 0.2667]`
- `h* = 0.25 × [0.4667, 0.1333]`
- `h* = [0.1167, 0.0333]`

*Step 2 — IR of the construction*:
- `IR² = α' V^(-1) α = [0.02, 0.01] × [[26.67, −6.67], [−6.67, 26.67]] × [0.02, 0.01]`
- `= [0.02, 0.01] × [0.4667, 0.1333] = 0.02×0.4667 + 0.01×0.1333 = 0.00933 + 0.00133 = 0.01067`
- `IR = √0.01067 = 0.1033`

So the manager has an IR of ~0.10. To earn 1% alpha with 10% TE, you need this IR. To earn 1% with 5% TE, you need IR = 0.20.

*Step 3 — With forecast uncertainty*.
- Suppose `P = diag(0.0004, 0.0001)` (the manager is uncertain about both forecasts).
- `(V + P)^(-1)`: a quick solve gives weights smaller than `h*` because the manager down-weights the high-uncertainty assets.

*Sanity check (Python).*
```python
import numpy as np
V = np.array([[0.04, 0.01], [0.01, 0.04]])
alpha = np.array([0.02, 0.01])
lam = 4
h = (1/lam) * np.linalg.inv(V) @ alpha
print("h* =", h.round(4))               # -> [0.1167, 0.0333]
IR2 = alpha @ np.linalg.inv(V) @ alpha
print("IR  =", round(IR2**0.5, 4))      # -> 0.1033

# With forecast uncertainty
P = np.diag([0.0004, 0.0001])
h_CE = (1/lam) * np.linalg.inv(V + P) @ alpha
print("h*_CE =", h_CE.round(4))         # smaller, more conservative
```

## Anti-patterns

- **Using the sample covariance matrix without shrinkage.** The sample `V` is dominated by estimation error; the optimal `h` will be wildly over-fit to noise.
- **Trusting the manager's alpha at face value.** The certainty-equivalent `V + P` formula is the only honest version; without it, the construction is over-confident.
- **Setting `λ` from a target TE without ensuring `α` is well-estimated.** A high TE with a noisy alpha is a guaranteed disappointment.
- **Forgetting the residualisation step.** The alpha must be expressed in *residual* (benchmark-relative) terms; using total-return alpha leads to double-counting of factor exposure.

## Practitioner Notes

- **2026 update.** Construction in modern practice is dominated by **Black–Litterman** and its descendants (Idzorek 2005, Meucci 2010 "Fully Flexible Views"). The naïve `V^(-1) α` of the 1999 book is rarely used; the certainty-equivalent version `(V+P)^(-1) α` is the institutional default.
- **Factor risk models.** Barra (now MSCI Barra), Axioma (now part of Qontigo), and internal factor models provide `V` and `P` for institutions. The agent should use a factor model for `V`; the Ledoit–Wolf shrinkage of the sample covariance is a fallback when no factor model is available.
- **Constraints.** The unconstrained `h*` is rarely implementable — long-only, sector neutrality, turnover limits, factor neutrality, ESG constraints all push the solution away from the unconstrained optimum. Modern construction uses a constrained optimiser (cvxpy, MOSEK, Gurobi).

## Key Takeaways

1. The optimal active portfolio is `h* = (1/λ) V^(-1) α` in the unconstrained case; `(1/λ) (V+P)^(-1) α` under forecast uncertainty.
2. The **value-added** at the optimum is `0.5 IR² / λ`; the IR² is the *quality* of the construction.
3. **V must be shrunk**; the sample covariance is unfit for production.
4. **P must be estimated honestly**; the most common error is under-estimating it.
5. Construction is the *math* of the manager's view; the *judgment* of the manager is in α, V, and P.

## Connects To

- **ch10–11**: α comes from forecasting.
- **ch12**: the IC of the signal determines the achievable IR; construction cannot do better than the IC allows.
- **ch16**: the cost of the construction is the cost of the trading that implements it.
- **ch17**: the performance analysis decomposes the realised return into the contributions of the construction.
- **`lopez-de-prado-afml` ch16 (Machine Learning Asset Allocation)**: the modern extension of the construction problem to ML-derived signals.
- **`cfa-portfolio-management` R26–27**: institutional portfolio construction.
