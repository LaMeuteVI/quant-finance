# Chapter 5: Determination of Forward and Futures Prices

## Core Idea
Forward prices of *investment* assets are pinned down exactly by no-arbitrage (cost of carry). Forward prices of *consumption* assets are only bounded above, and the gap is the convenience yield. A forward is valued by assuming the forward price is realized and then discounting.

## Frameworks Introduced
- **Cost-of-carry pricing (investment assets)**:
  - No income: `F₀ = S₀e^{rT}`.
  - Known income with PV I: `F₀ = (S₀ − I)e^{rT}`.
  - Known yield q: `F₀ = S₀e^{(r−q)T}`.
  - How: if F₀ is too high, buy spot, borrow and short the forward (cash-and-carry). If it is too low, short spot, invest and go long the forward (reverse cash-and-carry). The reverse trade requires short selling.
- **Value of an existing forward**:
  - Long: `f = (F₀ − K)e^{−rT}`, equivalently `f = S₀ − Ke^{−rT}` with no income.
  - Short: `(K − F₀)e^{−rT}`.
- **Stock index futures**: `F₀ = S₀e^{(r−q)T}`, with q the dividend yield. **Index arbitrage** keeps it in line: program trading of the basket vs futures.
- **Currencies (interest rate parity)**: `F₀ = S₀e^{(r−r_f)T}`. S is the domestic price of one unit of foreign currency. The foreign currency is an asset yielding r_f.
- **Commodities**:
  - Investment metals: `F₀ = (S₀ + U)e^{rT}`, or `S₀e^{(r+u)T}` with storage cost.
  - Consumption commodities: `F₀ ≤ S₀e^{(r+u)T}`.
  - **Convenience yield y** is defined by `F₀e^{yT} = S₀e^{(r+u)T}`.
- **Cost of carry c**: `c = r + u − q`.
  - Investment assets: `F₀ = S₀e^{cT}`.
  - Consumption assets: `F₀ = S₀e^{(c−y)T}`.
- **Futures vs forward**: they are equal when interest rates are deterministic. A positive correlation between the asset and interest rates makes futures > forwards.
- **Futures vs expected spot (CAPM)**:
  - The asset is positively correlated with the market (k > r): F₀ < E(S_T). This is **normal backwardation**.
  - Negative correlation: F₀ > E(S_T). This is **contango**.

## Key Concepts
- **Investment asset**: held for investment by a significant number of traders (gold, stocks, bonds).
- **Consumption asset**: held to be consumed (oil, copper, grain).
- **Short selling**: selling borrowed securities. The short pays any income on the shares to the lender and must post margin.
- **Delivery options & timing**: when F rises with maturity, the short delivers early. When it falls, the short delivers late.
- **Quanto / Nikkei 225 CME contract**: an index quoted in yen but settled in USD. Parity then fails, and a quanto adjustment is needed (Ch 30).

## Mental Models
- Think of the **forward price as spot plus the cost of carrying the asset to T**: financing + storage − income.
- **The foreign currency is a dividend-paying asset** whose yield is the foreign risk-free rate.
- **Convenience yield = the value of having the physical asset now**. High convenience yield (scarcity) → backwardated futures curve.
- Use "**value = PV(F₀ − K)**" to mark any forward to market.

## Anti-patterns
- **Mis-booking accruals as profit**: Kidder Peabody (Joseph Jett) booked the forward/strip price differential on Treasury strips as profit. The system reported a $100m profit that was really the passage of time in a forward price. The true outcome was a loss of about $350m.
- **Treating consumption commodities like gold**: shorting spot to arbitrage a low futures price is impossible if holders will not lend the commodity.

## Reference Tables
| Asset | Forward/futures price | Value of long forward (delivery K) |
|---|---|---|
| No income | `S₀e^{rT}` | `S₀ − Ke^{−rT}` |
| Known income PV I | `(S₀ − I)e^{rT}` | `S₀ − I − Ke^{−rT}` |
| Known yield q | `S₀e^{(r−q)T}` | `S₀e^{−qT} − Ke^{−rT}` |

## Worked Example
**Forward on a stock (Example 5.4).** S₀ = 25, K = 24, r = 10% and T = 0.5.
- F₀ = 25e^{0.05} = 26.28.
- The long forward is worth f = (26.28 − 24)e^{−0.05} = **2.17**.

**Currency arbitrage (Example 5.6).** The AUD rate is 3% and the USD rate is 1% (2 years). Spot is 0.7500 USD/AUD.
- Parity gives F = 0.75e^{(0.01−0.03)·2} = 0.7206.
- Suppose the market forward is 0.7000:
  1. Borrow 1,000 AUD, convert to 750 USD and invest at 1% → 765.15 USD.
  2. Buy 1,061.84 AUD forward for 743.29 USD. This exactly repays the AUD loan.
- Riskless profit: **21.87 USD**.

## Key Takeaways
1. Investment assets: F₀ = S₀e^{(r−q+u)T}, exactly, by arbitrage.
2. Consumption assets: only an upper bound. The convenience yield closes the gap.
3. Value a forward as PV(F₀ − K) for the long side.
4. Treat currencies and indices as assets with a known yield (r_f or q).
5. Futures ≈ forwards unless maturities are long and rates are strongly correlated with the asset.

## Connects To
- **Ch 3**: basis = spot − futures, driven by cost of carry.
- **Ch 17**: the same yield trick values index and currency options.
- **Ch 18**: futures as an asset with yield r (Black's model).
- **Ch 35**: convenience yield and commodity futures curves.
