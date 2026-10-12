# Chapter 16: Trading Costs and Electronic Markets
> **Source**: CFA Program Curriculum 2022, Level II, Reading 44 · Portfolio Management | Larry Harris (drawn from *Trading and Electronic Markets: What Investment Professionals Need to Know*, CFA Institute Research Foundation, 2015)

## Core Idea
Trading costs are a direct drag on portfolio performance and come in explicit (receipted) and implicit (price impact, delay, opportunity) forms. Each measurement method answers a different question: effective spread measures cost at the moment of one trade, VWAP compares you with other traders, implementation shortfall measures the total cost of carrying out the investment decision. Electronic markets have cut costs but fragmented liquidity, created speed competition and new systemic and abuse risks that desks, algorithm designers and regulators must manage.

## Learning Outcomes Covered
- Explain components of execution costs (explicit vs. implicit)
- Calculate and interpret effective spreads and VWAP transaction cost estimates
- Describe the implementation shortfall approach
- Describe the factors driving electronic trading systems and market fragmentation
- Identify and contrast types of electronic traders
- Describe characteristics and uses of electronic trading systems and the advantages of low-latency traders
- Describe risks of electronic trading and regulatory mitigation
- Describe abusive practices detectable by real-time surveillance

## Frameworks Introduced
- **Cost taxonomy**: fixed costs (buy-side traders, systems, space) plus variable costs = explicit (commissions, taxes, stamp duties, exchange fees: costs you can get a receipt for) + implicit (bid-ask spread, market impact, delay/slippage, opportunity cost).
  - When to use: decompose any execution cost report; explicit costs are visible, implicit costs must be estimated against a benchmark price.
- **Effective spread method** (benchmark = midquote at order entry/trade):
  - Cost per share, buy: `Trade price − (Bid + Ask)/2`; sell: `(Bid + Ask)/2 − Trade price`. Total cost = cost per share × trade size. Effective spread = 2 × cost per share.
  - When to use: single-fill, small orders. Failure mode: understates costs for large orders split into pieces (market impact moves the later midquotes) and ignores delay and opportunity costs. Price improvement (filled inside the quote) makes it smaller than the quoted spread; walking the book makes it larger.
- **VWAP transaction cost estimate** (benchmark = interval VWAP from order start to completion):
  - Buy: `(Trade VWAP − VWAP benchmark) × Trade size`; sell: `(VWAP benchmark − Trade VWAP) × Trade size`.
  - When to use: simple to interpret ("did I do better than everyone else trading while I traded?") and for evaluating algorithms that spread orders through the day.
  - Failure mode: biased toward zero when your trades are a large share of volume or trade at the market rate, because you are the VWAP. A lone large buyer has an estimated cost of zero regardless of impact. Sponsors should be wary of managers who only report VWAP.
- **Implementation shortfall (IS)** (benchmark = decision/arrival/strike price, the midquote when the decision to trade was made): value of a paper portfolio that traded the full order at the decision price minus the actual portfolio value. Captures all explicit costs plus market impact, delay and opportunity costs. (Detailed decomposition at Level III; see ch17.)
  - When to use: the investment-management perspective; the only one of the three that includes unfilled orders.
  - Caveat: opportunity cost depends on the time window and the assumed fill price.
- **Limit order book / market spread logic**: best bid (inside bid) and best ask (inside ask) across dealers define the market (inside) spread, which is narrower than any single dealer's spread; a market order walks the book, so impact grows with order size relative to depth.
- **Why speed matters (taking, making, canceling)**: electronic traders need to take opportunities before others, acquire time precedence when making liquidity, and cancel stale orders quickly. Value comes from being faster than competitors, not from absolute speed.
- **Latency model**: total latency = learn about the event + decide/respond + transmit the order. Minimize by colocation (servers in the exchange's room, equal-length cables for fairness), microwave rather than fiber links, fewer routers, direct data feeds, fast hardware, fast in-memory code and precomputed contingency tables.
- **Systemic-risk controls**: pre-launch software testing and exchange mock sessions, market access controls, developer access controls with peer review, real-time order-flow surveillance with automatic shut-off, ban on sponsored naked access, price limits and trading halts, converting market orders into marketable limit orders.

## Key Concepts
- **Explicit costs**: direct, receipted costs (commissions, transaction taxes, stamp duties, exchange fees).
- **Implicit costs**: indirect costs from price concessions: spread, market impact, delay and opportunity costs; no receipt, but real.
- **Market (price) impact**: price concession needed to complete a trade; small for small orders (cost is the spread), large when you must walk the book.
- **Delay cost (slippage)**: loss when price moves away between decision and execution, often from information leakage.
- **Opportunity cost**: loss from the portion of an order not executed while price moves in the expected direction.
- **Quoted (market/inside) spread**: best ask minus best bid; **midquote** = (best bid + best ask)/2.
- **Effective spread**: twice the signed distance between trade price and prior midquote; the spread actually experienced.
- **Price improvement**: execution at a better price than the quoted bid/ask.
- **Dealer**: trades for its own account and provides immediacy; essential in markets where buyers and sellers rarely coincide (most bond markets).
- **Market fragmentation**: the same instrument trades on multiple venues (exchanges, ATS/ECN/MTF, dark pools, dealers), so liquidity per venue is a small fraction of the total; handled via liquidity aggregation ("super books") and smart order routing.
- **Order-driven market**: orders are matched by rules (exchange, ATS or broker system); electronic systems have largely replaced floors here.
- **High-frequency trader (HFT)**: completes round trips within about a minute (often milliseconds), trades in and out many times a day in small size; **low-latency trader** may hold up to a day or more (news traders, parasitic traders).
- **Parasitic traders**: front runners (trade ahead of liquidity demanders) and quote matchers (lean on standing orders' option value).
- **Hidden order / IOC order / pinging**: hidden orders are visible only to the venue/broker; immediate-or-cancel (IOC) orders probe for hidden liquidity; pinging uses tiny IOCs to detect hidden orders.
- **Pegged (floating) limit order**: limit price keeps a fixed distance from a benchmark (for example two ticks below the ask), needing very low latency.
- **Dark pool**: venue that does not publish its liquidity and is open to selected clients; **midspread order** is pegged to the quote midpoint.
- **Flickering quote / leapfrog**: exposed orders quickly placed and canceled; dealers repeatedly improving by one tick to jump ahead of buy-side bids when spreads are wide.
- **Collocation**: placing traders' servers in the exchange's data center.

## Formulas & Reference Tables
| Quantity | Formula |
|---|---|
| Quoted spread | `Ask − Bid` |
| Midquote | `(Bid + Ask)/2` |
| Effective spread (per share, buy) | `2 × [Trade price − Midquote]` |
| Effective spread (per share, sell) | `2 × [Midquote − Trade price]` |
| Effective-spread cost estimate | `[Trade price − Midquote] × Trade size` (buy), sign reversed for sell; for multi-fill orders sum fills |
| VWAP | `Σ(Pᵢ·Qᵢ)/ΣQᵢ` |
| VWAP cost estimate | `(Trade VWAP − VWAP) × Size` (buy); `(VWAP − Trade VWAP) × Size` (sell) |
| Implementation shortfall | `Paper portfolio value (at decision price) − Actual portfolio value`; in cost terms = explicit costs + execution/impact + delay + opportunity |
| Latency (serial process) | `Σ step latencies`; light travels about 300 km per ms in vacuum, around 31% slower in fiber (Chicago-New York 1,146 km: minimum round trip about 8 ms; New York-London 5,576 km: about 37 ms) |
| Crude impact loss (Flash Crash) | `average impact ≈ ½ × price drop (uniform fill)`: 0.5 × 5% = 2.5% × $4.1bn ≈ $100m ≈ 0.37% of $27bn fund |

| Measure | Benchmark price | Includes delay? | Includes unfilled? | Bias |
|---|---|---|---|---|
| Effective spread | Midquote at trade/order entry | No | No | Understates large split orders |
| VWAP | Interval volume-weighted average | Partly | No | Toward zero when you dominate volume |
| Implementation shortfall | Decision/arrival midquote | Yes | Yes | Sensitive to horizon and fill assumption |

Electronic trader taxonomy:
| Type | What it does | Risk/edge |
|---|---|---|
| Electronic dealer | Posts bids/offers, profits from round-trip spreads; cancels around news and scheduled releases; keeps small inventory | Adverse selection from news traders |
| Electronic arbitrageur | Trades legs of an arbitrage portfolio across markets: (1) take both legs (safest, costliest), (2) offer one leg and take the other, (3) offer both legs (cheapest, riskiest, legging risk) | Needs very fast systems |
| News trader | Parses news feeds, sends marketable orders against stale quotes; may be right only occasionally | Round-trip costs when wrong |
| Front runner (order anticipation) | Detects large orders being sliced from patterns and trades ahead; legal if information is properly obtained (market data), illegal if from tips | Raises costs for liquidity demanders |
| Quote matcher | Leans on standing orders as free options; exits against them if wrong | Standing order may vanish |
| Buy-side trader (OMS + algos) | Fills portfolio manager orders via brokers' algorithms | Needs randomization to avoid detection |

## Mental Models
- **Match the benchmark to the question**: "what did this single fill cost?" is effective spread; "did I beat the market while trading?" is VWAP; "what did it cost to implement the decision?" is implementation shortfall.
- **Zero VWAP cost is not zero cost**: if you were the market, VWAP is blind to your impact; always cross-check with arrival price.
- **Liquidity is a cost-time trade-off**: impatience pays spread and impact; patience pays delay and opportunity costs. Optimal execution balances the two (see ch17).
- **Speed is zero-sum and relative**: the HFT arms race burns resources to gain precedence; liquidity demanders ultimately bear the costs.
- **Algorithms leak patterns**: constant child-order size or timing is a signal for order-anticipation AI; randomize size, timing and venue.
- **Models fail in regime change**: machine-learning trading systems learn from repeated patterns and have little precedent to rely on in volatility spikes, so a kill switch is standard.

## Worked Example
**Illiquid stock sale (Level II Example 1, recomputed).** Sell 12,000 shares of a small cap (limit C$9.95): three sell orders, 2,000 at 10.15 (market 10.12/10.24), 3,000 at 10.11 (market 10.11/10.22), 5,000 at 10.01 average (market 10.05/10.19); 2,000 shares unfilled and canceled; other tape: 2,000 at 10.20 and 1,000 at 10.15; next-day price 9.50.
- Quoted spreads: 0.12, 0.11, 0.14 (average 0.1233).
- Effective spread (sell) = 2 × (midquote − price): 2 × (10.18 − 10.15) = 0.06; 2 × (10.165 − 10.11) = 0.11; 2 × (10.12 − 10.01) = 0.22; average 0.13.
- Interpretation: trade 1 got price improvement (above bid), trade 2 hit the bid exactly (effective = quoted), trade 3 exceeded the bid size and walked down the book (effective larger than quoted).
- Market VWAP (13,000 shares) = 131,230/13,000 = C$10.0946; fund trade VWAP (10,000 shares) = C$10.0680; VWAP cost = 10,000 × (10.0946 − 10.0680) = C$266 (⚠ Errata: the printed solution must read trade VWAP of C$10.0680 for the fund's sales only).
- IS view: the 2,000 unsold shares, still to sell at 9.50 next day, represent delay/opportunity cost the effective spread and VWAP methods never show.

**Implementation shortfall decomposition (illustrative, my numbers; the formal decomposition is a Level III topic).** Decision: buy 10,000 shares when midquote = 50.00. Order reaches the market at 50.10 (delay). 7,000 shares fill at average 50.20, commission 0.02/share; 3,000 never fill and the stock closes at 50.80.
- Delay cost = 7,000 × (50.10 − 50.00) = 700; execution (impact) cost = 7,000 × (50.20 − 50.10) = 700; opportunity cost = 3,000 × (50.80 − 50.00) = 2,400; explicit fees = 7,000 × 0.02 = 140; total = 3,940, or 78.8 bps of 500,000.
- Check against paper vs. actual: paper gain 10,000 × 0.80 = 8,000; actual gain = 7,000 × 0.60 − 140 = 4,060; shortfall = 3,940. The two reconcile. The unfilled shares account for about 61% of the cost, so VWAP or effective spread would have understated the damage badly.

## Anti-patterns
- **Reporting only VWAP to sponsors**: biased toward zero for large or participation-rate trades; supplement with arrival-price shortfall.
- **Using effective spread on a parent order sliced over hours**: later fills occur at prices already pushed by earlier child orders.
- **Ignoring unfilled orders**: a limit order that never fills shows no explicit cost yet can carry the largest opportunity cost.
- **Using a fixed-rate participation algorithm in a falling, illiquid market**: the Flash Crash showed a volume-participation algorithm accelerating as volume rose, feeding its own price impact.
- **Sending market orders in markets without price limits**: use marketable limit orders priced within a reasonable collar.
- **Regular, identifiable child-order patterns**: front-running AI detects them.
- **Allowing clients naked sponsored access**: removes broker risk controls.
- **Basing analysis on rumors or selectively presented news**: manipulation (pump-and-dump, bluffing) preys on analysts; Standard V(A) Diligence and Reasonable Basis applies.

## Exam Focus & Traps
- **Midquote benchmark sign**: for sells, cost = midquote − trade price; a fill above the midquote gives a negative cost.
- **Effective spread = 2 × cost per share**; the per-share transaction cost is half the effective spread (do not mix them up; Question 4 asks for the average effective spread: 0.04 for the BYYP-type buy example).
- **Trade price at the ask with zero price improvement**: effective spread equals quoted spread; better than ask means improvement; worse than ask means walking the book.
- **Market impact of trade 2 (practice problem)** = trade price minus prevailing ask or midquote depending on the question's definition; read the stem for the benchmark.
- **Inside spread vs. dealer spread**: inside spread (best ask minus best bid) can be smaller than every dealer's own spread.
- **Walking the book**: weighted average price of a market order across levels (for example 200 at 100.49 and 800 at 100.51 gives 100.506).
- **Fragmentation causes the need to adapt strategies** (not latency or HFT).
- **Move servers closer to the exchange** is the answer to a communication-speed priority; hiring more people or complex operating systems is wrong.
- **Machine learning works best in well-understood, repetitive environments**, poorly in new markets or volatility spikes.
- **Legality**: front running based on tips is illegal; using public data feeds and pattern detection is generally legal. Manipulation requires proving scienter.
- **Electronic trading lowered spreads and implementation shortfall** (despite parasitic traders), with bonds the least electronified.
- **Statement about bonds**: electronification has had a smaller, not greater, impact on corporate and municipal bonds than on equities.
- **Systemic-risk fixes**: testing, access controls, real-time surveillance, price limits and halts all help; no single measure suffices.

## Key Takeaways
1. Total trading cost equals explicit costs plus spread, impact, delay and opportunity costs; implicit costs need a benchmark.
2. Effective spread is for single fills, VWAP for interval comparison, implementation shortfall for the full cost of the investment decision including unfilled shares.
3. Treat a zero VWAP slippage with suspicion when your order is a large part of volume.
4. Fragmented liquidity requires aggregation and smart order routing; large orders are sliced over time and venues, randomized to avoid detection.
5. Speed matters only relative to competitors, for taking, making and canceling; low latency comes from colocation, microwave links, in-memory code and precomputed responses.
6. Electronic markets lower costs on average yet create new tail risks (runaway algorithms, fat fingers, overlarge orders, malevolent streams) addressed by testing, access control, surveillance and halts.
7. Front running, wash trading, spoofing, pump-and-dump, gunning, squeezes and corners are the abuses surveillance targets; analysts must verify information independently.
8. Algorithms must be built on models of impact, fill probability and volume, and must include limits that stop destructive feedback loops (Flash Crash lesson).

## Connects To
- **ch15**: transfer coefficient and turnover limits; trading costs are one reason realized IR is below the fundamental law's forecast.
- **ch17**: Level III implementation shortfall decomposition, algorithm selection, order types and trade strategy.
- **ch01**: market structure, order types and venues underlying limit order books.
- **ch03**: market efficiency and limits to arbitrage that parasitic and arbitrage traders exploit.
- **`cfa-equity-portfolio-management` ch04**: transaction costs and turnover in active portfolio construction.
- **`cfa-ethics-gips`**: market manipulation (Standard II(B)) and diligence and reasonable basis (Standard V(A)).
