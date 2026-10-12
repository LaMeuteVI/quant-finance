# Chapter 10: Mechanics of Options Markets

## Core Idea
Exchange-traded options are standardized (size, expiration, strikes), cleared by the Options Clearing Corporation (OCC) and margined only on the writer's side. Contract terms adjust for splits and stock dividends but not for cash dividends. OTC options are tailored alternatives.

## Frameworks Introduced
- **Four basic positions**: long call, short call, long put, short put. Writing = taking a short position and receiving the premium.
- **Moneyness**:
  - Call: ITM if S > K, ATM if S ≈ K, OTM if S < K. The reverse holds for puts.
  - **Intrinsic value** = max(S − K, 0) for a call, max(K − S, 0) for a put.
  - **Time value** = option price − intrinsic value.
- **Stock option specification (US)**:
  - 1 contract = 100 shares.
  - Expiration is the third Friday of the expiration month. Weeklies, LEAPS (long-dated) and FLEX options also exist.
  - Strikes are at $2.50, $5 or $10 intervals.
- **Adjustment rules**:
  - n-for-m split: the strike becomes K·m/n and the number of shares n/m times as many.
  - Stock dividends are handled like splits.
  - Cash dividends: no adjustment, except for large ones.
- **Naked (uncovered) option margin**: the greater of:
  1. 100% of proceeds + 20% of the underlying − OTM amount.
  2. 100% of proceeds + 10% of the underlying (call) or 10% of the strike (put).
- **OCC**: it guarantees performance, records positions and assigns exercises randomly to writers.

## Key Concepts
- **Option class / series**: all options of one type on one stock / a class with the same K and T.
- **Market maker**: quotes bid/ask and provides liquidity. The exchange caps the spread.
- **Offsetting order**: closes a position. **Open interest** counts the outstanding contracts.
- **Position limits / exercise limits**: caps on contracts per side of the market.
- **Warrants**: options issued by the company, which are dilutive on exercise.
- **Employee stock options (ESOs)**: company-issued call options for compensation (Ch 16).
- **Convertible bonds**: bonds that include the right to convert into stock.
- **OTC options**: tailored strikes and maturities, with counterparty risk mitigated by collateral.

## Mental Models
- Think of **option buyers as having limited, known losses**, while writers carry potentially unlimited liabilities. That is why only writers post margin.
- Use **intrinsic + time value** to reason about early exercise. An American option with positive time value should be sold, not exercised.
- **Splits change nothing economically**, and the contract adjustment preserves both sides' positions.

## Anti-patterns
- **Assuming cash dividends are protected**: they are not. A dividend drop in S hurts calls and helps puts.
- **Writing naked options without margin headroom**: the margin is recomputed daily, and adverse moves trigger calls.
- **Using options for tax planning without checking wash-sale and constructive-sale rules** (Business Snapshot 10.1).

## Reference Tables
| Position | Payoff at T | Max loss |
|---|---|---|
| Long call | max(S_T − K, 0) | premium |
| Short call | −max(S_T − K, 0) | unlimited |
| Long put | max(K − S_T, 0) | premium |
| Short put | −max(K − S_T, 0) | K − premium |

## Worked Example
**Naked call margin (Example 10.3).** The investor writes 4 naked call contracts: option price $5, K = $40, S = $38 (OTM by $2).
- Calculation 1: 400 × (5 + 0.2 × 38 − 2) = **$4,240**.
- Calculation 2: 400 × (5 + 0.1 × 38) = $3,520.
- The initial margin is $4,240. If the option were a put, it would be $2 ITM: 400 × (5 + 0.2 × 38) = $5,040.

## Key Takeaways
1. 1 US stock option = 100 shares. Expiration is the third Friday. K is adjusted for splits but not for cash dividends.
2. Only writers post margin. The rule is the greater of the 20% and 10% calculations above.
3. The OCC stands behind every exchange-traded option and assigns exercises randomly.
4. Price = intrinsic + time value. Positive time value argues against early exercise.
5. Warrants, ESOs and convertibles are options issued by the company: they are dilutive.

## Connects To
- **Ch 11**: bounds and put–call parity.
- **Ch 12**: strategies combining options.
- **Ch 16**: ESOs.
- **Ch 17–18**: options on indices, currencies and futures.
