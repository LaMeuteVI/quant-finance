# Chapter 1: Market Organization and Structure
> **Source**: CFA Program Curriculum 2020, Level I, Reading 36 · Portfolio Management (Equity/Markets) | Larry Harris, PhD, CFA

## Core Idea
The financial system moves money, assets and risk across time, place and entities, and discovers the equilibrium rate of return that clears savings against borrowing. An analyst must know *what* trades (securities, currencies, contracts, commodities, real assets), *who* intermediates, *how* positions are taken and leveraged, *how* orders are instructed and executed, and *what makes a market well-functioning*. Execution cost, leverage and margin arithmetic are where this chapter bites in practice.

## Learning Outcomes Covered
- explain the main functions of the financial system
- describe classifications of assets and markets
- describe major securities, currencies, contracts, commodities, real assets and their subtypes
- describe financial intermediaries and their services
- compare long, short and leveraged positions
- calculate the leverage ratio, the return on a margin transaction, and the margin-call price
- compare execution, validity and clearing instructions; market vs limit orders
- define primary and secondary markets and how secondary markets support primary markets
- describe quote-driven, order-driven and brokered markets
- describe characteristics of a well-functioning financial system and the objectives of regulation

## Frameworks Introduced
- **Six purposes of the financial system**: save, borrow, raise equity capital, manage risk, exchange assets for immediate delivery (spot), and trade on information.
  - When to use: to diagnose *why* a counterparty trades (motive, not holding period or risk, separates an investor from an information-motivated trader).
  - How: classify the trade by motive. Investors expect only a fair (unconditional) return. Information-motivated traders (active managers) expect a conditional return above the fair return.
- **Three functions of the financial system**: (1) enable the six purposes, (2) discover the rate of return that equates aggregate savings and borrowing (the equilibrium interest rate), (3) allocate capital to its best uses (allocational efficiency).
  - Why it works: every required return = common equilibrium rate + adjustments for risk, term and liquidity (equity > debt, long > short, illiquid > liquid).
- **Asset and market classification tree**:
  - Financial assets = securities, currencies, contracts. Physical assets = commodities and real assets.
  - Securities: debt, equity, pooled vehicles; public vs private. Markets: spot vs forward/futures/options; primary vs secondary; money (<= 1 year) vs capital; traditional vs alternative.
- **Leveraged-position framework (margin)**:
  - When to use: any purchase on margin (or short sale) where return on equity, leverage ratio or call price is needed.
  - How: (1) equity = price x shares / leverage ratio, loan = remainder; (2) net P&L = price change + dividends − interest − commissions; (3) return = P&L / initial equity (include the purchase commission in the initial investment); (4) margin-call price from the maintenance requirement.
- **Order instruction taxonomy**: execution (market, limit, all-or-none, hidden, iceberg/display size), validity (day, GTC, IOC/fill-or-kill, good-on-close/open, stop), clearing (who settles; long vs short sale flag).
- **Order precedence hierarchy** (order-driven markets): (1) price priority, (2) display precedence at a price, (3) time precedence.
- **Three trade-pricing rules**: uniform (call markets, single price maximizing volume), discriminatory (continuous markets, standing order's limit price), derivative (crossing networks, midpoint of another market's quote).
- **Complete vs operationally vs informationally efficient markets**: complete = needed instruments exist; operationally efficient = low trading costs; informationally efficient = prices reflect all available fundamental information.

## Key Concepts
- **Equilibrium interest rate**: the price of moving money through time, at which aggregate savings supply equals aggregate borrowing plus equity-issuance demand.
- **Allocational efficiency**: capital goes to the most productive projects; needs accurate information and low-cost trading.
- **Information-motivated trader**: trades to earn a return on information beyond the fair return for bearing risk (active manager).
- **Broker vs dealer**: a broker is an agent who does not trade against the client; a dealer trades against the client and supplies liquidity through time. A broker-dealer has a conflict of interest on how orders are filled.
- **Arbitrageur**: connects buyers and sellers who arrive at the same time in different markets (or in related instruments), moving liquidity across markets; dealers move liquidity through time.
- **Alternative trading system (ATS / ECN / MTF)**: exchange-like venue with no regulatory authority over subscribers; a dark pool does not display orders.
- **Securitization**: pooling assets in a special purpose vehicle (SPV/SPE) and selling claims (often tranches, senior first, junior as "toxic waste") to investors, which improves liquidity and diversification.
- **Clearinghouse**: guarantees or escrows settlement; in futures it is the buyer to every seller and seller to every buyer, funded by initial and variation margin.
- **Forward vs futures**: a forward is a customised bilateral OTC contract with counterparty and liquidity problems; a futures contract is standardised and clearinghouse-guaranteed, with daily mark-to-market.
- **Long / short exposure**: a long put holder is long the option but short the underlying (Exhibit 1: long call = long, short call = short, long put = short, short put = long).
- **Short rebate rate**: interest rebated to a short seller on the collateral proceeds; negative or tiny when a stock is "on special" (hard to borrow).
- **Payment in lieu**: dividend or interest the short seller must pay the securities lender.
- **Margin terms**: call money rate (margin-loan rate), initial margin requirement (e.g., Regulation T), maintenance margin requirement (often 25%), margin call.
- **Bid-ask spread / making vs taking a market**: standing limit orders make the market; market and marketable limit orders take it.
- **Quote-driven / order-driven / brokered markets**: customers trade with dealers / a matching engine ranks orders by rules / brokers find counterparties for unique assets.
- **Pre-trade and post-trade transparency**: publication of quotes and orders vs publication of prices and sizes after execution. Dealers prefer opacity, buy-side prefers transparency.
- **Underwritten vs best-effort offering; shelf registration; rights offering**: bank guarantees the sale vs acts as broker only; securities registered once and sold piecemeal into the secondary market; existing holders receive options to buy at a discount.

## Formulas & Reference Tables
- `Leverage ratio = Position value / Equity = 1 / Initial margin requirement` (40% margin gives 2.5x)
- `Approx. equity return = Leverage ratio × Asset return` (ignores interest, dividends, commissions)
- `Initial investment = Equity + Purchase commissions`, `Equity = (Price₀ × Shares) / Leverage`, `Loan = Price₀ × Shares − Equity`
- `Return on margin trade = [ (P₁ − P₀)×N + D×N − Loan×call rate − Commissions ] / Initial equity investment`
- `Margin-call price (long) P* = P₀ × (1 − Initial margin) / (1 − Maintenance margin)`. Derived from `(E₀/share + P − P₀)/P = m`.
- `Margin-call price (short) P* = P₀ × (1 + Initial margin) / (1 + Maintenance margin)`. Derived from `(1+e)P₀ − P = m·P` (equity includes the short-sale proceeds plus posted margin).
- `Dealer/market spread = best offer − best bid` (the market spread is never wider than any single dealer's spread).
- `Placement cost % = (Gross proceeds − Net proceeds) / Net proceeds` in the reading's convention.
- `Average fill price = Σ(price × size) / Σ size` (discriminatory pricing, walking the book).

| Instruction | Fills when | Price risk | Execution risk |
|---|---|---|---|
| Market order | immediately | high, especially large or thin | low |
| Limit order | at limit or better | capped at limit | may not fill (regret when price runs away) |
| Stop (sell) | after a trade at or below the stop, then becomes market (or limit if stated) | stop-market can fill far below the stop | stop-limit may never fill |
| IOC / FOK | on receipt only | per limit | cancel if not filled |
| Good-on-close | at the close | closing price | - |

| Market structure | Liquidity provider | Typical instruments |
|---|---|---|
| Quote-driven (dealer, OTC) | dealers | most bonds, currencies, spot commodities |
| Order-driven | other traders' orders | exchanges, ECNs, automated systems |
| Brokered | broker networks | blocks, real estate, art, IP, taxi medallions |

| Pricing rule | Where | Price |
|---|---|---|
| Uniform | call markets, opening/closing auctions | single price maximizing volume |
| Discriminatory | continuous order-driven | each standing order's limit price |
| Derivative | crossing networks | midpoint of the primary market quote |

## Mental Models
- **Dealers move liquidity through time, arbitrageurs move it across markets, brokers/exchanges match buyers and sellers present at the same place and time.**
- **A limit order is a price protection, a market order is a time protection.** Choose by the decay rate of your information: perishable information means market (or marketable limit) orders, but cap cost with limits if transaction costs can exceed the expected alpha.
- **Stop orders are not insurance.** Only an option (a put struck at the floor) guarantees the exit price. Stop-sell orders add to downward momentum.
- **Leverage is a multiplier on equity returns, and interest is a fixed drag.** Expect about `L × r` minus a financing cost; losses exceed the multiplier-implied loss.
- **Banks, insurers and brokers are tranches.** Depositors senior, equity junior: thin capital means weak incentives to lend carefully, which is why regulators set capital minimums.
- **Better prices require information plus cheap trading.** If trading costs are high, informed traders stay out, and prices become less informative.

## Worked Example
**Leveraged stock purchase (recomputed).** Buy 1,000 shares at $20, leverage 2.5, call money rate 5%, sell at $15 after one year, dividend $0.10/share, commission $0.01/share each way.
1. Position = $20,000; equity = 20,000 / 2.5 = $8,000; loan = $12,000; purchase commission $10, so initial investment = $8,010.
2. Sale proceeds $15,000 − loan $12,000 − interest $600 + dividend $100 − sale commission $10 = $2,490 remaining.
3. Return = (2,490 − 8,010) / 8,010 = **−68.9%**.
4. Interpretation: the naive check 2.5 × (−25%) = −62.5%; the extra −6.4 points come from interest and commissions net of the dividend.

**Margin-call price.** Buy at $20 with 40% equity; maintenance 25%: P* = 20 × 0.60 / 0.75 = **$16.00**. A short at $50 with 50% initial and 30% maintenance: P* = 50 × 1.5 / 1.3 = **$57.69** (price rising hurts the short).

**Walking the book.** Bids 100.1 (15), 100.2 (8), 100.3 (10); offers 100.4 (4), 100.5 (6), 100.6 (12). Buy 15 limit 100.5: fills 4 at 100.4 and 6 at 100.5, average 100.46; the remaining 5 rest on the book at 100.5 if it is a day order, and cancel if IOC.

## Anti-patterns
- **Using market orders for large size in thin stocks**: price concessions can exceed expected alpha.
- **Treating a stop-loss as a guaranteed exit**: a stop-sell becomes a market order that can fill far below the stop in a fast market.
- **Ignoring financing costs when quoting leveraged returns**: the L × return shortcut overstates results.
- **Believing a limit order trades at its limit price**: it is an instruction to get the best price available, never worse than the limit.
- **Confusing the direction of the stop price with the limit price**: a stop conditions *when* the order becomes live; a limit caps *what price* is acceptable.
- **Using a broker-dealer discretionary order without specifying how it is filled**: the dealer leg profits from worse prices for you.
- **Treating "public prominence" as "public security"**: only properly registered securities are public.

## Exam Focus & Traps
- **Margin return**: denominator is the *equity* (plus purchase commission), not the position value. Interest is on the loan only.
- **Margin call**: always solve equity/price = maintenance margin. Long: P* = P₀(1−e)/(1−m). Short formula has plus signs.
- **Long put = short exposure** to the underlying; short put = long exposure. Options: the *holder* is long, the *writer* is short.
- **Broker vs dealer**; **dealer vs arbitrageur**: same instrument at different times (dealer) vs same time in different markets (arbitrageur).
- **Stop vs limit**: a stop-buy triggers when the price rises to the stop; a stop-sell triggers when it falls to the stop.
- **Order-driven priority**: price, then display, then time.
- **Pricing rule by venue**: call = uniform, continuous = discriminatory, crossing = derivative.
- **ETFs**: authorised participants keep the price near NAV via in-kind creation/redemption; closed-end funds can trade at large discounts or premiums and are secondary-market only.
- **Futures margin** (CFA example): initial $77,630, loss $30,000 leaves $47,630 < maintenance $57,500, so the variation margin call restores the account to *initial* margin, $30,000.
- **Rights offerings** are options (short-term warrants); an IPO "underpricing" stems from the underwriter's incentive conflict.
- **Complete markets** = instruments exist; **operationally efficient** = low cost; **informationally efficient** = prices reflect information.

## Key Takeaways
1. Identify trade motive first: saving, borrowing, equity raising, hedging, spot exchange, or information trading.
2. Required return = common equilibrium rate + premiums for risk, term and illiquidity.
3. For margin problems, compute equity, loan, net P&L, then divide by the initial investment including commissions.
4. Margin-call price: P₀(1−e)/(1−m) for longs, P₀(1+e)/(1+m) for shorts.
5. Choose order type by the decay of your information and the impact cost of your size; hide or iceberg large orders.
6. Futures beat forwards on counterparty risk and liquidity because of the clearinghouse and standardisation.
7. Liquid secondary markets lower primary-market financing costs.
8. Regulation addresses fraud, agency problems, fairness, standards, capital adequacy and long-term liability funding.

## Connects To
- **ch02**: indexes summarise the markets described here (price-, equal-, value-weighted construction).
- **ch03**: operational efficiency and informed trading are the preconditions for informationally efficient prices.
- **`cfa-level1-curriculum` ch08-10**: personal revision notes on the same reading family (markets, indexes, efficiency).
- **`cfa-equity-portfolio-management` ch02**: passive investing uses ETFs, creation/redemption and index replication.
