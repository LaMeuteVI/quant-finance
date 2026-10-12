# Chapter 12: Using Multifactor Models
> **Source**: CFA Program Curriculum 2022, Level II, Reading 39 · Portfolio Management | Jerald E. Pinto, PhD, CFA, and Eugene L. Podkaminer, CFA (case "Constructing Multifactor Portfolios" by Yin Luo and Sheng Wang, Wolfe Research)

## Core Idea
Returns of many assets are driven by a small set of systematic factors, and the arbitrage pricing theory (APT) says expected return is then linear in factor sensitivities. Multifactor models turn that into a working toolkit: price assets, split a manager's active return into factor tilts and security selection, split active risk (tracking error) into active factor risk and active specific risk, build factor/index-replicating portfolios, and decide which priced risks you are best placed to bear. The question to ask of any active manager is "how much of the result was a factor bet versus real stock picking?"

## Learning Outcomes Covered
- Describe APT, its assumptions and its link to multifactor models
- Define arbitrage opportunity and determine whether one exists
- Calculate expected return from factor sensitivities and factor risk premiums
- Describe and compare macroeconomic, fundamental and statistical factor models
- Explain sources of active risk; interpret tracking risk and the information ratio
- Describe uses of multifactor models and interpret their output
- Describe the benefits of considering multiple risk dimensions

## Frameworks Introduced
- **Arbitrage Pricing Theory (APT, Ross 1976)**: for well-diversified portfolios, `E(Rp) = RF + λ₁βp,1 + … + λKβp,K`.
  - When to use: pricing portfolios/assets when more than one source of systematic risk matters, or to test for mispricing.
  - How: (1) assume a K-factor return-generating process; (2) assume enough assets to diversify away specific risk; (3) assume no arbitrage among well-diversified portfolios. Estimate λ (factor risk premiums) and RF from portfolios with known sensitivities (K+1 equations for K+1 unknowns). Compare each portfolio's quoted expected return with the model value.
  - Why it works / failure mode: any deviation from the line lets you build a zero-investment, zero-factor-risk portfolio with positive expected profit, and buying pressure restores the line. APT does not name or count the factors; wrong factor choice means "mispricing" is just model error. Needs well-diversified portfolios, not single stocks.
- **Arbitrage test (replication)**: Form a portfolio of existing portfolios with the same factor sensitivities as the target; if expected returns differ, buy the cheap one (higher return) and short the replicating mix.
- **Three model families**: macroeconomic (factors are surprises, sensitivities by regression), fundamental (factors are returns to attributes, sensitivities specified first), statistical (factors extracted from return data: factor analysis or principal components).
- **Carhart four-factor model**: `Rp − RF = ap + bp1·RMRF + bp2·SMB + bp3·HML + bp4·WML + εp` (market, size, value, momentum).
- **Active return decomposition**: Active return = Σₖ (portfolio sensitivityₖ − benchmark sensitivityₖ) × factor returnₖ + security selection.
  - When to use: evaluating a manager, checking that "stock picker" claims hold.
  - How: take beginning-of-period sensitivities for portfolio and benchmark, difference them, multiply by realized factor returns, sum = return from factor tilts; the remainder of the active return = security selection.
  - Failure mode: a manager can look skilled when one factor tilt coincided with a strong factor return; selection may be zero or negative.
- **Active risk decomposition**: Active risk squared = active factor risk + active specific risk. Decompose in variance (additive), then take the square root for tracking error.
- **Factor (pure) portfolio**: sensitivity 1 to one factor and 0 to all others; use it long to bet on, short to hedge, that factor.
- **Multifactor portfolio construction (benchmark vs risk parity)**: equally weight pure factor portfolios (BM) or equalize each factor's risk contribution (RP) using a rolling-window covariance estimate; backtest with rolling-window in-sample/out-of-sample steps.
- **Comparative advantage in bearing risk**: tilt toward priced risks that do not hurt you (e.g., endowment or wealthy investor with secure income takes business-cycle risk) and away from those that do.

## Key Concepts
- **Factor**: a variable or characteristic with which asset returns are correlated; systematic factors are priced (compensated).
- **Factor sensitivity (beta, loading)**: change in asset return per unit change in the factor, holding other factors constant.
- **Factor risk premium (λ)**: expected reward for a portfolio with sensitivity 1 to the factor and 0 to others, above RF.
- **Arbitrage**: risk-free operation, no net investment, expected positive profit (not "risk arbitrage").
- **Factor surprise**: actual minus predicted value of a macro variable; expected value zero.
- **Standardized beta**: `(attribute value − cross-sectional mean)/(cross-sectional stdev)`; 0 = average, 1 = one stdev above. Industry membership uses 0/1 dummies.
- **Active return**: `Rp − RB`. **Active risk / tracking error (TE) / tracking risk**: `s(Rp − RB)`.
- **Information ratio (IR)**: mean active return per unit of tracking error.
- **Active factor risk / active specific (security selection) risk**: parts of active risk squared due to factor tilts versus residual stock-specific bets.
- **Return attribution vs risk attribution**: sources of excess return vs sources of volatility or tracking risk.
- **Statistical factors**: factor analysis (best explain covariances) or principal components (best explain variances); hard to interpret, no asset-class tuning.
- **Style factors (across asset classes)**: value, momentum, carry, size, low volume/volatility; **Macro factors**: growth, rates, inflation.
- **Smart beta / alternative index**: rules-based systematic tilts to factors, a transparent, low-cost version of what used to be called alpha.

## Formulas & Reference Tables
- General factor model: `Rᵢ = aᵢ + bᵢ₁I₁ + bᵢ₂I₂ + … + bᵢKIK + εᵢ` (E(ε)=0).
- APT: `E(Rp) = RF + Σⱼ λⱼβp,j`; with no riskless asset RF is replaced by λ₀ (zero-factor-risk portfolio return).
- Pure factor portfolio j: `E = RF + λⱼ`, so `λⱼ = E(factor portfolio) − RF`.
- Portfolio parameters: weighted averages of asset intercepts and sensitivities using market-value weights.
- Macroeconomic model: `Rᵢ = aᵢ + bᵢ₁F₁ + … + bᵢKFK + εᵢ`; here aᵢ = expected return, Fₖ = surprise = actual − predicted.
- Fundamental model: factors are returns (not surprises), so intercept is **not** expected return; betas standardized.
- Standardized beta: `bᵢₖ = (Attribute value ik − Average attribute k) / σ(attribute k)`.
- Carhart (equilibrium): `E(Rp) = RF + βp,1RMRF + βp,2SMB + βp,3HML + βp,4WML` (alpha has zero expectation).
- Active return: `Rp − RB`; decomposition `Σₖ(βp,k − βB,k)·Fₖ + security selection`.
- Tracking error: `TE = s(Rp − RB)`; annualize: daily × √250 (or √252), monthly × √12 (assumes serially uncorrelated).
- Information ratio: `IR = (R̄p − R̄B) / s(Rp − RB)` (assumes same systematic risk as benchmark).
- Active risk squared: `s²(Rp − RB) = active factor risk + active specific risk`.
- Active specific risk: `Σᵢ (wᵢᵃ)² σ²εᵢ` (active weights wᵢᵃ = w_portfolio − w_benchmark, σ²εᵢ = residual variance).
- Active factor exposure: `bⱼᵃ = Σᵢ wᵢᵃ bⱼᵢ`; active factor risk = `Σⱼ Σₖ bⱼᵃ bₖᵃ cov(Fⱼ, Fₖ)`. Active factor risk can also be found as active risk squared minus active specific risk.

| | Macroeconomic | Fundamental | Statistical |
|---|---|---|---|
| Factors | Surprises in macro variables | Returns to stock attributes (value, size, leverage, industry) | Portfolios extracted from returns |
| Sensitivities | Estimated by regression after building factor series | Specified first (standardized attributes); factor returns then estimated by regression | Estimated jointly |
| Intercept | Expected return | Not expected return | n/a |
| Number of factors | Few (parsimonious) | Many (e.g., 67 in Connor: 55 industries + 12 others) | Few |
| Interpretation | Good | Best for attribution and style analysis | Poor |
| Best use | Embed economic views | Attribution, risk analysis, manager style | Cross-asset, minimal assumptions |

Connor (1995): macroeconomic factors (5) explained about 11% of return variance for 779 US stocks; BARRA fundamental model about 43% (industries alone 16.3%). Macro factors added nothing once the fundamental factors were included; but no tests of significance, and industry factors are not truly systematic risk.

Typical tracking error ranges (US equity): passive ≤ 0.10%; enhanced index about 2%; diversified active large-cap 2-6%; aggressive active 6-10%+.

Fixed-income factors: duration, credit, currency, geography (Dopfel's 6-sector style model: short/intermediate/long government, investment grade credit, MBS, high yield, weights constrained to sum to 100%).

## Mental Models
- **Surprise, not level**: in a macro model the expected part of inflation or GDP is already in prices (the intercept); only the unexpected part moves returns.
- **Variance adds, volatility does not**: always decompose active risk in variance terms (active risk squared), then sqrt to get TE.
- **Factor bet vs stock pick**: separate the manager's return into "I leaned on HML" and "I chose better stocks". High TE with mostly factor risk = a closet style bet; high specific share = a concentrated stock picker.
- **Pure factor portfolio = a clean hedge or bet**: long to speculate, short to hedge the exposure.
- **Prefer simple weights for multifactor portfolios**: equal weighting of pure factors typically does at least as well as complex optimization; risk parity lowers volatility and about doubles US Sharpe versus equal weight, with lower return.
- **Ask who you are relative to the average investor**: harvest premia on risks you bear cheaply (long horizon, secure income) and avoid risks that hit your liabilities (inflation for cost-escalating endowments).

## Worked Example
**1. APT parameters and arbitrage (recomputed).** Portfolios A (E=7.5%, β=0.5) and B (E=15%, β=2.0): solve `0.075 = RF + 0.5λ` and `0.15 = RF + 2λ` → λ = 5%, RF = 5%. Model: `E = 5% + 5%β`. C (β=0.4) should earn 7.0% (matches). New portfolio D (β=0.45) quoted at 8% vs model 7.25%; 0.5A + 0.5C has β=0.45 and E=7.25%. Buy $10,000 D, short $10,000 of the 50/50 A-C mix: net investment 0, factor beta 0.45 − 0.45 = 0, expected payoff $10,800 − $10,725 = $75. Interpretation: D is underpriced; flows bid its price up until E falls to 7.25%.

**2. Macro model portfolio return.** R_MANM = 0.09 − 1·F_INFL + 1·F_GDP + ε; R_NXT = 0.12 + 2·F_INFL + 4·F_GDP + ε; weights 1/3 and 2/3. Portfolio: intercept 0.11; inflation beta (−1/3 + 4/3) = 1; GDP beta (1/3 + 8/3) = 3. Expected return = 11% (intercept). Surprises: inflation +1%, GDP 0, errors 0.5%: `0.11 + 1(0.01) + 3(0) + (1/3)(0.005) + (2/3)(0.005) = 12.5%`. Interpretation: expected return is the intercept; only the surprise terms move it.

**3. Active return attribution (Carhart, curriculum case).** Active sensitivities (portfolio − benchmark): RMRF −0.05, SMB −0.05, HML +0.40, WML +0.02; factor returns 5.52%, −3.35%, 5.10%, 9.63%. Contributions: −0.2760%, +0.1675%, +2.0400%, +0.1926% = +2.1241% from factor tilts; security selection −0.05%; active return 2.0741%. HML contributes 98% of active return. Interpretation: self-described "stock picker" is a large-cap value manager whose edge was a value tilt in a year value paid; if growth had won, he would have lagged. Question him on HML timing and on his selection discipline.

**4. Active risk decomposition.** Suppose active exposures b = (HML +0.40, SMB −0.20), factor variances 36 and 25 (%²), cov(HML,SMB) = −5. Active factor risk = 0.40²(36) + 0.20²(25) + 2(0.40)(−0.20)(−5) = 5.76 + 1.00 + 0.80 = 7.56 %². With active specific risk 4.44 %², active risk squared = 12.00 %² and TE = 3.46%. Factor share = 63%. Interpretation: most of the tracking risk is deliberate factor tilt, so the manager's skill claim must be about factor timing, not stock selection.

**5. Information ratio.** Portfolio 9%, benchmark 7.5%, TE 6% → IR = 1.5/6 = 0.25 (below a 0.30 minimum in the curriculum's low-active-risk guideline example).

## Anti-patterns
- **Using the APT with single stocks or concentrated portfolios**: the arbitrage argument needs well-diversified portfolios.
- **Treating the intercept of a fundamental model as expected return**: that only holds for macro (surprise) models.
- **Plugging the level of a macro variable instead of its surprise**: predicted values are already in the intercept.
- **Adding standard deviations of risk components**: variances add, vols do not.
- **Reading a high IR from one favorable factor year as skill**: check whether the active return came from tilts.
- **Believing "alpha" is skill when factors are omitted**: size/value/momentum exposure shows up as alpha under a market-only model.
- **Equating statistical factors with economic meaning**: interpretation is usually not possible.
- **Look-ahead bias in backtests**: fit factors/covariance on past windows only; for multifactor allocation the rolling window is applied twice (pure factors, then weights).
- **Counting industry dummies as priced risk**: an investor can simply exclude an industry; it is not systematic risk.

## Exam Focus & Traps
- ⚠ Errata (2022): the solution to Practice Problem 14 should read that, with a macroeconomic factor model, the expected return is the intercept (when all model factors equal zero). So for Portfolio 1, expected return = intercept 2.58%, not the realized return (6.00%) and not intercept + something.
- ⚠ Correction (minor): Example 1 of the text labels Portfolio C's expected return as "E(R_B)"; it is E(R_C) = 0.05 + 0.05 × 0.4 = 0.07.
- APT assumptions: factor model describes returns, many assets so specific risk diversifies, no arbitrage among well-diversified portfolios. "Arbitrage opportunities exist" is the wrong assumption (a common item).
- To find the long/short leg: the portfolio with the higher expected return than its replicating mix is bought; in the practice problem, Fund C (3.0%) vs a 60/40 mix of A and B (2.8%) with equal beta 0.9 → buy C, short the mix.
- Surprise = actual − predicted (e.g., GDP 1.0% vs 1.5% → −0.5%). Compute each factor effect = sensitivity × surprise, then add. Portfolio sensitivity = weighted average.
- Back out expected return from a realized one: realized 5% = E − 1.5(2%) + 2(−3%) + 3% error → E = 11%.
- Active factor risk is not zero for a portfolio whose factor sensitivities differ from the benchmark in any factor, even if it only loads on one factor itself (the benchmark may load on the others).
- IR of an index fund that meets its objective is ~0 (active return about zero). To raise IR a manager can take active factor risk or active specific risk.
- Fundamental factor models are the best choice to analyze a manager's style (growth vs value); statistical models are easiest to apply across asset classes but hardest to interpret. Multifactor models are useful for both active and passive management (passive: replicate index factor exposures with a sample).
- Fundamental model: you first specify sensitivities, then estimate factor returns; macro: first factor series, then estimate sensitivities.
- Pure factor portfolio long = bet on a factor; short = hedge a long exposure (e.g., short portfolio D to hedge time-horizon risk).

## Key Takeaways
1. APT: `E(R) = RF + Σ λβ`; solve λ and RF from portfolios with known betas, then test any new portfolio for mispricing by replication.
2. Know which model type fits the job: macro for embedding economic views, fundamental for attribution and style analysis, statistical for cross-asset use with minimal assumptions.
3. Decompose active return into factor tilts (Δsensitivity × factor return) and security selection; judge a manager on both.
4. Decompose active risk in variance: factor (industry + style) versus specific; use TE and IR for guideline setting (e.g., TE below 3% and IR above 0.30 for a low-active-risk mandate).
5. Index funds should show about 0 active return, ≤ 0.10% TE, and IR near 0.
6. Factor portfolios give clean bets and hedges; multifactor portfolios can be equal-weighted or risk parity, built with a double rolling window to avoid look-ahead bias.
7. Factors extend beyond equity: duration, credit, inflation, growth, carry, momentum, value across asset classes; ESG scores can be layered over a duration/spread decomposition.
8. Use the comparative-advantage lens to choose which priced factor risks to hold, instead of a CAPM two-fund answer for everybody.

## Connects To
- **ch11**: factor and smart-beta ETFs implement these factor exposures; ETF TE is active risk of a passive fund.
- **ch13**: factor sensitivities feed parametric VaR and risk decomposition of portfolio market risk.
- **ch14**: backtesting and rolling-window simulation of factor strategies (look-ahead bias, out-of-sample).
- **ch15**: fundamental law, IC and transfer coefficient connect to IR and active risk.
- **`cfasi-equity-investment-styles`**: factor investing in practice (value, momentum, quality, low volatility).
- **`cfa-quantitative-methods` ch08**: multiple regression used to estimate sensitivities.
- **`cfa-asset-allocation-cme` ch07**: factor-based asset allocation and risk budgeting.
