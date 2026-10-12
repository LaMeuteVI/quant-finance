# Chapter 1: Introduction
> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed. (Wiley, 2012) | Chapter 1, pp. 1–21

## Core Idea
Risk management exists because the shareholder's risk–return calculus and the firm's own risk–return calculus are **not the same**. A shareholder should only charge for *systematic* risk; the firm must survive, and regulators supervise *total* risk. Two complementary mechanisms manage risk — **risk decomposition** (fix each exposure one by one) and **risk aggregation** (rely on diversification) — and every institution in this book uses both.

## Frameworks Introduced
- **Markowitz mean–variance framework**: characterise every risky investment by `(μ, σ)`; portfolios of two risky assets satisfy `μ_P = w₁μ₁ + w₂μ₂` (Eq. 1.1) and `σ_P = √(w₁²σ₁² + w₂²σ₂² + 2ρw₁w₂σ₁σ₂)` (Eq. 1.2).
  - *When to use*: screening and first-pass sizing of multi-asset portfolios; the basis of mean–variance optimisation (chapter 13 of `cfasi-portfolio-construction`).
  - *How*: estimate `(μ₁,σ₁)`, `(μ₂,σ₂)`, `ρ` from history → sweep `w₁ ∈ [0,1]` → plot the `(σ_P, μ_P)` locus → pick the northwest-most point.
  - *Why it works / failure mode*: diversification benefit scales with `−ρ`, so the locus bends northwest whenever `ρ < 1`. It fails because it is **mean–variance only** — it ignores skewness, kurtosis and tail dependence, which is exactly what the rest of this book is built to measure.

- **The Efficient Frontier**: the limit of how far one can move "northwest" in `(σ, μ)` space; no portfolio dominates a point on it. With a risk-free asset it becomes the **Capital Market Line** `FM` (tangent from point F to the risky frontier), and `M` is the **market portfolio**.
  - *How*: point `I` holds `β_I` in `M` and `1 − β_I` in bills; point `J` borrows `β_J − 1` at `R_F` and puts everything in `M`: `E(R_I) = (1−β_I)R_F + β_I E(R_M)`, `σ_I = β_I σ_M`; `E(R_J) = (1−β_J)R_F + β_J E(R_M)`, `σ_J = β_J σ_M`. The same formulas hold for `β_I < 1` and `β_J > 1`.
  - *Failure mode*: the line is straight **only** under six restrictive assumptions (Hull's list): two-moment preferences, independent residuals across assets, common single-period horizon, borrowing/lending at one risk-free rate, no taxes, and **homogeneous expectations**. Real returns are non-normal (skew, excess kurtosis) and residuals are cross-sectionally correlated — Ford and GM is the textbook counter-example.

- **Capital Asset Pricing Model (CAPM)**: regress `R = a + βR_M + ε` (Eq. 1.3) and require `E(R) = R_F + β(E(R_M) − R_F)`. `β` = systematic risk, `α` = value added by management. Because all investors hold `M`, the value-weighted average alpha across investors is zero.
  - *Practitioner rule*: use CAPM beta as the **performance benchmark**, not as the risk engine. Estimate alpha by comparing realised return against `R_F + β(R_M − R_F)`.
  - *Failure mode*: betas are unstable; a single-factor market model cannot price a book with two sector-specific factors. Move to **Arbitrage Pricing Theory** — multi-factor, `R = a + β₁F₁ + … + β_k F_k + ε`, each factor a separate source of systematic risk, with unsystematic risk defined as the residual unrelated to *all* factors.

- **Risk aggregation vs. risk decomposition**:
  - *Risk decomposition*: front office splits the book by risk factor (one trader per FX pair, rate curve, equity index); each trader holds that factor's risk measures inside daily limits; breaches require hedging trades or a documented limit waiver before the close.
  - *Risk aggregation*: middle office nets the whole book across all factors daily, exploiting diversification; when aggregate risk is too high, diagnose the source and act.
  - *Which to use when*: decomposition for **market** risk and for idiosyncratic credit (credit derivatives since the late 1990s allow single-name and index protection); aggregation for **credit portfolios** (10,000 names at 0.01% each beats 40% to one borrower) and for **insurance** (one auto policy is unforecastable; 100,000 are).
  - *Why it works*: aggregation works only if exposures are genuinely uncorrelated — a small Texas bank lending only to oil is far less diversified than a global bank.

- **Bankruptcy-costs argument**: the reason a firm must care about total, not just systematic, risk. Distress destroys value — customers and suppliers defect, assets must be sold below fair value, brand/reputation is impaired, fees to accountants and lawyers run, and the firm stops being run for shareholders. Lenders price this in as higher interest, so equity ultimately bears the expected bankruptcy cost.
  - *Magnitude (Business Snapshot 1.1)*: a $2bn-market-cap acquirer paid $1bn cash for a related business, resold it three years later for $100m (10% of price), then went bankrupt. Professional fees ran ≈ **$10m/month**; after two years and three restructurings the successor entity had a market cap of **$700,000**, wholly owned by banks and bondholders — shareholders got nothing. The Lehman Brothers holding-company bankruptcy racked up close to **$2bn** in US and European legal/accounting fees alone (FT, Sept 2010).
  - *Asymmetry that matters for sizing*: a small diversifying acquisition can **reduce** total risk; a large leveraged one can detonate it. Most spectacular corporate failures trace to the second kind.
  - *Why financial institutions are different*: confidence is the funding. If default probability is perceived as anything other than very low, wholesale deposits, commercial paper and other funding dry up and a **solvent** bank is liquidated anyway (Lehman; Northern Rock in the UK).

## Key Concepts
1. **Expected return**: probability-weighted *mean* of outcomes, not the modal or most likely outcome — a persistent misreading that corrupts every downstream risk number.
2. **Standard deviation of return**: `σ_R = √(E(R²) − [E(R)]²)`, the one-period measure of return dispersion.
3. **Correlation** `ρ`: the single parameter that determines whether diversification pays; the pivot between risk aggregation and concentration risk.
4. **Systematic risk**: return variance attributable to common factors; the only component CAPM charges for, and the only one a diversified shareholder cannot shed.
5. **Nonsystematic (idiosyncratic) risk**: firm-specific risk that diversified shareholders can eliminate — but which kills the firm itself.
6. **Beta**: slope of the regression of an asset's return on the market portfolio's return; systematic-risk per unit of capital.
7. **Alpha**: return above CAPM; zero-sum across investors, so positive alpha is always somebody else's negative alpha.
8. **Efficient frontier**: the northwest bound of achievable `(σ, μ)`; a portfolio off it is dominated.
9. **Capital Market Line**: the frontier after adding a risk-free asset — a straight line because borrowing and lending are assumed at the same `R_F`.
10. **Risk decomposition**: identifying and managing risks one at a time (front-office, single-factor limit ownership).
11. **Risk aggregation**: reducing risk by portfolio diversification (middle-office, whole-book netting).
12. **Bankruptcy costs**: the value destroyed in the bankruptcy process itself; the economic reason firms cap total risk.
13. **Regulatory capital anchor**: if there is a 0.1% probability of a ≥$2bn annual loss, a regulator can justify requiring $2bn of equity — covering the loss with 99.9% probability.
14. **Investment grade**: `BBB− / Baa3` and above; below is noninvestment grade = speculative = junk. Moody's ladder `Aaa, Aa, A, Baa, Ba, B, Caa, Ca, C` maps to S&P `AAA … C`; `BBB+ ≈ Baa1`.
15. **Rogue-trader losses**: Barings 1995, Allied Irish Bank 2002, Société Générale 2007, UBS 2011 — all traceable to weak front-office position-data collection procedures, not to exotic models.

## Formulas & Reference Tables
`μ_P = w₁μ₁ + w₂μ₂` (Eq. 1.1); `σ_P = √(w₁²σ₁² + w₂²σ₂² + 2ρw₁w₂σ₁σ₂)` (Eq. 1.2); `R = a + βR_M + ε` (Eq. 1.3); `E(R) = R_F + β[E(R_M) − R_F]`; `E(R_P) = R_F + β(R_M − R_F)` (realised-market version).

Table 1.1 — one-year return on $100,000 in a stock:

| Probability | Return |
|---|---|
| 0.05 | +50% |
| 0.25 | +30% |
| 0.40 | +10% |
| 0.25 | −10% |
| 0.05 | −30% |

Table 1.2 — two-asset frontier (`μ₁=10%, σ₁=16%; μ₂=15%, σ₂=24%; ρ=0.2`), all recomputed:

| `w₁` | `w₂` | `μ_P` | `σ_P` |
|---|---|---|---|
| 0.0 | 1.0 | 15% | 24.00% |
| 0.2 | 0.8 | 14% | 20.09% |
| 0.4 | 0.6 | 13% | 16.89% |
| 0.6 | 0.4 | 12% | 14.87% |
| 0.8 | 0.2 | 11% | 14.54% |
| 1.0 | 0.0 | 10% | 16.00% |

Minimum-variance point is between `w₁ = 0.6` and `w₁ = 0.8`: at `w₁ = 0.8` you get `μ_P = 11%` at `σ_P = 14.54%`, which **dominates** both the 60/40 mix and investment 1 alone (10%, 16%).

## Mental Models
- **Use CAPM when** benchmarking an active manager's realised return; **use APT/factor models when** the book is exposed to sector or style factors CAPM omits — because a one-factor model prices Ford and GM as if their only shared driver is "the market".
- **Use aggregation when** exposures are genuinely independent (auto claims, granular loan books); **use decomposition when** they are one concentrated position (a single-FX trader, a single-name credit) — aggregation on a book of one is just position sizing.
- **Ask "who bears this risk?" before aggregating.** Diversification is only free for risks the firm can actually shed; operational and reputation risk sit inside the firm and cannot be netted away.
- **Think bankruptcy costs, not just CAPM, when sizing any large or leveraged move.** Expected value alone approved the acquisition in Business Snapshot 1.1; the $10m/month fee burn and the $700k residual equity show what the firm actually owned.
- **When in doubt about model assumptions, check the CAPM assumption list.** Six assumptions, four of which (two-moment preferences, independent residuals, homogeneous expectations, common horizon) are plainly false in practice — which is precisely why the rest of this book measures risk with full distributional machinery.

## Code Examples
```python
import numpy as np

def two_asset_frontier(mu, sigma, rho, w1_grid=np.linspace(0, 1, 201)):
    w1 = w1_grid; w2 = 1 - w1
    mu_p = w1 * mu[0] + w2 * mu[1]
    var_p = w1**2 * sigma[0]**2 + w2**2 * sigma[1]**2 + 2 * w1 * w2 * rho * sigma[0] * sigma[1]
    return w1, mu_p, np.sqrt(var_p)

# Table 1.2 reproduction
w1, mu_p, sd_p = two_asset_frontier([0.10, 0.15], [0.16, 0.24], 0.2)
for target in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    i = np.argmin(abs(w1 - target))
    print(f"w1={w1[i]:.1f}  mu={mu_p[i]:.4%}  sigma={sd_p[i]:.4%}")

def capm_required_return(rf, beta, mu_market):
    return rf + beta * (mu_market - rf)

def capm_alpha(observed_return, rf, beta, rm):
    """alpha = realised return minus the CAPM benchmark for that beta."""
    return observed_return - (rf + beta * (rm - rf))
```
`⚠ reconstructed` — the book gives the formulas and tables, not code.

## Worked Example
**Two-asset frontier (Table 1.2, fully recomputed).** `μ₁ = 10%, σ₁ = 16%, μ₂ = 15%, σ₂ = 24%, ρ = 0.2`.

- `w₁ = 0.6, w₂ = 0.4`: `μ_P = 0.6(10%) + 0.4(15%) = 12.00%`.
  `σ_P² = 0.36(0.16²) + 0.16(0.24²) + 2(0.6)(0.4)(0.2)(0.16)(0.24) = 0.009216 + 0.009216 + 0.0036864 = 0.0221184`
  `σ_P = √0.0221184 = 0.148723` → **14.87%**.
- `w₁ = 0.8, w₂ = 0.2`: `σ_P² = 0.64(0.0256) + 0.04(0.0576) + 2(0.8)(0.2)(0.2)(0.16)(0.24) = 0.016384 + 0.002304 + 0.0024576 = 0.0211456`; `σ_P = 0.145416` → **14.54%**.

**Interpretation:** at `w₁ = 0.6` you are 2pp better in expected return and 1.13pp better in risk than asset 1 alone — the textbook diversification gain. Pushing to `w₁ = 0.8` drops risk a further 0.33pp while giving up only 1pp of return, which is why the minimum-variance weight sits on the 0.6–0.8 segment. Analytic minimum: `w₁* = (σ₂² − ρσ₁σ₂)/(σ₁² + σ₂² − 2ρσ₁σ₂) = (0.0576 − 0.00768)/(0.0256 + 0.0576 − 0.01536) = 0.04992/0.06784 = 0.7359`.

**CAPM check.** `R_F = 6%`, `E(R_M) = 12%` → required return at `β = 0.2, 0.5, 1.4` is **7.2%, 9.0%, 14.4%** (recomputed).

**Hedge-fund alpha check (Q1.14).** Market returned 10%, `R_F = 5%`, `β = 0.6`, `α = 4%` → return = `0.05 + 0.6(0.10 − 0.05) + 0.04 = 0.12` → **12%**.

## Anti-patterns
- **Confusing "expected" with "likely".** Expected return is the mean. A portfolio with a 0.05 probability of −30% can have a 10% expected return. Never read an expected value as a modal value.
- **Diversifying away survivable risk but not survival risk.** Shareholder logic says ignore idiosyncratic risk; that logic will bankrupt the company. Never let CAPM justify an un-hedged concentration.
- **Assuming correlation is stable.** `ρ` is estimated, regime-dependent, and rises precisely in the states that matter (crashes). Diversification benefits computed on calm-period `ρ` vanish in the tail.
- **Using only two moments.** Skewness and excess kurtosis are ignored by mean–variance; the whole of chapters 10–14 exists to fix that.
- **Deploying capital structure trade-off theory without the bankruptcy-cost side.** WACC arithmetic alone will happily lever a company into insolvency.
- **Diversifying into correlated regimes without checking.** Lenders across sectors/geographies look diversified in a single year and are not across a cycle.

## Practitioner Notes
- **CRO mandate:** the risk function's primary responsibility is to understand the portfolio of risks *currently taken and planned*, decide whether they are acceptable, and if not, specify the action. Analysis alone is not the deliverable.
- **Escalation discipline:** when a risk measure is heading outside limits near the close, the trader's only two options are hedging trades or a special permission to keep the position. "It will come back tomorrow" is not one of them.
- **Middle-office aggregation** is where diversification is actually harvested — and where a single-factor view can be checked against the whole book.
- **Credit diversification recipe:** 10,000 borrowers at 0.01% of funds each beats 40% to one name; prefer distinct geographies and industries. Even perfect diversification leaves systematic risk — the default rate itself is cyclical (≈1% in an average year, lower in booms, materially higher in downturns).
- **Credit derivatives** allow decomposition of credit risk and index-level protection against economy-wide defaults; note the base rate — for every protection buyer there is a seller, and many sellers (CDO tranches, monoline insurers) took outsized losses in 2007.
- **Ratings:** Moody's, S&P, Fitch; treat a rating as an attribute of the issuer rather than of an individual bond, and remember notched categories (`AA+/AA/AA−`, `Aa1/Aa2/Aa3`) plus the investment-grade boundary at `BBB− / Baa3`.
- **⚠ Practitioner update (as of 2026)**: the S&P US-sovereign downgrade to `AA+` mentioned in the text dates the book to August 2012 and has been superseded many times since; treat sovereign ratings as time-varying, not fixed. Basel capital measurement (chapters 15–18) is likewise dated: see the 2026 status notes in those chapters and the EU/UK FRTB and Basel III Endgame delay trackers before citing any regulatory number as current.

## Key Takeaways
1. Risk–return trade-offs are between risk and **expected** return; expected return is the probability-weighted mean.
2. `σ_P = √(w₁²σ₁² + w₂²σ₂² + 2ρw₁w₂σ₁σ₂)` — `ρ` alone decides whether combining assets creates or destroys risk.
3. Adding a risk-free asset makes the efficient frontier the straight **Capital Market Line**, and every investor should hold the same **market portfolio** `M` at the point of tangency.
4. CAPM prices a single factor; **APT** is its multi-factor extension, with one source of systematic risk per factor.
5. Shareholders should care about systematic risk; **companies must care about total risk** because of bankruptcy costs and because regulators supervise total risk.
6. **Risk decomposition** and **risk aggregation** are complements, not alternatives: front office decomposes by factor, middle office aggregates the book.
7. Regulators size capital off a loss-probability statement: 0.1% chance of ≥$2bn loss ⇒ $2bn equity covers it with 99.9% probability.
8. Rogue-trader blowups (Barings, AIB, SocGen, UBS) were data-and-controls failures long before they were modelling failures.

## Connects To
- **ch02**: takes the bank's balance sheet and shows which of these risks actually dominate a bank.
- **ch07**: replaces the two-moment world of this chapter with risk-neutral vs real-world valuation, the foundation of every forecast the agent will build.
- **ch11**: `ρ` is introduced as a constant here; copulas show what happens when it is stochastic and tail-dependent.
- **ch12**: the loss-probability anchor in §1.5 is exactly what VaR and Expected Shortfall quantify — the book's regulatory core.
- **`hull-derivatives`**: CAPM/APT and the market portfolio are the same theory Hull develops into risk-neutral pricing.
- **`cfasi-portfolio-construction`**: implements the efficient-frontier / mean–variance machinery of §1.1–1.2 at portfolio scale.
- **`cfa-portfolio-management`**: beta, alpha, the Capital Market Line and the CAPM benchmark in exam-legal form.
- **`cfa-wealth-institutional-management`**: the "financial institutions care about total risk" argument applied to GIPS-style institutional portfolios.
