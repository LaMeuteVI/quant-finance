# Cheatsheet — Asset Allocation, CME and Behavioral Finance

## Decision rules
| When | Do | Because |
|---|---|---|
| Client bias is cognitive | Moderate with information and records | Reasoning errors yield to data (ch01) |
| Client bias is emotional | Adapt the plan, use neutral questions and defaults | Feelings do not switch off; exception endowment with goals at risk (ch01) |
| Need a client type fast | Active/passive then risk level, then test linked biases | Top-down behavioral alpha is cheaper than bottom-up (ch02) |
| Forecast uses history | Run regime, survivorship, smoothing, date and rationale checks | Samples mislead (ch03) |
| Return forecast needed | Anchor on yield plus nominal growth, then adjust valuation | GDP is stabler than P/E (ch03, 04) |
| Horizon is 1-3 years | Overlay cycle phase | Signal-to-noise highest there (ch03) |
| Horizon beyond a cycle | Converge to unconditional mean | Cycles average out (ch03) |
| Policy rate negative | Use equilibrium r_neutral as baseline | Observed rate is distress, not equilibrium (ch03) |
| Market is partly integrated | Singer-Terhaar with φ | Nests CAPM extremes (ch04) |
| Private asset volatility | De-smooth first | Optimizer overweights smoothed assets (ch04) |
| Legal liability exists | Liability-relative; bonds not cash anchor | Shortfall is the risk (ch06, 07) |
| Several distinct goals | Goals-based sub-portfolios | Probability of failure per goal (ch06, 07) |
| Unstable optimizer weights | Reverse-optimize, Black-Litterman | Fix inputs, not outputs (ch07) |
| Taxable account | After-tax inputs, wider band, tax-inefficient assets sheltered | Taxes shrink risk and return (ch08) |
| TAA proposed | Inside IPS ranges, judge by Sharpe or IR vs SAA | Costs, taxes and tracking error (ch06, 08) |

## Decision tree: which allocation approach
1. Legal liability with penalty? Liability-relative (surplus optimization, hedging/return-seeking if overfunded and conservative, integrated ALM for banks/P&C).
2. Many goals with different priority? Goals-based modules.
3. Else asset-only MVO with robustness checks.

## Cycle phase map
| Phase | Curve | Short rate | Assets |
|---|---|---|---|
| Initial recovery | Steep | Low | Small cap, high yield, EM |
| Early expansion | Flattening | Rising | Stocks trend up |
| Late expansion | Flattening from long end | Rising | Commodities, inflation hedges |
| Slowdown | Flat or inverted | Peaking | Utilities, quality; spreads widen |
| Contraction | Steepening | Falling | Bonds; stocks bottom before recovery |

## Trade-off matrix
| Choice | Gain | Give up |
|---|---|---|
| Wider rebalancing band | Lower cost and tax | Risk drift (ch07, 08) |
| Surplus optimization | Simple liability link | Single period (ch07) |
| Resampled MVO | Diversified, smooth | Inherits estimation error (ch07) |
| Risk parity | Balanced risk | Ignores returns, needs leverage (ch07) |
| Factor-based allocation | Risk transparency | No larger attainable set (ch06) |
| Illiquid assets | Illiquidity premium 2-6% | Liquidity under stress (ch04, 08) |

## Thresholds and defaults
| Item | Value |
|---|---|
| Hypothesis test sample | about 30 observations (ch03) |
| Sample VCV | at least 10 observations per asset (ch04) |
| Business cycle | average 56 months; expansion 39, contraction 17 (ch03) |
| Recession | typically 12-18 months (ch03) |
| Taylor weights | 0.5 on growth gap and inflation gap (ch03) |
| Singer-Terhaar φ | 0.75-0.90 developed; 0.50-0.75 EM and real estate (ch04) |
| Human capital | about 30% equity-like, 70% bond-like (ch06) |
| Pairwise correlation | above 0.95 is not diversifying (ch06) |
| z values | 0.674 (75%), 1.28 (90%), 1.645 (95%), 2.33 (99%) (ch07) |
| Taxable band | `R_pt/(1 − t)` (ch08) |
| Bubble | more than 2σ from trend; crash 30%+ in months (ch02) |

## Exam traps
| Trap | Correct reading |
|---|---|
| Higher frequency data | Improves variance and correlation, not the mean (ch03) |
| Peso problem | Feared event missing: return up, risk down (ch03) |
| Average beta and market return | Compute state by state (ch03) |
| Output gap sign | L3 trend minus actual; L2 actual minus potential (ch03, 05) |
| Break-even inflation | Overstates expected inflation if π > 0 (ch05) |
| Steep curve | Ambiguous: expected hikes or term premium (ch05) |
| Real rate and growth volatility | Positively related (ch05) |
| Conservatism vs representativeness | Prior overweighted vs new information (ch01) |
| Passive Preserver | Passive, low risk, emotional (ch02) |
| Funding ratio after equal dollar drop | Falls when assets < liabilities (ch07) |
| Surplus low-risk end | Hedging bonds, not cash (ch07) |
| Taxable rebalancing band | Divide by (1 − t), not multiply (ch08) |
| Taxes and correlation | Unchanged (ch08) |
| Source slips | Sharpe ratios printed x100 in one L3 R5 solution (ch06); the "54/74" equity weight and risk figures in L3 R6 are wrong, use about 65% and 87% (ch07) |
