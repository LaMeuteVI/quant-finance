# Chapter 3: Hedging Strategies Using Futures

## Core Idea
A hedge swaps price risk for basis risk. Choose the contract (asset, maturity) that minimizes basis risk, then size it with the minimum-variance hedge ratio (or beta for equity portfolios). Remember that hedging can create cash-flow and business risks of its own.

## Frameworks Introduced
- **Short hedge vs long hedge**:
  - Short hedge: you own or will sell the asset, so you lose when the price falls. You sell futures.
  - Long hedge: you will buy the asset, so you lose when the price rises. You buy futures.
- **Basis & effective price**:
  - Basis `b = S − F`.
  - Hedging with a close-out at t₂ locks in the effective price `F₁ + b₂` (the initial futures price plus the final basis).
  - The only residual uncertainty is `b₂`. That is **basis risk**.
- **Choice of contract**:
  - Asset: take the most correlated futures contract.
  - Delivery month: choose the month *just after* the hedge's expiration. This avoids delivery-month erratic pricing and minimizes basis risk.
- **Minimum-variance hedge ratio**: `h* = ρ · σ_S / σ_F`. It equals the slope of the regression of ΔS on ΔF. The hedge effectiveness is ρ².
- **Optimal number of contracts**: `N* = h* · Q_A / Q_F`.
  - Tailing the hedge (daily settlement): use `N* = h* · V_A / V_F`, with values instead of quantities.
- **Equity portfolio hedge (CAPM beta)**: `N* = β · V_A / V_F`.
  - To move beta from β to β*, trade `(β* − β) · V_A / V_F` contracts. Negative means short.
- **Stack and roll**: build a long-dated hedge from a sequence of short-dated futures. It is exposed to roll basis risk and funding needs.

## Key Concepts
- **Hedge ratio**: the ratio of the futures position size to the exposure size.
- **Cross hedging**: hedging with futures on a *different but correlated* asset (jet fuel hedged with heating oil).
- **Hedge effectiveness**: the proportion of variance eliminated, `ρ²`.
- **Tailing the hedge**: adjusting for daily settlement by using dollar values (`V_A`, `V_F`).
- **Strengthening / weakening basis**: the basis increases / decreases. Strengthening helps a short hedger and hurts a long hedger.

## Mental Models
- Think of **"Effective price = F₁ + b₂"**: once you hedge, you are no longer speculating on price, only on basis.
- Use **ρ·σ_S/σ_F**, not 1.0, whenever the hedging asset differs from the exposure.
- **Hedging is a competitive decision**: if no competitor hedges, hedging can *increase* the variance of your margins. Price pass-through matters.
- **Shareholders can diversify**: the theoretical case against corporate hedging (but transaction costs and financial distress favor it).

## Anti-patterns
- **Hedging a long-term obligation with rolled short-dated futures without funding lines**: Metallgesellschaft (early 1990s). Oil prices fell, margin calls drained cash, management unwound the hedge, and the loss was $1.33bn.
- **Judging a hedge by the P&L of the futures leg alone**: the treasurer who hedges and "loses" on futures while the underlying gains. Educate the board beforehand.
- **Using h = 1 for a cross hedge**: this overhedges or underhedges when σ_S ≠ σ_F or ρ < 1.

## Code Examples
```python
import numpy as np
dF = np.array([0.021,0.035,-0.046,0.001,0.044,-0.029,-0.026,-0.029,0.048,-0.006,-0.036,-0.011,0.019,-0.027,0.029])
dS = np.array([0.029,0.020,-0.044,0.008,0.026,-0.019,-0.010,-0.007,0.043,0.011,-0.036,-0.018,0.009,-0.032,0.023])
rho = np.corrcoef(dS, dF)[0,1]
h = rho * dS.std(ddof=1) / dF.std(ddof=1)   # ≈ 0.78
N = round(h * 2_000_000 / 42_000)          # ≈ 37 contracts
```
- **What it demonstrates**: the minimum-variance hedge ratio from historical price changes (airline example).

## Worked Example
**Airline cross hedge (Example 3.3).** The airline buys 2m gallons of jet fuel in 1 month and hedges with heating oil futures (42,000 gal each).
- The data give σ_F = 0.0313, σ_S = 0.0263 and ρ = 0.928.
- The hedge ratio is h* = 0.928 × 0.0263 / 0.0313 = 0.78.
- The number of contracts is N* = 0.78 × 2,000,000 / 42,000 ≈ 37 long contracts.

**Equity hedge.** A portfolio worth $5.05m has β = 1.5. The index future is 1,010 × $250 (V_F = $252,500).
- Full hedge: N* = 1.5 × 5.05m / 252,500 = 30 contracts short.
- To cut β to 0.75: short 15 contracts.

**Yen hedge (Example 3.1).** A company shorts 4 September yen futures at 1.0800¢. It closes out at F = 1.0250¢ when S = 1.0200¢.
- The effective price is 1.0800 + (1.0200 − 1.0250) = 1.0750¢/¥.
- For ¥50m that is $537,500.

## Key Takeaways
1. Hedging converts price risk into basis risk. Choose the contract that minimizes basis variance.
2. Size with `h* = ρσ_S/σ_F`, and with `β·V_A/V_F` for equity portfolios.
3. Pick the delivery month just after the end of the hedge.
4. Rolling hedges create funding liquidity risk. Secure credit lines before rolling large hedges.
5. Communicate the hedging objective internally. The hedge's P&L alone is not the right scorecard.

## Connects To
- **Ch 2**: margin mechanics behind stack-and-roll cash flows.
- **Ch 5**: why basis exists (cost of carry, convenience yield).
- **Ch 6**: duration-based hedging with interest rate futures.
- **Ch 19**: dynamic delta hedging generalizes the hedge ratio.
- **CAPM**: beta as the regression slope of portfolio vs index excess returns.
