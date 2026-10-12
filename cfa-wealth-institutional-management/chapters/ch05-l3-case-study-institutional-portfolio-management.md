# Chapter 5: Case Study in Portfolio Management: Institutional
> **Source**: CFA Program Curriculum 2023, Level III, Reading 28 · Portfolio Management | Gabriel Petre, CFA (Quadrivium University endowment / QUINCO case)

## Core Idea
A $8 billion university endowment (QU, run by the investment office QUINCO) wants to raise its illiquid exposure, add a tactical overlay and keep a disciplined rebalancing process. The case is a chain of eight reusable decisions: how to size illiquidity (liquidity budget, time-to-cash, stress), how to justify more private markets (illiquidity premium, unsmoothed inputs, Monte Carlo), what to do when a manager pitch is conflicted (Code and Standards), which vehicle to use for a tactical tilt or a rebalance (ETF vs futures vs total return swap vs cash managers, decided by cost, leverage, horizon and speed) and how to answer an ESG protest (integration plus engagement, divestment last). Every decision is framed as situation → analysis → decision → why.

## Learning Outcomes Covered
- discuss tools for managing portfolio liquidity risk (profiling, rebalancing and commitment pacing, stress tests, derivatives)
- discuss capturing the illiquidity premium as an objective
- analyze asset allocation and portfolio construction against liquidity needs and risk/return requirements; recommend actions
- analyze manager-selection conduct against the Code and Standards
- analyze the costs and benefits of derivatives versus cash-market techniques for exposures
- demonstrate derivatives overlays in tactical asset allocation (TAA) and rebalancing

## Frameworks Introduced
- **Liquidity management stack (time-to-cash + liquidity budget)**: classify every holding into time-to-cash buckets, then set minimum weights for the liquid buckets and a maximum for the illiquid one.
  - When to use: any asset owner with spending or capital-call outflows and private-market holdings.
  - How: (1) list cash outflows (distributions to the university, capital calls) and inflows (donations, distributions); (2) define buckets, e.g. <1 week "highly liquid" (budget at least 10%), <1 quarter "liquid" (at least 35%), <1 year "semi-liquid" (at least 50%), >1 year "illiquid" (at most 50%); (3) profile bottom-up, vehicle by vehicle (separate account vs commingled fund vs ETF vs futures; lock-ups, notice periods, gates), then aggregate; (4) test the profile under stress; (5) monitor drift.
  - Reading the budget: the minimums are cumulative ("within one quarter or faster"), otherwise a 24% "liquid" bucket would breach the 35% floor even in normal conditions. The source does not say this explicitly, so state your reading when you answer.
  - Why it works: the budget is set from stress results, so the portfolio can meet outflows without forced sales. Failure mode: profiling at asset-class level hides vehicle differences (a concentrated small-cap EM commingled fund may only offer quarterly liquidity).
- **Stress test with three liquidity leaks**: stress assets and liabilities at once (volatility, correlations, liquidity; higher distributions; donations drop).
  - Three leaks in the case: (a) capital calls exceed distributions, so private weight rises; (b) gates on hedge funds and real estate funds; (c) the smoothing effect (private valuations lag, so private weight rises relative to falling public assets, cutting the percentage that is liquid even though dollars of liquidity are unchanged).
  - Design: historical events (2008), statistical (extreme value theory) or hypothetical scenarios.
- **Rebalancing stack for a mixed liquid/illiquid portfolio**: (1) systematic rules (calendar or percent-range) with bands wider for more volatile classes; (2) automatic adjustment, using a liquid public proxy to offset drift in a private class (private equity beta 1: if PE is 1% over target, cut public equity 1%; this fixes market beta but raises illiquidity risk); (3) multi-year commitment pacing for private funds using cash flow models of calls and distributions.
  - When to use: always for illiquids, because rebalancing them is extremely costly and liquidity falls in stress.
- **Illiquidity premium capture**: expected compensation for tying up capital for an uncertain period; positive in private equity and private real estate and rising with the length of the illiquidity horizon.
  - Estimation: put-option approach (Chaffe 1993; Staub and Diermeier 2003): illiquid price = marketable price − value of a put struck at the marketable price; premium = difference in expected returns of the two. Public low-liquidity stocks also earn a premium (Pastor and Stambaugh), but it is hard to isolate from market, value and size factors and index-level estimates may not match the few funds actually held.
- **Playbook A: raise private equity and real assets (18%→23% PE, 13%→16% real assets)**
  - Situation: endowment trails peers since 2008, return expectations fell for every asset class, spending of 5% plus 2-3% inflation needs 7-8% nominal, risk tolerance is a 12-14% volatility range.
  - Analysis: unsmooth private returns, run mean-variance with net-of-fee assumptions, then Monte Carlo on 20-year purchasing power. Result: expected real return 5.0%→5.3%, volatility 12.5%→13.2%, Sharpe 0.33→0.34, probability of a 25% purchasing-power erosion 35%→30% (equivalently 65%→70% chance of keeping at least 75%).
  - Decision: approve, phase in over 2-3 years.
  - Why: lower return expectations force more risk for the same return; the portfolio was more conservative than peers; the illiquid book is mature and diversified by manager and vintage; higher volatility is inside the 12-14% band. Conditions: avoid concentration in a few funds, stay inside the liquidity budget (confirm in stress), accept higher fees (already net in the inputs).
- **Playbook B: conflicted manager selection (facts → standards → action)**: Genex Venture Capital (GVC) is run by a QU trustee, the president and treasurer press for it, its pitch uses what looks like non-public university information and shows returns above third-party databases, a presenter is the CIO's ex-colleague, and the sponsoring PM's wife is the founder's daughter. Required conduct is in the Exam Focus section.
- **Playbook C: choose the implementation vehicle for a tactical tilt** (1% US equity overweight = $80m notional; ETF, futures, total return swap). Cost rule: total = commissions + spread + price impact + management fee + mispricing/tracking + roll + funding (all in bp), plus a leverage term.
  - Unlevered: ETF 35 bp, futures 42 bp, TRS 51 bp, so ETF wins (and is flexible, no margin monitoring, no counterparty).
  - Levered 4x: add ETF borrowing (75% borrowed × (Libor 2% + 50 bp)) = 187.5 bp; futures and TRS lose the Libor on the 75% of cash no longer deposited = 150 bp. Totals: ETF 222.5, futures 192, TRS 201. Futures win by 30.5 bp over ETF, provided the team accepts the quarterly roll and daily margin work.
  - Why: ETFs are cash-hungry (margin capped at 50%, so at most 2x at instrument level); futures and TRS free cash; TRS has zero tracking error but counterparty credit risk and OTC complexity.
- **Playbook D: rebalance by cash market or by derivatives** (QUINCO: calendar-quarter policy, monthly monitoring, corridor per class, discretion to go to target or to the corridor edge; illiquids rebalance by pacing commitments, not trades). International developed equity at 11.5% breached its 11% ceiling (target 9%, ±2%); fixed income at 6.5% was inside its 6-12% corridor.
  - 0.5% trade (to the edge, one quarter): cash 30 bp (5 spread, 5 impact, 20 cash drag) vs futures 24 bp (3, 4, 17 mispricing). Futures win and keep managers in place.
  - 2.5% trade (to target, one year): cash 60 bp (5, 5, 50 drag) vs futures 82 bp (4, 4, 68 tracking, 6 roll). Cash wins.
  - Rule: derivatives for small, temporary, fast, reversible moves; cash for large, permanent realignments. Futures cost rises with horizon (tracking risk accumulates), cash drag rises with trade size. Two futures legs (equity short + bond long) add tracking error.
- **Playbook E: ESG protest (Portro Inc.)**: students demand divestment after an ILO report on supplier labor abuses; QU is invested through index exposure and one concentrated manager overweight.
  - Analysis: monitoring had already flagged Portro's social score; the manager was engaged at the last quarterly review and had a robust ESG process but no formal policy.
  - Decision: stay invested; escalate through PRI collaborative engagement and proxy votes for supply-chain disclosure; formal reply to students; separate decision on campus merchandise (pulled temporarily).
  - Why: QUINCO's policy is ESG integration plus responsible ownership, not exclusion; divestment is a last-resort, suboptimal mitigation. The updated policy requires manager due diligence on ESG policy, process, disclosure and consistency, monitoring of carbon metrics and ESG ratings, and PRI signatory status.

## Key Concepts
- **Liquidity management**: policies ensuring the portfolio meets cash outflows in a timely, orderly way without distressed sales.
- **Time-to-cash table**: buckets by days/weeks/quarters to convert holdings to cash without moving the price.
- **Liquidity budget**: minimum weights in liquid buckets and maximum in the illiquid bucket; the liquidity benchmark for portfolio construction.
- **Gate**: a fund manager's right to refuse or limit withdrawals in stress, lengthening time-to-cash.
- **Smoothing effect**: lagged private valuations that raise private weight relative to liquid assets in a drawdown.
- **Unsmoothing (de-smoothing)**: removing serial correlation from appraisal-based returns so risk is not understated.
- **Commitment pacing**: annual private-fund commitment level that targets an allocation given modeled calls and distributions.
- **Geometric smoothing (Yale) spending rule**: `Spending_t = 66% × Spending_{t−1} + 34% × (5% × MV_{t−1})`; stabilizes payouts but is countercyclical in rate.
- **Active risk budget**: tracking-error limit versus policy (QUINCO: 100 bp raised to 250 bp, of which up to 150 bp for TAA, leverage up to 5% of portfolio value).
- **Overlay**: derivative positions that change exposures while external managers stay in place.
- **Mispricing / tracking error (vehicle)**: gap between vehicle and index return; ETF from premium/discount and cash drag, futures from supply-demand and dividend and rate differentials, TRS none.
- **Cash drag**: return lost while money moves between managers or while a manager sells and the other buys.
- **Rebalancing corridor**: percent range around target; breach triggers rebalancing to target or to the corridor edge.
- **Fair-value / mean-reversion TAA model**: compares market price to model value over a 1-3 year horizon, trades only if the deviation exceeds costs.
- **ESG integration**: explicit, systematic inclusion of ESG factors in analysis and decisions (CFA Institute/PRI definition).

## Formulas & Reference Tables
- Spending rule: `S_t = w·S_{t−1} + (1−w)·r·MV_{t−1}` with `w` = weight on prior spending (0.66), `r` = 5%, `MV_{t−1}` = prior year-end market value.
- Required nominal return ≈ spending rate + inflation = 5% + 2-3% = 7-8% (real-value preservation).
- Portfolio liquidity by bucket: `%bucket = Σ_i (weight_i × share of i in bucket)`.
- Leveraged cost: borrowed fraction `b = 1 − 1/L`. ETF extra = `b × (Libor + spread)`; futures/TRS extra = `b × Libor` (lost interest on cash not deposited).
- Total implementation cost (bp) = sum of components; levered total = unlevered total + leverage term.
- Breakeven leverage, ETF vs futures (case numbers): `35 + 250b = 42 + 200b` gives `b = 0.14`, `L = 1/(1−b) ≈ 1.16`. Above about 1.16x futures are cheaper.
- Illiquid price = marketable price − put value (strike = marketable price).
- Rebalancing band: width should rise with asset volatility; transaction costs, correlations among classes and investor risk tolerance also shape it.

| Exhibit | Unlevered cost (bp) | Levered 4x add-on | Levered total |
|---|---|---|---|
| ETF | 35.0 | 187.5 | 222.5 |
| Futures | 42.0 | 150.0 | 192.0 |
| Total return swap | 51.0 | 150.0 | 201.0 |

| QU liquidity profile (%) | Highly liquid | Liquid | Semi-liquid | Illiquid |
|---|---|---|---|---|
| Current, normal | 19 | 26 | 22 | 33 |
| Current, stress | 15 | 26 | 20 | 39 |
| Proposed, normal | 14 | 24 | 23 | 39 |
| Proposed, stress | 11 | 25 | 21 | 43 |

## Mental Models
- Use the liquidity budget as the cap on private markets: the allocation is chosen by return and risk, then checked against stressed liquidity, never the reverse.
- Use a public proxy to hold risk steady when private assets drift, but remember it fixes beta, not illiquidity.
- Use derivatives for speed and reversibility, cash managers for permanence: cost crossover is horizon and size.
- When leverage is on the table, re-run the vehicle choice; the cheapest unlevered vehicle can be the dearest levered one.
- Treat a conflict as a disclosure-and-recusal problem first (disclose, recuse, document), a hiring problem second.
- Use engagement before exclusion when policy is integration; divest only when engagement fails and the thesis is broken.

## Worked Example
**Liquidity budget check on the proposed SAA under stress.** Inputs: proposed stress profile 11 / 25 / 21 / 43 (highly liquid / liquid / semi-liquid / illiquid); budget at least 10 / 35 / 50 and illiquid at most 50, read cumulatively.
1. Within one week: 11% ≥ 10%, pass by 1 point.
2. Within one quarter: 11 + 25 = 36% ≥ 35%, pass by 1 point.
3. Within one year: 11 + 25 + 21 = 57% ≥ 50%, pass by 7 points.
4. Illiquid: 43% ≤ 50%, pass by 7 points.
Interpretation: compliant, but two buckets have a 1-point cushion in stress. Add monitoring triggers and slow the commitment pace; if the budget were read bucket by bucket (25% vs 35%) the portfolio would fail, so the reading must be agreed with the board.

**Vehicle choice at 4x leverage.** Futures: 42 + 0.75 × 200 = 192 bp. ETF: 35 + 0.75 × 250 = 222.5 bp. Difference 30.5 bp, about $0.24m a year on $80m. Interpretation: take futures, with a written roll and margin procedure.

**Spending rule in a drawdown.** Base: `0.66 × 358.1 + 0.34 × 0.05 × 7,002.3 = 355.4` ($m). Assume the endowment drops 20% to 5,601.8: `0.66 × 355.4 + 0.34 × 0.05 × 5,601.8 = 329.8`. Spending falls only 7.2% while assets fall 20%, so the effective rate is 5.9%, above the 5% target. Interpretation: the smoothing that protects the university's budget raises liquidity demand exactly when donations and distributions dry up.

## Anti-patterns
- Feeding appraisal-based private volatility into mean-variance: understated risk inflates the optimal illiquid weight.
- Profiling liquidity by asset class instead of by vehicle and contract terms.
- Comparing vehicles only unlevered when the overlay will be levered (or vice versa), or ignoring the interest earned on freed cash when judging TAA profitability.
- Choosing futures for a large, permanent rebalance because the first quarter looks cheap.
- Equal-width bands for cash and private equity (cash band should shrink; PE band should widen).
- Relying on "everyone knows" instead of formal disclosure of a family tie to a manager.
- Treating divestment as the default answer to an ESG controversy under an integration policy.

## Exam Focus & Traps
- Longer illiquidity horizons carry higher premia, so favor longer-term, not shorter-term, private holdings. Low-liquidity public equity is only a partial substitute: the premium is hard to isolate from market, value and size factors.
- Band-policy question: the lowest-volatility class with a wide band (cash 0-15%, sd 1.5%) needs tightening; the highest-volatility class with a tight band (private equity 20-25%, sd 27.2%) needs widening.
- Bottom-up liquidity: multiply each class weight by its liquid/illiquid share, sum. For the practice portfolio: liquid = 1 + 24 + 0.5×39 = 44.5% (floor 30%); illiquid = 21 + 0.5×15 = 28.5% (cap 40%), so room exists to add illiquids.
- Leverage arithmetic: 4x means borrow 75%; 3x means borrow 66.7%. Practice case: ETF 27 + 143 = 170 bp vs futures 32 + 120 = 152 bp, futures by 18 bp.
- ETF vs TRS for an unlevered tilt: ETF needs the most capital, is the most liquid and has tracking error; TRS needs little capital, is OTC, has exact index replication and counterparty risk.
- Standards in the GVC case: Winter: VI(A) disclosure of conflicts, I(B) independence, III(E) confidentiality, I(C)/III(D) performance accuracy, V(A) diligence. Hall: IV(A) loyalty as trustee, VI(A), III(E). University president/treasurer: IV(A), VI(A), I(B). Allen: I(C), III(D). Davis: I(B), VI(A); disclose explicitly, do not assume it is known.
- Langhorne/Dixon: falsely claiming CFA Institute "member firm" status breaks I(C), VII(A), VII(B); deducting a hypothetical 1% fee from the benchmark but a lower actual fee from the composite (average about 0.63% on a $60m account) breaches GIPS and III(D), possibly I(D); an all-expenses golf trip threatens I(B).
- Spending rule: the geometric rule lowers payout in strong markets and raises the rate in weak ones; it worsens liquidity strain in a downturn.
- Illiquid classes are rebalanced by pacing commitments, not by selling positions.
- **⚠ Correction**: Exhibit 10's expected returns (7.5% current, 7.8% proposed) sit slightly below the weighted averages of the Exhibit 7 inputs (7.64% and 7.97%; real 5.03% and 5.35%); volatilities (12.5%, 13.2%) and Sharpe ratios (0.33, 0.34) reproduce. The breakeven leverage of about 1.16x is derived here, not in the source, and ignores interest earned on freed cash.


## Key Takeaways
- Set the liquidity budget from stress results and check any allocation change against it (the case passes by a 1-point margin in two buckets).
- More private markets can raise expected return and lower long-term shortfall risk even as volatility rises; justify with unsmoothed inputs and Monte Carlo, and confirm fit with the risk tolerance and liquidity budget.
- Illiquid rebalancing runs through commitments and public proxies; liquid rebalancing runs through bands, with wider bands for volatile classes.
- Vehicle choice flips with leverage: ETF best unlevered (35 vs 42 vs 51 bp), futures best at 4x (192 vs 201 vs 222.5 bp).
- Derivatives suit small, temporary rebalances (24 vs 30 bp); cash suits large permanent ones (60 vs 82 bp).
- In a manager search, conflicts are handled by disclosure and recusal; verify performance against third-party data.
- Under an ESG integration policy, engage and vote first; divest last.

## Connects To
- **ch04**: endowment model, spending rules and IPS constraints that this case applies.
- **ch06**: another case study; risk analysis of a household rather than an institution.
- **ch07**: unsmoothing, liquidity stress and ESG risks developed further for sovereign funds.
- **`cfa-alternative-investments` ch06**: asset allocation to alternatives, illiquidity premium and private-market risk.
- **`cfa-derivatives` ch06**: futures, swaps and overlays used for TAA and rebalancing.
- **`cfa-asset-allocation-cme` ch08**: real-world constraints (liquidity, spending) in strategic allocation.
- **`cfa-portfolio-management` ch19**: manager selection and monitoring.
- **`cfa-ethics-gips`**: Standards I, III, IV, V, VI, VII and the GIPS benchmark and fee rules.
