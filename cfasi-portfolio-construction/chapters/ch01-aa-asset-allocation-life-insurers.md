# Chapter 1: Asset Allocation in Life Insurance Companies (Asset Allocation nelle compagnie di assicurazione vita)
> **Source**: CFA Society Italy x Advisor Private, "Asset Allocation" guide (Advisor Private no. 25, 2020), Introduction and Chapter 1 | Daniele Cappellini, CFA, and Orazio Di Miscia; closing insert on clear investment objectives is Vanguard-sponsored (attributed below)

## Core Idea
Asset allocation is the allocation of wealth across asset classes (groups sharing the same risk factors such as rates and currency). **Strategic asset allocation (SAA)** uses long-run return and risk assumptions; **tactical asset allocation (TAA)** exploits short-term mispricing. For a life insurer the problem is **liabilities-driven (LDI)**: guaranteed capital or minimum returns, long and uncertain liability cash flows, and a solvency regulator. Allocation is therefore a multi-period, scenario-based **ALM** optimization of value, risk and capital, not a one-shot Markowitz run.

## Frameworks Introduced
- **Performance decomposition (Brinson-style)**: `Portfolio performance = SAA + TA + SS + IR`. When to use: judging a manager after a fair interval against a unique, ex-ante, replicable multi-asset benchmark. How: (1) fix SAA/benchmark; (2) TA (allocation) = over/underweight of asset classes versus SAA; (3) SS (selection) = better securities inside each class; (4) IR = interaction residual, small unless the portfolio is very unbalanced. Why it works: separates policy, timing and stock-picking skill. Failure mode: dropping a position after short-term underperformance instead of judging over the horizon the thesis implied. Brinson et al. (Determinants of portfolio performance) found SAA explains most of the variation of returns over time; the finding is debated but the primacy of SAA is widely accepted.
- **Insurance IPS for Ramo I (guaranteed life) portfolios**: the Investment Policy Statement lists objectives and constraints.
  - Return objective: at least the guaranteed minimum plus the company margin (management fees); this feeds **Value of In-Force (VIF)** = present value of future profits.
  - Regulatory capital (Solvency II): Solvency ratio = Own Funds / SCR; SCR is the capital to absorb a 1-in-200 style shock on market-consistent assets minus liabilities (formulation: SCR = Own Funds loss when assets are stressed while liabilities absorb part of the shock). Market risk SCR covers equity, rates, spread, property, currency, concentration, and illiquidity; standard formula versus internal model.
  - Liquidity: project asset and liability cash flows (gap cumulato) so that surrenders and claims never force sales when unrealized losses exist.
  - Universe: bond-heavy; growing private markets/real assets, within IVASS rules (2016 revision widened allowed classes but demands demonstrated understanding of risks).
  - Time horizon: long, consistent with liability run-off (simulations run about 60 years, monthly steps).
- **Insurance (statutory) return**: `Insurance return = (coupons + dividends + issue discount + realized gains/losses) / average capital`. Unrealized gains are excluded; returns are pooled across clients through average capital (principle of mutuality), unlike fund returns that are per unit. Rising rates lift the book yield of old policies as new money is reinvested; falling rates erode it.
- **Risk Appetite Framework (RAF)**: Risk Strategy (which risks to take/avoid) -> Risk Appetite (desired level) -> Risk Preference/soft limit (warning level) -> Risk Tolerance/hard limit -> Risk Capacity (point of recapitalization). Each breach level triggers pre-agreed management actions. Value, risk and capital form a circular relation: more value needs more risk, which consumes more capital.
- **ALM-driven SAA process (7 steps)**: (1) set return targets of each asset class; (2) generate real-world stochastic scenarios (term structures 3m-30y, spreads, equity, FX, inflation, alternatives) with volatilities and correlations; (3) project assets and liabilities jointly in every scenario for each candidate allocation; (4) measure impact on policyholder returns, P&L, and capital absorption; (5) plot candidates on risk-return space and form an efficient frontier; (6) filter by RAF limits and current and projected solvency; (7) pick the proposal, feed back product design (capital-efficient guarantees). No closed form: the optimum emerges from simulation and judgment.

## Key Concepts
- **LDI (liabilities driven investment)**: investing to meet contractually due future cash outflows.
- **Ramo I**: Italian life policies with guaranteed capital and/or minimum return; **Ramo III** are unit/index-linked with benefits tied to fund values.
- **Inverted production cycle**: the insurer promises long-dated guarantees first and invests premiums later in shorter assets.
- **Duration mismatch / reinvestment risk**: assets shorter than liabilities; falling rates threaten the guarantee, rising rates inflict capital losses if surrenders force sales.
- **Convexity of liabilities**: liabilities gain value faster than assets when rates fall, shrinking available capital.
- **SCR / MCR**: Solvency Capital Requirement / Minimum Capital Requirement.
- **Own Funds**: available capital (market-consistent assets minus liabilities, adjusted).
- **VIF**: present value of future in-force profits.
- **Real-world scenarios (RW)**: scenarios with differing expected returns, as opposed to risk-neutral ones.
- **Chopra-Ziemba (1993) result**: errors in expected returns hurt mean-variance outcomes roughly 10x more than errors in variances, and variance errors matter about twice as much as covariance errors.
- **Risk parity**: weights set so each component contributes equal risk, independent of return forecasts.
- **Naive fixed-split allocation**: preset risky/risk-free percentages matched to standard risk profiles.

## Formulas & Reference Tables
- `Performance = SAA + TA + SS + IR` (IR = interaction).
- `Solvency ratio = Own Funds / SCR`.
- `Insurance return = (coupons + dividends + issue discount + realized P/L) / average capital`.
- Chopra-Ziemba sensitivity of optimal weights to input error: mean error : variance error : covariance error ≈ 10 : 2 : 1.
- Cost drag (Vanguard insert): `FV = 100,000 x (1 + r)^30`, r = 6% gross.

| Scenario (30y, 6% gross, 100k start) | End value (recomputed) |
|---|---|
| No fees | 574,349 |
| 0.25% fee, deducted from return | about 533k (source shows 532,899) |
| 0.62% fee (US equity-fund asset-weighted average ER, end 2019) | about 477k (source shows 477,141) |
Subtracting the fee from the return gives 535,071 and 481,666 instead; gap is 53-56k depending on fee timing. The conclusion (about 10% of terminal wealth lost) is robust.

## Mental Models
- Use LDI thinking whenever outflows are contractual: the liability profile is both constraint and opportunity.
- Use SAA for the answer to "what mix serves this balance sheet", TAA only for short, modest tilts.
- Use scenario ALM instead of a point-estimate frontier when guarantees create convex payoffs and path dependence.
- Use soft/hard limits so that governance decisions are pre-committed before stress hits.
- Control costs first: markets are uncontrollable, fees are controllable.

## Worked Example
Compare two 30-year fee drags. Inputs: 100,000 start, 6% gross, fees 0.25% vs 0.62% deducted from annual return. Steps: 1.0575^30 = 5.3507 and 1.0538^30 = 4.8167. Result: 535,071 vs 481,666, a 53,405 gap (about 10% of terminal wealth). Interpretation: a 37 bp fee spread compounds into a tenth of final wealth; active fund selection must clear that hurdle before adding value.

## Anti-patterns
- Applying strict Markowitz to insurers: the optimizer concentrates in a few "efficient" classes.
- Chasing high star-rated funds (Morningstar ratings were unreliable predictors of 3-year outperformance; flows follow past stars).
- Bottom-up "fund collecting" without a portfolio-level plan.
- Reacting to market rumors or short-term underperformance; failing to rebalance; market timing.
- Reaching for yield in a falling-rate environment without capital assessment.

## Practitioner Notes
- Define objectives that are measurable and attainable; if the plan needs exceptional returns, revise saving or spending, not risk.
- The investor's risk tolerance and horizon are the main constraints; also tax, liquidity, legal, and ethical exclusions; review regularly.
- Regular, increasing contributions are more reliable than market returns (Vanguard insert).
- Insurance book-value return differs from total return: do not benchmark Ramo I mandates on mark-to-market alone.

## Key Takeaways
- SAA dominates long-run return variability; TAA and selection are second-order.
- Expected returns are the most dangerous input to an optimizer.
- Insurer allocation = value x risk x capital under Solvency II, solved by joint asset-liability simulation.
- Liability convexity means falling rates hurt capital even when assets gain.
- RAF thresholds convert risk appetite into automatic management actions.
- Costs compound: 0.37% extra fee costs about 10% over 30 years.
- Define benchmark ex ante and judge over the full horizon.

## Connects To
- **ch02**: institutional allocation framework generalizing these constraints.
- **ch03**: allocation within funds and the VAAM model.
- **`cfa-asset-allocation-cme`**: capital-market expectations, Markowitz, risk parity.
- **`cfasi-portfolio-construction` ch05**: passive implementation of the SAA.
