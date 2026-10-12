# Chapter 11: Properties of Stock Options

## Core Idea
Without any model of volatility, no-arbitrage alone gives option price bounds, put–call parity for Europeans, and the result that an American call on a non-dividend-paying stock should never be exercised early.

## Frameworks Introduced
- **Six factors and their effect**:

| Factor ↑ | Euro call | Euro put | Amer. call | Amer. put |
|---|---|---|---|---|
| S₀ | + | − | + | − |
| K | − | + | − | + |
| T | ? | ? | + | + |
| σ | + | + | + | + |
| r | + | − | + | − |
| Dividends | − | + | − | + |

- **Bounds (no dividends)**:
  - Calls: `c ≤ S₀`, `c ≥ max(S₀ − Ke^{−rT}, 0)`.
  - Puts: `p ≤ Ke^{−rT}` (and `P ≤ K` for American puts), `p ≥ max(Ke^{−rT} − S₀, 0)`.
- **Put–call parity (European)**:
  - No dividends: `c + Ke^{−rT} = p + S₀`. A fiduciary call equals a protective put.
  - With dividends: `c + D + Ke^{−rT} = p + S₀`.
- **American bounds**: `S₀ − K ≤ C − P ≤ S₀ − Ke^{−rT}`. With dividends: `S₀ − D − K ≤ C − P ≤ S₀ − Ke^{−rT}`.
- **Early exercise rules**:
  - American call, no dividends: **never exercise early**. You would give up the insurance and the time value of K. So C = c.
  - American put: early exercise can be optimal when deep ITM. The interest earned on K outweighs the insurance.
  - Dividends: an American call may be exercised just before an ex-dividend date.

## Key Concepts
- **Fiduciary call**: a call + a zero-coupon bond paying K.
- **Protective put**: a put + the stock.
- **Synthetic positions**: `S = c − p + Ke^{−rT}`, `c = p + S − Ke^{−rT}`, and so on.
- **Capital-structure view (Merton)**: equity = a call on the firm's assets with strike = debt. Debt = riskless debt − a put on the assets.

## Mental Models
- **Parity is a replication identity**. Any mispricing is arbitraged by buying the cheap side (c + bond or p + stock) and selling the other.
- Think of an **American call as always worth more alive than dead** when the stock pays no dividends.
- A **put has a max value of K** (American) or Ke^{−rT} (European). Deep ITM puts behave like short stock plus a bond, so early exercise earns interest.

## Anti-patterns
- **Applying parity to American options**: it only gives bounds.
- **Exercising an American call early on a non-dividend stock** "to lock in profit": selling the option is always better.
- **Forgetting dividends in the bounds**: subtract PV(D) from S₀ everywhere.

## Worked Example
**Parity arbitrage (European).** S₀ = 31, K = 30, T = 0.25, r = 10%, c = 3.
- Parity implies p = 3 + 30e^{−0.025} − 31 = **1.26**.
- If the market put is 2.25: buy the call, short the put and short the stock. Invest 31 − 3 + 2.25 = 30.25 at 10% for 3 months → 31.02. At T, pay 30 for the share (via whichever option applies). **Profit = 1.02**.
- If the market put is 1: buy the put and the stock, sell the call. Borrow 29 → repay 29.73 at T and receive 30. **Profit = 0.27**.

**American bounds (Example 11.3).** C = 1.50, S₀ = 19, K = 20, T = 5/12, r = 10%.
- 19 − 20 ≤ C − P ≤ 19 − 20e^{−0.1×5/12}, so 0.18 ≤ P − C ≤ 1.00.
- The American put is worth between **$1.68 and $2.50**.

## Key Takeaways
1. σ raises every option price. r raises calls and lowers puts. Dividends lower calls and raise puts.
2. c + Ke^{−rT} = p + S₀: memorize it and use it to build synthetics.
3. Lower bounds: c ≥ S₀ − Ke^{−rT}, p ≥ Ke^{−rT} − S₀.
4. Never exercise an American call early on a non-dividend-paying stock. American puts may be exercised early.
5. Equity is a call on firm assets. Risky debt = riskless debt − a put.

## Connects To
- **Ch 13**: trees show early exercise of American puts.
- **Ch 15**: BSM gives exact European prices satisfying parity.
- **Ch 24**: Merton's model of credit risk.
- **Ch 12**: parity explains why a covered call looks like a short put.
