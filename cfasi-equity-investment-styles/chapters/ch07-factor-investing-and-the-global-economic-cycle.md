# Chapter 7: Factor Investing and the Global Economic Cycle (Markov-Switching Regimes and Style-Index Behaviour)
> **Source**: CFA Society Italy × Advisor Private, *Factor Investing* guide (2018), Ch. 2 "Factor investing e ciclo economico globale" | Valerio Sullo, PhD; plus Invesco-sponsored insert on how the roles of academics, advisers and managers are changing (attributed where used)

## Core Idea
Factor premia are not constant. This chapter classifies the global economy into four regimes using a **Markov-Switching (MS) model** on a leading indicator (OECD CLI) and an inflation-acceleration measure, then measures how the MSCI World index and five style indices (Quality, Momentum, Minimum Volatility, High Dividend, Value-Weighted) behave in each. Practical result: no style beats the market in every regime, Stagflation is the worst phase for the market and for most styles, and the regime with the highest expected market return (Heating Up) is the one where factors add least. The decision rule is to identify, or better forecast, the likely regime and tilt factors accordingly.

## Frameworks Introduced
- **Single-factor and multifactor return models**
  - `Ri = a_i + b_i F + s_i e_i`, so `E[Ri] = a_i + b_i E[F]` and `Var(Ri) = b_i^2 Var(F) + Var(e_i)`: risk splits into factor exposure and idiosyncratic parts.
  - With excess returns and the market as factor (Jensen 1968): `Ri - rf = a_i + b_iM (RM - rf) + e_i`; if alpha is statistically zero this is the CAPM, `E[Ri - rf] = b_iM E[RM - rf]`.
  - Multifactor (APT, Ross 1976): `Ri = a_i + sum_j b_ij F_j + e_i`. Fama-French (1992) found market, size and value factors; later research suggests factor premia are cyclical and not all significant.
- **Four-regime macro cycle (Gupta et al. 2014, MSCI)**
  - Axes: business cycle (OECD Composite Leading Indicator, CLI) and inflation acceleration (3-month minus 36-month rolling change in CPI).

| Regime | CPI acceleration | CLI |
|---|---|---|
| Heating Up | Accelerating | Rising |
| Goldilocks | Decelerating | Rising |
| Stagflation | Accelerating | Falling |
| Slowing Growth | Decelerating | Falling |

- **Markov-Switching model**
  - Form: `DY_t = m(s_t) + C(s_t) e_t`, s_t in {1,...,M}; covariance in state s is `Sigma(s) = C(s)'C(s)`; a mixture of normals whose weights change over time as regime probabilities, so returns can be skewed and fat-tailed.
  - Advantage over heuristic counting of "how often each regime occurred": it lets you test the number of regimes and the significance of each state's parameters, and does not require pre-labelling observations (counting risks misclassifying high-variance episodes).
  - Limits: 32 parameters estimated from 181 quarterly observations (Q4 1972-Q4 2017); multiple local maxima in the likelihood; convergence difficulty; the Schwarz information criterion alone would favour a three-state model; sign restrictions on intercepts were imposed to keep states interpretable.
- **Regime classification rule**: label each quarter with the regime of highest smoothed probability (Hamilton 1994).
- **Regime-conditional market model**: `R_Mkt,t = m(s_t) + s(s_t) e_t` (drift and volatility per regime).
- **Regime-conditional factor model**: `R_i,t = a(s_t) + b_i(s_t) R_Mkt,t + s(s_t) e_i,t`, i.e. alpha, beta and idiosyncratic risk per style index per regime.

## Key Concepts
- **Heating Up**: growth and inflation rising together; strongest market returns, low volatility.
- **Goldilocks**: growth continuing, inflation easing; the most persistent regime; good returns, rising volatility.
- **Stagflation**: falling activity with rising prices; worst for the market; markets anticipate further deterioration.
- **Slowing Growth**: low growth, falling inflation (the recession state); highest volatility but expected rebound.
- **Transition matrix**: probability of moving from one regime to another; the diagonal measures persistence.
- **Expected duration**: `D_i = 1 / (1 - P_ii)` quarters.
- **Smoothed probability**: model's estimate of the probability of each regime at each date.
- **Skewness and kurtosis**: third and fourth standardised moments (`E[(x-m)^3/s^3]`, `E[(x-m)^4/s^4]`); normal has 0 and 3; kurtosis above 3 means fat tails.
- **Style index correlations**: between 0.60 and 0.95 in the sample and rising sharply in crises; Minimum Volatility is the least correlated but its covariance also rises under stress.
- **Alpha instability**: alpha estimates are close to zero and statistically weak, consistent with a reasonably efficient market; betas are the stable part.
- **Procyclical vs anticyclical**: styles and the market are procyclical in Heating Up and anticyclical in Slowing Growth.

## Formulas & Reference Tables
- Expected duration: `D = 1/(1 - P_ii)`: 3.2 quarters (Heating Up), 2.1 (Stagflation), 3.1 (Slowing Growth), 6.6 (Goldilocks). The source rounds to 3, 2, 3, 6.
- Regime frequencies in the sample: Heating Up 16.57%, Stagflation 11.60%, Slowing Growth 16.02%, Goldilocks 55.80%.

**Transition matrix as estimated (read each column as the origin regime, each row as the destination; columns sum to 1)** ⚠ The source text says rows are origin, but the printed numbers only sum to 1 by column and its narrative (Heating Up to Goldilocks 31%, Stagflation to Slowing Growth 40%) matches the column reading. The stationary distribution of the column-stochastic matrix (about 17%, 13%, 16%, 55%) reproduces the sample frequencies.

| To \ From | Heating Up | Stagflation | Slowing Growth | Goldilocks |
|---|---|---|---|---|
| Heating Up | 0.686 | 0 | 0.195 | 0.040 |
| Stagflation | 0 | 0.519 | 0 | 0.111 |
| Slowing Growth | 0 | 0.398 | 0.674 | 0 |
| Goldilocks | 0.314 | 0.083 | 0.131 | 0.849 |

Reading: from Heating Up the economy usually moves to Goldilocks; Goldilocks almost never jumps directly to recession (Slowing Growth probability 0) but has about 11% chance of Stagflation; Stagflation is unstable and leads to Slowing Growth with about 40% probability; Slowing Growth exits to Heating Up or Goldilocks. Typical sequence: Heating Up, Goldilocks, Stagflation, Slowing Growth.

**MSCI World TR by regime (annualised %, Q4 1972-Q4 2017)**: expected return Heating Up 23.3 (t 5.1), Goldilocks 12.6 (t 4.6), Slowing Growth 10.5 (t 1.1, not significant), Stagflation -6.7 (t -1.3, not significant). The printed volatilities (4.6, 5.2, 7.1, 5.2) are far too low for annualised equity volatility; use only their ordering: Slowing Growth highest, Heating Up lowest. **⚠ Scale issue** in the source.

**Style indices by regime: betas to MSCI World (from the guide's regression tables)**

| Style | Heating Up | Goldilocks | Stagflation | Slowing Growth |
|---|---|---|---|---|
| Quality | 1.12 | 0.83 | 0.79 | 1.11 |
| Momentum | 1.50 | 0.86 | 0.83 | 1.15 |
| Minimum Volatility | 0.61 | 0.73 | 0.57 | 0.63 |
| High Dividend | 0.75 | 1.02 | 0.86 | 0.63 |
| Value-Weighted | 0.79 | 1.08 | 1.08 | 0.79 |

**Excess return of style indices vs the market by regime (annualised %, from the guide's chart)**

| Regime | Quality | Momentum | Min Vol | High Div | Value-W | Market |
|---|---|---|---|---|---|---|
| Heating Up | 22.8 | 28.2 | 13.6 | 18.6 | 20.4 | 23.4 |
| Goldilocks | 15.5 | 5.9 | 7.9 | 11.7 | 13.5 | 12.6 |
| Stagflation | -0.7 | -0.9 | 2.1 | -1.4 | -7.1 | -6.7 |
| Slowing Growth | 16.9 | 19.6 | 11.9 | 10.5 | 10.6 | 10.5 |

(Style indices history: Minimum Volatility from Q2 1988; others from Q2 1994.)

## Mental Models
- **Use Heating Up as "buy the market, not the factor"**: only Momentum beats the market (with higher volatility), and alpha is rare because expectations are already high.
- **Use Goldilocks to favour Quality and Value-Weighted**: falling inflation raises the real value of dividends and rewards firms with strong real fundamentals; Momentum lags.
- **Use Stagflation to hold Minimum Volatility**: it is the only style with a positive return; Value-Weighted suffers most since expected cash flows shrink.
- **Use Slowing Growth to keep Quality, Momentum and Minimum Volatility**: markets look ahead and rebound, but volatility is highest and Value-Weighted lags.
- **Remember that performance tracks real activity more than prices**: the macro-regime effect comes mostly from growth (CLI), less from inflation.
- **Use correlation warnings for diversification**: style indices correlate 0.60-0.95, and spike in crises, so do not treat them as independent.

## Worked Example
Expected duration and persistence (recomputed).
- Inputs: P(Goldilocks to Goldilocks) = 0.849; P(Stagflation to Stagflation) = 0.519.
- Steps: D = 1/(1 - 0.849) = 6.6 quarters; D = 1/(1 - 0.519) = 2.1 quarters.
- Result: Goldilocks lasts on average about 6.6 quarters; Stagflation about 2.1.
- Interpretation: a Stagflation spell is short and unstable (40% chance of Slowing Growth next); Goldilocks is persistent, hence the 56% sample share.

Regime-weighted expected market return (illustrative, using sample frequencies and the estimates above).
- Inputs: shares 16.57%, 55.80%, 11.60%, 16.02%; returns 23.35, 12.61, -6.75, 10.54.
- Steps: 0.1657 x 23.35 = 3.87; 0.5580 x 12.61 = 7.04; 0.1160 x -6.75 = -0.78; 0.1602 x 10.54 = 1.69; sum = 11.8% a year.
- Result: unconditional expected return about 11.8%; Stagflation is only 11.6% of the time but costs about 0.8 points of return.
- Interpretation: knowing the regime mix matters; overweighting Min Vol when Stagflation probability rises hedges the weakest state.

## Anti-patterns
- Fixing the number of regimes a priori and counting events (circular and misclassification-prone).
- Over-trusting a high-dimensional MS model estimated on few observations.
- Reading regime alphas as reliable: most are statistically near zero.
- Assuming the post-2009 Goldilocks (the longest in almost 50 years, supported by central-bank easing) is normal.
- Treating style indices as diversifiers when correlations are 0.60-0.95 and rise under stress.
- Rotating on realised regime rather than forecast regime; by the time the indicator is published the market has moved (markets are forward-looking and lag/lead growth).

## Practitioner Notes
- The post-2008 volatility regime: low-volatility spells in Q1 1995-Q4 1997, Q1 2004-Q4 2007 and Q4 2011-Q4 2017; the latest, about six years, coincides with central-bank easing (Fed 2009, BoJ 2013, ECB 2011). The guide notes the stabilisation is partly artificial and without close precedent, making forecasting hard.
- Statistical moments of equity returns vary over time; kurtosis above 3 in three quarters of the sample (fat tails); Momentum and Quality are the styles most prone to extreme values.
- Invesco insert: demand for new factor products raised concerns that managers launch back-tested, data-mined products without theoretical grounding; investors increasingly use academics for independent factor research, advisers shift from manager selection to integrating factors into strategy and risk monitoring, large institutions internalise smart-beta while buying complex quantitative products externally.
- Method literature cited: Gupta et al. (MSCI 2014), Markovic and Rousing (Credit Suisse 2016) on factor rotation, Roncalli on risk parity.

## Key Takeaways
1. Factor premia vary with the economic regime; ignoring the cycle risks mis-timed factor bets.
2. Four regimes from CLI and CPI acceleration: Heating Up, Goldilocks, Stagflation, Slowing Growth.
3. Goldilocks is the most persistent state (6.6 quarters, 56% of the sample); Stagflation is short and usually followed by Slowing Growth.
4. MSCI World does best in Heating Up (23.3%), worst in Stagflation (-6.7%); volatility peaks in Slowing Growth.
5. In Heating Up only Momentum beats the market; Quality and Value-Weighted lead in Goldilocks; Minimum Volatility is the only positive style in Stagflation; Quality, Momentum and Min Vol hold up in Slowing Growth.
6. Style betas to the market vary by regime; Value-Weighted is highest-beta in Goldilocks and Stagflation; Momentum highest in Heating Up.
7. Style indices correlate strongly and more so in crises, limiting diversification.
8. The edge lies in identifying, or forecasting, the prevailing regime; the model's limits (few data, many parameters) call for caution.

## Connects To
- **ch06**: factor definitions, models and zoo that this chapter conditions on the cycle.
- **ch08**: active vs passive implementation and evaluation of factor products, including factor timing.
- **ch05**: J.P. Morgan cycle-phase table for value, growth, momentum, quality, risk and size.
- **ch03**: value's behaviour through crises.
- **`cfa-asset-allocation-cme`**: business-cycle scenarios and capital-market expectations.
- **`cfa-quantitative-methods`**: regime-switching, skewness and kurtosis.
