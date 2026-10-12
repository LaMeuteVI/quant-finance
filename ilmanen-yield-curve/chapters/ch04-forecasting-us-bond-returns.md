# Chapter 4: Forecasting U.S. Bond Returns
> **Source**: Antti Ilmanen, *Understanding the Yield Curve, Part 4: Forecasting U.S. Bond Returns*, Salomon Brothers U.S. Fixed-Income Research (August 1995)

## Core Idea
The bond risk premium is **time-varying and partly predictable**. Four market-based predictors together explain about **10%** of the monthly variation in the 20-year Treasury's excess return over 1965–95: **term spread, real yield, inverse wealth (a depressed stock market), and momentum**. The combined out-of-sample forecast has the right sign about **61%** of the time, and its correlation with the next 12 months' excess return is **0.57**. Dynamic duration strategies built on it (the "scaled" and "1/0" strategies) earned far higher returns and Sharpe ratios than static bond holdings, consistently across decades. The economic story is a **cycle of fear and greed**: investors demand high premia near troughs, when wealth is low, and bid premia down near peaks.

## Frameworks Introduced
- **Cycle of fear and greed (wealth-dependent risk aversion)**:
  - Required premia rise when risk rises (rate volatility, stock–bond covariance, inflation uncertainty) or when aggregate risk aversion rises.
  - Risk aversion rises when current wealth is low **relative to past wealth**. So expected excess returns of stocks and bonds are high at the **end of recessions** and low at the **end of expansions**.
  - Alternative explanations: lagged portfolio flows (poor stock returns push money into bonds), sentiment swings, and underreaction of long-rate expectations to inflation shocks.
- **The four-predictor model**:

  | Predictor | Definition | Role | Sign |
  |---|---|---|---|
  | **Term spread** | 5y spot − 3m spot | overall BRP proxy (contaminated by rate expectations) | + |
  | **Real yield** | 5y spot − latest year-on-year CPI | inflation-adjusted value / BRP proxy | + |
  | **Inverse wealth** | `0.1·(Wₜ₋₁ + 0.9Wₜ₋₂ + 0.9²Wₜ₋₃ + …)/Wₜ`, W = S&P 500 total-return level | risk-aversion proxy and a filter for the term spread | + |
  | **Momentum** | +1 if the long yield is >5bp below its 6-month moving average, −1 if >5bp above, 0 inside the 10bp band | trend following, anti-whipsaw band | + |

  - Why combine them: a steep curve with a **depressed** stock market more likely reflects a high required premium (tightening and inflation are unlikely). A steep curve with a **strong** stock market more likely reflects expected hikes. Inverse wealth filters the expectations "noise" out of the term spread.
  - The first three are **value** indicators (buy when markets are weak). Momentum is a **trend** indicator that complements them.
- **Out-of-sample discipline against data snooping**:
  - Each month, re-estimate the regression on an **expanding window** of data available at that date (start 1955–64 → forecast January 1965), then forecast next month.
  - Choose predictors on economic grounds, check subperiod stability, and test on data after the relation was identified.
  - In-sample results overstate performance. The scaled strategy earned 11.15% in-sample against 8.64% out-of-sample.
- **Dynamic strategies (self-financed, vs 1-month bill)**:
  - **Scaled**: hold (predicted monthly excess return in %) units of the 20y bond. For example 0% → cash, +1% → 1 unit, +2% → 2 units (leveraged), −1% → short 1 unit. The Sharpe ratio is independent of the scaling constant.
  - **1/0**: hold 1 unit if the prediction is > 0, else cash. It uses only the sign, trades about 1.5 times a year, never shorts, and is less risky.
  - Static benchmarks: **always-bond** and a **50/50 bond–cash** mix.
- **Critical-questions checklist for any backtest**:
  1. Economic reason?
  2. Out-of-sample?
  3. Stable across subperiods (rolling correlations, decade splits, cumulative wealth plots)?
  4. Transaction costs?
  5. Risk-adjusted (Sharpe, downside)?
  6. Could the excess return be fair pay for bearing risk at high-risk-aversion times?
- **From forecast to target duration** (benchmark 4 years):

  | Predicted excess return | Aggressive | Moderate | Conservative |
  |---|---|---|---|
  | Negative | −2 | 0 | 3.0 |
  | Low | 1 | 2 | 3.5 |
  | Average | 4 | 4 | 4.0 |
  | High | 7 | 6 | 4.5 |
  | Very high | 10 | 8 | 5.0 |

  Implement with on-the-run Treasuries or futures. The duration range scales with risk aversion and confidence in the model.

## Key Concepts
- **Expected excess bond return / near-term BRP**: the one-month expected return of the long bond over the 1-month bill.
- **Long-run BRP**: the long-run average expected return of a long-duration strategy over a short-duration one. It differs from the near-term BRP when the premium is abnormally high or low.
- **Inverse wealth**: an exponentially weighted (λ = 0.9) past stock level divided by the current level. It is above 1 after a stock decline and below 1 in a steady bull market (about 0.91 at 1% monthly growth). It was below 1 in 84% of months.
- **Momentum dummy**: a moving-average breakout rule with a neutral band to avoid whipsaws.
- **In-sample vs out-of-sample forecast**: fitted values with full-sample coefficients involve peeking. Expanding-window re-estimation uses only information available at the time.
- **Data-snooping bias**: spurious "findings" produced by intensive searching of the same data.
- **Correct-sign frequency (hit rate)**: the share of months in which the forecast and realized excess return have the same sign. It is 61% monthly and stable near 60% across subperiods.
- **Career risk**: the risk of unconventional underperformance relative to peers. "Better to lose conventionally than to gain unconventionally" deters managers from slow, high-odds strategies.
- **Tactical asset allocation**: dynamic shifting between bonds and cash based on return forecasts.

## Formulas & Reference Tables
- Forecast model (1965–95 full-sample OLS; monthly excess return in % per month, continuously compounded):
  `E(excess return) = −10.15 + 0.37·TermSpread + 0.20·RealYield + 9.85·InverseWealth + 0.34·Momentum`
  - t-stats: −4.98, 2.24, 2.89, 4.81, 2.02. R² = 10.3%.
- Inverse wealth: `IWₜ = 0.1·Σₖ≥₀ 0.9ᵏ·Wₜ₋₁₋ₖ / Wₜ`

**Correlation with next month's 20y excess return, 1965–95**

| Yield level | Lagged return | Bond volatility | Term spread | Real yield | Inverse wealth | Momentum | **Combination** |
|---|---|---|---|---|---|---|---|
| 0.11 | 0.05 | 0.03 | **0.21** | **0.16** | **0.14** | **0.09** | **0.32** |

**Conditional average excess returns (annualized), 1965–95**

| Condition at month start | Share of months | 20y excess return |
|---|---|---|
| Term spread > 0 / < 0 | 87% / 13% | +2.63% / −12.40% |
| Inverse wealth > 1 / < 1 | 16% / 84% | +6.24% / −0.36% |
| TS > 0 and IW > 1 | 12% | **+11.95%** |
| TS > 0 and IW < 1 | 75% | +1.23% |
| TS < 0 and IW > 1 | 4% | −9.76% |
| TS < 0 and IW < 1 | 9% | **−13.60%** |

**Strategy performance, 1965–95 (excess over 1m bill, annualized)**

| Strategy | Avg excess | Volatility | Sharpe |
|---|---|---|---|
| Scaled (4 predictors) | 8.64% | 12.80 | 0.68 |
| 1/0 (4 predictors) | 4.16% | 7.92 | 0.53 |
| Always-bond | 0.67% | 10.42 | 0.06 |
| 50/50 bond–cash | 0.33% | 5.21 | 0.06 |
| Scaled / 1/0 on term spread only | 3.87% / 2.96% | — | — |

**By subperiod (Sharpe ratio)**

| Strategy | 1965–74 | 1975–84 | 1985–94 | 1990–95 |
|---|---|---|---|---|
| Scaled | 0.72 | 0.75 | 0.87 | 1.10 |
| 1/0 | 0.16 | 0.36 | 0.84 | 0.86 |
| Always-bond | −0.38 | −0.14 | 0.56 | 0.63 |

Both dynamic strategies beat the 50/50 mix by at least 200bp in every decade.

**Signal strength (f = forecast, % per month)**

| f | < −1 | −1 to −0.5 | −0.5 to 0 | 0 to 0.5 | 0.5 to 1 | > 1 |
|---|---|---|---|---|---|---|
| Correct sign | 65% | 63% | 65% | 53% | 57% | 67% |
| Avg excess return (annualized) | −15.68 | −3.80 | −8.57 | 3.92 | 4.15 | 15.66 |
| Share of months | 9% | 11% | 19% | 25% | 21% | 15% |

**Horizon effect: frequency of beating or matching both cash and bond**

| Horizon | Month | Quarter | Year | 3 years | 5 years |
|---|---|---|---|---|---|
| Scaled | 35% | 46% | 58% | 85% | 92% |
| 1/0 | 61% | 58% | 64% | 73% | 92% |

## Mental Models
- **Treat the term spread as a noisy BRP proxy and inverse wealth as its filter.** A steep curve in a stock slump means premium, and a steep curve in a stock boom means expected hikes.
- **When bonds and stocks both look cheap, trust the cheapness.** Both-cheap months earned about +12% per year and both-rich months about −14% per year.
- **Think in odds, not certainties.** A 60/40 edge is very attractive in competitive markets, but the forecast is wrong 40% of the time. The edge shows up over 3–5 years, not over a month.
- **Magnitude carries information.** Scaled beats 1/0 and extreme forecasts produce extreme average returns, even though the hit rate barely rises with signal strength.
- **Risk measures do not predict returns.** Bond volatility has a correlation of 0.03 with the next month's excess return, so high-risk periods do not by themselves pay more.

## Worked Example
**Plugging values into the four-predictor model (hypothetical values, recomputed).** Forecasts are in % per month.
- **Recession-trough setup**:
  - Inputs: term spread 2.0%, real yield 3.5%, inverse wealth 0.95 (stocks have fallen versus their recent path), momentum +1 (the yield broke 5bp below its 6-month average).
  - Forecast = −10.15 + 0.74 + 0.70 + 9.3575 + 0.34 = **+0.99% per month** (≈ 11.8% annualized). This is in the top "> 0.5–1" bucket, bordering "very high".
  - Action: an aggressive investor with a 4-year benchmark goes to about 7–10 years of duration, and a conservative one to about 4.5–5. The scaled strategy holds about 1 unit of the 20y bond.
- **Late-expansion setup**:
  - Inputs: term spread 0.5%, real yield 2.0%, inverse wealth 0.88 (a strong bull market), momentum −1.
  - Forecast = −10.15 + 0.185 + 0.40 + 8.668 − 0.34 = **−1.24% per month**.
  - Action: 1/0 → cash. Scaled → short about 1.2 units. Target duration: aggressive −2, moderate 0, conservative 3.
- **Inverse wealth intuition**: with steady 1% monthly stock growth, IW = 0.1/1.01 ÷ (1 − 0.9/1.01) ≈ **0.91**. A 10% one-month drop after that trend lifts IW to about **1.02**. The +9.85 coefficient then adds about 1.1% per month to the forecast.
- **Sharpe check**: scaled 8.64/12.80 = **0.68**. Always-bond 0.67/10.42 = **0.06**, so the dynamic strategy's reward-to-volatility is more than 10 times higher.

## Anti-patterns
- **Assuming a constant risk premium when interpreting the curve**: the premium is identifiably high or low ahead of time.
- **Backtesting with in-sample coefficients**: this is hindsight, and it inflated the scaled return from 8.64% to 11.15%.
- **Kitchen-sink predictor sets**: a small, economically motivated set is more robust out of sample. Ilmanen found no additional predictor that consistently helped.
- **Using macroeconomic data as primary predictors**: they are backward-looking, published with a lag, and measured with error. Market-based variables are forward-looking.
- **Judging a slow strategy on monthly results**: monthly beat-both frequencies are only 35–61%. At a 5-year horizon both strategies reach 92%.
- **Expecting to profit from the forecast in a trend reversal year**: in 1994 both dynamic strategies stayed long and underperformed the 50/50 mix.

## Practitioner Notes
- In August 1995 the model was **bearish**. Predictions had been negative since the end of May 1995 because of a strong stock market (low inverse wealth) and a relatively flat curve. Ilmanen stressed that a low premium means a thin cushion and vulnerability to bad news, not a certain loss.
- Predicted premia were low in the 1960s and 1970s and **exceptionally high in 1982–85** (high real yields and term spreads). They spiked at cyclical troughs (1970, 1974, 1982), after the 1987 crash, and in the 1990 Gulf War recession, which coincided with inverse wealth spikes.
- Negative forecasts in the 1960s, 1973–74, 1979–80 and 1989 are hard to square with a "premium always positive" view, but they appeared in the data.
- The dynamic strategies did best in **bad times**. During NBER recessions: always-bond +6.55% per year, scaled +19.75%, 1/0 +9.08%. The scaled strategy made its money shorting in the late-1970s/early-1980s bear market and roughly matched bonds in the 1980s bull market.
- Rolling 60-month correlations are mostly positive. In the early 1990s the real yield and momentum faded, while the term spread and inverse wealth held at about 0.20.
- Why the edge survives: it is not an arbitrage (40% wrong), career risk and peer benchmarking punish unconventional losses, the strategy is slow (few, long-lived trades), and many investors either trust subjective forecasts or believe markets are unpredictable.
- The same predictors forecast shorter bills and bonds and international bond excess returns (Ilmanen, *Journal of Finance* 1995). The tools extend to spread and relative-value forecasting by combining mean-reverting spreads with filters.
- 20y bond excess returns correlate 0.997 with raw returns and −0.97 with long-rate changes, so forecasting excess returns ≈ forecasting yield changes.

## Key Takeaways
1. Forecast the near-term BRP with term spread + real yield + inverse wealth + momentum. Together they explain about 10% of monthly variance, with a 61% hit rate and a 0.57 correlation with 12-month returns.
2. Use inverse wealth to tell a "premium" steep curve from an "expectations" steep curve.
3. Scale duration with the size of the forecast, not just its sign, within risk limits (e.g. −2 to 10 years around a 4-year benchmark for aggressive investors).
4. Insist on out-of-sample, expanding-window backtests and subperiod stability before trusting any bond timing rule.
5. Judge dynamic duration strategies over 3–5 years. Beat-both frequencies rise from about 35–60% monthly to 92% over 5 years.
6. The premium is countercyclical: extend duration near troughs and after equity sell-offs, and shorten late in expansions when the curve is flat and stocks are strong.

## Connects To
- **ch02**: FSP/term spread as a BRP proxy. The persistence factor above 1 means steep curves are followed by higher, not lower, bond returns.
- **ch03**: the long-run average BRP (the anchor that dynamic strategies deviate from) and the steepness buckets (inverted → −2.6%, >300bp → +12.5%).
- **ch06**: expected-return decomposition for curve trades, and using predictability for barbell/bullet timing.
- **`cfa-asset-allocation-cme` ch04**: forecasting fixed-income returns and the use of term spread and real yields in CMEs.
- **`tuckman-fixed-income` ch08**: the risk premium in the short-rate drift.
- **`cfa-fixed-income` ch14**: active duration and yield-curve positioning.
