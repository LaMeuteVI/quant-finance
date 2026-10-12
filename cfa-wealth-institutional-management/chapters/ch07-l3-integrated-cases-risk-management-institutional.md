# Chapter 7: Integrated Cases in Risk Management: Institutional
> **Source**: CFA Program Curriculum 2023, Level III, Reading 30 · Portfolio Management (Risk Management) | Steve Balaban, CFA; Arjan Berkelaar, PhD, CFA; Nasir Hasan; Hardik Sanjay Shah, CFA (sovereign wealth fund case "R-SWF")

## Core Idea
For a long-horizon asset owner (pension fund, sovereign wealth fund, endowment, foundation), risk management exists to avoid an existential threat: the interaction of market losses with illiquidity, so that obligations cannot be met and the portfolio cannot be rebalanced. The reading builds the toolkit (seven risk lenses, unsmoothing, commitment bands, a five-step liquidity plan, enterprise risk management, universal ownership and climate/social risk) and then runs it through a $50bn savings SWF that adds a direct airport investment and a direct minority stake in a beverage maker. Three scenes (approval, year 3, year 5) show how identified risks become real and what a sound response looks like.

## Learning Outcomes Covered
- discuss financial risks in the portfolio strategy of an institutional investor
- discuss environmental and social risks in that strategy
- analyze and evaluate financial and non-financial risk exposures
- discuss methods to manage risks of long-term direct investments
- evaluate strengths and weaknesses of an enterprise risk management (ERM) system and recommend improvements

## Frameworks Introduced
- **Seven lenses of financial risk**: use all, because no single metric is enough.
  - Top-down (board and CIO guardrails) vs bottom-up (team risk per sub-portfolio); portfolio-level vs asset-class-specific (hedge funds may only have monthly returns, so the aggregate is not comparable); return-based (easy, biased by past style) vs holdings-based (granular, costly, often infeasible for hedge funds and private assets); absolute (standard deviation, CVaR, maximum drawdown) vs relative (tracking error); short-term (factor-based VaR, near-term loss) vs long-term (Monte Carlo: probability of purchasing power loss, of missing payouts, of reaching a return target over 5-20 years); quantitative vs qualitative (history is backward-looking; guard against bias in both); pre- vs post-investment (due diligence on people, ethics, operations, auditors, custodian, fee terms before investing, because exit is hard).
- **Market-liquidity interaction (the central risk)**: needs rise in a crisis (payouts, accelerated capital calls, larger rebalancing flows) while sources shrink (contributions and gifts fall, private distributions stop, liquid assets become undesirable to sell). Cash and fixed income are the only reliable sources, and long-term owners hold little of them. Private assets are locked for 5-10 years, hedge funds gate, and public equities may be unattractive to sell at lows. Failure to rebalance in a crisis also forfeits the rebound.
- **Illiquid-asset risk checklist**: (1) uncertain call and distribution schedule (drawdown structure; committing too much risks the denominator effect, too little misses the target); (2) smoothed, appraisal-based returns that understate volatility and correlation and make mean-variance over-allocate; (3) no cheap rebalancing; (4) secondary sales only at a discount.
- **Return-smoothing fixes**: use a public proxy (small-cap equities for private equity) or unsmooth observed returns. Geltner removes first-order serial correlation; Okunev-White extends to higher orders; GLM (Getmansky-Lo-Makarov) models a moving average. After unsmoothing, volatility and equity beta rise. Mean-variance still fails because it assumes constant weights and ignores calls and distributions; no accepted alternative exists, so practitioners cap illiquid weights.
- **Direct vs fund investing**: direct saves GP fees (typically 2% base plus 20% of profit) and gives control, with no unfunded commitments and a free choice of exit timing; costs are a dedicated team (or buying a GP), limited deal sourcing, concentration, governance and liability (not a limited partner), adverse selection if reliant on external sourcing, and pay constraints on public funds.
- **Five-step liquidity management plan**: (1) set parameters (percent liquid daily/monthly; bands on invested capital plus uncalled commitments as a percent of total assets; escalation triggers such as cutting commitments or selling secondaries at a threshold); (2) assess portfolio liquidity from legal terms (lock-ups, notice) and track it over time; (3) model all cash flows; (4) stress test needs and flows (an art, no standard); (5) pre-agree an emergency plan on what to sell in what order, shared with the board to prevent panic.
- **ERM chain**: board sets goals and risk tolerance (volatility, drawdown, VaR/CVaR; asset-only for SWFs and endowments, asset-liability for pensions and insurers); the IPS adds liquidity parameters, active risk budget, leverage and derivative limits, ethics rules; management implements the SAA and measures risk by factor (equity, rate, credit, inflation, currency, liquidity); the risk team reports and triggers action (hedge, rebalance, secondary sale, reduce commitments). Often overlooked: currency (devaluation, costly or impossible hedges in frontier markets), drift from the SAA, and whether active risk comes from stock picking rather than hidden factor tilts.
- **Universal ownership**: a large diversified owner holds a slice of the economy, so costs externalized by one holding (pollution, labor abuse) reduce others' returns through insurance, taxes, input prices and disasters; remediation costs more than prevention, so owners should internalize externalities.
- **Climate risk map**: physical (rising seas, extreme heat, storms, wildfires; hits real assets and private equity that cannot be sold easily; insurance becomes costly or unavailable), transition (carbon pricing, coal phase-out, vehicle bans, policy that may be abrupt), opportunities (clean energy, efficiency, storage, smart grids, materials; adaptation such as agriculture and water). Tool: climate scenario analysis (2°C, 3°C, 4°C worlds, IEA and IPCC scenarios, TCFD recommendation).
- **Social risk map**: hard to quantify but financially real: community relations and social license to operate (consultation, fair land acquisition and resettlement, alternative jobs), supply-chain labor standards, and a "just" transition (worker displacement, energy cost effects on poor households).
- **Playbook 1: approval of two direct investments (scene 1: $100m airport build-operate-transfer in Sunnyland; $25m for 35% of Atsui Beverage, ABC)**
  - Facts: airport 25-year concession, $500m cost, $300m non-recourse debt, 35% of revenue to the authority, 70% of revenue regulated charges, expected 15% IRR; ABC minority stake at about 10x EBITDA ($7m EBITDA, $50m revenue), $20m of the $25m for plant modernization, 40% headcount cut, tariffs of up to 100% protect it, election pending, river with unique biodiversity.
  - Analysis: liquidity risk is not a leading risk (0.2% and 0.05% of assets, no liability pressure, direct control of exit). Real risks: traffic (airport), tariff removal (ABC), currency in frontier markets (airport revenue mostly dollar-linked, so manageable; ABC unclear), climate (runway 1 km from the sea, 25-year life), political and counterparty risk, management quality, reputation from job cuts. Weaknesses in the discussion: optimism and anecdote (the Head of PE's love of the product, "island" comfort) instead of numbers.
  - Decision demanded: scenario analysis with base, low and high cases (traffic low case about 10-11% IRR, high case high teens, capex ±10% about 13%), a view on tariff probability, and an action plan tied to triggers.
  - Why: scenario analysis is the best tool for an event with an uncertain outcome (traffic, election).
- **Playbook 2: risks materialize (scene 2, year 3)**
  - Airport: delay into year 3, cost overruns borne by the contractor, delay penalties disputed, operator AOG may renegotiate its fixed fee, rising seas and storms more frequent, heat narrows the season. Response: scenario analysis of climate impact; adaptation (storm-surge protection, with government and other beach-dependent investors sharing cost; be a contributor, avoid dodging a climate levy, to protect reputation); keep the operator happy, use the concession's incentives and break clauses, claim a concession extension if the government is liable for delay; hedge floating interest-rate exposure.
  - ABC: recession, devaluation, tariffs cut from 100% to 20%, 2-year notice for layoffs, waste dumped in the river, shorter breaks, no soap. Response sequence: engage management and change incentives (reward retention and compliance, not just margin), lobby government (a 50% cut is unworkable and 100% of jobs are at risk if tariffs sink the firm), retrain or pay reduced salary during a transition, give it a year, then exit via a distressed-asset team or a sale back; develop healthier products against the sugar-reduction trend. Primary environmental risks: sea level (airport) and waste (ABC); the shared social risk is reputation.
- **Playbook 3: ERM review (scene 3, year 5)**: airport revenue 50% below plan with costs 50% above; ABC sold for $27m (8% above cost; proceeds from a buyer for whom local production hedges currency).
  - Strengths: a full committee session devoted to risk; senior voices raised concerns.
  - Weaknesses: risks not quantified; no pre-agreed conditional action plan or hedges; too little attention to reputation and ESG because both deals were small; a vote driven by "it is small".
  - Recommendations: scenario analysis (base, optimistic, pessimistic) before investing; triggers and pre-set actions; ESG and reputational checklists for every direct deal regardless of size; independent challenge on enthusiastic deal sponsors; monitoring of direct deals after investing.

## Key Concepts
- **Existential threat**: loss event that stops the organization meeting its long-term objectives (market loss plus failure to meet cash flows).
- **Asset owner**: pension, SWF, endowment or foundation, distinct from banks and insurers by horizon and regulation.
- **Denominator effect**: the total portfolio falls more than the stale private marks, so the private share jumps.
- **Unfunded commitment**: capital promised but not yet called; part of exposure and liquidity need.
- **Unsmoothing**: statistical removal of serial correlation from reported returns.
- **Public market proxy**: liquid index standing in for a private asset's risk.
- **Savings fund (SWF type)**: converts non-renewable assets into diversified financial assets for future generations.
- **Build-operate-transfer (BOT) / PPP**: private party builds and runs a facility, then hands it to the state.
- **Non-recourse project debt**: lenders can claim only project assets.
- **Social license to operate**: community acceptance sustaining a firm's activity.
- **Physical vs transition climate risk**: damage from climate itself vs cost of the shift to low carbon.
- **Just transition**: sustainability measures designed to limit worker and household harm.
- **Active risk budget**: tracking-error allowance for active management.
- **Scenario analysis**: evaluation of outcomes under defined base, low and high states.

## Formulas & Reference Tables
- Geltner unsmoothing: `r*_t = (r_t − ρ·r_{t−1}) / (1 − ρ)`, where `r_t` is the observed return, `ρ` the first-order autocorrelation, `r*_t` the unsmoothed return. Unsmoothed variance exceeds observed variance when `ρ > 0`.
- Exposure share (illiquid): `(invested + uncalled commitments) / total assets`; set bands and escalation triggers on this ratio, not on invested capital alone.
- Position size: `investment / total assets` (airport 100/50,000 = 0.2%; ABC 25/50,000 = 0.05%).
- Direct deal valuation by multiple: EV = EBITDA × multiple (7 × 10 = $70m); a 35% stake = $24.5m, so $25m is about fair.
- Gross sale multiple (money multiple): 27/25 = 1.08x, about 1.6% a year over five years, before any interim cash.

| Risk driver | Needs rise | Sources fall |
|---|---|---|
| Payouts / support | more support to university or government | contributions, gifts and budgets cut |
| Capital calls | accelerated at distressed prices | distributions stop |
| Rebalancing | larger flows after big moves | liquid assets unattractive to sell at lows |

Unsmoothing evidence (quarterly Cambridge Associates data, 1990-2019, four classes): adjusted volatility and equity beta are higher than observed for all four. The effect is largest for venture capital, where the adjusted-volatility bars read roughly 39-48% against a much lower observed figure. The chart is not machine-readable, so exact values are omitted.

## Mental Models
- Use a long-horizon asset owner's edge (patience, counter-cyclical capacity) only after a liquidity plan is in place; the edge disappears when illiquids crowd out the sources of liquidity.
- Use unsmoothed volatility and betas for allocation decisions, reported volatility only for reporting.
- Use direct investing when you have the team and governance; use funds for diversification and access when you do not.
- Use scenario analysis (not a single expected IRR) for binary or political risks; decide in advance what you will do in each state.
- Use "small relative to the fund" for financial materiality only; reputational and ESG materiality does not scale with size.
- Use engagement and incentive redesign first for a distressed minority position, an exit plan with a deadline second.

## Worked Example
**Denominator effect (illustrative).** Portfolio 100: private 30, public 70. Public falls 30% to 49; stale private marks fall only 10% to 27. Total 76; private share = 27/76 = 35.5% versus 30% before. If private commitments of 10 are still uncalled, exposure after calls (if funded from public) = (27 + 10)/76 = 48.7% of assets. Interpretation: apparent drift and a squeeze on liquid assets arise even though no one traded; limits must refer to invested plus uncalled.

**Unsmoothing (illustrative series).** Observed returns, %: 2, 4, 5, −1, −3, −2, 1, 3 (sample standard deviation 2.90%). First-order autocorrelation estimated at 0.479. Apply `(r_t − 0.479·r_{t−1})/(1 − 0.479)` to get seven unsmoothed returns with standard deviation 5.24%. Interpretation: the true volatility is almost twice the reported figure; a mean-variance model fed the reported 2.9% would overweight the asset. (Seven pairs is too few for a real estimate; the point is the mechanics.)

**Sizing the case deals.** Airport: $100m is 0.2% of $50bn and 1.96% of the $5.1bn infrastructure book ($100m/($100m + $5,000m)); ABC: $25m is 0.05% of the fund and 0.4% of the $6.025bn private equity base used in the source. Interpretation: both are financially immaterial, which is exactly why the committee under-weighted reputational risk.

## Anti-patterns
- Reading the observed volatility of private assets at face value.
- Checking liquidity on invested capital but ignoring uncalled commitments.
- Letting a sponsor's enthusiasm replace stress cases ("love at first sip").
- Treating a stated baseline IRR as a risk assessment.
- Assuming a small ticket cannot do outsized reputational damage.
- Relying on one risk metric (VaR) for a portfolio mixing public and private assets.
- Counting on public-equity or hedge-fund liquidity in a crisis.
- Leaving currency, drift and political risk unowned.
- Waiting for a crisis to decide what to liquidate first.

## Exam Focus & Traps
- Guideline answers: liquidity risk would not be highlighted for the two deals (small, no liabilities, direct control), though it is the main portfolio risk for long-term investors; traffic risk for the airport and tariff risk for ABC need scenario analysis, not reassurance; for the election risk the Head of PE's rapport building is insufficient without quantified impact.
- Interest-rate risk on project borrowing: hedge it. Health-trend risk: develop healthier products.
- Primary environmental risk: climate and rising seas (airport; adaptation plus scenario analysis) and waste dumping (ABC; persuade, educate, regulations catch up and cleanup costs more). Common social risk: reputation (soap, breaks, job cuts, supply-chain labor).
- ERM answer structure: key facts, strength (dedicated committee, broad risk list), weaknesses (no quantification, no conditional plan, thin ESG attention for small deals), recommendations (scenario analysis, pre-agreed actions, hedging).
- Direct investing: no unfunded commitments and exit control, but concentration, adverse selection and governance risks.
- Unsmoothing raises volatility and market correlation; mean-variance remains inadequate even after unsmoothing; practical fix is constraining illiquid weights.
- Banks and insurers are excluded from this reading's liquidity focus (asset-liability and capital rules dominate).
- **⚠ Correction**: the airport funding is described as roughly 70/30 debt/equity, but $300m of $500m is 60% debt; the memo's $6bn private equity base does not reconcile with the stated 10% private capital allocation either. Both are source inconsistencies; the chapter uses the stated figures.


## Key Takeaways
- Existential risk for asset owners is market loss plus illiquidity; the denominator effect and gates make it worse.
- Always measure private assets with unsmoothed or proxy-based risk and cap their weights.
- A five-step liquidity plan (parameters, assessment, cash-flow model, stress test, emergency plan) with bands on invested plus uncalled capital is the control system.
- Direct investing buys fee savings and control at the price of team, concentration and governance risk.
- Climate and social risks enter through scenario analysis, adaptation, engagement and incentive design.
- Quantified scenarios and pre-agreed actions separate a risk discussion from a risk process.
- Size does not cap reputational risk; a $25m stake produced a diplomatic and headline problem.

## Connects To
- **ch04**: institutional investor types and IPS elements the ERM chain supports.
- **ch05**: endowment case: liquidity budget, commitment pacing and ESG integration policy in practice.
- **ch06**: household risk case, same discipline (identify, size, manage, monitor) at a different scale.
- **`cfa-alternative-investments` ch06**: private market allocation, fees and illiquidity.
- **`cfa-portfolio-management` ch08**: risk management intro (tolerance, budgeting, VaR/CVaR).
- **`cfa-portfolio-management` ch13**: market risk measurement (VaR, stress tests, scenario analysis).
- **`cfa-asset-allocation-cme` ch08**: constraints and real-world asset allocation.
- **`cfa-derivatives` ch06**: hedging interest-rate and currency risk.
