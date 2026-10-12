# Chapter 20: Derivative Markets and Instruments (Derivatives)

## Core Idea
A derivative derives its performance from an underlying. There are two families:
- **Forward commitments** (forwards, futures, swaps) *oblige* both parties to transact.
- **Contingent claims** (options, credit derivatives, ABS) give a *right* to one party.

Derivatives trade on exchanges (standardized, cleared) or OTC (customized, dealer-based). They are used to transfer risk, discover prices, lower transaction costs, go short easily and improve market efficiency.

> Source note: the companion reading "Basics of Derivative Pricing and Valuation" in this repo is an **empty LaTeX draft** (title and learning-outcome table only). For pricing and valuation, use the `hull-derivatives` skill: ch05 (forward pricing), ch07 (swaps), ch11 (parity), ch13 (binomial), ch15 (BSM).

## Frameworks Introduced
- **Parties**: the buyer is the **long** (holder); the seller is the **short** (writer).
- **Exchange-traded vs OTC**:

| Feature | Exchange-traded | OTC |
|---|---|---|
| Terms | Standardized | Customized |
| Counterparty risk | Clearinghouse guarantee | Dealer (mitigated by collateral / central clearing post-2008) |
| Liquidity | High | Varies |
| Transparency / regulation | High | Lower (much stricter since Dodd-Frank / EMIR) |
| Settlement | Daily mark-to-market | Per contract |
| Dealer role | Market makers, scalpers | Dealers hedge (lay off) risk with offsetting trades |

- **Forward commitments**:
  - **Forward**: OTC, fixed price for a future transaction. Can be cash-settled (**NDF / contract for differences**).
  - **Futures**: exchange-traded, standardized, **daily settlement** (mark-to-market), clearinghouse guarantee, **price limits**. The futures price **converges to spot at expiration**, otherwise arbitrage is possible.
  - **Swap**: a series of exchanged cash flows (plain vanilla: fixed vs floating). Value is zero at inception. Only net payments are exchanged.
- **Contingent claims**:
  - **Options**: call (right to buy) / put (right to sell). American (any time) vs European (at expiration) — the names refer to exercise style, not geography.
    - Moneyness for a call: ITM if S > X, ATM if S = X, OTM if S < X. The reverse holds for a put.
    - Call holder: loss limited to the premium, unlimited upside.
    - Put holder: loss limited to the premium; the gain is capped at X − premium, because S ≥ 0.
  - **Credit derivatives** (protection buyer vs protection seller):
    - **Total return swap**: the buyer pays the bond's total return and receives floating; the seller bears the credit loss.
    - **Credit spread option**: a call on the credit spread.
    - **CDS**: periodic premiums in exchange for a payment after a credit event. Economically, insurance.
    - **Credit-linked note**.
  - **Asset-backed securities**: tranched claims on a pool (the curriculum treats them as a form of derivative).
- **Hybrids**: callable and convertible bonds, swaptions, futures options, etc.
- **Purposes and benefits**:
  1. **Risk allocation, transfer and management**: change exposure without selling the asset (e.g., keep votes and dividends).
  2. **Price and information discovery**: futures lead spot prices (index futures trade before the equity open), and implied volatility gives a forward-looking view of risk.
  3. **Operational advantages**: low capital needed (leverage), low transaction costs, **easy shorting**.
  4. **Market efficiency**: arbitrage aligns prices.
- **Criticisms**: too speculative or gambling-like, too complex, sources of systemic risk (leverage, interconnectedness).
- **Carry properties of the underlying**: storage costs (bananas ≠ gold ≠ oil), income (dividends, coupons), convenience. The **net cost of carry** drives forward pricing.

## Key Concepts
- **Clearing** (verify and record the trade) vs **settlement** (transfer of money).
- **Open interest**: number of contracts outstanding.
- **Arbitrage**: identical cash flows must have identical prices. This is the **law of one price** and the foundation of derivative pricing.
- **Notional principal**: the base for swap payments. It is not exchanged.

## Mental Models
- **Forward commitment = obligation, symmetric payoff. Contingent claim = right, asymmetric payoff, paid for with a premium.**
- **A derivative price is set by replication**, not by expectations of the underlying.
- **Credit derivatives separate credit risk from funding.**

## Anti-patterns
- ⚠ **Update vs the notes**: OTC derivatives are no longer "basically unregulated". Post-2008 reforms mandate central clearing, margin, trade reporting and platform trading for standardized OTC derivatives.
- **Confusing the contract side with the exposure**: a long put is *short* the underlying.
- **Ignoring counterparty risk** in uncollateralized OTC trades.

## Worked Example
**Option payoffs at expiration.** X = 50, premium = 3.

| S_T | Long call payoff / profit | Long put payoff / profit |
|---|---|---|
| 40 | 0 / −3 | 10 / +7 |
| 50 | 0 / −3 | 0 / −3 |
| 60 | 10 / +7 | 0 / −3 |

- Call break-even at 53; put break-even at 47.
- Maximum put gain = 50 − 3 = 47 (if S_T = 0).

**Forward vs futures on the same asset.** Both lock the price at F₀. Futures realize the P&L daily (margin flows); forwards settle at maturity. The total P&L is the same when interest rates are deterministic.

## Key Takeaways
1. Forward commitments (forwards, futures, swaps) are obligations. Contingent claims (options, CDS, ABS) are rights.
2. Exchange trading: standardized and cleared, with daily settlement. OTC: customized, dealer-based, now increasingly cleared.
3. Futures converge to spot at expiration. Swaps start with zero value.
4. Credit derivatives: TRS, spread options, CDS, CLNs.
5. Benefits: risk transfer, price discovery, low costs, easy shorting, efficiency. Pricing rests on no-arbitrage.

## Connects To
- **Ch 8**: market structure, clearinghouses.
- **Ch 17**: ABS.
- **Ch 19**: credit risk.
- **`hull-derivatives` skill**: ch01–02 (markets), ch05 (forward pricing), ch07 (swaps), ch10–13 (options), ch25 (credit derivatives).
