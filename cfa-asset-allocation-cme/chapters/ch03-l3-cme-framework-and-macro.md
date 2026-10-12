# Chapter 3: Capital Market Expectations, Part 1: Framework and Macro Considerations
> **Source**: CFA Program Curriculum 2023, Level III, Reading 3 · Portfolio Management (Asset Allocation) | Christopher D. Piros, PhD, CFA

## Core Idea
Capital market expectations (CME) are forecasts of risk and return for asset classes; they are the input that turns an investment policy statement into a strategic (and tactical) asset allocation. The goal is not pinpoint accuracy for each asset class but a realistic overall return level plus internal consistency across asset classes (cross-sectional) and across horizons (intertemporal). A disciplined seven-step process, a catalogue of data and behavioral pitfalls, and a macro toolkit (trend growth, business cycle, inflation, monetary and fiscal policy, yield curve, international linkages) turn history and economics into forward-looking expectations. Part 2 (ch04) builds asset-class-specific forecasts on this base.

## Learning Outcomes Covered
- discuss the role of, and framework for, CME in portfolio management
- discuss challenges in developing capital market forecasts
- explain how exogenous shocks affect economic growth trends
- apply trend growth analysis to CME (labor + productivity, anchoring bonds and equities)
- compare econometric, indicator and checklist approaches to economic forecasting
- discuss how business cycles affect short- and long-term expectations (five phases)
- relate inflation to the cycle and to cash, bonds, equity, real estate returns
- discuss monetary and fiscal policy effects on the cycle (Taylor rule, zero and negative rates, policy mix)
- interpret the yield curve as an economic predictor and link it to policy
- identify macro, interest rate and exchange rate linkages between economies

## Frameworks Introduced
- **Seven-Step CME Framework**: a disciplined routine to produce documented, consistent expectations.
  - When to use: any institution that sets strategic or tactical allocations from explicit forecasts.
  - How: (1) specify the expectations needed (asset-class universe, horizons); (2) research the historical record and return drivers; (3) choose methods/models and their information needs; (4) determine the best data sources and frequencies; (5) interpret the current environment with common assumptions and consistent judgment; (6) provide and document the expectations with their reasoning; (7) monitor outcomes versus expectations and feed back.
  - Why it works / failure mode: forces explicit assumptions and one set of inputs for all asset classes. The universe should include every class that gets a distinct allocation but be as small as possible. Feedback is limited because a meaningful hypothesis test needs about 30 observations, so step 7 is often qualitative.
- **Good-forecast test**: unbiased, objective and well researched; efficient (small errors); internally consistent across asset classes and horizons.
- **Pitfall Checklist for Forecasts** (nine families): data limits (timeliness, revisions, redefinitions, rebasing); measurement errors (transcription, survivorship, appraisal smoothing); historical-estimate limits (nonstationarity, asynchronicity, fat tails); ex post risk as a biased proxy for ex ante risk (peso problem); method biases (data mining, time period); ignoring conditioning information; misread correlation; psychological biases; model uncertainty.
  - When to use: before accepting any historical statistic or empirical relationship as a forecast input.
  - How: for each input ask what regime it comes from, whether it was known in real time, whether an economic rationale exists ("no story, no future"), and whether it holds out of sample.
- **Regime-Relevance Test (two questions)**: (1) Is there a reason to believe a fundamental regime change occurred in the sample? (2) Do the data support that it occurred? If both yes, use only the relevant sub-period or a statistical technique that models regime shifts; otherwise use the longest history with reasonable stationarity (more observations give more precise estimates).
- **Conditional vs unconditional forecasting**: compute expected returns state by state (expansion, recession), then probability-weight. Do not average the inputs first (see Worked Example 1).
- **Trend Growth Decomposition**: potential GDP growth = labor input growth (potential labor force size + participation) + labor productivity growth (capital deepening + total factor productivity, TFP).
  - When to use: initial estimate of long-run growth; extrapolate component trends, then adjust for known differences. Mature economies are stable; emerging economies need larger adjustments.
  - Why it matters: trend growth disciplines DCF earnings forecasts, links to average real default-free yields (faster trend growth implies higher average real yields), sets the inflation-safe speed limit for actual growth, and anchors long-run equity appreciation.
- **Equity Value Anchor**: `V_e = GDP × S_k × PE`. In the long run neither capital's share of income nor the P/E can rise forever, so aggregate equity value grows at about nominal GDP growth; over finite horizons add the expected change in `S_k` and in P/E. Dividend yield = payout ratio / P/E (set any two, infer the third). Higher-growth countries do not reliably earn higher equity returns because growth is priced and capital deepening can depress returns on capital.
- **Three Economic Forecasting Approaches**: econometric models, indicators, checklists (see table below); use a blend.
- **Five-Phase Business Cycle Map**: initial recovery, early expansion, late expansion, slowdown, contraction, each with typical policy, rates, curve and asset behavior (table below). Business cycle information is most valuable over horizons of roughly 1-3 years.
- **Inflation Transmission by Asset Class**: cash (floating real rate), bonds (discount-rate effect only), stocks (cash flows and discount rates move together if inflation stays in the expected range), real estate (leases and supply) (table below).
- **Taylor Rule**: `i* = r_neutral + π_e + 0.5(Y_e − Y_trend) + 0.5(π_e − π_target)`. Use as a framework for the central bank's stance and likely path, not as a mechanical forecast; every input is unobservable and judgmental.
- **Policy-Mix Matrix**: persistent loose fiscal policy raises real rates; persistent loose monetary policy raises expected inflation; nominal rates are high (loose-loose), low (tight-tight) or mid (mixed).
- **Negative-Rate CME Rule**: do not use an observed negative policy rate as the risk-free baseline for long-run expectations; use the long-run equilibrium short rate (`r_neutral` plus a small spread), and model short-horizon paths that converge to it.
- **External Balance Identity**: `(X − M) = (S − I) + (T − G)`; the capital account mirrors the current account.
- **Impossible Trinity** (policy trilemma): free capital flows, a fixed exchange rate and independent monetary policy cannot coexist.

## Key Concepts
- **Capital market expectations (CME)**: expectations about the risk and return prospects of asset classes, used in strategic and tactical asset allocation.
- **Cross-sectional consistency**: expectations for different asset classes derive from common assumptions so combined portfolios make sense.
- **Intertemporal consistency**: short-horizon forecasts converge to and are compatible with long-horizon forecasts.
- **Regime / nonstationarity**: a change in the governing risk-return relationships, so different parts of a series have different statistical properties.
- **Survivorship bias**: a series that includes only entities that survived, overstating returns (notorious for hedge fund data).
- **Appraisal (smoothed) data**: appraisals replace transactions for illiquid assets, biasing volatility down and correlations with other assets down.
- **Asynchronicity**: observations labelled the same date are not simultaneous (time zones), distorting correlations and creating false lead-lag effects; worse at daily and weekly frequency.
- **Peso problem**: prices embed fear of a rare negative event that did not occur in the sample, so ex post returns overstate and ex post risk understates what was expected ex ante (the opposite error appears if one rare event is in a short sample, overstating tail risk such as VaR).
- **Data-mining bias**: searching a dataset until a significant pattern appears; test with an economic rationale and out-of-sample data.
- **Time-period bias**: results driven by start and end dates (the small-cap premium swings from about 0.4% to 3.5% a year depending on the start year).
- **Conditioning information**: current economic and market state used to adjust risk and return; ignoring it yields unconditional forecasts that mislead.
- **Analyst biases**: anchoring, status quo, confirmation, overconfidence, prudence, availability.
- **Model, parameter and input uncertainty**: wrong structure; estimated-with-error parameters; incorrect or proxied inputs (for example a proxy for the market portfolio). Model uncertainty is potentially the most serious.
- **Exogenous shocks**: policy changes, new technology, geopolitics, natural disasters, natural resources/critical inputs, financial crises; they can alter trend growth, level of output or both.
- **Output gap**: trend-implied GDP minus actual GDP; large negative in recovery, closed in late expansion.
- **Leading, coincident, lagging indicators; diffusion index**: indicators ahead of, with and behind the cycle; the diffusion index counts how many components point up.
- **Look-ahead bias (LEI)**: the revised indicator history fits past cycles better than it did in real time.
- **Nowcasting (for example GDPNow)**: real-time estimate of current-quarter GDP, a forecast of the advance estimate; volatile early in the quarter and silent beyond quarter-end.
- **Automatic stabilizers**: progressive taxes and means-tested transfers that dampen cycles without legislation.
- **Quantitative easing (QE)**: large-scale central bank purchases of high-quality securities funded by new reserves.
- **Zero lower bound**: the belief that policy rates cannot go below zero because investors would hold currency; negative policy rates proved sustainable since deposit and reserve convenience value exceeds the small negative rate.
- **Current account / capital account**: net goods, services, income and transfers versus net FDI and portfolio flows; they sum to zero by construction.

## Formulas & Reference Tables
Symbols: `i*` target nominal policy rate; `r_neutral` real policy rate if growth is at trend and inflation on target; `π_e`, `π_target` expected and target inflation; `Y_e`, `Y_trend` expected and trend real growth; `X, M` exports, imports; `S, I` private saving, investment; `T, G` taxes, government spending.

- Taylor rule: `i* = r_neutral + π_e + 0.5(Y_e − Y_trend) + 0.5(π_e − π_target)`
- Real-rate form: `i* − π_e = r_neutral + 0.5(Y_e − Y_trend) + 0.5(π_e − π_target)` (the real policy rate deviates from neutral by half the growth and inflation gaps).
- Equity value: `V_e = GDP × S_k × PE`; `g_equity ≈ g_nominalGDP + Δ(S_k) + Δ(PE)`; `dividend yield = payout / PE`
- Return decomposition used in the reading (log): `r ≈ real GDP growth + inflation + Δ(EPS/GDP) + Δ(P/E) + dividend yield`
- Trend growth: `g_potential ≈ g_labor input + g_labor productivity` (productivity = capital deepening + TFP)
- Conditional CAPM: `E(R | state) = R_f + β_state [E(R_M | state) − R_f]`; unconditional `E(R) = Σ p_state × E(R | state)`
- External balance: `(X − M) = (S − I) + (T − G)`
- Regime-weighted forecast: `E(R_horizon) ≈ w_exp × r_exp + w_con × r_con`, with the weights drifting from the current phase toward the long-run frequencies as the horizon lengthens.

| Approach | Strengths | Weaknesses |
|---|---|---|
| Econometric models | Quantitative, consistent, tests effect of exogenous changes, can be robust | Complex, needs forecasts of exogenous inputs, mis-specification risk, false precision, weak at turning points |
| Leading indicators | Simple, intuitive, aimed at turning points, easy to obtain | Revisions and look-ahead bias, overfit in sample, false signals, often only binary guidance |
| Checklists | Flexible, broad, structural change easy to add | Subjective, time-consuming, inconsistent over items and time, prone to bias |

| Phase | Policy | Short rates | Bond yields / curve | Assets |
|---|---|---|---|---|
| Initial recovery (short, a few months) | Stimulative, shifting to tightening | Low, bottoming | Long yields bottoming; curve steep | Stocks rise briskly; small caps, high yield, EM do well |
| Early expansion | Withdrawing stimulus | Moving up | Stable or slightly rising; curve flattening | Stocks trend up; profits rise fast |
| Late expansion | Becoming restrictive | Rising, above average | Rising more slowly; curve flattening from the long end inward | Stocks volatile; cyclicals lag, commodities and inflation hedges lead |
| Slowdown | Tight | At or near peak | Yields peak, may fall sharply; curve flat or inverted | Credit spreads widen; utilities and quality stocks best |
| Contraction (typically 12-18 months) | Progressively stimulative | Falling | Falling; curve steepens, steepest near next recovery | Stocks fall early but turn up before recovery; spreads wide until trough |

| Persistent policy mix | Real rates | Expected inflation | Nominal rates |
|---|---|---|---|
| Loose fiscal, loose monetary | High | High | High |
| Tight fiscal, loose monetary | Low | High | Mid |
| Loose fiscal, tight monetary | High | Low | Mid |
| Tight fiscal, tight monetary | Low | Low | Low |

| Asset | Effect of inflation (within expected cyclical range / outside it) |
|---|---|
| Cash (floating short-term instruments) | Roughly zero duration, floating real rate; attractive when rates rise; deflation is attractive only if the zero bound binds |
| Nominal bonds | Pure discount-rate effect: rising inflation causes capital losses; if inflation leaves the expected range the long end moves more; deflation helps top-quality, hurts low-quality credit |
| Stocks | Little effect while cash flows and discount rates move together; threat if inflation is unexpectedly high (central bank must brake) or very low (recession); pricing-power firms gain, asset-intensive, commodity and leveraged firms hurt by deflation |
| Real estate | Leases reprice over time; unexpected inflation tends to lift values but depends on lease length and supply; deflation hurts non-prime property |

Cycle facts (NBER, US, since 1854): about 66 cycles, average 56 months peak to peak, shortest 17 and longest 128 months; contraction averaged about 17 months, expansion about 39 months.

## Mental Models
- **Anchor then tilt**: use trend growth (and its link to yields and equity value) as the long-run anchor, then add cyclical and policy tilts that fade toward the anchor as the horizon grows.
- **Horizon dial**: over 3 months to 3 years the current cycle phase has most signal; beyond that, forecasts converge to the cycle-averaged unconditional mean; below about 3 months, transitory market noise dominates.
- **Slope equals expected short rates plus term premium**: steep at the trough, flat or inverted at the peak, re-steepening in contraction; the term premium is itself procyclical, so inverted inflation expectations need not mean an inverted curve.
- **Pushing versus pulling on a string**: restrictive policy works reliably, expansionary policy at the bottom does not; monetary policy errors are most likely at the top.
- **No story, no future**: a statistical relationship without an economic rationale and out-of-sample support is data mining until proven otherwise.
- **Consistency over precision**: a set of coherent, documented expectations beats a few brilliant but mutually inconsistent calls.

## Worked Example
**1. Conditional vs unconditional CAPM (recomputed).** Risk-free 2%. Beta is 0.8 in expansion and 1.2 in recession; market return is 12% and 4%; each state has probability 0.5.
- Expansion: `2% + 0.8 × (12% − 2%) = 10.0%`. Recession: `2% + 1.2 × (4% − 2%) = 4.4%`.
- Unconditional expected return: `0.5 × 10.0% + 0.5 × 4.4% = 7.2%`.
- Shortcut (wrong): average beta 1.0 and average market return 8%, giving `2% + 1.0 × 6% = 8.0%`. It overstates by 0.8% because beta is high when the market premium is low; the product of averages differs from the average of products. Interpretation: always compute state by state, then weight.

**2. Taylor rule.** `r_neutral = 2.25%`, target inflation 2%, trend growth 2.5%, expected growth 3.5%, expected inflation 3%.
- `i* = 2.25% + 3% + 0.5 × (3.5% − 2.5%) + 0.5 × (3.0% − 2.0%) = 2.25 + 3 + 0.5 + 0.5 = 6.25%`.
- Real policy rate = `6.25% − 3% = 3.25%`, which is 1.0 percentage point above neutral (half of 1% + half of 1%, equals 1%). Interpretation: policy is restrictive; expect higher short rates and a flatter curve.

**3. Equity return check against growth (1946-1999 style).** Components of the 12.18% log return: real GDP 3.14, inflation 4.12, EPS/GDP 0.00, P/E 0.95, dividend yield 3.97 (they add to 12.18).
- The P/E contributed `54 × 0.95% = 51.3%` cumulative, or `exp(0.513) = 1.67`, so the market stood about 67% above growth-consistent value.
- Forward baseline with labor input 0.9%, productivity 1.5%, inflation 2.1%, dividend yield 2.25%, no P/E change: `0.9 + 1.5 + 2.1 + 2.25 = 6.75%`.
- If the P/E premium is expected to unwind over 30 years: `51.3% / 30 = 1.71%` a year, giving about 5.04% a year; over 5 years: `51.3% / 5 = 10.26%`, giving `6.75 − 10.26 = −3.51%` a year. Interpretation: historical averages carrying valuation expansion must be stripped before use.

**4. Horizon and cycle weights.** Regime model: equities +2% a month in expansion, −2% in contraction; expansions average 39 months, contractions 20, so long-run weights are about 2/3 and 1/3 (39/59 = 0.66), and the unconditional return is `(2/3)(2%) + (1/3)(−2%) = 0.67%` a month, about 8% a year. If the economy starts in contraction: 3 months is about −6% cumulative; a 1-year forecast about −18% (less than −24%); 5 years with weights 0.6/0.4 gives `12 × (0.6 × 2% − 0.4 × 2%) = 4.8%` a year; 10 years is close to 8%. Interpretation: the longer the horizon, the closer the forecast is to the unconditional average.

## Anti-patterns
- Extrapolating the longest historical mean as the expected return (the late-1990s approach that produced double-digit projections and underfunding).
- Using revised data or revised LEI history as if known in real time (look-ahead bias).
- Mixing index bases or ignoring redefinitions (for example CPI methodology changes).
- Using appraisal-based volatilities and correlations directly in an optimizer.
- Treating a one-off event in a short window as a stable tail probability, or ignoring a feared event that did not occur.
- Averaging beta and market return separately across states.
- Using a negative observed policy rate as the risk-free rate in a building-block model.
- Assuming higher GDP growth countries have higher equity returns without checking valuation and return on capital.
- Using business cycle phase calls for 10-year expectations, or for horizons of a few days.
- Presenting model output with false precision and no sensitivity to the exogenous inputs.
- Treating the Taylor rule output as the actual policy rate.

## Exam Focus & Traps
| Trap | Correct reading |
|---|---|
| Higher-frequency data improve precision of the mean | They improve variance, covariance and correlation precision, not the sample mean |
| Covariance matrix with more assets than observations | Needs observations greater than assets, otherwise some portfolios show spurious zero risk; use a factor structure |
| Peso problem direction | Feared event not occurring: returns biased up, risk biased down; rare event occurring in the sample: tail risk overstated |
| Appraisal data | Volatility biased down and correlations understated |
| Status quo versus anchoring versus availability | Status quo: perpetuate recent observations; anchoring: first number dominates; availability: vivid or recent events dominate; prudence: dampening forecasts to avoid career risk |
| Unconditional return | Probability-weight state-by-state conditional returns |
| Trend growth and yields | Real default-free yields tied to real trend growth, nominal to nominal |
| Equity-GDP link | Aggregate equity value grows with nominal GDP in the long run; dividend yield is separate |
| Cycle phase yield curve | Steep at recovery and contraction end, flat or inverted at slowdown |
| Inflation and stocks | Little effect only while inflation stays within the expected range |
| Policy mix | Fiscal moves real rates, monetary moves expected inflation; mixed combinations give ambiguous nominal rates |
| Taylor rule coefficients | 0.5 on both gaps; expected (not current) inflation and growth |
| Fiscal vs monetary policy for the cycle | Monetary policy is the key cyclical tool; fiscal is secondary except automatic stabilizers and major regime change |
| Negative rates | Do not use as the baseline risk-free rate; use the long-run equilibrium rate |
| Current and capital accounts | Mirror images; a tax cut raises the current account deficit and the capital account surplus; exchange rate effect is ambiguous a priori |
| Shared yield curves across countries | Two markets share a yield curve only with free capital mobility and a credibly permanent fixed rate; a weaker currency link implies higher yields |
| Real rate differentials | Not automatically exploitable because PPP fails over investment horizons |
| Nowcasting scope | GDPNow forecasts the advance estimate only for the current quarter |

## Key Takeaways
1. Follow the seven-step CME routine and judge success by consistency across asset classes and horizons, not by point accuracy for one class.
2. Get the overall return level right: realistic forward-looking return projections matter more than precision in any single asset class.
3. Screen every historical input for regime change, survivorship, smoothing, asynchronicity, ex post bias, data mining, time period and conditioning information.
4. Anchor long-run bonds on trend real (nominal) growth and equity appreciation on nominal GDP growth, then adjust for share-of-profit and valuation changes.
5. Combine econometric, indicator and checklist approaches; business cycle information is most valuable for 1-3 year horizons.
6. Map each cycle phase to policy, short rates, curve slope and assets; the curve steepens in contraction and flattens or inverts at the peak.
7. Use the Taylor rule as a stance framework, treat negative-rate and QE periods with scenarios converging to an equilibrium neutral rate, and read the policy mix for real versus nominal rates.
8. Link economies through the current and capital accounts, rate and exchange rate expectations, and the trilemma; real rate differentials need a currency view.

## Connects To
- **ch04**: asset-class-specific forecasting (equity, fixed income, real estate, currencies) that applies this framework.
- **ch05**: pricing-kernel and economic-factor view of investment markets; the L2 treatment of the same cycle, policy and curve relationships.
- **ch01**: behavioral biases of individuals; the analyst biases here (anchoring, confirmation, overconfidence) are the same effects applied to forecasting.
- **ch02**: behavioral finance in the investment process (analyst forecasts, committees) and remedies that mitigate forecasting bias.
- **ch06**: strategic asset allocation consumes these expectations.
- **ch07**: optimization and Black-Litterman depend on consistent CME inputs.
- **`cfa-economics`**: growth, business cycles, monetary and fiscal policy, trade and exchange rates behind the macro layer.
- **`cfa-fixed-income`**: yield curve dynamics and term structure behind slope interpretation.
