# Chapter 7: Expected Returns and the Arbitrage Pricing Theory
> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2e, McGraw-Hill 1999 | Chapter 7, pp. 174–193

## Core Idea

The APT states that a stock's expected excess return is the sum of its factor exposures times a set of factor forecasts. Unlike the CAPM it does not name the factors, the exposures, or the weights — that is exactly where the manager's art lives. Its practical value to an active manager is not as a *consensus* return model but as a flexible engine for turning whatever you can forecast (gold, oil, bonds, the yen, growth stocks) into a cross-section of expected returns and hence into alpha.

## Frameworks Introduced

- **Arbitrage Pricing Theory (APT)**: `r_n = Σ_k X_{n,k} · f_k + e_n` for excess returns; and `E[r_n] = Σ_k X_{n,k} · m_k` where `X_{n,k}` = stock n's exposure to factor k, `m_k` = the factor forecast for factor k.
  - **When to use**: when your edge is about *relative* pricing across a coverage universe rather than about the market portfolio.
  - **How**: (1) pick factors you can actually forecast, (2) estimate exposures, (3) forecast factor returns, (4) take the cross-sectional difference between each stock's forecast and the benchmark's.
  - **Why it works / failure mode**: follows from ruling out **quasi-arbitrage** — an active position with zero exposure to all factors but a positive expected excess return, at near-zero risk and zero cost, could be added to any portfolio for free. If such positions exist, the APT equation fails. It fails in practice on *factor forecasting*, not on model qualification.

- **Qualified model**: a factor model for which some set of factor forecasts `m_k` makes the APT equation hold. Theorem: a model is qualified **iff portfolio Q is diversified with respect to that factor model** — i.e. among all portfolios with Q's factor exposures, Q has minimum risk.
  - **Why it works**: easy to satisfy. Empirically (BARRA U.S. Equity), unexplained variance falls as coverage widens: MMI (20 stocks) 2.51%, OEX (100) 0.99%, S&P 500 (500) 0.30%, FR1000 0.21%, FR3000 0.18%, ALLUS (~6,000) 0.17%. Over 99% of variance is explained for well-diversified portfolios.

- **Portfolio Q**: the maximum-Sharpe-ratio portfolio of the coverage universe; plays the role the market portfolio plays in the CAPM (the CAPM is the special case where Q *is* the market).
  - **Operational proxy**: "the manager" — the portfolio that best represents the aggregate stock-picking ability of the active investment community, used as the benchmark whose betas generate the consensus return forecast.

- **Three-layer discipline** (motivating stories ≠ implementations ≠ the theory). Never confuse a particular APT implementation with the theory itself; two equally informed scholars will build different implementations, and that is expected.

- **Structural vs statistical models** (see Code Examples / table below) — the six implementations the book sketches.

## Key Concepts

- **Factor exposure `X_{n,k}`** — stock n's sensitivity to factor k; in the BARRA structural model it is a function of current stock characteristics (earnings yield, size, industry).
- **Factor forecast `m_k`** — the manager's expected return on factor k; the only free parameter of the model.
- **Factor return `f_k`** — the realized realization of factor k over the estimation window.
- **Residual `e_n`** — the stock-specific return left after factor exposures are accounted for; this is the active opportunity.
- **Quasi-arbitrage** — near-certain gain at near-zero risk and zero cost; excluding it is what forces the APT relationship. The book calls the resulting vulnerability the "arbitrary" pricing theory.
- **Qualified model** — see above; the technical requirement is diversification of portfolio Q, not model correctness.
- **Unpredictability by consensus** — if every active manager shared the same information the APT would be worthless. Model flexibility *is* the source of edge.
- **Idiosyncratic residual variance** — the active opportunity available from better-than-consensus forecasts.
- **Collinearity** — overlapping factor definitions create redundant exposures; the book notes the BARRA model is explicitly built to avoid it while Haugen–Baker-style sector/descriptor models often do not.

## Formulas & Reference Tables

**Factor model**

`r_n = Σ_{k=1..K} X_{n,k} · f_k + e_n` (Eq. 7.1) — `r_n` excess return, `f_k` factor return, `e_n` residual (mean zero).

**APT expected-return relation**

`E[r_n] = Σ_{k=1..K} X_{n,k} · m_k` (Eq. 7.2) — `m_k` = factor forecast.

**Alpha versus consensus**

`α_n = E[r_n] − E_b[r_b]` where `E_b[r_b] = Σ_k X̄_k · m_k` is the benchmark's expected excess return at the benchmark's factor exposures.

**Consensus-exposure CAPM comparison**: `E[r_n] = r_f + β_n · (E[r_M] − r_f)` with `β_n = X_{n,market}`. In Table 7.2 the CAPM forecast uses a 6% expected market excess return.

**Model diversification evidence (Table 7.3)**

| Portfolio | # Assets | Unexplained variance (%) |
|---|---|---|
| MMI | 20 | 2.51 |
| OEX | 100 | 0.99 |
| S&P 500 | 500 | 0.30 |
| FR1000 | 1000 | 0.21 |
| FR3000 | 3000 | 0.18 |
| ALLUS | ~6000 | 0.17 |

**Structural model 1 (given exposures, estimate factor returns)**: cross-sectional regression of realized excess returns on known exposures → factor returns; forecast those factor returns.

**Structural model 2 (given factor returns, estimate exposures)**: set market exposure to 1; regress (stock return − NYSE return) on the other factor returns → exposures.

**Structural model 3**: hybrid — estimate exposures as in model 2, attribute returns as in model 1.

**Statistical model 1 (PCA)**: eigendecompose the `N × N` covariance matrix; typically the **first 20 components explain ≥90% of the risk**. Factor returns are orthogonal by construction; exposures for out-of-sample stocks come from regressing their returns on the factor returns.

**Statistical model 2 (Maximum Likelihood Factor Analysis)**: full ML fit of Eq. (7.1) assuming exposures `X_{n,k}` constant over the window. Example scale: 500 stocks × 60 months with 10 factors uses **30,000 returns** to estimate **5,000 exposures + 600 factor returns**.

**Statistical model 3 (dual)**: when `N > T` (typical), analyze the `T × T` covariance matrix instead, reversing the roles of exposure and factor return (Connor & Korajczyk).

**International additivity** (from the Chapter 6 law):

`IR_total² = BR_C·IC_C² + BR_M·IC_M² + Σ_countries BR_i·IC_i²`

## Mental Models

- **"Build from your forecasting strengths."** Use breadth-of-coverage and factor structure to capture risk, but choose factors you can forecast. There is no use building the most qualified model in the world if you cannot forecast its factor returns.
- **"Naming the task makes it clearer."** A "bond market beta" factor forecast *is* a forecast of bond returns. A "growth" factor forecast *is* your view on growth stocks. Naming does not make it easier, but it makes failure diagnosable.
- **"Structure beats a crank."** Statistical models leave no latitude to forecast (`m_k` defaults to the historical average). Structural factors tie `m_k` to something you can reason about, so common sense and alternative estimators can cross-check each other.
- **"Diversification makes the model qualify."** Qualification is nearly free; forecasting is the scarce input. Do not spend research budget on a more perfect factor set.
- **"Indexing the tail."** Adding a small new universe with your best forecast on it can push the benchmark to weight it heavily, wrecking your active risk — the practical failure of additivity noted in Chapter 6's footnote.

## Code Examples

```python
import numpy as np

def apt_expected_returns(X, m):
    """X: (N,K) exposures. m: (K,) factor forecasts. -> (N,) expected excess returns."""
    return np.asarray(X) @ np.asarray(m)

def alpha_vs_benchmark(X, m):
    r = X @ m
    return r - (X.mean(axis=0) @ m)      # benchmark = equal-weighted universe

def estimate_factor_returns(R, X, ridge=0.0):
    """Structural model 1: cross-sectional regression R ~ X -> factor returns f."""
    A = np.column_stack([X, np.ones(len(X))])
    if ridge:                                  # guards against collinear exposures
        A = np.vstack([A, np.sqrt(ridge) * np.eye(A.shape[1])])
    coef, *_ = np.linalg.lstsq(A, R, rcond=None)
    return coef[:-1]                            # factor returns

def capm_expected_returns(beta, market_excess=0.06):
    return beta * market_excess

def is_qualified(X):
    """Proxy for 'Q diversified wrt factor model': exposures must span the
    factor space without singularity."""
    return np.linalg.matrix_rank(X) == X.shape[1]

def pca_factors(R, n_components=20):
    """Statistical model 1. R: (T,N) returns -> (factors, explained var ratio)."""
    cov = np.cov(R, rowvar=False)
    vals, vecs = np.linalg.eigh(cov)
    order = np.argsort(vals)[::-1][:n_components]
    return vals[order], vecs[:, order]
```

**Implementation map (reconstructed from the book's six sketches)**

| Model | Given | Estimated | Forecasts | Practitioner |
|---|---|---|---|---|
| Structural 1 | exposures | factor returns | factor returns | Trend-following/quant shops |
| Structural 2 | factor returns | exposures | factor returns | Fundamental/tilt funds |
| Structural 3 | primitives | both | factor returns | Hybrid desks |
| Statistical 1 | — | PCA factors | historical mean | Academics; no latitude |
| Statistical 2 | — | ML factors | historical mean | Barra-style risk models |
| Statistical 3 | — | dual (T×T) | historical mean | Connor–Korajczyk |

## Worked Example

**Cross-sectional alpha under a five-factor structural model (recomputed).** Factor forecasts: heavy-electrical industry 6.0%, growth 2.0%, bond beta −1.0%, size −0.5%, ROE 1.0%. General Electric exposures: industry 1.0, growth −0.24, bond beta 0.13, size 1.56, ROE 0.15 (market beta 1.10, unused in APT).

- `E[r_GE] = 1.0(6.0) + (−0.24)(2.0) + 0.13(−1.0) + 1.56(−0.5) + 0.15(1.0)`
- `= 6.00 − 0.48 − 0.13 − 0.78 + 0.15 = 4.76%`
- Benchmark (heavy-electrical industry, exposure 1.0) = `1.0(6.0) = 6.00%`
- **`α_GE = 4.76 − 6.00 = −1.24%`**

Interpretation: GE is cheap-looking on size and expensive-looking on growth and bond beta, and that more than offsets its exact industry fit. The entire cross-section of alphas comes from exposure differences — the factor forecasts themselves cancel in the benchmark-relative calculation.

**Scale illustration (recomputed).** In the book's 20-stock APT-vs-CAPM table the mean APT forecast is 4.26% while the mean CAPM forecast is 6.14%, an average residual of −1.88%. The book's own point: swapping factor assumptions generates "mountains of research" — which is a feature (flexibility) and a warning (results are assumption-driven).

## Anti-patterns

- **Using APT as a consensus model.** The book's verdict is blunt: its flexibility makes it *inappropriate* as a model of consensus expected returns. If everyone uses it, it has no edge.
- **Confusing a motivating story with the theory.** Economic narratives about why a factor might work are neither necessary (factors need not be macro) nor sufficient.
- **Confusing your implementation with the theory.** Two good practitioners will build different models; a difference in output is not evidence that one is wrong.
- **Over-investing in factor qualification.** Qualification follows from diversification and is nearly free. Effort belongs in `m_k`.
- **Statistical-model complacency.** With PCA factors the only defensible forecast is the historical average; if you cannot forecast the historical average better than a random draw, do not build a statistical APT model.
- **Ignoring collinearity.** Haugen–Baker-style models replacing 50+ industries with 10 sectors and 13 risk indices with 40 descriptors produce collinear exposures and unstable attribution.
- **Blind spot: coverage.** The CAPM in theory requires universal coverage; the APT allows you to concentrate on any desired group of stocks. That flexibility is a feature, and also a governance problem.

## Practitioner Notes

**The international-portfolio additivity check (recomputed).** Following 400 US + 300 Japan + 200 UK + 100 Germany stocks at `IC = 0.02`, revised annually: `IR² = 1000 × 0.02² = 0.400`. With 12 currency bets and 12 country-allocation bets per year, matching that contribution requires `IC_C = IC_M = √(0.40/24) = 0.129` — implausibly high. At a realistic `IC = 0.075` the two macro sleeves contribute only `24 × 0.075² = 0.135`, total `IR² = 0.535`, `IR = 0.731`. **Design consequence: with broad stock coverage, currency and country timing cannot be expected to move the needle; spend the budget on stock-level breadth.**

**Manager allocation (recomputed).** Three equity managers with IRs 0.75 / 0.50 / 0.30 optimally allocated give the sponsor `IR = √(0.75² + 0.50² + 0.30²) = 0.95`. Diversifying manager skill is as valuable as diversifying assets — the sponsor should weight toward the strongest skill, not evenly.

**Regulatory/industry anchor**: the CAPM's core assumption that all participants know every stock's expected excess return is itself the flaw to stress-test against; the book calls the resulting consensus a "guideline that should be neither ignored nor taken as gospel."

## Key Takeaways

1. `E[r_n] = Σ_k X_{n,k}·m_k` — expected excess return is exposures × factor forecasts. Nothing more is specified.
2. Qualification is automatic if portfolio Q is diversified w.r.t. the model; forecasting `m_k` is the hard part.
3. Over 99% of variance is explained for well-diversified portfolios (BARRA), so model risk is rarely the binding constraint.
4. The APT's arbitrariness is its weakness as consensus theory and its strength as a private alpha engine.
5. Structural factors give forecast latitude; statistical factors give none — choose based on where your skill is.
6. With broad coverage, macro/currency sleeves add little: you would need `IC ≈ 0.129` to match the stock sleeve.
7. Manager diversification: IR 0.75/0.50/0.30 optimally combined = 0.95.
8. Alpha is entirely the exposure *difference* versus the benchmark; factor forecasts cancel.

## Connects To

- **ch 06**: the APT supplies genuine independent bets — factor forecasts — that determine the breadth `B` in the Fundamental Law; international additivity is that law applied across sources.
- **ch 08**: the theory of valuation formalizes the risk-adjusted expected return that the APT factor forecast represents.
- **ch 09**: DDM and returns-based analysis are the practical means of producing `m_k`.
- **ch 03**: the BARRA risk model reused here as an APT factor structure.
- **ch 02**: the consensus/equilibrium expected return that the APT forecast is differenced against.
- **`hull-derivatives` ch NN**: no-arbitrage reasoning in continuous time, the same logic that drives the APT's quasi-arbitrage proof.
- **`cfa-equity-valuation` / `cfa-economics`**: factor-based expected return estimation in the curriculum framing.
