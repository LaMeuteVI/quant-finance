# Chapter 6: Asset Allocation to Alternative Investments
> **Source**: CFA Program Curriculum 2023, Level III, Reading 20 · Portfolio Management (Alternative Investments) | Adam Kobor, Mark D. Guinney

## Core Idea
Alternatives are added to a stock/bond portfolio for one of four roles (capital growth, income, risk diversification, safety), but their reported risk is understated by smoothing and non-normality, and their cash flows are lumpy and illiquid. Allocating well therefore means unsmoothing returns, using tail-aware tools (Monte Carlo, mean-CVaR, risk factors), planning liquidity and commitment pacing explicitly, and monitoring against the program's goals, not just a benchmark.

## Learning Outcomes Covered
- explain the roles of alternatives in multi-asset portfolios
- compare alternatives and bonds as risk mitigators of a long equity position
- compare traditional (asset-class) and risk-based approaches to the opportunity set
- discuss investment considerations (risk, return, vehicle, liquidity, fees, tax, build vs buy) and suitability
- discuss approaches to asset allocation (Monte Carlo, optimization, risk factor-based)
- explain liquidity planning (commitment pacing, capital calls) and monitoring of alternative programs

## Frameworks Introduced
- **Four functional roles**: capital growth (public/private equity, distressed), income (fixed income, real estate), risk diversification (real assets, many hedge funds, private credit vs yield curve risk), safety (government bonds, gold).
  - When to use: before choosing weights, assign each asset class a job; a risk-reducing role is not served by assets with correlation above about 0.8 to equities.
  - How: map each asset to H/M potential per role; hedge funds range from risk-reducing (arbitrage) to return-enhancing (activist); private equity is mainly a return enhancer with limited diversification; real assets and real estate hedge unexpected inflation.
- **Two-step asset allocation (liquid first, then alternatives)**: set the broad stock/bond/real-estate mix using robust liquid-asset data, then break it down into liquid vs private buckets (equity and equity-like; fixed income and fixed-income-like; real estate; each marketable or private).
  - When to use: when alternatives lack long, clean histories.
- **Traditional vs risk-based classification**: traditional = roles, liquidity, macro regime (growth, inflation-hedging, deflation-hedging); risk-based = regress asset returns on factors: equity market, size, value, liquidity (Pastor-Stambaugh), nominal duration, inflation (10-year breakeven), credit spread, currency.
  - Why it works / failure mode: reveals that nominally different assets share equity beta and exposes false diversification; but factor choice is subjective, betas move with look-back (commodity inflation beta is unstable), R² is 0.8-1.0 for traditional assets but only 0.3-0.7 for alternatives, so much risk stays idiosyncratic.
- **Three allocation tools (complementary)**: (1) Monte Carlo simulation with regime switching or fat-tailed inputs, scored on probability of meeting the goal; (2) optimization (MVO with constraints, or mean-CVaR); (3) risk factor-based optimization implemented through asset classes.
- **Takahashi-Alexander private fund cash-flow model**: contributions `C_t = RC_t × (CC − PIC_{t−1})`, distributions `D_t = RD_t × NAV_{t−1} × (1+G)`, `RD_t = (t/L)^B`, `NAV_t = NAV_{t−1}(1+G) + C_t − D_t`.
  - When to use: to size annual commitments (commitment pacing), forecast calls and distributions, and stress liquidity.
- **Unsmoothing (Ang)**: `r_unsmoothed,t = (r_reported,t − s × r_reported,t−1) / (1 − s)`, with s the first-order serial correlation.
- **Monitoring checklist**: program goals and thesis, benchmark and performance (IRR and MOIC), firm and process (key person, alignment, style drift, risk management, client/asset turnover, client profile, service providers).

## Key Concepts
- **Equity beta vs correlation**: beta = response size, correlation = strength of linear link; hedge funds have beta around 0.4 but correlation about 0.8; commodities beta 0.3 but correlation 0.2. Diversification power comes from low correlation.
- **Unsmoothing**: removing the autocorrelation from appraisal-based returns to estimate true volatility. Serial correlation: private real estate 0.85, private equity 0.38, distressed hedge funds 0.36, high yield 0.34.
- **Fat tails / negative skew**: observed CVaR exceeds normal CVaR when kurtosis is high and skew negative; private real estate (skew −2.8, excess kurtosis 9.6) and equity market-neutral (−1.17, 3.55) show the biggest gaps.
- **CVaR (expected shortfall)**: expected loss given loss beyond the VaR threshold; used for optimization when tails matter.
- **Regime-switching model**: mixture of normal regimes (quiet, crisis) with different means, volatilities and correlations; produces skew and fat tails.
- **Capital commitment (CC), paid-in capital (PIC), NAV, bow parameter (B)**: commitment total; capital already called; fund value; steepness of the distribution schedule (higher B = later distributions).
- **Vintage-year diversification**: spreading commitments across years because private returns depend heavily on vintage.
- **Drawdown/call-down fund**: PE, private credit, real estate, real asset funds called in stages over about 3-5 years; typical 10-year life plus 1-2 year extension; 30-day call notice; default can forfeit the interest.
- **Side pocket**: illiquid assets segregated from fund redemption terms.
- **Gate / lock-up / holdback**: limits on redemption amount; typical US hedge fund lock-up 1 year with 10% early-redemption penalty; 10% holdback until audit; 30-90 days' notice.
- **Blind pool**: committed capital to unidentified assets.
- **Fund of one / SMA**: customized vehicle; no GP capital alongside LPs, so weaker alignment; SMAs give transparency and control.
- **Probability of purchasing-power impairment**: IC-defined chance of losing a set fraction (for example 40%) of real endowment value over 10 years after spending and gifts.
- **MOIC**: (current value + distributions) / invested capital; complements time-sensitive IRR.
- **UBIT**: US tax on tax-exempt investors from unrelated business income; offshore feeders can shield.

## Formulas & Reference Tables
- Fisher: `(1+r_real)(1+π) − 1`; 5% real with 2% inflation = 7.1% nominal.
- Geometric return ≈ `μ_arith − σ²/2`; portfolio geometric return is not the weighted average of asset geometric returns.
- `σ_annual = σ_quarterly × √4` valid only without serial correlation.
- Private-fund model: see Frameworks. RD_t for L=12, B=2.5: 0%, 1%, 3%, 6%, 11%, 18%, 26%, 36%, 49%, 63%, 80%, 100%; for B=5: 0, 0, 0, 0, 1, 3, 7, 13, 24, 40, 65, 100.
- Commitment pacing: required NAV target = `target weight × projected total portfolio value`; scale commitment by NAV per unit committed from the model; spread over several vintages.
- Gross to net hedge fund: 3% quarterly gross, 2% mgmt (0.5% per quarter), 20% incentive on net per quarter gives about 8.2% a year vs 12.6% gross.

Illustrative capital market assumptions (return / volatility / corr to equities / beta): public equity 6.5/17.0/1.00/1.00; government bonds 2.3/4.9/−0.60/−0.17; private credit 6.5/10.0/0.70/0.40; hedge funds 5.0/8.1/0.83/0.40; commodities 4.5/25.2/0.21/0.31; public real estate 6.0/20.4/0.60/0.72; private real estate 5.5/13.8/0.37/0.30; private equity 8.5/15.7/0.81/0.74.

| Approach | Strengths | Limitations |
|---|---|---|
| Traditional (roles/liquidity/regime) | easy to communicate; fits liquidity and mandate implementation; scenarios | overstates diversification; hides risk drivers (govts and high yield both "fixed income") |
| Risk-based (factors) | common language for public/private; integrated risk | look-back sensitivity; implementation hurdles (liquidity, manager selection); subjective factor set |
| MVO | simple | over-allocates to alternatives (understated risk, normality), concentrated, input-sensitive; needs constraints |
| Mean-CVaR | captures skew and tails (macro gets more weight, real estate dropped) | needs many scenarios; complex |
| Monte Carlo | tests goal probability, non-normal | model dependent |

Liquidity terms: hedge funds subscribe monthly/quarterly, redeem quarterly or annually with 30-90 days notice, gates, 10% holdback. Private funds: no redemption; secondary sale at discount, needs GP approval; distributions as realized; in-kind at termination.

Time horizon: private programs need 5-7 years to build and 10-12 to unwind; avoid private real estate, real assets, PE if horizon is under 15 years.

Fees: mgmt 0.5%-2.5%, incentive 10%-20%; pass-through expenses 0.05%-0.20% for large funds, up to 0.5% for small; PE fee on commitment makes J-curve worse.

## Mental Models
- **Bonds shrink volatility, alternatives help reach the goal**: over a short horizon government bonds (correlation about −0.6) cut volatility most (70/30 equity/bonds about 11.1% vs 11.9% with cash); over long horizons, low expected return makes missing the target the larger risk because return grows with time and volatility with √time.
- **Two risk dimensions**: volatility/drawdown for interim pain; shortfall probability for the objective. A "lower-risk" portfolio by volatility can be the higher-risk one by goal probability.
- **Reported volatility is a lower bound**: smoothing and survivorship/back-fill bias understate risk; always test autocorrelation and unsmooth before optimizing.
- **Optimizer as advisor, not decider**: MVO corner solutions follow inputs; constrain, then check that many different allocations give similar frontier points.
- **Pending capital needs a proxy**: hold public equity for undrawn PE, high yield for private credit, REITs for private real estate, energy stocks or commodity futures for real assets, while waiting for calls.
- **Liquidity is a stress problem**: calls speed up and distributions slow in bear markets (GPs also extend fund life), exactly when public assets are down; plan for faster calls and slower distributions.
- **Do not judge illiquid funds early**: wait until most assets are monetized; use IRR and MOIC together and a vintage peer group.

## Worked Example
**Unsmoothing and fees.** Reported quarterly private equity volatility annualizes to 9.5%; serial correlation 0.38 (t-stat about 4.1). Unsmoothing gives about 14.0% (Cambridge Associates index, per the reading). Quarterly rule `r_u = (r_t − 0.38 r_{t−1}) / 0.62`. For a reported 4% following 2%: (0.04 − 0.0076)/0.62 = 5.2%.

**Private fund model (CC = 100, L = 12, B = 2.5, G = 13%, 25% then 50% of remaining called).** Calls: 25, 37.5, 18.75, 9.4, 4.7, ... NAV path: 25, 65.4, 90.4, 105.0, 110.0 (peak, year 5), 104.7, 88.7, 64.5, 37.6, 15.7, 3.6, 0.0. Distributions: 0, 0.3, 2.3, 6.6, 13.3, 22.0, 30.7, 36.4, 35.5, 27.0, 14.3, 4.0. Raising B to 5 delays distributions, lets NAV grow higher, but keeps cumulative net cash flow negative longer.

**Single-year roll.** NAV €30m, all capital called, 20% distribution at year-end 2021, 12% growth: distribution = 30 × 1.12 × 20% = €6.72m; NAV 2022 = 30 × 1.12 × 0.80 × 1.12 = €30.1056m.

**Commitment pacing.** £1bn portfolio, 6% growth, 20% PE target. In 5 years portfolio = 1,000 × 1.06⁵ = £1,338m, target NAV about £268m. A £100m commitment peaks near £110m NAV, so a single commitment would be about £243m. Better: roughly £70m a year over four vintages (2017-2020), reaching the target about year 5, then keep committing (slower) to maintain 20%.

**Liquidity check (Example 9).** $750m endowment, 5% spending ($37.5m) plus 20% calls on private NAV ($202.5m × 20% = $40.5m) = $78m over 12 months vs $75m of cash plus governments. Respond by lifting cash and short-duration government bonds to the top of ranges, trimming public equity and hedge funds (notice 60-90 days, gates possible), and accept that private weights will drift up in a sell-off (real estate toward its 13% cap).

**Mean-CVaR vs MVO.** Same 60% L/S equity hedged and 5.0% expected return: MVO fills the remaining 40% with equity market-neutral (vol 7.3%, CVaR −7.7%); mean-CVaR fills with macro (vol 7.8%, CVaR −6.8%). Multi-asset at 6.8% return: MVO holds 22% real estate, mean-CVaR holds none (99% CVaR −20.7% vs −15.6%).

## Anti-patterns
- **Using raw reported volatility and correlation of private assets**: smoothing shows false diversification (private real estate unsmoothed volatility is about 3x reported).
- **Unconstrained MVO output as policy**: concentrates in PE and cash/fixed income and over-allocates to alternatives.
- **Over-committing early to hit target weights**: pre-2008 over-commitments met capital calls when liquidity was scarce, forcing secondary sales at discounts or default.
- **Treating "alternatives" as one diversifier**: hedge funds and PE have correlation above 0.8 to equities; only some strategies diversify.
- **Judging a program only against peer indices**: index providers differ widely (3-year event-driven returns of 3.8%, 0.8% and 6.8% for three providers).
- **Ignoring the leverage lenders' first claim**: margin calls with about two days' notice drain liquidity just when fund stress peaks.
- **Chasing a hot unwinding PE sleeve**: small residual NAV produces extreme percentage returns.
- **Imposing fixed ESG or tax rules on commingled vehicles**: commingled hedge funds rarely meet look-through criteria; SMAs are limited to very large clients.

## Exam Focus & Traps
- Bonds vs alternatives: bonds win on short-horizon volatility reduction; alternatives win on long-horizon target probability (because of higher expected return). The stock-bond negative correlation (about −0.6) was a low-inflation feature; it was positive in the 1970s-1990s when inflation was higher.
- Beta vs correlation: low beta with high correlation (hedge funds) = milder but still synchronized moves.
- Inflation hedges: commodities and inflation-linked bonds highest inflation sensitivity; real estate, timber, farmland (leased farmland behaves like core real estate), energy, infrastructure.
- Distressed debt behaves equity-like; direct lending behaves like bonds of similar credit quality.
- Which approach for which client (Example 7): newly wealthy, unsophisticated investor, MVO plus Monte Carlo (education); sophisticated IC with tail concerns and alternatives exposure, mean-CVaR; risk factor approach needs permanent staff and active monitoring.
- Constraint check: choose the highest-return portfolio whose 1-year 99% CVaR does not breach the covenant (Portfolio D: 99% CVaR −19.4% vs −20% trigger).
- Alternatives suit only investors with a long horizon (15+ years for private), expertise, governance, tolerance for limited transparency.
- Fund of funds: single consolidated capital call and report but extra fees and less customization. Funds of one lack GP co-investment alignment.
- Tax: US favors real estate (depreciation), timber (capital gains, depletion), energy; UBIT for tax-exempts; use offshore feeders.
- IRR is cash-flow-timing sensitive; MOIC ignores timing; use both.
- ⚠ Source typos to not copy: Example 8 shows "× 1.12%" (should be × 1.12) and the unsmoothing text says the unsmoothed volatility is higher than "the unsmoothed data" (means the reported data). Result €30,105,600 is right.

## Key Takeaways
1. Define each alternative's role (growth, income, diversification, safety) before sizing it; do not assume risk reduction from assets with correlation above 0.8.
2. Unsmooth returns whenever serial correlation is significant; account for survivorship and back-fill bias.
3. Evaluate risk in two ways: volatility/drawdown and probability of meeting the objective; bonds help the first, return-seeking alternatives help the second.
4. Use several tools together: constrained MVO, mean-CVaR, Monte Carlo (regime-switching), and risk factor decomposition; check robustness to inputs.
5. Build private allocations through multi-year, multi-vintage commitment pacing with a cash flow model; target NAV on projected portfolio size.
6. Stress liquidity: faster calls, slower distributions, extended fund life, gates, margin calls; hold liquid proxies for undrawn commitments and keep a cash/government bond buffer for 12-24 months of liabilities.
7. Account for fees, expenses, taxes and vehicle choice (LP, feeder, FoF, SMA, liquid alt) in return assumptions; use a building-blocks method (risk-free + factors + alpha − fees − taxes).
8. Monitor goals, thesis, performance (IRR plus MOIC, peer vintages) and the firm (key person, alignment, style drift, service providers, asset and client flows).

## Connects To
- **ch05**: hedge fund strategy behaviour and the conditional factor model underlying the hedge fund allocation inputs.
- **ch01**: alternatives structures, fees and valuation basics.
- **ch02, ch03, ch04**: real estate, private equity and commodity characteristics that feed capital market assumptions.
- **`cfa-asset-allocation-cme` ch06-ch08**: asset allocation process, factor-based and liability-relative approaches, real-world constraints.
- **`cfasi-portfolio-construction` ch15**: practitioner case for alternatives in portfolio construction.
- **`cfa-wealth-institutional-management` ch04**: institutional investors' liquidity and horizon constraints.
