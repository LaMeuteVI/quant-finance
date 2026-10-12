# Chapter 1: Derivative Markets and Instruments
> **Source**: CFA Program Curriculum 2020, Level I, Reading 48 · Derivatives | Don M. Chance, PhD, CFA

## Core Idea
A derivative is a contract that **transforms** the performance of an underlying: it pays off on a source of risk without requiring you to own that risk source. Two families exist. **Forward commitments** (forwards, futures, swaps) oblige both sides and have linear payoffs and zero value at inception. **Contingent claims** (options, credit derivatives, and implicitly ABS tranches) give one side a right, cost a premium up front and have non-linear payoffs. Prices are set by **no-arbitrage**, a relative-valuation principle that ties the derivative to its underlying plus the risk-free rate, and never by forecasting the underlying.

## Learning Outcomes Covered
- Define a derivative; distinguish exchange-traded vs OTC derivatives.
- Contrast forward commitments with contingent claims.
- Define forwards, futures, options (calls/puts), swaps and credit derivatives, and compare their characteristics.
- Compute value at expiration and profit for long/short calls and puts.
- Describe the purposes of derivative markets and the controversies around them.
- Explain arbitrage and its role in pricing and market efficiency.

## Frameworks Introduced
- **Two-class taxonomy of derivatives**:
  - *Forward commitments* bind both parties to transact at a future date on terms fixed today: **forward contract**, **futures contract**, **swap**. Payoff is linear in the underlying. No money changes hands at initiation, so the value at t = 0 is zero.
  - *Contingent claims* give the holder a **right but not an obligation**, which depends on a random outcome: **options**, **credit derivatives** (CDS, credit spread options, CLNs, TRS) and **asset-backed securities**, which behave like short puts. Payoff is non-linear. The long pays a premium, so the value at t = 0 is positive.
  - **Hybrids** combine the building blocks: callable and convertible bonds, capped/floored swaps, options on futures, swaptions.
  - When to use: classify any instrument by asking two questions. Is there an obligation on both sides? Is there an up-front premium?
- **Exchange-traded vs OTC trade-off matrix** (see table below):
  - Standardization buys liquidity, clearing and a credit guarantee, at the cost of flexibility and privacy.
  - Customization buys an exact hedge, at the cost of counterparty risk and lighter oversight (increasingly reduced by Dodd–Frank and EMIR-type central-clearing and reporting mandates).
  - Failure mode: assuming OTC means illiquid. An OTC position can often be offset with the original dealer, while some listed contracts have almost no open interest. Liquidity follows trading interest, not venue.
- **Futures mark-to-market and margin mechanics**:
  1. Both parties post **initial margin**, a performance bond and not a down payment. No loan is created, unlike equity margin. It is typically < 10% of the contract value.
  2. Each day the clearinghouse sets a **settlement price** (an average of the final trades) and credits the gains of one side from the losses of the other.
  3. If the balance falls below the **maintenance margin**, a **margin call** requires a deposit back up to the **initial** margin, not merely up to maintenance.
  4. Failure to meet the call leads to forced close-out, and the defaulter remains liable for further losses. The clearinghouse backstops losses through its guarantee fund.
  5. **Price limits** (limit up / limit down / locked limit) cap daily moves to protect the clearinghouse's credit exposure.
  6. Summed variation-margin flows = fT(T) − f₀(T) = S_T − f₀(T), because the futures price **converges** to spot at expiration. The total P&L is therefore the same as a forward's, but it is received daily, not at T.
- **Hedge-portfolio (no-arbitrage) pricing principle**:
  - Combine the derivative with the underlying so that risk is eliminated. The riskless combination must then earn the risk-free rate.
  - The derivative's price is the unique price that makes this true.
  - Consequence: you never discount a derivative's expected payoff at a risky rate. The risk premium is already embedded in the spot price, so doing so would double count.
  - The principle requires **storability** of the underlying (the ability to hold it), which is the mirror image of the ability to **short** it. Markets on non-storable underlyings (electricity, weather, fresh fish) are harder to price and have been less successful.
- **Arbitrage and the law of one price**:
  - Two assets, or combinations of assets, with identical future payoffs must have the same price today.
  - A true arbitrage requires **zero risk AND zero capital**: selling the overpriced side funds the purchase of the underpriced side.
  - Arbitrage is **relative**, not absolute, valuation. It tells you the price of one asset given another, never the fundamental value of either.

## Key Concepts
- **Underlying**: the source of risk the derivative pays on. It can be an asset (stock, bond, currency, commodity) or a non-asset (interest rate, credit, weather, electricity, insurance claims).
- **Long / holder / buyer vs short / writer / seller**: the long benefits when the value of what it owns rises. The short has an obligation to deliver.
- **Forward contract**: an OTC agreement for the buyer to purchase the underlying from the seller at a later date at a fixed price F₀(T) agreed at signing.
- **Non-deliverable forward (NDF) / cash-settled forward / contract for differences**: settles with a payment of S_T − F₀(T) instead of delivery. The economic effect is identical, since the long can buy spot at S_T and effectively pays F₀(T).
- **Futures contract**: a standardized, exchange-traded forward with daily settlement of gains and losses and a clearinghouse credit guarantee.
- **Offset**: closing a futures position by taking the opposite trade before expiration.
- **Open interest**: the number of contracts outstanding (each has one long and one short).
- **Swap**: an OTC exchange of a series of cash flows, one floating and the other fixed or floating on a different underlying. It behaves like a **series of forwards**. The most common is the **plain vanilla** fixed-for-floating interest rate swap.
- **Notional principal**: the amount on which swap payments are computed. It is not exchanged in an interest rate swap, but it may be exchanged in a currency swap.
- **Basis swap**: floating vs floating, e.g. Libor vs T-bill (their spread is the **TED spread**). **Overnight indexed swap (OIS)**: floating leg tied to an overnight rate (Fed funds type).
- **Option**: the buyer pays a **premium** for the right to buy (**call**) or sell (**put**) at the **exercise (strike) price** X. **European** options can be exercised only at expiration and **American** options at any time up to it. The style names have nothing to do with geography.
- **Moneyness**: a call is in the money when S > X and out of the money when S < X. A put is the reverse. At the money (S = X) has zero exercise value.
- **Credit derivative**: a contract in which a protection seller compensates a protection buyer for a specified credit loss on a third party.
- **Total return swap**: the protection buyer pays the total return on a bond or loan and receives a fixed or floating rate.
- **Credit spread option**: a call on a bond's yield spread over a default-free benchmark.
- **Credit-linked note (CLN)**: a note whose principal is reduced if a reference obligation defaults. The note buyer is the protection seller.
- **Credit default swap (CDS)**: periodic premium payments in exchange for compensation after a credit event (bankruptcy, failure to pay, involuntary restructuring). The payout is usually set by auction.
- **Asset-backed security (ABS)**: a pool of debt carved into **tranches** with prioritized claims. Prepayments and defaults hit the most junior tranches first.
  - A **CMO** is backed by mortgages, with prepayment risk borne by Class C, then B, then A.
  - A **CDO** (CBO/CLO) is backed by bonds or loans, with credit risk borne by the equity (junior) tranche, then mezzanine, then senior.
- **Price discovery / information discovery**: futures prices reveal the price at which uncertainty can be eliminated. Option prices reveal **implied volatility** (the VIX, a "fear gauge" for the S&P 500).

## Formulas & Reference Tables
**Payoffs and profits at expiration** (S_T = underlying price at T, X = strike, c₀/p₀ = premiums paid at t = 0, Π = profit):

| Position | Value at expiration (payoff) | Profit Π | Max gain | Max loss | Breakeven |
|---|---|---|---|---|---|
| Long forward | `S_T − F₀(T)` | same (no premium) | unlimited | F₀(T) | S_T = F₀(T) |
| Short forward | `−[S_T − F₀(T)]` | same | F₀(T) | unlimited | S_T = F₀(T) |
| Long call | `c_T = max(0, S_T − X)` | `max(0, S_T − X) − c₀` | unlimited | c₀ | X + c₀ |
| Short call | `−max(0, S_T − X)` | `−max(0, S_T − X) + c₀` | c₀ | unlimited | X + c₀ |
| Long put | `p_T = max(0, X − S_T)` | `max(0, X − S_T) − p₀` | X − p₀ | p₀ | X − p₀ |
| Short put | `−max(0, X − S_T)` | `−max(0, X − S_T) + p₀` | p₀ | X − p₀ | X − p₀ |

**Futures daily settlement**: the day-t cash flow to the long is `f_t(T) − f_{t−1}(T)`. Summed over the life of the contract, `Σ = f_T(T) − f₀(T) = S_T − f₀(T)` (convergence).

**Margin call rule**: if `Balance < Maintenance margin`, the deposit required is `Initial margin − Balance`.

**First pricing model (cost of carry, no income)**: `F₀(T) = S₀ × (1 + r)^T`. Any other forward price creates arbitrage (see Worked Example 3).

**Exchange-traded vs OTC**

| Feature | Exchange-traded (futures, listed options) | OTC (forwards, swaps, OTC options, CDS) |
|---|---|---|
| Terms | Standardized by the exchange (size, expiry, underlying) | Customized by the parties |
| Credit risk | Clearinghouse guarantee, margin, daily MTM | Counterparty default risk (only the net debtor can default) |
| Liquidity providers | Market makers (scalping) and speculators | Dealers (mostly ISDA member banks) who hedge with similar but not identical trades |
| Transparency | Full reporting to exchange and regulators | Private, lower transparency (reporting is increasing post-2010) |
| Regulation | Heavy, national level | Lighter; Dodd–Frank / EU rules push central clearing and reporting |
| Settlement | Overnight clearing | Bilateral |

**Forward vs futures vs swap vs option**

| | Forward | Futures | Swap | Option |
|---|---|---|---|---|
| Venue | OTC | Exchange | OTC | Both |
| Obligation | Both | Both | Both | Short only |
| Initial value | 0 | 0 (reset daily) | 0 | Premium > 0 |
| Who can default | Either (net debtor) | Clearinghouse-guaranteed | Either (net debtor) | Short only (OTC) |
| Cash flows | One, at T | Daily | Series | Premium at 0, payoff at exercise |
| Payoff shape | Linear | Linear | Linear | Non-linear (kinked at X) |

**Market-size measures**:
- Exchange market: volume (number of contracts, which mixes unequal contract sizes) and open interest.
- OTC market: **notional principal**, which is unambiguous but massively overstates the money at risk, and **gross market value**, which is realistic but model-dependent and can be disputed.
- Interest rate contracts dominate OTC notional (≈82% at end-2017), followed by FX (≈16%).

## Mental Models
- **Think of a derivative as a transformation machine**: a mutual fund passes the return of the underlying through, while a derivative reshapes it (leverage, a floor, a cap, a sign flip). That is the working test for what counts as a derivative.
- **A put + the asset = insurance**. Bad outcomes trigger the payoff and good outcomes cost only the premium. By symmetry, **ABS/CDO investors are short puts**: they earn a steady return until prepayments or defaults cut it.
- **A swap is a strip of forwards**, and a futures contract is a forward that is re-struck daily. All three forward commitments can do the same economic job. Choose on credit, flexibility, privacy and the number of payment dates.
- **Default risk belongs to whoever owes the net amount**. In forwards and swaps either side can be the debtor. In options, once the premium is paid, only the writer can default.
- **Use arbitrage as a relative ruler, not a crystal ball**. The no-arbitrage forward price is the price of *eliminating* uncertainty, not a forecast of S_T.

## Worked Example
**1. Futures margin (initial margin £10, maintenance £6, long 1 unit at 120).**

| Day | Settle | MTM | Balance | Action |
|---|---|---|---|---|
| 1 | 122 | +2 | 12 | none |
| 2 | 118 | −4 | 8 | none (8 ≥ 6) |
| 3 | 115 | −3 | 5 | margin call: deposit 10 − 5 = **5** → 10 |
| 4 | 117 | +2 | 12 | none |

Check: deposits 10 + 5 = 15, cumulative P&L = 117 − 120 = −3, and the ending balance is 15 − 3 = **12**. The call restores the **initial** margin (£5), not just the maintenance level (£1).

**2. Option P&L (call X = 50, c₀ = 1.50; put X = 20, p₀ = 1.50).**
- Call at S_T = 45 / 50 / 55: payoff 0 / 0 / 5, profit −1.50 / −1.50 / +3.50. Breakeven = 51.50.
- Put at S_T = 18 / 22: payoff 2 / 0, profit +0.50 / −1.50. Breakeven = 18.50.
- The writers' results are the exact negatives (zero-sum before costs).

**3. Two arbitrages (r = 4% per period, no dividends).**
- *Mispriced relative stocks*:
  - AXE = 50 goes to 75 or 40. BYF = 38 goes to 60 or 32.
  - Both move in the ratio 75/60 = 40/32 = 1.25, so a short in 100 AXE is exactly hedged by a long in 125 BYF.
  - Short 100 AXE (+5,000), buy 125 BYF (−4,750), lend 250.
  - Either state: sell BYF for 7,500 or 4,000, which exactly covers the AXE buy-back (7,500 or 4,000). The bond is worth 250 × 1.04 = **260**, a riskless profit from zero capital.
  - No-arbitrage requires AXE = 1.25 × BYF: either AXE = 47.50 or BYF = 40.
- *Mispriced forward*:
  - Borrow 50, buy 1 AXE, sell it forward at 54.
  - At T, deliver for 54 and repay 52: **+2** whatever S_T turns out to be.
  - The arbitrage-free forward price is 50 × 1.04 = **52**.

## Anti-patterns
- **Calling mutual funds or ETFs derivatives**: they pass returns through; they do not transform them.
- **Treating the futures margin as a down payment on a loan**: it is a performance bond. No borrowing takes place.
- **Topping up only to the maintenance margin**: the rule is to restore the initial margin.
- **Linking "American/European" to geography**: both styles trade everywhere.
- **Reading payoff diagrams as return distributions**: "limited loss, unlimited gain" for a long call says nothing about the probability of each outcome.
- **Using notional principal as a measure of risk**: a swap's value at risk is the PV difference between its legs, a small fraction of notional.
- **Labelling merger or "risk arbitrage" as arbitrage**: it requires risk and capital, so it is speculation.
- **Believing that no-arbitrage makes vigilance useless**: the no-arbitrage condition holds only because traders keep looking for violations.

## Exam Focus & Traps
- **Premium vs value**: the option premium is paid at t = 0. The value at expiration is the payoff. Profit = payoff − premium (long) or premium − payoff (short).
- **Put max gain** = X − p₀ (the underlying cannot go below 0). **Short put max loss** = X − p₀. A **short call** has unlimited loss.
- **Forwards and futures have the same total payoff** (S_T − F₀), but the timing differs (daily vs at T). The difference is small when rates are low and maturities short.
- **Futures reduce credit risk** through daily settlement, margin and the clearinghouse. Forwards and swaps remain exposed to the net debtor. Option buyers bear credit risk only on the writer.
- **Characteristics that are not derivative traits**: a *low* degree of leverage (derivatives are high-leverage), being "created in the spot market", being "less volatile than spot markets".
- **What derivatives reveal**: the price at which uncertainty can be eliminated (forward commitments) and implied volatility (options). They do not reveal the "most widely used strategy".
- **The rebuttal to the destabilization critique**: crashes and panics (South Sea, Mississippi, 1929) long predate modern derivatives. Orange County showed that leverage does not need derivatives.
- **Arbitrage definition**: risk-free profit **with zero capital**. "Earning a return in excess of the risk taken" is an abnormal return, not arbitrage.
- **Interest rates, credit, weather and electricity are underlyings but not assets.** Say "underlying", not "underlying asset".
- **Swap credit risk** is far below a loan's, because only net payments are exchanged and principal is not. It is still non-trivial: at default, the net PV of all remaining payments is at stake.

## Key Takeaways
1. Classify every derivative by obligation (commitment vs claim), venue (exchange vs OTC) and payoff shape (linear vs kinked).
2. Forward commitments start at zero value. Options start at the premium. That premium buys the removal of the obligation.
3. Futures = standardized forwards + daily MTM + clearinghouse guarantee + price limits. A margin call restores the balance to the initial margin.
4. Payoffs: call max(0, S_T − X), put max(0, X − S_T), forward S_T − F₀(T). Profit subtracts the premium for the long.
5. Derivatives exist to transfer risk cheaply: low capital, low transaction costs, easy shorting, and information discovery (forward prices, implied volatility).
6. Price by no-arbitrage: build a riskless hedge portfolio, make it earn r_f. This needs a storable, shortable underlying.
7. Arbitrage is relative valuation and requires zero risk and zero capital. It is the mechanism that keeps derivative and spot prices consistent.

## Connects To
- **ch02**: formal pricing and valuation of forwards, futures, swaps and options (cost of carry, put–call parity, binomial model).
- **ch03**: Level II valuation of forward commitments mid-life (FRAs, currency/equity/interest rate swaps).
- **ch04**: option valuation (binomial trees, BSM).
- **ch05–ch07**: Level III uses of options, swaps, forwards and futures, and currency hedging.
- **`cfa-fixed-income` ch04**: ABS and CMO tranching in depth. **`cfa-fixed-income` ch11**: CDS pricing.
- **`hull-derivatives` ch01–ch02**: markets, CCPs and margin mechanics. **ch07**: swaps. **ch10**: option markets mechanics.
- **`cfa-level1-curriculum` ch20**: the owner's personal revision notes on this reading.
