# Chapter 1: Overview of Private Wealth Management
> **Source**: CFA Program Curriculum 2023, Level III, Reading 21 · Portfolio Management | Christopher J. Sidoni, CFP, CFA, and Vineet Vohra, CFA

## Core Idea
Private wealth management is a goal-driven process: understand the client (information, goals, risk tolerance), test whether capital is sufficient for the goals (deterministic or Monte Carlo), codify the answer in an Investment Policy Statement (IPS), build the portfolio (traditional or goals-based), then report, review, and judge success by goal achievement and process, not by returns alone. Unlike institutional mandates, the objectives are fuzzy, competing, and change over time, so the adviser's job is as much clarifying and educating as optimizing.

## Learning Outcomes Covered
- contrast private vs institutional client concerns; discuss information needed for advising private clients
- identify tax considerations; identify and formulate goals; evaluate risk tolerance
- describe technical and soft skills of advisers
- evaluate capital sufficiency; discuss retirement planning principles
- discuss IPS parts; prepare the objectives section; evaluate and improve an IPS
- recommend and justify allocations and investments; describe reporting and review practice
- evaluate success of an investment program; discuss ethics and compliance; relate service level to client segment

## Frameworks Introduced
- **Private vs institutional comparison**: objectives, constraints (time horizon, scale, taxes), governance, sophistication, regulation, uniqueness.
  - When to use: deciding why a private client should not copy an endowment allocation (illiquid hedge funds, private equity).
  - How: private = diverse, vague, competing, changing objectives; shorter and multiple horizons; smaller scale; tax-sensitive; informal governance; behavioral risk. Institutional = specific, liability-linked, stable objectives; often (theoretically) infinite horizon; formal board/committee.
- **Client information set**: (1) personal (family, ID/KYC, employment, source of wealth, investment background, return objective, ESG/liquidity preferences); (2) financial (personal balance sheet = net worth statement, cash flows, expenses); (3) tax (from tax returns); (4) other (wills, trusts, insurance, governance: who may approve policy, trade, transfer money; service/reporting needs).
  - Why it works: sources of wealth reveal experience with volatility (steady saver vs recent business sale).
- **Goal framework**: planned goals (quantifiable: retirement, specific purchases, education, family events, wealth transfer, philanthropy) vs unplanned goals (property repairs, medical/elder care, other shocks). Adviser tasks: goal quantification, goal prioritization, goal changes.
  - Failure mode: priority is set by importance to the client, not by which need falls first.
- **Risk tolerance decomposition**: risk tolerance (willingness + ability to bear risk) = attitude; risk capacity = objective ability (wealth, income, horizon, liquidity needs); risk perception = subjective assessment of an investment's riskiness (can be shaped by the adviser). Overall tolerance is the lower of willingness and capacity in practice.
  - How: questionnaire (numeric score) plus conversation; then assess tolerance goal by goal.
  - Failure mode: questionnaires are subjective, framing-sensitive (percent vs currency loss, small vs large portfolio), and of unclear predictive power.
- **Capital sufficiency analysis (capital needs analysis)**: determine whether the client has or will accumulate enough to meet goals.
  - Deterministic forecast: single straight-line return (e.g., 6% for 15 years); simple but ignores variability.
  - Monte Carlo simulation: random trials from assumed distributions (mean, standard deviation, correlations; optionally inflation, taxes, fees, horizon/life expectancy). Output = percentile wealth paths and probability of success. Typical guidance 75%-90% probability of success (no industry standard).
  - Fixes when probability is too low: raise contributions, cut goal amount, delay goal, take more risk only if within tolerance and capacity.
- **Retirement analysis methods**: mortality tables (probability-weight cash outflows), annuity pricing (PV of fixed or inflation-linked payments; hedges longevity risk), Monte Carlo (reflects actual portfolio, scenario flexibility).
- **Investment Policy Statement (IPS) for a private client**: (1) background and objectives; (2) investment parameters (risk tolerance, time horizon, asset class preferences, other preferences such as ESG/legacy holdings, liquidity, constraints); (3) portfolio asset allocation (target plus upper/lower bounds, or ranges if tactical); (4) portfolio management (discretionary authority, rebalancing, tactical changes, implementation); (5) duties and responsibilities (adviser, custodian, IPS review); (6) appendix (modeled portfolio behavior, capital market expectations).
  - Purpose: links the client's circumstances to strategic allocation, enforces discipline in drawdowns, focuses on long-term goals, documents fiduciary process.
- **Portfolio construction, traditional approach**: identify asset classes -> capital market expectations -> allocation (mean-variance optimization with min/max constraints) -> assess constraints (embedded gains, residential real estate) -> implement (active/passive, factors, vehicles, currency hedging) -> asset location.
- **Goals-based investing**: assign funds to each goal, optimize each goal portfolio to a maximum volatility or target probability of success; the total is the sum of goal portfolios.
  - Pro: clients express risk tolerance per goal. Con: the aggregate may not lie on the total-portfolio efficient frontier.
- **Success evaluation triad**: goal achievement (still likely to meet goals without drastic plan changes), process consistency, portfolio performance (absolute and relative, risk-adjusted).

## Key Concepts
- **Private wealth management**: investment management and financial planning for individuals and families.
- **Personal balance sheet (net worth statement)**: assets (cash, brokerage, retirement, private business, cash-value insurance, real property, personal assets) minus liabilities (consumer, auto, student, property loans, margin debt).
- **Tax avoidance / reduction / deferral**: avoidance = legal exclusion (tax-free accounts, gifts within allowances; not evasion); reduction = lower the tax effect (tax-exempt bonds, tax-efficient asset classes); deferral = postpone recognition (low turnover, tax-deferred accounts), valuable when future rates are expected to be lower.
- **Human capital**: NPV of future labor income; converted to financial capital over the career.
- **Planned vs unplanned goals**: quantifiable and time-bound vs unforeseen needs.
- **Risk capacity**: objective ability to take financial risk without damaging goals.
- **Risk perception**: subjective view of how risky an outcome is; malleable.
- **Longevity risk**: risk of outliving resources; a life annuity mitigates it.
- **Probability of success**: share of Monte Carlo trials meeting the objective.
- **Shortfall magnitude**: how badly a failed trial misses; usually not reported but decisive for remedies.
- **Annuity puzzle**: retirees avoid annuities despite benefits (hope of lifestyle upside, loss of control, high cost).
- **Consumption gap**: retirees spend less than economic models predict (loss aversion, uncertainty).
- **Asset location**: placing asset classes in the accounts where their tax treatment is best (income-heavy assets in tax-deferred accounts).
- **Discretionary vs non-discretionary authority**: act without vs only with client consent.
- **Time-based vs threshold-based rebalancing**: calendar-driven vs triggered by drift beyond a set percentage (more common).
- **Mass affluent / HNW / UHNW**: service segments with rising customization, shrinking client-to-manager ratios, longer horizons.
- **Family office**: specialists hired exclusively to serve one wealthy family.
- **KYC (Know Your Customer)**: obtain essential facts on each client, including risk/return objectives and origin of wealth (anti-money-laundering link).
- **Robo-advisor**: primarily digital adviser; online questionnaire, MVO-based allocation, ETF/fund implementation, automatic rebalancing, low cost.

## Formulas & Reference Tables
- Net worth: `Net worth = Total assets − Total liabilities` (Exhibit 1 couple: €7,115,000 − €640,000 = €6,475,000).
- Deterministic growth: `FV = PV·(1+r)ⁿ` with a flat r; Monte Carlo replaces r with draws from a distribution (mean μ, σ, correlations).
- Geometric (modeled compound) return from arithmetic return: `r_g ≈ μ − σ²/2`. Checks against the sample IPS: US stocks 8.5 − 22²/200 = 6.08 (shown 6.1); non-US 10 − 26²/200 = 6.62 (6.6); bonds 3.5 − 8²/200 = 3.18 (3.2). Clients confuse expected (arithmetic) with compound return, so show both.
- Mortality-weighted PV of retirement spending: `PV = Σ_t S_t·CF_t/(1+r)ᵗ`, S_t = survival probability at plan year t.
- Goals-based aggregate weight: `w_total = Σ_g (Capital_g/Capital_total)·w_g`.
- Time-weighted return (reports): chain-link sub-period returns; do not use `gain / beginning value` (Exhibit 11: 7,233,864 / 136,928,682 = 5.28% vs reported TWR 5.31%).

| Segment | Typical wealth | Service model |
|---|---|---|
| Robo-advisor (mass affluent, small) | small portfolios | digital, low fee, MVO + ETFs |
| Mass affluent | ~$250k-$1m (practice guidance) | little customization, many clients per manager, technology-heavy, commission or fee model |
| High net worth ("private client" $1m-$10m) | up to ~$50m | customized investments, tax and estate planning, illiquid assets, specialists |
| Ultra high net worth | above ~$50m | multi-generational horizon, complex tax/estate, concierge/bill pay, family governance, family office |

Global adults by wealth (Credit Suisse 2017, millions): $0.1-1m 391.0; $1-5m 31.4; $5-10m 3.0; $10-50m 1.5; over $50m 0.1.

Regulation: MiFID II (EU 2018: demonstrate suitability, minimum competence, no commissions for independent advisers/discretionary managers); Common Reporting Standard (OECD/G20 2014: automatic exchange of account information); FATCA (US 2010: non-US institutions report US taxpayers' accounts). US DOL Fiduciary Rule and SEC Best Interest Rule were proposed, not enacted, at publication.

## Mental Models
- Treat the client as a liability-free asset owner with unstated liabilities: your first job is to manufacture the liability (quantified, prioritized goals), then the portfolio follows.
- Use the lower of risk tolerance and risk capacity; a high-capacity but anxious client still gets the lower-risk portfolio, otherwise they abandon the plan at the bottom.
- Do not let capital sufficiency drive portfolio construction: raising risk to hit a probability target may breach tolerance.
- Monte Carlo output is a conversation tool, not a forecast: probability is hypersensitive to the return assumption, so use forward-looking capital market expectations, not history.
- Goal-specific risk tolerance: low for near-term goals (education in 5-10 years, property), higher for long-dated or flexible goals (retirement, discretionary spending the client is willing to cut).
- Reporting vs review: reporting is one-way, review is an engaged dialogue; the horizon mismatch (decades of goals vs quarterly statements) is the adviser's behavioral risk.

## Worked Example
**Mortality-weighted retirement liability.** Client age 72 needs €100,000 real per year for 20 years, real discount rate 3%. Using the sample mortality table survival probabilities (97%, 93%, 90% ... 14%):
- Certain-life PV = Σ 100,000/1.03ᵗ for t=1..20 = **€1,487,747**.
- Survival-weighted PV = Σ S_t·100,000/1.03ᵗ = **€895,743**.
- Interpretation: the weighted figure is 40% lower because it expects early death on average; it understates the need if the client has above-average longevity (education, healthcare), which is exactly longevity risk. A life annuity or a high Monte Carlo success target addresses the tail.

**Goals-based aggregation.** €3.1m portfolio, €500k ski cottage in 7 years (16.13% of capital) and €2.6m retirement. Cottage portfolio 70% IGB/8% HYB/12% EE/5% GEE/3% RE/2% COM (expected return 4.41%, σ 4.56%); retirement portfolio 27/7/35/19/9/3 (7.12%, σ 11.15%). Aggregate IGB = 0.1613·70 + 0.8387·27 = 33.9% (source rounds to 34%); equity-European 31.3%. Aggregate return 6.68% with σ 10.0% versus 6.77% for the pure mean-variance optimum at the same σ: the goals-based mix gives up about 0.1% for goal-level intelligibility (recomputed from the exhibit correlation matrix).

**Monte Carlo reading (Exhibit 3).** At year 20 the 75th percentile is −$249,205 and success is 69%: in 31% of trials the client runs out of money. Below the 75%-90% guidance, so adjust contributions, goal size, timing or return.

## Anti-patterns
- **Using "growth" or "growth and income" as the objective**: too vague; objectives must be quantified (inflation-indexed withdrawals, bequest amounts) and ranked.
- **Taking the client's stated horizon at face value**: a retiree's horizon is the lifetime of the household (and often beyond), not "10 years until retirement"; state "exceeds 10 years".
- **Copying an endowment's illiquid-heavy mix** onto a small private portfolio with shorter horizon and tax drag.
- **Prioritizing goals by timing**: an imminent antique purchase can crowd out retirement.
- **Relying on a questionnaire score alone**, or on historical returns as Monte Carlo inputs.
- **Reporting only a holdings list**: no allocation, performance, flows, benchmark, currency or market commentary.
- **Ignoring the fee conflict**: advising on mortgage vs cash purchase while paid on AUM without disclosure.
- **Discussing one family member's affairs with another** (confidentiality breach) even when you advise both.

## Exam Focus & Traps
- Tax strategy classification: tax-free account = avoidance; tax-deferred account = deferral; swapping to a more tax-efficient asset = reduction; delaying a sale until post-retirement = deferral (and maybe reduction). Moving high-dividend stocks into a tax-free account = avoidance.
- Risk tolerance vs risk capacity vs risk perception: capacity is objective, tolerance is attitude, perception is situational and can be shaped.
- Monte Carlo "probability of success": read the percentile row against the target amount (50th percentile $553,803 > $500,000 pledge means a bit above 50% success). Remember Monte Carlo does not give shortfall magnitude.
- Annuity puzzle vs consumption gap vs loss aversion: refusing to give up control of assets = annuity puzzle; spending less than affordable = consumption gap; wanting to raise spending if projections allow is not loss aversion.
- Goals-based optimization targets a stated maximum volatility or probability of success per goal; the questionnaire alone is not the basis.
- IPS: pure strategic managers omit "tactical changes"; liquidity needs already in objectives need not be repeated; a specific dated cash need (charitable pledge in 15 years) belongs in the objectives section, not in the parameters.
- Soft vs technical: educating the client = soft; building a portfolio for unique circumstances = technical; speaking the client's language = language fluency (technical).
- Standards: suitability = III(C), confidentiality = III(E), KYC links to III(C), conflicts = I(B) and VI, loyalty/prudence/care = III(A), diligence = V(A).
- Success: if the client and adviser agreed that beating a benchmark mattered, a goal-successful program trailing it by 0.40% can still be judged unsuccessful. Agree the definition of success at the outset.
- Mass affluent with a high client-to-manager ratio and technology service: segment inference questions.

## Key Takeaways
1. Build the plan from information (personal, financial, tax, governance), then goals, then risk; never start from products.
2. Quantify and rank goals; re-open them at every review because they change.
3. Assess risk tolerance per goal using questionnaire plus conversation; take the lower of willingness and capacity.
4. Use Monte Carlo for probability and scenarios, deterministic for simplicity; aim for roughly 75%-90% success and inspect shortfall magnitude.
5. Retirement: mortality tables and annuities size the liability; Monte Carlo tests the actual portfolio; plan for longevity and loss aversion.
6. The IPS is the operating manual: objectives, parameters, allocation with bands, discretion, rebalancing (threshold-based), implementation, responsibilities, annual review.
7. Choose traditional (total-portfolio MVO) or goals-based construction knowingly; location (asset placement by tax) applies to both.
8. Judge success on goals, process, and performance, and agree the definition of success up front.

## Connects To
- **ch02**: taxes, concentrated positions, estate planning and gifting in depth (the topics this chapter only sketches).
- **ch03**: risk management for individuals (human capital, insurance) built on the personal balance sheet introduced here.
- **ch04**: institutional investors, the contrast set for private clients.
- **ch06**: case study following one family through five life stages with the same planning loop.
- **`cfa-asset-allocation-cme` ch01-02**: behavioral biases that drive client risk perception and the annuity puzzle; **ch06-08**: asset allocation approaches and real-world constraints.
- **`cfa-portfolio-management` ch18**: performance evaluation (time-weighted return, benchmarks).
- **`cfa-ethics-gips`**: Standard III duties (suitability, loyalty, confidentiality).
