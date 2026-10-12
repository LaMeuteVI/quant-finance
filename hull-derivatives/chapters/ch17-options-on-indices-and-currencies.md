# Chapter 17: Options on Stock Indices and Currencies

## Core Idea
A stock index is like a stock paying a continuous dividend yield q. A foreign currency is like a stock paying yield r_f. BSM extends by replacing S₀ with S₀e^{−qT}. Index puts provide portfolio insurance, and currency options hedge FX exposures, including via zero-cost range forwards.

## Frameworks Introduced
- **Merton's extension (known yield q)**:
  - `c = S₀e^{−qT}N(d₁) − Ke^{−rT}N(d₂)` and `p = Ke^{−rT}N(−d₂) − S₀e^{−qT}N(−d₁)`.
  - `d₁ = [ln(S₀/K) + (r − q + σ²/2)T]/(σ√T)`.
  - Parity: `c + Ke^{−rT} = p + S₀e^{−qT}`.
  - Equivalently, use F₀ = S₀e^{(r−q)T} in Black's formula (Ch 18).
- **Index options**: cash-settled, 100 × (index − K) per contract.
  - **Portfolio insurance**: buy β × V_A/(100 × S₀) put contracts.
  - For β ≠ 1, choose K using CAPM to map the desired portfolio floor to an index level.
- **Currency options (Garman–Kohlhagen)**: q = r_f.
  - Treasurers receiving FX buy puts. Those paying FX buy calls.
- **Range forward (collar)**: long put at K₁ + short call at K₂ (for a receiver), zero cost. It locks the FX rate between K₁ and K₂.
- **Trees**: use a = e^{(r−q)Δt} for indices and a = e^{(r−r_f)Δt} for currencies. American options are valued by backward induction.

## Key Concepts
- **Dividend yield q**: the continuous rate of dividend payout on the index. If q varies, use its average over the option's life.
- **Implied q** from put–call parity or futures prices.
- **FX quote convention**: S = the domestic price of one foreign unit. Put(A→B, K) = Call(B→A, 1/K) scaled.
- **Flex options, LEAPS, VIX options**: other index products.
- **Stocks-beat-bonds guarantees**: they are costly long-dated puts. Stocks outperform on average but not reliably (Business Snapshot 17.1).

## Mental Models
- **One formula, three underlyings**: stocks with q, indices with q, and FX with r_f. Only the "yield" changes.
- **Insurance cost = put premium**. Pick K by the floor you can accept, and scale by β for non-index portfolios.
- **Collars trade upside for downside at zero cost**. Useful when budgets forbid option premiums.

## Anti-patterns
- **Buying index puts 1:1 for a high-beta portfolio**: this under-insures. Multiply by β and map the strike via CAPM.
- **Mixing FX quote directions** (USD/GBP vs GBP/USD) when setting K and r_f.
- **Using the spot dividend yield for long-dated index options** when q is seasonal or trending.

## Worked Example
**Implied volatility of a GBP call (Example 17.2).** 4-month ATM call: S₀ = K = 1.6000, r = 8% (USD), r_f = 11% (GBP), price 4.3¢.
- σ = 20% gives 6.39¢ and σ = 10% gives 2.85¢.
- By interpolation or iteration, the implied volatility is **14.1%**.

**Portfolio insurance.** A $500,000 portfolio has β = 2.0, the index is at 1,000, r = 12% and q = 4%. The manager wants a floor of $450,000 in 3 months.
- Map through CAPM: portfolio −10% corresponds to the index at ≈ 960.
- Buy 2 × 500,000/(100 × 1,000) = **10 put contracts with K = 960**.

## Key Takeaways
1. Replace S₀ by S₀e^{−qT}: q = dividend yield for indices and r_f for currencies.
2. Index options settle in cash: 100 × (index − K) per contract.
3. Portfolio insurance: β × V_A/(100·S₀) puts, with K chosen via CAPM.
4. Range forwards give a zero-cost band for FX hedgers.
5. American index and FX options: use trees with the right growth factor a.

## Connects To
- **Ch 5**: F₀ = S₀e^{(r−q)T} and interest rate parity.
- **Ch 15**: base BSM.
- **Ch 18**: Black's model uses the futures or forward price directly.
- **Ch 19**: portfolio insurance via dynamic hedging.
- **Ch 26**: quanto and exotic FX options.
