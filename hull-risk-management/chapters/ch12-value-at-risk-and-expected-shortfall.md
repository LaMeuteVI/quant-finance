# Chapter 12: Value at Risk and Expected Shortfall

> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed. (Wiley, 2012) | Chapter 12, pp. 255–275

## Core Idea

Value at Risk (VaR) is the loss threshold that is exceeded with probability `1 − α` (e.g. 1% for a 99% VaR). Expected Shortfall (ES) — also called Conditional VaR, Average Value at Risk, or Expected Tail Loss — is the **expected loss conditional on exceeding the VaR**. ES is a *coherent* risk measure (Artzner et al. 1999) because it is subadditive and satisfies all the axioms; VaR is not subadditive for non-normal distributions and therefore fails the coherence property. This is the single most important reason the Basel Committee replaced VaR with ES in the **Fundamental Review of the Trading Book (FRTB)** — see ch17 and the `frtb-market-risk-bcbs457` skill.

The chapter is the regulatory core: a quant agent that uses VaR/ES must understand the **backtesting** framework (Kupiec POF, traffic-light zones, the loss exceptions count) and the **model assumptions** (the difference between parametric, historical, and Monte Carlo VaR).

## Frameworks Introduced

- **VaR definition**:
  `VaR_α = inf { x : P(Loss ≤ x) ≥ α }` (the loss threshold that is exceeded with probability `1 − α`).
  - *When to use*: every time you report a "loss number" for a portfolio. VaR is the lingua franca of risk management.
  - *Why it works*: it is a single number that summarises the loss tail; it is intuitive (a 1% VaR is "the loss we expect to see once every 100 days").
  - *Failure mode*: VaR is not subadditive; `VaR(X + Y) ≤ VaR(X) + VaR(Y)` does NOT always hold for non-normal distributions. Diversification can *increase* VaR.

- **Expected Shortfall (ES)**:
  `ES_α = E[Loss | Loss > VaR_α]` (the average loss in the tail beyond the VaR).
  - *When to use*: as the modern replacement for VaR. ES captures the *severity* of the tail, not just the *threshold*.
  - *Why it works*: ES is subadditive (and hence coherent) for any distribution; it correctly rewards diversification.
  - *Failure mode*: harder to backtest than VaR (it requires more data to estimate the conditional expectation accurately).

- **Parametric (variance-covariance) VaR**:
  - For a normal distribution of losses, `VaR_α = μ + σ × z_α`, where `z_α` is the standard normal quantile (e.g. 2.33 for 99%).
  - *When to use*: when the loss distribution is approximately normal (linear portfolios of normal assets, short horizons).
  - *Why it works*: closed-form; easy to decompose by risk factor.
  - *Failure mode*: severely under-states tail risk for non-normal distributions (Student-t with low degrees of freedom, mixtures, etc.). A 99% VaR computed under normality can be the 95% VaR of the true distribution.

- **Historical simulation VaR**:
  - Take the empirical distribution of the last N days of P&L. `VaR_α` is the `(1−α)`-th percentile.
  - *When to use*: when the loss distribution is non-normal but you have enough data to estimate the empirical quantiles.
  - *Why it works*: makes no parametric assumption; respects the actual tail.
  - *Failure mode*: with 250 daily observations, the 99% VaR is the 2nd- or 3rd-worst loss — extremely noisy. The 99.9% VaR is impossible to estimate from daily data.

- **Monte Carlo VaR**:
  - Simulate the portfolio under many scenarios; `VaR_α` is the `(1−α)`-th percentile of the simulated loss distribution.
  - *When to use*: when the portfolio has non-linear payoffs (options, mortgages, structured products) that are not captured by the parametric formula.
  - *Why it works*: handles arbitrary payoffs and distributions; the only "complete" method.
  - *Failure mode*: the simulation requires a calibrated model; the model error dominates the simulation error in most cases.

- **The **VaR backtesting** (traffic-light) framework**:
  - Count the number of "exceptions" (days when the loss exceeded the previous day's VaR) over a 1-year (250-day) period.
  - Basel 1996 traffic-light zones (still used for IMA backtesting under FRTB; see `frtb-market-risk-bcbs457`):
    - **Green zone** (0–4 exceptions): model is "acceptable".
    - **Yellow zone** (5–9 exceptions): model is in a "warning" zone; supervisor may require remediation.
    - **Red zone** (≥ 10 exceptions): model is "inaccurate"; supervisor may impose a capital add-on.
  - *Why it matters*: this is the formal regulatory test for an IMA-approved VaR model.
  - *Failure mode*: with 99% VaR and 250 days, the expected number of exceptions is 2.5; the 95% confidence interval is approximately [0, 6]. The traffic-light framework accommodates this noise but not much more.

- **The Kupiec Proportion of Failures (POF) test**:
  - H0: the true exception rate equals `1 − α`. The likelihood ratio statistic is `LR_POF = 2 [log((1 − p̂)^(N−x) p̂^x) − log((1 − p)^(N−x) p^x)]`, where `p = 1 − α`, `x` is the observed number of exceptions, `N` is the sample size, and `p̂ = x/N`.
  - Under H0, `LR_POF ~ χ²(1)`.
  - *When to use*: as a more formal version of the traffic-light framework. The 95% critical value is 3.84; reject H0 if `LR_POF > 3.84`.

- **The Christoffersen independence test**:
  - H0: the exceptions are serially independent. The statistic is `LR_ind = 2 [log(L_A) − log(L_0)]`, where `L_A` is the likelihood under an HMM with two states and `L_0` is the iid likelihood.
  - *When to use*: to detect *clustering* of exceptions (e.g. a regime of high volatility).

## Key Concepts

1. **VaR_α** — the loss threshold exceeded with probability `1 − α`.
2. **ES_α** — the expected loss conditional on exceeding VaR_α; the *coherent* version of VaR.
3. **Coherent risk measure** — a risk measure satisfying translation invariance, subadditivity, positive homogeneity, and monotonicity (Artzner 1999).
4. **Backtesting exception** — a day when the loss exceeded the previous day's VaR.
5. **Traffic-light zones** — green (0–4), yellow (5–9), red (≥ 10) over 250 days at 99% VaR.
6. **Kupiec POF test** — the formal likelihood-ratio test of the exception rate.
7. **Christoffersen independence test** — the test for serial dependence in exceptions.
8. **Parametric VaR** — `μ + σ × z_α`; assumes normal returns.
9. **Historical simulation** — empirical quantiles from past P&L.
10. **Monte Carlo VaR** — quantiles from simulated scenarios; the only "complete" method.
11. **Conditional VaR (CVaR)** — another name for ES; the term is more common in academia.
12. **Spectral risk measure** — a generalisation of ES using a weighting function over the tail; ES is the special case of equal weights.

## Formulas & Reference Tables

**VaR and ES for the normal distribution**

`VaR_α = μ + σ × z_α`, where `z_α` is the standard normal quantile at level α (e.g. 2.326 for 99%).
`ES_α = μ + σ × φ(z_α) / (1 − α)`, where `φ` is the standard normal density.

For α = 99%: `z_0.99 = 2.326`, `φ(2.326) = 0.0265`, so `ES_0.99 = μ + σ × 0.0265 / 0.01 = μ + σ × 2.665`.

**Parametric VaR with N independent positions**

If `V_t = Σ_i w_i r_{i,t}` and `r_{i,t} ~ N(μ_i, σ_i²)` independently, then `V_t ~ N(Σ w_i μ_i, Σ w_i² σ_i²)` and `VaR_α = Σ w_i μ_i + z_α × √(Σ w_i² σ_i²)`.

**VaR for a Student-t distribution**

If `r ~ t_ν(μ, σ²)`, then `VaR_α = μ + t_α × σ × √((ν − 2) / ν)`. For `ν = 4` (typical fat-tail parameter), the multiplier is `√(2/4) = 0.707`. The `t_0.99` for ν = 4 is 3.747, so `VaR_0.99 = μ + 3.747 × 0.707 × σ = μ + 2.65 × σ` — the same as the normal ES. **The normal 99% VaR understates the true Student-t 99% VaR by 13%** for ν = 4.

**Kupiec POF statistic**

`LR_POF = −2 ln((1−p)^(N−x) × p^x) + 2 ln((1 − x/N)^(N−x) × (x/N)^x)`

Reject H0 at 95% if `LR_POF > 3.84`.

**Traffic-light zones for 99% VaR, 250 days**

| Zone | Exception count | Action |
|---|---|---|
| Green | 0–4 | Model acceptable |
| Yellow | 5–9 | Investigation; supervisor may require remediation |
| Red | 10+ | Model inaccurate; capital add-on |

**ES-VaR relationship for the normal distribution**

`ES_α = VaR_α + σ × φ(z_α) / (1 − α)`. For α = 99%: `ES_0.99 = VaR_0.99 + 0.339 × σ`.

**Spectral risk measure**

`M_φ(X) = ∫₀¹ φ(p) × F^{-1}_X(p) dp`, where `φ` is a positive, decreasing weighting function. ES corresponds to `φ(p) = 1/(1−α)` for `p ∈ (α, 1]` and 0 otherwise.

## Mental Models

- **VaR is a threshold; ES is a magnitude.** Use ES when the question is "how bad can it get?", use VaR only for a single-number summary.
- **Coherence matters.** A non-coherent risk measure can be exploited by an adversary (or by a naive diversification programme) to produce a "less risky" portfolio that is actually riskier.
- **Backtesting is the only honest test.** Any risk model can be fitted to past data; the question is whether it predicts the next period's tail. The traffic-light framework is the institutional standard.

## Worked Example (RECOMPUTED)

*Setup.* A $10M portfolio of equities, daily volatility 1.5%, normal distribution assumed. 99% VaR over 1 day.

*Step 1 — Parametric VaR*.
- `σ_daily = 1.5% = 0.015` (in decimal).
- `z_0.99 = 2.326`.
- `VaR_0.99 = 2.326 × 0.015 × $10M = 0.0349 × $10M = $348,900`.

*Step 2 — Parametric ES*.
- `ES_0.99 = 2.665 × 0.015 × $10M = $399,750`.

*Step 3 — Student-t VaR (ν = 4)*.
- `t_0.99(ν=4) = 3.747`.
- `VaR_t = 3.747 × 0.015 × √(2/4) × $10M = 3.747 × 0.015 × 0.707 × $10M = $397,200`.

The Student-t VaR is *14% larger* than the normal VaR — a material difference.

*Step 4 — Kupiec POF test*.
- Over 250 days at 99% VaR, observe 6 exceptions.
- `p = 0.01`, `x = 6`, `N = 250`, `p̂ = 0.024`.
- `LR_POF = −2 ln((0.99)^244 × 0.01^6) + 2 ln((0.976)^244 × 0.024^6)`
- `= −2 [244 × ln(0.99) + 6 × ln(0.01)] + 2 [244 × ln(0.976) + 6 × ln(0.024)]`
- `= −2 [244 × (−0.01005) + 6 × (−4.6052)] + 2 [244 × (−0.02429) + 6 × (−3.7297)]`
- `= −2 [−2.452 − 27.631] + 2 [−5.926 − 22.378]`
- `= −2 [−30.083] + 2 [−28.305]`
- `= 60.166 − 56.610 = 3.556`
- Critical value at 95%: 3.84. So we *do not reject* H0 at 95% — the model is still acceptable. But 6 exceptions is at the boundary of the yellow zone, so the supervisor will probably flag it.

*Step 5 — Backtest over 1 year*.
- Exceptions per quarter: 2, 1, 1, 2 = 6 total.
- All in one cluster? If so, the independence test would reject — even though the rate is acceptable, the clustering suggests a regime issue.

*Sanity check (Python).*
```python
import math
from scipy.stats import norm, t as student_t

V, sigma_d, alpha = 10e6, 0.015, 0.99
z = norm.ppf(alpha)
VaR_norm = z * sigma_d * V
ES_norm  = (norm.pdf(z) / (1 - alpha)) * sigma_d * V
print(f"Normal VaR 99%: ${VaR_norm:,.0f}")   # ~$348,900
print(f"Normal ES  99%: ${ES_norm:,.0f}")    # ~$399,750

# Student-t with nu=4 degrees of freedom
nu = 4
t_q = student_t.ppf(alpha, nu)
scale = math.sqrt((nu - 2) / nu)
VaR_t = t_q * sigma_d * scale * V
print(f"Student-t VaR 99%: ${VaR_t:,.0f}")   # ~$397,200

# Kupiec POF
import math
N, x, p = 250, 6, 0.01
p_hat = x/N
LR = -2*( (N-x)*math.log(1-p) + x*math.log(p) ) + 2*( (N-x)*math.log(1-p_hat) + x*math.log(p_hat) )
print(f"Kupiec LR: {LR:.3f}  (95% critical = 3.841)")
```

## Anti-patterns

- **Using only VaR.** It is non-coherent; report ES as well, especially under FRTB.
- **Using a normal distribution without checking the tails.** Use Student-t, EVT, or empirical quantiles.
- **Backtesting at 99% VaR with 250 days of data.** The 95% confidence interval is too wide for fine-grained model selection; use 99.9% VaR for stricter tests (with the corresponding increase in data requirements).
- **Treating the traffic-light framework as a one-shot test.** The framework is designed to be applied *rolling* — supervisors look at the count over multiple quarters.
- **Ignoring the serial dependence of exceptions.** A model can have the right *rate* but cluster exceptions in regimes; the Christoffersen test catches this.

## Practitioner Notes

- **2026 update — FRTB replaced VaR with ES at 97.5% confidence, with a multiplier calibrated to stress conditions.** The Basel's preferred metric is `ES_t × m_t`, where `ES_t` is the 97.5% ES at time `t` and `m_t` is a multiplier that depends on the backtesting exception count and the P&L attribution test. The Hull 4th edition (2012) describes the pre-FRTB world; the `frtb-market-risk-bcbs457` skill covers the binding standard.
- **Backtesting the IMA (Internal Models Approach) under FRTB** uses a "traffic light" approach similar to the 1996 framework, but with different zones and a more direct link to capital add-ons.
- **ES is harder to backtest than VaR.** The empirical literature (e.g. Acerbi–Szekely 2014) shows that ES backtests require more data than VaR backtests. The FRTB approach uses a *parallel* backtest of VaR (red-zone traffic light) and a P&L attribution test, rather than directly backtesting ES.
- **Coherent risk measures beyond ES.** Convex risk measures, distortion risk measures, and spectral risk measures are generalisations; ES is the most commonly used coherent measure in practice.
- **The Hull 4th edition's chapter 12 is somewhat dated by FRTB.** A reader who needs the binding 2026 regulatory framework should consult the `frtb-market-risk-bcbs457` skill; the Hull chapter provides the conceptual foundation (coherence, ES, backtesting) but the FRTB regulatory text has specific numbers (97.5% confidence, multiplier values, IMA vs SA, default risk charge, residual risk add-on) that the 2012 chapter does not reflect.

## Key Takeaways

1. **VaR is a threshold; ES is a tail average.** Use ES as the modern standard.
2. **VaR is not coherent; ES is.** Coherence is the property that makes a risk measure respect diversification.
3. The traffic-light backtesting framework is the **institutional standard** for IMA VaR validation.
4. **Kupiec POF and Christoffersen independence tests** are the formal statistical tests of the backtest exception count.
5. **FRTB replaced VaR with ES at 97.5%** — the `frtb-market-risk-bcbs457` skill is the binding source.

## Connects To

- **ch11** (Correlations and Copulas): the choice of copula directly affects the VaR of a multi-asset portfolio; Student-t copula gives fatter joint tails.
- **ch13** (Historical Simulation and EVT): the practical methods for non-parametric VaR.
- **ch14** (Model-Building Approach): the parametric VaR is the linear model approach to VaR; the historical and Monte Carlo are non-linear.
- **ch17** (Fundamental Review of the Trading Book): the regulatory framework that replaced VaR with ES at 97.5%.
- **`frtb-market-risk-bcbs457` skill**: the binding source for FRTB's ES-based capital requirement.
- **`hull-derivatives` ch15 (Volatility Smiles)**: the volatility surface is the input to the option-portfolio VaR; local vol vs stochastic vol changes the tail shape.
- **`lopez-de-prado-afml` ch14 (Backtest Statistics)**: the formal statistical framework for risk-model backtesting.
