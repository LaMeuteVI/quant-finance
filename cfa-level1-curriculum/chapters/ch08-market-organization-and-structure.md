# Chapter 8: Market Organization and Structure (Equity)

## Core Idea
The financial system moves money through time and across risks. It lets people save, borrow, raise equity, manage risk, trade spot and trade on information, and it sets equilibrium returns and allocates capital to its best uses. Intermediaries, order types and market structures are how that happens. A well-functioning system is complete, operationally efficient and informationally efficient.

## Frameworks Introduced
- **Three functions of the system**:
  1. Channel savings to investment.
  2. Determine equilibrium rates of return.
  3. Allocate capital efficiently.
- **Six uses by participants**: save, borrow, raise equity, manage risk, exchange assets (spot), trade on information (active management).
- **Asset classes**:
  - Financial: securities (fixed income, equity, pooled vehicles), currencies, contracts.
  - Physical: commodities, real assets.
  - Fixed income is short term (< 1y, money market), intermediate (1–5y) or long term (> 5y, capital market).
- **Pooled vehicles**:
  - **Open-end** funds redeem shares at NAV. **Closed-end** funds trade on the secondary market.
  - **ETFs/ETNs** use authorized participants and in-kind creation/redemption.
  - **Hedge funds**: limited partnerships with incentive fees and leverage.
- **Contracts**: forwards (counterparty and liquidity risk), futures (clearinghouse, margin, daily settlement), swaps, options (premium), insurance.
- **Intermediaries**: brokers (agents), block brokers, investment banks, exchanges, alternative trading systems / dark pools, dealers (principals), securitizers (SPVs, tranches), depository institutions, prime brokers, insurers, arbitrageurs, clearinghouses and custodians.
- **Positions and exposure**:

| Position | Contract side | Exposure to the underlying |
|---|---|---|
| Long call | Long | Long |
| Short call | Short | Short |
| Long put | Long | Short |
| Short put | Short | Long |

- **Short selling**: borrow the security, sell it, buy it back later and return it. Losses are unbounded. The short seller pays the lender any dividends.
- **Margin (leveraged) positions**:
  - Leverage ratio = position value / equity = 1 / initial margin.
  - Initial margin is ≥ 50% for US stocks; maintenance margin is 25% (FINRA).
  - Margin-call price for a long position: `P₀ × (1 − IM)/(1 − MM)`.
- **Order instructions**:
  - **Execution**: market, limit, marketable limit, all-or-nothing, hidden, iceberg/display size.
  - **Validity**: day, GTC, IOC/fill-or-kill, good-on-close/open, **stop** (stop-loss sell below the stop price; stop-buy above it).
  - **Clearing**: who settles (give-up to a prime broker).
- **Primary markets**:
  - **Underwritten** offering: the bank guarantees the sale. **Best-efforts**: the bank acts only as agent.
  - **Book building**; accelerated book build.
  - Private placements, shelf registration, dividend reinvestment plans (DRPs), government auctions.
  - IPOs are typically **underpriced**, so prices often rise on day one.
- **Secondary markets**:
  - **Call markets** (batch auctions, liquid only at the call) vs **continuous** markets.
  - **Quote-driven (dealer/OTC)**: most bonds, FX and spot commodities.
  - **Order-driven**: matching rules by price priority, then display, then time. Pricing rules: uniform (call markets), discriminatory, derivative.
  - **Brokered markets**: unique, illiquid assets.
- **Well-functioning system**: complete markets, operational efficiency (low costs), informational efficiency (prices reflect fundamentals), plus regulation against fraud and agency problems and for fairness and capital adequacy.

## Key Concepts
- **Allocational efficiency**: capital flows to its most productive uses.
- **Call money rate**: the interest rate on margin loans.
- **Primary dealers**: dealers that central banks trade with.
- **Dark pool**: an ATS that does not display orders.
- **Toxic waste**: the most junior securitization tranche.

## Mental Models
- **Brokers match; dealers take the other side.** Know who is your counterparty.
- **Leverage = 1/margin**: 50% margin means 2× leverage, so a 10% price fall costs 20% of equity.
- **Order type = a trade-off between price certainty and execution certainty.**

## Anti-patterns
- ⚠ **Correction vs the notes**: the notes say "fixed-income investments represent ownership rights". It is **equities** that represent ownership. Fixed income is a contractual claim.
- **Using market orders in illiquid names**: execution risk and price impact.
- **Ignoring the margin-call price on leveraged longs**.

## Worked Example
**Margin purchase.** Buy 1,000 shares at $40 with 50% initial margin and 25% maintenance margin. Call money rate is ignored.
- Equity = $20,000; loan = $20,000. Leverage = 2×.
- Margin-call price = 40 × (1 − 0.5)/(1 − 0.25) = **$26.67**.
- If the price rises to $50: return on equity = (50,000 − 20,000 − 20,000)/20,000 = **+50%**, versus +25% unlevered.

## Key Takeaways
1. The system saves, lends, raises equity, transfers risk, trades and prices capital.
2. Brokers act as agents. Dealers act as principals. Exchanges and ATSs match orders.
3. A long put and a short call are both short exposure to the underlying.
4. Leverage = 1/IM. Margin-call price = P₀(1 − IM)/(1 − MM).
5. Know the order types (execution, validity, clearing) and the market structures (quote-, order-, broker-driven).

## Connects To
- **Ch 9**: indexes as benchmarks.
- **Ch 10**: informational efficiency.
- **Ch 12**: equity securities.
- **Ch 20**: derivatives.
- **Hull Ch 2 / Ch 10** (`hull-derivatives`): futures margin, options markets.
