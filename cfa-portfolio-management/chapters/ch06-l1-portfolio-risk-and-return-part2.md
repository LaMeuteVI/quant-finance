# Chapter 6: Portfolio Risk and Return: Part II
> **Source**: CFA Program Curriculum 2020, Level I, Reading 53 · Portfolio Management | Vijay Singal, PhD, CFA

## Core Idea
With homogeneous expectations the optimal risky portfolio for everybody is the market portfolio, so the capital allocation line becomes the capital market line (CML) and only systematic risk (beta) is rewarded. The CAPM turns that into a pricing rule, `E(Ri) = Rf + βi[E(Rm) − Rf]`, which doubles as a required-return estimator, a security-selection screen (alpha vs. the SML) and the basis of four performance measures (Sharpe, Treynor, M², Jensen's alpha), each suited to a different "who holds what" situation.

## Learning Outcomes Covered
- Describe combining a risk-free asset with a risky portfolio (lending and borrowing/leveraged portfolios)
- Explain the CAL and the CML
- Explain systematic vs. nonsystematic risk and why only systematic risk earns a premium
- Explain return-generating models (single-index, market model, multifactor) and their uses
- Calculate and interpret beta (from correlation/covariance and by regression)
- Explain the CAPM, its assumptions and the SML; calculate expected return with it
- Describe and apply the CAPM/SML (capital budgeting, security selection, portfolio construction)
- Calculate and interpret the Sharpe ratio, Treynor ratio, M², and Jensen's alpha

## Frameworks Introduced
- **Capital market line (CML)**: `E(Rp) = Rf + [(E(Rm) − Rf)/σm]·σp`
  - When to use: pricing efficient (fully diversified) portfolios built from the risk-free asset and the market; passive investing.
  - How: set the intercept to Rf and the slope (the "market price of risk") to the market's Sharpe ratio; lending portfolios sit between Rf and M (w₁ ≥ 0 in Rf), borrowing/leveraged portfolios beyond M (w₁ < 0). Portfolio risk is just `σp = (1 − w₁)σm` because Rf has zero variance and zero covariance. With a borrowing rate Rb > Rf the line kinks at M: slope `(E(Rm) − Rf)/σm` to the left, the flatter `(E(Rm) − Rb)/σm` to the right.
  - Why it works / failure mode: the tangent portfolio is the market only under homogeneous expectations; the "market" must be proxied (e.g. S&P 500) and every proxy changes the CML.
- **Total variance decomposition (single-index / market model)**: `σi² = βi²σm² + σe²` (systematic + nonsystematic) with `Ri − Rf = βi(Rm − Rf) + ei` and market-model form `Ri = αi + βiRm + ei`.
  - When to use: separating priced from unpriced risk; estimating beta by regressing the asset's returns on the market's; computing abnormal (company-specific) return `ei = Ri − (αi + βiRm)`.
  - How: regress historical Ri on Rm (slope = β, intercept = α); the error term is uncorrelated with the market so it drops out of Cov(Ri, Rm).
  - Why it works: the argument for "no reward for diversifiable risk" is a no-arbitrage/demand argument: if idiosyncratic risk paid a premium, everybody would buy it and diversify it away, bidding its price up until the premium is zero.
- **CAPM and the security market line (SML)**: `E(Ri) = Rf + βi[E(Rm) − Rf]`, plotted with beta on the x-axis; intercept Rf, slope = market risk premium `Rm − Rf`, market at β = 1.
  - When to use: required return for valuation and capital budgeting, spotting mispriced securities, benchmarking managers; applies to every asset or portfolio, efficient or not.
  - How: estimate β (covariance/variance or regression), choose Rf and the market premium, compute; compare your forecast return with the CAPM return: forecast above SML = undervalued (buy), below = overvalued (sell/short).
  - Failure mode: single-period, single-factor, unobservable market, unstable beta, weak empirical support.
- **Performance appraisal measures** (Sharpe, Treynor, M², Jensen's alpha) — see formulas below.
  - When to use: Sharpe and M² (total risk) when the portfolio is the investor's whole (not fully diversified) portfolio or a single manager's mandate; Treynor and Jensen's alpha (beta risk) when the portfolio is a component of a well-diversified aggregate.
- **Security selection around a passive core**: start from the market proxy, then add or overweight assets with positive Jensen's alpha and down-weight/underweight (or short) those with negative alpha; weight in each non-market security ∝ `αi/σ²ei`; rank by information ratio `αi/σei`.
  - When to use: constructing a portfolio when you hold views that differ from the market's and want to size active positions.
  - Why it works / failure mode: alpha only pays if your forecast really differs from the consensus; transaction costs must be compared with the size of the mispricing.

## Key Concepts
- **Capital allocation line (CAL)**: combinations of the risk-free asset with any risky portfolio; the CML is the CAL whose risky portfolio is the market.
- **Market portfolio**: the optimal risky portfolio under homogeneous expectations; in theory all risky assets (including human capital and non-investable assets), in practice a value-weighted index proxy. Not all assets are tradable, and not all tradable assets are investable.
- **Homogeneity of expectations**: everyone uses the same cash-flow and required-return inputs, hence the same optimal risky portfolio and one market price. With heterogeneous beliefs (Analyst B at €95, C at €125 on a €111.84 share) no unique optimal portfolio exists; the market price becomes the marginal informed investor's view and the benchmark.
- **Passive vs. active portfolio**: passive replicates a market-cap-weighted index and assumes prices are unbiased; active over/underweights vs. the benchmark based on own valuations.
- **Lending vs. borrowing portfolio**: on the CML to the left of M (positive Rf weight) vs. to the right (negative Rf weight, leverage).
- **Systematic (market, non-diversifiable) risk**: affects the entire market (rates, inflation, cycles, political shocks); priced.
- **Nonsystematic (idiosyncratic, company/industry-specific, diversifiable) risk**: avoidable by combining low-correlation assets; not priced.
- **Beta**: sensitivity of an asset to the market, `Cov(Ri, Rm)/σm² = ρi,m σi/σm`; market β = 1, risk-free β = 0, portfolio β = weighted average of betas.
- **Return-generating model**: gives expected return from risk factors; multifactor models (macroeconomic, fundamental, statistical) generalize it; statistical factors risk data-mined spurious factors.
- **Security characteristic line (SCL)**: plot/regression of the security's excess return on market excess return, `Ri − Rf = αi + βi(Rm − Rf)`; slope β, intercept Jensen's alpha.
- **Security market line vs. CML**: SML = expected return vs. beta, valid for any asset; CML = expected return vs. total risk, valid only for efficient portfolios. Total risk equals systematic risk only for diversified portfolios.
- **Arbitrage pricing theory (APT)**: `E(Rp) = RF + Σ λj βp,j`; many factors, no-arbitrage derivation, but factors unspecified, hence rarely used directly.
- **Fama–French/Carhart four-factor model**: `Ri − Rf = αi + βMKT·MKT + βSMB·SMB + βHML·HML + βUMD·UMD`; size, value (book-to-market), momentum; empirical, not an equilibrium model.
- **Performance evaluation = measurement + attribution + appraisal**: what happened, why it happened, skill or luck.
- **Information ratio**: alpha per unit of nonsystematic risk, `αi/σei`; abnormal return added per unit of diversifiable risk taken.

## Formulas & Reference Tables
```
CML:            E(Rp) = Rf + [(E(Rm) − Rf)/σm] σp          σp = (1 − w₁)σm     w₁ = weight in Rf (negative = borrowing)
Kinked CML:     w₁ ≥ 0: Rf + [(E(Rm)−Rf)/σm]σp ;  w₁ < 0: Rb + [(E(Rm)−Rb)/σm]σp
Portfolio var.: σp² = Σ wi²σi² + Σ_{i≠j} wi wj ρij σi σj          Cov(i,j) = ρij σi σj,  Cov(i,i) = σi²
Variance split: σi² = βi²σm² + σe²    (systematic + nonsystematic; for diversified portfolio σe² ≈ 0 → σp = βpσm)
Single index:   E(Ri) − Rf = βi[E(Rm) − Rf]        realized: Ri − Rf = βi(Rm − Rf) + ei
Market model:   Ri = αi + βiRm + ei                (αi = Rf(1 − βi) if CAPM holds)
Beta:           βi = Cov(Ri,Rm)/σm² = ρi,m σi/σm        βm = 1, β(Rf) = 0, β(portfolio) = Σ wi βi
CAPM / SML:     E(Ri) = Rf + βi[E(Rm) − Rf]        Market risk premium = E(Rm) − Rf
General model:  E(Ri) − Rf = Σ_j βij E(Fj)         (factor 1 = market premium)
APT:            E(Rp) = RF + λ₁βp,1 + … + λKβp,K
4-factor:       Ri,t − Rf,t = αi + βi,MKT MKTt + βi,SMB SMBt + βi,HML HMLt + βi,UMD UMDt
Sharpe ratio:   SR = [E(Rp) − Rf]/σp               (slope of CAL; ex post uses sample means and s.d.)
Treynor ratio:  TR = [E(Rp) − Rf]/βp
M² (RAP):       M² = SR_p × σm + Rf = (Rp − Rf)(σm/σp) + Rf ;   M² alpha = M² − Rm
Jensen's alpha: αp = Rp − {Rf + βp[Rm − Rf]}       = βp × (TR_p − (Rm − Rf))  (vertical distance above SML; αm = 0)
SCL:            Ri − Rf = αi + βi(Rm − Rf)
Info. ratio:    IR = αi/σei ;  σ²ei = σi² − βi²σm² ;  nonmarket weight ∝ αi/σ²ei
Number of estimates for N assets (full covariance model): N returns + N variances + N(N−1)/2 correlations (1,000 assets → 499,500)
```

| Measure | Risk used | Needs positive numerator? | Output | Use when |
|---|---|---|---|---|
| Sharpe | total (σ) | yes | ratio, rank only | portfolio is the investor's entire holding |
| M² | total (σ) | yes (ranks same as Sharpe) | % return at market's risk; M² alpha vs. market | same as Sharpe, but wants a % figure |
| Treynor | systematic (β) | yes, and β > 0 | excess return per unit β, rank only | portfolio is one slice of a diversified whole |
| Jensen's α | systematic (β) | no | % abnormal return | diversified investors; manager ranking; ≈ max fee worth paying |

| Line | x-axis | Applies to | Intercept | Slope |
|---|---|---|---|---|
| CAL | σp | Rf + any risky portfolio | Rf | Sharpe ratio of that risky portfolio |
| CML | σp | Rf + market portfolio | Rf | (E(Rm) − Rf)/σm |
| SML | β | every asset and portfolio | Rf | E(Rm) − Rf |
| SCL | Rm − Rf | one security (regression) | Jensen's α | β |

CAPM assumptions: risk-averse utility-maximizing rational investors; frictionless markets (no taxes/transaction costs, can borrow and lend at Rf; short selling costs matter most); one common single holding period; homogeneous expectations; infinitely divisible assets; price takers. Short-sale constraints are the one relaxation that can bias prices, others are largely benign.

## Mental Models
- **CML for efficient portfolios, SML for anything**: if the asset is fully diversified, total risk = systematic risk, and CML and SML agree (σ = βσm). For a single stock, never price off σ; price off β.
- **Priced risk is the part you cannot diversify**: two assets with equal beta have equal expected return regardless of how volatile each is on its own. Asset A with twice B's total risk but ⅔ systematic has 1.33× B's systematic risk, so it needs the higher return, not B.
- **Alpha is a vertical distance from the SML; beta is the horizontal position**: a point above the SML is "cheap" (return > required), below is "rich". An asset can enter a portfolio with positive alpha simply because it is poorly correlated with the base index and still earns enough for its beta.
- **Sharpe tells you who wins when you're all-in; Treynor/Jensen tell you who wins when you're a satellite**: in the pension example, Y wins on Sharpe/M² (σ 10%) but Z wins on Treynor/Jensen (β 0.6, α 5.4%). The "best manager" depends on what else the client owns.
- **M² is Sharpe in percentage clothing**: lever or delever the portfolio to the market's σ and compare returns; positive M² alpha means beating the market at equal total risk. Same ranking as Sharpe.
- **Leverage moves you along the line, it does not change the slope** (unless Rb > Rf, where it flattens). Borrowing 50% at Rf on a market with E = 15%, σ = 20%, Rf = 5% gives 20% return at σ = 30%.
- **Beta is an estimate, not a fact**: short windows (12 months) track the current beta but are noisy; 3–5 years are steadier but may be stale; daily vs. monthly data and the market proxy all move it.

## Worked Example
**1. Beta and CAPM return (recomputed).** Market σ = 25%, E(Rm) = 10%, Rf = 3%. ANR before an acquisition: ρ = 0.95, σ = 50% → β = 0.95 × 0.50/0.25 = 1.90, E(R) = 3% + 1.90 × 7% = **16.3%**. After: ρ = 0.75, σ = 30% → β = 0.90, E(R) = **9.3%**. The drop of 1.0 in beta lowered the required return by exactly the 7% premium. Cross-check by covariance: ρσiσm = 0.70 × 0.25 × 0.15 = 0.02625, divided by σm² = 0.0225, gives β = 1.17.

**2. Four performance measures side by side.** Rf = 3%, market return 9% with σ = 19%.

| Mgr | Ret | σ | β | CAPM E(R) | Sharpe | Treynor | M² (alpha) | Jensen α |
|---|---|---|---|---|---|---|---|---|
| X | 10% | 20% | 1.10 | 9.6% | 0.350 | 0.064 | 9.65% (+0.65) | +0.40% |
| Y | 11% | 10% | 0.70 | 7.2% | 0.800 | 0.114 | 18.2% (+9.20) | +3.80% |
| Z | 12% | 25% | 0.60 | 6.6% | 0.360 | 0.150 | 9.84% (+0.84) | +5.40% |
| Mkt | 9% | 19% | 1.00 | 9.0% | 0.316 | 0.060 | 9.00% (0) | 0 |

M² for Y: 0.80 × 0.19 + 0.03 = 18.2%. Jensen α for Z: 12 − (3 + 0.6 × 6) = 5.4%. Reading: all three beat the market on every measure, so the plan is satisfied; as a sole manager choose Y (total risk), as one of several in a diversified plan choose Z (systematic risk). Both lie above the SML.

**3. Selecting non-index stocks.** Nikkei proxy: E = 12%, σ = 18%, Rf = 2%. Stocks P (15%, σ 30%, β 1.5), Q (18%, 25%, 1.2), R (16%, 23%, 1.1). Alphas: P = 15 − (2 + 1.5 × 10) = −2% (exclude or short); Q = +4%; R = +3%. Non-systematic variances: P 0.0171, Q 0.0158, R 0.0137. Relative weights ∝ α/σ²e: Q = 0.04/0.0158 ≈ 2.5, R = 0.03/0.0137 ≈ 2.2, so Q gets about 15% more than R.

**4. Capital budgeting with CAPM.** Drug project with β = 2.3, Rf = 2%, market 12%: required return = 2% + 2.3 × 10% = 25%. Expected cash flows (success probability 50%): −500, −200, 200, 200, 200, 500 ($m, years 1–6) discounted at 25% → NPV = −400 − 128 + 102.4 + 81.9 + 65.5 + 131.1 = **−$147.1m**: reject.

## Anti-patterns
- **Pricing a single stock off its total risk (σ)**: only β is rewarded; a volatile but market-uncorrelated asset (β = 0) should earn only Rf.
- **Expecting a premium for idiosyncratic risk** (or concentrating "because the stock is volatile"): the premium is zero by construction; diversify it away.
- **Ranking with Sharpe/Treynor when the excess return is negative**: a riskier negative-excess portfolio looks "better" (less negative); Treynor additionally fails for negative-beta assets.
- **Using a mismatched benchmark** (real estate fund vs. the S&P 500): alpha, M² and Treynor all inherit the benchmark error.
- **Using Sharpe for a satellite sleeve, or Treynor/Jensen for a concentrated all-in portfolio**: total vs. systematic risk must match the client's diversification.
- **Treating one historical beta as truth**: estimation window, frequency, and index proxy change it; the CAPM is ex ante but applied with ex post data.
- **Reading a small alpha as skill**: alpha is an estimate; the CAPM may be the wrong model (size, value and momentum can masquerade as alpha), and fees/trading costs can exceed it.
- **Ignoring the borrowing-rate kink**: assuming one straight CML beyond M overstates the leveraged investor's reward per unit of risk.
- **Assuming the CAPM beta of ≈ 0 gold or EM is a "free" diversifier without checking return**: a β near zero or negative asset is worth its diversification only if its price/return is acceptable (insurance has negative β and negative expected return and is still rational to buy).

## Exam Focus & Traps
- **Which line**: CAL = Rf + any risky portfolio; CML = Rf + market portfolio; SML = E(R) vs. beta, all assets; SCL = regression of excess returns. "Graph of the CAPM" = SML. Correctly priced individual assets plot on the SML; efficient portfolios on the CML.
- **Above CML = unachievable; below = dominated (inferior).** Right of M = borrowing/leveraged; left of M (return below the market's) = lending.
- **Highly risk-averse investors still hold the market portfolio** (same risky portfolio) but mostly the risk-free asset; the optimal portfolio is set by indifference-curve tangency, not by the highest CAL slope.
- **"Total risk is the sum of systematic and nonsystematic"** refers to variances, not standard deviations.
- **Beta algebra**: β = ρσi/σm. Market β = 1 ⇒ average beta of all assets = 1. Rf β = 0. Beta of a portfolio is the weighted average, including 0 for the risk-free share (20% Rf, 30% market, 50% stock with β 2 → β = 1.30, E = 4% + 1.3 × 12% = 19.6%).
- **Expected return below Rf is possible** for negative-beta assets.
- **Beta rankings**: with σ (25, 20, 20), ρ (0.6, 0.7, 0.8) and σm = 15, betas are 1.00, 0.93, 1.07: highest total risk is security 1, highest beta is security 3, least market risk is security 2. Do not confuse total risk with market risk.
- **Market risk premium = E(Rm) − Rf** (equal to the "excess market return"). Intercept of the market model ≠ intercept of the SCL in meaning: regress raw returns → αi = Rf(1−β) under CAPM; regress excess returns → α is Jensen's alpha.
- **Ex post Jensen's alpha** uses realized Rp, average Rf, estimated β and *realized* average market return.
- **Which measure is "consistent with the CAPM"**: Jensen's alpha and Treynor (both use beta); Sharpe and M² use total risk.
- **A measure that needs no comparison**: only Jensen's alpha has an absolute meaning (zero = fair); Sharpe and Treynor must be compared with another portfolio's value; M² needs the market's return.
- **Estimated return > CAPM return ⇒ undervalued.**
- **Two-step**: if the question stresses "homogeneous expectations" the consequence is that all investors hold the same optimal risky portfolio (the market), not the S&P 500 per se. "Price takers" and "single period" do not by themselves create a market portfolio; homogeneity does.
- **Fama–French/Carhart**: size (SMB), value (HML), momentum (UMD) added to the market factor; model is empirical and has no equilibrium theory behind it.
- Utility, variance and CAPM questions often hide units: percentages must be converted to decimals before multiplication by squared terms.

## Key Takeaways
1. The CML is the CAL with the market portfolio as its risky component: `E(Rp) = Rf + [(E(Rm) − Rf)/σm]σp`; passive investors position themselves on it, and leverage (borrowing at Rf) moves them beyond M with higher return and proportionally higher risk.
2. Total variance = βi²σm² + σe²; only the systematic part is priced, because diversifiable risk can be removed for free (about 30 randomly selected stocks across sectors remove most of it; use index funds otherwise).
3. Estimate beta as Cov(Ri, Rm)/σm² or with a regression of the asset's returns on the market's; know the estimation-window trade-off (short = current but noisy, 3–5 years = stable but stale).
4. CAPM gives the first-pass required return for valuation and capital budgeting and the SML identifies over/undervaluation: an expected return above the SML is a buy. Portfolio beta is the weighted average of component betas.
5. The CAPM is limited (single factor, single period, unobservable market, unstable beta, weak empirical fit); APT and the Fama–French/Carhart four-factor model add factors but not equilibrium theory (APT) or stability (four-factor).
6. Use Sharpe/M² for undiversified or stand-alone portfolios and Treynor/Jensen for components of a diversified portfolio; always use the correct benchmark and check that excess returns (and β for Treynor) are positive.
7. Jensen's alpha is the best selection and manager-ranking measure and approximates the most a client should pay for active management; size active positions ∝ α/σ²e and rank by information ratio, net of transaction costs.
8. Heterogeneous beliefs break the unique optimal risky portfolio; the market portfolio then serves as the benchmark and the passive default.

## Connects To
- **ch05**: provides the efficient frontier, utility, CAL and two-fund separation on which the CML/CAPM rest; also the returns measures (TWR etc.) used as inputs to performance appraisal.
- **ch07**: portfolio planning and construction (IPS, strategic asset allocation, active/passive and top-down/bottom-up) applies these ideas, including the passive/active choice.
- **ch12**: multifactor models extend the single-index/market model, APT and the Fama–French/Carhart structure introduced in section 5.
- **ch15**: active-portfolio analysis (information ratio, fundamental law of active management, active risk/return) develops the alpha/information-ratio logic of section 7.
- **ch18**: performance evaluation (attribution, appraisal, benchmark selection, risk-adjusted measures) builds on Sharpe, Treynor, M² and Jensen's alpha.
- **`cfa-asset-allocation-cme` ch07**: mean-variance optimization (MVO) at the asset-class level, including constraints and its sensitivity to inputs.
- **`cfa-quantitative-methods` ch07**: linear regression (the engine of the beta/alpha estimate, R², standard errors); **ch03**: covariance, correlation and expected value.
- **`cfa-corporate-finance` ch03**: CAPM as the standard cost-of-equity input to WACC; **ch02**: required return for NPV.
- **`cfa-equity-valuation` ch05**: CAPM and the multifactor build-up for required return on equity.
