# Chapter 34: Swaps Revisited

## Core Idea
Most swap variants are valued by assuming floating rates equal their forward values and discounting at OIS rates. This covers amortizing, step-up, basis, compounding and most currency swaps. Swaps paying a rate in the "wrong" time or currency need convexity, timing or quanto adjustments. Swaps with embedded options (accrual, cancelable) need option models.

## Frameworks Introduced
- **Variations on the vanilla deal** (value via forwards):
  - Amortizing / step-up notional.
  - Different payment frequencies on the two legs.
  - Forward-start swaps.
  - **Basis swaps** (floating vs floating, e.g., 3m vs 6m, or SOFR vs term rate).
- **Compounding swaps**: interest on each leg compounds at a specified rate (e.g., the forward rate + spread) until a single final payment. Value by assuming the forward rates are realized.
- **Currency and nonstandard swaps**:
  - Fixed-for-floating cross-currency swaps.
  - **Diff (quanto) swaps**: a foreign floating rate applied to a domestic notional. These need a quanto adjustment.
- **CMS / CMT swaps**: the floating leg is a swap or Treasury yield observed at the reset. These need a convexity adjustment (and a timing adjustment if paid later).
- **LIBOR/SOFR-in-arrears swaps**: the rate is observed and paid at the same date. This needs a timing adjustment.
- **Equity swaps**: the total return on an index is exchanged for fixed or floating. The value is zero just after each reset.
- **Swaps with embedded options**:
  - **Accrual swap**: the fixed side accrues only on days the floating rate is within a range. It equals a vanilla swap + a strip of daily binary options.
  - **Cancelable swap**: a vanilla swap + a Bermudan swaption to cancel. **Cancelable compounding swaps** also exist.
  - **Extendable swaps** are the mirror case.
- **Other swaps**: commodity swaps, volatility and variance swaps, index amortizing swaps (the notional depends on the rate path), and the P&G "5/30" leveraged swap.

## Key Concepts
- **Discounting at OIS**: the standard for collateralized swaps.
- **Hypothetical confirmations**: legal term sheets defining day counts, business-day conventions and fixing sources.
- **Leverage in swaps**: payoffs multiplied by formulas in rates or prices can produce extreme sensitivity.

## Mental Models
- **Default approach: "forwards are realized, discount at OIS."** Then ask whether the payoff is paid in the natural numeraire. If not, apply the Ch 30 adjustment.
- **Decompose embedded options**: vanilla swap + binaries (accrual), or + a Bermudan swaption (cancelable).
- **Leverage formulas should be stress-tested**, not just valued at the forwards.

## Anti-patterns
- **P&G 5/30 swap (1993)**: a 5-year, $200m notional swap whose spread depended on the 5-year CMT yield and the 30-year Treasury price. P&G effectively sold a highly leveraged put on bond prices. Rates rose in 1994 and P&G lost ≈ **$90m**.
- **Valuing CMS or in-arrears swaps with unadjusted forwards**.
- **Treating accrual swaps as vanilla**: their binary options carry large gamma near the range boundaries.

## Worked Example
**Compounding swap (Example 34.1).** 3 years, annual resets, notional $100m. Pay fixed 4%, compounding at 3.9%. Receive the 12-month rate, compounding at the rate − 20bp. All forward rates = 5%, OIS = 4%.
- **Fixed leg**:
  - Year 1: 4.
  - Year 2: 4 × 1.039 + 4 = 8.156.
  - Year 3: 8.156 × 1.039 + 4 = **12.474m**.
- **Floating leg** (assume forwards are realized at 5%, compounding at 4.8%):
  - Year 1: 5.
  - Year 2: 5 × 1.048 + 5 = 10.24.
  - Year 3: 10.24 × 1.048 + 5 = **15.732m**.
- **Value** to the fixed payer = (15.732 − 12.474)/1.04³ ≈ **$2.90m**.

## Key Takeaways
1. Most swaps: assume forwards are realized and discount at OIS.
2. CMS, in-arrears and diff swaps need convexity, timing or quanto adjustments.
3. Accrual swap = swap + daily binaries. Cancelable swap = swap + a Bermudan swaption.
4. Equity swaps reset to zero value on payment dates.
5. Leveraged formula swaps (P&G) demand stress tests and scenario analysis.

## Connects To
- **Ch 7**: vanilla swaps.
- **Ch 30**: the adjustments.
- **Ch 29 / Ch 32**: swaptions and Bermudans.
- **Ch 26**: binaries and variance swaps.
- **Ch 37**: mishaps (P&G, Gibson Greetings).
