# Patterns — CFA Portfolio Management

## Margin Return and Call Price
**When to use**: leveraged purchase or short sale. **How**: equity = P₀N/L; loan = P₀N − equity; P&L = ΔP·N + dividends − loan × rate − commissions; return = P&L / (equity + purchase commission). Long call price P* = P₀(1−e)/(1−m); short P* = P₀(1+e)/(1+m). **Trade-offs**: L × asset return overstates results (interest, fees); losses exceed the multiple. (ch 01)

## Index Return by Weighting Rule
**When to use**: computing or auditing any index. **How**: beginning-period weights (price Pᵢ/ΣP; equal 1/N; cap QᵢPᵢ/ΣQP; float fQP; fundamental Fᵢ/ΣF); PR = Σw·PRᵢ, TR adds income; after a split D_new = ΣP_after/V_before. **Trade-offs**: cap = momentum, equal/fundamental = contrarian with turnover. (ch 02)

## Anomaly Triage
**When to use**: before trading a published anomaly. **How**: (1) persistent out of sample? (2) survives a multifactor risk adjustment? (3) survives costs? (4) economic rationale or data mining? (5) joint hypothesis: model and efficiency tested together. **Trade-offs**: most anomalies fail 2 or 3. (ch 03, 14)

## Return-Measure Selector
**When to use**: before quoting any return. **How**: one period → HPR; compounding → geometric; forecast → arithmetic; manager skill → TWR (value at each flow, link); investor experience or PE → MWR (IRR); annualize (1+r)^c − 1; gross for skill, net/after-tax/real for the client; tax first, then inflation. **Trade-offs**: MWR < TWR when cash was added before a weak stretch. (ch 05)

## Two-Asset and N-Asset Risk
**When to use**: portfolio σ. **How**: σp² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂; equal weight N: σ²/N + (N−1)/N · avg Cov; ρ = −1 zero risk at w₁ = σ₂/(σ₁+σ₂). **Trade-offs**: correlation, not count, sets the floor; correlations rise in crises. (ch 04, 05)

## Optimal Portfolio with a Risk-Free Asset
**When to use**: choosing one client's mix. **How**: (1) tangency (max Sharpe) risky portfolio P; (2) y* = [E(Rp) − Rf]/(Aσp²) in P, rest in Rf (y* > 1 = borrow); U = E − ½Aσ². **Trade-offs**: borrowing rate above Rf kinks the CAL. (ch 05, 06)

## Add-an-Asset Test
**When to use**: new holding in an existing portfolio. **How**: accept if Sharpe_new > ρ_new,p × Sharpe_p, equivalent to E(Rnew) > Rf + (σnew ρ/σp)(E(Rp) − Rf). **Trade-offs**: low or negative ρ lowers the hurdle; costs not included. (ch 05)

## CAPM Pricing and Security Selection
**When to use**: required return, mispricing, capital budgeting. **How**: β = Cov/σm² (or regression slope); E(R) = Rf + β[E(Rm) − Rf]; forecast above the SML = undervalued; active weight ∝ α/σ²ₑ, rank by α/σₑ; project NPV at the CAPM rate. **Trade-offs**: unstable beta, proxy-dependent, single factor. (ch 06)

## Performance Measure Chooser
**When to use**: ranking managers. **How**: whole portfolio of the client → Sharpe or M² (= Sharpe × σm + Rf); one sleeve of a diversified whole → Treynor or Jensen α; check positive excess return and β > 0 for ratios. **Trade-offs**: same data can flip the winner (Y vs Z). (ch 06)

## IPS Build (RRTTLLU)
**When to use**: new client or review. **How**: fact-find; risk objective (absolute and/or relative, VaR with a probability); take the lower of ability and willingness; return objective (inflate real target (1+π)ⁿ, solve r); five constraints; check consistency; attach SAA and rebalancing policy; review on schedule. **Trade-offs**: aggressive target forces counselling down. (ch 04, 07)

## TAA Contribution and Rebalancing Rule
**When to use**: measuring deviations from policy. **How**: Σ(w_start − w_policy) × R_period; drift wᵢ,end = wᵢ(1+Rᵢ)/(1+Rp); corridor or calendar trigger. **Trade-offs**: non-rebalancing is an unmeasured bet. (ch 07)

## Risk Management Loop
**When to use**: setting up or auditing risk governance. **How**: tolerance (inside view: failure points; outside view: risk drivers) → risk budget in factor terms → measure → compare → modify (avoid, self-insure, transfer, shift) → report. **Trade-offs**: self-insuring risk above tolerance is denial. (ch 08)

## Technical Chart Trade
**When to use**: timing a fundamentally chosen name. **How**: confirm prior trend; identify pattern; wait for 3-5% or multi-day breakout; target (H&S: neckline − (head − neckline); double top: valley − height; flag: pole); check volume; read oscillators with the trend. **Trade-offs**: lagging, default settings crowded. (ch 09)

## ML Validation Split
**When to use**: any data-driven model. **How**: clean; train/validate/test (for example 60/20/20); tune on validation; judge on untouched test; large train-validation gap = overfit. **Trade-offs**: little data or regime change favours simple models. (ch 10, 14)

## ETF Selection by Horizon
**When to use**: choosing an ETF. **How**: cost = 2c + s + (months/12) × fee; short horizon → deepest volume, tightest spread; long → lowest fee and rolling tracking difference (≈ −fee); check premium/discount and structure (ETN, swap, leveraged daily reset). **Trade-offs**: thin cheap ETFs cost more to trade. (ch 11)

## APT Arbitrage Test
**When to use**: mispricing among diversified portfolios. **How**: solve λ and RF from K+1 portfolios; model price for new portfolio; replicate its betas with a mix; buy the higher-return side, short the other: zero investment, zero beta, positive payoff. **Trade-offs**: factor choice may be wrong. (ch 12)

## Active Return and Risk Attribution (Factor)
**When to use**: factor bet versus stock pick. **How**: Σ(b_p,k − b_B,k) × F_k + selection = active return; active factor risk = Σⱼₖ bⱼᵃbₖᵃcov; add active specific risk Σ(wᵃ)²σ²ε; variances add, then √. **Trade-offs**: one strong factor year looks like skill. (ch 12)

## VaR Calculation and Choice of Method
**When to use**: loss threshold. **How**: parametric VaR = −(μ − zσ) × V with daily μ = annual/250, σ = annual/√250 (z 1.65, 2.33); historical = sorted P&L percentile; Monte Carlo for options and fat tails; add CVaR, IVaR, stress tests with full repricing. **Trade-offs**: never scale daily VaR by √T; calm window understates. (ch 13)

## Rolling-Window Backtest
**When to use**: testing a rule. **How**: write hypothesis, universe, costs, dates; point-in-time data with realistic lags; in-sample formation then out-of-sample test at every layer; report Sharpe, drawdown, CVaR, skew, kurtosis; t > 3, cross-validate across markets; bootstrap and Monte Carlo as complements. **Trade-offs**: one historical path. (ch 14)

## Fundamental-Law Sizing
**When to use**: choosing active risk. **How**: IR = TC·IC·√BR; σ_A* = TC × (IR/SR_B) × σ_B; SR_P² = SR_B² + (TC·IR)²; benchmark weight = 1 − σ_A*/σ_A(fund); Grinold μ = IC·σ·S. **Trade-offs**: correlated bets and uncertain IC shrink realized IR. (ch 15)

## Trading Cost Measurement
**When to use**: reviewing execution. **How**: effective spread for single fills; VWAP cost for interval comparison (blind when you are the market); IS including unfilled shares. **Trade-offs**: horizon and fill assumptions move IS. (ch 16)

## Implementation Shortfall Decomposition
**When to use**: post-trade analysis. **How**: delay Σsⱼ(P0 − Pd); trading Σsⱼ(pⱼ − P0); opportunity (S − Σsⱼ)(Pn − Pd); fees; bps = IS/(S·Pd) × 10⁴; market-adjusted = arrival cost − β × index cost; added value vs pre-trade estimate. **Trade-offs**: unrounded averages. (ch 17)

## Trade Strategy Selection
**When to use**: each ticket. **How**: motivation → urgency; four inputs (order % ADV, security, market conditions, risk aversion); benchmark; algorithm (POV/VWAP ≤ 5-10% of volume, arrival price for urgent liquid, TWAP for completion, liquidity seeking or dark for large, SOR for small); venue by asset class. **Trade-offs**: speed buys impact, patience buys risk. (ch 17)

## Brinson Attribution
**When to use**: top-down managers. **How**: BF allocation (wᵢ−Wᵢ)(Bᵢ−B); selection Wᵢ(Rᵢ−Bᵢ); interaction (wᵢ−Wᵢ)(Rᵢ−Bᵢ); check sum = R − B; macro version at asset-owner level. **Trade-offs**: wrong hierarchy misleads; arithmetic needs smoothing across periods. (ch 18)

## Benchmark and Skill Appraisal
**When to use**: judging a manager. **How**: seven Bailey-Tierney tests; P = M + S + A and corr tests; Sortino, appraisal ratio α/σₑ, capture ratios, max drawdown; several ratios must agree over a long record. **Trade-offs**: peer groups suffer survivorship. (ch 18)

## Manager Search and Fee Check
**When to use**: hire, retain, fire. **How**: universe by role and risk (not returns); quantitative record; investment and operational DD; Type I/II audit including rejected and fired managers; vehicle choice; fee = base + s × performance with floor, cap, HWM; judge net of fees. **Trade-offs**: Type I error is visible, Type II invisible. (ch 19)
