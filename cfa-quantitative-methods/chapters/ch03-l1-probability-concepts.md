# Chapter 3: Probability Concepts
> **Source**: CFA Program Curriculum 2020, Level I, Reading 8 · Quantitative Methods | DeFusco, McLeavey, Pinto, Runkle

## Core Idea
Probability turns beliefs about an uncertain future into numbers that obey consistent rules: add for "or", multiply for "and", weight scenarios for totals, and reverse conditioning with Bayes' formula. Expected value, variance, covariance and correlation then give the inputs for portfolio expected return and risk, where co-movement (covariance) drives diversification.

## Learning Outcomes Covered
- define random variable, outcome, event, mutually exclusive and exhaustive events
- state the two defining properties of probability; distinguish empirical, subjective and a priori probabilities
- convert between probability and odds for / against
- distinguish unconditional vs conditional probability; apply multiplication, addition and total probability rules
- calculate joint probability, probability of "A or B", and joint probability of independent events
- distinguish dependent from independent events
- use conditional expectation and tree diagrams
- calculate covariance and correlation; interpret scatter plots
- calculate expected value, variance and standard deviation of a random variable and of portfolio returns
- calculate covariance from a joint probability function
- update a probability with Bayes' formula
- solve counting problems with factorial, combination and permutation rules

## Frameworks Introduced
- **Two defining properties of probability**: (1) `0 ≤ P(E) ≤ 1`; (2) probabilities of any set of mutually exclusive and exhaustive events sum to 1.
- **Three types of probability**: empirical (relative frequency from history, needs stable relationships), subjective (personal judgment, central to investing and Bayes), a priori (logical deduction, e.g. equally likely outcomes). Empirical and a priori are "objective" because they do not vary by person.
- **Odds and probability**:
  - Odds for E = `P(E)/[1 − P(E)]`; "a to b" for E means `P(E) = a/(a + b)`.
  - Odds against E = `[1 − P(E)]/P(E)`; "a to b" against means `P(E) = b/(a + b)`.
  - Dutch Book Theorem: inconsistent probabilities create riskless profit (pairs arbitrage: short the stock pricing in too high a chance, buy the one pricing in too low a chance).
- **Probability rules (the toolkit)**:
  - Conditional: `P(A|B) = P(AB)/P(B)`, P(B) ≠ 0.
  - Multiplication: `P(AB) = P(A|B)·P(B)`; independent events: `P(AB) = P(A)P(B)`.
  - Addition: `P(A or B) = P(A) + P(B) − P(AB)` (subtract the overlap; if mutually exclusive, P(AB) = 0).
  - Total probability: `P(A) = Σ P(A|Sᵢ)P(Sᵢ)` over mutually exclusive, exhaustive scenarios Sᵢ.
  - Total probability for expected value: `E(X) = Σ E(X|Sᵢ)P(Sᵢ)`.
  - When to use: build scenarios first (economic regimes, default/no default), estimate conditional probabilities inside each, then roll up.
- **Independence**: A, B independent iff `P(A|B) = P(A)`. Information about an independent event is useless for forecasting; information about a dependent event is useful. For random variables, independence means `P(X,Y) = P(X)P(Y)` for all pairs; independence is stronger than being uncorrelated (correlation captures only linear relation).
- **Tree diagram method**: branch on scenarios with conditional probabilities; each terminal node's unconditional probability is the product of branch probabilities; roll back with total probability for expectation.
- **Scenario technique for a default premium**: split into default / no default, compute the expected terminal value per 1 invested, set equal to the risk-free terminal value, solve the promised yield: `R = (1 + R_F)/(1 − P(default)) − 1` (zero recovery). Requires a larger premium if risk-averse or positive recovery is ignored.
- **Bayes' formula (inverse probability)**: `P(Event|Info) = [P(Info|Event)/P(Info)]·P(Event)`.
  - How: (1) list mutually exclusive, exhaustive events and priors; (2) assign likelihoods P(Info|Eventᵢ); (3) compute P(Info) with total probability; (4) posterior = likelihood × prior / P(Info); (5) check the posteriors sum to 1.
  - Why it works: the ratio P(Info|Event)/P(Info) is greater than 1 when the event makes the information more likely than it is on average. With equal (diffuse) priors the posterior equals the likelihood.
  - Failure mode: the answer is only as good as the priors and likelihoods; never confuse P(Info|Event) with P(Event|Info).
- **Portfolio expected return and variance (2-asset and n-asset)**: expected value is linear, `E(Rp) = Σ wᵢE(Rᵢ)`; variance needs the full covariance matrix, `σ²(Rp) = ΣΣ wᵢwⱼ Cov(Rᵢ,Rⱼ)`.
  - Inputs: n expected returns, n variances, n(n − 1)/2 distinct covariances.
  - Insight: with more holdings, off-diagonal covariances dominate (n variance terms vs n² − n covariance terms); diversification benefit grows as correlation falls below +1.
- **Counting decision tree**: (1) finite outcomes? (2) assign all n items to n slots: n!; (3) three or more labels: multinomial; (4) choose r of n, order irrelevant: combination; (5) order matters: permutation; (6) otherwise multiplication rule or enumeration.

## Key Concepts
- **Random variable**: a quantity whose outcomes are uncertain (e.g. next year's return).
- **Event**: a specified set of outcomes (one outcome or many).
- **Mutually exclusive / exhaustive**: only one can occur at a time / together they cover all outcomes.
- **Unconditional (marginal) probability**: P(A) with no restriction.
- **Conditional probability**: P(A|B), probability of A given B has occurred.
- **Joint probability**: P(AB), both occur.
- **Complement**: Aᶜ, "not A"; P(A) + P(Aᶜ) = 1.
- **Prior / likelihood / posterior**: belief before information / probability of the information given an event / belief after updating.
- **Expected value**: probability-weighted average of outcomes; a forecast or population mean, as opposed to a historical sample mean.
- **Variance / standard deviation**: probability-weighted squared deviation from E(X) / its positive square root; zero variance means no randomness.
- **Conditional expected value**: `E(X|S) = ΣP(Xᵢ|S)Xᵢ`; revises a forecast when information (scenario) arrives.
- **Covariance**: probability-weighted product of deviations of two variables from their means; sign shows direction, units are hard to read; Cov(R,R) = σ²(R).
- **Correlation**: `ρ = Cov/(σᵢσⱼ)`, unit-free, between −1 and +1; measures linear association only.
- **Joint probability function**: P(X,Y), the probability of each pair of values.
- **Scatter plot**: points of paired observations; shows nonlinear patterns and outliers that a single correlation hides.
- **Spurious correlation**: apparent association from chance, from dividing two variables by a third, or from a common third driver.
- **Factorial / combination / permutation / multinomial**: counting tools for orderings, unordered selections, ordered selections, and labelings.

## Formulas & Reference Tables
Symbols: P probability, E expected value, wᵢ portfolio weight (Σwᵢ = 1), σ standard deviation, ρ correlation.

| Quantity | Formula |
|---|---|
| Conditional probability | `P(A|B) = P(AB)/P(B)` |
| Multiplication rule | `P(AB) = P(A|B)P(B) = P(B|A)P(A)` |
| Independent events | `P(AB) = P(A)P(B)`; k independent events: product of all |
| Addition rule | `P(A or B) = P(A) + P(B) − P(AB)` |
| Total probability (2 scenarios) | `P(A) = P(A|S)P(S) + P(A|Sᶜ)P(Sᶜ)` |
| Total probability (n scenarios) | `P(A) = Σᵢ P(A|Sᵢ)P(Sᵢ)` |
| Odds for / against | `P/(1−P)` ; `(1−P)/P` |
| Expected value | `E(X) = ΣP(Xᵢ)Xᵢ` |
| Variance | `σ²(X) = E{[X − E(X)]²} = ΣP(Xᵢ)[Xᵢ − E(X)]²` |
| Conditional expected value | `E(X|S) = ΣP(Xᵢ|S)Xᵢ` |
| Total probability, expected value | `E(X) = ΣE(X|Sᵢ)P(Sᵢ)` |
| Variance decomposition (footnote) | `σ²(X) = E[σ²(X|S)] + σ²[E(X|S)]` |
| Covariance (forward-looking) | `Cov(Rᵢ,Rⱼ) = E{[Rᵢ − E(Rᵢ)][Rⱼ − E(Rⱼ)]}` |
| Covariance (joint probabilities) | `Cov = ΣᵢΣⱼ P(Rᵢ,Rⱼ)[Rᵢ − E(Rᵢ)][Rⱼ − E(Rⱼ)]` |
| Sample covariance | `Σ(Rᵢ,t − R̄ᵢ)(Rⱼ,t − R̄ⱼ)/(n − 1)` |
| Correlation | `ρᵢⱼ = Cov(Rᵢ,Rⱼ)/(σᵢσⱼ)`; `Cov = ρσᵢσⱼ` |
| Expected value properties | `E(wR) = wE(R)`; `E(Σwᵢ Rᵢ) = ΣwᵢE(Rᵢ)`; `E(XY) = E(X)E(Y)` if uncorrelated |
| Variance properties | `σ²(wR) = w²σ²(R)`; `σ²(c + R) = σ²(R)`; Cov(constant, R) = 0 |
| Portfolio expected return | `E(Rp) = Σ wᵢE(Rᵢ)` |
| Portfolio variance (general) | `σ²(Rp) = Σᵢ Σⱼ wᵢwⱼ Cov(Rᵢ,Rⱼ)` |
| Portfolio variance (2 assets) | `σ²(Rp) = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρ₁₂σ₁σ₂` |
| Number of distinct covariances | `n(n − 1)/2` |
| Multiplication rule of counting | `n₁ × n₂ × … × n_k` |
| Factorial | `n! = n(n−1)…1`, `0! = 1` |
| Multinomial | `n!/(n₁!n₂!…n_k!)` |
| Combination | `nCr = n!/[(n−r)!r!]`; symmetric: nCr = nC(n−r) |
| Permutation | `nPr = n!/(n−r)!` |
| Bayes' formula | `P(E|I) = [P(I|E)/P(I)]P(E)` ; `P(I) = ΣP(I|Eᵢ)P(Eᵢ)` |
| Default-risk yield (zero recovery, 1 period) | `R = (1 + R_F)/(1 − P(default)) − 1` |

Interpretation table:

| Correlation / covariance | Meaning for a two-asset portfolio |
|---|---|
| ρ = +1 | no diversification; σp = w₁σ₁ + w₂σ₂ |
| 0 < ρ < 1 | partial diversification |
| ρ = 0 | variance = sum of weighted variances |
| ρ < 0 | strong risk reduction at the same expected return |
| ρ = −1 | variance can reach 0 with suitable weights |

## Mental Models
- **Probabilities must be consistent, or someone can arbitrage you.** Conditional, joint and unconditional probabilities (and expected values) have to reconcile through the total probability rule; check any set of beliefs this way.
- **Total probability is a weighted average over scenarios.** Same structure as portfolio return: scenario probabilities are the weights and they sum to 1.
- **Bayes reverses the arrow**: from "if X then data" to "given data, how likely X". Start with the priors, ask how surprising the data would be under each hypothesis, normalize.
- **Correlation tells direction and linearity, not causation or dependence.** Y = (X − 4)² has zero correlation with X yet is perfectly dependent; plot the scatter and check outliers.
- **Covariance is the lever of diversification.** Variances are the same whatever the weights; the benefit comes from the cross-terms, which grow quadratically in number as assets are added.
- **Expected value is linear, variance is not.** Portfolio expected return needs only weights and means; portfolio risk needs the whole covariance matrix.
- **Independent screens multiply**: five lenient criteria can leave 2% of the universe; stacking filters shrinks the candidate list fast.

## Worked Example
**A. Portfolio expected return, variance and diversification.** Weights 50% S&P 500, 25% US long-term corporate bonds, 25% MSCI EAFE; expected returns 13%, 6%, 15%; covariance matrix (%²): variances 400, 81, 441; Cov(S&P, bonds) = 45, Cov(S&P, EAFE) = 189, Cov(bonds, EAFE) = 38.
1. `E(Rp) = 0.5(13) + 0.25(6) + 0.25(15) = 11.75%`.
2. `σ²p = 0.5²(400) + 0.25²(81) + 0.25²(441) + 2(0.5)(0.25)(45) + 2(0.5)(0.25)(189) + 2(0.25)(0.25)(38) = 100 + 5.0625 + 27.5625 + 11.25 + 47.25 + 4.75 = 195.875`.
3. `σp = √195.875 = 14.0%`. With zero covariances the SD would be √132.625 = 11.5%, so the positive covariances cost 2.5 points of risk; negative covariances would push it lower at unchanged expected return.
4. Correlations: bonds-EAFE `38/(9 × 21) = 0.20`; S&P-bonds 0.25; S&P-EAFE 0.45.

**B. Bayes (earnings surprise).** Priors: beat 0.45, meet 0.30, miss 0.25. Likelihood of a capacity-expansion announcement: 0.75, 0.20, 0.05. `P(expands) = 0.75(0.45) + 0.20(0.30) + 0.05(0.25) = 0.41`. Posteriors: beat `0.75/0.41 × 0.45 = 0.8232`; meet `0.1463`; miss `0.0305`; sum 1.0000. The news lifts the beat probability from 45% to 82%.

**C. Total probability and conditional expectation (EPS).** Declining rates (prob 0.60): EPS 2.60 w.p. 0.25, 2.45 w.p. 0.75, so `E(EPS|decline) = 2.4875`. Stable rates (0.40): EPS 2.20 w.p. 0.60, 2.00 w.p. 0.40, so `E(EPS|stable) = 2.12`. `E(EPS) = 0.6(2.4875) + 0.4(2.12) = 2.3405`; variance 0.038785, SD 0.197.

**D. Two-fund portfolio.** 75% fund A (E = 20%, σ = 25%) and 25% fund B (E = 12%, σ = 14%), Cov = 120. `ρ = 120/(25 × 14) = 0.34`; `E(Rp) = 18%`; `σ²p = 351.5625 + 12.25 + 45 = 408.8125`, `σp = 20.22%`.

## Anti-patterns
- **Confusing P(A|B) with P(B|A)**: base-rate neglect; use Bayes with the unconditional P(Info).
- **Adding probabilities of overlapping events**: `P(A or B) = P(A) + P(B)` only for mutually exclusive events, otherwise subtract P(AB).
- **Multiplying probabilities of dependent events without conditioning**: `P(AB) = P(A)P(B)` is valid only under independence.
- **Using scenarios that overlap or omit outcomes**: the total probability rule requires mutually exclusive and exhaustive scenarios.
- **Treating zero correlation as independence**: nonlinear dependence is invisible to correlation.
- **Reading a high correlation as a causal or tradable relation**: check for spurious correlation and outliers before building a strategy.
- **Computing portfolio risk as a weighted average of SDs**: valid only at ρ = +1.
- **Forgetting the covariance cross-terms factor of 2** in the 2-asset formula, or using SD instead of variance in the matrix.
- **Using sample covariance (n − 1) as if it were forward-looking**, or mixing percent and decimal units in the same calculation.
- **Anchoring on a historical empirical probability for a regime shift or rare event**: adjust subjectively when relationships change.

## Exam Focus & Traps
- Odds to probability: "1 to 7 for" gives 1/8; "15 to 1 against" gives 1/16 (probability of the event is b/(a + b) for odds against).
- Independence test and shortcut: if screens are independent, multiply fractions (e.g. 0.20 × 0.45 × 0.78 × 500 = 35.1 companies, about 35).
- Solving for an unknown conditional probability with total probability: `0.55 = P(A|S)(0.55) + 0.40(0.45)` gives P(A|S) = 0.673.
- Bayes problem pattern: given P(nonsurvivor) 0.40, P(pass) 0.55, P(pass|survivor) 0.85: first solve `P(pass|nonsurvivor) = (0.55 − 0.85 × 0.60)/0.40 = 0.10`; then `P(survivor|pass) = 0.51/0.55 = 0.927`; `P(nonsurvivor|fail) = 0.40 × 0.90/0.45 = 0.80`. A test that gives 0.927 vs a 0.60 prior and 0.80 vs 0.40 is effective.
- Expected recovery with two-stage tree: multiply branch probabilities to get joint probabilities (e.g. 0.75 × 0.45 = 0.3375), expected value = 0.755 per 1 in the textbook problem; and $63,600 for the 100,000 loan problem (0.4 × 42,000 + 0.6 × 78,000).
- Covariance from correlation: `Cov = ρσ₁σ₂` (0.24 × 0.64 × 0.56 = 0.086).
- Positive covariance means returns tend to be on the same side of their means at the same time, not equal expected values.
- Permutation vs combination: "rank the first three of five" is 5P3 = 60; "choose three of five" is 5C3 = 10; labeling 18 funds into 5 risk groups of 4, 4, 3, 4, 3 is 12,864,852,000.
- Units: variance in percent-squared; 400 (%²) = 0.0400 as a decimal. Do not mix.
- The conditional probability can be greater than, equal to or less than the unconditional probability.
- Unconditional variance of EPS = expected conditional variance + variance of conditional means (0.006371 + 0.032414 = 0.038785).

## Key Takeaways
1. Frame problems as mutually exclusive, exhaustive scenarios, then use the multiplication, addition and total probability rules.
2. `P(A or B)` subtracts the overlap; `P(AB)` multiplies only for independent events.
3. Keep probabilities and expected values internally consistent; inconsistency is an arbitrage opportunity (Dutch Book).
4. Expected value is a probability-weighted average (linear); variance of a portfolio requires the covariance matrix and the factor 2 on cross-terms.
5. Correlation = Cov/(σσ), bounded in [−1, +1], linear only; always inspect scatter plots for outliers and nonlinearity.
6. Diversification benefit increases as correlation decreases; with ρ < 1 portfolio SD is below the weighted-average SD.
7. Bayes: posterior = likelihood/unconditional × prior; compute the unconditional with total probability and verify posteriors sum to 1.
8. Pick the counting tool by whether all items are used, how many labels there are, and whether order matters: n!, multinomial, combination, permutation.

## Connects To
- **ch 02**: sample statistics (mean, variance, skewness) estimate the probabilistic quantities defined here.
- **ch 04**: probability distributions (binomial uses nCr, normal, lognormal) build on random variables and expectation.
- **ch 05**: sampling distribution and standard error rely on independence and variance of sums.
- **ch 06**: hypothesis testing uses conditional probabilities (Type I/II errors) and Bayesian reasoning.
- **ch 07**: regression builds on covariance and correlation; `Cov/σ²` is the slope.
- **`cfa-portfolio-management` ch 05**: portfolio risk and return, diversification, and the efficient frontier use the formulas here.
- **`cfa-fixed-income` ch 06**: default probability and expected loss use the scenario default-premium logic.
- **`cfa-derivatives` ch 04**: binomial option pricing uses combinations and probability-weighted expectations.
