# Cheatsheet — CFA Alternative Investments (L1 · L2 · L3)

## Decision rules
| When | Do | Because |
|---|---|---|
| Reading an alternative's Sharpe | Haircut for smoothing, survivorship, backfill | Biases understate risk and overstate return (ch01, 06) |
| Serial correlation is significant | Unsmooth before optimizing | True volatility is higher (PE 9.5% to 14%) (ch06) |
| Comparing funds | Compare net of fees | 2-and-20 vs 1.5-and-15 can explain the whole gap (ch01) |
| Valuing stable, level-NOI property | Direct cap, NOI1 / cap | Growth is implicit in c = r - g (ch02) |
| Income steps up or is non-level | DCF, terminal = NOI(N+1) / terminal cap | Direct cap undervalues (ch02) |
| Choosing terminal cap | At or above going-in | Older asset, more uncertainty (ch02) |
| Sizing a mortgage | Lower of LTV loan and DSCR loan | Both constraints bind (ch02) |
| Valuing a REIT | NAVPS, then P/FFO, P/AFFO, DDM | Assets, earnings and dividends each tell part (ch02) |
| Valuing a mature buyout | LBO model as a price ceiling | Financiers' hurdles set the maximum bid (ch03) |
| Valuing a seed-stage company | VC method, not DCF or multiples | No cash flow history (ch03) |
| Evaluating a PE fund | Net IRR vs same-vintage peers, DPI/RVPI/TVPI, PME | Time-weighted index comparison is invalid (ch03) |
| Long commodity futures | Total return = spot + roll + collateral | Contango erases spot gains (ch04) |
| Explaining curve shape | Inventories point to storage; hedger mix to hedging pressure | Evidence for backwardation premium is weak (ch04) |
| Adding a hedge fund strategy | Classify diversifier vs return enhancer first | EMN, macro, CTA diversify; L/S, distressed, convert arb add tail (ch05) |
| Judging a levered arbitrage fund | Ask what happens on the event day with leverage | Short-put payoffs blow up in crisis (ch05) |
| Fear of crisis loadings | Conditional factor model with crisis dummy | Exposures hide in calm periods (ch05) |
| Sizing PE commitments | Multi-vintage pacing from a cash-flow model | Single commitment overshoots (ch06) |
| Stress testing liquidity | Faster calls, slower distributions, gates | Both hit when public assets are down (ch06) |

## Decision tree: which alternative / tool
1. Need income and inflation link? Real estate, infrastructure, leased farmland. 2. Need equity-like growth and long horizon (15+ yrs)? PE. 3. Need diversification? Check correlation: below 0.8, e.g. macro, CTA, EMN, commodities. 4. Need liquidity? Listed REITs, liquid alts, futures. 5. Tail-aware client? Mean-CVaR / Monte Carlo; simple client? constrained MVO.

## Trade-off matrix
| Choice | Gain | Give up |
|---|---|---|
| Listed REIT vs private property | Liquidity, transparency, low entry | Control, low reported volatility (ch02) |
| REIT vs REOC | Tax transparency, yield | Growth retention, flexibility (ch02) |
| FoF vs direct hedge funds | Access, diligence, small tickets | Second fee layer, netting risk (ch01, 05) |
| FoF vs multi-strategy | Lower leverage | Slower reallocation, double fees (ch05) |
| Liquid alt vs private fund | Daily liquidity, no incentive fee | About 100-200 bps return (ch05) |
| Deal-by-deal vs total-return waterfall | Early carry (GP) | LP protection, clawback needed (ch03) |
| Swap vs futures commodity exposure | Customization, cash settlement | Counterparty risk (ch04) |
| SMA vs commingled | Transparency, control | Scale needed (ch06) |

## Thresholds and defaults
| Item | Value |
|---|---|
| Hedge fund fees | 1%-2% mgmt, 10%-20% incentive; FoF +1%/10% historically (ch01, 05) |
| PE fees | 1%-3% of committed capital, 20% carry, hurdle 7%-10% (ch01, 03) |
| LBO leverage | About 70% debt / 30% equity; targets 2.0x-2.5x buyout, 10x-30x VC (ch03) |
| REIT rules | Payout 90%-100%; 75% assets/income in real estate (ch02) |
| Core real estate leverage | At most 30% (ch02) |
| DSCR | 1.25-1.5x (ch02) |
| Real estate cycle | 17-18 years (ch02) |
| Merger arbitrage | Spread 3%-7%, leverage 3-5x, tail -20% to -40% (ch05) |
| Hedge fund liquidity | 30-90 day notice, 1-year lock-up, 10% holdback (ch06) |
| PE drawdown | Called over 3-5 years, 10-year life + 1-2 extension (ch06) |
| Private program horizon | 5-7 years to build, 10-12 to unwind, 15+ years horizon (ch06) |
| Diversifier test | Correlation to equities above 0.8 does not reduce risk (ch06) |

## Tells and smells
- Unusually smooth, steady returns: fraud or smoothing flag (ch01, 06).
- Low volatility and correlation in private real estate: appraisal artifact (ch02).
- High short interest plus special borrow: squeeze risk (ch05).
- IRR jump from credit-line funding: timing game (ch03).
- Index 80% energy: GSCI concentration (ch04).

## Exam traps
| Trap | Correct |
|---|---|
| Management fee base | Hedge fund: AUM; PE: committed capital (ch01, 03) |
| Hurdle type | Hard = fee on excess; soft = fee on entire return (ch01) |
| Bias direction | Survivorship and backfill inflate returns; smoothing deflates volatility (ch01) |
| Cap rate | c = r - g; terminal uses year N+1 NOI (ch02) |
| Direct cap vs DCF | Higher direct cap value means implied growth is higher (ch02) |
| Loan size | Take the lower of LTV and DSCR loans (ch02) |
| FFO to AFFO | Subtract straight-line rent and recurring capex; do not add depreciation back (ch02) |
| NAVPS | Excludes goodwill and deferred taxes; falls when cap rate rises (ch02) |
| Ownership | Investment / post-money, not pre-money (ch03) |
| Waterfall | American benefits GP; European benefits LP (ch03) |
| Contango sign | Negative roll; backwardation positive; spread = near - far (ch04) |
| Basis | Spot - near futures (Brent 3.92, not 0.05) (ch04) |
| Merger arb | Stock deal: short acquirer; cash deal: long target only (ch05) |
| Duration-neutral | Hedges only small parallel shifts (ch05) |
| Bonds vs alternatives | Bonds cut short-run volatility; alternatives raise target probability (ch06) |
| IRR vs MOIC | IRR sensitive to timing; MOIC ignores it; use both (ch06) |
