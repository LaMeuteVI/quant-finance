# Chapter 8: Asset Allocation with Real-World Constraints
> **Source**: CFA Program Curriculum 2023, Level III, Reading 7 · Asset Allocation | Peter Mladina; Brian J. Murphy, CFA; Mark Ruloff, FSA, EA, CERA

## Core Idea
A textbook efficient frontier assumes every owner can buy everything, frictionlessly, forever. Real allocation is bent by five forces: asset size and governance capacity, liquidity (of the owner's needs and of the asset classes), time horizon, external rules (regulation, taxes, ESG, religion), and the owner's own behavioral biases. The practitioner's job is to translate each constraint into modified inputs (after-tax returns, fixed weights, caps), a rebalancing policy, and a process that survives stress.

## Learning Outcomes Covered
- Size, liquidity, horizon, regulatory and other considerations as constraints on asset allocation
- Tax considerations in allocation and rebalancing (after-tax optimization, corridors, asset location)
- Recommend and justify revisions when objectives or constraints change
- Short-term (tactical) shifts in asset allocation
- Identify behavioral biases in allocation and how to mitigate them

## Frameworks Introduced
- **Constraint screen (size, liquidity, horizon, external)**: before optimizing, prune the opportunity set and fix inputs for each constraint.
  - When to use: every asset allocation study, and every re-evaluation.
  - How: (1) size and governance: can the owner access and monitor the asset class (minimums, qualified-purchaser rules, number of managers needed, share of manager AUM)? (2) liquidity: map expected outflows and stress them against asset liquidity; (3) horizon: set goal dates, expected human-capital run-off, liability duration; (4) external: regulatory caps, tax status, funding/accounting rules, credit covenants, mission screens; (5) encode as sub-asset-class limits, fixed weights or set-asides in the optimizer.
  - Failure mode: designing the allocation first and discovering later that it cannot be implemented (e.g. 15% private equity for a small, unstaffed fund).
- **After-tax portfolio optimization**: replace each asset's pre-tax return and risk by after-tax values, keep correlations, optimize.
  - How: `r_at = r_pt(1 − t)` (interest); `r_at = p_d·r_pt(1 − t_d) + p_a·r_pt(1 − t_cg)` (equities); `σ_at = σ_pt(1 − t)`; correlations unchanged; value tax-deferred balances at `v_at = v_pt(1 − t_i)`; optimize allocation and asset location jointly by treating each asset in each account type as its own asset.
  - Why: pre-tax and after-tax risk/return differ materially by asset, so adjusting after the fact is suboptimal. Interest-heavy assets (high yield) get cut most; low-risk IG bonds keep their risk-reducing role.
- **Strategic asset location**: put tax-inefficient assets (taxable bonds, high-turnover strategies, high dividend payers) in tax-deferred/exempt accounts; put equities taxed at low capital-gains rates in taxable accounts. Exception: bonds funding near-term spending stay accessible in taxable accounts.
- **Tax-adjusted rebalancing range**: `R_at = R_pt/(1 − t)`; a taxable account needs a wider band for equal risk.
- **Re-evaluation triggers (goals, constraints, beliefs)** and **glide paths**: pre-programmed changes tied to age or funded status written into the IPS.
- **Tactical asset allocation (TAA)**: short-term deviations from the strategic (SAA) policy portfolio within IPS ranges; discretionary (qualitative) or systematic (value, carry, momentum/trend signals).
- **Behavioral-bias controls**: formal process, global market portfolio as starting point, strict policy ranges, multiple risk frames, goals-based sub-portfolios, strong governance.

## Key Concepts
- **Economies/diseconomies of scale**: large owners cut per-participant governance cost, negotiate fees and access private markets (large DB plans beat small ones by about 45-50 bp a year risk-adjusted), but struggle to deploy into capacity-limited active strategies.
- **Governance capacity**: staff, expertise and committee discipline needed to run complex asset classes; it is a binding constraint for small owners (roughly institutions under US$500m, private wealth under US$25m).
- **Qualified purchaser / elective professional client / Professional Investor**: investor classifications gating private funds (US: natural person US$5m of investments; UK: two of three criteria incl. €500k portfolio; Hong Kong: HK$8m portfolio).
- **Liquidity needs vs liquidity of asset classes**: two dimensions that must be integrated and stress tested.
- **Illiquidity premium**: extra expected return for long-horizon owners (endowments, SWFs), unavailable to owners facing near-term payouts (e.g. frozen DB plan that may buy an annuity).
- **Time diversification**: belief that risk fades with horizon; under random walk it does not (dispersion of wealth rises).
- **Human capital run-off**: as bond-like human capital shrinks, financial capital shifts toward bonds (Bodie, Merton, Samuelson).
- **Contribution risk**: probability that required sponsor contributions exceed a threshold (e.g. 95th percentile of PV of contributions).
- **Strategic (SAA) vs tactical (TAA) allocation**; **GTAA**: opportunistic cross-asset valuation strategy.
- **Trend following / time-series momentum**: hold asset classes whose trailing 12-month excess return is positive; or moving-average crossover.
- **Loss aversion, illusion of control, mental accounting, representativeness (recency), framing, availability/familiarity (home bias)**: the six allocation-relevant biases.
- **VaR / CVaR**: loss threshold at a probability / average loss beyond it; with normal returns 5% VaR = mean − 1.65σ.
- **Shortfall probability**: probability of missing a stated goal (magnitude not captured).

## Formulas & Reference Tables
- After-tax return: `r_at = r_pt·(1 − t)`; equity with income and growth: `r_at = p_d·r_pt·(1 − t_d) + p_a·r_pt·(1 − t_cg)` (p_d + p_a = 1).
- After-tax risk: `σ_at = σ_pt·(1 − t)` (approximation: losses are muted by the same factor); correlation unchanged.
- After-tax value of tax-deferred assets: `v_at = v_pt·(1 − t_i)` (t_i = expected income tax rate on distribution); tax-exempt: no adjustment.
- After-tax rebalancing range: `R_at = R_pt/(1 − t)`.
- Embedded gains: adjust market value by the tax liability (sell-today approach; or discount the future liability at the after-tax asset return or at the after-tax risk-free rate).
- Time diversification (iid lognormal-like): ending wealth band `W₀·(1 + μ)^T·exp(±1.96·σ·√T)`; this reproduces the source table.
- 5% normal VaR `= μ − 1.65σ`; CVaR is larger in magnitude.
- Asset-size exposure check: `required ticket / manager AUM` should be modest (rule of thumb used: owner at most about 20% of a fund; manager capacity about 50 stocks × 3% of cap).
- Regulatory limits by owner type (examples from the reading):

| Owner | Typical external constraints |
|---|---|
| Insurers | Mostly fixed income; caps on equity (often 10%, up to 30% Switzerland, 50% Mexico), real estate (15% Israel, Korea), non-listed, high yield; risk-based capital, Solvency II; book-value accounting |
| Pension funds | Caps per asset class/entity (Canada 10% per entity, Switzerland 30% real estate, Brazil 70% equity); funding, accounting, contribution rules; US rules reward high equity (higher discount rate lowers pension cost) |
| Endowments/foundations | Tax-linked minimum spending (e.g. 5%); credit covenants; mission/ESG; very long horizon so higher risk allowed |
| Sovereign wealth funds | Mandate limits (KIC no domestic won assets; NBIM real estate max 7%); public scrutiny lowers risk |

- TAA risk constraints: allowable range per asset class around policy; tracking-error budget; predicted-volatility range. TAA evaluation: Sharpe(TAA) vs Sharpe(SAA); information ratio or t-stat of excess return; realized point vs SAA efficient frontier; attribution of over/underweights.
- Re-evaluation triggers: **goals** (business conditions, personal circumstances, risk appetite/capacity), **constraints** (payment changes, large inflow, regulation, horizon change such as lump-sum option, merging plans), **beliefs** (return outlook, trustee change). Formal study at least every five years; annual affirmation.
- Biases and fixes:

| Bias | Allocation symptom | Mitigation |
|---|---|---|
| Loss aversion | Abandoning allocation after losses; herding to peers | Frame risk as shortfall probability; fund high-priority goals with low-risk assets |
| Illusion of control | Extreme corner portfolios, big TAA, concentrated legacy stock | Start from global market portfolio; constraints around market weights; strict ranges |
| Mental accounting | Siloed buckets; keeping founder stock | Goals-based sub-portfolios (put concentrated stock in an aspirational goal) |
| Representativeness/recency | Return chasing; tactical tilts after recent moves | Pre-specified ranges, governance, documented beliefs |
| Framing | Choice driven by presentation (std dev only, first speaker) | Show std dev plus shortfall, VaR/CVaR, stress tests, Monte Carlo |
| Availability / familiarity | Home bias; liquidity over-preference after a crisis | Global market portfolio baseline; do not benchmark to peers |

## Mental Models
- **Feasibility before optimality**: an allocation you cannot implement or hold through a crisis is worth nothing; check ticket sizes, fund minimums, and manager capacity first.
- **Liquidity is a stress concept**: test needs and market liquidity together in a 2008-type event, when liquid assets get sold first and illiquids balloon as a share; rates of return mean-revert but wealth does not.
- **Taxes shrink the distribution, not just the mean**: lower after-tax volatility justifies higher equity allocation and wider bands in taxable accounts.
- **Location before allocation tweaks**: where an asset sits is a free lunch; high-yield and bonds sheltered, growth equity taxable.
- **Match the owner's definition of risk**: a DB sponsor with contribution risk may prefer long bonds even at lower expected return (70/30 with long bonds beats 70/30 aggregate on contribution risk; cutting equity to 60% cuts risk a lot for little extra PV cost).
- **TAA is a small, bounded, costed bet** against the SAA benchmark; it concentrates risk and costs trades and taxes.

## Worked Example
**1. After-tax optimization inputs (interest 40%, dividends/capital gains 25%).** IG bonds 3.0%/4.0% give 1.8%/2.4%; HY 5.0%/10.0% give 3.0%/6.0%; equity 8.0%/20.0% give 6.0%/15.0%; correlations unchanged (IG-HY 0.2, HY-equity 0.7, IG-equity 0). Source results: median-risk mix moves from 25/26/49 (IG/HY/equity) pre-tax to 38/7/55 after tax: HY is cut from 26% to 7%, IG rises, equity rises as its after-tax risk is lower. Extremes (min-risk, max-return) barely change.

**2. Rebalancing band for a taxable account.** Tax-exempt investor: 50% equity, band ±10%. Equities taxed at 25%: `10/(1 − 0.25) = 13.3%`, so 36.7%-63.3% (rounded 37%-63%). Rebalancing less often saves realized gains. Applied: 8.0% pre-tax band corresponds to 10.7% after tax (the $5.5m taxable account takes the 75%±10.7% alternative, the tax-deferred $3.0m account keeps ±8.0%).

**3. After-tax return screen (Young, tax 25%, target at least 6% after tax).** Muni 3% (tax-exempt, no adjustment), small cap 12% to 9.0%, large cap 10% to 7.5%, private equity 25% to 18.75%. Portfolio 3 (30/35/35/0): 0.90 + 3.15 + 2.63 = 6.68% with std dev 15.5%; Portfolio 2: 6.64% at 16.3% and its 5% PE slice (US$275k of 5.5m) is below the US$500k minimum; Portfolio 1: 9.15% but 28.2% risk. Portfolio 3 wins: meets return with the least risk and is feasible.

**4. Behavioral carve-out (Ivy Lee, US$20m).** Lifestyle goal needs US$1m a year for 40 years at 6% (60/40 portfolio, annuity due): PV = US$15.949m (recomputed 15,949,075). Fund it with US$16m diversified (9.6m equities + 6.4m bonds), sell US$11m of the US$15m concentrated stock, keep US$4m for the aspirational gift. This uses mental accounting constructively and quantifies the cost of keeping the stock.

**5. TAA under policy limits (trend signals).** Policy (target / min / max): IG 40 / 35 / 45; HY 10 / 5 / 15; DM equity 40 / 35 / 45; EM equity 10 / 5 / 15. Signals long IG (+3%) and DM equity (+4%), short HY (−3%) and EM (−11%). Tactical weights 45/5/45/5 (all at limits). Realized return with returns 3.45, −6.07, −0.32, −14.6: 0.375% vs policy −0.815%, about +120 bp; Sharpe −0.02 vs −0.23 (rf 0.5%) with slightly higher risk (6.2% vs 5.8%).

## Anti-patterns
- **Copying a large peer's allocation** (private equity, hedge funds) without the scale or staff: leads to fund tickets that are 35-50% of a manager's assets or 40% of a PE fund.
- **Sizing hedge-fund allocations from the asset class, not from fund capacity**: a US$400bn SWF at 5% needs about 150 funds, diluting alpha toward index-like fees.
- **Holding illiquids where outflows are likely** (frozen DB plan with lump-sum options, early-retirement incentives, falling enrollments, suspended inflows).
- **Applying the same policy to every jurisdiction/plan** (differing funding, regulatory, accounting rules).
- **Optimizing pre-tax then trimming for tax** or adjusting correlations for tax.
- **Rebalancing a taxable portfolio to target mechanically**: needless realized gains when risk is still within a tax-adjusted band.
- **Equal rebalancing bands for taxable and tax-exempt accounts** or placing bonds in taxable and equities in sheltered accounts by default.
- **Reading time diversification as lower risk**: probability of loss falls but magnitude of potential shortfall grows.
- **Tactical shifts outside IPS limits, or driven by the latest return**: recency and control bias, with trading and tax costs.

## Exam Focus & Traps
- Size: smaller owners are blocked by minimums and eligibility; large ones by capacity (manager AUM share). "Larger is not strictly better": plus economies of scale in governance and fees, minus capacity.
- Lower spending, rising enrollment, long horizon: more illiquid assets allowed (raise infrastructure/real estate, cut IG bonds). Opposite for falling inflows, annuity buyout plans, near distribution dates.
- Time horizon shifts allocation: human capital bond-like run-off raises bonds; priority of a goal changes risk of its sub-portfolio.
- Taxes: correlations unchanged; standard deviation and return adjusted; hence the two optimizations (pre-tax and after-tax) can share the correlation input. Favorable-tax assets belong in taxable accounts (not tax-deferred). After-tax volatility is lower, so taxable portfolios rebalance less often.
- Regulatory/funding: US accounting rewards equity (higher expected return assumption); lower contribution volatility prompts de-risking; extending bond duration (Proposal C) reduces surplus risk but not expected contributions, raising equity (Proposal B) lowers expected contributions.
- Overfunded, cyclical sponsor with weak economy: de-risk (e.g. 65/35 to 40/60).
- TAA is asset-only, may not breach IPS limits (Statement 3 false), measured by Sharpe ratio vs SAA (true); systematic TAA captures documented anomalies (value, carry, momentum), discretionary uses qualitative judgment. A 50/200-day crossover rule is systematic TAA.
- Bias identification: avoiding emerging markets after the family trust lost money = availability; continuing to chase equity after strong returns = representativeness (recency); "avoid losing money" = loss aversion; separate buckets = mental accounting; keeping founder stock = illusion of control plus mental accounting/endowment effect.
- Dollar-values in the VaR table: 5% VaR uses 1.65; P50 VaR −13.6%, CVaR −18.5%. Same risk, different frame.
- Rebalancing band formula divides by (1 − t), it does not multiply; 8.0% becomes 10.67%.
- Change of constraint vs goal vs belief: early retirement offer = change in constraints (horizon); new trustee views = beliefs; marriage/children/disability = goals.

## Key Takeaways
1. Screen the opportunity set for size, governance and eligibility before running an optimizer; use commingled vehicles or exclude asset classes you cannot access or monitor.
2. Match illiquid exposure to the owner's real, stressed liquidity needs, not just the mission's nominal horizon.
3. Re-run the allocation as horizons, human capital and liabilities evolve; use glide paths tied to age or funded status for pre-committed de-risking.
4. For taxable owners, optimize on after-tax return and risk with unchanged correlations, and decide location (bonds and income assets sheltered) in the same exercise.
5. Widen corridors for taxable accounts by `1/(1 − t)`; weigh the tax cost of every rebalance against drift risk.
6. Tailor policy to regulation, funding and accounting (insurers, pensions, endowments, SWFs) and treat ESG/religious screens as set-asides or constraints.
7. Run TAA only inside IPS ranges and judge it with Sharpe ratio, information ratio or t-stat against the SAA, remembering costs and risk concentration.
8. Defend against bias with process: global market portfolio as the anchor, pre-set ranges, multi-frame risk reporting, goals-based buckets, and strong governance.

## Connects To
- **ch07**: the MVO, liability-relative and goals-based frameworks that this chapter constrains; rebalancing corridor factors.
- **ch06**: overview of asset allocation, IPS and strategic vs tactical context.
- **ch01 / ch02**: full treatment of the behavioral biases and bias-aware investment processes.
- **ch03 / ch04**: capital market expectations that change with beliefs and regimes (the 1984-2014 vs 2015-2016 return outlook).
- **`cfa-portfolio-management` ch05-ch06**: portfolio risk and return foundations behind after-tax optimization and VaR.
- **`cfa-wealth-institutional-management` ch01-ch04**: private wealth (taxes, concentrated stock) and institutional investor constraints.
- **`cfasi-portfolio-construction` ch01, ch15**: practitioner views on asset allocation implementation and alternatives.
- **`cfa-alternative-investments` ch06**: asset allocation to alternatives under liquidity and size constraints.
