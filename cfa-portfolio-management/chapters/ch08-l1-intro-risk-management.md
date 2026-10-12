# Chapter 8: Introduction to Risk Management
> **Source**: CFA Program Curriculum 2020, Level I, Reading 55 · Alternative Investments & Portfolio Management | Don M. Chance, PhD, CFA, and Michael E. Edleson, PhD, CFA

## Core Idea
Risk management is not risk minimization: it is the process of defining the level of risk to take (risk tolerance), measuring the risk actually being taken, and adjusting the second toward the first to maximize value (firm) or utility (individual). It works top-down (governance, tolerance, budget) and bottom-up (identify, measure, monitor, modify), and its guiding motto is "no surprises": losses may happen, but their size should have been quantified and accepted in advance.

## Learning Outcomes Covered
- define risk management
- describe the risk management framework (seven elements)
- define risk governance and its elements (enterprise view, committee, CRO)
- explain how risk tolerance affects risk management
- describe risk budgeting and its role in governance
- identify financial and non-financial risks and how they interact
- describe methods to measure (metrics) and modify (avoid, accept, transfer, shift) risk and how to choose

## Frameworks Introduced
- **Risk management process / framework**: "define risk tolerance, measure risk, adjust exposure to tolerance."
  - When to use: any organization or individual taking risk; scale the formality, not the logic.
  - How (7 framework elements): (1) risk governance; (2) risk identification and measurement; (3) risk infrastructure (people, systems, risk capture, data model, analytics, stress engine, reports); (4) policies and processes (limits, escalation, checklists); (5) risk monitoring, mitigation and management (the decision "are risks within tolerance/budget? if no, modify and re-measure"); (6) communications (reporting upward and down, feedback loop to the board); (7) strategic analysis and integration (use risk analytics to see which activities add value). Loop: Board sets goals and tolerance → management allocates to risky activities → exposures measured → in line? If no, modify; if yes, monitor and report.
  - Failure mode: effort concentrated after an adverse event; risk tolerance debated only after a crisis ("buying insurance after the loss").
- **Individual risk management (6 ingredients)**: goals/objectives → choose investments and identify risks → evaluate exposure → consider alternatives to modify risk → implement (insure, hedge, trade) → evaluate and review. The individual is the governing body; the adviser is management.
- **Enterprise risk management (ERM)**: governance applied across the whole organization and its whole economic balance sheet. Example: a corporate pension fund in all equities with bond-like liabilities can become insolvent in a market drop combined with falling rates; the parent's own recession risk also lowers the pension's appropriate risk tolerance.
- **Risk tolerance determination ("inside" and "outside" views)**: inside = what shortfalls would make the organization fail its critical goals; outside = what uncertain forces (risk drivers) it is exposed to. Then set limits (e.g., max annual cash-flow variation, revenue exposure in a recession, currency exposure). Factors that should drive it: goals, expertise, ability to respond dynamically, going-concern loss capacity, competitive and regulatory landscape, scenario analysis. Factors that should not (but do): board members' personal agendas (agency problem), company size, calm markets, short-term pressure, management compensation.
- **Risk budgeting**: quantifies and allocates tolerable risk by specific metrics; bridges governance to management decisions.
  - Single-dimension budgets: standard deviation, beta, VaR, scenario loss. Multi-dimension: by risk class (equity, rates, commodity), risk factor tilts (value, size) layered on a beta budget, liquidity, currency, inflation exposure.
  - Benefit: forces risk trade-offs; invest where return per unit of risk is highest; each decision is benchmarked against the market (less of the risky asset vs full position plus market hedge), pushing every decision to add value net of risk.
- **Risk modification toolkit**: prevention/avoidance, acceptance (self-insurance, diversification), transfer (insurance), shifting (derivatives).

## Key Concepts
- **Risk**: exposure to uncertainty. Three senses: **risk driver** (the underlying uncertainty), **risk position** (size of the risky action) and **risk exposure** (potential value change); simple case exposure = position × driver (¥1,000,000 × 1% = ¥10,000).
- **Risk management**: process defining the level of risk to take, measuring it, and adjusting it toward the target to maximize value/utility.
- **Doctrine of No Surprises**: the impact of unpredictable events must already be quantified and considered, not predicted.
- **Risk governance**: top-down process and guidance (board level) aligning risk management with enterprise goals; includes oversight and tolerance setting.
- **Risk tolerance (appetite)**: extent to which the organization will accept losses, opportunity costs, and failure to meet objectives; sorts risks into acceptable, risk-limited, and unacceptable.
- **Risk budgeting**: any allocation of a portfolio or business by risk characteristics, within a total risk limit.
- **Chief risk officer (CRO)**: executive responsible for building and running the risk framework; participates in strategy, not just policing; the CEO or CFO should not do this role.
- **Risk management committee**: operational forum for risk issues beneath the board.
- **Financial risks**: market (rates, equities, FX, commodities), credit (default/counterparty), liquidity (valuation shock/transaction cost uncertainty when selling).
- **Non-financial risks**: settlement (Herstatt), legal, regulatory/accounting/tax (compliance), model, tail, operational (people, systems, processes, external events, cyber, rogue trader), solvency (running out of cash).
- **Wrong-way risk**: exposure to a counterparty rises when that counterparty's creditworthiness falls.
- **Systemic risk**: failure transmitting across the financial system; the ultimate risk interaction.
- **Value at risk (VaR)**: minimum loss expected over a period with a stated probability; three elements: currency amount, time period, probability.
- **Conditional VaR (CVaR)**: probability-weighted average of losses beyond the VaR level.
- **Self-insurance**: bearing a risk too costly to eliminate externally, usually with a reserve.
- **Risk transfer** (insurance, surety/fidelity bonds, reinsurance, catastrophe bonds) vs **risk shifting** (derivatives changing the payoff distribution).

## Formulas & Reference Tables
- Risk exposure (simple): `exposure = risk position × risk driver sensitivity` (e.g., ¥1,000,000 × 1% = ¥10,000).
- Normal distribution coverage: ±1σ ≈ 68%, ±2σ ≈ 95%, ±3σ ≈ 99%.
- VaR reading: "£3m at 5% one-day" means a loss of **at least** £3m is expected in about 1 day in 20. Not a maximum, not an expected loss.
- Leverage interaction (non-linear): 2× leverage gives 2% loss for a 1% baseline loss; with liquidity stress, a 10% baseline loss could be ≈25% instead of 20%, and a 30% baseline loss can mean failure.
- Counterparty example: put worth ¥100 with 2% independent default risk ≈ ¥98; if default probability is 10% or more exactly when the put is in the money, the true value is lower (wrong-way risk).

**Metrics by risk type**

| Risk / asset | Metric | Notes |
|---|---|---|
| General dispersion | Probability, standard deviation | σ weak for fat tails/asymmetry; may not exist for very fat tails |
| Equities (diversified) | Beta | Relative/market risk contribution; unsystematic risk ignored |
| Derivatives | Delta (1st order, small moves), gamma (2nd order, change in delta), vega (volatility), rho (rates) | "The Greeks"; derivatives hedge by assuming other risks |
| Fixed income | Duration | Interest-rate sensitivity, first order |
| Tail / cross-asset | VaR, CVaR, extreme value theory | VaR a minimum loss; accepted by bank regulators |
| Event | Scenario analysis (package of stresses with a theme), stress testing (extreme price moves) | Complement VaR; still model risk |
| Credit | Ratings, probability of default, loss given default, credit VaR, probability of rating change; ratios (current, interest coverage, ROA, debt/assets); CDS prices | Defaults rare, so aggregate similar firms |
| Operational / legal / regulatory | Subjective frequency and severity, third-party loss databases | Hardest to measure |

**Risk modification matrix**

| Method | Mechanism | Best for | Limits |
|---|---|---|---|
| Prevention / avoidance | Do not take the risk | Risks with few benefits, outside core competence | Gives up the return; cannot avoid everything; cost-benefit |
| Acceptance: self-insurance | Bear it, hold reserve/capital | Small, affordable, within tolerance | "Fine line between self-insurance and denial"; never for risk above tolerance |
| Acceptance: diversification | Combine imperfectly correlated risks | Always as starting point | Rarely sufficient alone |
| Transfer (insurance) | Premium for coverage; insurer pools low-correlated risks | Pool-able, diversifiable risks | Not for correlated/systemic or hard to pool risks; deductibles, exclusions, moral hazard clauses |
| Shifting (derivatives) | Changes payoff distribution across parties | Financial risks above appetite; most common for financial firms | Forwards/futures/swaps lock in, zero upfront; options flexible, premium upfront |

Forward commitments (forwards, futures, swaps): both parties obligated, no initial payment, lock in an outcome. Contingent claims (options): buyer pays premium, keeps upside, loss capped at premium; call = right to buy/pay a rate, put = right to sell/receive a rate.

**Risk classification table**

| Financial | Non-financial |
|---|---|
| Market, credit, liquidity | Settlement, legal, regulatory, accounting, tax, model, tail, operational (employees, rogue trader, disasters, cyber, terrorism), solvency |
| Individuals' extras: health, mortality (dying young), longevity (outliving resources), property and casualty, identity theft |

## Mental Models
- **Think of risk management as a thermostat**: tolerance is the setpoint, measurement the thermometer, modification the heating/cooling; cooling is not the only action (a 50/50 equity/cash portfolio drifting to cash may need risk added).
- **Use the "red zone on the dial" idea**: governance defines in calm times the worst losses it will tolerate, before a crisis frames the debate.
- **Market begets credit, credit begets operational (settlement), legal follows**: model risks as a chain, not as independent boxes; total risk is non-linear and worse than the sum of parts (LTCM 1998, 2008).
- **Prefer an enterprise view over silos**: asset risk tolerance in isolation differs from enterprise tolerance (pension fund vs sponsor; endowment vs university revenue; individual with human capital).
- **Choose modification by cost-benefit and tolerance, not by dogma**: avoid risks with little reward and no competence, self-insure the small and affordable, insure the pool-able, shift financial risks with derivatives; methods are not mutually exclusive.
- **Use risk budgets in risk-factor terms, not asset-label terms**: 20% hedge funds / 30% private equity / 50% stocks and bonds hides that the portfolio may be 70% driven by global equity returns.
- **Treat VaR as the entrance to the tail, not its depth**: pair with CVaR, scenarios and stress tests.

## Worked Example
**Interpreting VaR and normal-model tail risk.** A bank reports one-day 5% VaR = £3m.
1. Statement: with 5% probability (about 1 day in 20) the bank expects to lose **at least** £3m. The maximum loss is not bounded by VaR (it is the whole capital).
2. Over 250 trading days, expect about 12.5 days with losses at or beyond £3m; a CVaR figure (average of those days) would be higher than £3m.
3. Tail test with S&P 500 monthly data (1950-2018): mean 0.70%, sd 4.10%. October 1987 at −21.76% is a z-score of `(−21.76 − 0.70)/4.10 ≈ −5.5`. Under normality the source states such a month occurs about once per 2.2 million years (my recomputation with the rounded inputs gives a few million years, the same order); the second and third worst months (−16.94%, −14.58%) are z ≈ −4.3 and −3.7, roughly one in a few thousand and one in under 1,000 years. Three such events in 69 years rejects the normal assumption.
4. Interpretation: VaR from a normal model understates the left tail; supplement with extreme value theory, scenario analysis and stress tests, and treat the omission of fat tails as model risk.

## Anti-patterns
- **Equating risk management with risk avoidance**: a firm or portfolio that avoids all risk cannot create value; inflation and growth are lost in all-cash portfolios.
- **Setting risk tolerance after a crisis**: it happens anyway, but too late and with hindsight bias.
- **"Self-insuring" risks above stated tolerance**: this is denial, not governance (a €1bn loss limit with unhedged rogue-trader exposure up to €3bn).
- **Treating risks separately**: ignoring leverage × liquidity × solvency interactions, or wrong-way risk.
- **Relying on one metric (VaR, standard deviation) as a comfort blanket**: false sense of security; normal assumption hides fat tails.
- **Optimizing assets in isolation from liabilities and sponsor**: pension all-equity strategy with bond-like liabilities.
- **Concentrating in employer stock**: human capital and financial capital share the same risk (Enron).
- **Leaving risk management as a policing afterthought**: processes should embed risk at every decision point (investment, asset allocation).
- **Making the CEO or CFO the risk function**: lacks specialization and attention in a large organization.
- **Technology replacing judgment**: models and data need testing; risk systems can themselves be a source of error.

## Exam Focus & Traps
- "Not a goal of risk management": minimizing risk. Maximizing returns is also wrong; the goal is alignment with tolerance for value/utility.
- Framework element that sets context = **governance**; analytical/quantitative core = **identification and measurement**; action when out of line = **monitoring, mitigation and management**.
- Sequence: risk tolerance → risk budgeting → measure exposures (determine what is acceptable before measuring/accepting).
- Risk budgeting does **not** include determining target return; it need not prohibit or require hedging; any allocation by risk characteristics counts (beta limit 0.75, risk factors).
- Risk governance does **not** prescribe specific mitigation per business line; risk management committee does **not** approve the board's policies (it is operational; board approves).
- Risk tolerance is best discussed **before** a crisis, at board level; factors that should drive it: ability to respond dynamically to adverse events (not stable markets or board beliefs).
- Financial risk = originates in financial markets (market, credit, liquidity). Operational, settlement, legal, model, solvency = non-financial. "Risk of rates rising" = financial; "regulations make a transaction illegal" = non-financial; "trader without limits" = operational.
- Liquidity risk = uncertainty in the bid-ask/valuation spread, not the known spread cost; solvency risk (cash shortage) is what many practitioners also call liquidity risk.
- VaR = **minimum** loss at a probability, not maximum or expected; "5% one-day $1m" = lose at least $1m 5% of the time (not 95%, not "no more than").
- Delta/gamma = direct derivatives risk measures; beta and standard deviation are not.
- Scenario analysis and stress testing supplement VaR for extremes; loss given default is credit, not an extreme-event method.
- Acceptance/self-insurance (reserve fund) ≠ insurance (transfer) ≠ derivatives (shifting).
- Insurance works by pooling low-correlated risks; insurable risks are "typically diversifiable by the insurer", not necessarily cheaper or lower-limit.
- Wrong-way risk (counterparty owes more while less creditworthy) is the standard "interaction of risks" example, not simple correlated stock declines.
- Mortality risk = dying young (income stops for family); longevity risk = outliving assets.

## Key Takeaways
1. Define, measure, adjust: risk management aligns actual risk with a pre-set tolerance to maximize value or utility.
2. Set risk tolerance at governance level in advance, using inside (failure thresholds) and outside (risk drivers) views.
3. Convert tolerance into a risk budget expressed in risk characteristics (σ, beta, VaR, scenario loss, factor exposures), not just asset labels.
4. Use an enterprise view: include liabilities, sponsor risk, human capital and solvency, not just the asset pool.
5. Map risks into market, credit, liquidity and the non-financial set; always check their interactions (leverage + liquidity + solvency; wrong-way risk).
6. Use multiple measures: σ/beta/duration/Greeks for sensitivities, VaR/CVaR for tail, scenario and stress tests for the unmodelled; treat model and tail risk explicitly.
7. Choose among avoidance, self-insurance/diversification, insurance and derivatives by cost-benefit relative to tolerance; remember forwards lock in, options keep flexibility for a premium.
8. Appoint a CRO and a risk committee, report continuously, and loop feedback to the board.

## Connects To
- **ch07**: IPS risk objectives and risk budgeting across SAA, TAA and security selection.
- **ch05** and **ch06**: portfolio risk, beta and diversification mathematics underlying risk metrics.
- **ch13**: Level II measuring and managing market risk (VaR methods, CVaR, stress tests in depth).
- **ch14**: backtesting and simulation, relevant to model risk and scenario engines.
- **`cfa-derivatives` ch01** and **ch02**: forwards, futures, swaps, options used for risk shifting; Greeks.
- **`cfa-wealth-institutional-management` ch03**: risk management for individuals (human capital, insurance, longevity).
- **`cfa-fixed-income` ch06**: credit analysis measures (ratings, ratios, default probability).
- **`cfa-ethics-gips`**: duties to clients that underpin risk governance in practice.
