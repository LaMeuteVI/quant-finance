# Chapter 2: Futures Markets and Central Counterparties

## Core Idea
Futures differ from forwards through standardization, daily settlement (margining) and a clearing house that removes counterparty risk. Few contracts reach delivery, but the *possibility* of delivery is what anchors the futures price to spot at maturity.

## Frameworks Introduced
- **Contract specification**: what asset (grade), contract size, delivery arrangements (where), delivery months (when), price quotes, daily price limits, position limits.
  - When to use: before trading or hedging, check that the spec (grade, location, month) actually matches your exposure. A mismatch creates basis risk (Ch 3).
- **Margin mechanics (daily settlement)**:
  - Initial margin is posted. Gains and losses are credited or debited daily (marking to market).
  - If the balance falls below the **maintenance margin**, a **margin call** restores it to the *initial* margin level with **variation margin**.
  - Excess over initial can be withdrawn.
- **Clearing chain**: trader → broker → clearing member → exchange clearing house. Each layer margins the layer below.
- **OTC clearing (post-2008)**:
  - **Bilateral**: governed by an ISDA Master Agreement + Credit Support Annex (CSA). Collateral is posted.
  - **Central (CCP)**: the CCP novates the trade and becomes buyer to every seller and seller to every buyer. Members post initial and variation margin plus default fund contributions.
- **Convergence**: as the delivery period approaches, the futures price converges to spot. Otherwise a riskless buy-cheap/deliver trade exists.

## Key Concepts
- **Open interest**: total number of contracts outstanding. **Trading volume**: contracts traded in a day.
- **Settlement price**: the price just before the close, used for daily margining.
- **Limit up / limit down**: daily price movement limits. Trading halts at the limit.
- **Normal market / Inverted market**: futures prices increase / decrease with maturity.
- **Delivery options**: the *short* chooses when, where (and sometimes which grade) to deliver. The futures price reflects this choice.
- **Cash settlement**: used when delivery is impractical (stock indices).
- **Order types**: market, limit, stop (stop-loss), stop-limit, market-if-touched, discretionary, time-of-day, open, fill-or-kill.
- **Novation**: the CCP replaces the original bilateral contract with two contracts facing itself.

## Mental Models
- Think of a **futures contract as a forward that is re-struck every day**. Yesterday's gain or loss is paid in cash today, so credit exposure never accumulates.
- Use **futures when liquidity/credit matter most** and **forwards when you need an exact date, size or underlying**.
- **Margin is liquidity risk**: a perfectly hedged position can still need cash today (see Metallgesellschaft, Ch 3).

## Anti-patterns
- **Forgetting to close out before delivery**: a speculator can end up having to take physical delivery (Business Snapshot 2.1 — a bank's unanticipated delivery of live cattle).
- **Ignoring funding liquidity**: LTCM's arbitrage was right in the long term but insolvent in the short term because of collateral calls. Leverage + illiquidity → forced unwinding.

## Reference Tables
| Feature | Forward | Futures |
|---|---|---|
| Market | Private (OTC) | Exchange |
| Terms | Customized | Standardized |
| Delivery date | Usually one | Range of dates |
| Settlement | At end of life | Daily |
| Delivery | Usually occurs | Usually closed out before |
| Credit risk | Bilateral (mitigated by CSA) | Virtually none (clearing house) |

## Worked Example
An investor buys 2 gold futures (100 oz each) at $1,750/oz. Initial margin is $6,000 per contract ($12,000 total). Maintenance margin is $4,500 per contract ($9,000).
- On day 1 the price falls to $1,741 → loss 9 × 200 = $1,800, balance $10,200.
- A cumulative loss above $3,000 (price < $1,735) triggers a margin call back to $12,000.
- The daily cash flows sum to (F_close − F_open) × size. This is the same total P&L as a forward, only paid earlier.

## Key Takeaways
1. Daily settlement makes futures credit-safe but creates funding (liquidity) risk.
2. Delivery options belong to the short. They slightly lower the futures price.
3. Convergence to spot at delivery is an arbitrage result, not an assumption.
4. OTC markets now resemble futures markets: CCPs, mandatory margin, trade reporting.
5. Most futures are closed out before delivery. Hedgers use them for price exposure, not for physical supply.

## Connects To
- **Ch 3**: hedging with futures and basis risk.
- **Ch 5**: forward vs futures prices (equal when rates are constant).
- **Ch 9**: collateral, CSAs and XVAs.
- **Ch 24**: credit risk mitigation (netting, collateral).
