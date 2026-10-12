# Chapter 6: Interest Rate Futures

## Core Idea
Interest rate futures (Treasury bond futures, SOFR/Eurodollar futures) are priced and hedged with day-count conventions, delivery options (cheapest-to-deliver) and duration. Duration-based hedging works only for parallel curve shifts.

## Frameworks Introduced
- **Day counts**:
  - Actual/actual for Treasury bonds.
  - 30/360 for corporate bonds.
  - Actual/360 for money market instruments.
  - Accrued interest = coupon × (days since last coupon / days in period).
- **Price quotes**:
  - **Clean (quoted) price** + accrued interest = **dirty (cash) price**.
  - T-bill discount quote: `P = (360/n)(100 − Y)`.
  - Bond prices are quoted in dollars and 32nds: 90-05 = 90 + 5/32.
- **Treasury bond futures**:
  - Deliverable bonds have ≥ 15 years to maturity and < 25 years.
  - **Conversion factor (CF)** = the price of the bond per $1 face at a 6% yield.
  - Cash received by the short = `(Quoted futures price × CF) + Accrued interest`.
- **Cheapest-to-deliver (CTD)**: minimize `Quoted bond price − (Futures price × CF)`.
  - Yields > 6% favor low-coupon, long-maturity bonds.
  - Yields < 6% favor high-coupon, short-maturity bonds.
- **Futures price estimate**: compute the CTD cash futures price `(S − I)e^{rT}` and strip the accrued interest to get the quoted CTD futures price. Divide by the CF.
- **SOFR futures (3-month)**: settle on the compounded daily SOFR over the reference quarter. Quote = 100 − R. A 1bp move = $25 per contract.
- **Convexity adjustment**: forward rate = futures rate − ½σ²T₁T₂ (Ho–Lee). This matters for long maturities (Ch 30).
- **Duration-based hedge ratio**: `N* = (P·D_P)/(V_F·D_F)`. P = portfolio value, D_P = its duration at hedge maturity, V_F = futures contract price, D_F = duration of the underlying (CTD) at futures maturity.

## Key Concepts
- **Wild card play**: the short can declare intent to deliver up to 8 p.m. at the 2 p.m. settlement price.
- **Delivery options in T-bond futures**: which bond, which day and timing (wild card). All of them lower the futures price.
- **Eurodollar futures**: the legacy 3-month LIBOR contract, replaced by SOFR futures.
- **Asset-liability management (ALM)**: banks match the durations of assets and liabilities, or manage the gap.
- **Duration matching / portfolio immunization**: set the portfolio duration to zero or to the target.

## Mental Models
- Think of the T-bond futures price as **tracking the CTD bond divided by its CF**.
- Use **duration hedging as a first-order parallel-shift hedge**. Expect poor performance when D_F and D_P differ a lot, because short rates are more volatile than long rates.
- **SOFR futures ≈ strip of FRAs** with a convexity bias. Futures rates > forward rates.

## Anti-patterns
- **Assuming day-count conventions are harmless**: 30/360 vs actual/actual can create apparent arbitrage (Business Snapshot 6.1, February 28 vs March 1).
- **Hedging a 2-year exposure with 20-year bond futures via duration alone**: this is exposed to twists in the curve.

## Worked Example
**Cheapest-to-deliver (Example 6.1).** The settlement price is 93-08 = 93.25.
| Bond | Quoted price | CF | Cost = Price − 93.25 × CF |
|---|---|---|---|
| 1 | 99.50 | 1.0382 | 2.69 |
| 2 | 143.50 | 1.5188 | **1.87 (CTD)** |
| 3 | 119.75 | 1.2615 | 2.12 |

**Duration hedge (Example 6.6).** A $10m bond portfolio has D_P = 6.80. The futures price is 93-02 → V_F = $93,062.50. The CTD duration is D_F = 9.20.
- N* = (10,000,000 × 6.80)/(93,062.50 × 9.20) = 79.42 → **short 79 contracts**.

## Key Takeaways
1. Always convert quoted (clean) prices to cash (dirty) prices with the right day count.
2. The short's delivery options (CTD, timing, wild card) lower T-bond futures prices.
3. SOFR futures replace Eurodollar futures and settle on compounded overnight SOFR.
4. Futures rates must be convexity-adjusted before use as forward rates.
5. Duration-based hedging: `N* = P·D_P/(V_F·D_F)`. It is valid only for parallel shifts.

## Connects To
- **Ch 4**: duration, convexity, forward rates.
- **Ch 7**: SOFR futures and swaps are used to bootstrap the OIS curve.
- **Ch 22**: PCA/partial durations handle non-parallel shifts.
- **Ch 30**: the convexity adjustment in detail.
