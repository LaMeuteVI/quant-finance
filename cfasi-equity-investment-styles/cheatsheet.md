# Cheatsheet — Equity Investment Styles Guides (practitioner decision rules)

## Decision rules
| When | Do | Because |
|---|---|---|
| Stock looks cheap on P/B or P/E | Check ROE trend and leverage first | P/B = (ROE - g)/(K - g); collapsing ROE makes a trap (ch03) |
| Estimate of value is fragile | Widen margin to 30%+ | A 10% earnings miss wipes a 5% margin (ch02) |
| Comparing capital-hungry names | Use owner earnings and EV multiples | P/E hides maintenance capex and debt (ch02, 04) |
| Bank trades below book | Reclassify balance sheet; consider senior or preferred claim | European banks stayed under book for a decade (ch04) |
| Running pure value | Add momentum, quality, profitability | Value+momentum 11.8% vs 11.2% alone; drawdown over 60% (ch05) |
| Applying one multiple globally | Backtest per sector | P/B failed except telecoms, oil; dividend yield works in utilities (ch05) |
| Adding a factor | Run the five tests; haircut about 58% | Post-publication decay (ch06) |
| Optimiser inputs are noisy | Equal weight or inverse-vol | Max Sharpe has the most estimation risk (ch06) |
| Heating Up regime | Hold the market | Factors add least; only Momentum beats (ch07) |
| Stagflation | Minimum Volatility | Only style with a positive return (ch07) |
| Factor timing tempting | Use factor mix with small tilts | 1-3 year hit rate near 50% (ch08) |
| Low-vol or factor ETF | Check sector drift and correlation to market | Tech weight 15% vs 6% in low-vol (ch08) |
| Systematic vs discretionary | Compare information ratio and blend | Same IR, low correlation (ch09) |
| Quant allocation | Split by family; test overlap in 2007 and 2018 | Crowding makes neutral funds correlate (ch10) |
| Client prone to disposition effect | Pre-set stop and target as working orders | Mental stops rely on willpower (ch11) |
| Building a quant model | Several metrics per factor, point-in-time data, cost-aware turnover | Single-metric "Value" is a trap (ch12) |
| Several themes wanted | Equal-weight basket, cap overlaps | 18 of 24 themes had lower Sharpe than the basket (ch13) |
| Theme index beta near 1 | Read correlation and drawdown dates | Cloud and Healthcare Innovation mislead on beta (ch13) |
| Buying lithium for EVs | Size on volume growth, check execution and pricing | Raw materials only 10-22% of pack cost (ch19) |
| Hydrogen claim | Ask colour and electricity source | 99% still fossil (ch20) |
| Two "AI" or "Robotics" ETFs | Compare rulebook, replication, top-10, GICS | Same label, different baskets (ch21) |
| EM bonds | Decide hard vs local currency first | FX is about 11 of 11.9 points of local vol (ch22, 24) |
| EM allocation | Look at revenue weight, not only 13% cap weight | Revenue 42%, GDP 39% (ch22) |
| Short-listed funds | Verify mandate, KIID, factsheet before ranking | Two of six funds fell out on documents (ch25) |

## Decision tree: which implementation?
1. Want cheap directional factor exposure? Passive factor mix ETF (ch08).
2. Want decorrelation? Active multi-factor long/short multi-asset fund, check beta and skew (ch08).
3. Want a bottom-up edge? Discretionary value with multifactor guard rails (ch05).
4. Want rules and breadth? Systematic model, 4-step build (ch12).
5. Want a structural trend? Thematic EW sleeve, then product selection (ch13, 21).

## Trade-off matrix
| Choice | Gain | Give up |
|---|---|---|
| Deep value | Cheapness, margin | Concentration, drawdown, traps (ch05) |
| Long-only factor ETF | Cost, liquidity | Purity, market beta (ch08) |
| Long/short systematic | Pure factor, low beta | Shorting cost, capacity (ch12) |
| Cap-weight EM index | Simplicity | China about 38% (ch23) |
| Local-currency EMD | Carry, diversifier | FX volatility (ch24) |
| Thematic ETF | Cost, transparency | Concentration, label risk (ch21) |

## Thresholds and defaults
| Item | Value |
|---|---|
| Graham screen | P/E <= 15 on 3y earnings, P/B <= 1.5, P/E x P/B <= 22.5, assets >= 2x debt (ch01) |
| Margin of safety | 20-33% (ch01, 02) |
| Book size | 10-30 stocks (ch01) |
| Equity cash-flow duration | 8-12 years; value overprice payback 8-9 years (ch03) |
| Piotroski | Buy 8-9, short 0-1 (ch10) |
| Systematic default | V/M/Q equal weights, monthly, top/bottom 50 (ch12) |
| Climate score | Below 50 laggard, above 75 opportunity (ch18) |
| Pack cost | $137/kWh in 2020; range 300 miles (ch19) |
| EM weights | 13% cap, 39% GDP, 42% revenue (ch22) |
| Fund screen | USD class, UCITS daily, age over 3 years, AUM over $100m (ch25) |

## Tells and smells
- Factor launch backed only by back-tests, US-only evidence (ch07, 08).
- "Market neutral" fund with high correlation to other quants (ch10).
- Fund correlation to tech index above 0.9 or top-10 above 30% (ch17, 21).
- Single-year outlier driving information ratio (+38.6% in 2020) (ch25).
- Sponsor figures presented as evidence (ch09, 14, 23).
- Enhanced index with tracking error above 10% (ch25).
- Parametric VaR trusted for themes (March 2020) (ch13).
