# Chapter 5: Economics and Investment Markets
> **Source**: CFA Program Curriculum 2022, Level II, Reading 42 · Portfolio Management | Andrew Clare, PhD, and Thomas F. Cosimano, PhD

## Core Idea
Every financial asset is a claim on the real economy, so the economy can move a price only through three doors: default-free interest rates (real rate + expected inflation), the timing and size of expected cash flows, and risk premiums. The reading builds one pricing equation and adds one premium per asset class (inflation uncertainty, credit, equity, liquidity), each tied to the business cycle through the investor's marginal utility of consumption (the "pricing kernel"). It is the macro layer behind the building-block expected returns of ch04 and the cycle-aware tilts of ch06–ch08.

## Learning Outcomes Covered
- explain that economic factors move values only via default-free rates, expected cash flows, or risk premiums
- explain the role of expectations and of changes in expectations (news vs anticipated information)
- relate long-run growth, growth volatility and the average real short rate
- explain how the cycle drives policy rate, short rates, curve slope and relative bond performance
- decompose the nominal vs inflation-indexed yield spread (break-even inflation)
- explain how the cycle drives credit spreads and credit-sensitive bond performance; how product-market traits drive credit quality
- explain cycle effects on short- and long-term earnings growth, on the equity risk premium (consumption hedging) and on valuation multiples
- describe sector rotation logic and the economic drivers of commercial real estate

## Frameworks Introduced
- **Fundamental present value (pricing) equation**: `P_t^i = Σ_{s=1..N} E_t[CF_{t+s}^i] / (1 + l_{t,s} + θ_{t,s} + π_{t,s} + γ^i_{t,s} + κ^i_{t,s} + φ^i_{t,s})^s` (additive approximation of the exact multiplicative discount rate).
  - When to use: as the checklist for any "how does macro variable X affect asset Y" question. Ask: does X change expected cash flows, the real rate, expected inflation, inflation-uncertainty premium, credit premium, equity premium or liquidity premium?
  - How: start from the real default-free rate `l`; add expected inflation `θ` (nominal default-free); add inflation-uncertainty premium `π`; add credit premium `γ` (credit-risky bonds); add equity premium `κ` over credit (equities, so equity RP vs government bonds `λ = γ + κ`); add liquidity premium `φ` (property, high yield, MBS in stress).
  - Why it works / failure mode: it forces separation of numerator and denominator effects. Failure mode: a single macro shock often moves both (higher real growth raises earnings and the real rate, so equity impact is ambiguous).
- **Stochastic discount factor (pricing kernel / inter-temporal rate of substitution)**: `m_{t,s} = δ·MU(C_{t+s}) / MU(C_t)`; real default-free zero price `P_{t,s} = E_t[m_{t,s}]`; one-period real rate `l_{t,1} = 1/E_t[m_{t,1}] − 1`.
  - When to use: to explain why risk premiums exist and when an asset has a negative premium.
  - How: price any risky payoff as `P = E[payoff]·E[m] + cov(payoff, m)`, i.e. `P_{t,s} = E_t[P_{t+1,s−1}]/(1+l_{t,1}) + cov_t(P_{t+1,s−1}, m_{t,1})`. First term is the risk-neutral present value; the covariance term is the discount for risk. Payoffs that are high when marginal utility is low (good times) have negative covariance, lower price, higher expected return.
  - Why it works / failure mode: it unifies all premiums as one covariance with consumption. Gap: the covariance is not observable, so premiums are inferred or measured ex post only.
- **Taylor rule (neutral rate logic)**: `pr_t = l_t + ι_t + 0.5(ι_t − ι*_t) + 0.5(Y_t − Y*_t) = l_t + 1.5ι_t − 0.5ι*_t + 0.5·gap`.
  - When to use: gauge whether the policy rate is neutral, too low, or too high (e.g. "too low for too long" 2002–2005 meant credit bubble risk), and where the front end of the curve is headed in each cycle phase.
  - How: neutral rate = real equilibrium rate + target inflation (gap = 0, inflation on target). Above-target inflation or positive output gap pushes the policy rate above neutral.
  - Failure mode: central banks do not follow it mechanically; `l_t` and the output gap are unobservable and revised.
- **Break-even inflation (BEI) decomposition**: `BEI = y_nominal − y_real (same maturity zero-coupon, default-free) = θ_{t,s} + π_{t,s}`.
  - When to use: reading market inflation expectations or comparing nominal vs linkers.
  - How: BEI over-states expected inflation when the inflation-uncertainty premium is positive; observed BEI falls in recessions (lower demand for resources, less pricing power) and when crisis demand for linkers compresses real yields.
- **Yield curve as expectations + risk premium**: curve slope = expected path of short rates (policy, inflation) + term (bond risk) premium rising with maturity.
  - When to use: interpreting a steep, flat or inverted curve. Inversion (downward slope) is largely an expectation of falling rates; a steep curve is ambiguous (expected hikes, premium, or both, or cuts more than offset by premium).
  - How: decompose yield changes into level, slope, curvature (principal components: about 93-95% level, 4.5-7% slope, 0.3% curvature for the US and UK, 1999–2014).
- **Credit premium from price (pricing-equation inversion)**: `γ ≈ (CF/P − 1) − (l + θ + π)` for a one-period bond; risk-neutral spread = expected loss `= PD × (1 − RR)`; the actual spread exceeds expected loss because defaults cluster in recessions and recoveries fall then.
  - When to use: to split a spread into expected loss and compensation for bearing credit risk (ties to ch04 building blocks).
- **Equity valuation macro drivers**: a high P/E can come from (a) higher expected real earnings growth, (b) lower real rates (often lower growth volatility), (c) lower expected inflation, (d) lower inflation uncertainty, (e) lower equity risk premium (or lower operating/financial risk). Use **CAPE** (real price / 10-year average real earnings) to smooth the cycle.
- **Commercial real estate as part bond, part equity, part illiquid**: discount rate = tenant-quality curve (real, nominal, or credit-risky rate) + equity-like premium for the end-of-lease residual value + liquidity premium.

## Key Concepts
- **Information vs news**: only the unanticipated part of a release changes prices; prices can fall on "good" data that was less good than expected.
- **Inter-temporal rate of substitution `m`**: ratio of discounted marginal utility of future to present consumption; high in bad times, low in good times.
- **Real default-free rate `l`**: proxied by short-dated inflation-indexed government yields; rises with trend real growth and with growth volatility.
- **Neutral policy rate**: policy rate when inflation is on target and the output gap is zero (= real equilibrium rate + target inflation).
- **Output gap**: log actual minus log potential GDP; positive means above sustainable capacity (rising inflation), negative means slack (unemployment).
- **Inflation-uncertainty risk premium `π`**: extra yield on nominal default-free bonds because the real payoff is uncertain; negligible for T-bills, larger for long maturities; not asset specific.
- **Break-even inflation rate**: nominal zero yield minus real zero yield of equal maturity; equals expected inflation plus `π`.
- **Term (bond risk) premium**: positive on average and rising with maturity because long bonds hedge bad consumption outcomes less well than short bonds; falls in crises when government bonds are prized as a haven.
- **Credit spread / credit premium**: spread vs government bond of same currency and maturity; conceptually akin to, not equal to, the credit premium because it embeds expected loss.
- **Expected loss**: `PD × (1 − recovery rate)`; loss rates are counter-cyclical.
- **Equity risk premium (ERP)**: `λ = γ + κ`; return over default-free long bonds; positive because equities are a poor hedge of bad consumption outcomes (they fall in recessions).
- **Consumption hedging**: ability of an asset to pay off when marginal utility of consumption is high; assets that hedge can have negative premiums.
- **Cyclical vs defensive (non-cyclical) sectors**: durable/discretionary vs staple earnings; cyclicals have the more volatile earnings and spreads.
- **Liquidity premium `φ`**: compensation for inability to exit at fair value in bad times (commercial property, high yield, MBS in stress).
- **CAPE**: Shiller cyclically adjusted P/E (real price over 10-year average real earnings).

## Formulas & Reference Tables
- Pricing: `P_t^i = Σ E_t[CF^i_{t+s}] / (1 + l_{t,s} + θ_{t,s} + ρ^i_{t,s})^s` (general, ρ = risk premium).
- Real one-period bond: `P_{t,1} = E_t[m_{t,1}]`; `l_{t,1} = (1 − P_{t,1})/P_{t,1} = 1/E_t[m_{t,1}] − 1`.
- Risk premium via covariance: `r_{t,s} − l_{t,1} = −(1 + l_{t,1})·cov_t(m_{t,1}, P_{t+1,s−1}) / P_{t,s}`; negative covariance means a positive premium; positive covariance (hedge) means negative premium.
- Nominal default-free: `P = Σ CF/(1 + l + θ + π)^s`; inflation-uncertainty premium for a one-year zero: `π ≈ CF/P − 1 − (l + θ)`.
- Credit-risky: `P = Σ E[CF]/(1 + l + θ + π + γ)^s`; `γ ≈ CF/P − 1 − (l + θ + π)`.
- Equity: `λ = γ + κ`; discount rate `l + θ + π + λ` (government-bond-referenced) over perpetual cash flows.
- Commercial property discount rates: (1) inflation-indexed government tenant `l + κ + φ`; (2) fixed nominal government tenant `l + θ + π + κ + φ`; (3) corporate tenant `l + θ + π + γ + κ + φ`.
- Taylor: `pr = l + ι + 0.5(ι − ι*) + 0.5(Y − Y*)`.
- Expected loss: `EL = PD × (1 − RR)`.
- Rating vs fundamentals (Moody's, Exhibit 18): 

| Rating | Aaa | Aa | A | Baa | Ba | B | Caa |
|---|---|---|---|---|---|---|---|
| Pre-tax interest coverage (x) | 17.6 | 7.6 | 4.1 | 2.5 | 1.5 | 0.9 | 0.7 |
| FOCF / total debt (%) | 42.3 | 28 | 13.6 | 6.1 | 3.2 | 1.6 | 0.8 |
| Total debt / capital (%) | 21.9 | 32.7 | 40.3 | 48.8 | 66.2 | 71.5 | 71.2 |

- **Premium-by-cycle-phase map (pricing-kernel view)**. Directional synthesis of the reading; the reading gives the signs, not magnitudes.

| Component | Early recovery / trough | Mid expansion | Late expansion / peak | Recession |
|---|---|---|---|---|
| Real rate `l` | low (low growth, but crisis safe-haven demand can push it negative) | rises with trend growth | high; highest if growth volatile | falls; falls further with flight to linkers |
| Expected inflation `θ` | low / falling | stable to rising | peaking, central bank tightening | falling (weak demand); BEI falls |
| Policy / short rate | cut to low | rising | high (above neutral if gap > 0) | cut; curve steepens |
| Curve slope | steep (short rates low, long anchored) | moderate | flat to inverted (cuts expected) | steep during recession as short end falls |
| Term premium `π` | positive; may fall in a haven rush | positive | variable | falls (bonds prized as consumption hedge) |
| Credit spread `γ` | narrows fast from wide; low quality outperforms | tight; weak issuers rally most | tightest, undiscerning | widens; cyclicals and low ratings widen most; quality outperforms |
| Equity RP `κ`/`λ` | high, falling | moderate | low | rises (earnings uncertainty and higher required return) |
| Earnings growth | sharp rebound (operating leverage) | steady | peaks | falls (US real earnings fell about 60% in 2009) |
| P/E | rises from trough | high | high | falls |

- Evidence points to remember: UK real-yield decline 1985–2007 matched fall in GDP volatility ("great moderation"); cross-section correlation of real yields with growth 0.57 and with growth volatility 0.74 (7 countries, July 2007); government bond total returns rise with maturity while correlation with GDP is mostly negative (hedge); average term spread 1900–2011 US 0.24%, UK 0.14%; ex post real ERP 2.2% (Switzerland) to 5.1% (Australia), US 4.5%, world 3.2% over 1900–2017, so ex ante 3-5% plausible; US trailing P/E averaged 13.5 for 1900–1990 and about 45 around 2000; next-10-year real US equity return after CAPE peaks (1929, 1965, 1999): −0.3%, −5.4%, −4.1% per year; after CAPE lows (1921, 1980): +12.3%, +7.3%.

## Mental Models
- **Numerator/denominator test**: for any macro headline write which piece of the pricing equation it moves; if it moves both (growth), the net sign is ambiguous until you know which dominates.
- **Premiums are prices of bad-times exposure**: an asset that pays in recessions (short government bonds, linkers, perhaps gold) earns a low or negative premium; assets that crash in recessions (equities, high yield, property) earn high premiums. Rank premiums by how much the asset loses when consumption is low.
- **Think of the curve as a bet on the policy path plus an insurance fee**: inverted = market expects cuts; steep = path up or fee up or both. Never read a steep curve as a pure forecast of hikes.
- **Spreads are a risk-appetite thermometer**: when spreads compress, weak credits rally most and investors stop discriminating; when they widen, quality wins. So "reach for yield" works near troughs and fails near peaks.
- **Real estate = bond + equity stub + illiquidity**: stable rents (bond-like) with volatile capital values (equity-like, pro-cyclical); required premium sits near equities, plus a liquidity add-on.
- **Expectations first**: valuation reacts to the surprise vs priced-in consensus, not to the level of good or bad data.

## Worked Example
**Pricing-kernel risk premium on a default-free two-period bond (all recomputed).** Two states: bad (p = 0.4), good (p = 0.6). Kernel `m` = 0.954676 (bad), 0.954379 (good). `E[m] = 0.954498`, so `l_{t,1} = 1/0.954498 − 1 = 4.7671%`. Next-period price of the bond (then a one-period bond): 0.839181 (bad), 0.954840 (good); `E[P] = 0.908576`. Risk-neutral value `0.908576/1.047671 = 0.867234`. Market price `= Σ p·P·m = 0.867226`. Covariance `= 0.867226 − 0.867234 ≈ −0.000008` (direct computation −0.0000082). Expected holding-period return `= (0.908576 − 0.867226)/0.867226 = 4.768%`, premium over the real one-period rate about 0.001% (1 bp). Interpretation: the price is lower than the risk-neutral value because the bond falls in value in the bad state when marginal utility is high; doubling shock volatility widens the covariance to −0.000033 and the premium rises.

**Inflation-uncertainty and credit premia (one-year zero-coupons).** Real rate 1.25%, expected inflation 2.5%. Government zero priced 95.92 per 100: `100/95.92 − 1 = 4.2535%`; minus `(1.25 + 2.5) = 3.75%` gives `π ≈ 0.504%`. Corporate zero priced 94.21: `100/94.21 − 1 = 6.146%`; minus `(1.25 + 2.5 + 0.50)` gives `γ ≈ 1.90%`. Property decision (Supermarket plc lease): discount rate = 5.75% bond yield + 0.5% property risk premium + 1.0% liquidity = 7.25%; 10 rents of 500,000 plus 10,000,000 resale value at year 10 gives PV 8,437,796 (recomputed). Asking 8.2 million is below value, so the implied return is about 7.64% (> 7.25% hurdle): buy.

## Anti-patterns
- **Treating break-even inflation as expected inflation**: it includes the inflation-uncertainty premium (and liquidity effects in linkers), so it overstates expectations when `π > 0`; falling BEI can mean lower expectations, lower premium, or both.
- **Reading an upward-sloping curve as a forecast of rate rises**: positive term premia can mask flat or falling expected rates.
- **Equating credit spread with credit premium**: part of the spread is expected loss (`PD × (1 − RR)`); also recoveries fall just when defaults rise.
- **Assuming growth is automatically good for equities**: faster real growth raises earnings but also the real rate; outcome ambiguous.
- **Using the long-run average P/E as fair value**: equilibrium P/E moves with real rates, inflation, inflation uncertainty and ERP; a P/E above history can be justified (but CAPE extremes preceded poor 10-year returns).
- **Forgetting that supply, regulation and haven demand distort government curves** (UK pension rules/FRS17 inverting the long gilt end; Asian reserve buying; Dutch pension hedging pushing 30y below 10y).
- **Treating "default-free" as a given**: 2010–2012 euro crisis and sovereign CDS (Italy, Spain, Ireland) showed a non-zero sovereign credit premium; EM sovereigns carry one structurally.

## Exam Focus & Traps
- Risk premium is high when the future payoff is **negatively** related to the marginal utility of future consumption (pays little when an extra unit of consumption is most valuable); equivalently the covariance of price with `m` is negative. Hedging assets have the opposite sign and **negative** premia.
- Real rate is **positively** related to both trend real growth and the **volatility** of growth (counter-intuitive for volatility).
- Output gap > 0 means above sustainable capacity and higher inflation, not unemployment. Taylor example: l = 2%, inflation 3%, target 2%, gap 2% gives 6.5% (2 + 3 + 0.5 + 1).
- BEI question: if expected inflation rises while inflation uncertainty falls, the BEI direction is **indeterminate**; if BEI = 2.0% and `π` > 0, expected inflation is **below** 2.0%.
- Recession curve: short rates cut, long rates move less, so the curve **steepens**; late-expansion peak: **flattens or inverts** (inverted curve predicts recession). Flat curve plus predicted recession gives upward slope.
- Recession spreads: widen; AAA outperforms B-rated, cyclical + low rated widen most; when spreads narrow, lower-rated outperform (the "undiscerning" phase).
- Equilibrium P/E falls if inflation expectations rise, ERP rises, or real rates rise; rises if inflation uncertainty falls.
- Short-dated default-free bonds are the best consumption hedge; long-dated are less so (term premium); equities are the worst of the liquid classes.
- Property: rental income stable, capital values cyclical; the discount-rate difference vs equity is **liquidity**.
- Higher wealth lowers required risk premium (decreasing absolute risk aversion; marginal utility falls).
- Errata check: no 2022 Level II errata entry for Reading 42 was found in the errata file; Reading 42 content used as printed.

## Key Takeaways
1. Run every macro view through the pricing equation: real rate, expected inflation, inflation-uncertainty, credit, equity and liquidity premia, plus cash flows. Name which term moves.
2. Real rates rise with trend growth and growth volatility; falling volatility (great moderation) lowers real rates and lifts valuations.
3. Policy rate is anchored by neutral (real equilibrium + target inflation) and deviates with inflation and the output gap; "too low for too long" signals bubble risk.
4. Curve shape mixes expectations and term premium: inverted means cuts are expected; steep is ambiguous; recessions steepen, late expansions flatten.
5. Credit spreads are counter-cyclical, and widen most for cyclical, low-rated issuers; use quality over reach as cycles turn, reach for yield near troughs.
6. The equity premium exists because equities fail as a consumption hedge; ex ante 3-5% for developed markets; use CAPE for valuation context, with 10-year forward returns historically inversely linked to starting CAPE.
7. Cyclical earnings fall hardest in recessions and rebound hardest early in recoveries; defensives (staples) smooth the path: this is the economic logic of sector rotation.
8. Commercial property needs a discount rate of the tenant-quality curve plus an equity-like premium plus an illiquidity premium, and its capital values are pro-cyclical.

## Connects To
- **ch03**: macro framework and forecasting pitfalls that produce the growth, inflation and policy inputs used here.
- **ch04**: building-block (term, credit, liquidity) and Grinold-Kroner expected returns are the quantified versions of the premia derived here.
- **ch06**: strategic vs tactical allocation uses cycle-phase views of these premia.
- **ch07**: liability-relative and goal-based allocation depend on the real-rate and inflation premium logic.
- **`ilmanen-yield-curve` ch03**: bond risk premium, duration extension, term premium and the expectations-vs-premium curve decomposition.
- **`cfa-economics` ch04**: business cycle phases that drive the policy-rate and slope paths.
- **`cfa-derivatives` ch07**: currency and rate-hedging considerations when policy and inflation paths diverge across countries.
