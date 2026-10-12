# Chapter 4: Asset Allocation for Private Investors (Asset Allocation negli investimenti privati)
> **Source**: CFA Society Italy x Advisor Private, "Asset Allocation" guide (Advisor Private no. 25, 2020), Chapter 4 | Alessandro Sorvillo, CFA

## Core Idea
Private clients are not the rational utility maximizers of classical theory. Their goals are personal (a house, a child's university), their "risk" is the probability of missing the goal rather than standard deviation, and their biases cost real money (behaviour gap). The adviser's job: measure ability and willingness to take risk, identify cognitive vs emotional biases, then build an allocation that is a deliberate compromise between what is optimal and what the client will actually hold. Cognitive biases are moderated (corrected); emotional biases are adapted to.

## Frameworks Introduced
- **Cognitive vs emotional biases**: cognitive = errors in how information is processed or remembered; emotional = decisions driven by feelings. When to use: first diagnostic. How: classify each observed bias; cognitive ones can usually be worked around once the source is found; for emotional ones the practical solution is to adapt the plan. Distinction is not always clean but guides the remedy.
- **Common biases (clusters)**:
  - Frequent traders: cognitive dissonance (new information conflicting with prior beliefs is ignored or filtered), confirmation bias (seeking what confirms), overconfidence (overrating own skill; ignoring advisers, including private bankers).
  - Retail traders' trio: illusion of control (assigning too high a probability to own choices paying off), hindsight bias (seeing past outcomes as predictable, then trusting a supposed forecasting ability), mental accounting (separate compartments; reports "a 10,000 gain" on one trade while others lose; closes a winner and leaves losers open while feeling ahead).
  - Single-parameter focus: choosing a stock for its dividend or a bond for its coupon, a failure of Modigliani-Miller-style indifference between dividend and capital gain.
  - Italy-specific (author's observation): **liquidity bias** (refusing any investment, even short capital-guaranteed deposits, while holding cash: real wealth erodes with inflation and negative rates, and bail-in rules (EU, 2014) can impose losses on deposits) and **underlying bias** (excluding a whole instrument type a priori, e.g. refusing funds or insurance wrappers). Liquidity/underlying bias are easier to adapt around: reach the same goal with other instruments unless a feature is specific (e.g. succession planning via policies).
- **Ability vs willingness to take risk**: ability = objective capacity from income bracket, dependants, real and financial assets, horizon; willingness = subjective, from personality and past experience. Take the lower of the two as the binding constraint. In Italy, low financial literacy tends to make willingness over-conservative.
- **Risk-profile gathering**: collect hard and soft data on household wealth, family and lifestyle, existing risk cover (insurance), personal goals; then open questions that surface both tolerance and biases. Sample questions: capital protection vs return? past investing experience? control or delegation? self-rated skill? coupon income vs terminal capital? knowledge of equities vs bonds? Output: an IPS (financial plan).
- **Behaviorally modified asset allocation**: build the plan as a compromise between theory and what the client wants. Decide **moderate vs adapt** using wealth/savings and bias type: large wealth and high savings rate can afford to adapt more; low wealth or low saving should moderate toward the financially correct portfolio; emotional biases lean to adapting, cognitive to moderating. Deviation guide (Table 1, presented as advice not rule), as allowed departure from the rational allocation per asset:

| | Cognitive biases | Emotional biases |
|---|---|---|
| High wealth / savings | small change: +/- 5-10% per asset | major change: +/- 10-15% per asset |
| Low wealth / savings | stay close to the optimum: +/- 3-5% | small change: +/- 5-10% |

- **Goal-based layering and behavioral rebalancing**: split the plan into goal buckets with their own objective. Institutions set a risk level, model the mix and rebalance beyond a band; for a private investor, risk = probability of missing the goal, so rebalancing is judged against the goal, not back to a mix. Example from the text: a 70/30 bond/equity mix drifting to 60/40, where bonds fund the house deposit in 10 years and equity funds the child's university, may need no rebalancing because the bond bucket still delivers the reserve (the author cites Statman 2019).
- **Investor return vs investment return (TWRR vs MWRR)**: TWRR = manager skill, neutralizes cash flows; MWRR (modified Dietz) = what the investor really earned, sensitive to timing of deposits and withdrawals. Gap between them (and between fund return and average investor return) = **behaviour gap**.

## Key Concepts
- **Homo economicus**: rational maximizer assumed by classical theory (Modigliani-Miller; Markowitz 1952).
- **Behavioral finance**: field explaining systematic departures from rational choice.
- **Cognitive dissonance**: new information conflicting with held beliefs is rejected or distorted.
- **Confirmation bias**: seeking and weighting evidence that supports existing views.
- **Overconfidence**: overestimating own ability, hearing only oneself.
- **Illusion of control**: believing one can influence investment outcomes.
- **Hindsight bias**: treating past outcomes as having been predictable.
- **Mental accounting**: separate "drawers" for money, evaluating each in isolation.
- **Liquidity bias / underlying bias**: Italian-market biases (see above).
- **Bail-in**: EU rule allowing creditors, including depositors above guaranteed limits, to bear a bank's losses.
- **Ability / willingness to take risk**: objective capacity / subjective appetite.
- **IPS**: written plan with goals, risk profile, constraints.
- **TWRR / MWRR**: time-weighted / money-weighted rate of return.
- **Behaviour gap**: difference between what an investor could have earned and what was earned because of timing and plan deviations.

## Formulas & Reference Tables
- Subperiod return `r = (EMV - BMV) / BMV` measured whenever the client's invested amount changes (flows).
- `TWRR = (1 + r_1)(1 + r_2)...(1 + r_n) - 1` (chain-linked over subperiods separated by cash flows).
- Modified Dietz (MWRR approximation): `R = (EMV - BMV - sum CF_i) / (BMV + sum w_i x CF_i)`, `w_i = (CD - D_i) / CD`, where `CD` = days in the period, `D_i` = days elapsed from the start to flow `i` (weight = fraction of the period the flow is invested). The source formula images were lost in extraction and the source describes D_i as days since the flow originated; the reconstruction above is the standard version.
- Behaviour gap evidence (as cited, with sources): Davis Advisors 1994-2013: equity fund average 8.7% vs average fund investor 5.0%, gap 3.7% a year (verified 8.7 - 5.0 = 3.7); Morningstar (2009) on CGM Focus Fund: about +18% annualized over 10 years for the fund vs about -17% for the average investor (as quoted).

## Mental Models
- Use "moderate" for cognitive biases and "adapt" for emotional ones; use wealth and savings to decide how far you can bend.
- Use the lower of ability and willingness as the risk limit.
- Use goals, not volatility, as the unit of risk for individuals: probability of shortfall.
- Use TWRR to judge the manager, MWRR to judge the investor's actual experience.
- Use the behaviour gap as the sales argument for discipline and for automatic contributions/rebalancing.

## Worked Example
TWRR vs modified Dietz, with a badly timed inflow. Inputs: 100 invested on day 0; at day 90 the account is worth 120 and the client adds 100; at day 180 it is worth 190. Steps: sub-period 1 return = (120 - 100)/100 = +20.0%; sub-period 2 return = (190 - 220)/220 = -13.64%; TWRR = 1.20 x 0.8636 - 1 = +3.64%. Modified Dietz: flow weight = (180 - 90)/180 = 0.5, MWRR = (190 - 100 - 100) / (100 + 0.5 x 100) = -10/150 = -6.67%. Interpretation: the portfolio itself gained 3.6% (manager skill), but the investor lost 6.7% because the larger sum arrived just before the fall: the gap of about 10 points is behaviour gap in miniature.

## Anti-patterns
- Pushing the optimal portfolio onto a client who will abandon it in the first drawdown.
- Treating the risk questionnaire as only a compliance form and not a bias detector.
- Rebalancing a goal-based plan back to the original percentages without asking whether the goal is still funded.
- Letting a client hold only cash "to be safe" without showing the real-terms loss and bail-in exposure.
- Reporting only the fund's TWRR to a client who trades in and out.
- Same remedy for all biases: cognitive biases need information and reframing, emotional ones need plan design.

## Practitioner Notes
- Hard facts (wealth, income, dependants) fix ability; the conversation fixes willingness. Record both in the IPS.
- Ask open questions to surface bias (control vs delegation, coupon vs capital, self-rating of skill).
- Show total-portfolio performance to counter mental accounting; separate buckets for goals but integrated reporting.
- Use the Table 1 bands as starting guidance only; adapt to number of assets, return target and diversification level.
- The behaviour-gap figures come from third-party studies (Davis Advisors, Morningstar) cited by the author; check the current literature before quoting numbers to clients.

## Key Takeaways
- Real clients violate the rational-agent model; behavioral finance explains how and offers remedies.
- Distinguish cognitive from emotional biases: moderate the first, adapt to the second.
- Ability to take risk is objective; willingness is subjective; both go into the IPS.
- Wealth and savings determine how much room you have to accommodate biases (+/- 3-5% up to +/- 10-15% per asset).
- For individuals, risk is the probability of missing the goal; layer the plan by goals and rebalance with that lens.
- TWRR measures the manager; MWRR measures the investor; the difference reflects timing and behaviour.
- Poor timing of flows cost the average investor several points a year in the cited studies.

## Connects To
- **ch01**: the closing Vanguard insert on clear, measurable objectives (same goal-setting logic).
- **ch02**: institutional IPS, rebalancing bands and CPPI as the institutional counterpart.
- **ch03**: TWRR/attribution and rebalancing corridors in fund management.
- **ch05-ch08**: low-cost passive vehicles as discipline tools for retail investors.
- **`cfa-portfolio-management` ch04 and `cfa-asset-allocation-cme` ch01-ch02**: investor IPS, behavioral biases.
- **`cfa-wealth-institutional-management`**: private wealth, behavioral biases and client profiling.
- **`cfa-ethics-gips`**: TWRR and GIPS performance calculation.
