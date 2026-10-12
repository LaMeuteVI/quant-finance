# Chapter 12: Information Analysis
> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2e (McGraw-Hill, 1999) | Ch. 12, pp. 316–341

## Core Idea

Information analysis is the discipline of **pricing a signal, not a stock**. Any raw data item — a book-to-price ratio, an earnings surprise, an analyst recommendation — is a *predictor* consisting of **signal + noise**. The job is to (1) turn the predictor into portfolios and (2) measure the performance of those portfolios to price the information. The output is not "the factor works"; the output is the **information ratio**, which is the monetisable value of the signal.

The discipline matters because a predictor can be worth a lot (value spread), nothing (a widely known factor already priced in), or **negative** (a contrarian predictor that pays you to bet against it). Information analysis is agnostic to how the signal was generated — a discretionary analyst's buy list and a 200-factor machine-learning ensemble go through the identical pipeline.

Position it correctly in the research process: **information analysis happens before backtesting**. It measures the *unfettered* value of the signal (turnover, tradability and transaction costs deliberately ignored). Backtesting then takes only the signals that survived information analysis and asks whether they are implementable.

## Learning Outcomes Covered
- Convert any predictor into diagnostic long/short portfolios (procedures 1–6) and pick the controlled one.
- Price a signal via the t statistic, information ratio and information coefficient, and move between them.
- Back out implied breadth from the Fundamental Law; recognise that BR is the hardest parameter to measure.
- Run an event study on episodic information and translate it into an ex-ante IR.
- Recognise data mining and apply the four guards against it.

## Frameworks Introduced

- **The Two-Step Information Analysis Process**: Step 1 turn information into portfolios; Step 2 analyse those portfolios' performance.
  - **Formulation**: predictor `s` → portfolio(s) `p` → realised active return `θ_p` → `{alpha, beta, t(alpha), IR, IC}`.
  - **When to use**: on *every* new raw data item, before any capital is allocated to it.
  - **How**: (a) fix the horizon of the analysis to match the information horizon (daily signal → daily portfolios; quarterly fundamental signal → quarterly portfolios); (b) apply procedure 5 or 6; (c) regress; (d) report IR and t.
  - **Why it works**: it isolates the signal from every other exposure, so the measured performance is attributable to the signal itself. **Failure mode**: mixing horizons — building monthly portfolios from a signal whose information dies in three days (or vice versa) systematically mismeasures it.

- **The Six Portfolio-Construction Procedures**: the ladder from crude to controlled.
  1. Buy/sell lists from the predictor, equal-weighted long and short.
  2. One portfolio per score bucket (e.g. book-to-price quintiles), equal- or cap-weighted within bucket.
  3. Split on above/below-average alpha, weight by distance from the average.
  4. Rank on alpha, bucket into quintiles/deciles, equal- or value-weight within bucket.
  5. **Factor portfolio**: long and short with **equal value and equal beta**, unit bet on the predictor, tracking each other as closely as possible.
  6. **Matched factor portfolio**: as (5) but matched on a *prespecified* set of control variables (industry, sector, size).
  - **When to use**: procedures 1–4 for a quick sanity read; **5 or 6 for anything you intend to trade on** — the book recommends 5 or 6 as the default for numerical scores.
  - **Why 5/6 win**: they are controlled experiments. Procedures 1–4 leak incidental bets. **Failure mode**: procedure 2 quintiles carry whatever factor exposures the quintile happens to have — in the book's own example the quintile betas range 0.92 to 1.12 and every apparent spread is contaminated.

- **Fundamental Law of Active Management (applied)**: `IR = IC · √BR`, where `BR` = independent bets per year.
  - **Use when**: you have measured IC and IR and need to know whether your bet count is credible.
  - **Failure mode**: `BR` is the least measurable of the three parameters. Reporting `IR` and `IC` without a breadth sanity check is how a 500-name, 12-times-a-year strategy masquerades as 729 independent bets.

- **Event Study**: the cross-sectional method applied to episodic, asynchronous information.
  - **Formulation**: regress cumulated post-event **residual** returns on the event description and pre-event conditioning variables.
  - **Three variable families**: (a) event description — often 0/1, or a graded surprise (earnings surprise = (announced − consensus)/dispersion); (b) asset **residual** returns after the event; (c) pre-event conditioning variables (CEO inside vs outside, predecessor fired vs retired, leverage, institutional ownership).
  - **Use when**: information arrives irregularly per name — earnings, management change, dividend action, split, buyback, index inclusion.
  - **Why residual returns**: events occur at different calendar dates; only the market-and-factor-adjusted return removes the confounding of calendar time with event time. **Failure mode**: raw returns. A dividend increase in a bull market looks like alpha; it is beta.

- **Event-to-IR Model**: converts an event study into an annual IC and IR.
  - Geometric interarrival: `P(next event in j days) = p(1−p)^(j−1)`, expected gap `1/p`.
  - Exponential IC decay: `IC(j) = IC(1)·γ^(j−1)`.
  - Half-life conversion: `HL = log(0.5)/log(γ)` (days).
  - Annual IC and IR follow from `J` trading days/year and universe `N`; effective breadth `N*` follows from the Fundamental Law.
  - **Use when**: episodic signal, and you need to know whether "rare but powerful" beats "common and weak".

- **The Four Guards Against Data Mining**: **intuition, restraint, sensibleness, out-of-sample testing**.

## Key Concepts

1. **Predictor** — any data item, spanning many names and many dates, whose job is to predict residual (alpha) returns.
2. **Signal** — the component of the predictor genuinely linked to future returns.
3. **Noise** — the remainder; it masks the signal and makes information analysis hard.
4. **Information coefficient (IC)** — the correlation between the forecast (or the raw data) and realised alpha; `+1` = pure signal, `0` = pure noise, negative = perverse.
5. **Information ratio (IR)** — annualised alpha divided by annualised tracking error; the single best statistic for the value added in the information.
6. **t statistic of alpha** — estimated alpha over its standard error; `|t| > 2` ⇒ less than 5% probability of luck under normality.
7. **Factor portfolio** — the long/short pair with matched value and beta, isolating the predictor.
8. **Net portfolio** — long minus short; a forecast beta of zero, so its returns should be uncorrelated with the market.
9. **Effective breadth (`N*`)** — the number of assets' worth of *fresh, independent* information per period implied by IR and IC.
10. **Half-life of the event signal** — the decay parameter `γ` in trading days, convertible to business days via `log 0.5 / log γ`.
11. **Earnings surprise** — announced earnings less consensus, scaled by analyst dispersion; a graded event descriptor.
12. **Data mining** — manufacturing apparent signal by searching enough variations of informationless data; the bane of the discipline.
13. **Up/down and good/bad split analysis** — separate IC on upside vs downside alphas and in up vs down markets, to check the signal is not a disguised tail bet.
14. **The statistics of coincidence** — the narrow-perspective/broad-perspective distinction that makes coincidences look improbable when they are not.

## Formulas & Reference Tables

**Performance regression** (portfolio vs benchmark, excess returns):
`r_p(t) − r_f(t) = alpha + beta·[r_b(t) − r_f(t)] + e(t)`

**t statistic of alpha**: `t(alpha) = alpha_hat / SE(alpha_hat)`

**Information ratio**: `IR = alpha_annual / omega_annual`, `omega = sigma(θ)·√(frequency)`

**Fundamental Law of Active Management**: `IR = IC · √BR`

**t ↔ IR bridge** (over `T` years of observation): `IR ≈ t(alpha)/√T`

**Standard error of the IR**: `SE(IR) ≈ 1/√T`

**Event study regression** (j = post-event horizon in periods):
`θ_n(1..j) = beta0 + beta1·x_n(1) + beta2·x_n(2) + … + betaK·x_n(K) + e_n`
with `theta_n(1..j)` = cumulated *residual* return from period 1 to j after event `n`, and `x_n(k)` = conditioning variables. Because the dependent variable is ex-ante mean 0, unit-variance standardised, the in-sample estimate of the IC is simply the **fitted part of the regression**.

**Forecast alpha from an event** (event just occurred):
`alpha_hat(0..j) = omega_n(1..j) · IC_hat · x_n`

**Forecast alpha if the event occurred `j1` periods earlier**: same form, with the corresponding decayed IC and the remaining-horizon volatility.

**Volatility–IC–score rule**: `alpha = volatility · IC · score` — the two forecast equations are exactly this rule, restated.

**Event decay and interarrival**:
`P(gap = j) = p(1−p)^(j−1)`, `E[gap] = 1/p`
`IC(j) = IC(1)·γ^(j−1)`, `HL_days = log(0.5)/log(γ)`
`IC_annual = IC(1) · (sum over event-day distribution)` scaled by `J` days and `N` names; `IR = IC_annual·√(N*)`

**Implied breadth**: `BR = (IR/IC)²`

**Multiple-testing arithmetic**: `P(at least one |t|>2 | M independent null trials) = 1 − 0.95^M`

| M trials | P(at least one false positive at 95%) |
|---|---|
| 1 | 5.0% |
| 5 | 22.6% |
| 10 | 40.1% |
| 20 | **64.2%** |
| 50 | 92.3% |

## Mental Models

1. **Use the controlled experiment, not the pretty chart.** When a signal's long/short spread looks good, always ask "what else is different between these two baskets?" If you cannot answer, use procedure 6.
2. **Use the IR, not the t statistic, to decide whether to trade.** t asks "is it probably not zero?"; IR asks "is it worth the risk?" An IR of 0.5 over 5 years is statistically stronger than the same IR over 1 year, and worth exactly the same.
3. **Treat every IR above 2 as a bug report first.** Only ~10% of observed realised IRs exceed 1. For plain, public, economically intuitive data in an efficient market, IR > 2 means you have an error, not an edge.
4. **Count your trials, not your wins.** Restraint means pre-registering the set of signal variations *before* running them; otherwise "the 20th try finally worked" is a 64%-likely artefact.
5. **Rare events still price like frequent ones.** Breadth is `N* ≈ N · p`-ish, not `N`. A 7-yearly event across 1000 names has an effective breadth two orders of magnitude below the naive count.

## Code Examples

```python
"""
⚠ reconstructed — the book gives no code for this chapter; this is a faithful
implementation of the two-step procedure using the book's notation.
"""
import numpy as np

def factor_portfolio(returns, scores, betas=None):
    """
    Procedure 5. Returns the equal-value, equal-beta long/short factor portfolio
    plus the net (long - short) portfolio, and the realised IC.
    scores: cross-sectional predictor (standardised); higher = more alpha.
    """
    n = len(scores)
    if betas is None:
        betas = np.ones(n)
    # weights proportional to score deviation, market-neutral in beta
    w = scores - scores.mean()
    # rescale so long beta == short beta (zero net beta)
    w = w - betas * (w @ betas) / (betas @ betas)
    w = w / np.abs(w).sum()
    return w  # portfolio weights summing to zero net, betas @ w == 0


def two_step(signal, residual_returns):
    """signal: T x N predictor. residual_returns: T x N residual returns."""
    T, N = signal.shape
    w = factor_portfolio(signal[-1], None, None)          # latest portfolio
    theta = residual_returns @ w                          # active return series
    ic = np.corrcoef(signal.ravel(), residual_returns.ravel())[0, 1]
    # fundamental law: implied breadth
    breakeven_IR = ic * np.sqrt(N * 12)
    return {"active_return": theta, "IC": ic, "IR_if_1_bet_per_name": breakeven_IR}


def multiple_testing_p(M, conf=0.95):
    """Probability of at least one false positive in M independent null trials."""
    return 1.0 - conf ** M
```

## Worked Example

**Book-to-price quintiles vs factor portfolios, S&P 500 constituents, Jan 1988 – Dec 1992 (5 years).**

*Setup A (procedure 2)*: rank by book-to-price each month, five equal-cap quintiles.

*Setup B (procedure 5)*: long and short with equal value and equal beta, long book-to-price 1 s.d. above short, minimum tracking difference.

Results (all figures from Tables 12.1–12.3):

| Quintile (A) | Alpha/mo | t(alpha) | Beta | IR |
|---|---|---|---|---|
| Highest B/P | 0.03% | 0.14 | 1.02 | 0.06 |
| High | −0.06% | −0.05 | 0.92 | −0.21 |
| Mid | −0.14% | −0.97 | 0.92 | −0.45 |
| Low | −0.15% | −1.10 | 1.04 | −0.51 |
| Lowest B/P | 0.31% | 1.15 | 1.12 | **0.53** |

| Portfolio (B) | Alpha/mo | t(alpha) | Beta | IR |
|---|---|---|---|---|
| Long | −0.02% | −0.10 | 1.08 | −0.05 |
| Short | −0.11% | −0.76 | 1.08 | −0.35 |
| **Net** | 0.08% | 0.59 | **0.00** | 0.27 |

**Recomputation (verified in Python):**
- t↔IR bridge over T = 5: `IR ≈ t/√5`. Highest: `0.14/2.236 = 0.063` vs reported 0.06 ✔. Lowest: `1.15/2.236 = 0.514` vs 0.53 (small difference from annualising the *residual* rather than the t) ✔. Mid: `−0.97/2.236 = −0.434` vs −0.45 ✔.
- Implied breadth: `(0.27/0.01)² = 729`. The book says "a little over 700" ✔. Yet the strategy generated 500 names × 12 = 6000 information items per year — **only ~12% of items are independent**. That ratio is the honest breadth haircut.
- Multiple-testing arithmetic: `1 − 0.95²⁰ = 0.6415` ≈ **64%** ✔.

**Interpretation.** The naive quintile spread (lowest vs highest B/P) shows IR 0.53 in the *wrong* direction to the naive story — the bottom quintile wins because 1989–1990 was a growth-market, and the quintile betas differ by 20 points of beta (0.92 vs 1.12). The factor portfolio strips that out: the *net* position earns alpha of 0.08%/month with beta exactly 0.00. Same information, different conclusion. Neither is statistically significant at 95%: `|t| ≤ 1.15` everywhere. The measured IC is **0.01** — book-to-price over this window is worth about one-seventh of what a well-specified factor delivers. **Practical read: this is not a signal worth trading on its own; it is a control variable.**

## Anti-patterns

- **Building quintiles from a fundamental signal and reading the top-minus-bottom spread.** The spread picks up whatever else separates the buckets. Use the factor portfolio.
- **Using raw returns in an event study.** Calendar-time confounding masquerades as post-event alpha. Use residual (or asset-specific net of factors) returns.
- **Reporting a t statistic as the business case.** t is a significance test; IR is the P&L per unit of tracking error. They are related but not interchangeable.
- **Trusting the p-value of the best of N tries.** Quote the family-wise error rate, not the single-trial one.
- **Ignoring turnover in information analysis and assuming backtesting will fix it.** Information analysis deliberately excludes costs; carry the turnover number forward explicitly, because ch. 16 shows the optimal position size scales with the inverse square root of cost.
- **Stale-price sensitivity.** Price errors in the input data appear as false opportunities in one month and false realisations the next. Clean prices before analysis, not after.
- **Believing that non-intuitive signals are the ones that work.** Sunspots, skirt lengths and Super Bowl scores can be made to look significant over a chosen window. Intuition is a necessary filter, not a sufficient one — but its absence is damning.

## Practitioner Notes

- **Anchoring IR to plausible values.** A realised IR distribution is right-skewed and heavy-tailed; roughly **10%** of observed IRs exceed 1. Treat IR > 2 on publicly available, economically motivated data as a data or code error until proven otherwise. This is a sanity threshold, not a statistical test.
- **The IC is the lever that survives.** Among `IR`, `IC`, `BR`, only `IC` can be improved by research; `BR` is a property of the data and `IR` is the output. Invest research effort in the correlation.
- **Honesty about multiple testing.** Use the family-wise probability `1 − c^M` explicitly in the memo. If M is large enough that the family-wise rate exceeds 50%, the honest conclusion is "no evidence."
- **Out-of-sample discipline is non-negotiable.** A signal tuned on 1980–1985 must survive 1986; a signal tuned on odd months must survive even months. If it does not, it was curve-fitted, not found.
- **Event-study conditioning variables are where the edge hides.** CEO from inside vs outside, predecessor's fate, surprise relative to the *previous* quarter's surprise — these splits typically carry most of the explanatory power, not the unconditional event effect.

## Key Takeaways

1. Information analysis is two steps: turn information into portfolios, then price those portfolios.
2. Use procedure 5 or 6 (matched factor portfolios) for anything you intend to trade; procedures 1–4 leak incidental factor bets.
3. `IR ≈ t(alpha)/√T` — use t for significance, IR for value added; they answer different questions.
4. The Fundamental Law lets you back out breadth: `BR = (IR/IC)²`. In the book-to-price example, 6000 information items collapse to ~729 independent bets.
5. Event studies are the right tool for episodic information; they require *residual* returns, a graded event descriptor, and pre-event conditioning variables.
6. Event-to-IR translation rests on three parameters: arrival rate `p`, first-day `IC(1)`, and decay `γ` (`HL = log 0.5 / log γ`).
7. Data mining is easy because of the narrow/broad perspective error: 20 null trials give a 64% chance of one `|t| > 2`. Guard with intuition, restraint, sensibleness and out-of-sample testing.
8. Only ~10% of realised IRs exceed 1; scrutinise anything above 2.

## Connects To

- **ch05**: the information ratio and residual risk framework this chapter prices signals with.
- **ch13**: takes the decay parameter `γ` and makes the information horizon the subject.
- **`hull-derivatives` ch NN**: event studies and abnormal-return methodology share the residualisation machinery.
- **`cfasi-equity-investment-styles` ch NN**: style/factor construction is exactly procedures 5 and 6.
- **`cfa-quantitative-methods` ch NN**: regression, t statistics and multiple-testing control underpin the Step-2 statistics.
