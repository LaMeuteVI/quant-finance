# Chapter 5: Portfolio Risk and Return: Part I
> **Source**: CFA Program Curriculum 2020, Level I, Reading 52 · Portfolio Management | Vijay Singal, PhD, CFA

## Core Idea
Portfolio construction is a two-step problem: measure return and risk correctly (which return measure for which purpose, and why mean and variance are only part of the story), then use correlation to combine assets so that risk falls faster than return. Add a risk-free asset and the whole problem collapses to one optimal risky portfolio plus an investor-specific lending/borrowing decision (two-fund separation), chosen by tangency of the investor's indifference curve with the capital allocation line.

## Learning Outcomes Covered
- Calculate and interpret major return measures (holding period, arithmetic, geometric, money-weighted, time-weighted, annualized, gross/net, pre/after-tax, nominal/real, leveraged) and their uses
- Compare money-weighted and time-weighted returns and evaluate performance with them
- Describe characteristics of major asset classes (risk, return, correlation, skewness, kurtosis, liquidity)
- Calculate and interpret mean, variance, covariance, correlation from historical data
- Explain risk aversion and its implications for portfolio selection (utility, indifference curves)
- Calculate and interpret portfolio standard deviation; describe diversification with imperfect correlation
- Describe the minimum-variance frontier, global minimum-variance portfolio, Markowitz efficient frontier
- Select the optimal portfolio from investor utility and the capital allocation line

## Frameworks Introduced
- **Return-measure selection (which return for which job)**:
  - When to use: before quoting or comparing any performance number.
  - How: single predefined period → holding period return (HPR); multi-period asset behavior → geometric mean (true compound growth); statistical inference/forecast of one period → arithmetic mean; evaluating what an investor actually earned given own deposits/withdrawals → money-weighted return (IRR); evaluating a manager who does not control flows → time-weighted return (TWR); comparing different horizons → annualize; comparing managers' skill → gross return; what the client keeps → net, after-tax, real.
  - Why it works / failure mode: arithmetic mean is biased upward vs. realized wealth growth when returns vary (the −50%, +35%, +27% path has arithmetic mean 4% but ends at 0.8573, i.e. −5.0%/yr geometric). Using IRR to rate a manager penalizes or rewards him for the client's timing.
- **Mean-variance utility function**: `U = E(r) − ½Aσ²`
  - When to use: ranking risky alternatives for one investor; deriving the optimal point on the CAL.
  - How: put E(r) and σ in decimals; pick the A that matches investor risk aversion (A > 0 averse, 0 neutral, < 0 seeking); compute U for every candidate; choose max. A risk-free asset (σ² = 0) gives U = Rf for everyone, so U is also the "certainty equivalent" return.
  - Why it works / failure mode: only the ordering of U matters (U = 4 is not "twice as good" as U = 2), and U is not comparable across investors. It ignores skewness and kurtosis.
- **Capital allocation line (CAL) and two-fund separation**: `E(Rp) = Rf + [(E(Ri) − Rf)/σi] × σp`
  - When to use: investor can mix a risk-free asset with a risky portfolio.
  - How: (1) find the single optimal risky portfolio P as the CAL tangent to the efficient frontier (max Sharpe ratio) – identical for all investors; (2) choose each investor's mix on CAL(P) by tangency with the investor's indifference curve (lending left of P, borrowing right of P).
  - Why it works / failure mode: separates the investment decision (P) from the financing decision (how much Rf). Requires borrowing = lending rate and the same inputs for everyone; with a higher borrowing rate the CAL kinks beyond P.
- **Markowitz efficient frontier construction**: opportunity set → minimum-variance frontier → keep the part above the global minimum-variance portfolio (GMVP).
  - When to use: risky-asset-only portfolio selection.
  - How: for each target return find the minimum-variance portfolio; the curve's leftmost point is the GMVP; the upper arm is efficient, the lower arm is dominated (same σ, lower return).
- **Add-an-asset test**: add a new asset to portfolio P only if `E(Rnew) > Rf + (σnew ρnew,p / σp)[E(Rp) − Rf]`, equivalently `Sharpe_new > Sharpe_p × ρnew,p`.
  - When to use: deciding whether a candidate asset improves an existing portfolio.
  - How: compute the new asset's Sharpe ratio, compare to the portfolio Sharpe times its correlation with the portfolio. Low correlation lowers the hurdle; a negatively correlated asset can be worth adding even with a low or negative Sharpe.

## Key Concepts
- **Holding period return (HPR)**: total return over one specified period, `(P₁ − P₀ + I₁)/P₀`, = capital gain yield + income yield.
- **Arithmetic (mean) return**: simple average of period returns; easy statistics, but biased upward as a measure of compound growth.
- **Geometric mean return**: `[Π(1+Rt)]^(1/T) − 1`; the compound growth rate; never larger than the arithmetic mean (equal only if all returns are equal).
- **Money-weighted return (MWR)**: the IRR of the investor's cash flows (contributions negative, withdrawals and terminal value positive); reflects the size and timing of flows.
- **Time-weighted return (TWR)**: compound growth of $1 invested; value the portfolio at every external flow, compute subperiod HPRs, link them geometrically; neutralizes flows.
- **Annualized return**: `(1 + r_period)^c − 1` with c = periods per year (c < 1 for periods longer than a year); assumes the return is repeatable, which is its main limitation.
- **Gross return vs. net return**: gross is before management, custody, and administration fees (but after trading costs) and evaluates skill; net is after all fees and expenses and evaluates what the investor receives.
- **Real return**: nominal return stripped of inflation, `(1+r)/(1+π) − 1`; taxes are applied to the nominal return first, inflation after.
- **Leveraged return**: return on own equity when a position exceeds own capital (futures margin or borrowing); gains and losses are amplified, and interest on borrowing is deducted.
- **Expected return vs. historical mean**: expected is forward-looking `(1+E(R)) = (1+rrF)(1+E(π))(1+E(RP))`; historical mean is a (noisy) proxy.
- **Skewness / kurtosis**: asymmetry of the return distribution / fat tails; mean-variance ignores both, so investors supplement with VaR and conditional tail expectations.
- **Risk aversion (A) / risk tolerance**: A is the marginal return required per unit of added variance; tolerance is its inverse.
- **Indifference curve**: locus of (σ, E(R)) pairs giving the same utility; upward sloping and convex for the risk-averse, steeper = more risk averse, horizontal for risk-neutral, downward sloping for risk-seeking; never cross.
- **Covariance / correlation**: `Cov = ρσ₁σ₂`; correlation is bounded [−1, +1] and interpretable, covariance is not.
- **Investment opportunity set**: all (σ, E(R)) points attainable from available assets (the curve and everything to its right/inside).
- **Minimum-variance frontier / GMVP / efficient frontier**: lowest σ for each E(R); leftmost point; upper arm above the GMVP.
- **Capital allocation line (CAL)**: all combinations of Rf and a risky portfolio; slope is the market price of risk (Sharpe ratio of the risky portfolio).
- **Two-fund separation theorem**: every investor holds Rf plus the same optimal risky portfolio; only the mix differs.

## Formulas & Reference Tables
```
HPR:                R = (P₁ − P₀ + I₁)/P₀              multi-year: R = Π(1+Rt) − 1
Arithmetic mean:    R̄ = (1/T) Σ Rt
Geometric mean:     R_G = [Π(1+Rt)]^(1/T) − 1
MWR (IRR):          Σ CFt/(1+IRR)^t = 0                (periodic rate; annualize if period ≠ 1 yr)
TWR:                (1+r₁)(1+r₂)…(1+rₙ) − 1            annualized: [Π(1+r_year)]^(1/N) − 1
Annualization:      r_annual = (1 + r_period)^c − 1    c = 52 weekly, 12 monthly, 4 quarterly, 365/days, 2/3 for 18 months
Real return:        (1+r_real) = (1+r)/(1+π) = (1+rrF)(1+RP)
Nominal build-up:   (1+r) = (1+rrF)(1+π)(1+RP)
After-tax:          r_AT = r − t·r = r(1−t)             then real: (1+r_AT)/(1+π) − 1
Utility:            U = E(r) − ½Aσ²
Portfolio return:   E(Rp) = Σ wi E(Ri),  Σ wi = 1
Portfolio variance: σp² = Σᵢ Σⱼ wi wj Cov(i,j) = Σ wi²σi² + Σ_{i≠j} wi wj Cov(i,j)
Two assets:         σp² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρ₁₂σ₁σ₂
ρ = +1:             σp = w₁σ₁ + w₂σ₂ (no diversification)       ρ = −1: σp = |w₁σ₁ − w₂σ₂| (zero at w₁ = σ₂/(σ₁+σ₂))
Equal-weight N:     σp² = σ²/N + [(N−1)/N]·Cov̄  → Cov̄ as N→∞;   with common σ, ρ:  σp² = σ²/N + [(N−1)/N]ρσ²
Rf + risky asset:   E(Rp) = w₁Rf + (1−w₁)E(Ri);  σp = (1−w₁)σi
CAL:                E(Rp) = Rf + [(E(Ri) − Rf)/σi] σp  (intercept Rf, slope = Sharpe ratio of risky portfolio)
Optimal weight in risky portfolio (from U max on CAL):  y* = [E(Rp) − Rf]/(A σp²)   (y* > 1 → borrow)
Add-asset test:     E(Rnew) > Rf + (σnew ρnew,p/σp)[E(Rp) − Rf]  ⇔  (E(Rnew)−Rf)/σnew > ρnew,p × (E(Rp)−Rf)/σp
Normal ±1/2/3σ:     68% / 95% / 99% of observations
```
Historical reference data (Exhibit 7, US, 1926–2017, geometric mean return / σ): large-cap stocks 10.2/19.8, small-cap 12.1/31.7, long corporate bonds 6.1/8.3, long government bonds 5.5/9.9, T-bills 3.4/3.1, inflation 2.9/4.0. Real returns 1900–2017 (Exhibit 9): US equities 6.5% GM (σ 20.0), world equities 5.2% (σ 17.4), bonds 2.0%; US equity-over-bond premium 4.4% (GM). Correlations 1970–2017 (Exhibit 23): US large vs. small 0.72, international vs. US large 0.66, long corporate vs. long Treasury 0.89, stocks vs. bonds roughly −0.15 to 0.23, T-bills vs. stocks ≈ 0.

| Investor type | A | Indifference curve | Chooses |
|---|---|---|---|
| Risk-averse | > 0 | upward, convex | Max U; steeper curve = higher A |
| Risk-neutral | 0 | horizontal | Highest E(R), ignores σ |
| Risk-seeking | < 0 | downward sloping | Higher E(R) and higher σ both add utility |

| Correlation ρ | Diversification effect (two assets) |
|---|---|
| +1 | σp = weighted average of σ; none |
| > 0.90 | Practically none |
| < 0.50 | Desirable for diversification |
| 0 | Meaningful reduction (e.g. 50/50 of two 20% assets → 14.1%) |
| −1 | Risk can be driven to zero |

## Mental Models
- **Return measure = question you are answering**: "What did my money earn?" → IRR. "How good was the manager?" → TWR. "What does compounding do over a decade?" → geometric. "What is next year's expected outcome?" → arithmetic. Never mix them in one comparison.
- **Correlation is the diversification dial**: expected return is a weighted average and ignores ρ; risk is sub-additive whenever ρ < 1. Return is unaffected by ρ, so lowering ρ is a free lunch up to the limit of what is available.
- **Large portfolios are covariance machines**: as N grows, own variance fades like 1/N and the average covariance becomes the floor. Adding the 31st stock of the same market buys little; adding a new asset class (low ρ) buys a lot.
- **Two decisions, two portfolios**: choose P once for everyone (maximum Sharpe, no preferences needed), then dial lending/borrowing for the individual. A client with high risk aversion is not given a "safer risky portfolio", but more cash.
- **Every point strictly below the CAL is dominated** because a leveraged or de-leveraged mix of Rf and P gives more return for the same σ. Points above are unattainable.
- **Utility as certainty equivalent**: U = the risk-free rate that makes the investor indifferent. A 10% return with σ = 20% and A = 3 is worth only 4% certain.

## Worked Example
**1. TWR vs. MWR (Walbright-style fund).** 100m at 1 Jan; gains and dividends bring it to 110m + 2m dividend by 1 May (first subperiod return (10+2)/100 = 12%); 20m added (plus 2m dividend reinvested) → 132m base; at year end 140m + 2.64m dividend → (2.64 + 140 − 132)/132 = 8.06%. TWR = 1.12 × 1.0806 − 1 = **21.03%** (link, do not take a square root, the pieces cover one year). MWR: four-month flows −100, −20, 0, +142.64 → four-month IRR 6.28%, annualized 1.0628³ − 1 = **20.05%**. MWR < TWR because the extra 20m was invested before the weaker second subperiod. The manager's skill is 21.03%; the investor's realized experience is 20.05%.

**2. Geometric vs. arithmetic.** Returns −50%, +35%, +27%: arithmetic mean 4.0%/yr, but 1 × 0.50 × 1.35 × 1.27 = 0.8573, so geometric = −5.0%/yr. Compounding at 4% would claim 1.1249; the actual terminal wealth is 0.8573.

**3. Two-asset risk and the diversification-with-a-riskier-asset result.** 80% S&P 500 (E 9.93%, σ 16.21%), 20% EM (E 18.20%, σ 33.11%), Cov = 0.0050 (ρ ≈ 0.093): E(Rp) = 0.8 × 9.93 + 0.2 × 18.20 = 11.58%; σp² = 0.8²(0.1621²) + 0.2²(0.3311²) + 2(0.8)(0.2)(0.005) = 0.02281; σp = **15.10%**, lower than the 16.21% of the S&P alone while return rises by 1.65 points. Adding a *riskier* asset lowered portfolio risk because ρ is low.

**4. Optimal investor portfolio with a risk-free asset.** A: E 20%, σ 50%; B: E 15%, σ 33%; ρ = 0; Rf = 3%. Maximum-slope (tangency) risky portfolio has wA = 38.2% (38.16% exactly): E = 16.91%, σ = 27.94%, Sharpe = CAL slope = **0.4978**, so CAL: `E(Rp) = 0.03 + 0.4978σp`. For A = 2.5 the closed form gives y* = (0.1691 − 0.03)/(2.5 × 0.2794²) = **71.3%** in the risky portfolio, 28.7% in Rf, σp = 19.9%, E = 12.9%, U = 7.95%. (The reading compares only four preset points on the CAL: σ of 0, 12.1, 24.1, 34.2% give U = 3.0, 7.17, 7.74, 5.46%, and picks the 24.1% point; the true tangency optimum is slightly higher in utility.) Interpretation: all of this investor's wealth sits in just two funds.

## Anti-patterns
- **Averaging annual returns to describe multi-year growth**: arithmetic mean overstates compound wealth, the more so as volatility rises.
- **Judging a manager by IRR when the client controls the flows**: use TWR; use IRR for a PE fund where the GP controls the timing of calls and distributions.
- **Taking a square root to annualize a subperiod-linked return**: if the subperiods already sum to one year, the linked return is the annual return.
- **Annualizing a very short return as if repeatable**: 5% in one week "annualizes" to 1,164%, a meaningless figure.
- **Comparing nominal returns across eras/countries**: inflation (−10.3% to +13.3% annually in the US since 1926) swamps comparisons; use real returns.
- **Equating gross and net return in manager comparison**: gross isolates skill, but only net is what the client keeps. Use the one that answers the question.
- **Believing historical mean = expected return**: acceptable as a working assumption, but flag it; risk and correlation are much more stable than returns.
- **Relying on mean-variance alone for fat-tailed assets**: skew and kurtosis (and liquidity costs) lie outside the framework.
- **Owning your employer's stock on top of human capital**: your wage and your portfolio then share the same risk factor.
- **Adding assets that merely carry a new name**: each holding has trading and tracking cost; test with the add-an-asset rule.

## Exam Focus & Traps
- **Sign/units**: use decimals in `U = E(r) − ½Aσ²` (0.12, not 12). A is positive for risk-averse, 0 neutral, negative for risk-seeking; a lower A (e.g. −4 < 0 < 4) means less risk aversion.
- **Tax then inflation**: real after-tax return = `(1 + r(1−t))/(1+π) − 1`, not `r − t·r − π`.
- **Time-weighted needs valuation at each flow; money-weighted needs the flow timing**. Questions that add a large contribution just before a bad period will ask which is lower: MWR < TWR. A large contribution just before a good period → MWR > TWR.
- **Annualizing**: c = 365/days; 18 months → exponent 2/3; weekly from annual → exponent 1/52.
- **"Which return measure for buy-and-hold with annual deposits?"** The reading's own answer is the geometric mean (compounds returns, not amounts) when the question is about the strategy's return; money-weighted when the question is about the investor's actual return on money invested.
- **Gross return includes trading costs** (they are a cost of generating return); it excludes management, custody and tax costs.
- **σp with ρ = +1 is a weighted average; ρ = −1 does not automatically give zero** (only at w₁ = σ₂/(σ₁+σ₂)); ρ < 1 always gives σp < weighted average σ.
- **Correlation up in a decline** (stress) with weights and σ unchanged → portfolio volatility increases.
- **Large equally weighted portfolio**: what matters most is average covariance, not average variance or individual σ; the asset's own return does not affect portfolio variance at all.
- **Efficient frontier vs. minimum-variance frontier**: the efficient frontier is only the part above the GMVP. The GMVP is attainable and is the lowest-σ risky portfolio; a lower-σ point on a graph is "unattainable".
- **Dominant CAL beats the efficient frontier everywhere except at P** (tangent point); beyond P the superiority comes from borrowing at Rf; left of P from lending.
- **Optimal portfolios of different investors all lie on the same CAL**; they differ only in location.
- **Normal rule**: 68/95/99 for ±1/2/3σ. A "fat-tailed" return has more extreme observations than normal and is called kurtosis; negative skew = long left tail (mass concentrated right of the mean).

## Key Takeaways
1. Choose the return measure by the question: HPR for one period, geometric for compound growth, TWR for managers, MWR for the investor's own result; annualize with `(1+r)^c − 1`, and quote gross for skill and net/after-tax/real for what the client keeps.
2. Arithmetic means overstate growth; the gap widens with volatility, and a mixed-sign series can make the arithmetic mean positive while wealth falls.
3. Mean-variance is only a first approximation: check skewness, kurtosis (use VaR/CTE) and liquidity (bid–ask spread, price impact), especially in emerging-market equities and low-grade bonds.
4. Portfolio return is linear in weights; portfolio risk is not. `σp² = Σ wi²σi² + 2Σ wiwjρijσiσj`, so correlation, not asset count, determines how much risk can be removed (rule of thumb: ρ < 0.5 helpful, ρ > 0.9 almost useless).
5. In a many-asset portfolio, average covariance sets the floor of risk; diversify across asset classes, countries, and currencies, and use index funds for cost-efficient breadth.
6. The efficient frontier is the part of the minimum-variance frontier above the global minimum-variance portfolio; with a risk-free asset it is replaced by the single CAL through the max-Sharpe (tangent) portfolio P.
7. Two-fund separation: determine P once; individual risk aversion only sets the split between Rf and P, with y* = (E(Rp) − Rf)/(Aσp²) and borrowing when y* > 1.
8. Test any new asset against the existing portfolio with Sharpe_new > ρ × Sharpe_p, not by its stand-alone return.

## Connects To
- **ch04**: investment-policy and portfolio-management process that sets the risk and return objectives these tools implement.
- **ch06**: extends this reading by pricing risk: CML and SML, systematic vs. unsystematic risk, CAPM, and the Sharpe, Treynor, M² and Jensen's alpha performance measures.
- **ch07**: turns the optimal-portfolio theory into IPS-driven portfolio planning and construction (strategic asset allocation, active/passive, top-down/bottom-up).
- **ch18**: performance evaluation builds on TWR, geometric linking and attribution.
- **`cfa-asset-allocation-cme` ch07**: asset allocation principles that apply mean-variance optimization (MVO) with real-world inputs and constraints.
- **`cfa-quantitative-methods` ch02**: statistical measures of return (arithmetic, geometric, harmonic means, variance, covariance, skewness, kurtosis); **ch03**: expected value and covariance from probability models; **ch04**: normal distribution used for the 68/95/99 rule and shortfall risk.
