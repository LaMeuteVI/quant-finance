# Chapter 8: Valuation in Theory

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 8, pp. 199–223 (Part Two: Expected Returns and Valuation)

## Core Idea

Valuation is the discipline of producing a **consensus expected return vector** for every asset. The consensus is the *anchor* against which every active view is a deviation; without it there is no way to measure how unusual a forecast is. Grinold & Kahn place valuation in a unified factor-APT framework in which consensus expected returns are linear in factor premia and in factor loadings, with no estimation noise. The result is a clear separation: **expected returns come from valuation (the factor model); residual alpha is what active management adds.**

The fundamental law will reappear in ch11 with the time series of forecasts; this chapter is the **static equilibrium** view that gives the consensus its shape.

## Frameworks Introduced

- **The Factor Valuation Equation (the APT pricing equation)**: the consensus expected return is a linear function of factor loadings and factor premia.
  - *Formulation*: `E[R_i] = R_f + Σ_k β_{i,k} · λ_k` where `λ_k` is the risk premium of factor `k`.
  - *When to use*: as the canonical expression of the consensus, and as the starting point for any deviation (alpha).
  - *How*: (1) choose the factor model (the k factors); (2) estimate each `λ_k` (historical, fundamental, or implied); (3) read the consensus expected return for every asset from `R_f + β·λ`.
  - *Why it works*: the consensus must be **investible** — there must exist a portfolio that earns it. The factor structure guarantees investibility: a long-short factor portfolio can be constructed to harvest each `λ_k`.
  - *Failure mode*: the chosen factors do not span the cross-section; the resulting consensus is mispriced (and the "alpha" of an optimizer will be artifacts of model error rather than information).

- **Equilibrium ≠ Investment Process**: the consensus is the equilibrium expected return. The investment process uses an *active* view to tilt the portfolio away from the benchmark.
  - *When to use*: as a sanity check on any active strategy — does it have a *story* about why the consensus is wrong? If not, it is noise.

- **The Macroeconomic View**: premia arise from consumption and labor risks; in this view the *number* of factors equals the number of stochastic discount factor components.
  - *Why it matters*: determines the dimension of the consensus and the maximum possible IC.
  - *Failure mode*: using many factors when only a few carry risk premium inflates estimation noise.

- **The Fundamental (Bodie–Ross) View**: the consensus comes from **long-run discounted cash flow**; premia are the rates of return required by the long-run investor.
  - *When to use*: when cross-sectional premia must be made consistent with long-run growth assumptions.
  - *Failure mode*: the long-run DCF requires projections of cash flow decades into the future, which are themselves noisy.

- **The two views must agree**: the **consistency principle**. A consensus is only acceptable if the factor premia line up with the long-run DCF.
  - *Why it works*: it is a global sanity check — if your consensus implies equities should compound at 4% but DCF says 9%, one of them is wrong.

## Key Concepts

1. **Consensus expected return** — the cross-section of expected returns; the *center of the world* against which alpha is measured.
2. **APT pricing** — the multi-factor extension of CAPM; the consensus is linear in factor loadings.
3. **Risk premium `λ_k`** — the expected return of the factor-mimicking portfolio for factor `k` in excess of the risk-free rate.
4. **Factor-mimicking portfolio** — a tradable portfolio whose returns are perfectly correlated with one factor and uncorrelated with the others; the way to invest in a factor.
5. **Investibility constraint** — the consensus must correspond to a portfolio an investor can actually hold; the benchmark portfolio must be on the efficient frontier of the chosen factors.
6. **Macro view** — premia derive from aggregate consumption and labor risks (Cochrane-style).
7. **Fundamental view** — premia derive from long-run DCF projections of dividend streams.
8. **Active return** = realised return − consensus expected return; the random walk component is the consensus + a noise term, the alpha is a residual forecast.
9. **The random walk "benchmark" expected return** — when there is no information, the best consensus is the realised average return.
10. **Residual alpha** — the deviation of a manager's return forecast from the consensus; the active bet.
11. **Cross-section vs. time-series** — the consensus in a single snapshot vs. how the consensus evolves.

## Formulas & Reference Tables

**The valuation equation (linear, no estimation noise)**

`E[R_i] = R_f + Σ_k β_{i,k} λ_k`

For a portfolio with exposures `b = (b_1, …, b_K)` to the K factors:

`E[R_P] = R_f + b' λ`, where `b_k = Σ_i w_i β_{i,k}` and `w_i` are portfolio weights.

**Equilibrium and CAPM as a one-factor special case**

`E[R_i] = R_f + β_i (E[R_M] − R_f)`, where the single factor is the market and `λ_1 = E[R_M] − R_f`.

**The active view (residual alpha)**

`α_i = r̂_i − E[R_i]`, where `r̂_i` is the manager's **forecast** of the return of asset `i`, and `E[R_i]` is the consensus.

**The investibility constraint**

The benchmark portfolio `M` must be a factor portfolio; equivalently, every asset's expected return must be expressible as a linear function of the consensus factors.

**Consistency of macro and fundamental views**

If `λ` is the vector of premia from the macro view, then the long-run DCF of the market `M` must satisfy

`R_f + λ_M = DCF_{M,long-run}`,

where `λ_M = b'_M λ` is the benchmark's premium. Both sides must be reconciled; otherwise the consensus is internally inconsistent.

## Mental Models

- **Use the factor view when** you have a small number of well-measured factors and the cross-section is large; this is the standard institutional case.
- **Use the fundamental (DCF) view when** you must justify the level of expected returns to a client; the macro view alone is too abstract.
- **Always check consistency** between the two views; the consensus is wrong if they disagree.
- **The active view is a deviation from the consensus**, not from zero — the *direction* of the bet is alpha relative to a sensible zero, not raw return.

## Worked Example (RECOMPUTED)

*Setup*. Three assets with exposures to a single market factor: `β = [1.0, 1.5, 0.5]`. Risk-free `R_f = 2%`. Factor premium `λ = (E[R_M] − R_f) = 6%`.

*Step 1 — Consensus expected returns (CAPM)*.
- `E[R_1] = 2% + 1.0 × 6% = 8%`
- `E[R_2] = 2% + 1.5 × 6% = 11%`
- `E[R_3] = 2% + 0.5 × 6% = 5%`

*Step 2 — An active view*. The manager forecasts `r̂ = [9%, 9%, 8%]`.

*Step 3 — The alpha* (deviation from consensus).
- `α_1 = 9% − 8% = +1%`
- `α_2 = 9% − 11% = −2%` (bearish relative to consensus)
- `α_3 = 8% − 5% = +3%`

*Step 4 — Interpretation*. The manager is *bullish* asset 3 vs the consensus, *bearish* asset 2, and slightly bullish asset 1. The vector `α` is the active bet; the investment process must translate it into optimal portfolio weights.

*Sanity check (recomputation in Python is expected of any agent using this skill)*:
```python
import numpy as np
Rf, lam = 0.02, 0.06
beta = np.array([1.0, 1.5, 0.5])
consensus = Rf + beta * lam
forecast  = np.array([0.09, 0.09, 0.08])
alpha     = forecast - consensus
print("Consensus:", consensus.round(4))
print("Alpha    :", alpha.round(4))
# -> Consensus: [0.08 0.11 0.05]
# -> Alpha    : [ 0.01 -0.02  0.03]
```

## Anti-patterns

- **Confusing alpha with absolute return.** Alpha is a deviation from a *consensus*, not from zero.
- **Using zero as the consensus.** A zero expected return consensus makes every active view look like alpha; it also makes the "alpha" of any optimizer a function of estimation error.
- **Letting the consensus drift.** If the consensus is updated with stale data, every subsequent alpha is contaminated.
- **Ignoring the consistency principle.** A consensus that disagrees with long-run DCF is a future source of large tracking error.

## Practitioner Notes

- **2026 update.** The factor consensus in this 1999 book uses 1–3 factors. Modern practice (Barra, Axioma, MSCI) uses 30–80 risk factors; the consensus typically adds a multi-factor model on top of a CAPM core. The same structure (consensus → factor premia → investibility) holds; only the dimensionality has grown.
- **Multi-factor consensus and a single IC.** When the consensus has many factors, the *single IC* of any signal against the consensus is mechanically depressed; the formula `IR = IC × √B` still applies, but `IC` must be re-measured with the more complex benchmark in mind.
- **ESG as a factor.** ESG-driven premia are now part of standard institutional consensus (MSCI ESG Leaders, Bloomberg ESG-weighted). The consistency check between the consensus factor premia and long-run DCF of a portfolio must include the ESG factor; otherwise the consensus is internally inconsistent.

## Key Takeaways

1. The consensus is a **linear factor model of expected returns**; the active view is the deviation.
2. Consensus and DCF must agree; the consistency check is a global sanity test.
3. **The consensus must be investible**: the benchmark must be on the efficient frontier of the chosen factors.
4. **Active return is the deviation from the consensus, not from zero**.
5. The factor model sets the dimensionality of the consensus and the maximum possible IC of any active strategy.

## Connects To

- **ch01**: the four-stage process starts here — the consensus defines the input to stage 1 (information).
- **ch07**: the APT framework of this chapter is the multi-factor extension of CAPM.
- **ch09**: ch09 turns the theory of ch08 into practical factor portfolios and the investibility of consensus premia.
- **`hull-derivatives` ch04 (Interest Rates), ch11 (Correlations)**: the consensus's factor covariance matrix is the risk model; Hull ch11 covers correlation/copula estimation.
- **`cfa-asset-allocation-cme` Reading 25–28**: building blocks of the capital market expectations framework used here as "consensus".
