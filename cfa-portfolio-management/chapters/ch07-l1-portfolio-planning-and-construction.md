# Chapter 7: Basics of Portfolio Planning and Construction
> **Source**: CFA Program Curriculum 2020, Level I, Reading 54 · Alternative Investments & Portfolio Management | Alistair Byrne, PhD, CFA, and Frank E. Smudde, MSc, CFA

## Core Idea
Portfolio construction starts with a written Investment Policy Statement (IPS) that converts a client's situation into risk and return objectives plus five constraints (liquidity, time horizon, taxes, legal/regulatory, unique circumstances). The IPS is then combined with capital market expectations (by optimization or simulation) to produce the strategic asset allocation (SAA, the policy portfolio), which is implemented, risk-budgeted, drift-monitored and rebalanced. Most of the long-run outcome comes from the SAA, so the IPS quality drives everything downstream.

## Learning Outcomes Covered
- describe the reasons for a written IPS
- describe the major components of an IPS
- describe risk and return objectives and how they are developed for a client
- distinguish willingness from ability (capacity) to take risk
- describe the liquidity, time horizon, tax, legal/regulatory and unique-circumstance constraints and their implications for asset choice
- explain the specification of asset classes in relation to asset allocation
- describe principles of portfolio construction and the role of asset allocation relative to the IPS
- describe how ESG considerations integrate into planning and construction

## Frameworks Introduced
- **IPS in "objectives and constraints" format** (the RRTTLLU checklist: Return, Risk, Time horizon, Taxes, Liquidity, Legal/regulatory, Unique circumstances)
  - When to use: any new client or mandate (individual, pension, endowment, insurer); also any periodic review.
  - How: (1) fact-find (interview, questionnaire, ALM study for institutions); (2) state risk objective (absolute and/or relative, ability and willingness); (3) state return objective (absolute/relative, nominal/real, pre/post fee, pre/post tax, required return); (4) write the five constraints; (5) check that return and risk objectives are mutually consistent and feasible in current markets; (6) attach SAA and rebalancing policy as appendices; (7) review on schedule and on any material change.
  - Failure mode: a return target inconsistent with the risk target (high return without high risk), a nominal/real mismatch, or an unrealistic target not counselled down.
- **Risk tolerance = f(ability, willingness)** (Exhibit 1 matrix)
  - When to use: translating a client profile into the risk objective.
  - How: ability is objective (time horizon, income stability, wealth relative to liabilities/spending); willingness is subjective (psychometric questionnaire, discussion). If both agree, use that level. If they conflict, **use the lower of the two** and document; counsel the client on the conflict but do not try to change personality-based willingness.
  - Failure mode: letting a high-willingness client (Jacques case) take risk his finances cannot absorb.

| | Ability: below average | Ability: above average |
|---|---|---|
| **Willingness: below average** | Below-average tolerance | Resolution needed (adopt the lower, counsel) |
| **Willingness: above average** | Resolution needed (adopt the lower, counsel) | Above-average tolerance |

- **Strategic asset allocation process**: IPS (objectives + constraints) + long-term capital market expectations → optimization and/or simulation → SAA.
  - When to use: after the IPS exists. Kept separate from the IPS because objectives/constraints and market expectations differ in nature, sources and review cycles.
  - How: mean-variance optimization with a utility function `Uₚ = E(Rₚ) − λσₚ²`; tangency of the highest attainable indifference curve with the efficient frontier gives the optimal mix. Multi-period IPS constraints are better handled by simulation.
  - Failure mode: sensitivity to small errors in return/correlation forecasts; single-period model; threshold-style IPS targets rather than a true utility function.
- **Risk budgeting**: set the overall risk budget (decided at IPS time) and split it across SAA, tactical asset allocation (TAA) and security selection, each with its own limits and desired payoff.
- **Rebalancing policy**: calendar and/or corridor (bandwidth) rule that restores policy weights after drift.
- **ESG implementation approaches**: negative/exclusionary screening, best-in-class, shareholder engagement (active ownership), thematic investing, impact investing, ESG integration.
- **Risk parity**: weight asset classes by risk contribution instead of capital.

## Key Concepts
- **Investment policy statement (IPS)**: written document capturing client objectives, constraints, governance and procedures; the starting point of portfolio management and the benchmark for suitability checks.
- **Risk objective**: portfolio risk specification reflecting client risk tolerance; absolute (max loss, VaR, standard deviation), relative (tracking risk vs benchmark) or both.
- **Return objective**: stated absolute (X% nominal or real) or relative (benchmark + 1%, peer top quartile), net or gross of fees and tax; may be a required return to fund a goal.
- **Ability to bear risk**: objective capacity (horizon, income, surplus of assets over liabilities).
- **Willingness to take risk (risk attitude)**: subjective psychology, gauged by interview or psychometric questionnaire (e.g., Grable and Joo 5-item instrument, score 5-20, higher = more tolerant).
- **Tracking risk (tracking error)**: standard deviation of portfolio-minus-benchmark returns; a ±2 sd band covers about 95% under normality.
- **Value at risk (VaR)**: money measure of the minimum loss expected over a period at a given probability; the usual way to make an absolute loss limit operational.
- **Liquidity requirement**: expected cash withdrawals (tuition, claims, benefit payments, spending rule); covered by liquid, low-risk assets maturing when needed.
- **Time horizon**: period until the portfolio must start paying out or the client's circumstances change; may be multi-stage.
- **Human capital**: client's future labor income; its correlation with the portfolio is a unique-circumstance issue (oil trader should avoid oil stocks).
- **Asset class**: category of assets with similar characteristics and risk/return relationships; high intra-class correlation, lower inter-class correlation, mutually exclusive, collectively covering the investable universe.
- **Capital market expectations**: forecasts of asset class expected returns (risk-free rate plus risk premium(s)), standard deviations and correlations.
- **Strategic asset allocation (SAA) / policy portfolio**: baseline asset-class weights (and hedge ratios for currency, rate or inflation risk) expected to meet long-term objectives within constraints.
- **Tactical asset allocation (TAA)**: deliberate deviation from policy weights to exploit near-term forecasts.
- **Drift, bandwidth (corridor), rebalancing policy**: passive divergence of weights from policy, tolerated range, and the rule restoring weights.
- **Overlay portfolio**: derivative positions used to implement hedging or exposure policy separately from the underlying assets.

## Formulas & Reference Tables
- Expected utility: `Uₚ = E(Rₚ) − λσₚ²` (λ = risk aversion; higher λ = steeper indifference curves). Indifference curve: locus of (σ, E(R)) with equal U.
- Portfolio expected return: `E(Rₚ) = Σᵢ wᵢ E(Rᵢ)`
- Portfolio risk: `σₚ = √(Σᵢ Σⱼ wᵢ wⱼ Cov(Rᵢ,Rⱼ))`
- Covariance: `Cov(Rᵢ,Rⱼ) = ρᵢⱼ σᵢ σⱼ`
- Required nominal wealth: `FV_nominal = FV_real × (1 + inflation)ⁿ`
- Required return: `r = (FV_required / PV)^(1/n) − 1`
- TAA contribution: `Σᵢ (wᵢ,start − wᵢ,policy) × Rᵢ,period` (equivalently: actual return minus return at policy weights)
- Corridor limits: policy weight ± corridor.
- Drifted weight: `wᵢ,end = wᵢ,start(1+Rᵢ) / (1+Rₚ)`

**IPS sections** (no single standard): Introduction; Statement of Purpose; Duties and Responsibilities (client, custodian, managers); Procedures (keep IPS current, contingencies); Investment Objectives; Investment Constraints; Investment Guidelines (how to execute: leverage and derivatives use, excluded assets); Evaluation and Review; Appendices (A: SAA, B: Rebalancing policy). Objectives and constraints are most tied to distinctive client needs; Duties and Responsibilities is integral, not an appendix.

**Constraints table (RRTTLLU)**

| Item | What the IPS states | Implication for assets |
|---|---|---|
| Return | Required return, abs/rel, real/nominal, gross/net of fees and tax | Must be consistent with risk and the market environment (15% nominal plausible at 10% inflation, not at 3%) |
| Risk | Absolute and/or relative limits; ability vs willingness | Lower of ability and willingness governs |
| Time horizon | Accumulation period or time to change of circumstances | Short horizon: avoid illiquid/risky assets; long: can hold equities, private equity |
| Taxes | Status; income vs gains rates; deferral | Taxable: emphasize gains (deferral has time value), munis if US; tax-exempt (pension): indifferent |
| Liquidity | Planned and possible withdrawals | Earmark liquid, low-risk assets maturing with the need (P&C insurers: large short fixed income) |
| Legal/regulatory | Limits on asset classes, foreign exposure, self-investment; insider restrictions | Hard limits, e.g., Switzerland 50% listed equity / 30% real estate / unhedged FX 30%; Japan real estate not permitted; South Africa 75% equity / 25% real estate |
| Unique circumstances | Beliefs, values, ESG, concentrated holdings, human capital | Exclusions, benchmarks adjusted, de-emphasize correlated exposures |

**Absolute vs relative objectives**

| Type | Risk example | Return example |
|---|---|---|
| Absolute | Lose no more than 4% in 12 months with 95% probability (VaR); standard deviation cap | 6.2% nominal net of fees; real return target |
| Relative | Tracking risk of 2% vs TOPIX; return within ±X% of policy benchmark | Benchmark + 1%; top-half peer rank (weak: not investable, not all can be above average) |
| Liability-relative | Minimize probability of failing to meet pension payments | Beat the liability discount rate |

**Questionnaire** (Grable-Joo 5 items): coded 1-4 and summed, 5 to 20; sample mean 12.86, sd 3.01.

**ESG approaches**

| Approach | What it does |
|---|---|
| Negative (exclusionary) screening | Excludes sectors/companies on values (tobacco, gambling) or on norms (corruption, harmful processes); oldest approach |
| Best-in-class | Keeps only issuers above an ESG score threshold within each industry; no agreed rules, so customized |
| Shareholder engagement / active ownership | Dialogue, voting, proposals; IPS should set voting guidelines; delegated to manager or proxy agent |
| Thematic investing | Invests in themes (alternative energy); biases the portfolio, so show impact on total risk-return |
| Impact investing | Selected primarily for measurable social/environmental benefit |
| ESG integration | Adds ESG factors to ordinary security and industry analysis (e.g., option-dilution, labor liabilities) |

ESG issue examples: Environmental (climate, pollution, biodiversity, water scarcity); Social (data privacy, labor standards, human rights, diversity); Governance (board composition, audit committee, executive pay, bribery, lobbying). Standards: UN PRI, UN Global Compact, OECD Guidelines for Multinational Enterprises.

## Mental Models
- **Use the lower of ability and willingness** when they conflict, because overstating risk capacity leads to forced selling, while overstating caution only costs expected return; document the reasoning.
- **Think of the IPS as a communication contract, not a performance guarantee**: it guarantees understanding, not that objectives are achieved.
- **Think of return and risk objectives as one dial**: any target return implies a minimum risk; if no frontier portfolio meets both, negotiate (Gottschalk: 5% target at 10% risk gave 4.9% max, accepted).
- **Use diversification away from human capital**: if income depends on an industry or employer, underweight it in the portfolio (stockbroker: fewer equities; employee: no concentrated employer stock).
- **Prefer rule-based rebalancing** (corridor) over discretionary drift: drift is itself a risk exposure change; discretionary non-rebalancing is a TAA bet and must be measured as one.
- **Security selection is zero-sum before costs, negative-sum after costs**: the average active manager lags the market net of costs; only worth it where markets are inefficient or no passive exposure exists (non-listed real estate, infrastructure).
- **Treat asset class definition as a design choice**: split classes only if risk, return or implementability differ (correlations within class high, across class lower); regulation or manager structure may force splits even when correlations are high.

## Worked Example
**Return objective (Gascon case)**: €900,000 invested (€100,000 held as cash emergency fund), retirement in 20 years, target €2,000,000 in today's money, inflation 2%.
1. Nominal target: `2,000,000 × 1.02²⁰ = €2,971,895`.
2. Required return: `(2,971,895 / 900,000)^(1/20) − 1 ≈ 6.15%` → quoted as 6.2%; check: `900,000 × 1.062²⁰ = €2,997,318` (just above the target).
3. Interpretation: 6.2% nominal net of fees is a plausible but meaningful equity-heavy target; he has high ability (income €250k, assets, 20 years) and high willingness, so above-average risk tolerance is consistent. The pension wrapper is tax-exempt, so income and gains are equivalent; unique constraint: avoid oil stocks (human capital).

**TAA attribution (European charity, second half-year)**: policy weights 30/15/20/20/15, starting weights 32.0/15.5/18.9/19.1/14.6 (equities breach corridor at 32% upper limit and the committee only trimmed to the limit), period returns −9/−6/+4/+4/+2%.
- Actual return `= 0.32(−9) + 0.155(−6) + 0.189(4) + 0.191(4) + 0.146(2) ≈ −2.0%`.
- Return at policy weights `= 0.30(−9) + 0.15(−6) + 0.20(4) + 0.20(4) + 0.15(2) = −1.70%`.
- TAA contribution `= −2.0% − (−1.70%) = −0.30%` (by asset: −0.18, −0.03, −0.05, −0.04, −0.01).
- Interpretation: the committee's decision to under-rebalance cost 30 bp; the first-half policy-weight return was 6.55% (drift came from equities +15%).

## Anti-patterns
- **Setting a return target without testing it against risk and the economy**: a 15% nominal goal in a 3% inflation world is a guarantee of disappointment or excess risk.
- **Using peer-group ranking as the return objective**: peer returns are not investable, methods are opaque, and not everyone can be above median.
- **Stating an absolute loss limit without a probability** ("never lose more than 4%"): it is only operational as a VaR-type statement (95% probability).
- **Following the client's willingness while ignoring ability**: high risk appetite with volatile income, tight liabilities and short horizon (Jacques) calls for a cautious portfolio.
- **Trying to "fix" a client's risk attitude**: the adviser's role is to counsel on misperceptions, not alter personality.
- **Holding concentrated employer or industry exposure** alongside labor income in the same industry.
- **Using off-the-shelf benchmarks with exclusions**: screening changes expected return and risk; use a customized or ex-screened benchmark.
- **Ignoring ESG data quality**: disclosure standards, coverage and definitions differ across jurisdictions and vendors.
- **Never rebalancing, or rebalancing on feel**: weights drift to the best-performing asset (the charity) and become an unmeasured tactical bet.
- **Treating ESG as free or as costly by default**: academic evidence on return impact is mixed.

## Exam Focus & Traps
- "Least important reason for an IPS": a written IPS does **not** ensure objectives are achieved.
- Ability vs willingness: ability = objective (horizon, income, wealth/liabilities); willingness = subjective, hardest to quantify, measured by questionnaire. Conflict: conclusion follows the **lower**. The questionnaire measures willingness, not ability or VaR.
- Absolute vs relative: "within X of the DAX/TOPIX" or "beat FTSE 100 by 120 bp" = relative; "lose no more than €2.5m", VaR cap = absolute. Tracking risk of 2% implies ±4% about 95% of the time (it is a one-sd measure).
- Investment Guidelines section = how policy is executed (leverage, derivatives, exclusions). SAA and rebalancing policy go in appendices; Duties and Responsibilities does not.
- Nominal vs real: inflate the real target at (1+π)ⁿ first, then solve for the required return. Required return is quoted net of fees.
- Taxes: income generally taxed higher than gains and earlier; deferral has time-value benefit; tax-exempt investors are indifferent between income and gains.
- P&C insurers have greater liquidity needs than life insurers (unpredictable claims) and accept lower expected return.
- Asset class definition: within-class correlations **higher** than across classes; lower correlation = more distinct (Brazil vs US at 0.76 most distinct when others are 0.88-0.90).
- Asset class returns reflect exposure to **systematic** factors, not idiosyncratic risk or arbitrage.
- TAA = deliberate deviation from the policy portfolio; **drift** is passive. TAA contribution uses weight differences times returns.
- Negative screening vs best-in-class vs engagement: engagement does not exclude; screening and best-in-class shrink the universe; thematic and impact focus on positive objectives.
- Insider restrictions (director blackout windows) belong in the IPS (legal/regulatory).

## Key Takeaways
1. Write the IPS first: objectives (return, risk) and five constraints (time, tax, liquidity, legal, unique), then attach SAA and rebalancing policy.
2. Quantify risk in both absolute (VaR, loss cap with probability) and relative (tracking risk) terms when mandates are partial.
3. Set overall risk tolerance at the lower of ability and willingness; document conflicts and counsel rather than override.
4. Convert goals to returns with real-to-nominal inflation and a required-return calculation, and always check feasibility against risk and the market.
5. Define asset classes so they are homogeneous inside, differentiated outside, collectively exhaustive and implementable; ESG exclusions may require custom benchmarks.
6. Combine IPS and capital market expectations by optimization (utility `E(R) − λσ²`) or, for multi-period problems, simulation; revisit when expectations or the client change.
7. Budget risk across SAA, TAA and security selection; choose active only where skill and market inefficiency justify the cost.
8. Fix a rebalancing rule (corridor, calendar) and measure the cost or gain of any deviation as TAA.
9. Pick the ESG implementation approach explicitly in the IPS (screen, best-in-class, engagement, thematic, impact, integration) and tell managers how to vote and what benchmark applies.

## Connects To
- **ch04**: portfolio management process overview (planning, execution, feedback) of which this chapter is the planning step.
- **ch05** and **ch06**: portfolio risk and return math (covariance, efficient frontier, CML) behind the optimization used for SAA.
- **ch03**: market efficiency determines where security selection can add value.
- **ch10**: robo-advisers and ETFs as alternative organizing principles for retail portfolios.
- **`cfa-wealth-institutional-management` ch01**: IPS for individuals at Level III depth (return/risk/constraints, human and financial capital).
- **`cfa-wealth-institutional-management` ch04**: institutional IPS (pensions, endowments, insurers, banks).
- **`cfa-asset-allocation-cme` ch06–ch08**: strategic asset allocation, liability-relative approaches and real-world constraints.
- **`cfa-ethics-gips`**: Standard III(C) Suitability and fact-finding duties underpinning the IPS.
