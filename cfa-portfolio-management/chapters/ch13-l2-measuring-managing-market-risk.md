# Chapter 13: Measuring and Managing Market Risk
> **Source**: CFA Program Curriculum 2022, Level II, Reading 40 · Portfolio Management | Don M. Chance, PhD, CFA, and Michelle McCarthy Beck

## Core Idea
No single number describes market risk. VaR gives a probabilistic loss threshold, sensitivities (beta, duration/convexity, delta/gamma/vega) explain what drives the loss, and scenarios/stress tests cover what history and the normal curve miss. Good risk management combines all three and then turns them into constraints (risk budgets, position, scenario and stop-loss limits, capital allocation) that actually change behavior.

## Learning Outcomes Covered
- explain VaR in measuring portfolio risk; compare parametric, historical simulation and Monte Carlo VaR; estimate and interpret each
- describe advantages, limitations and extensions of VaR (CVaR, incremental VaR, marginal VaR, ex ante tracking error)
- describe sensitivity and scenario risk measures, compare them with VaR, use equity/fixed-income/option exposure measures
- explain constraints: risk budgeting, position limits, scenario limits, stop-loss limits; use risk measures in capital allocation
- describe the risk measures used by banks, asset managers, pension funds and insurers

## Frameworks Introduced
- **Value at Risk (VaR)**: the minimum loss expected to be equalled or exceeded x% of the time over a stated horizon, under assumed market conditions; stated in currency or % of portfolio value.
  - When to use: a single comparable loss-frequency number across portfolios, desks, asset classes; regulatory reporting; capital allocation.
  - How: (1) decompose holdings into risk factors (risk decomposition); (2) collect factor histories over a lookback period (or specify parameters); (3) apply one of three methods; (4) read the left-tail cutoff (5%, 1%, or 16% = one standard deviation).
  - Failure mode: read as a maximum or worst case; it is only a floor on the tail. "5% VaR of 2.2 = a loss of at least 2.2 occurs about 1 trading day in 20."
- **Parametric (variance-covariance / analytical) VaR**: assumes normal risk-factor returns; uses expected return, standard deviations and correlations.
  - When to use: linear portfolios (cash equities, bonds) with reliable parameters; fast and transparent.
  - How: portfolio mean and σ from weights and covariances; convert to the VaR horizon (divide mean by T, σ by √T); VaR = −(μ − z·σ) × value, z = 1.65 (5%), 2.33 (1%), 1.00 (16%).
  - Failure mode: options and non-linear payoffs (truncated, non-normal distribution); fat tails; very sensitive to covariance inputs.
- **Historical simulation VaR**: reprice today's portfolio under each historical factor return in the lookback, sort P&L worst to best, take the percentile.
  - When to use: non-normal or option-containing portfolios when the lookback is representative of the future.
  - How: apply fixed current weights to each day's factor returns; sort; the 5th percentile is the 5% VaR. Can weight recent data more.
  - Failure mode: no new events; a short or calm window understates risk (a 1987-88 window overstates crash frequency); all observations equally weighted by default.
- **Monte Carlo simulation VaR**: simulate many random factor outcomes from a user-specified distribution (with the correlation matrix), reprice, sort, take the percentile.
  - When to use: many risk factors, options and embedded options, any distribution (fat tails, skew); the most flexible.
  - How: choose distribution and parameters, number of draws (no standard; more draws = more reliable but slower), preserve correlations, then read the percentile. With normal inputs and large samples it converges to parametric VaR.
  - Failure mode: garbage-in (parameters and distribution are assumptions); computational cost.
- **Scenario risk measures (historical / hypothetical)**: portfolio P&L under a multi-factor, large shock. Historical = replay of 1987, LTCM, 2001, 2008. Hypothetical = never-seen co-movements. **Reverse stress testing** targets the portfolio's top exposures and asks what would hurt them all together (including where hedges stop hedging).
  - How: reprice with full valuation models (do not apply delta-gamma or duration-convexity to options in big shocks); apply the shock instantaneously (no remedial trading) to test survivability; map instruments created after the event to proxies or factors.
- **Constraint toolkit**: risk budgeting (allocate VaR or ex ante tracking error), position limits (issuer, country, currency, liquidity as % of ADV), scenario limits (higher tolerance for more extreme scenarios), stop-loss limits and drawdown control, capital allocation (economic capital with hurdle rates). Use them in combination; scenario limits are the final screen after position, exposure and VaR/TE limits.

## Key Concepts
- **Market risk**: loss from moves in equity prices, interest rates, exchange rates, commodity prices; distinct from credit and operational risk.
- **Lookback period**: the historical window supplying risk-factor data.
- **Risk decomposition**: mapping holdings (e.g., a foreign convertible) into currency, equity and curve exposures.
- **Conditional VaR (CVaR) / expected shortfall / expected tail loss**: average loss given the VaR cutoff is breached; strictly not a VaR.
- **Incremental VaR (IVaR)**: change in portfolio VaR from a discrete change (add or resize a position): VaR(after) − VaR(before).
- **Marginal VaR (MVaR)**: change in VaR for a very small change in a position; computed with calculus; position-weighted MVaRs sum to total VaR, giving each position's contribution.
- **Ex ante tracking error (relative VaR)**: VaR of (portfolio − benchmark holdings), typically a 1σ annualized figure; near zero for an index replica. With a cash benchmark it equals plain VaR.
- **Ex post tracking error**: historical deviation of realized portfolio returns from the benchmark; judges skill, but reflects a strategy change only slowly (1 of 200 data points the next day).
- **Sensitivity measure**: response of value to one risk-factor change (beta, duration, convexity, delta, gamma, vega); says nothing about probability.
- **Key rate (partial) duration / credit spread duration**: price sensitivity to specific curve maturities / to spread moves with risk-free rates fixed.
- **Granularity**: width of risk-factor buckets; wider buckets assume perfect correlation inside the bucket.
- **Stress test**: scenario applying extreme negative shocks to a particular exposure.
- **Surplus at risk**: VaR of assets minus liabilities (liabilities entered as short fixed-income positions), usually over one year.
- **Economic capital**: capital a firm needs to survive severe losses at a very high confidence (e.g., 99%-99.99%, one year).
- **Drawdown control (portfolio insurance)**: increasing hedges as losses grow, a dynamic alternative to stop-loss liquidation.
- **Correlation risk**: correlations rising toward 1 in stress, removing diversification.

## Formulas & Reference Tables
- Parametric VaR (return form): `VaR% = −[E(Rp) − z·σp]`, `VaR$ = VaR% × V`; z (5%) = 1.65, z (1%) = 2.33, z (16%) = 1.00. `z = (R − μ)/σ`.
- Two-asset portfolio: `E(Rp) = w₁E(R₁) + w₂E(R₂)`; `σp = √(w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρ₁₂σ₁σ₂)`.
- Horizon scaling: `μ_daily = μ_annual/250`, `σ_daily = σ_annual/√250`. Do NOT scale a daily VaR by √250 or 250 (valid only with zero mean); recompute with annualized μ and σ.
- Historical/Monte Carlo VaR (5%): the 5th percentile of the sorted P&L. `CVaR = mean(losses beyond VaR cutoff)`. For a normal distribution: `CVaR% = −μ + σ·φ(zα)/α` (φ = standard normal pdf, α = tail probability).
- Incremental VaR: `IVaR = VaR(new weights) − VaR(old weights)`.
- Bond: `ΔB/B ≈ −D·Δy/(1+y) + ½·C·(Δy)²` (D = duration, C = convexity; the book writes the first term with the 1/(1+y) factor, i.e., modified duration D/(1+y)).
- Equity (CAPM): `E(Ri) = RF + βi[E(RM) − RF]`; `β = Cov(Ri,RM)/Var(RM)`.
- Option approximation: `Δc ≈ Δ·ΔS + ½·Γ·(ΔS)² + Vega·Δσ`. Call delta in [0,1], put delta in [−1,0]. Portfolio Greeks are the position-weighted sums; an ETF has delta 1, no gamma or vega.
- Capital allocation: return on allocated capital = expected profit / capital; compare to a hurdle rate.
- Funding ratio = assets / PV(liabilities).

| Method | Distribution | Options | Needs history | Speed | Main weakness |
|---|---|---|---|---|---|
| Parametric | normal (usually) | poor | only for parameter estimates | fastest | fat tails, non-linearity |
| Historical simulation | whatever occurred | good | required | fast | past may not repeat |
| Monte Carlo | any, user-specified | good | optional | slowest | model/parameter risk |

| Measure | Answers | Blind spot |
|---|---|---|
| VaR | how often losses of at least X occur | size beyond cutoff, liquidity, regime change |
| Sensitivities | what drives the risk, hedge ratios | probability and volatility differences across assets |
| Scenarios/stress | what a specific severe event costs | probability of the event; choice of scenario |

## Mental Models
- **VaR is a doorway, not a floor of the building**: it marks where the bad tail starts. CVaR tells what is behind the door; stress tests tell what the worst room looks like.
- **Three lenses**: VaR (how likely), sensitivities (why), scenarios (how bad if the model is wrong). Constraints should use more than one.
- **Use scenario limits as the last screen**, after size, exposure and VaR/TE limits, with looser tolerance for more extreme scenarios; a portfolio with zero stress sensitivity earns the risk-free rate.
- **Leverage dictates the measure**: leveraged players (banks, hedge funds) need high-confidence, short-horizon loss measures and pass/fail stress tests for solvency; long-only managers need relative measures (tracking error, active share) at low confidence over longer horizons.
- **Limit placement beats confidence level**: a loose 99% limit constrains less than a tight 84% limit.
- **Stressing makes the scenario writer timid**: pre-2008 US house-price stresses were about half the eventual move because bigger looked "irresponsible"; deliberately err toward severity.

## Worked Example
80% SPY / 20% SPLB, $150m, inputs annual: SPY 10.5% / 20%, SPLB 6% / 8.5%, ρ = −0.06 (book inputs, recomputed).
1. `E(Rp) = 0.8×10.5% + 0.2×6% = 9.60%`; `σp = √(0.64×0.04 + 0.04×0.007225 + 2×0.8×0.2×(−0.06)×0.2×0.085) = 15.988%`.
2. Daily: `μ = 0.0384%`, `σ = 15.988%/√250 = 1.0112%`.
3. 5% VaR: `1.65×1.0112% − 0.0384% = 1.630%` → **$2.445m** (about 1 day in 20 loses at least this). 1% VaR: `2.33×1.0112% − 0.0384% = 2.318%` → **$3.477m**. 16% VaR: **$1.459m**.
4. Annual 5% VaR: `1.65×15.988% − 9.60% = 16.78%` → **$25.2m**; naive `$2.445m×√250 ≈ $38.7m` and `×250 ≈ $611m` are both wrong.
5. IVaR for moving to 90/10: new daily σ = 1.1365%, new mean 0.0402%; VaR $2.752m; **IVaR ≈ +$307k**.
6. Normal-tail CVaR at 5%: `(−μ + σ·φ(1.645)/0.05)×V ≈ $3.07m`, i.e., about 26% above the VaR.
Book simulation results for comparison: historical (2015-19 data, low-vol equity period) 5% VaR $1.62m, CVaR $2.67m; Monte Carlo (10,000 normal draws) 5% VaR $2.52m. Historical VaR is lower because the SPY lookback volatility (13.6%) was well below the long-run 20% used in the parametric/MC inputs.
**⚠ Correction**: the source reports a Monte Carlo CVaR of $4.40m for a 5% VaR of $2.52m; for normal inputs the tail average should be about $3.1m, so treat that figure as unreliable. The source also quotes "500 historical returns" next to a 1,006-observation sample (50 tail points); the 1,006 count is the consistent one.

Second example (capital allocation): Portfolio A earns €50k on €325k (15.4%); Portfolio B earns €100k on €1,000k (10%). With a 15% hurdle, A creates value and B does not despite larger absolute profit.

## Anti-patterns
- **Reading VaR as the maximum loss** or as "95% of the time we lose less than X": VaR is a minimum loss in the tail; most days produce gains.
- **Annualizing daily VaR by √T (or by T)** without a zero-mean assumption: rescale μ and σ first.
- **Parametric VaR on option books**: payoffs are non-linear and the distribution changes with price, vol and time; use historical or Monte Carlo and full revaluation.
- **Delta-gamma or duration-convexity in large scenarios for options**: second-order terms fail at extreme moves; fully reprice.
- **Calm lookback window**: low-vol periods understate VaR; override with long-run judgment or add stress.
- **Imposing standalone desk VaR limits that sum to the firm limit**: with imperfect correlation the firm never uses its appetite; use marginal-VaR budgets or deliberate over-allocation.
- **Stress-testing against only the last crisis**: you hedge the replay and become vulnerable to the next one; add hypothetical and reverse stress tests.
- **Producing scenarios without actions or tolerances**: set limits per scenario and decide in advance what to trim or disclose.
- **Ignoring liquidity and correlation breakdown**: VaR understates both; use position limits (e.g., % of average daily volume) and gross exposure.

## Exam Focus & Traps
- Definition wording: "5% VaR = $X" means a loss **of at least** $X on 5% of days; the 95% confidence statement is "loss no more than $X 95% of the time". A 1% VaR is 2.33σ, not a 1% move; one σ = 16% VaR (84% confidence).
- Sign convention: VaR is reported as a positive number; step 3 flips the sign of (μ − zσ).
- Annualizing: use annual μ and σ (σ × √250), then compute VaR. Daily VaR × √250 is a distractor.
- Higher confidence (lower tail probability) means higher VaR; one-day to 10-day typically scales σ by √10.
- CVaR is best obtained from historical or Monte Carlo output; it is "average loss given VaR is exceeded", not a VaR itself. IVaR = discrete change; MVaR = infinitesimal change; MVaRs sum to total VaR (budgets built on them add up to the total).
- Which method for which case: options and non-normal returns → historical or Monte Carlo; many assets and complex distributions → Monte Carlo; simple linear and normal → parametric.
- Sensitivity vs VaR: sensitivities give no probability. Duration assumes parallel shift (effective correlation 1 across the curve). Duration and delta are first order; convexity and gamma second order; vega is the volatility effect (first order).
- Reverse stress test = start from the portfolio's top exposures and design a shock that hits them together (not reversing the sign of 2008).
- Hedge funds, banks and insurers use pass/fail stress tests; long-only managers do not rely on them for solvency. Insurance P&C: economic capital and VaR; life: asset-liability matching and scenarios including longevity.
- Pension: surplus at risk treats liabilities as short bonds; zero if assets match liabilities exactly; liability-hedging vs return-generating portfolios.
- Backward-looking (std dev, ex post TE, Sharpe, historical beta) vs current-holdings measures (VaR, ex ante TE, duration, stress): know which uses which.
- Stop-loss (cumulative loss triggers liquidation) is not risk budgeting; budgeting allocates VaR or TE.

## Key Takeaways
1. State VaR as "loss of at least X, p% of the time, over horizon h" and always report the method, lookback, confidence and horizon alongside it.
2. Choose the method by portfolio: parametric for linear/normal, historical for representative lookbacks and options, Monte Carlo for complex or fat-tailed cases; expect them to disagree and reconcile why.
3. Add CVaR for tail size, MVaR/IVaR for trade decisions, and ex ante tracking error for benchmarked mandates.
4. Decompose risk with sensitivities so a high VaR can be traced to high-beta equities, long duration or large delta.
5. Run historical, hypothetical and reverse stress tests with full revaluation; set tolerance levels and action steps for each.
6. Stack constraints: position limits for concentration and liquidity, VaR/TE budgets for diversified risk, scenario limits as final screen, stop-loss or drawdown control for trending losses.
7. Allocate capital where return per unit of economic capital clears the hurdle; the binding constraint (economic, regulatory or cash) is the one to price.
8. Match the toolkit to the entity: leverage, risk-factor mix and accounting/regulation decide which measures matter.

## Connects To
- **ch 08**: introductory risk-management framework (risk governance, risk types) this reading quantifies.
- **ch 14**: backtesting and simulation; VaR is validated by counting exceedances, and Monte Carlo/historical simulation mechanics are developed there.
- **ch 15**: ex ante vs ex post tracking error, active share and the fundamental law (benchmark-relative risk).
- **ch 12**: factor models supply the factor exposures and covariance matrices used in parametric VaR and tracking-error decomposition.
- **`hull-derivatives` ch 22**: VaR and expected shortfall, coherent risk measures, model-building vs historical simulation in depth.
- **`cfa-derivatives` ch 04**: option Greeks (delta, gamma, vega) used as sensitivity measures.
- **`cfa-fixed-income` ch 05**: duration, convexity and key rate duration behind the bond sensitivity measures.
