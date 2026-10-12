# Chapter 7: Swaps

## Core Idea
A swap is a portfolio of forward contracts. Value it by assuming today's forward rates (or forward FX rates) are realized and discounting at risk-free (OIS/SOFR) rates. Swaps transform the nature of assets and liabilities: fixed↔floating, currency A↔currency B.

## Frameworks Introduced
- **Plain vanilla interest rate swap**: pay fixed and receive floating (e.g., compounded SOFR) on a notional principal. The principal is not exchanged.
- **Transformations**:
  - A pay-fixed swap turns a floating-rate loan into a fixed one. A receive-fixed swap does the reverse.
  - Swaps convert fixed/floating *investments* the same way.
- **Bootstrapping the risk-free (OIS) curve**: a new swap has zero value. Solve iteratively for the zero rates that make each swap rate's value zero. OIS rates are used for discounting.
- **Valuation via forward rates (FRA portfolio)**:
  1. Compute the forward rate for each floating period.
  2. Compute the net cash flows assuming the forwards are realized.
  3. Discount at risk-free rates.
- **Valuation via bonds**: V_swap(receive fixed) = B_fixed − B_float. Just after a payment date, B_float = notional.
- **Comparative-advantage argument**: firms borrow where they have a relative advantage and swap. The apparent gains are often illusory (they reflect credit spreads and the lender's right to reprice floating loans).
- **Fixed-for-fixed currency swap**: exchange principals at the start and the end. Value = B_D − S₀B_F (for receiving domestic), or as a portfolio of FX forwards.
- **Other swaps**: amortizing, step-up, forward swaps, compounding swaps, constant-maturity swaps (CMS), cross-currency basis swaps, equity swaps, variance swaps, commodity swaps.

## Key Concepts
- **Swap rate**: the fixed rate that makes a new swap worth zero. It is the par yield of the risk-free curve.
- **Notional principal**: the base for computing payments. It is never exchanged in IRS.
- **Market maker (dealer) quote**: bid/offer on the fixed rate vs floating.
- **ISDA Master Agreement / Confirmation**: the legal framework and trade terms.
- **Day count conventions** apply to both legs (Actual/360 for floating, 30/360 for fixed, typically).
- **Credit risk in swaps**: exposure exists only when the swap has positive value to you. It is usually much smaller than the notional.
- **Credit default swap (CDS)**: insurance against default by a reference entity (Ch 25).

## Mental Models
- Think of an IRS as **long a floating-rate bond, short a fixed-rate bond** (or vice versa).
- **A swap starts at zero value**. Its value evolves as the curve moves: receive-fixed gains when rates fall.
- For currency swaps, **the principal exchange dominates** the risk. The FX exposure is on the principal, not just on the coupons.

## Anti-patterns
- **Local authorities speculating with swaps** (Hammersmith & Fulham, 1987–89): huge interest rate bets. The council lost several hundred million pounds. The House of Lords ruled it had no authority to enter the swaps, so the contracts were void and the banks absorbed the losses. Check counterparty capacity.
- **Taking comparative-advantage "savings" at face value**: they usually reflect credit risk being transferred.

## Worked Example
**Valuing a pay-fixed-3% swap (Example 7.1).** Notional $100m, remaining life 1.2 years, exchanges at 0.2, 0.7 and 1.2 years.
- Risk-free rates are 2.8%, 3.2% and 3.4% (continuous).
- The floating rate for 0.2 is 2.50% (a mix of observed and forward). The forwards are 3.36% and 3.68%. In semiannual terms: 2.516%, 3.388%, 3.714%.

| t | Fixed | Float | Net | DF | PV |
|---|---|---|---|---|---|
| 0.2 | −1.500 | +1.258 | −0.242 | 0.9944 | −0.241 |
| 0.7 | −1.500 | +1.694 | +0.194 | 0.9778 | +0.190 |
| 1.2 | −1.500 | +1.857 | +0.357 | 0.9600 | +0.343 |

- Swap value to the fixed payer: **+$0.292m**.

## Key Takeaways
1. Swaps = portfolios of forwards. Value them by assuming forwards are realized, then discount at OIS/SOFR.
2. The swap rate is the par yield. New swaps are worth zero, which is how the OIS zero curve is bootstrapped.
3. IRS transform fixed↔floating exposures. Currency swaps transform currency exposures.
4. Credit exposure on a swap is its (positive) mark-to-market, not its notional.
5. Check the legal capacity of counterparties and do not over-trust comparative-advantage arguments.

## Connects To
- **Ch 4**: forward rates, FRAs, bootstrapping.
- **Ch 9 / Ch 24**: CVA on swap portfolios.
- **Ch 25**: credit default swaps.
- **Ch 29**: swaptions.
- **Ch 34**: non-standard swaps (CMS, compounding, variance).
