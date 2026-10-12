# Chapter 15: Analysis of Active Portfolio Management
> **Source**: CFA Program Curriculum 2022, Level II, Reading 43 · Portfolio Management | Roger G. Clarke, Harindra de Silva, Steven Thorley

## Core Idea
Active management value is the correlation between the bets a manager takes (active weights vs. benchmark) and what the securities then deliver (realized active returns). The fundamental law of active management decomposes the expected information ratio into skill (IC), portfolio construction efficiency (TC) and number of independent bets (breadth): `IR ≈ TC · IC · √BR`. Use it to size active risk, to compare strategies (stock picking vs. market timing), and to see why constraints and low breadth destroy most of the theoretical alpha.

## Learning Outcomes Covered
- Describe how value added by active management is measured (active return, active weights, attribution)
- Calculate and interpret the information ratio (ex ante and ex post) and contrast it with the Sharpe ratio
- Describe and interpret the fundamental law: transfer coefficient, information coefficient, breadth, active risk (aggressiveness)
- Explain how IR helps in manager selection and in choosing the level of active risk
- Compare active strategies (market timing vs. security selection) and evaluate strategy changes with the law
- Describe practical strengths and limitations of the fundamental law

## Frameworks Introduced
- **Value added via active weights**: `R_A = R_P − R_B = Σ Δwᵢ · Rᵢ = Σ Δwᵢ · R_Aᵢ` with `Δwᵢ = w_P,i − w_B,i`, `ΣΔwᵢ = 0`, `R_Aᵢ = Rᵢ − R_B`.
  - When to use: decompose any outperformance by position; positive value added if and only if realized active returns are positively correlated with active weights.
  - How: (1) list active weights, (2) compute each asset's return relative to the benchmark return, (3) multiply and sum.
  - Failure mode: "alpha" is often used loosely for active return, which implicitly assumes β = 1 vs. the benchmark (strict alpha = `R_P − β_P·R_B`).
- **Two-level attribution (asset allocation vs. security selection)**: `R_A = Σ Δw_j · R_B,j + Σ w_P,j · R_A,j` (Eq. 4), where j indexes asset classes, Δw_j is the deviation from the policy weight, and R_A,j is the active return inside asset class j.
  - When to use: decompose a multi-asset portfolio of active funds.
  - How: allocation effect = active class weights × benchmark class returns; selection effect = **actual** class weights × within-class active returns (the interaction term is arbitrarily assigned to selection).
- **Information ratio vs. Sharpe ratio**: `SR = (R_P − R_F)/σ_P` (absolute); `IR = (R_P − R_B)/σ(R_P − R_B) = R_A/σ_A` (relative to benchmark).
  - When to use: SR to rank total portfolios or asset classes; IR to evaluate active managers and decide how much active risk to run.
  - Key properties: SR is unchanged by cash or leverage (two-fund separation). IR is unchanged by scaling active weights by a constant (unconstrained), but shrinks when cash is added to the portfolio.
- **Optimal active risk and Sharpe improvement** (benchmark-plus-active combination):
  - `SR_P² = SR_B² + IR²` (Eq. 7)
  - `σ_A* = (IR / SR_B) · σ_B` (Eq. 8)
  - How: with a manager of given IR, set active risk to σ_A* by mixing the manager with the benchmark (or shorting the benchmark to scale up). Benchmark weight needed = `1 − σ_A*/σ_A(manager)` (negative means short benchmark / leverage the active fund).
  - Failure mode: IR → 0 implies σ_A* → 0, i.e., hold the benchmark. Negative IR is lost when squaring, so Eq. 7 cannot rank negative-IR managers.
- **Correlation triangle**: forecasts μᵢ ↔ realized active returns R_Aᵢ = **IC** (signal quality); forecasts μᵢ ↔ active weights Δwᵢ = **TC** (portfolio construction); active weights ↔ realized active returns = value added.
- **Grinold rule**: `μᵢ = IC · σᵢ · Sᵢ`, with Sᵢ the standardized score (cross-sectional mean 0, standard deviation 1), σᵢ the active volatility of asset i.
  - Optimal unconstrained active weights (uncorrelated active returns): `Δwᵢ* = (μᵢ/σᵢ²) · σ_A/(IC·√BR)` (Eq. 11).
- **Fundamental law of active management**:
  - Basic (unconstrained): `E(R_A)* = IC · √BR · σ_A`, `IR* = IC · √BR`.
  - Expanded (constrained): `E(R_A) = TC · IC · √BR · σ_A`, `IR = TC · IC · √BR`.
  - Ex post: `E(R_A | IC_R) = TC · IC_R · √BR · σ_A`; `R_A = E(R_A | IC_R) + noise`.
  - Why it works: mean-variance optimization gives weights proportional to risk-adjusted forecasts; value added is then the product of forecast quality, number of independent bets, and risk taken. Failure mode: all four inputs are estimated with error and rest on independence assumptions (see Limitations).

## Key Concepts
- **Active return (value added)**: portfolio return minus benchmark return, `R_A = R_P − R_B`; positive or negative after the fact, expected positive before the fact.
- **Active weight**: portfolio weight minus benchmark weight; active weights sum to zero and drive all value added.
- **Active risk (tracking risk, tracking error, aggressiveness)**: standard deviation of active return, σ_A; "residual risk" when beta-adjusted.
- **Benchmark qualities**: representative of the investable universe, replicable at low cost, weights verifiable ex ante and returns timely ex post.
- **Zero-sum property**: versus a float-adjusted cap-weighted index covering the whole market, active management is zero-sum before costs, so average realized IR across funds with the same benchmark is about zero (narrower benchmarks are not zero-sum).
- **Closet index fund**: advertises active management but holds near-benchmark weights; Sharpe ratio close to the benchmark's, tiny active risk, IR near zero or negative after fees.
- **Active share**: half the sum of absolute active weights, `½ Σ|Δwᵢ|` (Cremers and Petajisto); detects closet indexing from holdings.
- **Information coefficient (IC)**: ex ante risk-weighted correlation between forecast active returns μᵢ and realized active returns; typically small (below 0.20), must be positive to justify active management.
- **Transfer coefficient (TC)**: risk-weighted correlation between forecast active returns (or optimal active weights) and actual active weights; typically 0.20 to 0.90; 1.0 means no binding constraint, 0 means no value transfer.
- **Breadth (BR)**: number of independent active decisions per year; equals N only if active returns are cross-sectionally uncorrelated and decisions independent over time; can be non-integer, below N (correlated bets) or above N (near-arbitrage).
- **Realized IC (IC_R)**: ex post correlation between active weights' basis (forecasts) and realized active returns; may be negative.
- **Constraint-induced noise**: the part of realized active return unrelated to forecasting success, caused by constraints (long-only, turnover limits).
- **Two-fund separation**: all investors hold the max-Sharpe risky portfolio combined with cash/leverage.
- **Strategy risk (Qian and Hua)**: extra active risk from uncertainty in IC over time (σ_IC), which lowers realized IR.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Benchmark / portfolio return | `R_B = Σ w_B,i Rᵢ`; `R_P = Σ w_P,i Rᵢ` |
| Active return | `R_A = R_P − R_B = Σ Δwᵢ R_Aᵢ` |
| Strict alpha | `α_P = R_P − β_P R_B` |
| Sharpe ratio | `SR_P = (R_P − R_F)/σ_P`; annualize: mean × 12, σ × √12 (monthly data) |
| Cash/leverage invariance | `SR_C = (w σ_P SR_P)/(w σ_P) = SR_P` |
| Information ratio | `IR = R_A/σ_A`, `σ_A = σ(R_P − R_B)` |
| Scaling invariance | `IR(c·Δw) = c R_A/(c σ_A) = IR` |
| Total risk decomposition | `σ_P² = σ_B² + σ_A²` (β = 1) |
| Sharpe with active | `SR_P² = SR_B² + IR²` |
| Optimal active risk | `σ_A* = (IR/SR_B)·σ_B` (× β if β ≠ 1); constrained: `σ_A* = TC·(IR*/SR_B)·σ_B` |
| Constrained Sharpe at optimum | `SR_P² = SR_B² + (TC·IR*)²` |
| Optimality condition | `E(R_A)/σ_A² = [E(R_B) − R_F]/σ_B²` |
| Grinold rule | `μᵢ = IC · σᵢ · Sᵢ` |
| IC | `IC = ρ(R_Aᵢ/σᵢ, μᵢ/σᵢ)` (risk-weighted) |
| TC | `TC = ρ(μᵢ/σᵢ, Δwᵢσᵢ)` (single-factor model) |
| Basic law | `E(R_A)* = IC√BR σ_A`; `IR = IC√BR` |
| Expanded law | `E(R_A) = TC·IC·√BR·σ_A`; `IR = TC·IC·√BR` |
| Conditional on realized IC | `E(R_A | IC_R) = TC·IC_R·√BR·σ_A` |
| Variance split ex post | share from forecast skill = `TC²`; from noise = `1 − TC²` |
| Time-series IC (binary calls) | `IC = %correct − %incorrect = 2p − 1` |
| Breadth rule of thumb | `BR ≈ N/[1 + (N−1)ρ̄]`, ρ̄ = average active-return correlation |
| Strategy risk | `σ_A = σ_IC · √N · σ_RM`; `E(R_A) = IC/σ_IC · σ_A` (lowers IR) |
| Pair active risk | `σ_A = √(σ₁² + σ₂² − 2ρσ₁σ₂)` |
| Active share | `½ Σ|w_P,i − w_B,i|` |

Reference ranges: ex post long-term equity benchmark Sharpe 0.20 to 0.60; realized IR of funds typically within -0.30 to +0.30 over long periods; IC under 0.20; TC 0.20 to 0.90.

## Mental Models
- **Alpha = volatility × IC × score**: a forecast of relative rank only becomes a return forecast after scaling by the asset's own active volatility and by how good you really are.
- **IR is the "pure skill" ruler; aggressiveness is a dial.** Choose the manager by highest expected IR, then set active risk with `σ_A* = (IR/SR_B)σ_B` using benchmark mixing.
- **Skill is a pipeline with leaks**: forecasts (IC) leak into weights (TC), weights are multiplied by the number of independent bets (√BR). The weakest link dominates.
- **Breadth beats skill at the margin**: IC 0.05 on 100 independent bets (IR 0.50) rivals IC 0.15 on 9 bets (IR 0.45). Market timing has tiny breadth, so needs high accuracy.
- **Constraints tax aggressiveness**: unconstrained IR is flat in active risk; constrained IR slopes down as risk rises (TC falls), so a long-only manager should run less active risk than the unconstrained formula suggests.
- **Low TC means noisy results**: with TC = 0.6, only 36% of performance variance is explained by forecasting success; good forecasts can coexist with bad outcomes.

## Worked Example
**A. Optimal active risk and Sharpe uplift (all numbers recomputed).** Benchmark: expected excess return 6.4%, σ_B = 16.0%, SR_B = 0.40. Manager: IR = 0.30, active risk 8.0%.
1. σ_A* = (0.30/0.40) × 16.0% = 12.0%.
2. SR_P = √(0.40² + 0.30²) = 0.50.
3. Check: expected active return = 0.30 × 12.0% = 3.6%; total excess return = 6.4% + 3.6% = 10.0%; σ_P = √(16² + 12²) = 20.0%; SR = 10/20 = 0.50.
4. Implementation: hold 12.0/8.0 = 1.5× the active fund, short 0.5× the benchmark.
5. With constraints (TC = 0.50, IR* = 0.30, σ_B = 16%, SR_B = 0.40): σ_A* = 0.5 × 0.75 × 16 = 6.0%; SR = √(0.40² + 0.25 × 0.09) = 0.43 (0.427). A manager at 8% active risk should hold 25% benchmark, 75% fund.

**B. Fundamental law with constraints (four uncorrelated assets).** Score ±1, active vols 25%/50%/25%/50%, IC = 0.20, BR = 4, σ_A = 9.0%.
- Forecasts μ = IC·σ·S = +5, +10, −5, −10%. Optimal weights `μ/σ² · σ_A/(IC√BR)` = +18%, +9%, −18%, −9%.
- Unconstrained: E(R_A) = 0.18·5 + 0.09·10 + 0.18·5 + 0.09·10 = 3.6% = 0.20 × 2 × 9.0 (IR = 0.40).
- Constrained actual weights +6, +4, +7, −17: E(R_A) = 0.30 + 0.40 − 0.35 + 1.70 = 2.05% (source rounds to 2.1%); active risk still 9.0%; TC = correlation of (Δw·σ) with (μ/σ) = 0.577 (source: 0.58); law: 0.577 × 0.20 × 2 × 9.0 = 2.08%, matching within rounding. IR falls from 0.40 to ~0.23.

**C. Market timing vs. selection.** Credit timing quarterly (IG vs HY): active vol of the spread `√(2.84² + 4.64² − 2·0.575·2.84·4.64) = 3.80%` per quarter (7.60% annualized). With 55% hit rate IC = 0.10 and BR = 4: IR = 0.10 × 2 = 0.20; at σ_A = 2.0% E(R_A) = 40 bps/year; active weight = 2.0/7.6 = 26.3%. Monthly independent decisions give IR = 0.35 (BR = 12); daily would give 1.58 but is implausible, and at 4% active risk long-only constraints (TC ≈ 0.62) cut it to 0.98.

## Anti-patterns
- **Counting N securities as breadth**: correlated forecasts (same sector, same factor, slow-moving signals such as earnings yield) are not independent bets. Monthly stock picking on 500 names does not give BR = 6,000 (IR of 3.87 is a red flag).
- **Ignoring the transfer coefficient**: quoting `IC·√BR` for a long-only, turnover-limited portfolio overstates IR by 20%–80%.
- **Raising active risk without checking constraints**: for constrained funds IR drops as aggressiveness rises, so alpha does not scale linearly.
- **Using SR to judge an active manager and IR to judge a total portfolio**: wrong ruler for the question.
- **Comparing Sharpe ratios over different periods or ranking by IR with negative values via Eq. 7**: the sign is lost when squaring.
- **Using IC as a fixed known constant**: skill is uncertain and time-varying; strategy risk lowers realized IR to roughly 45%-91% of the law's prediction for stock selection.
- **Paying active fees for closet indexing**: very low active share and near-zero IR.

## Exam Focus & Traps
- **Sharpe vs. IR response to cash/leverage**: SR unchanged by cash or leverage; IR unchanged by scaling active weights but changed by adding cash. Market-neutral long-short funds: SR = IR when the benchmark is the risk-free rate.
- **Attribution formula**: selection term uses actual portfolio weights `w_P,j`; allocation term uses active weights times benchmark class returns. Check that total = portfolio return − policy return.
- **Basic vs. expanded law**: basic has no TC (TC = 1); the expanded form multiplies IR by TC. Optimal active risk with constraints also carries a TC factor.
- **Square-root scaling**: IR scales with √BR, not BR; doubling independent bets raises IR by 41%, not 100%.
- **Binary timing IC** = proportion correct minus proportion incorrect (55% right means IC = 0.10, not 0.55).
- **Variance attribution**: TC² share from forecast quality, 1 − TC² from noise.
- **Optimal weight to benchmark**: `1 − σ_A*/σ_A(fund)`; a result above 1 for the fund means shorting the benchmark.
- **Ex ante IC must be positive**; realized IC can be negative.
- **Zero-sum**: only for a benchmark covering the full float-adjusted market, before costs.
- **Rounding**: the source quotes TC = 0.58 in the four-asset example (exact 0.577) and active return 2.1% (exact 2.05%); answers within rounding are fine.

## Key Takeaways
1. Value added equals the sum of active weights times security returns relative to the benchmark; no active weights, no value added.
2. Judge managers by IR (active return ÷ tracking risk), and use SR for whole portfolios; combine an active fund with the benchmark so that `SR² = SR_B² + IR²`.
3. Set active risk at `σ_A* = (IR/SR_B)·σ_B` (times TC when constrained) and adjust it by mixing with the benchmark rather than by changing weights.
4. `IR = TC·IC·√BR`: improve skill, widen truly independent breadth, or relax constraints (long-short, lower turnover limits).
5. Market timing has low breadth (4 to 12 decisions a year) so needs high accuracy; cross-sectional stock selection wins through breadth.
6. Constraints cut the information ratio (long-only plus 10% caps cut IR from 0.49 to 0.34 in the global equity example, and to 0.28 at higher active risk).
7. With TC < 1, a share `1 − TC²` of performance variance is noise, so judge managers over long periods.
8. Haircut every law-based forecast for correlated bets, slow signals and uncertain IC before relying on it.

## Connects To
- **ch05–ch06**: Sharpe ratio, efficient frontier, CAPM, and mean-variance foundations used for SR and two-fund separation.
- **ch12**: multifactor models supply the risk model that defines residual (active) returns and breadth.
- **ch16**: trading costs and implementation shortfall are the practical drag on TC (turnover limits) that the fundamental law ignores.
- **ch18**: performance evaluation measures realized active return, attribution and risk-adjusted metrics ex post.
- **ch19**: manager selection uses IR, active share and skill assessment.
- **`cfa-equity-portfolio-management` ch04**: active equity portfolio construction (long-only vs. long-short, tracking-risk budgets, TC in practice).
- **`cfa-equity-portfolio-management` ch03**: active equity strategies whose IC and breadth the law evaluates.
