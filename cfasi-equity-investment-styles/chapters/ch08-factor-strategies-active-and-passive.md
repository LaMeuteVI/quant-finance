# Chapter 8: Using Factors: Active and Passive Strategies (Smart-Beta Products, Factor Mixing, Multi-Asset Long/Short Funds, Due Diligence)
> **Source**: CFA Society Italy × Advisor Private, *Factor Investing* guide (2018), Ch. 3 "Utilizzo di factor: strategie attive e passive" | Marco Castagna, CFA and Andrea Semino, CFA (Credit Suisse Asset Management). Data to 2017; several charts credited to MSCI, Vanguard, AQR, HSBC AM, Goldman Sachs, S&P, Morningstar.

## Core Idea
Academic factors are long/short, concentrated, illiquid and high-turnover; investable factor products must trade purity for capacity. Two implementation routes exist. **Passive smart beta** (long-only ETFs, index funds, certificates) is cheap, transparent and suited to the directional core, and combining several uncorrelated factor indices ("factor mix") gives a better risk-return profile than any single factor. **Active factor funds** can be multi-factor, long/short and multi-asset, targeting low correlation to markets; they need rigorous due diligence on process, people, cost and realistic performance metrics. A portfolio test combining both improved return per unit of risk from 0.48 to 1.02.

## Frameworks Introduced
- **Academic vs investable factors**
  - Academic factor portfolios are long/short, concentrated, ignore liquidity and generate heavy turnover; shorting can be costly or prohibited, capacity is limited and trading costs erode returns.
  - Investable factor indices start from a cap-weighted parent index (liquidity), tilt toward the factor and stay long-only; cost: lower purity (higher correlation with the market). Correlation to the cap-weighted benchmark is much higher for long-only than for long/short versions of momentum, size and value (Vanguard analysis, S&P 500, 2000-2014).
  - MSCI index ladder, from most pure to most investable: market-neutral/pure factor indexes, long/short, optimised (e.g. Minimum Volatility), high exposure (e.g. Enhanced Value), high capacity (e.g. Value Weighted), cap-weighted benchmark.
  - MSCI Minimum Volatility construction: minimise risk subject to caps on stock, sector and country weights versus the parent index, style-exposure and turnover constraints.
- **Why factors exist (two logics)**
  - Behavioural/systematic risk premium: investors systematically avoid or overpay for certain characteristics (they overpay for volatile, glamorous, widely covered stocks, hence value and low volatility premia).
  - Market-structure effects: restrictions on short selling, leverage and asset allocation create asymmetries (small-cap exposure is limited for many investors, supporting the size premium).
  - Evidence that factors replicate active returns: Frazzini, Kabiler and Pedersen (2013) explain Berkshire Hathaway's excess return largely with Value, Quality and Low Risk factors.
- **Decoupling from price and debt**: factor weighting breaks the link between index weight and share price or debt outstanding, reducing concentration in the most expensive stocks or largest debtors.
- **Passive vs active vehicle choice**
  - ETF: listed, intraday liquidity, bid-ask spread, many underlying indices, suited to the strategic core.
  - Index fund: dealing through the intermediary at end-of-day NAV, often lower TER and several share classes (hedged, accumulating/distributing), no intraday liquidity.
  - Tracker certificate: often cheapest, may not pass through dividends, no asset segregation: counterparty risk on the issuer.
  - Selection criteria: factor definition, turnover, capacity and liquidity (small-cap or illiquid factors), TER and trading costs, tracking to theory.
- **Factor timing by market phase (illustrative scheme)**
  - Early bull market: contrarian factors (Value, Size, Reversal). Mature bull: pro-cyclical large-cap Momentum. Recession/bear: defensive factors (Low Volatility/Minimum Volatility, Quality, High Dividend).
  - Warning: factor timing requires forecasting the regime before it is priced; MSCI's table of how often each of seven MSCI World factor indices beat the cap-weighted index from 1976 shows that over 1 and 3 years the probability is close to 50%, rising with horizon; an equal-weighted mix of the seven factors beat the market more often than any single factor.
- **Factor mixing (passive multi-factor)**
  - What: equal-weight a small set of factors with complementary cyclicality (Value, Quality, Momentum, Minimum Volatility), conceptually an active satellite built with passive tools.
  - Evidence (MSCI World, 2000-2017 EUR): correlations of excess returns are low or negative for Value vs Quality (-0.53), Value vs Momentum (-0.09), Value vs MinVol (-0.17); Europe and US show the same pattern.
  - Sample result (MSCI, Jun 2001-Sep 2017): Factor Mix return 5.53% a year with 12.02% volatility and tracking error 2.88%, information ratio 0.44, better than each single factor index.
- **Active multi-factor, long/short, multi-asset funds**
  - Three differences from passive smart beta: multi-factor (value, momentum, carry, defensive), long/short (market beta near zero), multi-asset (equities, bonds, currencies, commodities; carry applies outside equities).
  - Diversification: AQR hypothetical long/short factor correlations (1990-2015) Value vs Momentum -0.62; Carry and Defensive near zero against the others.
  - Investment-spectrum ladder (AQR): market → add style tilt → go long/short → go multi-style → go multi-asset, each step raising efficiency and diversification.
- **Factor weighting methods in active funds**
  - Dollar weighted (equal); discretionary/factor timing (doubtful value-added); risk parity (equal risk per factor via volatility parity, VaR/CVaR parity, or mean-variance); drawdown management; factor tilting.
  - Guide's view: start from risk parity and apply a limited tactical tilt, since factor timing is even harder than market timing.
- **Five Pillars due diligence (adapted from Morningstar's Analyst Rating)**: Parent company, Process, People, Price, Performance.
  - Parent: long experience in systematic strategies; beware firms that entered after factor popularity using back-tests only.
  - Process: clear, repeatable, applied; factors with deep independent academic evidence, an economic rationale, clear definitions (a mix of indicators per factor, not too many: Novy-Marx 2016 warns that combining many signals overfits), global not just US evidence, net of trading costs. Preferred factor set: Value, Momentum, Carry, Defensive/Low Beta.
  - People: team with quantitative, maths, physics and engineering backgrounds, a reliable research function that updates the model without changing its core.
  - Price: control turnover and costs: in-house trading desks, algorithmic execution, liquid instruments, averaging indicators to reduce noise, company-wide order netting. Bank-provided risk-premia swaps can cost over 50 bps, while direct implementation reduces trading costs to a few bps. Illustration (HSBC AM): annualised two-way turnover of risk-premia strategies falls from 78 to 56 (-28%) with netting.
  - Performance: judge decorrelation, not just return: average and rolling correlation to equity and hedge-fund indices, dispersion versus equities, similar returns in up and down markets, drawdown control, positive skewness and low kurtosis (risk premia are not normally distributed).

## Key Concepts
- **Smart beta**: rules-based factor index investing; AUM in smart-beta ETFs exceeded USD 650bn in late 2017 (+22% in 2017; five-year compound growth 31%; over 1,200 products on 40 markets). MSCI factor-benchmark assets grew over 40% a year for four years to EUR 184bn.
- **Factor concentration in the US**: 78.15% of factor AUM is US equity; global developed 13.11%, bonds 4.33%, Europe 0.89%, EM 0.85%, Japan 0.24%.
- **Cost by vehicle (Morningstar, EUR bn / average TER)**: mutual funds 33.1 / 0.51%; ETFs 78.0 / 0.19%; other products 61.7 / 0.56%; total 172.7 / 0.38%.
- **Pure factor portfolio**: isolates one characteristic with market-neutral long/short exposure.
- **Purity vs investability**: the central trade-off of any factor index.
- **Factor mix / multi-factor index**: combination of factor tilts in one index.
- **Carry**: return from holding higher-yielding assets; applies to bonds, currencies and commodities.
- **Defensive / low beta**: long low-risk, short high-risk assets.
- **Active alpha persistence**: S&P persistence data: of 631 US equity funds in the top quartile at September 2014 only 2.85% were still there in September 2016 (21.24% after one year).
- **Manager risk**: risk that a selected active manager loses alpha.
- **Low-volatility drift**: Technology weight in low-volatility products rose to about 15% versus a 6% five-year average, so the defensive label changed (Goldman Sachs 2017); if volatilities mean-reverted those stocks would be more volatile than average.

## Formulas & Reference Tables
- Sharpe ratio: `(Rp - Rf) / sigma_p`. Return/risk ratio used in the guide: annual return divided by annualised volatility. Information ratio: `active return / tracking error`.
- MSCI World factor indices vs cap-weighted (Jun 2001-Sep 2017, EUR):

| Index | Return | Volatility | Return/risk | Active return | Tracking error | IR |
|---|---|---|---|---|---|---|
| Minimum Volatility | 5.86% | 10.86% | 0.54 | 1.60% | 7.10% | 0.23 |
| Quality | 5.82% | 12.46% | 0.47 | 1.56% | 4.28% | 0.36 |
| Value Weighted | 4.50% | 14.63% | 0.31 | 0.24% | 2.69% | 0.09 |
| Factor Mix A-Series | 5.53% | 12.02% | 0.46 | 1.27% | 2.88% | 0.44 |
| MSCI World (cap-weighted) | 4.26% | 13.65% | 0.31 | - | - | - |

- Four-portfolio multi-asset test (Jan 2000-Dec 2017):

| Portfolio | Composition | Return | Risk | Return/risk | Worst month | Max drawdown |
|---|---|---|---|---|---|---|
| A | 60% cap-weighted equity / 40% bonds | 3.95% | 8.26% | 0.48 | -6.70% | -30.40% |
| B | 48% equity / 32% bonds / 20% hedge-fund index | 4.11% | 8.00% | 0.51 | -6.80% | -28.23% |
| C | 48% passive factor equity / 32% bonds / 20% hedge-fund index | 4.93% | 7.31% | 0.67 | -6.23% | -23.17% |
| D | 48% passive factor equity / 32% bonds / 20% active multi-factor long/short funds | 6.09% | 5.94% | 1.02 | -4.08% | -19.48% |

  (Equity: MSCI World NR; factor equity: MSCI World Factor Mix A Series; bonds: Bloomberg Barclays Global Aggregate EUR hedged; hedge funds: HFRI Fund Weighted Composite; active funds: equal-weighted composite of six UCITS multi-factor long/short multi-asset funds, using live record, then same-volatility non-UCITS record, then back-test with costs for early years.)
- Average two-way annualised turnover of risk-premia sleeves without/with netting: bonds 43/33, equity 14/10, FX 21/13 (components rounded in source), total 78/56 (-28%).

## Mental Models
- **Use passive factor ETFs for the directional core and a single long exposure**: low TER, transparent, but beta near 1 and single asset class.
- **Use active multi-factor long/short funds as a diversifying satellite**: look for low beta, low and stable correlation to equities and hedge funds, positive skew.
- **Use factor mix instead of factor timing**: equal-weighting uncorrelated factors raised the probability of beating the benchmark above any single factor and reduced tracking error.
- **Use net-of-cost, multi-region evidence when judging a factor**: if it works only in US data or before costs, skip it.
- **Use risk parity as the neutral factor weighting**: apply only small tactical tilts.

## Worked Example
Return/risk and information ratio (recomputed from the guide's data).
- Inputs: Factor Mix return 5.53%, volatility 12.02%; benchmark return 4.26%, tracking error 2.88%.
- Steps: return/risk = 5.53/12.02 = 0.46; active return = 5.53 - 4.26 = 1.27%; IR = 1.27/2.88 = 0.44.
- Result: Factor Mix has about the same return/risk as Quality (0.47) but a much higher IR (0.44 vs 0.36) because its tracking error is lower.
- Interpretation: diversification across factor tilts delivers steadier relative performance.

Portfolio D vs A.
- Inputs: A return 3.95%, risk 8.26%; D return 6.09%, risk 5.94%.
- Steps: return/risk A = 0.478; D = 1.025; drawdown improves from -30.4% to -19.5% (difference 10.9 points).
- Result: D delivers 2.14 points more return with 28% less volatility ((8.26-5.94)/8.26).
- Interpretation: most of the gain comes from replacing part of the diversifying sleeve with uncorrelated factor strategies, but backtests, composite construction and the 2000-2017 window (flattering to alternatives) limit extrapolation.

## Anti-patterns
- Buying a smart-beta product named after a factor with no check of definition, turnover, capacity and costs.
- Assuming long-only factor ETFs deliver the academic premium: they carry market beta.
- Treating "low volatility" as defensive without checking sector drift (tech weight rose to 15%).
- Trying to time factors by guessing the regime; success probability over 1-3 years is near a coin flip.
- Selecting active funds on past return, not decorrelation, drawdown control and process.
- Over-relying on back-tests; many managers launched products from data-mined signals.
- Paying bank risk-premia swap fees (over 50 bps) when direct execution costs a few bps.
- Believing size is an independent premium: once controlled for value the small-cap advantage nearly vanishes.

## Practitioner Notes
- Smart-beta growth is concentrated in US equity; the guide links this to US market efficiency: in the SPIVA scorecard few active funds beat the benchmark over five years, which pushes investors toward factors.
- Factor products can be combined: passive factor ETFs for directional risk, active multi-factor long/short funds for diversification.
- Reasons to prefer passive: transparent holdings and costs, lower turnover costs, lower TER (factor ETFs cost more than cap-weighted ones but less than active funds), lower manager risk.
- Reasons to prefer active: multi-factor, long/short, multi-asset exposure; ability to exploit negative momentum, carry and curve factors; skilled trading cost control.
- Investor survey (Invesco 2017, ch.6 insert) and indexation by factor of single-asset universes show demand outstripping supply for fixed-income and multi-asset factor products.

## Key Takeaways
1. Academic factors are long/short and unconstrained; investable indices are long-only and tilt from a cap-weighted parent, accepting lower purity.
2. Factors originate from systematic investor behaviour or market-structure constraints.
3. Factor mix of Value, Quality, Momentum and Minimum Volatility works because correlations among them are low or negative.
4. Factor timing has doubtful results; prefer risk parity or equal mix with limited tilts.
5. Active multi-factor long/short multi-asset funds add decorrelation and carry/defensive exposures that equity-only smart beta lacks.
6. Due diligence uses five pillars: parent, process, people, price, performance; judge decorrelation, skew and kurtosis, not only return.
7. Transaction costs and turnover determine net factor returns; netting and direct execution cut costs sharply.
8. A portfolio combining passive factor equity and active multi-factor funds had return/risk of 1.02 versus 0.48 for 60/40.

## Connects To
- **ch06**: factor definitions, models, smart-beta weighting schemes, bond factors.
- **ch07**: factor behaviour by economic regime, motivating (and limiting) factor timing.
- **ch05**: active multifactor stock selection, factor crowding through indices and swaps.
- **ch09-ch12**: systematic investing, a fuller treatment of rules-based active strategies.
- **`cfasi-portfolio-construction`**: passive investments, ETF and fund selection (due diligence parallels).
- **`cfa-portfolio-management`**: active vs passive, manager selection and alpha/beta separation.
- **`cfa-equity-portfolio-management`**: smart beta and factor-based strategies.
