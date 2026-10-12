# Chapter 17: Trade Strategy and Execution
> **Source**: CFA Program Curriculum 2023, Level III, Reading 25 · Portfolio Management | Bernd Hanke, Robert Kissell, Connie Li, Roberto Malamut

## Core Idea
Trading is the last link of the investment process: a good idea is worth only what survives implementation. The trade strategy (how fast, where, with which benchmark and algorithm) follows from why the manager trades (profit, risk, cash flow, index/corporate event), and from four inputs: order, security, market conditions and trader risk aversion. The central tension is the trader's dilemma (trading too fast creates market impact, too slow creates market risk and alpha decay). Costs are measured ex post with implementation shortfall (IS), decomposed into delay, trading (execution), opportunity and fixed costs, and cross-checked against benchmarks (arrival, VWAP, TWAP, close), a market-adjusted cost and a pre-trade estimate. Governance (trade policy, best execution, allocation, error log) closes the loop.

## Learning Outcomes Covered
- Discuss motivations to trade and how they relate to trading strategy
- Discuss inputs to the selection of a trading strategy
- Compare benchmarks for trade execution
- Recommend and justify a trading strategy (given relevant facts)
- Describe factors that determine the selection of a trading algorithm class
- Contrast equity, fixed income, options and futures, OTC derivatives and spot currency markets for trade implementation
- Explain how trade costs are measured and determine the cost of a trade
- Evaluate the execution of a trade
- Evaluate a firm's trading procedures (processes, disclosures, record keeping) for good governance

## Frameworks Introduced
- **Motivation-to-urgency map**: four motivations drive the strategy.
  - Profit seeking: urgency follows expected alpha decay (short-term event or mispricing: high urgency; long-term fundamental or value: low urgency).
  - Risk management / hedging: rebalance to target risk, duration, beta; derivatives (futures) are cheap if the mandate allows, otherwise ETFs or the underlying; illiquid underlying raises cost.
  - Cash flow: inflows/outflows, redemptions, margin calls (margin call: urgent; redemption at NAV: low urgency, trade at the close).
  - Corporate actions / index reconstitution / distributions: index funds trade at the close to match the benchmark and NAV price.
  - When to use: first step of any trade ticket; it tells you urgency and the right benchmark.
- **Four strategy inputs**: order (side, size, % of ADV), security (type, short-term alpha, volatility, liquidity profile), market conditions (current volume, spreads, volatility, liquidity crises, seasonality), user risk aversion (higher aversion means higher urgency).
- **Trader's dilemma**: "Trading too fast results in too much market impact, but trading too slow results in too much market risk." Choose the best price-time trade-off by slicing the order.
  - Impact (temporary: reverts after the trade; permanent: information content) falls as the horizon lengthens; execution risk (about volatility times square root of time) rises with it.
- **Reference price (benchmark) taxonomy**:

| Category | Benchmarks | Typical user |
|---|---|---|
| Pre-trade (known before trading) | decision price, previous close, opening price, arrival price | alpha-driven PMs (arrival/decision); quants (previous close as decision proxy) |
| Intraday | VWAP, TWAP | passive/rebalancing, no short-term view, two-sided lists |
| Post-trade | closing price | index funds, NAV-valued funds, tracking-error control |
| Price target | fair value limit (for example buy at $20.50 or better) | PMs with a valuation view |

  - Do not use the opening price as benchmark if you trade in the opening auction (your order moves it); same for the close and the closing auction when measuring versus the close of your own order.
- **Strategy by trade type** (the five curriculum cases):
  - Short-term alpha equity buy: high urgency, price target benchmark (limit); part in opening auction (sized to expected auction volume, roughly 1% to 4% of daily volume) plus arrival price algorithm for the rest; avoid dark pools (risk of non-execution).
  - Long-term alpha fixed income (illiquid bond): no urgency; sell gradually over days or weeks in varied sizes to limit information leakage and dealer inventory pressure; reference prices are weak because unrelated market moves swamp impact.
  - Risk rebalance (macro fund, cut risk from 14% toward 10% target): passive, TWAP over one to two days; keep the buy/sell list balanced in beta so the hedge holds.
  - Client redemption at NAV: closing price benchmark; send to the closing auction; if the order is large relative to auction liquidity (for example 50% of closing volume), split (for example 90% auction, 10% VWAP into the close) to avoid pushing NAV and hurting the client.
  - New index mandate (for example $150m Russell 2000, 3% TE): equitize with futures near the close (or ETF if derivatives are barred), then build the stocks over days and unwind the futures.
- **Execution implementation menu**:
  - Principal (broker risk) trade: the broker takes the risk and prices it into the spread. Agency trade: the broker only finds the other side; risk stays with the buy side.
  - High-touch (humans, blocks, illiquid securities) versus low-touch (DMA and algorithms, liquid securities).
  - Quote-driven (dealers, RFQ: non-binding quotes valid only when given) versus order-driven (limit order books).
- **Algorithm classes**:

| Class | How it trades | Use when | Weakness |
|---|---|---|---|
| Scheduled: POV | follows real-time volume at a participation rate (10% means 1,000 shares per 10,000 traded) | no adverse price view, order about 5% to 10% of volume or less | chases price; may not finish |
| Scheduled: VWAP | time slices on historical U-shaped volume curve | same; part of a risk-balanced basket | forces trades in thin markets; may not finish |
| Scheduled: TWAP | equal slices per period | completion within the window is the priority; volume uncertain or spiky | ignores liquidity |
| Liquidity seeking (opportunistic) | trades fast when liquidity at a good price appears, sweeps the book, uses dark pools | large order, fast, minimal leakage, thin/episodic liquidity | market-order heavy |
| Arrival price | front-loaded, near price at order receipt | adverse price expectation, high risk aversion, liquid stock, order under about 15% of volume | higher impact |
| Dark aggregator | executes only in non-displayed venues | very large order vs volume, wide spreads, leakage fear, need not fill fully | execution uncertainty |
| Smart order router (SOR) | routes small orders to best venue (NBBO for market orders, highest fill probability for limits) | small orders, many venues, fast markets | not for large orders |

  - Algorithm types by purpose: execution algorithms (implement a PM decision) versus profit-seeking algorithms (decide and trade: electronic market makers, quant funds, HFT).
  - Machine learning in execution: clustering groups stocks by microstructure features (spread, trade size, volatility, tick size, queue depth, volume) to pick the best algorithm per cluster; LASSO (penalized regression assuming sparsity) selects the few relevant predictors for high-frequency short-term forecasts.
- **Market comparison for implementation**:

| Market | Structure and transparency | Large urgent | Large non-urgent | Small |
|---|---|---|---|---|
| Equities | lit exchanges plus dark pools/ATS/MTF/SI; most advanced, fragmented | broker risk trade (small caps) | algorithms (large caps) or high-touch agency (illiquid) | electronic |
| Fixed income | bilateral, dealer-centric, opaque; algorithms mostly on-the-run Treasuries and bond futures | broker risk via RFQ | high-touch agency | broker risk via RFQ |
| Exchange-traded derivatives | transparent; futures dominate volume | sweep the book | algorithms | DMA |
| OTC derivatives | dealers; post-trade reporting (SDRs) under Dodd-Frank, push to central clearing | broker risk | high-touch agency (customization may need price concession) | n/a |
| Spot FX | fully OTC, tiered interbank structure, opaque; no central venue | RFQ to several dealers | algorithms (TWAP) or agency | DMA |

- **Implementation shortfall (Perold)**: `IS = Paper return − Actual return` where paper = all shares at the decision price Pd with no cost.
  - `IS = [Σsⱼpⱼ − Σsⱼ·Pd] + (S − Σsⱼ)(Pn − Pd) + Fees` = execution cost + opportunity cost + fixed fees; S > 0 buy, S < 0 sell.
  - Express in bps as `IS / (S × Pd) × 10,000` (denominator: total order shares times decision price, not executed shares).
- **Expanded IS (Wagner)**: execution cost splits into delay cost `Σsⱼ(P0 − Pd)` (decision to market release, P0 = arrival price) and trading cost `Σsⱼpⱼ − Σsⱼ·P0`.
  - `Expanded IS = Delay + Trading + Opportunity + Fees`.
  - Delay: cut it with pre-trade analysis and broker/algorithm performance metrics so the trader can release immediately. Opportunity: cut it by sizing the order to what the market absorbs inside the PM's price limit and redirecting cash to the next best idea.
- **Benchmark cost formulas (post-trade TCA)**: `Cost = Side × (P − P*) / P* × 10,000 bps` (Side = +1 buy, −1 sell; P = average execution price; P* = reference). Positive means underperformance, negative means saving.
  - Arrival cost (P* = arrival price: equals the trading cost component), VWAP cost, TWAP cost, closing (MOC) cost, always evaluate against the benchmark selected at the strategy stage.
  - **Market-adjusted cost** `= Arrival cost − β × Index cost`, with `Index cost = Side × (Index VWAP − Index arrival)/Index arrival × 10,000`. It strips out the part of the move that would have occurred without your order.
  - **Added value** `= Arrival cost − Estimated pre-trade cost` (positive means worse than the pre-trade model expected).
- **Trade governance**: written trade policy (mandated by SEC, MiFID II, Japan FSA, Hong Kong SFC) covering: meaning of best execution, factors determining the execution approach, eligible brokers and venues, monitoring process, aggregation/allocation, trade-error treatment.
  - Best execution = most favorable terms for the client across price, cost, speed, likelihood of execution and settlement, size, nature of the trade; it is a trade-off, not "lowest cost at all times".
  - MiFID II: "all sufficient steps" (stricter than MiFID I's "all reasonable steps"); bans bundling of commissions with research (soft dollars).

## Key Concepts
- **Trade urgency**: how fast (aggressively) or slow (patiently) an order is executed over its horizon; higher with high alpha decay, directional exposure or high risk aversion.
- **Alpha decay**: erosion of short-term alpha after the decision, caused by price moving toward the forecast whether or not you trade.
- **Short-term (trade) alpha**: expected price move over the trading horizon excluding your own impact (appreciation, depreciation or reversion).
- **Information leakage**: disclosure of trading intent that moves prices against you; mitigated by splitting orders, varying size/venue/order type and using dark venues.
- **Lit versus dark venue**: lit venues show pre- and post-trade prices, size and depth; dark pools report only post-trade, so fills depend on an offsetting order arriving.
- **Market impact**: adverse price move caused by your order; temporary (reverts) plus permanent (information). Larger % of ADV means larger impact.
- **Execution risk**: risk of adverse price movement during the horizon, proxied by volatility; falls as urgency rises.
- **Percentage of ADV**: order size divided by average daily volume, the standardized size measure (1m shares is 2% of ADV for a 50m-ADV stock but 25% for a 4m-ADV stock).
- **Liquidity and volatility**: negatively related; in crises (1987, LTCM 1998, 2008, quant deleveraging of August 2007) liquidity collapses while volatility spikes. On-the-run government bonds are liquid, off-the-run less so.
- **Equitization**: temporarily investing cash with futures or ETFs to avoid cash drag until the underlying positions are built.
- **Market-on-close (MOC) / closing auction**: execution at the official close, matching NAV and index valuation.
- **Direct market access (DMA)**: buy side uses a broker's connectivity to hit the exchange order book itself.
- **Front running**: trading ahead of anticipated orders; illegal where information is improperly obtained; a risk of slow high-touch execution in liquid names.
- **Trade aggregation and allocation policy**: pooled fills are allocated pro rata (and fairly pre- and post-trade) with an audit trail.
- **Trade error log**: errors and any gain or loss are reported to compliance and documented; the goal is that the client suffers no adverse impact.
- **Best Execution Monitoring Committee (BEMC)**: cross-functional body (execution, compliance, risk) that maintains the broker list and reviews execution quality; records kept for years (five years in the United Kingdom).
- **Illegal practices named**: fake volumes (venue trades with itself), quote stuffing (flooding orders and cancellations), spoofing (bidding or offering with intent to cancel).

## Formulas & Reference Tables
| Quantity | Formula |
|---|---|
| Order size relative | `% ADV = Order shares / ADV` |
| Paper return | `(Pn − Pd) × S` |
| Actual return | `Σsⱼ·Pn − Σsⱼ·pⱼ − Fees` |
| Execution cost | `Σsⱼ·pⱼ − Σsⱼ·Pd` |
| Opportunity cost | `(S − Σsⱼ)(Pn − Pd)` |
| Fixed fees | `|Σsⱼ| × fee per share` |
| IS ($) | `Execution + Opportunity + Fees` |
| IS (bps) | `IS($) / (|S| × Pd) × 10,000` |
| Delay cost | `Σsⱼ·P0 − Σsⱼ·Pd` |
| Trading cost | `Σsⱼ·pⱼ − Σsⱼ·P0` |
| Cost ($) / ($ per share) / (bps) | `Side×(P−P*)×Shares` / `Side×(P−P*)` / `Side×(P−P*)/P*×10⁴` |
| Index cost (bps) | `Side×(Index VWAP − Index arrival)/Index arrival × 10⁴` |
| Market-adjusted cost | `Arrival cost − β × Index cost` |
| Added value | `Arrival cost − Pre-trade estimated cost` |
| TWAP | simple average of prices over the horizon |
| VWAP | `ΣPᵢQᵢ / ΣQᵢ` |

Benchmark-to-situation selector:
| Situation | Benchmark | Strategy |
|---|---|---|
| Short-term alpha, high decay | arrival or decision price (plus price target) | arrival price algorithm, front-loaded |
| No view, rebalancing two-sided list, low urgency | VWAP or TWAP | scheduled algorithm |
| Spiky volume, completion priority | TWAP | TWAP (finishes in the window) |
| Index fund, redemption at NAV, index change | closing price | MOC / closing auction (plus futures equitization for inflows) |
| Large order, leakage fear, fill not mandatory | arrival/VWAP with limits | dark aggregator or liquidity seeking |
| Small marketable order, many venues | NBBO / best price | smart order router |
| Illiquid bond, no urgency | none reliable | gradual high-touch, multiple dealer quotes |

Mapping urgency drivers:
| Raises urgency | Lowers urgency |
|---|---|
| High alpha decay, adverse trend (buying in rising market) | Low decay, favorable trend |
| High risk aversion, directional (all-buy) list | Balanced buy/sell list (net beta near zero) |
| Margin call | Redemption at NAV, quarterly hedge-fund redemption |
| Small order, liquid stock | Large order, illiquid stock (patience cuts impact) |

## Mental Models
- **Urgency is priced in two currencies**: pay impact to go fast, pay risk and alpha decay to go slow; the optimum depends on decay rate, volatility and risk aversion.
- **Match benchmark to mandate, not to convenience**: the benchmark chosen at the strategy stage must also be used in the post-trade evaluation.
- **IS is the full bill**: only IS sees unfilled shares (opportunity cost) and the delay between decision and release; arrival cost sees only trading cost.
- **Delay and opportunity costs are the controllable leaks**: fix them with process (pre-trade analysis, broker scorecards) and by sizing orders to liquidity.
- **Correct for the tide**: buying in a rising market looks expensive even when the trader did well; subtract beta times index move.
- **The same trade, different venue**: liquid and standardized means electronic; illiquid, customized or large means dealer or broker.
- **A fund valued at the close should trade at the close** (unless that harms the client through impact).
- **Algorithm choice is a data problem**: cluster stocks by microstructure, test algorithms per cluster, then optimize.

## Worked Example
**Impulse Robotics (CFA example, recomputed).** Decision price Pd = 10.00 (Monday close). Tuesday: limit buy 1,000 at 9.98, no fill, order expires, close 10.05. Wednesday (new limit 10.07): released when price is 10.03 (30 minutes after the PM's order), 700 shares filled at 10.07, fees 14, close 10.08; 300 shares canceled.
- Paper gain = 1,000 × (10.08 − 10.00) = 80; actual = 700 × 10.08 − 700 × 10.07 − 14 = −7; IS = 80 − (−7) = 87, which is 87 bps of 10,000.
- Execution cost = 700 × (10.07 − 10.00) = 49; opportunity cost = 300 × (10.08 − 10.00) = 24; fees = 14; total 87.
- Expanded: delay = 700 × (10.03 − 10.00) = 21; trading = 700 × (10.07 − 10.03) = 28; opportunity 24; fees 14; total 87. Delay is 24.1% and opportunity 27.6% of the cost: more than half the cost is process and sizing, not market impact.

**RLK buy (CFA in-text question, recomputed).** Buy 100,000 at decision price 30.00, limit 30.50, released at 30.10, 80,000 filled (30,000 at 30.20, 20,000 at 30.30, 20,000 at 30.40, 10,000 at 30.50), commission 0.02, close 30.65.
- Execution = 2,425,000 − 2,400,000 = 25,000; opportunity = 20,000 × 0.65 = 13,000; fees = 1,600; IS = 39,600 = 132 bps of 3,000,000.
- Delay = 80,000 × 0.10 = 8,000 (20.2%); trading = 2,425,000 − 2,408,000 = 17,000; opportunity 13,000 (32.8%).
- Diagnosis: trim the order to 80,000 and put the other 600,000 into the second-best idea; add broker metrics to cut the 10:30 delay.

**Benchmark costs and market adjustment (all recomputed).**
- Buy at 30.05 vs arrival 30.00: +16.7 bps. Buy at 30.05 vs VWAP 30.04: +3.3 bps (underperformed). vs TWAP 30.06: −3.3 bps (outperformed). MOC buy at 30.40 vs close 30.50: −32.8 bps (better than the close).
- Buy at 30.50, arrival 30.00: arrival cost 166.7 bps; index 500 to VWAP 505 = 100 bps; beta 1.25 so expected move 125 bps; market-adjusted cost = 41.7 bps.
- Added value: executed at 50.35 vs arrival 50.00 = 70 bps against a 60 bps pre-trade estimate: +10 bps worse than expected.

**Practice-problem recomputations (BYYP and West Commerce).**
- BYYP (buy 120,000 at decision 40.00, released 40.50, 90,000 filled for 3,727,500, average 41.4167, fee 0.02, close 42.50): execution 127,500 (delay 45,000 + trading 82,500); opportunity 30,000 × 2.50 = 75,000; fees 1,800; IS = 204,300 = 425.6 bps. Arrival cost: 226.3 bps with the exact average (227.2 bps with the rounded 41.42 used in the printed answer); answer B either way.
- West Commerce (sell 10,000 at decision 27.10, released 26.90, 9,000 filled at average 26.6333, fee 0.03, close 26.00): execution 4,200; opportunity 1,000 × 1.10 = 1,100; fees 270; IS = 5,570 = 205.5 bps (answer C); delay = 9,000 × 0.20 = 1,800. Arrival cost = +99.1 bps (100.4 with the rounded 26.63), index cost for a sell with index 600 to 590 = +166.7 bps, market-adjusted = 99.1 − 0.9 × 166.7 = about −50 bps, a saving of about 50 bps (answer B).
- LIM (buy 25,000, decision 23.01, released 23.09, average 23.45, index 2,150 to 2,184, beta 0.95): delay = 25,000 × 0.08 = 2,000; arrival cost 155.9 bps; index 158.1 bps; market-adjusted 155.9 − 0.95 × 158.1 = 5.7 bps, so almost all the cost came from buying in a rising market.
- ADV test: ABC 45,000 / 195,000 = 23.1% (greatest impact); DEF 1.3%; XYZ 1.1% but highest volatility (greatest execution risk).

## Anti-patterns
- **Benchmarking a closing-auction order against its own close, or an opening-auction order against the open**: the order contaminates the reference.
- **Using a passive VWAP/TWAP or dark pool for a short-lived mispricing**: alpha decays before you finish, and dark fills may never come.
- **Dumping a large redemption into the closing auction**: a 50% share of closing volume depresses NAV and the client's proceeds (fiduciary problem).
- **Reading arrival cost as total cost**: it excludes delay (decision to release) and opportunity cost (unfilled shares).
- **Keeping a stale-limit order size**: sizing beyond what the market absorbs inside the limit leaves a large opportunity cost; trim and reallocate.
- **Ignoring market drift in TCA**: judging a trader or broker on unadjusted cost in a rising (buys) or falling (sells) market.
- **One execution approach for all asset classes**: the optimal approach differs by asset class, liquidity and market mechanism (Theme 1 in the curriculum case); only the principles (and the broker selection process) should be consistent.
- **Defining best execution as the lowest price and cost only**: omits speed, likelihood of execution and fit with the investment process.
- **Choosing a broker by relationship comfort**: an exclusive broker needs regular, documented, unbiased comparison; subjective opinion is not justification.
- **Using high-touch for liquid names**: slow, opaque, costly, exposed to front running.
- **Handling trade errors informally**: errors and gains or losses must be logged and escalated to compliance.
- **Hiding all-buy list risk**: an all-buy or all-sell basket has market exposure; mix sides or hedge to keep a balanced beta.

## Exam Focus & Traps
- **Statement checks**: higher urgency means lower execution risk (true); higher urgency with larger size increases market impact (not reduces); high alpha decay demands more aggressive trading (not less).
- **TWAP versus VWAP versus POV**: TWAP is chosen to exclude outliers (benchmark) and to guarantee completion in the window (algorithm); VWAP and POV may fail to finish in thin markets.
- **Benchmark mapping**: price-target benchmark for a valuation-limited buy; arrival or decision for alpha trades; closing price for index funds, redemptions and index changes; previous close is a proxy for decision price for quant models.
- **Algorithm mapping**: arrival price needs liquid stock and order under about 15% of volume; scheduled needs order up to about 5% to 10% of volume; a 20% order with leakage worry points to liquidity seeking; dark aggregator needs tolerance for partial fills.
- **Dark pool facts**: transactions and quantities are always reported post-trade (so "not reported" is false); anonymity yes, certainty of execution lower.
- **IS denominator**: total order shares times decision price (100,000 × 30.00), not executed shares.
- **Sell-side signs**: for a sell, cost uses side = −1; a sale executed below arrival is a positive cost; a falling market makes the unadjusted cost look worse and the market-adjusted cost smaller.
- **Opportunity cost for unfilled shares uses Pn − Pd**, with the sign of the order (sell: Pd − Pn gain or loss reversed by S < 0).
- **Rounding**: use unrounded average prices; the printed answers sometimes round the average (227.2 vs 226.3 bps; 100.4 vs 99.1 bps) but the option choice does not change.
- **Market-adjusted cost uses the stock's beta**, not 1; subtract beta times index cost.
- **Delay cost uses executed shares only** (opportunity cost covers the rest).
- **Fixed income and OTC**: bilateral and dealer-centric; algorithms mainly for on-the-run Treasuries; large urgent trades go to broker risk via RFQ; large non-urgent to high-touch agency.
- **Derivatives for hedging**: futures first if the mandate allows; else ETFs; for specialized sector or geographic credit risk, trade the cash securities.
- **MiFID II**: "all sufficient steps"; soft-dollar bundling banned; research must be paid explicitly.
- **Trade errors**: disclose to compliance and document so the client suffers no adverse impact; "disclose all errors to clients" is not the stated policy.
- **Pro-rata allocation** of partially filled pooled orders is correct governance; a list of pre-approved, regularly reviewed brokers is correct; "lowest-cost brokers only" is wrong (quality, stability, settlement, capital commitment also count).
- **Opportunity cost of ordering**: ABC/XYZ illustration: knowing only 80,000 ABC shares can be filled below fair value and redirecting 20,000 shares to XYZ turned $20,000 of profit into $24,000.

## Key Takeaways
1. Start with the motivation to trade; it sets urgency and the benchmark (profit: arrival/decision; rebalance: VWAP/TWAP; cash flow and index: close).
2. Four inputs (order, security, market conditions, risk aversion) plus alpha decay choose the point on the impact-versus-risk frontier.
3. Large % of ADV, illiquidity and low decay argue for patience; high decay, volatility, directional exposure and risk aversion argue for speed.
4. Match algorithm class to the situation: scheduled for small low-view orders, liquidity seeking and dark aggregators for large leakage-sensitive orders, arrival price for urgent liquid orders, SOR for small orders.
5. Equities and exchange-traded derivatives are electronic; fixed income, OTC derivatives and large or illiquid trades rely on dealers and high-touch; spot FX is a tiered OTC market.
6. IS = execution + opportunity + fees; expanded IS splits execution into delay and trading; delay and opportunity are the most manageable leaks.
7. Evaluate with the benchmark chosen at the strategy stage, and use market-adjusted cost and added value to separate skill from market drift and pre-trade expectation.
8. Good governance: written trade policy with a broad best-execution definition, approved and monitored brokers (BEMC), pro-rata allocation, trade error log, long record retention.

## Connects To
- **ch16**: effective spread, VWAP cost and the Level II IS concept; this chapter provides the full Level III decomposition and the algorithm and strategy layer.
- **ch15**: transfer coefficient and turnover costs; execution shortfall is one reason realized IR is below the fundamental-law forecast.
- **ch11**: ETFs and futures used for equitization and hedging; creation/redemption affects ETF trading cost.
- **ch18**: execution costs are embedded in realized portfolio returns that performance evaluation analyzes; trade costs are part of transactions-based attribution.
- **ch13 and ch08**: risk targets (volatility, duration, beta) that trigger risk-rebalance trades.
- **`cfa-equity-portfolio-management` ch04**: portfolio construction, transaction cost and turnover constraints.
- **`cfa-ethics-gips`**: Standard III(A) best-execution duty to clients, fair allocation, and market-manipulation practices (spoofing, quote stuffing).
