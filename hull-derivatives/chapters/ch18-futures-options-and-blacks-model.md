# Chapter 18: Futures Options and Black's Model

## Core Idea
A futures price behaves like a stock with dividend yield q = r (it has zero drift in a risk-neutral world). European futures options are priced with Black's model. When option and futures expire together, a European futures option equals the European spot option, so Black's model is widely used for spot options too.

## Frameworks Introduced
- **Futures option payoffs**:
  - Exercising a call gives a long futures position + cash (F − K).
  - Exercising a put gives a short futures position + cash (K − F).
- **Why futures options are popular**: futures are more liquid and easier to price-discover than spot. They avoid physical delivery and settle in cash plus a futures position. Commissions are lower.
- **Put–call parity (European futures options)**: `c + Ke^{−rT} = p + F₀e^{−rT}`.
- **Bounds**: `c ≥ (F₀ − K)e^{−rT}` and `p ≥ (K − F₀)e^{−rT}`. American futures calls may be exercised early (deep ITM).
- **Risk-neutral drift of F**: zero. The futures price is a martingale under the risk-neutral measure.
- **Black's model (1976)**:
  - `c = e^{−rT}[F₀N(d₁) − KN(d₂)]` and `p = e^{−rT}[KN(−d₂) − F₀N(−d₁)]`.
  - `d₁ = [ln(F₀/K) + σ²T/2]/(σ√T)`.
- **Black for spot options**: with F₀ = the forward/futures price for maturity T, Black values the European spot option. There is no need to estimate q or storage costs.
- **Trees for futures**: p = (1 − d)/(u − d). Futures cost nothing to enter, so a = 1.
- **American futures vs spot options**:
  - Normal (contango) market: the American futures call > the American spot call, and the American futures put < the American spot put.
  - The reverse holds in an inverted market.

## Key Concepts
- **Options on futures on interest rates, commodities, indices and currencies**.
- **Futures-style options**: the option premium itself is marked to market daily. Its value then equals the expected payoff with no discounting.
- **Serial options**: options expiring before the nearest futures on that underlying.

## Mental Models
- **"Futures = stock with q = r"**: every Chapter 17 result applies with S₀ → F₀, q → r.
- Use **Black whenever you have a clean forward price**. It sidesteps dividend, storage and convenience-yield estimation.
- **Deep ITM American futures calls** can be worth exercising: you get the cash now and earn interest.

## Anti-patterns
- **Assuming American futures options = American spot options**: they differ unless the futures curve is flat.
- **Using spot volatility for futures options** when the futures and spot volatilities differ (commodities with mean reversion).

## Worked Example
**Black put (Example 18.6).** A 4-month European put on commodity futures: F₀ = K = 20, r = 9%, σ = 25%.
- ln(F/K) = 0, so d₁ = σ√T/2 = 0.07216 and d₂ = −0.07216.
- N(−d₁) = 0.4712 and N(−d₂) = 0.5288.
- p = e^{−0.09/3}[20 × 0.5288 − 20 × 0.4712] = **$1.12**.

## Key Takeaways
1. A futures price has zero risk-neutral drift, so treat it as a stock yielding r.
2. Black: c = e^{−rT}[F₀N(d₁) − KN(d₂)].
3. The European futures option equals the European spot option when maturities coincide. Use Black for spot too.
4. Parity: c + Ke^{−rT} = p + F₀e^{−rT}.
5. Futures trees use p = (1 − d)/(u − d). American futures options may be exercised early.

## Connects To
- **Ch 5**: futures prices and cost of carry.
- **Ch 17**: the known-yield extension.
- **Ch 28**: the forward measure and why Black works for rates.
- **Ch 29**: Black's model for caps, swaptions and bond options.
- **Ch 35**: commodity futures options.
