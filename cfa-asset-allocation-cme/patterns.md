# Patterns — Asset Allocation, CME and Behavioral Recipes

## Seven-Step CME Routine
**When to use**: producing a documented set of expectations for allocation.
**How**: 1. List asset classes and horizons (universe as small as workable). 2. Study history and return drivers. 3. Choose methods and data needs (DCF for long horizons, converging for short). 4. Pick sources and frequency. 5. Interpret with one common set of assumptions. 6. Document reasoning. 7. Compare outcomes on the same cycle and feed back.
**Trade-offs**: feedback is mostly qualitative (about 30 observations needed for a test); consistency beats precision. (ch 03)

## Input Screening for a Historical Statistic
**When to use**: before using any sample mean, volatility, correlation or relationship.
**How**: 1. Regime test: reason for a break and data evidence? Then use the relevant sub-period. 2. Check survivorship, appraisal smoothing, revisions, asynchronicity. 3. Ask "what story?" and test out of sample. 4. Test sensitivity to start and end dates. 5. Compute conditional by state, then probability-weight.
**Trade-offs**: shorter samples are more relevant but less precise; higher frequency helps variance and correlation, not the mean. (ch 03)

## Trend-Growth Anchor
**When to use**: long-run equity and bond expectations.
**How**: 1. Estimate growth = labor input + labor productivity; adjust the extrapolation for known differences. 2. Equity: `D/P + nominal GDP growth`, then add expected change in profit share and P/E (spread repricing over the horizon). 3. Bonds: real (nominal) yields gravitate to real (nominal) trend growth. 4. Strip valuation expansion from historical returns.
**Trade-offs**: growth is priced and capital deepening depresses returns, so high-growth countries need not earn more. (ch 03, 04)

## Cycle-Phase Overlay
**When to use**: 1-3 year tactical expectations.
**How**: 1. Locate the phase (output gap, employment, PMIs, LEI, curve). 2. Map to policy and rates, curve slope, spreads and assets (recovery: risk assets; late expansion: inflation hedges; slowdown: quality and rate-sensitive; contraction: duration and quality). 3. Fade to the unconditional mean as the horizon extends. 4. Check what is priced in.
**Trade-offs**: phases vary in length and amplitude; cyclical vs secular is hard to separate. (ch 03, 05)

## Taylor-Rule Policy Path
**When to use**: judging policy stance and projecting short rates.
**How**: 1. Fix `r_neutral`, inflation target, trend growth. 2. Plug expected inflation and growth; `i* = r_neutral + π_e + 0.5·gap_growth + 0.5·gap_inflation`. 3. Compare to the actual rate: "too low for too long" signals bubble risk. 4. Add judgment from central bank communication; at negative rates, use r_neutral as the long-run baseline.
**Trade-offs**: all inputs are unobservable; the rule is a frame, not a forecast. (ch 03, 05)

## Pricing-Equation Routing
**When to use**: tracing any macro shock to an asset.
**How**: 1. Write `P = ΣE[CF]/(1 + l + θ + π + γ + κ + φ)^s`. 2. Mark which term moves: cash flows, real rate, expected inflation, inflation-uncertainty, credit, equity or liquidity premium. 3. If both numerator and denominator move, net sign is ambiguous.
**Trade-offs**: premiums are inferred, not observed. (ch 05)

## Building-Block Return Forecast
**When to use**: asset-class expected returns.
**How**: 1. Bonds: `r_f + term + credit (spread − expected loss) + liquidity`; project YTM adjusted for horizon vs Macaulay duration. 2. Equities: Grinold-Kroner. 3. Real estate: `cap rate + NOI growth − %Δcap`. 4. Integrate with Singer-Terhaar (φ about 0.75-0.90 developed, 0.50-0.75 EM and real estate) and add an illiquidity premium. 5. De-smooth private assets and shrink the covariance matrix.
**Trade-offs**: equilibrium models assume liquid markets. (ch 04)

## Covariance Estimation Ladder
**When to use**: before any optimizer.
**How**: 1. Sample matrix only if observations are at least 10 times assets. 2. Factor model to cut parameters (N=100, K=5: 4,950 to 515). 3. Shrink toward the factor target. 4. De-smooth private assets. 5. ARCH for time-varying volatility.
**Trade-offs**: shrinkage is biased but lowers mean-squared error. (ch 04)

## Behavioral Alpha Top-Down Diagnosis
**When to use**: classifying a client or advisor quickly.
**How**: 1. Decide active vs passive (did the client risk own capital?). 2. Place on the risk scale. 3. Test the biases tied to the candidate type. 4. Classify (PP, FF, II, AA) and tailor: goals for emotional types, data for cognitive types. 5. Moderate cognitive errors, adapt to emotional ones.
**Trade-offs**: biases cluster but overlap; detection shows presence, not magnitude. (ch 01, 02)

## Approach Selection and Economic Balance Sheet
**When to use**: opening any allocation study.
**How**: 1. Build economic balance sheet (human capital, PV of pensions, goals). 2. Legal liability with a penalty: liability-relative. Many goals with different priorities: goals-based. Otherwise asset-only. 3. Specify asset classes by the five criteria. 4. Start at the global market portfolio and justify every departure. 5. Test robustness with Monte Carlo and CME sensitivity.
**Trade-offs**: more classes add spurious precision. (ch 06, 07)

## Stabilizing the Optimizer
**When to use**: MVO gives concentrated or unstable weights.
**How**: 1. Reverse-optimize implied returns. 2. Layer views with Black-Litterman. 3. Optionally resample. 4. Constrain only for real constraints. 5. Check risk budget: `(E(R_i) − r_f)/MCTR_i` equal.
**Trade-offs**: resampling adds smoothness, not new information. (ch 07)

## Constraint Screen and After-Tax Run
**When to use**: before implementation.
**How**: 1. Check size, governance, eligibility, ticket vs manager AUM. 2. Stress liquidity needs against asset liquidity. 3. Convert returns and risks to after-tax; keep correlations; place assets by tax efficiency. 4. Widen taxable band `R_pt/(1 − t)`. 5. Add regulatory, ESG and funding limits.
**Trade-offs**: tax lowers volatility, which favors equity in taxable accounts. (ch 08)

## Goals-Based Module Allocation
**When to use**: individuals with several goals.
**How**: 1. Set horizon and required probability per goal. 2. Pick the module maximizing `E(R)T − zσ√T` annualized. 3. Discount goal cash flows at that rate. 4. Aggregate capital-weighted; surplus to a labeled module.
**Trade-offs**: rates are conservative, so expect surplus. (ch 07)
