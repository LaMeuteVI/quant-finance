# Chapter 18: Portfolio Performance Evaluation
> **Source**: CFA Program Curriculum 2023, Level III, Reading 26 · Portfolio Management | Marc A. Wright, CFA (ed.)

## Core Idea
Performance evaluation answers three linked questions: what was the return (measurement), how was it earned (attribution), and was it skill or luck (appraisal). Attribution only has value if it mirrors the manager's actual decision process and reconciles to the reported return. Appraisal only has value if the benchmark is valid, and no single ratio proves skill: use several tools that agree, with a long enough record.

## Learning Outcomes Covered
- Explain measurement, attribution and appraisal and how they interrelate; describe attributes of an effective attribution process
- Contrast return vs risk attribution and macro vs micro attribution; contrast returns-, holdings- and transactions-based attribution
- Interpret equity attribution (BHB, Brinson-Fachler, factor-based) and fixed-income attribution output
- Choose a risk attribution approach; separate asset-owner results from manager results
- Describe liability-based and asset-based benchmarks, tests of benchmark quality, impact of misspecification, problems benchmarking alternatives
- Calculate and interpret Sortino ratio, appraisal ratio, capture ratios, maximum drawdown, drawdown duration; state limits of appraisal measures; evaluate manager skill

## Frameworks Introduced
- **Three components of performance evaluation**: measurement (what), attribution (how), appraisal (skill or luck).
  - When to use: structure any manager review. Measurement feeds attribution; attribution plus risk feed appraisal; appraisal feeds back into the investment process.
  - How: compute absolute and excess return and ex post risk; decompose; then rank managers on risk-adjusted measures and test consistency with the stated process.
- **Effective attribution criteria**: it must (1) account for all of the portfolio's return or risk, (2) reflect the investment decision process, (3) quantify the manager's active decisions, (4) fully explain excess return or risk.
  - Failure mode: a bottom-up stock picker with no sector view analysed by sector allocation. Sector "effects" are then a by-product, not a decision, and the output misleads.
- **Brinson-Hood-Beebower (BHB) and Brinson-Fachler (BF) attribution**: excess return `R − B` split into allocation, selection and interaction by sector `i`. BF differs from BHB only in how the sector allocation effect is computed (benchmark-relative).
  - When to use: top-down managers who choose sector/country/asset-class weights and then securities. BF is the industry default.
  - How: build sector weights and returns for portfolio (`wᵢ, Rᵢ`) and benchmark (`Wᵢ, Bᵢ`); apply the formulas below; sum over sectors; check the sum equals `R − B`.
  - Why BF is better: BHB rewards any overweight in a sector with positive return, even if it lagged the total benchmark. BF compares the sector with the total benchmark `B`, so the opportunity cost of the money is charged.
- **Factor-based (returns-based) attribution (Carhart)**: active return = Σ (active factor exposure × factor return) + residual selection.
  - When to use: factor-driven or quant managers, or when holdings are not available.
  - How: regress or estimate sensitivities for portfolio and benchmark, take differences, multiply by factor returns, sum to "factor tilts return", the remainder is "security selection". Then ask whether the biggest tilt is consistent with the stated process (skill) or not (luck).
- **Fixed-income attribution (three GRAP-style approaches)**: (1) exposure decomposition, duration based; (2) yield curve decomposition, duration based; (3) yield curve decomposition, full repricing. Candidates must interpret, not calculate.
- **Risk attribution selector** (Exhibit 9): match the approach to the process and the mandate.
- **Bailey-Tierney benchmark quality criteria** (seven): unambiguous, investable, measurable, appropriate, reflective of current investment opinions, specified in advance, accountable.
- **Return decomposition `P = M + S + A`** to test a benchmark and to size style vs active return.
- **Normal portfolio / misfit return**: `true active = P − normal`, `mismeasured active = P − investor benchmark = true active + misfit`.

## Key Concepts
- **Performance measurement**: computing portfolio and benchmark returns (absolute and excess) and risk.
- **Performance attribution**: explaining sources of excess return (return attribution) or of risk (risk attribution).
- **Performance appraisal**: judging skill vs luck using risk, return and attribution together.
- **Macro attribution**: effect of the asset owner's decisions (tactical deviation from strategic allocation, manager selection, implementation gaps).
- **Micro attribution**: effect of the portfolio manager's allocation and selection decisions on total fund results.
- **Returns-based attribution**: uses only portfolio returns; easiest, least accurate, most open to manipulation; the usual choice for hedge funds.
- **Holdings-based attribution**: uses beginning-of-period holdings; misses intra-period trades, so may not reconcile (residual = timing or trading effect); suits low-turnover or passive strategies; accuracy rises with higher-frequency data.
- **Transactions-based attribution**: uses holdings and every trade including costs; most accurate, reconciles to the client return, doubles as an error diagnostic, but is costly and data-hungry.
- **Arithmetic vs geometric attribution**: arithmetic effects add to `R − B` but need smoothing (Cariño, Menchero) to link multiple periods; geometric effects compound to the geometric excess return and need no smoothing. Arithmetic is the choice for non-specialist clients.
- **Allocation effect**: value from holding sector weights different from benchmark weights.
- **Selection effect**: value from different security returns inside a sector (BHB weights it by benchmark weight).
- **Interaction effect**: cross term of the active weight and the active return; often folded into selection.
- **Tracking risk (tracking error)**: standard deviation of `Rp − RB`; the denominator of the information ratio.
- **Minimum acceptable return (MAR)**: investor-specific hurdle used as the Sortino target.
- **Drawdown / drawdown duration**: peak-to-trough cumulative loss; time from the start of the drawdown to full recovery (drawdown phase plus recovery phase).
- **Normal portfolio**: the portfolio that best represents the manager's typical positions in the opportunity set.
- **PME (public market equivalent)**: replicates private-equity capital calls and distributions in a public index to compare IRR with public returns.

## Formulas & Reference Tables
Notation: `wᵢ, Rᵢ` portfolio weight and return in sector i; `Wᵢ, Bᵢ` benchmark weight and return; `R = Σwᵢ Rᵢ`; `B = Σ Wᵢ Bᵢ`; weights sum to 100% (negative weights allowed for leverage or shorts).

| Effect | BHB | Brinson-Fachler |
|---|---|---|
| Allocation Aᵢ | `(wᵢ − Wᵢ)·Bᵢ` | `(wᵢ − Wᵢ)·(Bᵢ − B)` |
| Selection Sᵢ | `Wᵢ·(Rᵢ − Bᵢ)` | same |
| Interaction Iᵢ | `(wᵢ − Wᵢ)·(Rᵢ − Bᵢ)` | same |
| Total | `ΣA + ΣS + ΣI = R − B` | same |

- Total allocation is identical in BHB and BF: `ΣAᵢ = Σwᵢ Bᵢ − B`, because `Σ(wᵢ − Wᵢ) = 0`.
- Selection plus interaction combined: `wᵢ(Rᵢ − Bᵢ)`.
- Geometric excess return: `G = (1 + R)/(1 + B) − 1 = (R − B)/(1 + B)`.
- Carhart four-factor: `Rp − Rf = αp + b₁·RMRF + b₂·SMB + b₃·HML + b₄·WML + εp`. RMRF is market minus T-bill, SMB small minus big, HML high minus low book-to-market, WML winners minus losers.
- Factor attribution: contribution of factor k = `(b_p,k − b_B,k) × factor return_k`; factor tilts total + selection = active return.
- General factor model: `Rp = αp + b₁F₁ + … + b_kF_k + εp`.
- Fixed income, duration based: `% total return = % income return + % price return`; `% price return ≈ −Duration × ΔYTM` (plus convexity). Yield-curve factors: shift (level), slope, curvature; plus spread and bond-specific spread; residual grows with large yield moves.
- Benchmark test decomposition: `P = B + A`; `P = M + S + A` with `S = B − M` (style), `A = P − B` (active), `E = P − M`. A good benchmark has `corr(A, S)` not statistically different from zero and a significantly positive `corr(S, E)`.
- Misfit: `P − B_investor = (P − Normal) + (Normal − B_investor)`.
- Sharpe `S_A = (R_A − r_f)/σ_A`. Treynor `T_A = (R_A − r_f)/β_A`. Information ratio `IR = E(Rp − RB)/σ(Rp − RB)`.
- Appraisal ratio (Treynor-Black): `AR = αp/σ_ε`, with σ_ε the standard deviation of regression residuals (a standard deviation, not a variance).
- Sortino: `SR_D = (R_p − r_T)/σ_D`; `σ_D = √[ Σ min(r_t − r_T, 0)² / N ]`. N counts all periods, not only the below-target ones.
- Upside capture `UC = R(m)/R(B)` when `R(B) ≥ 0`; downside capture `DC = R(m)/R(B)` when `R(B) < 0`, using geometric average returns in up and down periods. Capture ratio `CR = UC/DC`.
- Drawdown: `MaxDD = min[(V_t − V_peak)/V_peak, 0]`. Gain needed to recover a loss L: `L/(1 − L)` (10% → 11.1%, 20% → 25%, 30% → 42.9%, 50% → 100%, 60% → 150%).

Risk attribution selector (Exhibit 9):

| Decision process | Relative (vs benchmark) | Absolute |
|---|---|---|
| Bottom-up | Position's marginal contribution to tracking risk (times active weight) | Position's marginal contribution to total risk |
| Top-down | Attribute tracking risk to relative allocation and selection decisions | Factor's marginal contribution to total risk and to specific risk |
| Factor-based | Factor's marginal contribution to tracking risk and active specific risk | Factor's marginal contribution to total risk and to specific risk |

Attribution data choice:

| Approach | Data | Accuracy | Best for |
|---|---|---|---|
| Returns-based | Total returns | Lowest | Hedge funds, no holdings |
| Holdings-based | Start-of-period holdings | Medium (misses trades) | Low-turnover, passive |
| Transactions-based | Holdings + trades + costs | Highest, reconciles | Active, high-turnover, audit |

Fixed-income approaches:

| Approach | Method | Use | Trade-off |
|---|---|---|---|
| Exposure decomposition (duration-based) | Group by duration bucket and sector, Brinson-like | Marketing, client reports | Simple, easy to explain; less detail |
| Yield-curve decomposition (duration-based) | Return from income, roll, shift, slope, curvature, spread, specific, residual; run on portfolio and benchmark | Analysts and PMs | More transparency, more data |
| Yield-curve decomposition (full repricing) | Reprice each bond off spot curves | Quant and risk teams | Most precise, costly, hard for non-specialists |

Asset-based benchmark types: absolute/target return; broad market index; style index; factor-model-based; returns-based (Sharpe style analysis, weights non-negative and sum to 1); manager universe (peer group); custom security-based (strategy) benchmark.

## Mental Models
- Attribution answers "what did the manager decide?", not "what happened in the market?". If a decision is not in the process, drop it from the model (a country-allocation lens can flatter a manager, a sector lens can condemn the same manager).
- Use BF, not BHB, to judge over- and underweights: the sign of an allocation effect depends on whether the sector beat the total benchmark `B`, not on whether its own return is positive. Overweight a sector that lagged `B` and you lose, even if the sector rose.
- Active return is `style + active`: a broad index that ignores style lumps style into "skill" or "failure". Measure against the normal portfolio first.
- Risk attribution is the other half of return attribution: an allocation gain that came from a large tracking-risk bet is not equal to one earned cheaply.
- Prefer several weak, independent confirmations (attribution, IR, Treynor, Sortino, capture, process fit) to one strong statistic. Skill needs many years of data to confirm (paradox of skill: as the field gets better, luck explains more of the dispersion).
- Large drawdowns are stress tests of the process: look at how the manager and the firm reacted, not only the depth.

## Worked Example
Brinson attribution of a three-sector equity portfolio (Exhibit 2 data; recomputed in python).

| Sector | w | W | R | B |
|---|---|---|---|---|
| Energy | 50% | 50% | 18% | 10% |
| Health care | 30% | 20% | −3% | −2% |
| Financials | 20% | 30% | 10% | 12% |

Steps: `R = 10.1%`, `B = 8.2%`, excess `1.9%`.
- BHB allocation `(w − W)·B`: 0.0, −0.2, −1.2, total **−1.4%**.
- BF allocation `(w − W)(B − 8.2%)`: 0.0, −1.02, −0.38, total **−1.4%** (same total, different sector split).
- Selection `W(R − B)`: 4.0, −0.2, −0.6, total **+3.2%**.
- Interaction `(w − W)(R − B)`: 0.0, −0.1, +0.2, total **+0.1%**.
- Check: −1.4 + 3.2 + 0.1 = 1.9%. If you forget interaction you are 10 bps short, which is the classic reconciliation error.

Interpretation: all the value came from picking energy stocks (+4.0 points of the 3.2% total selection); the manager's sector weights cost 140 bps. Health care's BF effect (−1.02) is far worse than its BHB effect (−0.2) because the extra 10% was held in a sector 10.2 points below the total benchmark.

Sortino check (MAR 4%, ten annual returns 6, 8, −1, 18, 12, 3, −4, 5, 2, 11): squared shortfalls sum to 0.0094, `σ_D = √(0.0094/10) = 3.07%`, mean excess `6.0% − 4.0% = 2.0%`, Sortino = **0.65**.

Appraisal ratio check: portfolio return 9%, σ 20%, market 8%, σ 12%, beta 1.4, r_f 3%. `α = 9 − [3 + 1.4×5] = −1.0%`; residual variance `0.20² − 1.4²×0.12² = 0.011776`, so `σ_ε = 10.85%`; `AR = −0.01/0.1085 = −0.092`. Dividing by the variance (0.011776) gives −0.849, the trap answer.

Capture and drawdown: S&P 500 Jan 2011-Feb 2012 peaks in April 2011, falls to −16.26% in September, recovers fully in February 2012: 5 months down, 5 months recovery, 10 months in total.

## Anti-patterns
- **Using a sector-allocation model for a bottom-up stock picker** (or country model for a sector rotator): the "effects" are not decisions; the attribution does not reflect the process.
- **Using the wrong benchmark** (e.g., MSCI Pacific for a Japan-only manager, Russell 3000 for a value manager): the misfit return hides true skill or fakes it; any later attribution or appraisal is meaningless.
- **Changing the benchmark after poor results**: unethical and breaks the "specified in advance" test.
- **Treating factor-attribution "selection" as skill without checking the stated process**: a big HML tilt in a value year can be luck.
- **Reading BHB sector allocation signs against the sector's own return** instead of the total benchmark.
- **Peer-group benchmarks without checking comparability**: invites herding around the median; rank flips on tiny return changes.
- **Ranking skill from 3-5 years of data**: one realized path out of many; track record too short for statistical certainty.
- **Using Sharpe for skewed strategies** (option writing, trend following): symmetric volatility penalty hides negative skew; use Sortino or capture and drawdown.
- **Assuming positive asymmetry means skill**: a rolling long-put hedge shows capture ratio above 1 by construction.
- **Counting on diversification to cut downside capture** without noting that correlations converge to 1 in crises.

## Exam Focus & Traps
- Measurement = what; attribution = how; appraisal = skill vs luck. "Measures excess return" is measurement; "distinguishes skill from luck" is appraisal; "explains how excess return was achieved" is attribution.
- Macro attribution is the asset owner's decisions (policy deviations, manager selection); micro is the PM's decisions. Macro uses the same BF formulas with managers/asset classes as the "sectors", folding interaction into selection.
- Returns-based attribution is the least accurate and is used when holdings are not available (hedge funds); the question that says "uses only total portfolio returns" is returns-based. Transactions-based reconciles.
- Allocation effect in BF uses `Bᵢ − B`; selection uses `Wᵢ` (benchmark weight), not `wᵢ`. Option with `wᵢ(Bᵢ − B)` is wrong (uses the full weight, not the active weight); option with `WᵢBᵢ` is a benchmark contribution, not an allocation effect.
- Interaction can be positive when an underweight meets negative selection (financials in the worked example) and vice versa.
- In fixed-income attribution: duration (shift) effect is negative when you are long duration and yields rise; flattener plus overweight at the long end gives a positive slope effect; overweight corporates when spreads widen hurts the spread effect; the residual grows when yields move a lot.
- Fixed-income exposure decomposition is for marketing and client reports; duration-based yield curve decomposition for analysts and PMs.
- Risk attribution choice: absolute mandate vs benchmark-relative, then bottom-up vs top-down vs factor. Market-neutral bottom-up with T-bill hurdle: marginal contribution to total risk. Bottom-up vs MSCI index: marginal contribution to tracking risk. Top-down sector timer with hedged market, T-bill + 300 bps: factor contributions to total and specific risk.
- Liability-based benchmarks suit the total DB pension fund (funded status) and liability-hedging sleeves; younger workforce means more equity; more inflation-indexed benefits means more real-return bonds.
- The seven Bailey-Tierney criteria: a cap-weighted bond index rebalanced often fails "investable"; an index with foreign bonds for a domestic manager fails "appropriate".
- Sortino: sqrt of the average squared shortfall over all N periods; the target semideviation can be backed out from `(Rp − MAR)/Sortino`.
- Capture ratio `> 1` means convex (positive asymmetry); `< 1` concave. A negative capture appears when manager and benchmark have opposite signs.
- Maximum drawdown is the single worst peak-to-trough, not an average; drawdown duration includes the recovery phase.
- Hedge fund benchmarks: broad indexes and cash plus spread fail the factor-sensitivity test; peer indexes suffer survivorship, backfill and stale-price bias (smoothed returns bias risk down). Real estate: appraisal smoothing, mixed leverage; open-end funds use time-weighted returns, closed-end funds IRR. Private equity: IRR, PME (Long-Nickels, PME+, Kaplan-Schoar, Direct Alpha), peer by vintage. Commodities: futures-based indexes, market-cap weighting not possible because futures have zero net market capitalization.

## Key Takeaways
1. Evaluate in three layers: measure, attribute, appraise; each needs the one before it.
2. Use Brinson-Fachler with the manager's real decision hierarchy (country, sector, security); always reconcile effects to `R − B` and show interaction or fold it into selection explicitly.
3. Choose the attribution data level by turnover and data quality: returns-based for opaque funds, transactions-based for active books.
4. Add risk attribution so every return source has a matching risk source.
5. Validate the benchmark against the seven criteria and the `corr(A,S)`, `corr(S,E)` tests before drawing any conclusion about skill; measure against the normal portfolio.
6. Use Sortino, capture ratios and drawdown for skewed or capital-preservation mandates; use the appraisal ratio and IR for active-risk efficiency.
7. Combine attribution, several appraisal ratios, a long record and qualitative process review; skill claims need convergent evidence.
8. Benchmark alternatives with their own tools (peer indexes with bias adjustments, PME, futures indexes) and state the limits.

## Connects To
- **ch04**: IPS, benchmarks and the portfolio management process that attribution feeds back into.
- **ch12**: multifactor models underlying factor-based attribution and alpha.
- **ch15**: active management analysis (information ratio, fundamental law of active management).
- **ch19**: manager selection uses these appraisal and attribution outputs as its quantitative layer.
- **`cfa-ethics-gips`**: GIPS standards for composite and return presentation.
- **`cfa-asset-allocation-cme` ch08**: strategic asset allocation versus tactical deviation, which macro attribution measures.
- **`cfa-wealth-institutional-management` ch04**: liability-driven benchmarks and funded status for pension funds.
