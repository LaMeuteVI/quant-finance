# Chapter 4: Active Equity Investing: Portfolio Construction
> **Source**: CFA Program Curriculum 2023, Level III, Reading 18 · Portfolio Management | Jacques Lussier, PhD, CFA, and Marc R. Reinganum, PhD

## Core Idea
Active return has three sources (exposure to rewarded factors that differs from the benchmark, true alpha skill such as timing and mispricing, and idiosyncratic luck), and portfolio construction is the art of combining four building blocks (factor weightings, alpha skills, position sizing, breadth of expertise) so that those insights survive risk, cost and capacity limits. Active Share (how different the holdings are) and active risk (how different the returns are) are distinct: factor-diversified products can have high Active Share and low tracking error, while closet indexers have both low. Risk should be budgeted only where the manager has skill.

## Learning Outcomes Covered
- describe the elements of investment philosophy that shape portfolio construction
- discuss approaches (systematic vs discretionary, bottom-up vs top-down, benchmark-aware vs agnostic)
- distinguish Active Share from active risk and relate each to strategy
- apply risk budgeting; use absolute and relative, heuristic and formal (VaR, CVaR, drawdown) risk measures
- explain how AUM, position size, liquidity and turnover affect construction (implicit costs, slippage, capacity)
- evaluate the efficiency of a portfolio structure for its mandate
- compare long-only, long extension (130/30), long/short and equitized market-neutral approaches

## Frameworks Introduced
- **Active return decomposition (Equations 1 and 2)**: `R_A = Σ ΔWᵢRᵢ = Σ(β_pk − β_bk)F_k + (α + ε)`.
  - When to use: diagnosing where a manager's excess return came from; checking claimed style.
  - How: (1) regress portfolio and benchmark excess returns on rewarded factors (Market, Size, Value, Momentum, often BAB and Quality); (2) multiply each active exposure by the factor's return; (3) the residual is α + ε (skill plus luck plus model misspecification); (4) examine R² (unexplained share of variance).
  - Failure mode: alpha vs luck cannot be separated with few observations; a missing factor shows up as fake alpha; factor exposures can drift (use sub-periods).
- **Four building blocks**: (1) over/underweight rewarded factors, (2) alpha skills (factor timing, unrewarded-factor timing such as sectors/oil/themes, security selection, finding new factors), (3) position sizing (conviction vs idiosyncratic risk), (4) breadth of expertise (number of independent decisions).
- **Full fundamental law of active management**: `E(R_A) = IC × √BR × σ_RA × TC`.
  - Use when: judging whether an excess-return target is plausible given skill, breadth, constraints.
  - How: IC = correlation of forecast and realized active returns; BR = independent decisions per year (not number of stocks); TC = how fully insights become weights (long-only constrained ~0.25-0.6, unconstrained 1); σ_RA = active risk. Solve for the missing input.
  - Failure mode: decisions are rarely independent (100 low-P/B stocks is ~1 decision); IC may fall as the portfolio widens.
- **Two-by-two approach map (Exhibit 6)**: systematic vs discretionary, bottom-up vs top-down. Systematic bottom-up: balanced rewarded factors, no factor timing, diversified. Discretionary top-down: macro factors, factor timing, diversified or concentrated. Systematic top-down: rare. Factor timing mostly discretionary and top-down.
- **Active Share vs active risk quadrant (Exhibit 7)**:

| | Low active risk | High active risk |
|---|---|---|
| **High Active Share** | Diversified multi-factor / factor-neutral diversified stock picks (AS ~0.7, TE ~2-3%) | Concentrated stock picker (AS > 0.9, TE 8-12%+), concentrated factor bets, sector rotator |
| **Low Active Share** | Pure index (AS 0, TE 0); closet indexer (AS ~0.25, TE < 2%) | Rare (few active weights but large factor/sector bets) |

- **Risk budgeting (four steps)**: choose absolute vs relative risk measure suited to the mandate; understand what drives risk (factors, sectors, securities, timing); set the total budget (policy decision); allocate it across positions/factors only where the manager has skill and diversify the rest.
- **Optimization framing**: objective function (maximize Sharpe ratio if absolute, information ratio if relative, or maximize a factor score, or minimize risk) plus constraints (security, sector, active risk, volatility, weighted-average cap, turnover). Heuristic weighting alternatives: score-proportional, rank-proportional (5/15 = 33% for best of five), top-x% then equal/risk weight.
- **Heuristic vs formal constraints**: heuristic = position, sector, factor, currency, leverage, illiquidity, turnover, carbon limits (bottom-up, outcome risk is a result); formal = volatility, TE, skewness, drawdown, VaR, CVaR, IVaR, MVaR (forward-looking, need risk models).
- **Well-constructed portfolio test**: clear philosophy and consistent process; promised risk/structure; risk-efficient delivery; reasonably low costs. Between two products with equal risk and cost, prefer the one with higher Active Share and lower unexplained risk.

## Key Concepts
- **Active weight (ΔW)**: portfolio weight minus benchmark weight; the source of all active return.
- **Rewarded vs unrewarded risk factors**: Market, Size, Value, Momentum (plus liquidity, low beta, quality) earn long-run premia; sector, region, oil price do not (timing them is alpha, not beta).
- **Alternative beta**: return historically labelled alpha that is really factor exposure obtainable cheaply; raises the fee bar for active managers.
- **Active Share**: ½ Σ |w_p − w_b|; 0 = benchmark, 1 = no overlap; fully controlled by the manager; ignores correlations; depends on the chosen benchmark (about +12% if S&P 500 mandate measured vs Russell 1000).
- **Active risk / tracking error**: σ of active returns; realized (historical) vs predicted (forward, needs variance-covariance estimates, EWMA or GARCH).
- **Closet indexer**: advertised active but with low Active Share and active risk.
- **Idiosyncratic risk**: security-specific risk; falls with number of holdings and lower stock volatility; also falls with lower average cross-correlation.
- **Transfer coefficient (TC)**: correlation between intended and actual active weights; reduced by long-only, size and liquidity constraints.
- **Risk contribution (CV, CAV)**: weight × covariance with the portfolio (absolute) or active weight × covariance of relative returns (relative).
- **Gross exposure / net exposure**: longs + |shorts| / longs − |shorts|. **Dollar neutral ≠ market neutral** (beta-matched).
- **130/30 (long extension)**: 130% long, 30% short, net 100%, gross 160%; the shorts fund the extra longs; lets underweights exceed benchmark weights.
- **Equitized market neutral**: market-neutral long/short overlaid on index exposure (futures/ETFs) to recover equity beta.
- **Slippage**: execution price vs bid-ask midpoint at order entry; includes market impact and volatility/trend cost.
- **Capacity**: AUM at which position and liquidity constraints change the strategy; small caps and short-term reversal degrade fastest, value scales best.
- **Short squeeze**: forced buy-in cascade after a sharp price rise and margin calls.
- **Weighted-average capitalization, minimum/maximum position sizes**: typical heuristic constraints.

## Formulas & Reference Tables
`R_A = Σ ΔWᵢ Rᵢ`  with ΔWᵢ = W_Pi − W_Bi
`R_A = Σₖ (β_pk − β_bk) F_k + (α + ε)`
`Active risk σ_RA = √[ Σ (R_At − mean R_A)² / (T − 1) ]` (tracking error)
`Active variance AV_p = ΣᵢΣⱼ (xᵢ − bᵢ)(xⱼ − bⱼ) RCᵢⱼ`; `CAVᵢ = (xᵢ − bᵢ) RCᵢp`
`σ²_RA = Var(Σ (β_pk − β_bk)F_k) + σ²_ε`  (factor part + idiosyncratic part)
`Active Share = ½ Σᵢ |w_p,i − w_b,i|` (sum over every security in portfolio or benchmark)
`E(R_A) = IC × √BR × σ_RA × TC`
`Information ratio = active return / active risk`; `Sharpe ratio = (R − R_f)/σ`
`Portfolio variance V_p = ΣᵢΣⱼ xᵢ xⱼ Cᵢⱼ`; `CVᵢ = xᵢ Cᵢp`; % contribution = CVᵢ / V_p
`Var(R_p) = Var(Σ β_pk F_k) + Var(ε_p)`; share explained = R²
`Equal-weight diversification: σ_p = √[σ²/n + (1 − 1/n) C σ²]` with C average correlation (0.24 for Russell 1000 since 1979)
`Geometric return ≈ R_a − σ²/2`; levered by L: `L·R_a − (Lσ)²/2 − (L−1)×funding cost`
`Position limit from liquidity = ADV% limit × ADV`; `ADV ≈ turnover% × market cap`
`Heuristic position cap examples: min(5 × benchmark weight, 2%); min(10 × benchmark weight, benchmark weight + 1%)`

| Exhibit values (source) | Figures |
|---|---|
| Russell 1000 factor exposures (1990-2016) | Market 0.99, Size −0.16, Value 0.02, Momentum −0.01, alpha +0.05%/mo, R² 0.99 |
| Russell 1000 Value | Market 0.92, Size −0.23, Value 0.41, Mom 0.13, alpha −0.05%, R² 0.95 |
| Mid-cap value fund (gross of fees) | Market 0.90, Size 0.13, Value 0.59, Mom 0.09, alpha −0.35%/mo, R² 0.74 |
| Factor monthly returns | Market 0.64%, Size 0.16%, Value 0.18%, Momentum 0.61% |
| Typical profiles | Multi-factor product: 250+ names, AS ~0.70, TE ~±3%; concentrated stock picker: ~100 names or fewer, AS > 0.90, TE 8-12%+; closet indexer AS ~0.25, TE < 2% |
| Funds (Petajisto 2009) | Vanguard index 0/0%; RiverSource 0.54/4.4%; T. Rowe Mid-Cap Value 0.93/5.4%; AIM Constellation 0.66/9.7%; GMO Quality 0.65/12.9%; Sequoia 0.97/14.1% |
| Portfolio volatility vs holdings (avg corr 0.24) | 25% stock vol: 14.1% (10 names), 12.9% (30), 12.6% (50), 12.4% (100), 12.3% (500); 30% stock vol: 16.9, 15.5, 15.2, 14.9, 14.7 |
| Long/short structures (% of capital) | Long-only 100/0 gross 100 net 100; 130/30 gross 160 net 100; market neutral 50/50 gross 100 net 0 (or 100/100 gross 200); directional low-risk 80/40 gross 120 net 40; net short 40/100 gross 140 net −60 |
| Hedge-fund style targets | Gross 150-200%, net 0-60% |
| Fees (2016) | Active extension 0.5-1.5%; market-neutral/directional 1-2% + 20% performance |
| Collateral | 20% short may need 40% of short value; 100% short may need 200% |

## Mental Models
- **Where is my skill?** Take risk only where you can forecast (timing factors, sectors, securities) and diversify or neutralize the rest; a multi-factor manager balances factors, a sector rotator times sectors, a stock picker accepts idiosyncratic risk.
- **Independent decisions, not holdings**: breadth is the count of uncorrelated bets; a 100-stock single-factor value book has far fewer than 100.
- **Absolute and relative risk behave differently**: adding a low-volatility asset (cash) lowers absolute risk but can raise active risk if the benchmark is equity; adding a high-vol asset correlated with the benchmark can lower active risk.
- **Active Share per fee dollar**: with equal fees, AS 0.80 buys twice the "active" management of AS 0.40; but AS alone says nothing about the risk taken.
- **Leverage has a ceiling**: compounded return peaks near L = R_a/σ² (here 2.5x for 10% / 20%); beyond it volatility drag destroys return, and funding costs shift the peak left.
- **Capacity shrinks idiosyncratic strategies**: large AUM forces more names, larger caps, slower turnover, and alpha decays (Lynch's Magellan: ~2%/month alpha at ~USD 40m to 0.2% at ~USD 10bn).
- **Shorts complete the factor**: Size, Value, Momentum are long/short factors; long-only investors only harvest half; long/short balances risk and raises the transfer coefficient but adds borrow, collateral and recall risk.

## Worked Example
**1. Active return decomposition (verified).** Mid-cap Value Fund vs Russell 1000 (Exhibits 2-3). Active exposures: Market 0.90 − 0.99 = −0.09; Size 0.13 − (−0.16) = +0.29; Value 0.59 − 0.02 = +0.57; Momentum 0.09 − (−0.01) = +0.10. Times factor returns (0.64%, 0.16%, 0.18%, 0.61%) gives −0.058% + 0.046% + 0.103% + 0.061% = +0.152% per month from factor tilts. Alpha difference = −0.35% − 0.05% = −0.40%. Total ≈ −0.25% per month (reported excess 0.40% − 0.64% = −0.24%, difference from rounding). Interpretation: the Value tilt paid, but a large negative alpha (and high unexplained risk, R² 0.74) wiped it out: investigate.
**2. Active Share (illustrative, verified).** Benchmark weights 20/15/15/10/10/15/15; portfolio 30/25/20/15/10/0/0 (two names not held). Σ|Δw| = 10+10+5+5+0+15+15 = 60; Active Share = 30%, which is closet-indexer territory despite 5 positions.
**3. Fundamental law (verified).** IC 0.2, σ_RA 4%, TC 0.6: 20 independent decisions give 0.2 × √20 × 4% × 0.6 = 2.15%; 40 give 3.04%. To match 2.15% with IC 0.1 needs BR = 80; a 20-decision manager needs IC 0.28 to match 3.04%. ⚠ Correction: the source's stand-alone example (IC 0.10, TC 0.25, σ 6%, one decision gives 15 bp) says about 40 decisions give 1%; exact BR = (1%/0.15%)² = 44.
**4. Risk contribution (verified).** Weights 40/50/10, vols 20%/12%/6%, correlations AB 0.4, AC 0.2, BC 0.2: variance 0.014212 (σ 11.92%); contributions A 59.2%, B 39.3%, C 1.4%. A 40% weight causes 59% of risk. Same math applies to sectors or factors.
**5. Leverage (verified).** Asset R_a 10%, σ 20%: unlevered compound 8%; 2x gives 12%; 3x also 12% (no gain); with 2% funding cost 3x gives 8%.
**6. Capacity.** Smallest stock cap USD 2bn, 1% trades daily (USD 20m); rule max 10% of ADV and 2% of assets: USD 200m fund limited by ADV to USD 2m (1%); a USD 1bn fund still USD 2m. A USD 5bn fund at 2% needs USD 100m positions, but only ~35% of the Russell 1000 trade that much daily.

## Anti-patterns
- **Using Active Share alone** to describe risk: high AS with low TE (diversified factor funds) and low AS with high TE can both exist.
- **Calling factor beta "alpha"**: pay alpha fees only for return beyond rewarded-factor exposure.
- **Counting stocks as decisions**: overstates breadth and confidence.
- **Choosing the wrong benchmark for Active Share** (S&P 500 mandate vs Russell 1000 inflates AS).
- **Scaling active risk without relaxing constraints**: long-only, short, leverage, liquidity and position limits cut the transfer coefficient so the information ratio falls as risk rises.
- **Ignoring tail and leverage risk (2008 examples)**: a 2x levered "AAA" mortgage book and a synthetic index position (commercial paper + equity swap) both suffered forced liquidations just before prices recovered.
- **Tight constraints in calm markets**: sector limits OK in normal volatility can produce large active losses in sector-specific volatility spikes (energy 2014-15, tech 2000-02); tighten in stress.
- **Dollar neutral = market neutral**: long and short books can have different betas, factor loadings, and drivers.
- **Letting AUM drift the strategy**: alpha decays and style changes unannounced; close the fund or disclose.
- **Heuristic weighting instead of optimization without checking efficiency**: score/rank weighting may allocate active risk inefficiently.

## Exam Focus & Traps
- Active return formula: ΔW × R summed; decomposition into β differences × factor returns + α + ε. Market factor is long-only; other factors are long/short, so a market-cap benchmark has Market β ≈ 1 and zero net other factors (but a large-cap index has negative Size exposure).
- Active Share = ½ Σ|Δw|, between 0 and 1, can be controlled fully; active risk cannot. Two managers at the same Active Share can have very different active risk (sector vs security bets; banks vs banks lower than banks vs tech).
- Concentrated stock picker: AS > 0.9, TE high, large unexplained risk; multi-factor: AS ~0.7, TE ~3%, 250+ names, factor-diversified; sector rotator: high TE, sector-driven risk; closet indexer: low targeted TE, narrow sector deviation limits, small single-security risk limits.
- Systematic: factor balance, no timing, rules, optimizer, diversified; discretionary: depth, may time factors, concentrated; top-down alpha mostly from factor timing; bottom-up alpha mostly security selection.
- Risk measure choice: long/short or absolute-return manager benchmarked to cash plus uses absolute risk (volatility, drawdown); long-only index-relative uses active risk. Sharpe ratio objective for absolute, information ratio for relative.
- Adding cash: lowers absolute risk, raises active risk. Low-vol / min-variance objectives produce Market β < 1 with Value and low-beta (BAB) tilts.
- VaR is a minimum loss at a probability; CVaR is the average loss beyond VaR (expected shortfall, not strictly a VaR); IVaR = change in VaR from adding a position; MVaR = effect of an infinitesimal change.
- Fundamental law: BR = independent decisions; TC = 1 if unconstrained; increase in IC, BR, TC or σ raises E(R_A) (BR via square root).
- Smaller AUM: higher explicit costs, lower implicit costs, can sustain higher turnover; slippage is greater for small caps and in volatile markets; commissions < slippage.
- 130/30: net exposure 100%, gross 160%; benefit is more symmetric expression of views and a better transfer coefficient; not riskless leverage. Long/short as a long-only replacement has higher fees and complexity.
- Collateral and recall risk apply to the short book; unlimited loss on shorts in theory; naked shorting restricted.
- Market-neutral strategies' limits: hard to keep beta at zero, limited bull-market upside unless equitized.

## Key Takeaways
1. Decompose active return into factor tilts, alpha and luck before paying for it; factor-explained excess return is alternative beta.
2. Match structure to claimed skill: factor skill gives many small positions; stock-picking skill gives concentration and idiosyncratic risk; timing skill gives macro/sector exposure.
3. Use Active Share and active risk together: AS is simple arithmetic and fully controlled; TE depends on correlations and factor exposures.
4. Budget absolute risk for absolute-return mandates and active risk for benchmark-relative ones; allocate the budget to skill-linked risks only.
5. Back constraints and objective functions by the manager's philosophy; heuristic limits are guard rails against overconfidence, but monitor for breaches as prices move.
6. Account for AUM, liquidity, slippage and turnover; a strategy that cannot be implemented at scale is a different product.
7. Long/short, 130/30 and market-neutral relax the long-only constraint (higher TC, better factor and risk balance) at the price of fees, borrow, collateral, operational and leverage risk.
8. Judge a portfolio as well constructed if it delivers promised risk characteristics efficiently at low cost, and fits the client's total portfolio.

## Connects To
- **ch 01**: costs, income and the passive-active spectrum.
- **ch 02**: passive/factor core and tracking-error mechanics used when building core-satellite portfolios.
- **ch 03**: strategies (fundamental, quantitative, factor, activist) whose signals this chapter turns into weights.
- **`cfa-portfolio-management` ch 12**: multifactor models and factor risk attribution; **ch 15**: fundamental law, information ratio, transfer coefficient; **ch 13**: VaR, CVaR; **ch 16**: trading costs and slippage; **ch 17**: trade execution; **ch 19**: manager selection.
- **`cfa-asset-allocation-cme` ch 07**: risk budgeting in asset allocation.
- **`cfa-alternative-investments` ch 05**: long/short equity and market-neutral hedge funds.
- **`cfasi-equity-investment-styles` ch 06-12**: factor and systematic investing practice.
