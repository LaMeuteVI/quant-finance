# Chapter 20: Volatility Smiles and Volatility Surfaces

## Core Idea
Traders do not believe in lognormality. They keep BSM as a quoting device and encode the true distribution in implied volatility as a function of strike and maturity: the volatility surface. Equity smiles slope downward (skew). FX smiles are U-shaped.

## Frameworks Introduced
- **Calls and puts have the same implied volatility** for the same K and T. This follows because put–call parity holds for both market prices and BSM prices.
- **FX smile (U-shape)**:
  - Both tails are heavier than lognormal.
  - OTM puts *and* OTM calls therefore have higher implied volatility than ATM.
  - Causes: jumps and stochastic volatility.
- **Equity skew (downward slope)**: a heavier left tail and a thinner right tail. Causes:
  - **Leverage**: price down → leverage up → volatility up.
  - **Volatility feedback**: volatility up → required return up → price down.
  - **Crashophobia**: demand for crash protection since 1987.
- **Ways to characterize the smile**: plot implied volatility against K, against K/S₀, against K/F₀, or against **delta**. The delta convention is typical in FX (25-delta risk reversals and butterflies).
- **Volatility surface**: implied volatility as a function of (K/S or Δ, T). Interpolate between quoted points to price new options. The smile flattens as T grows.
- **Minimum variance delta**: `Δ_MV = Δ_BSM + Vega_BSM · ∂E(σ_imp)/∂S`. For equities (negative skew), Δ_MV < Δ_BSM.
- **Role of the model**: here BSM is an interpolation tool. A new option is priced consistently with the traded ones.
- **Anticipated single jump**: a bimodal terminal distribution produces a **frown**. Implied volatility is highest near the money and lower away from ATM.

## Key Concepts
- **Implied distribution**: the smile implies the risk-neutral density. Breeden–Litzenberger: `g(K) = e^{rT} ∂²c/∂K²`.
- **Risk reversal**: 25Δ call implied volatility minus 25Δ put implied volatility. It measures skew.
- **Butterfly (strangle) quote**: the average of the 25Δ call and put implied volatilities, minus ATM. It measures curvature.
- **Sticky strike vs sticky delta**: two assumptions about how the surface moves when S moves.
- **Volatility term structure**: slopes up when short-dated implied volatility is historically low, and down when it is high (mean reversion).

## Mental Models
- **Implied volatility is "the wrong number to put into the wrong formula to get the right price"**. It is a price, not a forecast.
- Read **skew as a statement about tail probability**: high implied volatility on OTM puts means the market gives crashes more probability than lognormal does.
- Use the **surface for consistency**: price exotics or illiquid strikes with the volatility at the point of the surface that matches their risk.

## Anti-patterns
- **Using a single ATM volatility for OTM options**: this underprices crash puts and misprices the wings.
- **Delta-hedging equities with the BSM delta and ignoring skew dynamics**: use the minimum variance delta.
- **Assuming the smile stays fixed when S moves**: sticky-strike vs sticky-delta matters for P&L.

## Reference Tables
| Market | Smile shape | Tails vs lognormal | Main cause |
|---|---|---|---|
| FX | U-shaped smile | Both heavier | Jumps, stochastic volatility |
| Equity / index | Downward skew | Heavy left, thin right | Leverage, crashophobia |
| Anticipated binary event | Frown | Bimodal | Single large jump |
| Commodities (some) | Upward skew | Heavy right | Supply shocks |

## Worked Example
**Takeover announcement (Section 20.8).** The stock is at $50. News due in a few days will move it to $58 or to $42 (±$8). Consider a 1-month option.
- The true terminal distribution is **bimodal**, with little mass near $50.
- ATM options are worth relatively more than lognormal suggests, because a move of 8 is certain.
- Deep ITM and deep OTM options are worth relatively less.
- Inverting BSM gives the highest implied volatility at K ≈ 50, falling toward both wings. The result is a volatility **frown**, the opposite of the FX smile.

## Key Takeaways
1. Implied volatility is identical for calls and puts at the same (K, T).
2. Equity: downward skew (crash fear). FX: U-shaped smile (fat tails on both sides).
3. The smile is equivalent to the implied risk-neutral density.
4. The volatility surface (K, T) is the object the market prices. BSM is the interpolation engine.
5. Adjust delta for smile dynamics with the minimum variance delta.

## Connects To
- **Ch 15**: implied volatility.
- **Ch 19**: vega hedging by bucket.
- **Ch 26**: exotics priced off the surface; barriers are skew-sensitive.
- **Ch 27**: jump-diffusion, stochastic volatility and IVF/local volatility models that fit the smile.
