# Chapter 2: Security Market Indexes
> **Source**: CFA Program Curriculum 2020, Level I, Reading 37 · Portfolio Management (Equity and Alternatives block) | Paul D. Kaplan, Dorothy C. Kelly

## Core Idea
A security market index is a rule-based portfolio that stands in for a market, segment or asset class. Every index is the answer to five design choices: target market, constituent selection, weighting, rebalancing and reconstitution. The weighting rule is the dominant choice: the same five stocks gave a 3.45%, 10.40%, 1.49% or -1.66% price return depending on whether they were price-, equal-, cap- or float-cap-weighted. An index is only a valid benchmark, market proxy or fund blueprint if its construction matches the use you put it to.

## Learning Outcomes Covered
- Describe a security market index; compute index value, price return and total return
- Describe index construction and management choices; compare weighting methods
- Compute index value and return under each weighting method
- Describe rebalancing and reconstitution
- Describe uses of indexes; types of equity, fixed-income and alternative indexes; compare them

## Frameworks Introduced
- **Five index design decisions**: (1) target market, (2) which securities (full universe or sample; fixed count vs variable; rules vs committee), (3) weights, (4) rebalancing schedule, (5) reconstitution schedule.
  - When to use: audit any index before adopting it as a benchmark or product basis.
  - How: ask each question in order; the answers expose the hidden bets (size, momentum, value, turnover).
- **Divisor mechanics**: `V = Σ n_i·P_i / D`. The divisor is chosen at inception (often so the index starts at 1,000, or at N for a price-weighted index) and re-set after any event that is not a price move (split, constituent change) so the index level is unchanged by the event.
- **Weighting-method comparison** (what each rule implicitly bets on):
  - Price: weight proportional to price; arbitrary, a split changes all weights; needs divisor adjustment; no rebalancing. Tilt: high-priced stocks.
  - Equal: weight 1/N; small-cap and illiquid overweight relative to market; drifts, needs frequent rebalancing (sells winners, buys losers: contrarian); highest turnover.
  - Market-cap: weight proportional to `Q·P`; self-rebalancing; holds the market as is; implicit momentum tilt (winners grow in weight, overvalued stocks overweight).
  - Float-adjusted cap: as above but using `f·Q·P`, only shares available to the public (excludes controlling holders, corporates, governments; "free float" also strips foreign-ownership limits). Today's industry standard.
  - Fundamental: weight proportional to a price-independent size measure (book value, cash flow, revenue, earnings, dividends, employees, or a composite). Value tilt and contrarian rebalancing effect.
- **Rebalancing vs reconstitution**: rebalancing resets weights to the weighting rule on scheduled dates (usually quarterly); reconstitution re-applies membership criteria and adds/deletes securities, after which weights are re-applied. Both create turnover; reconstitution also creates front-running price effects.
- **Benchmark-fit test**: the benchmark must mirror the manager's mandate (e.g. global small-cap manager vs global small-cap index), otherwise skill is misjudged.
- **Beta-matched passive alternative**: `passive portfolio = β in index fund + (1 - β) in cash`; `α = R_active - R_passive`.

## Key Concepts
- **Security market index**: a portfolio of marketable securities representing a market, segment or asset class, valued regularly from actual or estimated prices.
- **Constituent securities**: the holdings of the index portfolio.
- **Price return index**: reflects only constituent price changes.
- **Total return index**: reflects price changes plus reinvestment of all dividends/interest since inception; always at or above its price index after inception, gap widening over time.
- **Divisor**: scaling constant that converts portfolio value to index level and absorbs non-price changes.
- **Price weighting**: weight = price / sum of prices (DJIA, Nikkei 225 in modified form).
- **Equal weighting**: weight = 1/N at inception and at each rebalancing.
- **Market-cap (value) weighting**: weight = constituent cap / total cap.
- **Float adjustment**: uses only freely tradable shares in the cap calculation.
- **Fundamental weighting**: weights from non-price fundamentals; produces higher fundamental-to-price ratios than the cap-weighted version.
- **Rebalancing**: restoring target weights; **reconstitution**: changing membership.
- **Broad market index**: covers the whole market, typically more than 90% of it (Wilshire 5000, Russell 3000 about 98% of US equities, SSE Composite).
- **Multi-market index**: combines national indexes (MSCI developed, emerging, frontier classes; regions); GDP-weighting of countries is a fundamental variant created to cut Japan's roughly 60% weight in the 1987 EAFE.
- **Sector index**: tracks an economic sector; sector families should sum to a broad index; no universal classification.
- **Style index**: size (large, mid, small) x value/growth classification gives six cells; defined differently by every provider; high turnover as stocks migrate between cells.
- **Aggregate bond index**: broad fixed-income index, e.g. the Bloomberg Barclays US Aggregate (about 8,000 securities, first fixed-income index).
- **Survivorship bias (hedge fund indexes)**: voluntary reporting means poor performers drop out, overstating index performance.

## Formulas & Reference Tables
- Index value: `V_PRI = Σ n_i·P_i / D` (n_i units held, P_i price, D divisor).
- Price return, index: `PR_I = (V_1 - V_0)/V_0 = Σ w_i·PR_i`, with `PR_i = (P_i1 - P_i0)/P_i0`.
- Total return, index: `TR_I = (V_1 - V_0 + Inc_I)/V_0 = Σ w_i·TR_i`, with `TR_i = (P_i1 - P_i0 + Inc_i)/P_i0`. Weights `w_i` are beginning-of-period weights.
- Multi-period: `V_T = V_0·(1+R_1)(1+R_2)...(1+R_T)` (geometric linking; same for price and total return versions).
- Weights: price `w_i = P_i/ΣP_j`; equal `w_i = 1/N`; cap `w_i = Q_iP_i/ΣQ_jP_j`; float-cap `w_i = f_iQ_iP_i/Σf_jQ_jP_j`; fundamental `w_i = F_i/ΣF_j`.
- Split adjustment (price-weighted): `D_new = Σ P_after / V_before`.

| Weighting | Self-rebalancing? | Split effect | Implicit tilt | Turnover |
|---|---|---|---|---|
| Price | Yes (no rebalancing) | Divisor must change; weights shift | High-priced stocks | Low |
| Equal | No (drifts, frequent) | None | Small/illiquid; contrarian | Highest |
| Cap / float-cap | Yes, only corporate actions | None | Momentum, large-cap | Low |
| Fundamental | No (periodic) | None | Value, contrarian | Medium |

| Index family | Construction challenge |
|---|---|
| Equity | Mostly mechanical rules; some committees (S&P 500, BSE Sensex) |
| Fixed income | Huge universe, maturities roll off, dealer-market, illiquid, prices estimated (matrix); costly to replicate |
| Commodity | Futures-based; weighting not obvious (equal in CRB, production/liquidity in S&P GSCI); return = collateral interest + price change + roll yield |
| Real estate | Appraisal, repeat-sales, REIT indexes; only REITs trade continuously |
| Hedge fund | Equal-weighted databases; constituents choose to report; low overlap, survivorship bias |

## Mental Models
- Use the weighting rule as a hidden factor bet: price = arbitrary, equal = small-cap and contrarian, cap = momentum and large-cap, fundamental = value.
- Use cap-weighted indexes when you want the market portfolio with minimal trading; use equal or fundamental when you want to avoid concentration in recent winners, accepting turnover.
- Use total return (not price) versions for performance measurement and benchmarking; price versions only for level or sentiment quoting.
- Use the benchmark-fit test before judging a manager; a mismatched benchmark flips conclusions.
- Use index-event awareness: anticipated additions are bid up before reconstitution (Russell 2000 annual reconstitution, Uranium Energy Corp. 2009 case, about +400% in the quarter), so passive funds buy high.

## Worked Example
Five-stock market (recomputed in python). Beginning prices A-E: 50, 25, 12.5, 10, 4. Ending prices: 55, 22, 8, 14, 6. Dividends: 0.75, 0.10, 0, 0.05, 0. Shares outstanding: 3,000; 10,000; 5,000; 8,000; 7,000.
1. Price returns by stock: +10%, -12%, -36%, +40%, +50%. Total returns: 11.5%, -11.6%, -36%, 40.5%, 50%.
2. Price-weighted: BOP sum 101.5, divisor 5, level 20.30; EOP sum 105 gives 21.00; PR = 3.45%; TR = (105 + 0.90 - 101.5)/101.5 = 4.33%.
3. Equal-weighted (20% each): PR = 10.40%, TR = 10.88%.
4. Cap-weighted: BOP caps total 570,500 (weights 26.29, 43.82, 10.96, 14.02, 4.91%); PR = 1.49%, TR = 2.13%; level 1,000 to 1,014.90 (price), 1,021.30 (total).
5. Float-adjusted (floats 100, 70, 90, 25, 80%): BOP cap 423,650; PR = -1.66%, TR = -0.94%.
6. Split check: A splits 2-for-1 (55 to 27.50). Sum of prices falls 105 to 77.50; new divisor = 77.50/21.00 = 3.69; A's weight drops from 52.38% to 35.48%.
Interpretation: same stocks, four answers from -1.66% to +10.40%. The large drop in heavily weighted B (a big cap stock, -12%) and rise of small names explain why equal-weight leads; float adjustment cuts the weight of closely held D (+40%), so float-cap does worse.

Short exam-style check: equal-weighted index of Able (10 to 12, div 0.75), Baker (20 to 19, div 1.00), Charlie (30 to 30, div 2.00): PR = (20% - 5% + 0)/3 = 5.0%; TR = 11.4%.

## Anti-patterns
- Comparing a price return index to a total return fund (overstates the shortfall, the gap widens with time).
- Assuming "equal weighted beating cap weighted" is manager skill; it usually means small-caps outperformed.
- Benchmarking a style or small-cap manager against a broad market index.
- Treating the divisor as constant; ignoring that splits distort price-weighted indexes (DJIA 30 stocks only).
- Believing a bond index is as cheaply replicable as an equity index.
- Using a hedge fund index without adjusting for survivorship and self-selection.

## Exam Focus & Traps
- Index value after a split: unchanged, divisor adjusted; the weights change only in price-weighted indexes.
- Total return index equals price index only at inception (or if no income is paid); not on rebalancing dates.
- Weights in return calculations are beginning-of-period weights.
- Equal weighting requires the most frequent rebalancing; price weighting is not rebalanced; cap weighting rebalances itself.
- Fundamental weighting has a value tilt and contrarian effect; cap weighting a momentum effect.
- Reconstitution reduces the chance the index no longer represents its target market (it does not reduce turnover).
- First step in construction: define the target market (it sets the universe).
- Hedge fund indexes: constituents determine the index (not the provider).
- Commodity index return components: interest, spot price change of futures, roll yield.

## Key Takeaways
1. An index is a portfolio with rules; return equals weighted average of constituent returns using beginning weights.
2. Total return index minus price index gap grows with time due to reinvested income.
3. The divisor absorbs non-price changes: splits and membership changes.
4. Weighting method is the main source of return differences between indexes on the same stocks.
5. Cap weighting self-rebalances but has momentum bias; equal and fundamental weighting need rebalancing and are contrarian.
6. Rebalancing resets weights; reconstitution resets membership; both create turnover and market impact.
7. Pick benchmarks to match mandate; use a beta-matched index plus cash to compute alpha.
8. Fixed income, commodity, real estate and hedge fund indexes each carry structural biases (liquidity, roll yield, appraisal smoothing, survivorship).

## Connects To
- **ch01**: market organization (dealer markets explain fixed-income index pricing problems).
- **ch04**: portfolio management overview (benchmarks and passive vs active choices).
- **ch05-06**: CAPM and beta use broad indexes as the market proxy.
- **ch03**: market efficiency (why index funds are a defensible default).
- **ch11**: ETFs are built on these indexes.
- **ch18**: performance evaluation depends on correct benchmark selection.
- **`cfa-equity-portfolio-management` ch02**: passive equity investing, index replication, tracking error.
- **`cfa-level1-curriculum` ch09**: personal notes on this reading.
