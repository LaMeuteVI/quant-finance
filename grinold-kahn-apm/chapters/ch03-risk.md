# Chapter 3: Risk

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 3, pp. 41–75

## Core Idea

Risk in active management is the **standard deviation of return**, and its cost is measured in **variance**. Standard deviation wins over semivariance, shortfall probability and value at risk not because it is philosophically superior but because it is the only candidate that is *universal, symmetric, flexible and — decisively — accurately forecastable and aggregable from assets to portfolios*. Active managers care about **active** and **residual** risk, not total risk; and active risk depends on the size of the **active position**, not the size of the benchmark position. Because historical covariance matrices are statistically hopeless for portfolios of realistic size, risk must come from **structural multi-factor models**.

## Learning Outcomes Covered

- Justify standard deviation as *the* risk measure against semivariance, shortfall probability and VaR, using forecastability and aggregation as the decisive criteria.
- Convert risk across time horizons with the `√T` rule, and state the autocorrelation assumption it rests on.
- Distinguish total risk, active risk (tracking error) and residual risk, and show that active risk scales with the *active* position, not the benchmark weight.
- Explain the two linear properties of variance (additive across assets, additive across time under zero autocorrelation) and the failure of standard deviation to be linear.
- Reject historical covariance matrices with the `T > N` argument and the sample-size arithmetic.
- Build a structural risk model: exposures, factor returns, specific returns, factor covariance `F`, specific covariance `Δ`.
- Choose factors under the **a priori** constraint and the three selection criteria: incisive, intuitive, interesting.
- Classify active risk into **inherent**, **intentional** and **incidental** bets and act on incidental bets.

## Frameworks Introduced

- **The Risk-Measure Criteria Test**: a risk measure must be universal, symmetric, flexible (works for assets and portfolios, past and future, any horizon) and accurately forecastable.
  - *When to use*: whenever choosing what to optimize — or how to *report* risk, which is a separate decision from how to *model* it.
  - *Why it fails for alternatives*: semivariance/target semivariance — ambiguous definition, half the data (statistical loss), aggregation from assets to portfolios is extremely difficult; asymmetry is unstable over time, so realized downside risk is a poor forecast of future downside risk. Shortfall probability — same problems, and worse as the target falls (extreme shortfalls informed by one or two observations). VaR — same problems plus, as the authors note elsewhere, no subadditivity.
  - *The normality trick*: **choosing how to define risk is separate from choosing how to report risk.** Assume normality and the mean and standard deviation fix semivariance, shortfall probability and VaR; then the *modelling* choice is standard deviation (asset-level, aggregable), and the *reporting* choice is any monotone transform of it.

- **Active Risk = f(active exposure, asset risk)** — the tracking-error budget must be allocated on *active* weights.
  - *Formulation*: `ψ_P² = Var(r_PA)`, computed from active weights `A_i = w_i − b_i`, active returns `r_PA = r_P − r_B`.
  - *Why it matters*: a 1% active position in a large-cap stock is **not** necessarily less risky than a 1% active position in a small-cap. Size-based position limits expressed as ±50% of benchmark weight are the wrong control; express limits in **active percentage points**.
  - *Failure mode*: liquidity may justify size-aware limits, but that is a cost argument, not a risk argument — and the two must be labelled differently.

- **The Two Linear Properties of Variance**: (1) variance adds across assets; (2) variance adds across time when returns are serially uncorrelated. **Standard deviation has neither property** — it is not a weighted average of constituent standard deviations.
  - *Consequence 1 (diversification)*: `σ_p² = w_1²σ_1² + w_2²σ_2² + 2w_1w_2ρ_12σ_1σ_2`; for a 50/50 portfolio `σ_p = σ√((1+ρ)/2)`. Equality with `0.5(σ_1+σ_2)` only at `ρ = 1`. **For risk, the whole is less than the sum of its parts.**
  - *Consequence 2 (horizon scaling)*: `σ(T) = σ_annual·√T`, so variance is linear in `T`. 5% annual active risk = 2.5% over one quarter, 10% over four years.
  - *Failure mode*: the `√T` rule silently fails under autocorrelation or volatility clustering (ARCH/E-GARCH, Bollerslev–Chou–Kroner 1992, cited by the authors). Annualized risk is a modelling convention, not a fact.

- **Elementary Risk Models and Why They Fail**:
  1. *Single-factor diagonal* — assumes residual returns uncorrelated, giving `σ_nm = β_nβ_mσ_M²` for `n≠m`, a conservative zero residual covariance.
  2. *Constant correlation* — one `ρ` for all pairs: useful for "quick and dirty" work, ignores industry linkage.
  3. *Full historical covariance* — statistically indefensible (below).
  - **Historical model failure, quantified**: an `N×N` covariance matrix needs `N(N+1)/2` independent estimates; a sample covariance from `T` periods has rank `min(N, T−1)`, so if `T ≤ N` **apparent riskless active positions exist**. For the S&P 500 that means >40 years of monthly data. Even with `T > N`: shorter windows than the forecast horizon, merger/spinoff breakage, selection bias (takeovers, LBOs, failures omitted), and sample bias — a 500-asset covariance matrix contains 125,250 independent numbers, so if 5% are poor, **6,262 are poor**.

- **Structural (Multi-Factor) Risk Model**: `r = Xb + u`, with `Cov(u, b) = 0` and `Δ` diagonal, giving `V = XFX' + Δ`.
  - *The one hard constraint*: **all factors must be a priori factors** — exposures must be known at the beginning of the period, even though factor returns are unknown.
  - *Three factor families*: **response/macro factors** (bond beta, inflation surprise, oil, FX, industrial production) — three defects: errors-in-variables from per-stock regressions (a 9-factor model on 1000 stocks = 1000 monthly regressions of 9 coefficients from ~60 months), nonstationarity, poor-quality government data. **Cross-sectional factors** (fundamental: dividend/earnings yield, analyst forecasts; market: historical volatility, past return, implied vol, turnover) — the authors' preferred family: *"In our experience, these cross-sectional comparisons are quite powerful factors."* **Statistical factors** (PCA, maximum likelihood, EM) — *factor ex machina*; avoided because they are hard to interpret, prone to spurious correlation, and assume constant exposures, so they **cannot capture momentum**.
  - *Three selection criteria*: **incisive** (distinguishes returns — low- vs high-vol stocks differ at least three times per year), **intuitive** (recognizable dimensions with credible stories), **interesting** (explains part of performance; e.g. large caps did well ⇒ size exposure worked).
  - *Risk index vs. descriptor*: broad categories (volatility, momentum, size, liquidity, growth, value, earnings volatility, financial leverage) each contain several **descriptors**; exposures are weighted combinations of descriptors, with weights chosen to maximize explanatory/predictive power, and multiple descriptors improve robustness.
  - *Standardization*: raw exposures are rescaled `x_std = (x_raw − E[x_raw]) / Std[x_raw]` to mean 0, sd 1, which also mitigates outliers. Example: GE size exposure `+1.90`, Netscape `−1.57` (Sep-1998).

- **The Three Uses of a Risk Model**: **the present** (current portfolio risk analysis, decomposition, marginal risk), **the future** (portfolio construction), **the past** (performance attribution).
- **Three-Way Risk Decomposition**: total ↔ active; market/benchmark ↔ residual; model ↔ specific.
- **Inherent / Intentional / Incidental Bets**:
  - *Inherent* — benchmark risk; constant, not under the manager's control (MMI's inherent risk is its S&P exposure; MMI beta `0.96`).
  - *Intentional* — the stocks the manager actually wants; high expected return should coincide with high marginal risk contribution (a *good* sign: portfolio is consistent with beliefs).
  - *Incidental* — unintended factor bets from screening or from incremental stock-by-stock decisions, each plausible alone. A yield screen silently becomes an industry bet on high-yield industries.
  - *Marginal contribution to active risk* `∂ψ_P/∂w_i`: in the Dec-1992 MMI vs. S&P 500 analysis, adding 1% to American Express raises active risk by 0.6 bp; AT&T (smallest, negative contribution) is the most diversifying; IBM (largest) the most concentrating.

## Key Concepts

1. **Standard deviation as risk** — universal, symmetric, flexible, accurately forecastable; aggregable from assets to portfolios.
2. **Variance as the cost of risk** — the book consistently prices risk in variance: `cost = A·σ²`, with `A` the risk-aversion coefficient.
3. **Risk aversion `A`** — the exchange rate between variance and expected return. At `A = 0.1`, 4% active risk costs `0.1 × (4%)² = 0.16%` of expected return.
4. **Active return** `r_PA = r_P − r_B` — the difference between portfolio and benchmark return.
5. **Active risk `ψ_P`** — standard deviation of active return; also called **tracking error**.
6. **Residual risk `ω_P`** — risk of the return orthogonal to the benchmark return; the risk that survives beta control.
7. **The `√T` horizon rule** — 5% annual active risk ⇒ 2.5% quarterly, 10% over four years; variance proportional to horizon length.
8. **Autocorrelation** — near zero for most asset classes; the assumption that makes variance additive across time.
9. **Semivariance / downside risk** — variance computed only on returns below the mean; equals exactly half the variance under symmetry (Magellan: 21.6 vs. 39.5 = 55%, slightly left-skewed).
10. **Shortfall probability** — `P(return < target)`; Magellan lost more than 10% in a month 3.4% of the time.
11. **Value at Risk (VaR)** — target probability mapped to a return; Magellan's worst 1% of monthly returns exceeded a 20.8% loss, i.e. $208 on $1,000.
12. **The `T > N` constraint** — historical covariance needs more periods than assets to avoid apparent riskless portfolios.
13. **Errors-in-variables problem** — response coefficients estimated by regression on measured macro series inherit the macro series' measurement error.
14. **Factor ex machina** — PCA/ML/EM factors that the estimation procedure manufactures rather than the market supplies.
15. **Fama–MacBeth cross-sectional regression** — the standard estimation procedure for factor returns: regress returns on exposures each period, minimizing (weighted) sum of squared specific returns, via GLS weighting by inverse specific variance (or `√market cap` as a proxy — specific variance scales roughly as size^-0.7).

## Formulas & Reference Tables

**Two-asset portfolio variance**

`σ_p² = w_1²σ_1² + w_2²σ_2² + 2w_1w_2ρ_12σ_1σ_2`

For `w_1 = w_2 = 0.5`: `σ_p = σ√((1+ρ)/2)` — equal to the weighted-average σ only if `ρ = 1`.

**Diversification with N equal-risk, equal-correlated assets**

`σ_p² = σ² [1/N + ((N−1)/N)·ρ]`  →  as `N → ∞`: `σ_p → σ√ρ`

**Horizon scaling / annualization**

`σ_annual = σ_monthly·√12`, generally `σ(T) = σ_annual·√T`

**Active return, active risk, residual risk**

`r_PA = r_P − r_B`
`ψ_P = Std{r_PA}`
`ω_P = Std{θ_PA}`, where `θ_P` is the part of excess return orthogonal to `r_B`

**Cost of risk (mean/variance penalty)**

`cost = A·σ²`. With `A = 0.1`: 4% active risk ⇒ `0.1 × 0.04² = 0.0016 = 0.16%`

**Structural return and risk structure**

`r = X·b + u`  (N excess returns; `X` = N×K exposure matrix; `b` = K factor returns; `u` = N specific/idiosyncratic returns)
`V = X·F·X' + Δ`  (`F` = K×K factor covariance; `Δ` = N×N diagonal specific covariance)

`Cov(u_n, b_k) = 0` (A1); `Cov(u_n, u_m) = 0` for `m ≠ n` (A2).

**Single-factor (diagonal) risk model**

`σ_nm = β_n β_m σ_M²` for `n ≠ m`; `σ_nn = β_n²σ_M² + σ²(u_n)`

**Constant-correlation model**

`σ_nm = ρ·σ_n·σ_m` for `n ≠ m`

**Standardized exposure**

`x_std = (x_raw − E[x_raw]) / Std[x_raw]`

**Empirical risk distribution, large U.S. equities (BARRA HICAP ~1200 stocks, 60-month windows, averaged over Jun-1980 / Jun-1990 / Dec-1998)**

| Percentile | Total risk (%) | Residual risk (%) | Beta |
|---|---|---|---|
| 90 | 50.8 | 45.0 | 1.67 |
| 75 | 40.1 | 34.3 | 1.36 |
| 50 (median) | 30.6 | 25.1 | 1.08 |
| 25 | 24.6 | 19.6 | 0.79 |
| 10 | 20.4 | 16.4 | 0.52 |

Typical totals 25–40%, typical residual 20–35%, typical beta 0.80–1.35. Risk distributions barely moved 1980–1998 (except the 90th percentile, which rose in 1998); betas declined over the period. **The median beta need not be 1 — only the capitalization-weighted beta equals 1.**

**BARRA U.S. model scale (1998)**: universe ≈ 1500 largest companies, 65 factor returns estimated monthly from ~1500 observations (52 of 65 factors are orthogonal industries); `R²` typically 30–40% for monthly equity cross-sections with ~1000 assets and ~50 factors, higher in months with large market moves.

**Kahn (1997) risk-forecast validation, 29 equity and bond funds, 1993–94**: with an accurate risk forecast, returns beyond 2σ should occur ~5% of the time.
- Portfolio-based (structural) forecasts: **zero** 3σ events, **one** 2σ event (3% of observations), 76% of observations below 1σ.
- Historical 3-year forecasts: **one** 3σ event (3%), **five** 2σ events (17%), 72% below 1σ.
- Neither method showed significant average over- or under-prediction; portfolio-based forecasts related far more strongly to subsequent realized risk.

**Kahn & Stefek (1996) risk-measure persistence**: 290 U.S. equity funds, 185 U.S. bond funds, 1160 individual U.S. equities; consecutive 5-year periods 1986–90 vs 1991–95. Method: regress period-2 risk measure on period-1, controlling for the variance-implied component (e.g. *abnormal* semivariance = semivariance − ½ variance). **Result: only standard deviation and variance persist. No alternative risk measure contains persistent information beyond variance.**

## Mental Models

1. **"Forecastability is the test, not philosophical fit."** When choosing a risk measure, ask: does it persist out of sample beyond what variance already tells you? Kahn & Stefek's answer for every alternative was no. If it doesn't persist, it cannot be a design parameter.
2. **"Risk is priced in variance, not in volatility."** Optimize and report consistently: if the objective uses `A·σ²`, marginal-risk contributions and gradients are linear in exposures, which makes the optimizer tractable.
3. **"Allocate risk budget in active percentage points, not benchmark percentages."** A ±50% relative position limit is not a risk control; the active weight in percentage points is.
4. **"Specific risk is the diversifiable risk; model risk is not."** The structural model's job is to tell you which exposures are shared (priced, systematic) and which are yours alone (specific, and the only place a stock-selection edge can hide).
5. **"If your factor exposures aren't known today, it isn't a factor."** The a priori constraint is what separates a usable risk model from a fitted decomposition.

## Code Examples

```python
# ⚠ reconstructed — risk decomposition and active-risk budgeting
import numpy as np

def total_variance(beta, sigma_m, sigma_eps):
    return beta**2 * sigma_m**2 + sigma_eps**2

def active_risk(w, b, cov):
    """tracking error: sd of (w-b)'r  == sqrt(a' Sigma a) with a = w - b"""
    a = np.asarray(w) - np.asarray(b)
    return float(np.sqrt(a @ cov @ a))

def residual_risk(w, b, cov):
    """residual (orthogonal-to-benchmark) risk"""
    a = np.asarray(w) - np.asarray(b)
    sd = np.sqrt(a @ cov @ a)
    cov_pb = np.asarray(b) @ cov @ a
    cov_bb = np.asarray(b) @ cov @ np.asarray(b)
    return float(np.sqrt(sd**2 - cov_pb**2 / cov_bb))

def cost_of_risk(sigma, A=0.1):
    """mean/variance cost in DECIMAL return units"""
    return A * sigma**2

# 4% active risk at A = 0.1
print(cost_of_risk(0.04))                 # 0.0016 -> 0.16%
print(0.10*np.sqrt(4), 0.05*math if False else 0.05*np.sqrt(4))  # horizon rule
```

```python
# ⚠ reconstructed — structural risk model: V = X F X' + Delta
def structural_cov(X, F, sigma_u):
    """X: (n,k) exposures, F: (k,k) factor covariance, sigma_u: (n,) specific vols"""
    X = np.asarray(X, float); F = np.asarray(F, float)
    V = X @ F @ X.T
    V[np.diag_indices_from(V)] += np.asarray(sigma_u, float)**2
    return V

def marginal_active_risk(w, b, cov):
    """d(tracking error)/dw_i  -- the 'marginal contribution to active risk'"""
    a = np.asarray(w, float) - np.asarray(b, float)
    sd = np.sqrt(a @ cov @ a)
    return (cov @ a) / sd
```

```python
# ⚠ reconstructed — the historical-covariance T > N trap, demonstrated
rng = np.random.default_rng(1)
n, T = 300, 120          # 300 assets, only 120 months  -> T < N
R = rng.normal(size=(T, n)) * 0.05
S = np.cov(R, rowvar=False)                  # 300x300 from 120 obs -> rank <= T-1 = 119
ev = np.linalg.eigvalsh(S)
print("min eigenvalue:", ev.min())          # <= 0 (numerically ~0) -> riskless active positions exist
print("rank deficiency:", n - np.linalg.matrix_rank(S))

# with T > N the trap disappears, but sample bias remains:
# a 500x500 covariance matrix has 500*501/2 = 125,250 independent numbers
print(500*501/2, 0.05*(500*501/2))
```

## Worked Example

**Exercise 3, recomputed — diversification with `σ = 35%`, `ρ = 0.50`.**

`σ_p² = σ²[1/N + ((N−1)/N)ρ]`, `σ_p = 0.35·√[1/N + ((N−1)/N)(0.5)]`

| N | `σ_p` |
|---|---|
| 5 | `0.35·√(0.2 + 0.8·0.5) = 0.35·√0.60 = 27.11%` |
| 20 | `0.35·√(0.05 + 0.95·0.5) = 0.35·√0.525 = 25.36%` |
| 100 | `0.35·√(0.01 + 0.99·0.5) = 0.35·√0.505 = 24.87%` |
| ∞ | `0.35·√0.5 = 24.75%` |

**Interpretation:** the reduction from `N = 5` to `N = 100` is only about 222 bp — the asymptotic floor is `σ√ρ`, and with `ρ = 0.5` you can never get below `24.75%` no matter how many stocks you hold. **This is the quantitative form of "most of the risk in a diversified equity portfolio is systematic."** Note that going from 1 asset (`35%`) to 5 already captures about 78% of the total achievable reduction.

**Exercise 2, recomputed — minimum-variance two-asset portfolio.** `σ_A = 25%`, `σ_B = 50%`, `ρ = 0.50`.

`Cov = 0.25 × 0.50 × 0.50 = 0.0625`
`w_A* = (σ_B² − Cov)/(σ_A² + σ_B² − 2Cov) = (0.25 − 0.0625)/(0.0625 + 0.25 − 0.125) = 0.1875/0.1875 = 0.75`
`w_B* = 0.25`
`σ_p = √(0.5625·0.0625 + 0.0625·0.25 + 2·0.75·0.25·0.0625) = √(0.035156 + 0.015625 + 0.023438) = √0.074219 = 27.24%`

**Interpretation:** the minimum-variance portfolio is 75% A / 25% B at 27.24% volatility — *higher* volatility than stock A alone (25%). Adding the higher-volatility asset reduces risk only because correlation is below 1, and the minimum-variance weight always overweights the low-variance asset. This is why minimum-variance portfolios are structurally **low-beta, value-tilted** portfolios — a real, deliberate active bet that must be labelled as such.

**Exercise 1, recomputed — GE monthly volatility.** Annual `27.4%` ⇒ monthly `0.274/√12 = 0.0791 = 7.91%`.

## Anti-Patterns

- **Estimating a full historical covariance matrix for a realistic universe.** `T > N` is required just to avoid apparent riskless positions; with 500 assets there are 125,250 numbers to estimate. Use a structural model.
- **Position limits expressed as ±X% of benchmark weight.** Active risk scales with the active weight in percentage points and the asset's risk, not with capitalization. A 1% active position in a small-cap can be riskier than a 1% active position in a mega-cap.
- **Optimizing with semivariance, shortfall probability or VaR.** Half the data, unstable asymmetry, and aggregation from assets to portfolios is essentially impossible. Report them if stakeholders want them; do not build portfolios on them.
- **Using macro/response factors naively.** Errors-in-variables, nonstationarity and poor-quality official data. If used, treat them as small supplements and shrink hard.
- **Trusting PCA/ML/EM "factor ex machina".** Spurious correlations, uninterpretable loadings, and structurally incapable of capturing time-varying exposures (momentum).
- **Ignoring incidental factor bets.** A yield screen is a hidden industry bet. Run the exposure decomposition *before* approving the trade, not after.
- **Annualizing risk under autocorrelation or GARCH effects without saying so.** The `√T` rule assumes serially uncorrelated returns; volatility clustering violates it.
- **Reporting a median beta of 1.** Only the capitalization-weighted beta is 1; the median was 1.08 in the HICAP table, and betas declined from 1980 to 1998.
- **Separating risk-model design from risk reporting.** The book is explicit that these are independent choices; conflating them leads to optimizing the wrong object.

## Practitioner Notes

- **Model risk management duty.** Because `Δ` is diagonal by construction, a structural model *understates* specific covariance (e.g. two large oil producers have positively correlated residuals). The single-factor model's zero residual covariance is deliberately conservative; production models add specific-risk adjustments or industry-level specific-risk blocks.
- **Validation duties named by the source.** (i) *Two-sigma frequency test* — with an accurate risk forecast, returns beyond 2σ should occur ~5% of the time; compare portfolio-based vs. historical forecasts on this count (Kahn 1997: 3% vs. 17%). (ii) *Persistence test* — regress period-2 risk on period-1; require high `R²` and significant positive `t`, controlling for the variance-implied component, before accepting any risk measure as a design input. (iii) *Multicollinearity check* — variance inflation factors must stay far below danger levels. (iv) *No systematic over- or under-prediction* — an always-conservative forecast will pass a naive 2σ test.
- **Model specification.** Industry factors act as the intercept in the cross-sectional regression and pick up the market return; they are the *more volatile* factors. The market has near-zero exposure to the risk indices, which pick up extra-market returns and are the *less volatile* factors. This is the clean way to separate market beta from active style exposure.
- **⚠ Practitioner update (post-1999)**: three material updates.
  1. *ES over VaR.* The Basel committee's Fundamental Review of the Trading Book (`BCBS MAR21`, Jan 2019) requires **expected shortfall at the 97.5% one-tailed confidence level** for regulatory capital, superseding VaR-based internal models; the 2016 revisions moved from 99% VaR to ES with multiplier **1.4**. VaR remains non-subadditive; ES is coherent. This does not change the *modelling* choice (standard deviation still aggregates and forecasts best) but it does change *what must be reported*.
  2. *Fat tails.* The book's normality assumption is acknowledged but the persistence study was designed to answer a different question — whether a wider distribution *persists for a given portfolio* — not whether tails are fat. Cross-sectionally, fat tails are real and are why a normal-mixture or Student-t factor return model is standard in production risk systems.
  3. *Specific risk is now modelled with better data.* Modern structural models (BARRA, Axioma, MSCI) add explicit liquidity, crowding, event/jump and derivatives-adjacency risk dimensions that did not exist in 1999. The a priori constraint still holds; the descriptor list is much longer.
  4. **Variance is quadratic in weights, so portfolio-level risk attribution should use *marginal* contributions** — Euler decomposition `TC_i = w_i (Σw)_i / σ_p` sums exactly to total volatility.

## Key Takeaways

1. Risk = standard deviation; the cost of risk = variance. Standard deviation wins because it is forecastable and aggregable, not because it captures everything.
2. Active risk depends on the **active position**, not the benchmark position. Budget risk in active percentage points.
3. Risk is linear in `√T`: 5% annual active risk is 2.5% quarterly and 10% over four years — variance, not volatility, is linear in the horizon.
4. Historical covariance models fail on the `T > N` rank argument plus sample bias (125,250 numbers in a 500-asset matrix; 5% bad ⇒ 6,262 bad).
5. Structural models `V = XFX' + Δ` with **a priori exposures** are the workable approach; Fama–MacBeth cross-sectional GLS is the standard estimation route, `R² ≈ 30–40%`.
6. Cross-sectional factors (size, value, momentum, volatility, liquidity, growth, earnings volatility, leverage) are the authors' preferred family; macro factors suffer errors-in-variables and nonstationarity; statistical "factor ex machina" cannot capture time-varying exposures.
7. Every alternative risk measure fails the persistence test beyond variance (Kahn & Stefek 1996), and structural risk forecasts beat historical ones on 2σ-exceedance frequency (3% vs. 17%, Kahn 1997).
8. Classify and act on active risk: **inherent** (benchmark, uncontrollable), **intentional** (should coincide with high marginal risk), **incidental** (the thing to cut first).

## Connects To

- **ch02**: supplies the beta forecast — the model-free input — and shows that only a good beta forecast is needed to separate market from residual.
- **ch04**: converts residual return and residual risk into **value-added**; ch03's `A·σ²` cost of risk is the penalty term in that objective.
- **ch05**: ch03's residual risk `ω_P` is the denominator of the **Information Ratio**, which is a *residual* not a Sharpe ratio.
- **ch06**: the fundamental law's `B` (breadth) is only meaningful because residual risk falls as `1/√N` through diversification.
- **ch14 (portfolio construction)**: the risk model is the covariance input; ch03's `V = XFX' + Δ` is literally the constraint matrix.
- **`cfasi-portfolio-construction`**: minimum-variance and risk-budgeting practice; the 75/25 result above is the minimum-variance tilt that practitioners must label as an active bet.
- **`cfa-portfolio-management`**: mean/variance theory, the efficient frontier and why `√ρ` is the diversification floor.
- **`cfasi-equity-investment-styles`**: maps the risk-index categories (size, value, momentum, volatility, liquidity, growth, leverage) onto the named investment styles.
- **`cfa-quantitative-methods`**: GLS/WLS estimation, Fama–MacBeth, eigenvalue rank and regression `t`-statistics used in the validation tests.
