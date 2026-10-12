# Patterns — CFA Alternative Investments Recipes

## Hedge Fund Fee Waterfall to Net Return
**When to use**: converting gross value into the LP's net return, or comparing funds.
**How**: 1. Management fee = rate x AUM basis (check beginning/average/end). 2. Incentive base = gain, less mgmt fee if "net of management fee", less hurdle if hard hurdle. 3. Apply HWM: fee only on excess over prior net peak. 4. Net = (V_end - fees - capital) / capital. 5. Compound with geometric mean, never the arithmetic average.
**Trade-offs**: HWM is per investor; the source mixes gross value with net HWM in year 3, follow it on the exam. Fee-for-fee, FoF adds a layer (1%/10%): 14% net becomes 11.6%. (ch 01, 05)

## Fund-of-Funds Netting Check
**When to use**: judging FoF value or multi-strategy alternatives.
**How**: 1. Net each underlying fund (G - m - i x (G - m)); losers pay no incentive. 2. Average nets. 3. Apply FoF fees. 4. Express total fees as share of blended gross.
**Trade-offs**: dispersion between funds raises effective fees (67.6% of gross in the example vs 39.7%). (ch 05)

## Data-Bias Haircut for Alternative Statistics
**When to use**: before trusting any reported Sharpe, volatility or correlation.
**How**: 1. Identify bias: survivorship, backfill, self-reporting, appraisal smoothing. 2. Test first-order autocorrelation. 3. Unsmooth: r_u = (r - s r_prev)/(1 - s). 4. Recompute volatility (PE 9.5% to about 14%). 5. Use Sortino, CVaR and stress tests for skew.
**Trade-offs**: unsmoothing is noisy and needs a long series; transaction-based indexes are an alternative. (ch 01, 02, 06)

## Due Diligence Grid
**When to use**: before committing to a hedge fund or PE fund, and monitoring after.
**How**: cover organization, portfolio management, operations and controls (independent auditor, administrator, custodian, prime broker), risk management, legal, fund terms (fees, liquidity, key person, GP capital). Treat unusually smooth returns as a fraud flag.
**Trade-offs**: takes time; mandatory for opaque, lightly regulated vehicles. (ch 01, 03, 06)

## Three-Approach Property Valuation
**When to use**: appraising private real estate.
**How**: 1. Income (direct cap for stable level NOI; DCF with terminal value NOI(N+1)/terminal cap when income is non-level). 2. Cost (land + replacement - depreciation - obsolescence). 3. Sales comparison (price per sq m adjusted). 4. Reconcile by data quality. 5. For land, compute value on completion minus all-in cost.
**Trade-offs**: direct cap hides growth in the cap rate (c = r - g); cost approach suits new or special-purpose property. (ch 02)

## Renovation / Step-Up Valuation
**When to use**: NOI is depressed or will step up.
**How**: value = stabilized NOI/(r - g) minus PV of lost income during works; or DCF with terminal cap at or above going-in. Check going-in cap against terminal cap for consistency.
**Trade-offs**: terminal cap drives the answer; a 100 bp exit move swings NPV more than entry spread. (ch 02)

## Loan Sizing and Leverage Test
**When to use**: financing a property or judging leveraged return.
**How**: 1. Max loan = min(LTV x V, NOI/DSCR/loan constant). 2. Equity dividend rate = (NOI - debt service)/equity. 3. Compare leveraged and unleveraged IRR; positive leverage only if property return exceeds loan rate.
**Trade-offs**: leverage raises return and downside; financing never changes value. (ch 02)

## REIT NAVPS Build
**When to use**: valuing a REIT/REOC or finding implied cap rate.
**How**: 1. Forward cash NOI = (LTM NOI - non-cash rent + acquisition effect) x (1 + g). 2. / cap rate. 3. Add cash, receivables, land, prepaids. 4. Subtract debt and liabilities, exclude goodwill and deferred tax. 5. / shares. Cross-check P/FFO, P/AFFO and DDM.
**Trade-offs**: NAV is unreliable when transactions dry up; +100 bp cap cut NAVPS 16.6% (leverage magnifies). (ch 02)

## FFO to AFFO Bridge
**When to use**: dividend capacity and payout analysis.
**How**: FFO = NI + RE depreciation + losses - gains (+ impairments). AFFO = FFO - straight-line rent - recurring capex and leasing costs. Payout = dividends / AFFO.
**Trade-offs**: non-standard definitions; compare like for like. (ch 02)

## LBO Exit Waterfall
**When to use**: bounding a bid or computing PE and management proceeds.
**How**: exit EV minus remaining senior debt minus capitalized preference shares = residual equity; split between PE and management; multiple = proceeds / invested; IRR = multiple^(1/T) - 1. Stress exit multiple, year and leverage.
**Trade-offs**: output is a ceiling price; part of return is leverage and credit conditions. (ch 03)

## VC Method with Rounds and Option Pool
**When to use**: valuing early-stage ventures.
**How**: exit value = metric x multiple; post-money = exit/ROI; pre-money = post - investment; ownership = investment/post; new shares = f x N_old/(1 - f) on fully diluted base; later rounds dilute by (1 - f_B).
**Trade-offs**: highly sensitive to forecast and ROI (10x-30x). (ch 03)

## Fund Performance Read (IRR, DPI, RVPI, TVPI, PME)
**When to use**: judging a PE/real estate fund as an LP.
**How**: compare net IRR with same-vintage peers; read DPI (cash banked), RVPI (GP marks), TVPI; apply PME against an index; check valuation policy and credit-line IRR boosts; keep waiting until assets are monetized.
**Trade-offs**: ratios are per dollar paid in; J-curve distorts early years. (ch 03, 06)

## Futures Total Return Decomposition
**When to use**: explaining commodity index or futures investor return.
**How**: price return (front) + roll return ((near - far)/near x % rolled) + collateral (rf x collateral fraction x time). Roll count: exposure / far-contract value.
**Trade-offs**: components add approximately; annualize consistently. Contango erases price gains. (ch 04)

## Curve Diagnosis
**When to use**: explaining contango/backwardation or choosing a theory.
**How**: calendar spread = near - far (positive = backwardation); inventories and convenience yield point to storage; producer vs consumer hedging points to hedging pressure; speculators' premium points to insurance theory.
**Trade-offs**: inputs unobservable; evidence weak. (ch 04)

## Merger Arbitrage Payoff
**When to use**: sizing a stock-for-stock deal.
**How**: buy target, short acquirer in the offer ratio; success locks the spread; failure reverses; break-even probability = loss / (loss + gain).
**Trade-offs**: leverage 3-5x, left tail -20% to -40%. (ch 05)

## Conditional Factor Model for Hedge Funds
**When to use**: finding crisis-only exposures of a fund or strategy.
**How**: regress on equity, credit, USD, VIX with a crisis dummy; drop factors correlated above 60% using adjusted R-squared; crisis exposure = beta + beta crisis; count funds with significant loadings.
**Trade-offs**: alpha only as good as the factor set. (ch 05)

## Private Fund Cash-Flow Model and Commitment Pacing
**When to use**: planning calls, distributions and NAV.
**How**: C_t = RC_t (CC - PIC); D_t = RD_t x NAV_{t-1}(1+G); RD_t = (t/L)^B; NAV_t = NAV_{t-1}(1+G) + C_t - D_t. Target NAV = weight x projected portfolio; commit over 3-4 vintages; hold liquid proxies for undrawn capital.
**Trade-offs**: stress with faster calls and slower distributions. (ch 06)

## Allocation Toolkit Selection
**When to use**: choosing how to size alternatives.
**How**: assign role first; set liquid mix, then split into private buckets; constrained MVO for simple clients, mean-CVaR or Monte Carlo for tail-aware ones, factor approach with permanent staff.
**Trade-offs**: unconstrained MVO over-allocates to alternatives. (ch 06)
