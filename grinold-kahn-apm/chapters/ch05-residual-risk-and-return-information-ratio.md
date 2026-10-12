# Chapter 5: Residual Risk and Return — The Information Ratio

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 5, pp. 109–140

## Core Idea

The **Information Ratio** is the central construct of active management: expected annual **residual** return divided by annual **residual** risk. It is *not* a Sharpe ratio. The ex post IR measures achievement; the ex ante IR measures *opportunity*, and the ex ante version is a **budget constraint** on the active manager — the **residual frontier**, a straight line through the origin in (`α_P`, `ω_P`) space. Given the frontier, the manager's aggressiveness is set by residual risk aversion, giving the simple pair of results `ω* = IR/(2λ_R)` and `VA* = IR²/(4λ_R)`. Because value added scales with the **square** of the IR, skill is worth far more than scale — and the next chapter shows why.

## Learning Outcomes Covered

- Define IR on **residual** (benchmark-orthogonal) return and risk, and contrast it explicitly with the Sharpe ratio.
- Distinguish ex post IR (achievement) from ex ante IR (opportunity), and read the IR off an alpha regression's `t`-statistic.
- Compute the characteristic portfolio A and prove its properties: `β_A = 0`, it attains the maximum IR, and its residual risk is `1/IR`.
- Use the residual frontier as a budget constraint and derive optimal residual risk and optimal value added.
- Calibrate a plausible ex ante IR from institutional targets (5–6% residual risk, 3–4% expected residual return ⇒ IR ≈ 0.64) rather than from wishful thinking.
- Read the empirical IR and active-risk distributions and know the fees/estimation-error caveats.
- Forecast alphas directly (binning) instead of forecasting expected returns and backing out alpha.

## Frameworks Introduced

- **The Information Ratio (the "can opener")**:
  `IR = α_P / ω_P` for a portfolio with `ω_P > 0`; `IR_P = 0` by convention if `ω_P = 0`.
  - *Ex post*: realized annual residual return ÷ annual residual risk. Treynor & Black (1973) call it the **appraisal ratio**. It can and frequently is **negative**.
  - *Ex ante*: the **highest** attainable ratio of annual residual return to residual risk over all portfolios — i.e. the IR of the portfolio optimized to your alphas. It "defines the residual frontier, the opportunities available to the active manager."
  - **Relation to the regression `t`-statistic**: if the alpha regression in Eq. 5.1 covers `Y` years, `IR ≈ t_α / √Y`. This is the bridge from a backtest regression to an IR estimate.
  - **⚠ Not a Sharpe ratio.** `SR = f_P/σ_P` (total excess return ÷ total risk); `IR = α_P/ω_P` (residual return ÷ residual risk). For a benchmark-relative mandate, `IR` is the correct metric and `SR` measures total risk-taking. A manager can have a poor IR and a high SR by simply levering beta; that is not skill.

- **The Characteristic Portfolio of Alpha (portfolio A)**: `h_A ∝ V⁻¹α`, where `V` is the covariance matrix.
  - *Properties* (from the technical appendix): (1) `β_A = 0` — typically long/short; (2) A has the **maximum** IR of any portfolio; (3) `σ_A = ω_A = 1/IR`; (4) any `P = B + κ·A` has `IR_P = IR`; (5) the maximum-Sharpe fully invested portfolio `Q` is a mixture of benchmark and A, so **`IR_Q = IR`**; (7) `IR_P = θ_P/ω_P` where `θ_P` is the residual return; (8) `IR = α'V⁻¹α`, and the benchmark's Sharpe ratio is `(IR·α)/σ_B`; (9) **`α = IR · MCRR_Q`**, i.e. `α_n = IR · Cov{θ_Q, θ_n}/ω_Q`.
  - **Practical validation duty**: because alpha is proportional to the *marginal contribution to residual risk* with constant `IR`, **half the marginal residual-risk contributions should equal the alphas of a manager with IR = 0.5.** Always run this check, especially on hand-built portfolios.

- **The Residual Frontier (budget constraint)**:
  `α_P / ω_P ≤ IR`, a line through the origin. `P*` is the tangency point with the value-added indifference curve.
  - *Interpretation*: along the frontier the manager can only buy residual return with residual risk. Any point *below* the frontier is a worse manager.
  - *Two frontiers coexist*: the fully-invested efficient frontier (from C through Q) and the **β = 1 frontier** (from B through P). Portfolios that dominate the β = 1 frontier exist but carry large active risk and therefore **business risk of poor relative performance**. The β = 1 frontier starts at the benchmark, which is the *minimum-risk portfolio with β = 1* (zero residual risk). Adding a **no-active-cash** restriction turns it into a parabola centered on the benchmark — "a constraint reduces our opportunities."

- **Aggressiveness Rule and Value-Added Rule**:
  `ω* = IR/(2λ_R)` and `VA* = IR²/(4λ_R)`.
  - Doubling IR doubles optimal residual risk. Doubling risk aversion halves it.
  - Value added grows with the **square** of IR. **Every investor, at any risk tolerance, seeks the strategy or manager with the highest IR.** Investors differ *only* in implementation aggressiveness.
  - *Sanity check on any proposed (IR, λ_R) pair*: compute `ω*` from `Eq. 5.10` and ask whether the resulting tracking error is something the business can accept. A "conservative" (IR = 0.50, λ_R = 0.15) pair yields `ω* = 1.67%` and `VA = 42 bp` — "probably not enough value to justify an active fee."

- **IR Classification Scale (used throughout the book)**: `IR = 0.5` **good** (top quartile); `IR = 0.75` **very good**; `IR = 1.0` **exceptional**.
- **Forecast Alphas Directly (binning)**: sort assets into five bins — strong buy / buy / hold / sell / strong sell — assign alphas `+2% / +1% / 0% / −1% / −2%`, compute the benchmark-weighted average alpha, and if it is not zero, subtract `benchmark_avg_alpha × β_i` from each alpha. The result is benchmark-neutral and, absent constraints, leads to a portfolio with beta 1.00.
  - *Why it works*: it avoids forecasting quantities (like the benchmark excess return) that will not influence the portfolio. **Alpha is what the optimizer consumes; forecasting expected returns and inverting is a lossy detour.**

## Key Concepts

1. **Ex post IR** — realized achievement; can be negative; `IR = realized annual residual return / annual residual risk`. Example from the text: `2.3%/3.45% = 0.67`, or `(−1.7%)/3.45% = −0.49`.
2. **Ex ante IR** — the opportunity; the maximum over all portfolios of `α_P/ω_P`.
3. **Residual frontier** — the line `α_P = IR·ω_P`; the manager's budget constraint.
4. **Characteristic portfolio A** — `V⁻¹α`; zero beta, maximum IR, residual risk `1/IR`.
5. **Alpha ↔ marginal residual risk** — `α_n = IR · MCRR_Q(n)`. The single best portfolio diagnostic in the book.
6. **Residual risk aversion `λ_R`** — willingness to trade residual risk for residual return; aggressive 0.05, moderate 0.10, restrained 0.15.
7. **Value added `VA*`** — `IR²/(4λ_R)`; the risk-adjusted residual return of the optimal portfolio, also called the certainty-equivalent residual return.
8. **The zero alpha identity** — since the benchmark is the characteristic portfolio of beta, `α_B = 0`; cash also has `α = 0`; so **any mixture of benchmark and cash has zero alpha.**
9. **Horizon scaling of IR** — expected return grows linearly in horizon, risk as `√T`, so **`IR` grows as `√T`**. Quarterly IR = annual IR / 2; monthly IR = annual IR / `√12`.
10. **Independence of IR from aggressiveness** — scaling active holdings by `φ` scales alpha and residual risk by `φ`; the ratio is unchanged. (This breaks with constraints — notably no-short constraints; see ch15.)
11. **Estimation error broadens the distribution** — with 300 funds of true IR = 0, the sample IR distribution centers on 0 but only shrinks toward zero as the observation period lengthens. Quarterly-return institutional data makes this worse.
12. **Empirical IR by asset class and fee level** — equity top quartile `0.63–0.78` before fees, `0.48–0.58` after. Bond top quartile `0.50–0.89` before fees; the after-fee bond numbers are *strikingly* worse than equity (median after-fee `−0.86` for mutual funds), see Kahn (1998).

## Formulas & Reference Tables

**Alpha regression (the definition of ex post alpha)**

`r_P(t) = α_P + β_P·r_B(t) + ε_P(t)`, `E[ε_P(t)] = 0`, residuals `θ_P(t) = r_P(t) − β_P·r_B(t) − α_P`

**Information ratio**

`IR_P = α_P / ω_P` for `ω_P > 0`; `IR_P = 0` if `ω_P = 0`
`IR = max over all P of (α_P/ω_P)`
`IR = α'V⁻¹α` (portfolio A's residual risk is `ω_A = 1/IR`)

**IR from the regression `t`-statistic**

`IR ≈ t_α / √Y` where `Y` = number of years in the regression

**Alpha ↔ marginal residual risk (the validation identity)**

`α_n = IR · MCRR_Q(n)`, `MCRR_Q(n) = Cov{θ_Q, θ_n}/ω_Q`

**Residual frontier (budget constraint)**

`α_P/ω_P ≤ IR`

**Value-added objective and optimal solution**

`VA = α_P − (λ_R/2)·ω_P²`
`ω* = IR/(2λ_R)`
`VA* = IR²/(4λ_R)`

**Optimal portfolio holdings (Proposition 2)**

`h_P = h_B + β_P·(α − β·µ_B)/λ_R + [1/ω_A]·(V⁻¹α)/(1/ω_A)` — the residual portfolio is proportional to portfolio A, scaled by `α_P`.

**Table 5.1 — Generic ex ante IR distribution (before fees)**

| Percentile | IR |
|---|---|
| 90 | 1.0 |
| 75 | 0.5 |
| 50 | 0.0 |
| 25 | −0.5 |
| 10 | −1.0 |

Symmetric around zero — consistent with active management as a zero-sum game.

**Table 5.3 — Optimal residual risk `ω* = IR/(2λ_R)`**

| | `λ_R` aggressive 0.05 | moderate 0.10 | restrained 0.15 |
|---|---|---|---|
| Exceptional `IR` 1.00 | 10.00% | 5.00% | 3.33% |
| Very good `IR` 0.75 | 7.50% | 3.75% | 2.50% |
| Good `IR` 0.50 | 5.00% | 2.50% | 1.67% |

**Table 5.4 — Optimal value added `VA* = IR²/(4λ_R)`**

| | 0.05 | 0.10 | 0.15 |
|---|---|---|---|
| `IR` 1.00 | 5.00% | 2.50% | 1.67% |
| `IR` 0.75 | 2.81% | 1.41% | 0.94% |
| `IR` 0.50 | 1.25% | 0.63% | 0.42% |

**Table 5.2 — IR is scale-invariant (4 stocks, 25% benchmark weights)**

| | α | Benchmark w | P total | P active | L total | L active |
|---|---|---|---|---|---|---|
| Stock 1 | 1.50% | 25.00% | 35.00% | +10.00% | 40.00% | +15.00% |
| Stock 2 | −2.00% | 25.00% | 10.00% | −15.00% | 2.50% | −22.50% |
| Stock 3 | 1.75% | 25.00% | 40.00% | +15.00% | 47.50% | +22.50% |
| Stock 4 | −1.25% | 25.00% | 15.00% | −10.00% | 10.00% | −15.00% |

L's active holdings are exactly 1.5× P's, so alpha and residual risk are both 1.5× and IR is unchanged.

**Table 5.8 — Annual active risk, U.S. active equity**

| Percentile | Mutual funds | Institutional portfolios |
|---|---|---|
| 90 | 9.87% | 9.49% |
| 75 | 7.00% | 6.47% |
| 50 | 4.76% | 4.39% |
| 25 | 3.66% | 2.85% |
| 10 | 2.90% | 1.93% |

**Table 5.9 — Annual active risk, U.S. active bonds**

| Percentile | Mutual funds | Institutional portfolios |
|---|---|---|
| 90 | 3.44% | 1.89% |
| 75 | 2.01% | 0.98% |
| 50 | 1.33% | 0.61% |
| 25 | 0.96% | 0.41% |
| 10 | 0.74% | 0.26% |

**Table 5.7 — Information ratios, U.S. active bonds**

| Percentile | MF before fees | MF after fees | Inst. before fees | Inst. after fees |
|---|---|---|---|---|
| 90 | 1.14 | 0.50 | 1.81 | 1.29 |
| 75 | 0.50 | −0.22 | 0.89 | 0.38 |
| 50 | −0.11 | −0.86 | 0.01 | −0.57 |
| 25 | −0.61 | −1.50 | −0.62 | −1.37 |
| 10 | −1.22 | −2.21 | −1.50 | −2.41 |

## Mental Models

1. **"The IR is a budget, not a score."** Once you have a defensible IR, your job is to find the tangency point on your frontier, not to chase a higher realized number. Opportunity and aggressiveness are separate decisions.
2. **"Squaring means skill beats scale."** `VA ∝ IR²`. Going from IR 0.5 to 0.75 is a 2.25× increase in value added; the same money spent doubling the portfolio size with the same IR adds zero.
3. **"Check `α_n = IR × MCRR_Q(n)` before you ship."** A hand-built portfolio that violates this proportionality has a construction error, not an edge.
4. **"Every client picks the highest IR; only implementation differs."** Sell strategy, not tracking error. Two managers with IR 0.75 and `λ_R` of 0.05 vs 0.15 offer the same opportunity at 7.5% vs 2.5% residual risk.
5. **"Short horizons shrink IR by `√T`."** A quarterly IR of 0.20 is an annual IR of 0.40. Always annualize before comparing anything.

## Code Examples

```python
# ⚠ reconstructed — the Information Ratio is RESIDUAL, not Sharpe
import numpy as np

def information_ratio(r_P, r_B):
    """r_P, r_B: arrays of PERIODIC EXCESS returns."""
    r_P = np.asarray(r_P, float); r_B = np.asarray(r_B, float)
    beta = np.cov(r_P, r_B, ddof=1)[0, 1] / np.var(r_B, ddof=1)
    theta = r_P - beta * r_B                 # residual return
    alpha = theta.mean()                     # per-period alpha
    omega = theta.std(ddof=1)                # per-period residual risk
    return alpha / omega, alpha, omega, beta

def sharpe(r_P, r_f=0.0):
    r_P = np.asarray(r_P, float)
    return r_P.mean() / r_P.std(ddof=1)

def ir_from_tstat(t_alpha, years):
    """IR ~= t_alpha / sqrt(Y). Works because IR grows as sqrt(horizon)."""
    return t_alpha / np.sqrt(years)

rng = np.random.default_rng(7)
r_B = rng.normal(0.01, 0.04, 60)
# a manager with true residual alpha = +0.10%/mo, residual sd = 4%/mo
r_P = 1.0*r_B + np.concatenate([[0.001], rng.normal(0, 0.04, 59)])
ir, a, w, b = information_ratio(r_P, r_B)
print(f"IR={ir:.3f} alpha={a:.4f} omega={w:.4f} beta={b:.3f} SR={sharpe(r_P):.3f}")
print("annualised IR (x sqrt(12)):", ir*np.sqrt(12))
```

```python
# ⚠ reconstructed — omega*, VA*, and the validation identity
import numpy as np

def optimal_residual_risk(IR, lam_R):
    return IR / (2 * lam_R)

def optimal_value_added(IR, lam_R):
    return IR**2 / (4 * lam_R)

def implied_risk_aversion(IR, omega):
    return IR / (2 * omega)

print("IR=0.60, lamR=0.12 ->", optimal_residual_risk(0.60,0.12), optimal_value_added(0.60,0.12))
print("IR=0.50 -> lamR for 4% tracking error:", implied_risk_aversion(0.50, 0.04))

def check_alpha_vs_mcrr(alpha, mcrr_Q, IR):
    """The book's Proposition 9: alpha_n = IR * MCRR_Q(n)"""
    return np.allclose(alpha, IR * mcrr_Q, atol=1e-12)
```

```python
# ⚠ reconstructed — the alpha-bin forecasting recipe
import numpy as np

def bin_alphas(ranks, betas, b_weights, bin_alphas=(0.02,0.01,0.0,-0.01,-0.02)):
    """ranks: 0=strong buy ... 4=strong sell; b_weights: benchmark weights"""
    a = np.asarray(bin_alphas, float)[np.asarray(ranks, int)]
    b_avg = float(np.asarray(a, float) @ np.asarray(b_weights, float))
    return a - b_avg * np.asarray(betas, float)      # benchmark-neutral alphas
```

## Worked Example

**Table 5.2, recomputed — alpha from active holdings only.**
`α_P = 0.10(1.50%) + (−0.15)(−2.00%) + 0.15(1.75%) + (−0.10)(−1.25%)`
`= 0.150% + 0.300% + 0.2625% + 0.125% = `**0.8375%** (≈ 0.84%).

For portfolio L, active holdings are 1.5× P's, so `α_L = 1.5 × 0.8375% = `**1.2563%**, and residual risk is also 1.5× (`3.06%` from `2.04%`), leaving `IR` unchanged. **This is the formal statement that IR is invariant to aggressiveness.**

**Problems 4–6, recomputed — the cost of a wrong IR.**

*Problem 4:* `λ_R = 0.12`, `IR = 0.60`.
`ω* = 0.60/(2×0.12) = `**2.50%**
`VA* = 0.60²/(4×0.12) = 0.36/0.48 = `**0.75%**

*Problem 5 (the IR is really 0.30, risk left at 2.50%):*
Correct optimum: `ω* = 0.30/(2×0.12) = 1.25%`, `VA* = 0.09/0.48 = `**0.1875%**.
Value actually earned at 2.50% risk: `α = IR·ω = 0.30 × 2.50 = 0.75%`; penalty `= (0.12/2)(2.50)² = 0.375%`; `VA = 0.75 − 0.375 = `**0.375%**.
**Value lost by using the wrong IR: `0.375 − 0.1875 = `**0.1875% (18.75 bp per year)** — a 25% reduction in value added. Overestimating your skill does not merely fail to help; it destroys value by levering risk into a lower-`IR` portfolio.

*Problem 6:* `IR = 0.50`, target `ω = 4%` ⇒ `λ_R = 0.50/(2×4) = `**0.0625** — between "aggressive" (0.05) and "moderate" (0.10).

**Problem 2, recomputed — IR needed for a 2.5% risk-adjusted return at `λ_R = 0.10`.**
`VA* = IR²/(4λ_R) ⇒ IR = √(0.025 × 0.40) = √0.010 = `**0.10**
`ω* = 0.10/(2×0.10) = `**0.50% active risk**
**Interpretation:** a 2.5% risk-adjusted return is essentially unattainable — it would require only 50 bp of tracking error. The frontier is the binding constraint, not the preference curve. This is the "life is a bit like that" case the text illustrates (the `VA = 2.5%` indifference curve lies *above* the IR = 0.75 residual frontier).

**Problem 3, recomputed — MMI portfolios vs. B (`f_B = 6%`; f_B assumed = 6% as the source's `f_Q = 6%` is the only forecast given).**

| Portfolio | `f` | α (= `f − β_B·f_B`) | `ω` | SR | IR |
|---|---|---|---|---|---|
| **B** (benchmark) | 6.00% | 6.00 − 1.000×6.00 = **0.00%** | `√(15.50² − 15.50²)` = **0.00%** | 6.00/15.50 = **0.387** | **0** (by definition) |
| **Q** (MMI, `σ` 15.82%) | 6.00% | 6.00 − 1.004×6.00 = **−0.024%** | `√(15.82² − (1.004×15.50)²)` = **2.85%** | 6.00/15.82 = **0.379** | −0.024/2.85 = **−0.008** |
| **C** (min-variance) | *not given* | *not computable* | `√(14.42² − (0.865×15.50)²)` = **5.31%** | — | — |

**Interpretation:** B has zero IR and zero residual risk by construction — the passive answer. Q's IR is essentially zero (a rounding-level negative residual return on 2.85% residual risk), meaning the MMI *portfolio* added nothing beyond its benchmark. C carries 5.31% residual risk; without a forecast `f_C` its IR and SR are not determinable from the data given (not specified in source). **The residual risk ordering B < Q < C is the point: the minimum-variance portfolio is the most "active" of the three in risk terms even though it may add no value.**

## Anti-Patterns

- **Confusing IR with the Sharpe ratio.** `IR` uses residual return and residual risk; `SR` uses total excess return and total risk. A high-beta levered portfolio has a high SR and (usually) a poor IR. Reporting SR for a benchmark-relative mandate is a category error.
- **Reporting a quarterly IR against an annual benchmark.** IR scales as `√T`; annualize before any comparison.
- **Treating the ex post IR as the ex ante IR.** A realized `IR = 0.67` over two years is not evidence that your forward opportunity is 0.67 — that is precisely the persistence question, and Kahn & Rudd (1995) address it separately.
- **Over-levering because of an over-optimistic IR.** Problem 5 shows a 25% value-added loss. Overestimating skill is actively harmful, not neutral.
- **Forgetting that estimation error widens the IR distribution.** With limited history the *realized* IR distribution is wider than the true one; backtests of short history overstate skill.
- **Ignoring that the no-short constraint degrades IR.** IR's scale-invariance breaks under constraints; ch15 prices this effect explicitly.
- **Quoting the after-fee IR distribution from the wrong asset class.** Bond after-fee IRs are dramatically worse than equity; the fee/asset-class interaction is not uniform.
- **Building alphas by forecasting expected returns and inverting.** Forecast alphas directly (binning or `IC × σ_θ × score`); the detour through `µ_B` adds error you do not need.
- **Skipping the `α = IR × MCRR` check on hand-built portfolios.** It is the cheapest available bug detector in the framework.

## Practitioner Notes

- **Units discipline for `λ_R`.** `λ_R = 0.10` with returns in percent means the penalty at `ω = 5%` is `0.5 × 0.10 × 25 = 1.25%` (the text's Fig. 5.3 numbers: 3.75% / 2.5% / 1.25% for `λ_R` of 0.15 / 0.10 / 0.05). In decimals the same `λ_R` is a 10,000× different parameter. `ω*` and `VA*` are unit-dependent; the IR is not.
- **Fee arithmetic is the real business constraint.** A "good" manager at `IR = 0.50` with restrained implementation earns `VA = 42 bp`. Against a typical active fee that is negative net value. Fee-based active management requires either `IR ≥ 0.75` or a materially lower `λ_R`.
- **Validation duties**: (i) verify `α_n = IR·MCRR_Q(n)` on every portfolio, especially hand-built ones; (ii) confirm `IR ≈ t_α/√Y` on the out-of-sample regression; (iii) confirm the realized active risk falls in the peer distribution (equity median 4–5%, bond institutional median 0.61%); (iv) confirm `ω` is at or below `ω*` given your claimed IR.
- **⚠ Practitioner update (post-1999)**: the IR itself has not been superseded, but the *evidence threshold* for believing one has.
  1. **Multiple testing.** Harvey, Liu & Zhu (2016, *Review of Financial Studies*) show that of 316 published factors, the median `t`-stat on alpha is 2.8, not the ~2.0 implied by a single test at 5%. Their recommendation: require **`t > 3.0`** for a newly discovered factor to be considered significant. For an established factor on a long sample, `t > 2.0` remains defensible. Since `IR ≈ t/√Y`, a `t = 3` result over 40 years is an `IR` of only `3/√40 = 0.47` — *below* top-quartile. **The bar for believing you have a 0.5 IR is materially higher in 2026 than in 1999.**
  2. **Deflated Sharpe / probability of backtest overfitting.** López de Prado (2014, *Journal of Portfolio Management*; *Advances in Financial Machine Learning*, 2018) shows that the more variants of a strategy are tried, the higher the *observed* Sharpe of the winner purely by chance. The **Deflated Sharpe Ratio** adjusts an observed Sharpe for skewness, kurtosis, sample length and the number of trials; the **Probability of Backtest Overfitting (PBO)** via CSCV estimates the fraction of backtests that would have had in-sample IR below out-of-sample IR. Run both before capital.
  3. **Capacity is inside the IR.** The book's IR is a pure forecast/construction quantity with no capacity, crowding or price-impact term. Modern IR estimates for a strategy with capacity `C` and cost per unit of active exposure `c` should be netted: `IR_net ≈ IR_gross − c·(traded fraction)/√B`. Report gross and net IR separately.
  4. **Expected shortfall, not VaR, for tail risk.** Residual risk here is measured by `ω`, a standard deviation. Under `BCBS MAR21` (FRTB, effective 2023) the regulatory tail metric is ES at 97.5%. IR remains the right *forecasting-efficiency* metric; do not substitute ES for the denominator of IR.
  5. **Short-horizon data.** The book's quarterly-data caveat has worsened: most 1990s institutional data were quarterly; today monthly and daily data are available but the *short-horizon* IRs are `1/√12` and `1/√52` of the annual, and their estimation error dominates. Always estimate IR on a consistent, annualized basis.

## Key Takeaways

1. `IR = α_P/ω_P` — **residual** return over **residual** risk. Not a Sharpe ratio. `IR = 0` for the benchmark by construction.
2. Ex post IR = achievement; ex ante IR = opportunity; `IR ≈ t_α/√Y` connects a backtest regression to a forward IR.
3. The residual frontier `α/ω ≤ IR` is a **budget constraint**; the optimal portfolio is the tangency of a value-added parabola with the frontier.
4. `ω* = IR/(2λ_R)` and `VA* = IR²/(4λ_R)`. Value added scales with the **square** of the IR — every investor picks the highest-IR strategy and differs only in aggressiveness.
5. Portfolio A (`V⁻¹α`) has `β = 0`, maximum IR, and residual risk `1/IR`; `IR = α'V⁻¹α`; and the key diagnostic `α_n = IR·MCRR_Q(n)`.
6. IR is **scale-invariant** (scaling active weights by `φ` scales alpha and residual risk by `φ`) — until constraints bind.
7. IR scales as `√T`: quarterly IR = annual/2, monthly = annual/`√12`.
8. Realistic calibration: 5–6% residual risk and 3–4% expected residual return ⇒ `IR ≈ 0.64`; good = 0.5, very good = 0.75, exceptional = 1.0. Overstating IR destroys value — a 2× overstatement cost 18.75 bp of annual value added in Problem 5.

## Connects To

- **ch04**: supplies `α_P` and `ω_P`, the two inputs to the value-added objective that this chapter optimizes; here `λ_R` replaces the total-risk `λ_T`.
- **ch06**: derives the structure behind the IR — the **Fundamental Law** `IR = IC·√B` explains why the IR classification scale (0.5/0.75/1.0) is reachable at all, and why breadth is the lever a manager controls.
- **ch10–11**: estimating the IR's components (IC, breadth, TC) is exactly the forecasting problem; the "rule of thumb" `α = σ_θ·IC·s` is the production estimator for the alpha vector that defines portfolio A.
- **ch12**: information analysis — how to measure IC, forecast IR, and separate skill from luck in the realized IR.
- **ch15**: the no-short constraint and its quantified cost to IR, which is where scale-invariance breaks.
- **`cfasi-portfolio-construction`**: implementation of the `IR`-conditional optimal residual portfolio and the practical tracking-error ranges (equity median 4–5%).
- **`cfa-wealth-institutional-management`**: appraisal ratio / information ratio in manager selection and GIPS-consistent performance reporting.
- **`cfa-portfolio-management`**: Treynor, Black, Sharpe and Merton measures of relative performance that the IR generalizes.
