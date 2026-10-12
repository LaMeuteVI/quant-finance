# Chapter 4: Common Probability Distributions
> **Source**: CFA Program Curriculum 2020, Level I, Reading 9 · Quantitative Methods | DeFusco, McLeavey, Pinto, Runkle

## Core Idea
A probability distribution is the complete description of a random variable; four of them (uniform, binomial, normal, lognormal) plus simulation cover nearly every model in investments (binomial option trees, CAPM/mean-variance, Black-Scholes-Merton, VaR). The practical skill is knowing which distribution fits which quantity: returns are (approximately) normal, prices are lognormal, success counts are binomial, and anything too complex gets simulated.

## Learning Outcomes Covered
- define probability distribution; discrete vs continuous random variables; probability function vs cdf
- calculate probabilities from a cdf (interval = difference of cdf values)
- define and use discrete uniform, Bernoulli, binomial; build a binomial tree for stock prices
- define and use the continuous uniform distribution
- key properties of the normal; univariate vs multivariate; role of correlation
- probability that a normal variable falls in an interval; standardize (z-score) and use the standard normal
- shortfall risk, safety-first ratio, Roy's safety-first criterion
- relation between normal and lognormal; why lognormal models prices
- discrete vs continuously compounded returns; compute a continuously compounded return
- Monte Carlo simulation: applications and limits; Monte Carlo vs historical simulation

## Frameworks Introduced
- **Probability function and cumulative distribution function (cdf)**: p(x)=P(X=x) for discrete variables, f(x)=pdf for continuous; F(x)=P(X≤x) for both.
  - When to use: any time you need a probability for a range, not a point.
  - How: P(a<X≤b)=F(b)−F(a). For continuous variables the endpoints carry zero probability, so `P(a≤X≤b)=P(a<X<b)` (not true for discrete variables, where mass sits on points). A valid probability function has 0≤p(x)≤1 and Σp(x)=1; a valid cdf is non-decreasing between 0 and 1.
- **Binomial model (Bernoulli trials)**: X~B(n,p) = number of successes in n independent trials with constant success probability p.
  - When to use: win/loss records (broker trades, manager hitting a tracking band), count of defaults in a bond portfolio, up-moves in a price tree.
  - How: (1) confirm two binary outcomes, constant p, independent trials; (2) `p(x)=C(n,x)·pˣ(1−p)ⁿ⁻ˣ`; (3) for "x or fewer" sum or use the cdf; for "x or more" use `1−F(x−1)`; (4) interpret as "how likely is a record this good/bad if the true p were the benchmark value" (a p-value in spirit).
  - Failure mode: independence is often false (defaults cluster in recessions, so the variance is understated); magnitude of gains/losses is ignored (a 70% hit rate can still lose money).
- **Binomial tree**: price moves up (×u, probability p) or down (×d, probability 1−p) each period; after n steps the number of up-moves is binomial, but the **price** is a function of that binomial variable, u, d and S₀ (price itself is not binomial).
  - When to use: option pricing (including American options with early-exercise tests at each node); approximating lognormal prices with many small periods.
  - How: build forward to terminal nodes (uuuS, uudS, uddS, dddS at t=3); number of paths to a node = C(n,x); value derivatives by stepping backward recursively, testing contingencies (exercise) at each node.
- **Standardization and the standard normal**: `Z=(X−μ)/σ`, N(z)=P(Z≤z).
  - When to use: any normal probability. Three steps for a shortfall: subtract the mean, divide by σ, evaluate N(·).
  - How: use symmetry. `N(−x)=1−N(x)`, `P(Z≥x)=1−N(x)`, `P(Z≥−x)=N(x)`. Quantiles: one-tail 90%=1.282, 95%=1.645, 99%=2.326; two-tail 90%=1.645, 95%=1.96, 99%=2.576.
- **Roy's safety-first criterion**: choose the portfolio that minimizes P(R_P<R_L), the probability of falling below the minimum acceptable return (threshold) R_L; under normality this is the portfolio that maximizes `SFRatio=[E(R_P)−R_L]/σ_P`.
  - When to use: downside-focused clients with a hard floor (education bill, liability funding, not invading principal).
  - How: (1) set R_L from the client need (e.g., needed cash/portfolio value); (2) compute SFRatio for each candidate; (3) pick the highest; (4) shortfall probability = N(−SFRatio). If a risk-free asset yields at least R_L, hold 100% of it (zero shortfall).
  - Why it works: SFRatio is "how many standard deviations the mean sits above the floor"; a bigger number means a smaller left-tail probability. Replace R_L with R_F and you get the **Sharpe ratio**, so the highest Sharpe portfolio minimizes P(return < risk-free rate).
  - Failure mode: relies on normality (fat tails understate shortfall); ranking can flip with tiny input changes (B at 10% rather than 11% mean would lose to A in the book's example); a hard need is better treated as a liability and matched.
- **Monte Carlo simulation (7 steps)**: (1) specify the quantity of interest in terms of underlying variables and starting values; (2) specify a time grid (K subperiods, Δt); (3) specify distributions for the risk factors (e.g., ΔS = μ·S·Δt + σ·S·Z); (4) draw random values of the risk factors; (5) compute the underlying variables (price path); (6) compute the quantity of interest for that trial and discount; (7) repeat for I trials and average. Steps 1–3 specify, steps 4–7 run.
  - When to use: path-dependent or complex payoffs (Asian options, MBS), asset-liability planning for pension plans, VaR (cutoff of the worst 5% of simulated P&L = 95% VaR), stress-testing a model's assumptions.
  - Failure mode: output is a statistical estimate, not an exact answer; garbage-in distributions give garbage-out; accuracy grows only with √trials (100× the trials for one extra digit).
- **Historical (back) simulation**: resample (with replacement) from the actual return history instead of assuming a distribution.
  - When to use: you trust the record and want no distributional assumption.
  - Failure mode: cannot show risks absent from the sample (a crash outside the window), and does not support "what if" analysis.

## Key Concepts
- **Random variable**: quantity whose outcome is uncertain; uppercase X is the variable, lowercase x an outcome.
- **Discrete random variable**: countable outcomes (even if infinite); **continuous**: uncountable, so P(X=x)=0 at any single point.
- **Probability function p(x)/f(x)**: probability (mass) or density at x; for continuous variables probabilities are areas under the pdf.
- **Cumulative distribution function F(x)**: P(X≤x), cumulates the probability function.
- **Discrete uniform**: n equally likely outcomes, p(x)=1/n; **continuous uniform** on (a,b): f(x)=1/(b−a), the basis for random-number generation.
- **Bernoulli trial**: one trial with two outcomes (1 with probability p, 0 with 1−p); binomial is a sum of n Bernoullis.
- **Univariate vs multivariate distribution**: one variable vs a joint distribution for a group; a multivariate normal for n assets needs n means, n variances and n(n−1)/2 distinct correlations (30 stocks = 435 correlations).
- **Normal distribution**: symmetric bell curve on (−∞,+∞), fully described by μ and σ²; skewness 0, kurtosis 3 (excess 0); mean=median=mode; any linear combination of normals is normal (so a portfolio of jointly normal assets is normal).
- **Central limit theorem (CLT)**: the sum or mean of many independent, identically distributed variables with finite variance is approximately normal whatever the underlying shape.
- **Shortfall risk**: risk that portfolio value or return falls below a minimum acceptable level over a horizon.
- **Lognormal distribution**: Y is lognormal if ln Y is normal; bounded below by 0, right-skewed; parameters are the mean and variance of the associated normal (of ln Y), not of Y itself.
- **Continuously compounded return**: `r=ln(S₁/S₀)=ln(1+HPR)`; always smaller than the HPR and additive over time.
- **IID returns**: independent (past returns do not predict future ones, i.e., weak-form efficiency) and identically distributed (stationary mean and variance).
- **Volatility**: standard deviation of continuously compounded returns, quoted annualized (convention: √250 trading days).
- **Value at Risk (VaR)**: loss level that is exceeded with a given small probability (5% or 1%) over a horizon; the variance-covariance method assumes normality.
- **Pseudo-random numbers**: uniform(0,1) draws from a seeded algorithm; same seed gives the same sequence. Any distribution can be sampled through the **inverse transformation method**: draw r~U(0,1), return F⁻¹(r).

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Binomial probability | `p(x)=n!/[(n−x)!x!]·pˣ(1−p)ⁿ⁻ˣ` |
| Bernoulli mean / variance | `p` / `p(1−p)` |
| Binomial mean / variance | `np` / `np(1−p)` (variance assumes independence) |
| Discrete uniform | `p(x)=1/n` |
| Continuous uniform pdf, cdf | `f(x)=1/(b−a)`; `F(x)=(x−a)/(b−a)` for a<x<b; mean `(a+b)/2`; variance `(b−a)²/12` |
| Interval from cdf | `P(a<X≤b)=F(b)−F(a)` |
| Normal pdf | `f(x)=[1/(σ√(2π))]·exp[−(x−μ)²/(2σ²)]` |
| Standardize | `Z=(X−μ)/σ` (use sample X̄ and s when μ, σ unknown) |
| Safety-first ratio | `SFRatio=[E(R_P)−R_L]/σ_P`; `P(R_P<R_L)=N(−SFRatio)` |
| Lognormal mean | `μ_L=exp(μ+½σ²)` (exceeds exp(μ)) |
| Lognormal variance | `σ_L²=exp(2μ+σ²)·[exp(σ²)−1]` |
| Price relative | `S₁/S₀=1+R₀,₁` |
| Continuous return | `r_t,t+1=ln(S_{t+1}/S_t)=ln(1+R_t,t+1)` |
| Terminal price | `S_T=S₀·exp(r₀,T)` |
| Additivity | `r₀,T=r₀,₁+r₁,₂+…+r_{T−1,T}` |
| Mean / variance over T (IID) | `E(r₀,T)=μT`; `σ²(r₀,T)=σ²T`; `σ(r₀,T)=σ√T` |
| Mean of future price | `E(S_T)=S₀·exp[E(r₀,T)+½σ²(r₀,T)]` |
| Annualized volatility | `σ_annual=σ_daily·√250` |
| Sample-statistic noise (normal data) | SD of sample skewness ≈ √(6/n); SD of sample kurtosis ≈ √(24/n) |

**Normal coverage intervals**

| Interval | Probability | Exact multiplier |
|---|---|---|
| μ ± ⅔σ | ≈50% | |
| μ ± σ | ≈68% (34.13% each side) | |
| μ ± 2σ | ≈95% | ±1.96σ for 95% |
| μ ± 3σ | ≈99% | ±2.58σ for 99% |

**Which distribution for what**

| Quantity | Model | Why |
|---|---|---|
| Count of successes in n yes/no trials | Binomial | independent, constant p |
| Equally likely outcomes / ignorance prior | Uniform | basis of random-number generators |
| Portfolio or asset returns over a horizon | Normal (approx.) | CLT, symmetry, closed under linear combos |
| Asset prices | Lognormal | cannot go below 0; right skew |
| Complex/path-dependent payoffs | Monte Carlo | no closed form |

## Mental Models
- **Returns are normal, prices are lognormal.** Normal has no floor (a return below −100% is impossible), so use it for returns, and use exp(·) of a normal return to get a price with a floor at 0.
- **Use the cdf, not the pdf, for any "at most / at least / between" question.** Every interval probability is a difference of two cdf values; every tail probability is `N(z)` or `1−N(z)`.
- **Safety-first = "how many sigmas of cushion do I have above my floor?"** The bigger the cushion, the smaller the tail. Sharpe ratio is the same idea with the risk-free rate as the floor.
- **Log returns add, simple returns multiply.** Convert to logs to scale over time (σ√T) and back to compounding to get wealth.
- **Binomial = coin-flip bookkeeping with a binary tree on top.** Count the paths (combinations) times the per-path probability.
- **Monte Carlo is "shaking the ladder"**: rehearse the policy under thousands of random futures before committing; historical simulation replays the one past you actually saw.
- **Fat tails**: when kurtosis > 3 the normal underestimates extreme returns; quarterly or annual diversified-equity returns fit better than daily or weekly; options and skewed payoffs fit poorly.

## Worked Example
**Broker audit (binomial).** Broker BB001: 3 profitable trades of 12. If prices are fair, p=0.5. Probability of 3 or fewer profitable: `F(3)=Σ C(12,k)·0.5¹²` for k=0..3 = (1+12+66+220)/4096 = 0.0730 (verified in Python: 0.072998). About 7.3%: suggestive but not conclusive. BB002: 5 of 8 profitable; `P(X≥5)=1−F(4)=0.3633`, so nothing unusual (a 36% chance under fair pricing). Tracking manager: hits the ±75 bp band in 6 of 8 quarters; if true hit rate is 90%, `F(6)=0.1869`, a moderate 18.7% chance of a record that bad or worse. Decide only after more evidence; also check size of gains/losses.

**Safety-first (Roy).** Client has C$800,000 and may withdraw C$30,000 next year without touching principal, so `R_L=30,000/800,000=3.75%`. Allocations (E(R), σ): A (25%, 27%), B (11%, 8%), C (14%, 20%).
SFRatio: A=(25−3.75)/27=0.787; B=(11−3.75)/8=0.906; C=(14−3.75)/20=0.5125. Pick B. `P(R_B<3.75%)=N(−0.906)=18.2%` (exact; 18.1% with table rounding to 0.91). Sensitivity: if B's mean were 10%, SFRatio=0.781 and A would win (0.787).

**Volatility from prices.** Astra closes 6,950 / 7,000 / 6,850 / 6,600 / 6,350. Log returns: 0.00717, −0.02166, −0.03718, −0.03861; sample SD (n−1) = 0.021261; annualized `0.021261×√250=33.6%`. With normal daily log returns, future prices are lognormal. Four points say nothing reliable about the mean.

**Monte Carlo sanity check (verified in Python).** European call, S₀=K=100, r=5%, σ=20%, T=1. Simulating 200,000 terminal prices `S_T=S₀·exp[(r−σ²/2)T+σ√T·Z]` and discounting the average payoff gives 10.49 (standard error 0.03) versus Black-Scholes-Merton 10.45: simulation converges to the analytic value, but analytics are faster and give sensitivities. Use Monte Carlo only where no formula exists (Asian call).

## Anti-patterns
- **Modeling prices as normal**: allows negative prices; use lognormal (or normal on returns).
- **Applying the binomial formula to correlated trials**: defaults in one sector or period are not independent, so variance np(1−p) is understated.
- **Treating the lognormal mean as exp(μ)**: the correct mean is exp(μ+½σ²); the parameters μ, σ² belong to ln Y, not Y.
- **Building symmetric ±kσ intervals for a lognormal**: it is skewed, so such intervals do not apply.
- **Using σ as the risk measure for a uniform variable**: ±σ bands capture different shares of probability depending on (a,b); ±2σ can extend past the limits.
- **Trusting the normal for tail risk (VaR) on daily data**: excess kurtosis means extreme losses occur more often than N predicts.
- **Reading Monte Carlo output as exact or as evidence of causality**: it is a statistical estimate under assumed distributions.
- **Annualizing with the wrong day count or without √T**: multiply daily σ by √250, not by 250.
- **Running historical simulation on a calm window and calling the result "risk"**: it contains only what happened in the sample.

## Exam Focus & Traps
- **Point probability for a continuous variable is 0**, so ≤ vs < does not matter; for discrete variables it does.
- **"x or fewer" = F(x); "x or more" = 1−F(x−1)** (not 1−F(x)).
- **Standard normal use**: negative z → `1−N(|z|)`; one-tail vs two-tail critical values (1.645 is one-tail 95% *and* two-tail 90%).
- **Parameters**: normal needs μ and σ² (note: question may give σ), binomial n and p, lognormal the mean and variance of the *log*, uniform a and b.
- **Roy's criterion picks the max SFRatio, not the max return and not the min σ.** Shortfall probability is N(−SFRatio). R_L = threshold return, expressed as a *return* (3.75%), not a dollar amount.
- **Sharpe = SFRatio with R_L=R_F**; a Sharpe ratio tells you who minimizes P(return < R_F) only under normality.
- **Multivariate normal**: needs correlations; count them as n(n−1)/2.
- **Skew/kurtosis**: binomial is symmetric only at p=0.5 (p=0.1 gives right skew, p=0.9 left skew); normal has kurtosis 3.
- **Continuously compounded return < holding period return**; r=ln(1+HPR) and HPR=e^r−1.
- **Monte Carlo vs historical simulation**: MC = analyst-chosen distributions (supports what-if, parameter-sensitive); historical = real data, no what-if, misses unseen risks. Both give estimates, not exact values.
- **Random number generator** produces U(0,1); the inverse transform converts them to other distributions; the draws are pseudo-random (seed-dependent).
- **Table rounding**: expected answers may use the 2-decimal z-table (0.3594) while exact software gives 0.3581; choose the closest option.

## Key Takeaways
1. Pick the model first: binary counts → binomial; returns → normal; prices → lognormal; complex payoffs → simulation.
2. Every probability for a range is a cdf difference; for the normal, standardize and use symmetry.
3. Binomial mean np, variance np(1−p); always check independence and constant p before trusting it.
4. Use Roy's safety-first (maximize [E(R)−R_L]/σ) for floor-driven clients; shortfall probability is N(−SFRatio), and Sharpe is the special case R_L=R_F.
5. Log returns are additive and scale with √T; annualize daily volatility with √250; ST=S₀e^r gives lognormal prices when log returns are normal (approximately so even if not, by the CLT).
6. The lognormal mean exp(μ+½σ²) exceeds exp(μ); parameters refer to ln Y.
7. Normal underestimates tails (kurtosis>3); be cautious for options, daily data and VaR.
8. Monte Carlo = specify distributions → simulate → average (more trials = √ improvement); historical simulation = resample history; neither replaces an analytic formula when one exists.

## Connects To
- **ch 03**: probability concepts (combinations, expected value, independence) underlie binomial and joint-normal ideas.
- **ch 05**: CLT, standard error and the t-distribution extend the normal to estimation.
- **ch 06**: normal/t/chi-square/F critical values drive every hypothesis test.
- **ch 02**: skewness, kurtosis, mean-variance and Chebyshev reasoning for judging normality.
- **ch 07 / ch 09**: regression and time-series models assume normal errors and use log transformations.
- **`cfa-derivatives` ch 02**: binomial and risk-neutral pricing built on the binomial tree.
- **`cfa-portfolio-management` ch 05/06/08**: mean-variance portfolios, Sharpe ratio, VaR.
