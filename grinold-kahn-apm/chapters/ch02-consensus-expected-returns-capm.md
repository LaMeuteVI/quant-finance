# Chapter 2: Consensus Expected Returns — The Capital Asset Pricing Model

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 2, pp. 11–40

## Core Idea

The CAPM is used here for one purpose: it supplies the **consensus expected returns** against which an active manager's own forecasts are measured. Its single economic claim is that the expected residual (benchmark-orthogonal) return of every stock and portfolio is zero, `E[θ_P] = 0`, so that expected excess return is entirely explained by beta. Crucially, the *return decomposition* into market and residual components requires no theory at all — only a good beta forecast. The theory enters only at the step where it sets residual expected return to zero.

The active manager's entire business is then the *difference* between their forecast excess returns and the CAPM consensus. If your forecast equals the consensus, optimal mean/variance portfolios are just the market portfolio and cash.

## Learning Outcomes Covered

- Decompose any excess return into market and residual components from a beta forecast, with no economic assumptions.
- State the CAPM security-market-line relationship and what it implies for consensus expected returns.
- Explain why expected *residual* returns must be zero (the "hot potato" / greater-fool argument) and what follows for passive investing.
- Distinguish the three forms of the efficient-markets hypothesis from the CAPM, and note where they agree and differ.
- Explain why historical average returns are a poor substitute for consensus expected returns.
- Justify why a beta-neutral (β = 1.0) manager does not need an accurate estimate of the expected market excess return.

## Frameworks Introduced

- **Return Separation**: `r_P = β_P · r_M + θ_P` with `E[θ_P] = 0` under CAPM.
  - *Formulation*: excess return splits into a market component scaled by beta plus a residual component with zero expectation and zero covariance with the market.
  - *When to use*: always, before any active decision. It converts an absolute-return problem into a relative-return problem.
  - *How*: (1) forecast `β_P`; (2) compute the market contribution `β_P·r_M`; (3) treat the remainder as active/residual; (4) require that any active position be justified by the residual alone.
  - *Why it works*: removing the market component eliminates the need to forecast `μ_M` and removes market-timing risk from the research mandate.
  - *Failure mode*: beta is a *forward-looking* quantity estimated from history. Betas regress to the mean; a stale 60-month regression beta is a biased forecast, and beta instability (especially around leverage events) breaks the decomposition.

- **The Consensus Portfolio Principle (separation theorem implication)**: mean/variance optimal portfolios are combinations of the market portfolio and the risk-free asset *if and only if* forecast excess returns equal CAPM consensus excess returns.
  - *When to use*: as the null hypothesis in any active strategy research. If the optimizer keeps producing market + cash, your forecasts contain no active information.
  - *Why it works*: it makes "consensus" operational rather than rhetorical.
  - *Failure mode*: confusing an optimizer that returns the benchmark with a strategy that has no edge, when the real cause is a constraint that pins the portfolio to the benchmark.

- **The "Hot Potato" Argument for `E[θ_P] = 0`**: market risk is necessary, residual risk is self-imposed; any positive expected residual return implies an offsetting holder with negative expected residual return (a "greater fool").
  - *When to use*: when stress-testing whether an assumed alpha is plausible, and when arguing internally about how much edge to underwrite.
  - *Why it works*: it is an accounting identity, not an assumption — for every overweight there is an equal underweight.
  - *Failure mode*: the argument breaks if someone holds *negative* residual risk (short the benchmark, or levered/derivative-embedded structures), or if residual positions are not closeable at zero expected cost. Structural constraints (limits to arbitrage, funding costs, dealer balance sheets) are precisely the modern escape hatch — and the source of persistent factor premia.

- **Three Forms of Efficient Markets**: weak (prices/volume), semistrong (prices + public fundamentals + analyst recommendations), strong (all information, public and private).
  - *When to use*: to frame what data an active strategy is permitted to exploit — semistrong EMH is the practical operating assumption for most live mandates.
  - *Note*: the CAPM is *consistent with* EMH but is **not** the same statement. EMH argues there are no greater fools; the CAPM only says any residual position has zero expected return. A manager can believe in EMH and still run active management on costs, taxes, liquidity and implementation.

## Key Concepts

1. **Excess return** `r` — total return minus the risk-free return over the same period. All CAPM statements are about excess returns, never total returns.
2. **Beta** `β_P` — the portfolio's covariance with the market divided by the market's variance; a *forecast*, not a description. The market has `β = 1`, the risk-free asset `β = 0`.
3. **Residual return** `θ_P` — the part of excess return uncorrelated with the market; the active manager's actual product.
4. **Residual variance** `σ_θ(P)²` — variance of `θ_P`; the true measure of active risk.
5. **CAPM consensus** — `E[θ_P] = 0` for all stocks and portfolios; `E[r_P] = μ_M·β_P`.
6. **Security Market Line** — expected excess return is linear in beta through the origin, with slope `μ_M` and intercept zero.
7. **Value-weighted residual identity** — the value-weighted sum of residual returns is *exactly* zero in every period, by construction of the market portfolio. CAPM goes further: it claims each component's *expectation* is zero.
8. **Historical vs. predicted beta** — BARRA predicted betas from fundamental attributes were better forecasts of future betas than 60-month return-regression betas; betas regress to the mean.
9. **Sample error of historical means** — `SE(μ̂) = σ/√Y`, roughly 16% for 35%-volatility stocks over five years, independent of observation frequency.
10. **Survivorship / universe instability** — new listings, mergers and delistings mean a "stock's historical average" is not an average over a homogeneous population.
11. **The burden of proof** — CAPM makes the passive portfolio the lower-risk benchmark alternative and pushes the evidentiary burden onto the active manager.
12. **Beta-neutral independence of `μ_M`** — with portfolio beta = 1.0, the market excess return contributes nothing to active return, so no accurate market-return forecast is required.
13. **Roll (1977)** — the joint hypothesis that the market portfolio is mean/variance efficient is untestable; cited by the authors as the reason to treat CAPM conclusions as conditional.

## Formulas & Reference Tables

**Beta (covariance form)**

`β_P = Cov(r_P, r_M) / Var(r_M) = Cov(r_P, r_M) / σ_M²`

**Historical beta via time-series regression** (periods `t = 1, …, T`)

`r_P(t) = α_P + β_P·r_M(t) + θ_P(t)`, with `E[θ_P(t)] = 0`

The fitted `β_P`, `α_P` are the **realized/historical** estimates; the forward-looking `β_P` used in forecasting is a different quantity.

**Return separation**

`r_P = β_P·r_M + θ_P`, with `Cov(θ_P, r_M) = 0`

**Variance decomposition**

`σ_P² = β_P²·σ_M² + σ_θ(P)²`

**CAPM consensus expected return (Security Market Line)**

`E[r_P] = μ_P = β_P · μ_M`, with `E[θ_P] = 0`

**Market and risk-free portfolios**

| Portfolio | Beta | Expected excess return |
|---|---|---|
| Market `M` | 1 | `μ_M` |
| Risk-free asset | 0 | 0 |
| Any portfolio `P` | `β_P` | `β_P·μ_M` |
| Active portfolio `P` (residual) | — | 0 by CAPM consensus |

**Standard error of a historical mean**

`SE(μ̂) = σ/√Y`, independent of sampling frequency once annualized.

**Illustrative beta table (60-month historical vs. BARRA predicted, vs. S&P 500, Dec-1992)**

| Stock | Historical beta | BARRA predicted beta | Disagreement |
|---|---|---|---|
| American Express | 1.21 | 1.14 | 0.07 |
| AT&T | 0.96 | 0.69 | 0.27 |
| Chevron | 0.46 | 0.66 | 0.20 |
| Coca Cola | 0.96 | 1.03 | 0.07 |
| Disney | 1.23 | 1.13 | 0.10 |
| Dow | 1.13 | 1.05 | 0.08 |

The gap is the point: a purely historical beta is a *noisy, mean-reverting* statistic; a fundamental-attribute beta is a better forecast.

## Mental Models

1. **"The decomposition is free; only the zero-expectation assumption costs you."** Use the market/residual split even if you reject the CAPM — it requires only a beta forecast and gives you a clean active-risk accounting.
2. **"Consensus = the market portfolio."** If a mean/variance optimizer hands you market + cash, your forecasts are the CAPM's forecasts. That is a testable diagnostic, not an opinion.
3. **"Strip market timing out of the mandate."** Hold beta at 1.0 and `μ_M` stops mattering. Then all research effort goes to residual returns, where the consensus prior is zero and the burden of proof is explicit.
4. **"A greater-fool test."** Before underwriting an alpha, ask who is on the other side of the trade and why they are losing. If you cannot name the counterparty and their reason, the edge is probably a compensation for illiquidity or a hidden funding cost.
5. **"Betas regress; fundamentals forecast."** Blend or shrink historical betas toward fundamental-attribute betas rather than trusting a raw 60-month regression.

## Worked Example

**Exercise 1 — Sears.** Predicted beta `= 1.05` vs. the S&P 500. The S&P 500 subsequently underperforms Treasury bills by `5.0%`.

- Under CAPM, `E[θ_Sears] = 0`, so the whole expected excess return is the beta-scaled market excess return.
- `E[r_Sears] = β · μ_M = 1.05 × (−5.0%) = −5.25%`
- Interpretation: Sears is 5% *worse* than expected *only because the market was bad*. Its expected residual contribution is zero. **This is exactly why a market-neutral active manager should not have held this position.**

**Exercise 2 — long-run market excess return.** If `μ_M = 7%` per year:

- `E[r_Sears] = 1.05 × 7% = 7.35%`
- Same beta, different market assumption → different absolute forecast, but **identical residual forecast (zero)**. Any active decision is unaffected.

**Exercise 3 — cross-correlation and residual vol.** Stock A: `β_A = 1.15`, `σ_A = 35%`. Stock B: `β_B = 0.95`, `σ_B = 33%`. Market `σ_M = 20%`.

- `σ_θ(A) = √(0.35² − 1.15²·0.20²) = √(0.1225 − 0.05290) = √0.0696 = 0.2638… ≈ 26.4%`
- `σ_θ(B) = √(0.33² − 0.95²·0.20²) = √(0.1089 − 0.03610) = √0.0728 = 0.2698… ≈ 27.0%`
- Cross-covariance from total variances: `Cov(A,B) = ½[σ_A² + σ_B² − σ_(A−B)²]`. Assuming residual returns are uncorrelated across stocks (as the problem states), `Cov(r_A, r_B) = β_A β_B σ_M² = 1.15 × 0.95 × 0.20² = 0.04370`.
- Then `Corr(A,B) = 0.04370 / (0.35 × 0.33) = 0.04370 / 0.1155 = 0.3784… ≈ 0.38`
- **Higher residual volatility: Stock B (27.0%) vs Stock A (26.4%).** Counterintuitive but correct — Stock B's lower beta offsets much of its higher total volatility, and A's beta *borrows* risk from the market that is *not* active risk.

*(All figures recomputed in Python: `σ_θ(A) = 0.263818…`, `σ_θ(B) = 0.269815…`, `Corr = 0.378355…`)*

## Anti-Patterns

- **Treating the beta estimate as the beta.** Historical beta is a realized, mean-reverting statistic; the forecast requires shrinkage or a fundamental model.
- **Using total volatility where residual volatility belongs.** Residual volatility is the risk you are paid for; total volatility blends in unavoidable market risk.
- **Forecasting `μ_M` when the mandate is beta-neutral.** It adds estimation error and market-timing temptation with zero effect on active return.
- **Assuming the value-weighted residual identity implies each residual's expectation is zero.** The identity is exact in every sample period; the zero-expectation claim is the economic hypothesis.
- **Confusing CAPM with EMH.** They are consistent, not identical. EMH is a statement about information; CAPM is a statement about expected residual return.
- **Reporting active return without stating the beta assumption.** An active return that is really market timing in disguise is mislabelled risk.
- **Ignoring universe instability.** Historical averages over a survivorship-filtered universe are not estimates of anything forward-looking.

## Practitioner Notes

- **Attribution discipline.** Because a "portfolio" is often a disguised basket of market, factor and residual bets, the first question at any investment committee should be: *what is the beta, and is it intended?* An unexplained active bet is an unpriced risk.
- **The consensus prior.** Since `E[θ_P] = 0` is the agreed starting point, every forecast should be expressed as a deviation with a stated standard error. A forecast of `+2%` residual return with a `±6%` standard error is not a forecast; it is a noise realization.
- **⚠ Practitioner update (post-1999)**: the CAPM's single-factor premise has been heavily tested and largely rejected as a complete return model. Fama–French (1992/1993) size and book-to-market; Carhart (1997) adding momentum; Fama–French (2015) five factors; Hou–Xue–Zhang (2015) `q`-factors — all find that market beta alone leaves a large, systematic residual. Treat the CAPM as (a) the *consensus benchmark prior*, and (b) a risk-decomposition device. Do **not** treat `E[θ_P] = 0` as a fact about traded assets in practice — it is best read as a null hypothesis you are required to beat, and the accumulated evidence says factor premia are the price of *tolerated* (limits-to-arbitrage) risk rather than mispricing. Note also that Grinold & Kahn's own ch07 APT and the modern factor literature cover this gap; the 1999 text treats APT as "interesting but not a source of consensus."

## Key Takeaways

1. The market/residual return decomposition is theory-free; only `E[θ_P] = 0` is the CAPM's economic claim.
2. `r_P = β_P·r_M + θ_P`, `σ_P² = β_P²σ_M² + σ_θ(P)²`, `E[r_P] = β_P·μ_M` under the consensus.
3. Consensus is *defined* by the market portfolio being mean/variance optimal — active views are deviations from `β_P·μ_M`.
4. Historical average returns are unusable: `SE(μ̂) = σ/√Y ≈ 16%` for 35%-volatility names over five years, before universe and nonstationarity problems.
5. Fundamental-attribute betas forecast future betas better than 60-month return regressions, and betas mean-revert.
6. Zero expected residual return follows from the "hot potato" logic: market risk is necessary, residual risk is self-imposed, and every overweight has an underweight.
7. Weak/semistrong/strong EMH are different claims; semistrong is the practical operating assumption for a live mandate.
8. Beta neutrality eliminates the need to forecast `μ_M` and isolates the research problem to residual returns with a zero prior.

## Connects To

- **ch01**: supplies the CAPM as the *consensus* return vector whose `IR`-based value-added machinery ch01 previewed.
- **ch03**: takes the beta forecast — the one model-free input here — and develops the full forward-looking risk model, including beta shrinkage and specific-risk forecasting.
- **ch04**: converts residual return and residual risk into **value-added**, and shows why a benchmark by definition adds no value.
- **ch06**: the `IC × √B` law makes the active problem quantitative; it assumes the residual return prior established here is zero-mean.
- **ch07**: the APT is the multi-factor alternative to this single-factor consensus, and the book's preferred expected-return framework for active use.
- **`cfasi-equity-investment-styles`**: the modern empirical (size, value, momentum, quality) answer to the CAPM's residual-is-zero claim.
- **`cfa-portfolio-management`**: capital allocation, efficient frontier and the separation theorem in the total-return setting this chapter generalizes.
- **`cfa-quantitative-methods`**: OLS regression, standard errors and the covariance/variance algebra underlying beta estimation.
