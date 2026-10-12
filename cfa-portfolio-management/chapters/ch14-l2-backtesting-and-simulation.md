# Chapter 14: Backtesting and Simulation
> **Source**: CFA Program Curriculum 2022, Level II, Reading 41 · Portfolio Management | Yin Luo, CFA, and Sheng Wang (Wolfe Research)

## Core Idea
A backtest asks how a rule-based strategy would have done in the past; it is only as honest as its data hygiene (point-in-time, survivors and casualties, realistic lags, costs) and only as informative as the future resembles history. Layer scenario analysis (regimes), historical and Monte Carlo simulation (randomness) and sensitivity analysis (distribution assumptions) on top, because fat tails and negative skew make a single historical path a poor guide to downside risk.

## Learning Outcomes Covered
- describe the objectives of backtesting an investment strategy
- describe and contrast the steps (strategy design, historical investment simulation, output analysis)
- interpret backtest metrics and visuals (Sharpe, Sortino, volatility, max drawdown, VaR/CVaR, skewness, kurtosis, log cumulative wealth)
- identify problems: survivorship bias, look-ahead bias, data snooping
- evaluate a historical scenario analysis (expansion vs recession, high vs low volatility)
- contrast Monte Carlo and historical simulation; explain inputs, decisions and interpretation
- demonstrate sensitivity analysis

## Frameworks Introduced
- **Three-step backtesting process**: strategy design → historical investment simulation → analysis of backtest output.
  - When to use: accept/reject a signal, screen, or allocation rule before capital is committed; used by fundamental managers too (e.g., does a valuation screen add excess return?).
  - How: (1) state goal and hypothesis, turn it into rules and fix key parameters: investment universe, return definition (single currency vs local; benchmark), rebalancing frequency and transaction costs (monthly typical), start/end dates (long history plus regime splits); (2) rebuild the portfolio each period from in-sample data and record out-of-sample (OOS) results; (3) compute return/risk statistics and visuals.
  - Failure mode: assumes the future resembles history; ignores costs and liquidity; results look better than live.
- **Rolling-window (walk-forward) backtest**: each rebalance date uses an in-sample window to form the portfolio, then measures the next OOS period; OOS data later become in-sample. Many samples, not two. A multi-layer strategy (e.g., factor portfolios then risk parity weights) needs the rolling window applied at each layer (e.g., 5 years of monthly data to estimate the covariance matrix for risk parity), or look-ahead bias creeps in.
- **Long-short hedged quantile portfolio** (Fama-French 1993 style): rank the universe on the signal, split into quintiles/deciles, long top, short bottom, equal- or cap-weighted within quantile. Drawback: not every manager can short.
- **Benchmark (equal-weight) vs risk parity (equal risk contribution) factor allocation**: BM weights each factor 1/N; RP weights so each factor contributes equally to portfolio risk, using volatilities and correlations (long-only weights summing to 100%). 1/N often matches or beats complex optimizers; RP lowers volatility and tail risk when factors differ in risk.
- **Historical scenario analysis**: re-run the backtest inside discrete regimes (recession vs expansion, VIX above vs below its 5-year moving average) to expose structural-break sensitivity. Regime labels (e.g., NBER recessions) are known only in hindsight, a built-in look-ahead.
- **Simulation (8 steps)**: (1) define the target variable (strategy return and its distribution); (2) key decision variables (asset/factor returns rᵢ,ₜ and weights ωᵢ,ₜ); (3) number of trials N (typically 1,000-10,000); (4) distributional properties (historical draws vs specified distribution); (5) random number generation; (6) compute the target for each draw; (7) repeat N times; (8) compute mean, volatility, Sharpe, CVaR, maximum drawdown.
  - **Historical simulation**: bootstrap (sample with replacement) historical periods without time order; a non-deterministic rolling-window backtest; preserves actual skew, kurtosis and cross-correlation; limited to what occurred.
  - **Monte Carlo simulation**: calibrate a multivariate distribution (mean, σ, correlations) and draw from it; flexible but model-dependent; complex and computation-heavy.
- **Sensitivity analysis**: change an input assumption (e.g., multivariate normal to multivariate skewed Student's t) and rerun to see how the target and risk metrics move.
  - Why it works / failure mode: reveals whether conclusions depend on the distribution choice; skewed t needs more parameters, so lower specification error but larger estimation error (bias-variance trade-off).

## Key Concepts
- **Backtesting**: applying a rule-based strategy to historical data to approximate real investing and learn its risk-return trade-off.
- **Investment universe**: all securities the strategy may hold (e.g., Russell 3000); must match the mandate (a domestic-only restriction means a domestic universe).
- **In-sample / out-of-sample (OOS)**: data used to build the portfolio vs the subsequent period used to evaluate it.
- **Trailing earnings yield**: trailing 12-month EPS / current price; usable when EPS ≤ 0, unlike P/E.
- **Maximum drawdown**: largest peak-to-trough loss; complements standard deviation, which does not capture path loss in non-normal series.
- **Sortino ratio**: Sharpe-like ratio using downside deviation.
- **Structural break (regime change)**: lasting change in market behavior (recession, policy shifts such as QE, technology shifts); visible as flattening or decay in a log cumulative-wealth plot.
- **Survivorship bias**: using only entities that survived to the end date; a special case of look-ahead bias.
- **Point-in-time (PIT) data**: data as known on each historical date, including casualties, restatement-free, with true release dates.
- **Look-ahead bias**: using information unavailable at the decision date (reporting lags, revised data, vendor back-filling, future index membership).
- **Reporting lag**: assumed delay between period end and data availability (about 1-2 months US/Canada/Japan, 2-3 Europe/UK/ANZ, about 3 EM Asia/LATAM/EMEA in the source study); too long creates stale data.
- **Data snooping (p-hacking)**: inferring after viewing results (running many tests, picking the best); yields false positives.
- **Cross-validation**: testing on data not used to form the inference (other regions, hold-out samples); rolling-window testing is a deterministic form.
- **Bootstrapping**: random sampling with replacement; needed when trials exceed the historical sample.
- **Inverse transformation**: converting a uniform random number into a draw from a target distribution.
- **Model calibration**: estimating distribution parameters from data by regression or distribution fitting.
- **Tail dependence**: assets crash together more than a normal model implies.
- **Sensitivity analysis**: studying how a target changes with an input assumption; contrast with scenario analysis, which splits or shocks the environment.

## Formulas & Reference Tables
- Trailing earnings yield: `EY = EPS(TTM) / Price`
- Portfolio return in simulation: `r_p,t = Σᵢ₌₁ᴷ ωᵢ,ₜ · rᵢ,ₜ`
- Sharpe ratio: `(mean return − rf) / σ` (long-short hedged series are often quoted with rf ≈ 0).
- CVaR (95%): average of returns at or below the 5th percentile; maximum drawdown: `min over t of (Wₜ / max_{s≤t} Wₛ − 1)`.
- Parameters for a K-variable multivariate normal: K means, K standard deviations, `K(K−1)/2` correlations or covariance elements (8 factors: 28; 9 factors: 36; 6 factors: 15).
- Bootstrap mapping: with N months, a uniform draw u selects month ⌈u·N⌉ (N = 374 → each month spans 1/374 = 0.00267).

| Problem | What goes wrong | Fix |
|---|---|---|
| Survivorship bias | only today's index members; flips conclusions (low-vol anomaly reversed: high-vol beat low-vol about 5.5x on survivors) | PIT universe incl. delisted names |
| Look-ahead bias | uses unreported or revised data; zero-lag inflated the US value backtest by almost 100% | PIT data; region-specific reporting lag (without making it stale) |
| Data snooping | best-of-many selection | higher bar (t > 3.0), cross-validation, pre-registered hypothesis |
| Ignoring costs | anomalies vanish after costs | include and disclose costs; lower turnover |
| Non-stationarity | one regime drives the result | long sample plus regime/scenario splits |

| Technique | Randomness | Uses | Weakness |
|---|---|---|---|
| Rolling-window backtest | none (deterministic path) | realistic, rule-following history | one path; past repeat assumed |
| Historical simulation | bootstrap of history | actual tails, correlation | only observed events |
| Monte Carlo | draws from fitted distribution | any scenario, extreme tails | wrong distribution understates risk |
| Scenario analysis | none (split sample) | regime robustness | regimes known ex post |
| Sensitivity analysis | varies inputs | assumption robustness | more parameters, estimation error |

## Mental Models
- **A backtest is a rejection filter first**: a strategy that fails historically is rarely adopted; passing proves little. Treat every strong result as a hypothesis for out-of-sample or cross-market validation.
- **Sharpe is stable, tails are not**: across rolling backtest, bootstrap and Monte Carlo the Sharpe ordering of BM vs RP held, while CVaR differed by method. Judge risk with CVaR, drawdown, skew and kurtosis, not only σ.
- **Maximum drawdown rule of thumb from the source**: about 3.3x annual volatility for the earnings-yield long-short (US 41.0% vs 12.4% vol; Europe 30.2% vs 9.9%).
- **Method disagreement is information**: if Monte Carlo with a normal or skewed t gives a much smaller CVaR than historical simulation, the assumed distribution is understating fat tails.
- **Use point-in-time or do not bother**: every data shortcut (current constituents, latest restated numbers, zero lag) biases toward optimistic results.
- **Prefer cross-markets validation**: if a strategy built in the US also works in nine other regions (RP cut volatility in all 10 markets and raised Sharpe in 7 of 10), it is probably not snooping.

## Worked Example
Historical simulation vs Monte Carlo trial, 8 factor portfolios (source inputs, recomputed).
- Bootstrap: random number 0.59163 × 374 = 221.3 → month 222 (September 2006). Factor returns: EY 2.5, B/M 0.3, growth −0.8, momentum 0.0, revision −0.8, ROE 2.5, D/E 0.5, quality −0.5 (%).
  - BM (equal weight 0.125): `0.125 × (2.5+0.3−0.8+0−0.8+2.5+0.5−0.5) = 0.46%`.
  - RP with May 2019 weights (6.0, 30.3, 11.7, 5.2, 10.4, 6.3, 9.6, 20.4 %): `≈ 0.17%`. Repeat for 1,000 trials, then compute Sharpe and CVaR.
- Monte Carlo trial 1 (multivariate normal draw: −3.2, −3.1, −0.2, 0.7, 2.3, −3.3, −1.7, 1.9 %): BM `= −0.83%`, RP `= −0.86%`.
- Backtest read-out: US earnings-yield long-short, 1986-2019: return 9.24%, vol 12.36%, Sharpe `9.24/12.36 = 0.75`, max drawdown −41.0%; Europe 6.65% / 9.90% / 0.67 / −30.2%. Similar Sharpe, lower return and lower vol in Europe. Distribution shows negative skew and excess kurtosis: expect negative surprises.
- Multifactor outcome (US, 1993-2019, monthly): BM mean 0.5%, σ 1.6%, skew −2.40, kurtosis 17.8, min −10.9%, VaR95 −2.6%, CVaR95 −7.9%, max drawdown 22.6%; RP mean 0.4%, σ 0.7%, skew +0.51, kurtosis 5.4, min −2.5%, VaR95 −0.7%, CVaR95 −0.9%, max drawdown 3.8%. Same return, less than half the volatility, far thinner left tail: RP is the better choice for a risk-averse investor.
- Scenario read-out (Sharpe, Strategy II minus Strategy I): high vol 0.68, low vol 0.96, recession 1.56, non-recession 0.52. Strategy II dominates in all four regimes; the gap is largest in recession.

## Anti-patterns
- **Using current index constituents** for a historical test: survivors only; can reverse a factor's sign.
- **Assuming zero reporting lag, or latest restated figures**: look-ahead; inflates Sharpe (almost doubled for US value).
- **A single flat lag for all firms**: stale data for early reporters; use region- or firm-specific lags or true PIT dates.
- **Testing dozens of variants and presenting the best**: data snooping; report the number of trials and demand t > 3.
- **Omitting transaction costs and shorting constraints**: many anomalies disappear; state whether costs are included.
- **Rolling only the first layer of a two-layer strategy**: estimating risk-parity weights on the full sample leaks future covariances.
- **Judging risk by volatility alone** for non-normal strategies: use max drawdown, CVaR, skew and kurtosis.
- **Running Monte Carlo with a normal distribution and calling it conservative**: understates tails (BM CVaR under MC normal and skewed t was less severe than backtest/historical simulation).
- **Short samples**: one regime only; findings may not generalize.

## Exam Focus & Traps
- Backtest steps: design → historical simulation → analysis; rolling-window divides data into many samples (statement "just two samples" is false); OOS becomes later in-sample.
- Survivorship bias is a type of look-ahead bias; PIT data fixes both but NOT data snooping.
- Look-ahead sources: reporting lags, data revisions (GDP is released about 30 days later and revised), vendor back-filling new companies, future index inclusion.
- Data snooping fixes: higher t-stat hurdle (above 3.0), cross-validation, other regions; choosing the model with the best t-stat is the classic tell.
- Historical simulation: random with replacement (bootstrapping) when trials exceed the sample; both historical and Monte Carlo simulation use random number generators (non-deterministic); Monte Carlo needs a distribution and a multivariate form when assets are correlated.
- Scenario analysis splits history by regime (recession/volatility, trade agreement vs not); sensitivity analysis changes input assumptions (normal → skewed t). Splitting by regime is not sensitivity analysis.
- Parameters count: K(K−1)/2 correlations, for all K variables (not only the correlated ones).
- Skewed t: accounts for skew and kurtosis but more parameters → larger estimation error.
- Risk-averse investors prefer positive skew, low kurtosis, smaller drawdown; VaR 95% "5% of the time losses of at least X"; CVaR is the average beyond VaR (CVaR is the more comprehensive tail measure).
- Typical trap: choosing "stale data" for an over-long reporting lag adjustment, not data snooping.
- Backtesting and historical simulation share the "past repeats" assumption; Monte Carlo alone does not use historical data directly (it only calibrates to it).

## Key Takeaways
1. Write the hypothesis, universe, return definition, rebalancing frequency, costs and dates before running anything.
2. Use rolling-window (walk-forward) construction, at every layer of a multi-layer strategy, so every decision uses only information then available.
3. Insist on point-in-time data including delisted names; apply realistic, region-appropriate reporting lags.
4. Report Sharpe together with drawdown, VaR/CVaR, skew and kurtosis, and plot cumulative wealth on a log scale to see decay and breaks.
5. Control data snooping: log the number of tests, require t > 3, cross-validate across markets and periods.
6. Test regimes (recession, volatility) with scenario analysis; they reveal whether a strategy is robust or regime-bound.
7. Complement the backtest with bootstrap historical simulation and Monte Carlo, then run sensitivity analysis on the distribution assumption; trust CVaR only when methods agree.
8. Prefer simple objective weighting (equal weight, risk parity) over fragile optimization, and judge allocation methods on tail risk, not just return.

## Connects To
- **ch 12**: multifactor models and factor portfolios that these backtests evaluate (value, momentum, quality, risk parity factor weighting).
- **ch 13**: VaR, CVaR, historical and Monte Carlo VaR methods and stress testing that the simulation section reuses.
- **ch 15**: active management metrics (information ratio, fundamental law) that a backtest estimates.
- **ch 16**: transaction costs and implementation shortfall; why costs erase backtested alpha.
- **ch 18**: performance evaluation (Sharpe, attribution) applied to realized, not backtested, results.
- **`cfa-quantitative-methods` ch 10 and ch 11**: machine learning (cross-validation, bias-variance trade-off) and big data projects.
- **`cfasi-equity-investment-styles`**: factor investing and systematic strategies being backtested.
- **`hull-derivatives` ch 22**: VaR and expected shortfall, Monte Carlo and historical simulation in depth.
