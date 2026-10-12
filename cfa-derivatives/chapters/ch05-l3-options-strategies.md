# Chapter 5: Options Strategies
> **Source**: CFA Program Curriculum 2023, Level III, Reading 8 · Derivatives & Risk Management (Portfolio Management) | Adam Schwartz, PhD, CFA, and Barbara Valbuzzi, CFA

## Core Idea
Every option strategy is a trade on **three things at once**: the direction of the underlying (delta), the speed of movement (gamma, and the theta you pay or collect for it), and the market's pricing of future volatility (vega). Pick a strategy by stating both a **directional view** and a **view on implied volatility relative to consensus**, then choose the structure whose Greeks match. Expiration payoff diagrams give max gain, max loss and breakeven. The Greeks explain P&L *before* expiration, and that is where most positions are managed and closed.

## Learning Outcomes Covered
- Replicate asset returns with options (synthetic forwards, synthetic calls and puts, put–call(-forward) parity).
- Covered call and protective put: objectives, payoff, value and profit at expiration, max profit and loss, breakeven, risks.
- Compare the delta of a covered call and a protective put with long asset + short forward.
- Compare buying a call vs writing a put against a short underlying position.
- Bull spread, bear spread, straddle and collar: objectives, payoff, profit, max profit and loss, breakeven.
- Uses of calendar spreads.
- Volatility skew and smile, term structure of volatility, volatility surface.
- Select strategies consistent with an investment objective. Use options to target equity risk exposures.

## Frameworks Introduced
- **Position equivalencies (building blocks)**. All legs have the same underlying, strike and expiry. With the stock position entered at the strike price, the payoffs are identical at expiration:
  - Synthetic long forward = long call + short put. Market makers use it to hedge a short forward sold to a client.
  - Synthetic short forward = short call + long put. It replaces borrowing and shorting stock (beware **early assignment** on American options).
  - Synthetic long put = short stock + long call. It turns a symmetric short into an asymmetric bearish bet with capped loss.
  - Synthetic long call = long stock + long put, i.e. the **protective put**. Equivalently, long forward + long put.
  - Parity: `S₀ + p₀ = c₀ + X/(1 + r)^T`. Put–call–forward parity: `F₀(T)/(1 + r)^T + p₀ = c₀ + X/(1 + r)^T`.
- **Covered call** (long stock + short call). Three classic uses:
  1. **Yield enhancement**: write OTM calls to monetize a view that realized volatility will be *below* implied volatility. You sell the right tail of the distribution.
  2. **Reducing a position at a favorable price**: write ITM calls. If exercised, the effective sale price = X + c₀ > S₀, because you capture the time value.
  3. **Target price realization**: write calls struck at the analyst's target price and roll them if the target is not reached.
  - Risks: opportunity loss above X, full downside below S₀ − c₀, and **short gamma** (delta falls toward 0 as S rises through X).
- **Protective put** (long stock + long put) = insurance.
  - The strike is the coverage level and (S₀ − X) is the **deductible**. A lower strike is cheaper and leaves more loss before protection starts.
  - Choose the expiry so the put outlives the feared event. Longer puts cost more but lose less value per day (smaller |theta|).
  - Sell the put back once the risk has passed to recover time value and any volatility spike.
  - Rolling protective puts continuously is very expensive and erodes long-term return. Use them occasionally, for specific short-term risks.
- **Delta equivalence (LO d)**: an ATM covered call (+100 stock, −50 from short call), an ATM protective put (+100, −50 from long put) and long 100 stock/short 50 forward all have **position delta ≈ +50**. For small moves they behave alike. For large moves they diverge through gamma: covered call = short gamma, protective put = long gamma, forward hedge = zero gamma.
- **Cash-secured (fiduciary) put**: write a put and escrow X (PV of X for a European option). A bullish investor is "paid to wait" and gets an effective purchase price of X − p₀. It is economically close to a covered call, via parity: −p ≈ −c + S − PV(X).
- **Hedging a short stock position (LO e)**:

| Position | Upside (S rises) | Downside (S falls) | Greeks |
|---|---|---|---|
| Short stock + **long call** | loss capped at X − S₀ + c₀ | keeps the gain on the short, minus c₀ | delta −1 + Δc, long vega, pays theta |
| Short stock + **short put** | unlimited loss, cushioned only by p₀ | gain capped at S₀ − X + p₀ | delta −1 + |Δp|, short vega, earns theta |

- **Money spreads** (same expiry, different strikes):
  - **Bull spread**: buy the lower strike, sell the higher strike. With calls it is a *debit* spread; with puts, a *credit* spread.
  - **Bear spread**: buy the higher strike, sell the lower strike. With puts it is a *debit* spread; with calls, a *credit* spread.
  - Purpose: a directional bet that gives up the tail beyond the short strike in exchange for a lower cost.
  - With American options, prefer **bull call** and **bear put** spreads. In a bull put or bear call spread the short leg can be assigned early while the long leg is still OTM.
- **Refining spreads (legging)**:
  - Add a short leg to a winning long option to lock in a minimum profit. Example: long 40 call at 1.50, stock rises to 48, write the 50 call at 1.91. The profit is then ≥ 0.41 and ≤ 10.41. Only about 4% of the maximum profit is locked in.
  - Raise delta before expected up-moves (buy back the short leg) and cut it before expected pauses (re-sell it).
- **Straddle** (long call + long put, same X and T): a **long-volatility** position.
  - To profit, *realized* volatility must exceed the *implied* volatility already priced into both premiums.
  - Event-driven straddles are hard because consensus already bids implied volatility up before the event.
  - Short straddle: collect premium, short gamma and vega, long theta, unlimited risk.
  - A **strangle** uses different strikes, typically OTM put + OTM call.
- **Collar** (long stock + long OTM put X₁ + short OTM call X₂ > X₁), also called a fence or hedge wrapper:
  - A **zero-cost collar** sets X₂ so that c₀ = p₀. This is usually done OTC, since listed strikes rarely match premiums exactly.
  - Economically it sits *between* equity and a risk-free bond. Widen the strikes and it tends to the stock; narrow them to X₁ = X₂ and it becomes a synthetic T-bill (a conversion).
  - It is used on concentrated, low-tax-basis holdings the client will not sell. Rate version: a long floor financed by a short cap on a floating-rate portfolio.
- **Calendar (time) spread** (same type and strike, different expiries):
  - **Long calendar**: buy the long-dated option, sell the near-dated one. Net debit, positive theta (the short option decays faster), delta ≈ 0, **short gamma**, **long vega**. Best case: the underlying pins the strike until the near expiry, then implied volatility rises or the longer-term directional view plays out.
  - **Short calendar**: buy near-dated, sell long-dated. It profits from a **large move either way** or a *fall* in implied volatility.
- **Risk reversal** (long OTM call + short OTM put = long; the reverse = short), usually delta-hedged:
  - It trades the **skew**. Go long the risk reversal when put implied volatility looks too rich relative to call implied volatility. It can be built roughly vega-neutral.
  - Unhedged, a long risk reversal is a cheap bullish structure: the short put finances the call.
- **Strategy selection matrix (Exhibit 32)**. Always state both the direction and the implied-volatility view:

| Expected change in implied vol ↓ / Outlook → | Bearish | Neutral / range | Bullish |
|---|---|---|---|
| **Decrease** | Write calls | Write straddle | Write puts |
| **Unchanged** | Write calls + buy puts (collar-like) | Calendar spread | Buy calls + write puts (risk reversal) |
| **Increase** | Buy puts | Buy straddle | Buy calls |

## Key Concepts
- **Intrinsic (exercise) value / time value**: premium = time value + Max(0, S − X) for a call. Covered-call writers are harvesting time value.
- **Naked call / naked put**: writing a call without owning the underlying, or writing a put without escrowing cash for purchase.
- **Debit vs credit spread**: net premium paid (effectively long options) vs net premium received (effectively short). This is unrelated to fixed-income credit spreads.
- **Position delta**: the signed sum of deltas × quantities. It gives the equivalent share exposure for small moves.
- **Long/short volatility**: positions that gain or lose when volatility rises (net positive or negative vega and gamma).
- **Implied volatility**: the σ that equates the BSM price to the market price. It is the medium for comparing options across strikes, expiries and assets.
- **Realized (historical) volatility**: the annualized standard deviation of past returns.
- **Volatility smile**: OTM puts *and* OTM calls trade at higher implied volatility than ATM options (U shape).
- **Volatility skew**: implied volatility rises for OTM puts and falls for OTM calls as the strike moves away from spot. This is the dominant shape in equity indexes since 1987, driven by demand for portfolio insurance.
- **Skew measure**: IV(90% moneyness put) − IV(110% moneyness call), e.g. 3-month S&P 500 ≈ 8.3 vol points in the reading's snapshot.
- **Term structure of volatility**: usually upward sloping ("contango"). It **inverts** in stress, when short-dated implied volatility exceeds long-dated. A common indicator is the 12M−3M ATM implied-volatility spread.
- **Implied volatility surface**: implied volatility across strike *and* expiry. It would be flat under BSM, but in practice it is not.
- **VIX options**: priced off **VIX futures**, not spot VIX. Used to hedge equity tail risk via long volatility.
- **Early assignment risk**: an American short leg can be exercised against you before expiration.

## Formulas & Reference Tables
Notation: S₀ and S_T = underlying price at initiation and at expiration; X = strike (X_L < X_H; X₁ < X₂ for a collar); c₀ and p₀ = premiums; V_T = value at expiration; Π = profit.

**Payoff / breakeven / risk master table** (all verified numerically; examples use PBR at S₀ = 15.84 unless stated)

| Strategy | V_T | Max profit | Max loss | Breakeven | Worked example |
|---|---|---|---|---|---|
| Covered call | S_T − Max(0, S_T − X) | (X − S₀) + c₀ | S₀ − c₀ | S₀ − c₀ | NOV 17 call @1.44: +2.60 / −14.40 / BE 14.40 |
| Protective put | S_T + Max(0, X − S_T) | Unlimited | S₀ − X + p₀ | S₀ + p₀ | NOV 15 put @1.46: max loss 2.30, BE 17.30 |
| Short (cash-secured) put | −Max(0, X − S_T) (+ cash X) | p₀ | X − p₀ | X − p₀ | SEP 17 put @1.76: +1.76 / −15.24 / BE 15.24 |
| Bull call spread | Max(0, S_T − X_L) − Max(0, S_T − X_H) | (X_H − X_L) − (c_L − c_H) | c_L − c_H | X_L + (c_L − c_H) | SEP 15/17 (1.64/0.51): +0.87 / −1.13 / BE 16.13; SEP 16/17: +0.54 / −0.46 / BE 16.46 |
| Bear put spread | Max(0, X_H − S_T) − Max(0, X_L − S_T) | (X_H − X_L) − (p_H − p_L) | p_H − p_L | X_H − (p_H − p_L) | NOV 16/15 (1.96/1.46): +0.50 / −0.50 / BE 15.50 |
| Long straddle | \|S_T − X\| | Unlimited up; X − (c₀ + p₀) down | c₀ + p₀ | X ± (c₀ + p₀) | X = 50, 2.29 + 2.28: −4.57, BE 45.43 / 54.57 |
| Short straddle | −\|S_T − X\| | c₀ + p₀ | Unlimited | X ± (c₀ + p₀) | +4.57 at S_T = 50 |
| Collar (long S, +put X₁, −call X₂) | S_T + Max(0, X₁ − S_T) − Max(0, S_T − X₂) | X₂ − S₀ − p₀ + c₀ | S₀ − X₁ + p₀ − c₀ | S₀ + p₀ − c₀ | NOV 15/17 (1.46/1.44) from 15.84: +1.14 / −0.86 / BE 15.86; stock cost 12: profit locked in [2.98, 4.98] |
| Short stock + long call | (S₀ − S_T) + Max(0, S_T − X) | S₀ − c₀ | X − S₀ + c₀ | S₀ − c₀ | Short at 15.84 + SEP 16 call @0.97: max loss 1.13, BE 14.87 |
| Short stock + short put | (S₀ − S_T) − Max(0, X − S_T) | S₀ − X + p₀ | Unlimited | S₀ + p₀ | Short at 15.84 + SEP 15 put @0.65: max gain 1.49, BE 16.49 |
| Long calendar (same X; sell T₁, buy T₂) | At T₁: value of T₂ option − payoff of T₁ option | Largest when S_{T₁} ≈ X (and IV ↑) | ≈ Net debit (large move either way) | Model-dependent (no closed form) | XYZ 45 calls: pay 3.81, receive 1.55, debit 2.26; at SEP expiry S = 45 → JAN call 3.48, gain 1.22 |

Bear call and bull put spreads (credit spreads) have the same shapes. The initial cash flow is an inflow, the max gain equals the net credit, and the max loss equals the strike width minus the net credit.

**Greek profile of each strategy (long position, near-the-money)**
| Strategy | Delta | Gamma | Vega | Theta | Volatility stance |
|---|---|---|---|---|---|
| Covered call | + (1 − Δc) | − | − | + | short vol |
| Protective put | + (1 + Δp) | + | + | − | long vol |
| Collar | small + (1 + Δp − Δc) | ≈ 0 | ≈ 0 | ≈ 0 | reduces exposure toward bond-like |
| Short put | + | − | − | + | short vol |
| Bull call spread | + | ± (+ near X_L, − near X_H) | ± | ± | mainly directional |
| Long straddle | ≈ 0 | + (large) | + | − (large) | long vol |
| Long calendar | ≈ 0 | − | + | + | long vol / range-bound until T₁ |
| Long risk reversal | + | small | ≈ 0 (by design) | small | long call skew vs put skew |

PBR Greek arithmetic, verified:
- NOV 17 covered call delta = 1 − 0.475 = **0.525**.
- NOV 15 protective put delta = 1 − 0.359 = **0.641**.
- Collar delta = 1 − 0.359 − 0.475 = **0.166**, with gamma = 0.075 − 0.086 = **−0.011**.
- SEP 15/17 bull call: delta 0.306, gamma −0.034, theta −0.004/day.
- SEP 16/17 bull call: delta 0.165, gamma −0.003, theta −0.003/day.
- Straddle at 50: delta 0.069, gamma 0.139, vega 0.114 per vol point, theta −0.075/day.

**Greek approximations (all else equal)**
- `Δp ≈ Δ × ΔS`
- `Δ_new ≈ Δ + Γ × ΔS`
- `Δp ≈ Θ × Δt` (Θ quoted per day)
- `Δp ≈ ν × Δσ` (ν quoted per vol point)
- `Call delta − Put delta = 1` (same inputs, no dividends). ATM: call delta ≈ 0.5, put delta ≈ −0.5.

**Volatility conversions**
- The standard deviation of *daily* returns annualizes with `σ_annual = σ_daily × √252`.
- The volatility over a 21-trading-day horizon from an annual figure: `σ_21d = σ_annual × √(21/252)`. Conversely, `σ_annual = σ_21d × √(252/21)`.
- A straddle's implied breakeven move ≈ annualized IV × √(days/252). Example: DAX one-month IV of 9.29% → 9.29% × √(21/252) = **2.68%** move needed.

## Mental Models
- **Sell tails you don't need, buy tails you fear.**
  - A covered call sells the right tail.
  - A protective put buys the left tail.
  - A collar swaps one tail for the other.
  - A spread sells the far tail to cheapen the near bet.
- **Think "implied vs my forecast", not "up vs down".** A premium is a volatility forecast.
  - Buy options (straddles, calls, puts) when you think realized volatility will exceed implied.
  - Write them (covered calls, cash-secured puts, short straddles) when you think the opposite.
- **Theta is the rent on gamma.** Long-gamma positions (long options, straddles, protective puts) bleed daily and need movement. Short-gamma positions collect rent and lose on jumps.
- **Use skew in your favor.** Because OTM puts are rich:
  - Bear *put* spreads are cheap: you sell the expensive OTM put.
  - Collars are often near zero-cost or even net credit.
  - Selling puts to enter a stock pays better.
- **Choose the strike by "profit per unit of premium at your target".** Compute (target − breakeven)/premium for each candidate, and discard strikes whose breakeven lies beyond your target.

## Worked Example
**1. Strategy dashboard on PBR (S₀ = 15.84).**
- **Covered call**: long stock, write NOV 17 at 1.44.
  - Max gain = (17 − 15.84) + 1.44 = **2.60**.
  - Max loss = BE = 15.84 − 1.44 = **14.40**.
  - Position delta for 100 shares = 100 − 47.5 = **+52.5 shares-equivalent**.
- **Protective put**: long stock, buy NOV 15 at 1.46.
  - Max loss = 0.84 deductible + 1.46 premium = **2.30**.
  - BE = **17.30**.
  - Delta = **+64.1** per 100 shares.
  - Theta −0.009/day, i.e. about 0.009 of value lost per day if nothing moves.
- **Zero-cost-style collar**: NOV 15 put / NOV 17 call. The net premium is 0.02 debit.
  - From 15.84, the outcome is bounded in **[−0.86, +1.14]**.
  - For a holder whose basis is 12, the profit is locked in **[+2.98, +4.98]**.
- **Bull call SEP 15/17 vs SEP 16/17**:

| Spread | Cost | Max profit | Max loss | Breakeven | Move to BE | Delta |
|---|---|---|---|---|---|---|
| 15/17 | 1.13 | 0.87 | 1.13 | 16.13 | +1.8% | 0.306 |
| 16/17 | 0.46 | 0.54 | 0.46 | 16.46 | +3.9% | 0.165 |

  - The 15 call is bought at 64.4% implied volatility vs 55.9% for the 16 call. A volatility-aware investor may prefer 16/17.

**2. Straddle repricing around an event (MNZA, S = 169, 44 days).**
- Initial straddle: 170 call 6.45 + 170 put 7.69 = **14.14**.
  - Breakevens: **155.86 / 184.14**. The expected ±10% move (16.90) clears them.
  - Vega = 0.234 + 0.234 = 0.468 per vol point. Delta ≈ 0.504 − 0.494 = +0.01.
- News lifts implied volatility from about 30% to about 45%. The premiums become 10.20 + 10.89 = **21.09**.
  - Vega predicted: 15 × 0.468 = **+7.02**. Actual change: **+6.95**.
  - New breakevens: 148.91 / 191.09, i.e. moves of −11.9% / +13.1% from 169.
- Conclusion: **do not trade**. The "volatility event" is already priced. The trader's edge disappeared when consensus implied volatility caught up.

**3. Put calendar spread on Euro Stoxx 50 (spot 3,500; same implied volatility).**
- Sell the 3-month 3,500 put at €119, buy the 6-month at €173. Debit **€54**.
- At 3-month expiry:

| Scenario | Outcome |
|---|---|
| Index flat at 3,500 | Long put (now 3-month) worth €119 → **+€65** (maximum) |
| Index at 4,200 | Both puts ≈ 0 → **−€54** |
| Index at 3,000, IV unchanged | Pay €500 on the short; long put worth €515 → **−€39** |
| Index at 3,000, IV up | Long put worth €530 → **−€24** (vega helps) |

- A range-bound near term with a bearish long-term view is the textbook use: the spread cheapens a long-dated hedging put.

## Anti-patterns
- **Treating the covered-call premium as "free income"**: you have sold the right tail and kept the full left tail. The opportunity loss is real.
- **Rolling protective puts forever**: the cumulative premium destroys long-run return. Buy insurance for identified, temporary risks and sell it back once the risk passes.
- **Buying an event straddle after implied volatility has already jumped**: the breakevens widen, so you need realized > the new implied volatility, not > the old one.
- **Choosing the strike on premium alone**: the cheapest OTM option can have a breakeven beyond your target (e.g., a 70-strike call at 0.40 with a £70 target has BE £70.40).
- **Bull put or bear call spreads with American options when early assignment matters**: the short leg can be exercised while the long leg is still OTM.
- **Assuming equal delta means equal risk**: a covered call, a protective put and a stock/forward hedge share delta but have opposite gamma and vega.
- **Holding a long calendar through a big move**: it is short gamma, and a large move either way kills the time-value differential.
- **Using spot VIX to evaluate VIX options**: they are priced and settled off VIX **futures**.

## Exam Focus & Traps
- **Breakevens that are easy to mix up**:
  - Covered call BE = **S₀ − c₀** (not X + c₀). It equals the max loss.
  - Protective put BE = **S₀ + p₀** (not X + p₀).
  - Protective put max loss = **S₀ − X + p₀** (add the premium; don't subtract it).
  - Short put BE = max loss = **X − p₀**.
- **Spread construction**: bull = buy low strike, sell high strike. Bear = buy high strike, sell low strike. Call bull and put bear spreads are **debits**; put bull and call bear spreads are **credits**. Max loss of a debit spread = net debit. Max gain = strike width − net debit.
- **Bull call BE** = X_L + net debit. **Bear put BE** = X_H − net debit. For PSÔL 40/50 calls (6.50/4.25): max profit **7.75**, BE **42.25**.
- **Straddle BE** = X ± total premium. The worst outcome is S_T = X, where the total premium is lost. The long straddle wants *higher volatility, quickly*.
- **Collar**: the profit is flat below X₁ and above X₂. A zero-cost collar still has a cost: the forgone upside above X₂.
- **Position delta of written options**: short call adds −Δc; short put adds +|Δp|. Examples:
  - 50 short MNZA 170 calls on 5,000 shares: 5,000 × (1 − 0.504) = **+2,480**.
  - 500 short 165 puts: −500 × 100 × (−0.384) = **+19,200**.
- **Short stock hedges**: *buy a call* caps the loss and keeps the downside profit (long vega, pays theta). *Write a put* only cushions by the premium and caps the profit (short vega, earns theta).
- **Smile vs skew**: if only the put IVs rise as strikes move OTM while call IVs fall, it is a **skew**. A **smile** needs *both* wings elevated.
- **Calendar direction**: long calendar = sell near, buy far, with a flat outlook until the near expiry. Short calendar = buy near, sell far, expecting a big move or an IV drop. A call calendar with the strike above spot (e.g., sell Feb 80, buy Dec 80 with S ≈ 75) expresses a **bullish** view after the near expiry.
- **FX hedging**: a call on the foreign currency = a put on the domestic currency.
  - To protect a future USD purchase with BRL, buy a USD call, i.e. a BRL put (or go long BRL/USD futures to buy USD). Selling calls or shorting futures does the opposite.
  - Reiter's €1m purchase: the call at US$1.25 plus US$0.02 premium caps the cost at **US$1,270,000**.
- **Realized vol** uses √252 (daily) and √12 or √(252/21) (monthly). Match the scaling to the return frequency.
- **⚠ Correction**: the reading's Eq. 13 annualizes "the standard deviation of daily percentage changes over a month" by × √(252/21). The correct factor for a daily-return standard deviation is **× √252**. The factor √(252/21) = √12 applies only to a volatility measured over a 21-day (monthly) horizon.
- **⚠ Correction**: in the practice solution on the Walnut 67.50 straddle, the cost is 1.99 + 2.26 = **4.25**. The breakevens are therefore **63.25 / 71.75** (the source switches to 4.26 → 63.24 / 71.76). The answer choice is unaffected.

## Key Takeaways
1. Know the equivalences: call − put = forward, stock + put = call, stock − call ≈ −put. They let you build, hedge or cheapen any exposure synthetically.
2. For each strategy, memorize V_T, max gain, max loss and breakeven (master table). Then reason with the Greeks for pre-expiry P&L.
3. Covered calls and short puts are short volatility (sell the right tail or collect the put premium). Protective puts and straddles are long volatility. Collars neutralize most of both.
4. Spreads trade profit potential for cost. Choose strikes by breakeven vs target and by profit per unit of premium, and use the skew to sell the rich wing.
5. Calendars exploit faster time decay of the near option. They are long vega and short gamma, so they need a quiet near term.
6. Implied volatility, skew and term structure encode fear and demand. Compare them with your own forecast (and with realized volatility) before buying or selling optionality.
7. Always set the objective first: direction + volatility view + horizon → strategy (Exhibit 32 matrix).

## Connects To
- **ch02**: L1 put–call parity, forward parity and option payoff basics, the foundation of all synthetic positions here.
- **ch04**: BSM and the Greeks: the delta, gamma, vega and theta numbers used to analyze each strategy, plus implied volatility.
- **ch06**: forwards, futures and swaps strategies. Alternatives to options for changing equity exposure (symmetric vs asymmetric payoffs).
- **ch07**: currency management. FX options, collars, risk reversals and seagulls for currency hedging.
- **`hull-derivatives` ch19**: Greek letters and hedging mechanics behind strategy risk management.
- **`hull-derivatives` ch20**: volatility smiles and skews, the empirical surface discussed here.
- **`passarelli-option-greeks` ch02**: a trader's framing of delta, gamma, theta and vega.
- **`passarelli-option-greeks` ch05**: volatility-selling strategies (covered calls, cash-secured puts).
- **`passarelli-option-greeks` ch06**: put–call parity and synthetics.
- **`passarelli-option-greeks` ch09**: vertical spreads (bull and bear spreads) in depth.
- **`passarelli-option-greeks` ch10**: wing spreads (butterflies, condors) extending the spread logic.
- **`passarelli-option-greeks` ch11**: calendar and diagonal spreads.
- **`passarelli-option-greeks` ch12–ch13**: delta-neutral trading of implied and realized volatility (risk-reversal and straddle hedging).
- **`passarelli-option-greeks` ch14**: volatility charts, reading IV vs realized volatility.
- **`passarelli-option-greeks` ch15**: straddles and strangles.
- **`passarelli-option-greeks` ch16**: ratio and complex spreads.
