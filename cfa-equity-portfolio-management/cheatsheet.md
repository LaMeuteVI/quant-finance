# Cheatsheet — CFA Equity Portfolio Management (L3 R15–R18)

## Decision rules
| When | Do | Because |
|---|---|---|
| Adopting a benchmark | Test rules-based, transparent, investable | Non-investable indexes (HFRI, Value Line Geometric) cannot be held (ch02) |
| Index has few liquid names and the mandate is large | Full replication | Lowest TE before costs (ch02) |
| Index has many constituents or AUM is small | Stratified sampling | Cheap, simple, accepts higher TE (ch02) |
| Need minimum TE with a cap on holdings | Optimization plus total-volatility constraint | TE-only optimization can be riskier than the index (ch02) |
| Cap-spanning index (Russell 3000) | Blend: replicate liquid core, sample the tail | Tail trading costs outweigh TE benefit (ch02) |
| Cash from flows or dividends sits idle | Equitize with futures/ETFs | Cash drag lowers beta below 1 (ch02) |
| Trade to match an index | Market-on-close order | Index prices at the close (ch02) |
| Futures count needed | (exposure × weight) / (multiplier × futures price), round | Multiplier is in the unit value (ch02) |
| Choosing equal, fundamental or min-variance weights | Treat as a factor bet, not free alpha | Size/value tilts, crowding, costs (ch02) |
| Large lendable passive book | Lend; manage collateral quality; recall before key votes | Fee can fund the expense ratio; reinvestment is the risk (ch01, 02) |
| Classifying a mandate | Pick segmentation axis that isolates the return driver | Size/style, geography, activity (ch01) |
| Classifying a manager | Check holdings count, rebalance trigger, sizing, risk view | Fundamental ~50 names vs quant ~400 (ch03) |
| Stock looks cheap | Ask why and what the catalyst is | No catalyst = value trap (ch03) |
| Factor back-test | Point-in-time data, rank IC, quantile spread, costs, out-of-sample | Pearson IC, survivorship and look-ahead bias mislead (ch03) |
| Pairs trade | Same-industry names, stretched ±2σ spread, mean-reverting ratio | Correlation alone is spurious (ch03) |
| Activist target | Slow growth, weak governance, idle assets, stake below 10% | Efficient or distressed firms are wrong targets (ch03) |
| Paying for active return | Regress on Market, Size, Value, Momentum first | Factor-explained part is alternative beta (ch04) |
| Same AS, different manager | Compare TE too | AS ignores correlations; sector bets vs stock bets differ (ch04) |
| Absolute-return or long/short manager | Absolute risk (vol, drawdown), Sharpe objective | Cash-plus benchmark (ch04) |
| Index-relative long-only manager | Active risk, information ratio objective | Benchmark-aware (ch04) |
| Raising active risk | Relax constraints at the same time | Transfer coefficient falls as constraints bind (ch04) |
| AUM grows | More names, larger caps, lower turnover; or close | Capacity and slippage bite (ch04) |

## Decision tree: passive vs active, then how
1. Efficient, well-covered segment, narrow benchmark, taxable, cost-sensitive? Passive; pick index, then replication / sampling / optimization / futures.
2. Client-specific mandate (ESG, exclusions) or inefficient segment, confidence in skill? Active.
3. Active: fundamental (depth, few names) or quantitative (breadth, factors); bottom-up or top-down; then size with fundamental law and risk budget.
4. Relax long-only only if short signals are decent: 130/30, long/short, equitized market neutral.

## Trade-off matrix
| Choice | Gain | Give up |
|---|---|---|
| Cap weight | Low turnover, capacity, transparency | Concentration (NASDAQ 100 ≈ 25 effective names) |
| Equal weight | Low concentration | Small-cap bias, rebalancing, capacity |
| Futures overlay | Cheap, fast, short easily | Roll, margin calls, basis, expiry |
| Swap | Any index, tax deferral | Counterparty, interest-rate, tax-policy risk |
| ETF vs mutual fund | Intraday, in-kind tax efficiency | Bid-ask, commissions |
| Quant | Breadth, discipline, low cost | Crowding, data snooping, factor risk |
| Fundamental | Conviction, company depth | Behavioral biases, key-person risk |
| Long/short, 130/30 | Higher TC, balanced factor exposure | Fees, borrow, recall, unlimited short loss |
| Heuristic constraints | Simple guard rails | Inefficient risk allocation |

## Thresholds and defaults
| Item | Value |
|---|---|
| Stock-loan fee | Developed ~0.2-0.5%; emerging large caps ~1-2%; specials ~5-15% |
| Cash collateral | 102-105% |
| Performance fee | 10-20% above hurdle, high-water mark |
| HHI range | 1/n to 1; effective N = 1/HHI |
| Active Share | 0 to 1; closet ~0.25; multi-factor ~0.7; stock picker >0.9 |
| Tracking error | Closet <2%; multi-factor ~2-3%; stock picker 8-12%+ |
| Fundamental law | E(R_A) = IC × √BR × σ_RA × TC |
| TC | Long-only ~0.25-0.6; unconstrained 1 |
| 130/30 | Long 130, short 30, net 100, gross 160 |
| Market neutral | 50/50 gross 100 net 0 (or 100/100 gross 200) |
| Average monthly IC | 5-6% is very strong |
| Covariance estimates | N(N+1)/2 |
| Idiosyncratic fall-off | Portfolio vol falls little beyond ~50 names (avg corr 0.24) |
| Leverage optimum | L ≈ (R_a − funding)/σ² |

## Tells and smells
- "Active" fund with 0.25 Active Share and sub-2% TE: closet indexer.
- Excess return explained by Size and Value betas: alternative beta billed as alpha.
- Back-test with today's index members or restated accounts: survivorship, look-ahead.
- Reversal signal with 30 bp per trade ignored: costs destroy it.
- 100 low-P/B stocks counted as 100 decisions: breadth overstated.
- TE reported with excess return never compared to fees: fees explain excess, sampling explains TE.
- Short book beta differs from long book while "dollar neutral": not market neutral.
- Yield on specials budgeted as recurring income.

## Exam traps
| Trap | Correct |
|---|---|
| Tracking error vs excess return | TE is a standard deviation (≥ 0); excess return is signed |
| Free-float adjustment | Improves investability; not lower liquidity |
| Price-weighted | One share of each; splits distort |
| HHI 0.0286 | 35 effective stocks |
| Cash drag | Negative in rising markets, positive in falling |
| Margin example 20% | Really 20.9% (1,400/6,700) |
| Futures basis risk | Contract tracks price, not dividends |
| Securities lending | Borrower gets votes; dividends manufactured, lender keeps income |
| Performance fee protection | High-water mark, not the hurdle, avoids paying twice |
| GICS | Market-oriented; ICB, TRBC, RGS production-oriented |
| Covered call | Income now, upside capped; cash-covered put obliges buying at strike |
| Quant characteristic | Not forecasting company prospects; that is fundamental |
| IC definition | Score at t vs return t→t+1 |
| Year-end data before publication | Look-ahead bias |
| Holdings vs returns style analysis | Holdings: current, bottom-up; returns: average over window, no disclosure needed |
| Active Share | ½ Σ|Δw|; controlled by manager; benchmark dependent |
| Adding cash | Lowers absolute risk, raises active risk |
| CVaR | Average loss beyond VaR, not a VaR |
| BR | Independent decisions, not number of stocks |
| Fundamental law correction | One-decision 15 bp example needs BR = 44 for 1%, not "about 40" |
| 130/30 | Not riskless leverage; net exposure stays 100% |
