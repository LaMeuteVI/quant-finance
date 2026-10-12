# Chapter 18: Asset Allocation

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 18, pp. 517–539

## Core Idea

Asset allocation in the residual framework is the **active decision** to tilt the portfolio away from the benchmark's *factor exposures*. The chapter develops the active bet as the deviation from the benchmark factor exposures, with the **asset allocation effect** as the contribution of the tilt to the realised return. The framework is the foundation of multi-asset active management.

## Frameworks Introduced

- **Active factor exposure (the active bet on factors)**:
  - `b_active = b_portfolio − b_benchmark`. The deviation of the portfolio's factor exposures from the benchmark's.
  - The active bet on a factor `k` is `b_k,active = Σ_i (w_i,P − w_i,B) × β_{i,k}`.
  - *When to use*: as the operational definition of asset allocation in the residual framework.
  - *Why it works*: separates the manager's view on *which factors to harvest* from the manager's view on *which individual assets to overweight*.

- **The value-added of active factor bets**:
  - `VA = (1/2) × λ'_active × V_FF^(-1) × λ_active`, where `λ_active` is the vector of active factor premia forecasts and `V_FF` is the covariance of factor premia.
  - *Why it matters*: the value-added of asset allocation is the value-added of the *factor bet*, not the value-added of the individual security bet.

- **The interaction of asset allocation and security selection**:
  - A good asset allocation decision can be undermined by poor security selection, and vice versa.
  - The optimal portfolio maximises the *sum* of the two value-added terms.

## Key Concepts

1. **Active factor exposure** — the deviation of the portfolio's factor loadings from the benchmark's.
2. **Asset allocation effect** — the contribution of active factor bets to the realised active return.
3. **Security selection effect** — the contribution of active security bets *within* each factor exposure.
4. **Factor premium forecast** — the manager's view on the future premium of each factor.
5. **Multi-asset active management** — the combination of asset allocation (across asset classes) and security selection (within asset classes).

## Worked Example (RECOMPUTED)

*Setup.* A US equity portfolio with benchmark factor exposures `b_B = [1.0, 0.2, 0.0]` (market, size, value). The manager's portfolio has `b_P = [1.05, 0.30, 0.10]`. The factor premium forecasts are `λ = [0.06, 0.02, 0.04]`. The factor covariance `V_FF = [[0.04, 0.005, 0.002], [0.005, 0.01, 0.001], [0.002, 0.001, 0.01]]`.

*Step 1 — Active factor exposure*:
- `b_active = [0.05, 0.10, 0.10]`.

*Step 2 — Value-added*:
- `VA = 0.5 × [0.05, 0.10, 0.10] × V_FF^(-1) × [0.05, 0.10, 0.10]`.
- Computing the inverse of `V_FF` and the resulting quadratic form is left to the agent (a 3×3 matrix).

*Step 3 — Interpretation*:
- The active bet is *overweight* all three factors. The market bet (+0.05) gives a small directional tilt; the size bet (+0.10) and value bet (+0.10) are the *active* views.

## Key Takeaways

1. **Asset allocation is the active bet on factor exposures.**
2. The **value-added of asset allocation** is the quadratic form in the active factor premia and the factor covariance.
3. **Security selection and asset allocation are complementary**, not substitutable.
4. The multi-asset active manager must combine the two decisions in a single optimisation.
