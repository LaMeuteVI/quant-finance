# Chapter 12: Trading Strategies Involving Options

## Core Idea
Combining options with each other, with the underlying and with zero-coupon bonds generates almost any piecewise-linear payoff. Choose the strategy that matches your view on direction *and* volatility, then check its cost, maximum loss and early-exercise risk.

## Frameworks Introduced
- **Principal-protected notes (PPN)**: a zero-coupon bond + a call. The investor gets the principal back plus upside. Feasibility depends on rates, dividends and volatility (low rates make PPNs expensive).
- **Option + underlying**:
  - **Covered call** (long stock, short call) ≈ short put.
  - **Protective put** (long stock, long put) ≈ long call.
  - Their reverses are the short-stock equivalents.
- **Spreads (same type of option)**:
  - **Bull spread**: buy low K, sell high K. It profits from a moderate rise with capped gain and loss.
  - **Bear spread**: buy high K, sell low K.
  - **Box spread** = a bull call spread + a bear put spread. Payoff = K₂ − K₁ for sure, so its value is (K₂ − K₁)e^{−rT}. This holds only for Europeans.
  - **Butterfly**: long K₁ and K₃, short 2×K₂ with K₂ midway. It profits if S_T stays near K₂ (a low-volatility view).
  - **Calendar spread**: sell short-dated, buy long-dated at the same K. It profits if S stays near K. Neutral, bullish and bearish variants exist.
  - **Diagonal spread**: different K and T.
- **Combinations (calls + puts)**:
  - **Straddle**: long call + long put at the same K. It is a bet on a big move (high realized volatility vs implied).
  - **Strip** (1 call + 2 puts): a big move, more likely down.
  - **Strap** (2 calls + 1 put): a big move, more likely up.
  - **Strangle** (bottom vertical combination): long OTM put + long OTM call. It is cheaper and needs a bigger move.
  - The short versions (top straddle, write a strangle) bet on calm, with large losses in big moves.
- **Other payoffs**: a portfolio of butterflies with narrow strike spacing replicates any payoff. The limit is a state-contingent claim.

## Key Concepts
- **Bull/bear spread aggressiveness**: both OTM (aggressive, cheap) → one ITM / one OTM → both ITM (conservative).
- **Vertical spread**: same T, different K. **Horizontal spread**: same K, different T.
- **Break-even points**: where profit = 0, i.e. K ± premium for straddles.
- **Early exercise risk**: American options in box or bull spreads can be assigned early and break the payoff.

## Mental Models
- **Direction vs volatility grid**: bullish + low volatility → bull spread or covered call. Neutral + high volatility → long straddle or strangle. Neutral + low volatility → butterfly, calendar or short straddle.
- A straddle bets on **realized volatility exceeding what the market already prices**. Announced events (earnings) are already in the premium.
- Build and read any strategy with **parity**: covered call = short put + bond.

## Anti-patterns
- **Treating American options as European in box spreads**: a trader "arbitraged" a box spread on American options, got early exercise and lost (Business Snapshot 12.1).
- **Buying straddles before well-known events** assuming a big move is not priced in.
- **Short straddles/strangles without stop-losses**: tail losses are unlimited on the call side.

## Reference Tables
| Strategy | Legs | View | Max loss | Max gain |
|---|---|---|---|---|
| Bull call spread | +C(K₁) −C(K₂) | Moderately up | Net debit | K₂ − K₁ − debit |
| Bear put spread | +P(K₂) −P(K₁) | Moderately down | Net debit | K₂ − K₁ − debit |
| Butterfly | +C(K₁) −2C(K₂) +C(K₃) | Pin at K₂ | Net debit | K₂ − K₁ − debit |
| Long straddle | +C(K) +P(K) | Big move | c + p | Unlimited (up) |
| Long strangle | +P(K₁) +C(K₂) | Bigger move | Cheaper premium | Unlimited (up) |

## Worked Example
**Bull call spread (Example 12.2).** Buy a 3-month call K = 30 for $3 and sell a 3-month call K = 35 for $1. The net cost is $2.

| S_T | Payoff | Profit |
|---|---|---|
| ≤ 30 | 0 | −2 |
| 30–35 | S_T − 30 | S_T − 32 |
| ≥ 35 | 5 | +3 |

- Break-even at S_T = 32. The gain is capped at $3 and the loss at $2.

## Key Takeaways
1. Pick the strategy from the *pair* (direction view, volatility view).
2. Spreads cap both gain and loss. Combinations express volatility views.
3. A box spread must be worth (K₂ − K₁)e^{−rT}, but only with European options.
4. Butterflies replicate state prices, so any payoff can be built from options.
5. Always compute the cost, break-evens and worst case before entering.

## Connects To
- **Ch 11**: parity links covered calls and short puts.
- **Ch 19**: Greeks of multi-leg positions (gamma/vega of straddles).
- **Ch 20**: implied volatility and smiles determine the relative cost of wings.
- **Ch 26**: exotic payoffs built from vanilla components.
