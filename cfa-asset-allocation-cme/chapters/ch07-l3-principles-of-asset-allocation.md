# Chapter 7: Principles of Asset Allocation
> **Source**: CFA Program Curriculum 2023, Level III, Reading 6 · Asset Allocation | Jean L.P. Brunel, CFA; Thomas M. Idzorek, CFA; John M. Mulvey, PhD

## Core Idea
Strategic asset allocation is the most important step of the investment process, and there are three families of frameworks to set it: asset-only mean-variance optimization (MVO) patched against its input sensitivity, liability-relative methods (surplus optimization, hedging/return-seeking, integrated ALM) when a liability stream exists, and goals-based sub-portfolios when an individual has several goals with different urgencies. Heuristics (60/40, age rules, risk parity, 1/N, endowment model) and a cost-benefit rebalancing policy complete the toolkit. The recurring lesson: the optimizer is only as good as its inputs and as faithful as its definition of risk.

## Learning Outcomes Covered
- Describe/evaluate MVO; recommend and justify an MVO allocation
- Interpret an allocation against the economic balance sheet (human capital, real estate)
- Asset class liquidity in allocation; absolute vs relative risk budgets
- Incorporate client risk needs; Monte Carlo and scenario analysis for robustness
- Investment factors in allocation; allocation based on the global market portfolio
- Liability characteristics; liability-relative approaches; recommend/justify one
- Goals-based allocation; heuristic and other approaches; factors driving rebalancing policy

## Frameworks Introduced
- **Mean-variance optimization (MVO), utility form**: choose weights maximizing `Uₘ = E(Rₘ) − 0.005·λ·σₘ²` (returns in %), subject to budget (Σw = 1) and usually no-short constraints.
  - When to use: asset-only strategic allocation with no explicit liability.
  - How: (1) estimate E(R), σ, correlations; (2) estimate λ from risk preference AND risk capacity; (3) solve numerically (any constraint kills the closed form); (4) read the efficient frontier; pick the point maximizing utility, or the highest-return point under a volatility cap / return target; (5) stress with Monte Carlo.
  - Failure mode: tiny return-input changes (50 bp) rotate whole asset classes in and out; frontier is concentrated; only means and variance count.
- **Reverse optimization (Sharpe 1974) + Black-Litterman (BL)**: back out the returns that make market-cap weights optimal, then tilt them with views.
  - When to use: to anchor expected returns so the optimizer stays diversified; BL when you hold views (absolute or relative, e.g. "APAC ex Japan beats Europe ex UK by 100 bp").
  - How: `μ = r_f + λ·Σ·w_mkt` (equivalently CAPM `r_f + β·MRP`); BL blends these implied returns with views weighted by confidence, and spills small correlated changes into other assets.
  - Why: returns become consistent with systematic risk, so the optimizer sees no free lunch to exploit. BL is a return-generation model, not an allocation model.
- **Resampled MVO (Michaud)**: Monte Carlo many input sets, optimize each, average the weights, pair with base inputs. Smoother, more diversified; criticized for frontier "bumps", over-diversified risky mixes, inherited estimation error, weak theory.
- **Risk budgeting**: allocate total (or active) risk where it earns return. `MCTRᵢ = βᵢ,P·σ_P`; `ACTRᵢ = wᵢ·MCTRᵢ`; ΣACTR = σ_P. Optimal when `(E(Rᵢ) − r_f)/MCTRᵢ` is equal across all assets and equals the tangency Sharpe ratio.
- **Factor-based allocation**: optimize over self-financing factor returns (size = small − large, valuation, credit, duration, market…) with collateral return added to stay in total-return space. Neither factors nor asset classes is inherently superior if exposures are equivalent (Idzorek-Kowara 2013); work in the space where you can make better assumptions.
- **Liability-relative allocation** (three approaches, see table below): surplus optimization, hedging/return-seeking (two-portfolio), integrated asset-liability.
- **Goals-based allocation (modules)**: split wealth into goal sub-portfolios; each goal has a horizon and required probability of success; choose the module with the highest probability- and horizon-adjusted minimum expectation (lowest funding cost), discount the goal cash flows at that rate, and aggregate.
- **Rebalancing corridor policy**: percent-range bands set by cost-benefit (Exhibit 48 below).

## Key Concepts
- **Risk aversion coefficient (λ)**: rate at which an investor gives up expected return for lower variance; typical 1-10, λ ≈ 4 moderate; λ = 0 is risk neutral (picks the max-return portfolio).
- **Certainty-equivalent return**: the Uₘ value, i.e. the risk-free return valued equally to the risky mix.
- **Risk preference vs risk capacity**: willingness (subjective, psychometric) vs ability (objective: net worth, income, emergency fund, savings rate) to bear losses; risk tolerance blends both.
- **Corner portfolio**: frontier point where an asset enters/leaves or a constraint starts/stops binding; mixes between adjacent corners are linear combinations.
- **Global minimum variance portfolio / max-return portfolio**: left and right ends of the constrained frontier; without extra constraints max-return = 100% in the highest-return asset.
- **Tangency portfolio / two-fund separation**: highest-Sharpe risky mix; with a risk-free asset the frontier is a straight line (cash + tangency).
- **Economic balance sheet**: financial assets plus human capital, real estate and other non-traded assets (and liabilities); non-tradable items enter the optimizer as fixed-weight constraints.
- **Conditional vs unconditional inputs**: conditional reflect current valuation/cycle; unconditional are 10+ year averages.
- **Surplus** `= MV(assets) − PV(liabilities)`; **funding ratio** `= MV(assets)/PV(liabilities)`; surplus return `= (ΔAssets − ΔLiabilities)/initial assets`.
- **Legal liability vs quasi-liability**: contractual (DB plan, insurance) vs mission-critical spending (endowment, individual consumption). **Fixed vs contingent** cash flows.
- **Basis risk**: mismatch between hedging portfolio and liabilities.
- **Minimum expectation return**: return achievable with the required probability over the horizon, `E(R)·T − z·σ·√T`, annualized.
- **Labeled goal**: goal described by features (capital preservation, growth) without a defined cash flow.
- **Corridor / tolerance band**: allowed deviation from target weight before rebalancing is triggered.

## Formulas & Reference Tables
- MVO utility: `Uₘ = E(Rₘ) − 0.005·λ·σₘ²` (% inputs); in decimals `Uₘ = E(Rₘ) − 0.5·λ·σₘ²`. Check: E=10%, λ=2, σ=20% gives 10 − 0.5·2·4 = 6%.
- Unconstrained optimum (decimals): `w* = (1/λ)·Σ⁻¹·(μ − r_f·1)`; weights sum to 1 only if μ is reverse-optimized from fully invested weights.
- Reverse optimization: `μ = r_f + λ·Σ·w_mkt`, with `λ = (E(R_mkt) − r_f)/σ_mkt²`; per asset `E(Rᵢ) = r_f + βᵢ,mkt·MRP`.
- Safety-first ratio (Roy): `[E(R_P) − R_L]/σ_P`, maximize; R_L = threshold (e.g. €60k/€1.2m = 5%).
- Risk budgeting: `MCTRᵢ = βᵢ,P·σ_P`; `ACTRᵢ = wᵢ·MCTRᵢ`; `% contribution = ACTRᵢ/σ_P`; optimum: `(E(Rᵢ) − r_f)/MCTRᵢ` equal for all i.
- Surplus objective: `U^LR_m = E(R_s,m) − 0.005·λ·σ²(R_s,m)`.
- Surplus return variance with liability proxied by hedge asset: `σ²_s = Var(Σwᵢ·Rᵢ − (L₀/A₀)·R_L)`.
- Funding ratio = A/L; surplus = A − L; both depend on the discount rate (LOWTECH: 4% gives surplus 0.239bn, ratio 1.106; 2% gives −0.539bn, 0.823).
- Risk parity: `wᵢ·Cov(rᵢ, r_P) = σ²_P/n` for all i; no closed form; then lever or hold cash to the desired risk.
- Minimum expectation (iid): `E(R)·T − z·σ√T` over T years, annualize; z = 1.28 (90%), 1.645 (95%), 2.33 (99%), 0.674 (75%).
- Goal capital = PV of goal cash flows at the module's adjusted return; overall allocation = capital-weighted average of module weights; surplus capital goes to a chosen "labeled" module.
- Heuristics: equity % = `120 − age` (or 100/125 variants); 60/40; 1/N.
- Rebalancing corridor drivers (percent-range policy, all else equal):

| Factor | Effect on corridor width | Reason |
|---|---|---|
| Transaction costs up | Wider | Higher hurdle for rebalancing benefit |
| Risk tolerance up | Wider | Less sensitivity to drift |
| Correlation with rest of portfolio up | Wider | Co-movement limits further divergence |
| Volatility of the rest of portfolio up | Narrower | Large drift more likely |
| Own volatility up | Ambiguous (costs vs risk); in practice wider and proportional (volatility-based, equal-probability) | Cost control |
| Capital gains tax rate up (taxable) | Wider | Each trade realizes tax |
| Illiquid asset | Wider | Trading cost |

- Liability-relative approaches compared:

| | Surplus optimization | Hedging/return-seeking | Integrated asset-liability |
|---|---|---|---|
| Complexity | Simple | Simple | Highest |
| Link A-L | Linear correlation | Linear or non-linear | Linear or non-linear |
| Risk levels | All | Conservative (basic case) | All |
| Funded status | Any | Positive surplus for basic case | Any |
| Periods | Single | Single | Multi-period |
| Typical user | Pension plans | Insurers, overfunded DB | Banks (ALM), P&C insurers (DFA) |

- Liability characteristics (Exhibit 23): fixed vs contingent flows; legal vs quasi; duration and convexity; size relative to sponsor; drivers (inflation, growth, rates, risk premium); timing/longevity; regulation on valuation.

## Mental Models
- **Optimizer = error maximizer**: it overweights assets whose inputs are accidentally too good; cure the inputs (reverse optimization/BL), not the output.
- **Constraints are either reality or crutches**: model real constraints (non-tradable house, liquidity caps, policy limits); if you need many constraints to tame output, you have specified the allocation by hand and should fix the inputs.
- **Surplus risk, not asset risk, is what a liability holder bears**: low-risk end of the frontier is the hedging asset (bonds), not cash.
- **Goals-based = swap the risk definition**: volatility becomes probability of missing the goal; need-type goals (90-99%) get a safe module, wishes and dreams (below 60-75%) get a risky one and cost less capital.
- **Equal dollars is not equal risk**: a 54/46-style mix can carry most of its variance from equities; risk budgets expose it, risk parity forces equality but ignores returns.
- **Rebalancing is a short-volatility, liquidity-supplying discipline**: it pays a diversification return when costs are low; widen bands where trading is expensive.

## Worked Example
**1. Utility and safety-first (Goddard, λ = 2, threshold 5%).** `U = E − 0.01σ²` (0.005·2). A (10, 20): 10 − 4 = 6.0. B (7, 10): 7 − 1 = 6.0. C (5.25, 5): 5.25 − 0.25 = 5.0. A and B tie on utility; tie-break with `(E − 5)/σ`: A 0.25, B 0.20, C 0.05. Recommend A (highest chance of clearing 5%, so the €60k withdrawal rarely invades capital). Same function with λ = 8 on (10, 12), (8, 8), (6, 2) gives 4.24, 5.44, 5.84: the high-λ client picks the safest, C.

**2. Risk-free asset overlay (CFFA).** Needs 6.5% nominal `= (1.04)(1.02)(1.004) − 1`. Tangency corner portfolio 4 (7.24%, σ 11.65%, Sharpe 0.433), r_f 2.2%. `6.5 = 7.24w + 2.2(1 − w)` gives w = 0.853; σ = 0.853·11.65 = 9.94%; Sharpe = 0.433 (verified). Blending corners 4 and 5 would hit 6.5% with lower Sharpe, so it is off the efficient line. (The source text prints "6.4"; 6.50 is correct.)

**3. Surplus vs asset-only optimization (own illustration, recomputed).** LOWTECH: A₀ = 2.5bn, PV(L) = 2.261bn at 4% so k = L/A = 0.904. Two assets: equities (7.5%, σ 18%) and corporate bonds (4.9%, 5.6%); liability return = bond return; ρ(eq, bonds) = −0.38; λ = 4. Weight w in equities: surplus return `= w·7.5 + (1−w)·4.9 − k·4.9`; surplus variance from weights (w equities, 1−w−k bonds).
- Surplus: w = 0 gives 0.47%, σ 0.54%; w = 0.2 gives 0.99%, σ 3.86%; w = 0.5 gives 1.77%, σ 10.08%.
- Utility-maximizing equity weight: **16.6%** (U = 0.70) in surplus space vs **31.2%** (U = 5.11) asset-only; minimum-risk equity weight 1.5% (surplus) vs 16.1% (asset-only).
- Interpretation: liability awareness cuts equity risk and makes bonds, not cash, the anchor. The funding ratio of 1.106 and surplus 0.239bn become 0.823 and −0.539bn at a 2% discount rate, so the discount rate is a first-order input.

**4. Goals-based (Smiths, US$25m, 2% inflation, spending 500k).** Module with highest horizon/probability-adjusted return per goal: Goal 1 (5y, 95%) Module A at 2.3% gives 2,430k (payments end of year, inflated from year 2); Goal 2 (25y, 85%, from year 6) F at 6.1% gives 6,275k; Goal 3 (10y, 90%, 10m bullet) D at 4.1% gives about 6.67-6.69m (rounding of the 4.1%); Goal 4 (20y, 75%, 10m) F at 6.8% gives about 2.68m. Total ≈ 18.05m, leaving 27.8% surplus in "capital preservation" Module C. Overall portfolio = capital-weighted module mix (E 7.2%, σ 8.0%). Minimum expectation check: portfolio E 7%, σ 10%, 5y, 90%: 35% − 1.28·22.4% = 6.3% total = about 1.2-1.3% a year, far below 7%.

## Anti-patterns
- **Feeding raw historical means into an optimizer**: yields 4-5 asset concentration and big swings; anchor with reverse optimization/BL.
- **Using constraints to hide bad inputs**: if constraints are doing the diversifying, revisit assumptions.
- **Treating cash as free of consequences**: either optimize it as a (low-risk) asset or size it from liquidity needs, but be explicit.
- **Proxying illiquid assets with an index and ignoring the vehicle**: private equity funds carry idiosyncratic risk the index diversified away; listed proxies overlap other asset classes and inflate correlations.
- **Equal weights mistaken for diversification**: sources of risk can be undiversified (equities carrying about 87% of variance in a 65/35 mix).
- **Risk parity without returns or leverage thought**: ignores expected returns, depends on opportunity set composition (7 equity + 3 bond classes means 70% equity risk), needs cheap leverage.
- **Applying goals-based machinery to a single-goal saver** without checking for hidden goals; or using surplus optimization without understanding the liability's drivers.
- **Discounting goals at expected return**: understates capital for need-type goals.

## Exam Focus & Traps
- Weights in surplus optimization are not asset-only weights: conservative end = hedging bonds, not cash. As risk tolerance rises, the two frontiers converge (identical at the max-return portfolio).
- Optimum from risk budgeting: ratio of excess return to MCTR equal across assets (not minimum total risk; Statement "different for all assets" is wrong).
- Risk parity: lowest-covariance asset (domestic bonds) gets weight above 1/n.
- Rebalancing band questions: higher transaction costs, illiquidity, taxes, risk tolerance, and correlation all widen; volatility of rest of portfolio narrows; higher own volatility widens in practice. Tax and illiquidity push wider, not narrower.
- Funding ratio when rates rise and A and L fall by the same dollars: ratio falls (205/241 = 0.851 to 180/216 = 0.833) because the plan is underfunded (A < L), so an equal dollar drop is a larger percentage hit to assets than to liabilities. Never assume an unchanged ratio.
- Hedging/return-seeking: hedge amount = PV(liabilities) (e.g. 85% = 8.5/10 into index-linked bonds if liabilities are inflation-driven); remaining surplus to return-seeking.
- Reverse optimization: weights are inputs, returns outputs (MVO is the opposite). Implied returns `r_f + β·MRP`, e.g. 2 + 0.6·5.5 = 5.3%.
- Goals-based: choose the module with the highest adjusted return for the given horizon and probability; the riskiest module is not always best at high success levels (at 99%, 5y, cash-heavy A wins).
- Factor-based: factors are zero-investment so low correlations; they resemble structural multi-factor model factors.
- ⚠ Correction: the reading text says the Exhibit 19 mix is about 54/46 equity/fixed income with 74% of risk from equities; the exhibit's own weights and ACTRs sum to about 65% equities (incl. REITs) / 35% bonds and about 87% / 13% of risk. Direction (risk more concentrated than capital) is right; do not quote the 54/74 figures.
- Percent weights in Exhibit 16 (resampled frontier) have corrupted axis labels in the source extraction; ignore the axis values.

## Key Takeaways
1. Pick the allocation by maximizing `E(R) − 0.005λσ²`; estimate λ from both willingness and capacity, then validate with Monte Carlo (essential when cash flows make wealth path-dependent).
2. Fix MVO instability at the input level: reverse optimization from market weights, Black-Litterman for views, resampling and real constraints as supplements.
3. Include human capital and housing as fixed-weight assets: a stable-income professional can hold more risk and should avoid assets correlated with her job.
4. Use risk budgets: optimal when excess return per MCTR is equal; check where the risk really comes from.
5. For liabilities, characterize them first (fixed/contingent, legal/quasi, duration, inflation link, longevity, regulation); the discount rate changes funding status.
6. Choose surplus optimization for general plans, hedging/return-seeking for conservative or overfunded investors with a positive surplus, integrated ALM for banks and P&C insurers.
7. For individuals with multiple goals, fund each with a module matched to horizon and urgency and size capital using minimum-expectation returns; review horizons and rebalance because portfolios will usually outperform the conservative discount rate.
8. Set rebalancing corridors by cost-benefit: widen for costs, illiquidity, taxes and high correlation; narrow when the rest of the portfolio is volatile.

## Connects To
- **ch03 / ch04**: capital market expectations framework and forecasting methods that supply the optimizer inputs.
- **ch06**: overview of asset allocation (strategic vs tactical, rebalancing introduction) that this chapter builds on.
- **ch08**: adds real-world constraints (taxes, liquidity, regulation) to these frameworks.
- **ch01 / ch02**: behavioral roots of mental accounts and goals-based investing.
- **`cfa-portfolio-management` ch05-ch06**: efficient frontier, CAPM and portfolio math underlying MVO.
- **`cfasi-portfolio-construction` ch01**: practitioner asset allocation (life insurers).
- **`cfa-wealth-institutional-management` ch04**: institutional liability profiles (DB plans, insurers, endowments).
- **`cfa-fixed-income` ch13**: liability-driven investing, immunization and cash flow matching for the hedging portfolio.
