# Chapter 2: Basics of Derivative Pricing and Valuation
> **Source**: CFA Program Curriculum 2020, Level I, Reading 49 · Derivatives | Don M. Chance, PhD, CFA

## Core Idea
Derivatives are priced by **replication and no-arbitrage**, not by discounting expected payoffs at a risky rate:
1. Combine the derivative with its underlying into a riskless position.
2. Force that position to earn the risk-free rate.
3. Read off the unique price.

Because the risk premium is already embedded in the spot price, investor risk aversion drops out. You can price *as if* everyone were risk neutral, discounting risk-neutral expected payoffs at r. The same logic gives you:
- the forward price (spot compounded at r, adjusted for carry);
- the value of a forward commitment mid-life (spot minus the PV of the locked-in price);
- put–call(–forward) parity;
- option bounds;
- the one-period binomial model.

## Learning Outcomes Covered
- Explain arbitrage, replication and risk neutrality in derivative pricing.
- Distinguish **value** from **price** for forwards, futures and swaps.
- Calculate a forward price with zero, positive or negative net cost of carry.
- Explain forward value/price at initiation, during the life of the contract and at expiration.
- Describe monetary and non-monetary benefits and costs of holding the underlying and their effect on forwards.
- Define an FRA and describe its uses.
- Explain why forward and futures prices differ.
- Explain how swaps are similar to, and different from, a series of forwards. Distinguish swap value from swap price.
- Explain exercise value, time value and moneyness. Identify the factors that drive option value and the direction of each effect.
- Explain put–call parity and put–call–forward parity.
- Value an option with a one-period binomial model.
- Explain when European and American option values differ.

## Frameworks Introduced
- **Pricing the underlying (the starting point)**:
  - `S₀ = E(S_T)/(1 + r + λ)^T − θ + γ`, where r is the risk-free rate, λ the risk premium, θ the PV of carrying costs and γ the PV of benefits (dividends, coupons, foreign interest, convenience yield).
  - Costs lower today's price. Benefits raise it.
  - Risk aversion (λ > 0) lowers the price of risky assets.
- **Arbitrage → replication → risk-neutral pricing chain**:
  1. *Arbitrage*: identical payoffs must carry identical prices (the law of one price). Buy the cheap side, sell the dear side, and lock in a riskless inflow with no capital.
  2. *Hedge*: long asset + short derivative (sized correctly) is riskless, so it must earn r.
  3. *Replication identities* (rearrange the hedge):
     - asset − derivative = risk-free bond;
     - asset − bond (borrowing) = derivative;
     - −derivative − bond = −asset.
     Use them to create synthetic positions when they are cheaper (e.g. index futures + T-bills = a synthetic index fund).
  4. *Risk neutrality*: since λ never enters the derivative price, discount **risk-neutral** expected payoffs at r. This does not assume investors are risk neutral. It only uses the fact that their risk aversion is irrelevant once the hedge exists.
  - Failure modes (**limits to arbitrage**): transaction costs larger than the mispricing, capital and funding constraints (interim cash outflows vs paper gains), model-input uncertainty (volatility for options) and short-sale constraints. The last can make arbitrage one-directional, which is common in commodities.
- **Price vs value (forward commitments)**:
  - The **price** (F₀(T), the swap rate, the futures price) is a contract term fixed at inception.
  - The **value** starts at 0 and moves with the market.
  - They are different quantities on different scales (a 100 price vs a −5.85 value) and are never compared to decide whether to trade.
  - For options, price = value = the premium.
- **Forward valuation over the life of the contract**:
  - At initiation, `V₀ = 0`, which pins down `F₀(T)`.
  - During the life, `V_t = S_t − PV_t(benefits) + PV_t(costs) − F₀(T)/(1 + r)^(T−t)`.
  - At expiration, `V_T = S_T − F₀(T)`.
  - Equivalent method: value = PV of (new forward price at t − original forward price), which is the offsetting-contract approach.
- **Swap = a series of off-market forwards**:
  - Each implied forward has its own zero-value price F₀(t_i), and these differ by maturity. The swap instead uses **one fixed price for every date**.
  - Some embedded forwards therefore have positive value and some negative, and the swap fixed rate is the single price that makes their **sum** zero.
  - Replicate a pay-fixed swap as: buy a floating-rate asset, financed by fixed-payment borrowing.
- **Six drivers of European option value**:
  - Direction of each effect: see the table below.
  - The asymmetric payoff makes **volatility always valuable**. Being "more dead" out of the money costs nothing, while being deeper in the money pays more.
- **Put–call parity (no carry)**: `S₀ + p₀ = c₀ + X/(1 + r)^T`.
  - Protective put = fiduciary call. Both pay max(S_T, X).
  - Any term can be synthesized from the other three.
  - If the two sides differ, sell the expensive side and buy the cheap side.
- **One-period binomial model**:
  1. Choose h shares per short call so that the portfolio is riskless.
  2. The portfolio then earns r.
  3. Solve for c₀.
  - Result: risk-neutral probability π, value = π-weighted payoff discounted at r. The true probability q does not appear.
- **American vs European**:
  - The right to exercise early is worth ≥ 0, so `C₀ ≥ c₀` and `P₀ ≥ p₀`.
  - **Calls on non-paying underlyings are never exercised early**: `c₀ ≥ S₀ − PV(X) > S₀ − X`, so the call is worth more alive than exercised, and `C₀ = c₀`. Only cash payouts (dividends, coupons) can justify exercising a call early, just before the ex-date.
  - **Puts can be optimally exercised early** when deep in the money: the gain is capped at X, and waiting delays receipt of X. Dividends *discourage* early exercise of a put (wait until after the ex-date). Carrying costs discourage early exercise of a call and encourage it for a put.

## Key Concepts
- **Holding period / expected spot price E(S_T)**: the investor's forecast. It drives the price of the underlying, never the forward price directly.
- **Risk-averse / risk-neutral / risk-seeking investors**: they require λ > 0, λ = 0 and λ < 0 (theoretical only) respectively.
- **Convenience yield**: a non-monetary benefit of holding a commodity when supply is tight or shorting is hard. It can put spot above the expected future spot price.
- **Carry (cost of carry)**: the net of the costs (storage, insurance) and benefits (income, convenience yield) of holding the asset, plus the opportunity cost of funds.
- **Arbitrage-free pricing / principle of no arbitrage**: the derivative price is inferred as the one that rules out riskless profit.
- **Off-market forward**: a forward struck at a price other than the zero-value price. One side pays the PV difference up front.
- **Forward rate agreement (FRA)**:
  - A forward on an interest rate (Libor, Euribor, Tibor), cash-settled at expiration on the discounted rate difference × notional.
  - The **long (a future borrower)** pays the fixed FRA rate and receives the floating rate, so it hedges *rising* rates. The short (a future lender) hedges falling rates.
  - The FRA rate is the **forward rate** implied by the term structure.
- **Synthetic FRA**: a "30-day FRA on 90-day Libor" (1×4 in months) = long a 120-day Eurodollar deposit + short a 30-day deposit.
- **Futures value**: the gain or loss accumulated since the last settlement. It resets to zero at each daily mark-to-market.
- **Exercise value (intrinsic value)**: max(0, S − X) for a call and max(0, X − S) for a put.
- **Time value (of an option)**: price − exercise value. It rises with volatility and time and **decays to zero** at expiration (time value decay). Do not confuse it with the time value of money.
- **Moneyness**: in, at or out of the money. At the money is treated as out of the money for payoffs.
- **Protective put**: long asset + long put. **Fiduciary call**: long call + risk-free zero-coupon bond with face value X.
- **Risk-neutral (synthetic, pseudo) probabilities π, 1 − π**: weights that make the discounted expected payoff equal the arbitrage-free value.
- **Hedge ratio h**: the number of units of the underlying per short call that makes the portfolio riskless.

## Formulas & Reference Tables
**Notation**: S₀, S_t, S_T are spot prices at 0, t, T. r is the periodic risk-free rate (discrete compounding). γ and θ are the PV of benefits and costs. F₀(T) is the forward price set at 0 for delivery at T. V_t(T) is the value to the long at t.

**Forwards**
- No carry: `F₀(T) = S₀(1 + r)^T`.
- With carry: `F₀(T) = (S₀ − γ + θ)(1 + r)^T = S₀(1 + r)^T − (γ − θ)(1 + r)^T`.
- Value at initiation: `V₀(T) = 0`.
- Value during the life: `V_t(T) = S_t − (γ − θ)(1 + r)^t − F₀(T)(1 + r)^−(T−t)`.
- Value at expiration: `V_T(T) = S_T − F₀(T)`. The short's value is the negative.
- Net-carry cases:

| Net carry | Condition | Effect on F₀ |
|---|---|---|
| Zero | γ = θ | `F₀ = S₀(1 + r)^T` |
| Positive benefits | γ > θ (e.g. dividend stock, coupon bond) | F₀ is lower than the zero-carry price |
| Net costs | θ > γ (e.g. storable commodity) | F₀ is higher than the zero-carry price |

⚠ **Correction / precision**: in the CFA's mid-life formula, γ and θ are PVs as of time 0 compounded to t. The formula is correct only if **no benefit or cost has been paid between 0 and t**. The robust version uses the PV at t of the benefits and costs **remaining** over (t, T]: `V_t = S_t − PV_t(remaining benefits) + PV_t(remaining costs) − F₀(T)/(1 + r)^(T−t)`.

**Futures vs forwards**

| Correlation of futures price with interest rates | Preferred by longs | Price relation |
|---|---|---|
| Zero, or rates constant/deterministic | Indifferent | Futures = Forward |
| Positive (gains reinvested at high rates, losses financed at low rates) | Futures | Futures > Forward |
| Negative | Forwards | Futures < Forward |

In practice the industry treats futures and forward prices as equal, and the difference grows with interest-rate volatility.

**Swaps**
- Cash flow to the fixed payer at each date i: `S_i − FS₀(n, T)`.
- Price condition: `Σ PV[S_i − FS₀] = 0`, which is equivalent to "the sum of the off-market forward values = 0".
- The interest rate swap fixed rate from discount factors: `s = (1 − DF_n)/Σ DF_i` (per period, per unit of notional).
- Value to the fixed payer at t (remaining dates j): `V = N × [(1 − DF_n) − s₀ × Σ DF_j] = N × (s_t − s₀) × Σ DF_j`, where s_t is the current par swap rate for the remaining term. The first form applies on a reset date. Between dates, the floating leg is worth (N + next known coupon) discounted to the next reset.

**Options** (c/p European, C/P American, X strike)
- Payoffs: `c_T = max(0, S_T − X)`, `p_T = max(0, X − S_T)`.
- Lower bounds, European and American call: `c₀ ≥ max[0, S₀ − X/(1 + r)^T]`, and `C₀` has the same lower bound.
- Lower bound, European put: `p₀ ≥ max[0, X/(1 + r)^T − S₀]`.
- Lower bound, American put: `P₀ ≥ max(0, X − S₀)`.
- Upper bounds: `c₀ ≤ S₀` and `p₀ ≤ X/(1 + r)^T` (European).
- Put–call parity: `S₀ + p₀ = c₀ + X/(1 + r)^T`.
- Put–call–forward parity: `F₀(T)/(1 + r)^T + p₀ = c₀ + X/(1 + r)^T`, equivalently `p₀ − c₀ = [X − F₀(T)]/(1 + r)^T`.
- Binomial model:
  - Up and down factors: `u = S₁⁺/S₀`, `d = S₁⁻/S₀`.
  - Hedge ratio: `h = (c₁⁺ − c₁⁻)/(S₁⁺ − S₁⁻)`.
  - Risk-neutral probability: `π = (1 + r − d)/(u − d)`, which requires d < 1 + r < u (otherwise arbitrage).
  - Values: `c₀ = [πc₁⁺ + (1 − π)c₁⁻]/(1 + r)` and `p₀ = [πp₁⁺ + (1 − π)p₁⁻]/(1 + r)`.

**Synthetics from put–call parity** (+ = long, − = short)

| Target | Replicate with |
|---|---|
| Long put | long call + short asset + long bond PV(X) |
| Long call | long put + long asset + short bond (borrow PV(X)) |
| Long asset | long call + short put + long bond |
| Long bond PV(X) | long asset + long put + short call (a riskless **conversion**) |
| Synthetic asset | long forward + long bond with face F₀(T) |

**Factors affecting European option values** (↑ = the factor increases)

| Factor ↑ | Call | Put | Why |
|---|---|---|---|
| Underlying price S | ↑ | ↓ | The call is a way to buy, the put a way to sell |
| Exercise price X | ↓ | ↑ | Hurdle effect. The put's maximum value is PV(X) |
| Time to expiration T | ↑ | ↑ usually, ↓ possible | More time for favourable moves. For a put, receipt of X is delayed (the effect dominates when the put is deep ITM, rates are high and T is long) |
| Risk-free rate r | ↑ | ↓ | The call defers paying X. The put defers receiving X |
| Volatility σ | ↑ | ↑ | Asymmetric payoff: the downside is floored at 0 |
| Benefits (dividends, coupons) | ↓ | ↑ | Payouts lower S and do not accrue to option holders |
| Carrying costs | ↑ | ↓ | The call avoids the costs of owning. Short sellers benefit from them |

**Early exercise (American)**

| | No payouts on underlying | Dividends/coupons | Carrying costs |
|---|---|---|---|
| Call | Never early: C₀ = c₀ | May exercise just before ex-date | Discourage early exercise |
| Put | May be optimal when deep ITM: P₀ > p₀ | Discourage (wait until after payment) | Encourage |

## Mental Models
- **The spot market prices risk and the derivatives market inherits it.** Never put λ into a derivative formula. If you are estimating a risk premium to price a forward, you have made a mistake.
- **Think of a long forward as a synthetic purchase with deferred payment**: you get the asset's price moves without paying S₀ today, so you earn interest on S₀ (F is higher) but give up its income (F is lower).
- **Value of a forward commitment = what you get minus the PV of what you promised.** For a forward that is S_t minus PV(F₀). For a swap it is PV(receive leg) minus PV(pay leg). The same template covers FRAs, swaps and futures (where the daily reset makes value zero after each settlement).
- **Put–call parity is a Lego set.** Four instruments, any three build the fourth. Use it to spot mispricing, to create synthetics (conversions and reversals) and to sanity-check model outputs: c − p must equal S − PV(X).
- **In the binomial model, volatility is the spread u − d.** The real-world probability of an up move is irrelevant because the hedge removes it.

## Worked Example
**1. Forward price and mid-life value (from the reading, recomputed).**
- Pricing: S₀ = £50, r = 3%, T = 0.25.
  - F₀ = 50 × 1.03^0.25 = **£50.37**.
  - With γ = £3 and θ = £4: F₀ = 50 × 1.03^0.25 − (3 − 4) × 1.03^0.25 = **£51.38**. Net costs raise the forward price.
- Valuation after one month (S = £52, T − t = 2/12):
  - No carry: V = 52 − 50.37 × 1.03^−0.1667 = **£1.88**.
  - With carry: V = 52 − (3 − 4) × 1.03^0.0833 − 51.38 × 1.03^−0.1667 = **£1.87** (the reading rounds to 1.88).
- Short-forward check: you own a stock worth $102 and are short a forward at $100 (1 year, r = 4%). The position is riskless, worth 100/1.04 = $96.15. Forward value to the short = 96.15 − 102 = **−$5.85** (+$5.85 to the long). The price is still $100.

**2. Forward valuation mid-life with a discrete dividend (extension, verified).**
- Inputs: S₀ = 100, r = 5%, T = 1 year, dividend of 2 at t = 0.5.
- Pricing:
  - PV(D) = 2/1.05^0.5 = 1.9518.
  - F₀ = (100 − 1.9518) × 1.05 = **102.9506**.
- Valuation at t = 0.25 with S_t = 108:
  - PV_t(D) = 2/1.05^0.25 = 1.9758.
  - V_t = 108 − 1.9758 − 102.9506/1.05^0.75 = **+6.7728** to the long.
- Cross-check by offsetting:
  - New forward price F_t = (108 − 1.9758) × 1.05^0.75 = 109.9758.
  - (109.9758 − 102.9506)/1.05^0.75 = **6.7728** ✓.

**3. Interest rate swap: price at inception, value one year later (extension, verified).**
- Pricing: 3-year annual pay-fixed swap, N = 10m, spot rates 2.0% / 2.5% / 3.0%.
  - DF = 0.980392, 0.951814, 0.915142.
  - s₀ = (1 − 0.915142)/2.847348 = **2.9803%**.
- Valuation one year later, just after the first exchange (remaining spot rates 1y 3.0%, 2y 3.5%):
  - DF = 0.970874, 0.933511.
  - V(pay-fixed) = 10m × [(1 − 0.933511) − 0.029803 × 1.904385] = **+$97,337**.
  - Check: the new par rate is 3.4914%, so 10m × (0.034914 − 0.029803) × 1.904385 = $97,337 ✓.
- Interpretation: rates rose, so the fixed payer (who locked in 2.98%) gains.

**4. Currency swap, fixed-for-fixed (extension, verified).**
- Pricing at inception: spot 1.10 USD/EUR, notionals EUR 10m ↔ USD 11m, 2-year annual.
  - Par rates from the curves (EUR 1.5% / 2.0%, USD 3.0% / 3.5%): EUR **1.9950%**, USD **3.4914%**.
  - Both legs are worth par at inception, so the value is 0.
- Valuation one year later, after the first exchange (1y rates EUR 2.5%, USD 3.2%; spot 1.15):
  - PV(EUR leg) = 10m × 1.019950/1.025 = EUR 9,950,735.
  - PV(USD leg) = 11m × 1.034914/1.032 = USD 11,031,058.
  - Value to the party receiving EUR and paying USD = 1.15 × 9,950,735 − 11,031,058 = **+USD 412,288**.
- Interpretation: the gain comes mostly from EUR appreciation (1.10 → 1.15).

**5. Equity swap: receive index return, pay fixed (extension, verified).**
- Setup: N = 10m, 2-year annual, fixed = 3.4914% (the USD par rate). At t = 0.5 the index has gone from 1,000 to 1,040 (total-return index, last reset at 0). Spot rates: 0.5y 3.3%, 1.5y 3.6%.
- Equity leg + notional at maturity = N × S_t/S_reset = 10m × 1.04 = 10,400,000.
- Fixed leg + notional = 10m × [0.034914/1.033^0.5 + 1.034914/1.036^1.5] = 10,157,934.
- Value to the equity receiver = **+$242,066**.
- Note the asymmetry: the equity leg is valued off the **last reset**, not the inception price.

**6. Options (from the reading, recomputed).**
- Lower bounds, with X = €60, r = 4%, T = 0.75:
  - S₀ = €70: European call ≥ **€11.74** and European put ≥ 0. The American call has the same bound, €11.74, which is above the €10 exercise value.
  - S₀ = €50: European put ≥ **€8.26**. The American put ≥ €10 (its exercise value).
- Put–call parity with X = ¥100,000, S₀ = ¥90,000, r = 2%, T = 2/12:
  - p₀ − c₀ = 100,000/1.02^0.1667 − 90,000 = **¥9,670**. If c₀ = ¥5,000, then p₀ = ¥14,670.
  - Via the forward: F₀ = 90,000 × 1.02^0.1667 = ¥90,298, and (100,000 − 90,298)/1.02^0.1667 = **¥9,670** ✓.
- Binomial: S₀ = £40, u = 1.20, d = 0.75, r = 5%, X = £38.
  - Terminal prices S⁺ = 48 and S⁻ = 30. Call payoffs c⁺ = 10, c⁻ = 0. Put payoffs p⁺ = 0, p⁻ = 8.
  - π = (1.05 − 0.75)/0.45 = **0.6667**.
  - c₀ = 0.6667 × 10/1.05 = **£6.35**. p₀ = 0.3333 × 8/1.05 = **£2.54**.
  - Hedge: h = 10/18 = 0.5556 share per short call. The portfolio is worth 16.67 in both states, which equals (0.5556 × 40 − 6.35) × 1.05 ✓.
  - Parity check: c − p = 3.81 = 40 − 38/1.05 ✓.

## Anti-patterns
- **Discounting a derivative's real-world expected payoff at r + λ**: this double-counts risk. Use risk-neutral probabilities and r.
- **Comparing the forward price with the forward value** to decide whether a contract is "cheap": they are different objects.
- **Setting the forward price equal to the expected future spot price**: F₀ reflects carry, not a forecast.
- **Using the true probability q in the binomial model**: only π matters.
- **Assuming a longer maturity always raises put value**: deep ITM European puts with high r can lose value with time.
- **Exercising an American call early on a non-dividend stock** "because the stock has peaked": selling the call dominates exercising it.
- **Treating put–call parity as "put = call"**: parity links them through S and PV(X). It is independent of volatility.
- **Treating the swap's implied forwards as at-market**: each is off-market. Only their sum has zero value.

## Exam Focus & Traps
- **Which factor does NOT affect the forward price?** The investor's risk attitude, the expected spot price and past prices paid.
- **Value at expiration** = S_T − F₀(T), not S_T − compounded F₀.
- **The mid-life formula discounts F₀, not S_t**: `V_t = S_t − F₀/(1 + r)^(T−t)`. Watch the (T − t) exponent.
- **Carry signs**: benefits (γ) reduce F₀, costs (θ) increase it. In the mid-life formula, benefits reduce the long's value and avoided costs increase it.
- **Conditions under which futures = forward prices**: constant rates, or zero correlation between futures prices and rates. Differences in "volatility of the forward vs the futures price" are a distractor.
- **Futures value** = accumulated gain since the last settlement, which is zero right after the mark-to-market.
- **An FRA rate is a forward rate**, not a spot rate or a zero-coupon rate.
- **Minimum value vs exercise value**: the minimum value uses PV(X), the exercise value uses X. The American call minimum is the European one (S − PV(X)). The American put minimum is the exercise value (X − S).
- **Riskless combinations from parity**: long asset + long put + short call (conversion) pays X for sure.
- **The only reason to exercise an American call early is a cash payout** on the underlying, and even then it is a necessary, not a sufficient, condition. Dividends make early exercise of a put *less* likely.
- **In the binomial model, volatility is represented by u − d**, not by σ directly.

## Key Takeaways
1. Price derivatives by building a riskless hedge and forcing it to earn r. Risk aversion and expected returns drop out.
2. `F₀(T) = (S₀ − γ + θ)(1 + r)^T`. Benefits lower the forward price and costs raise it. The value at inception is zero.
3. `V_t = S_t − PV(remaining carry net) − F₀/(1 + r)^(T−t)`, and at T `V_T = S_T − F₀`. Price is a fixed term; value moves.
4. A swap is a strip of off-market forwards sharing one fixed price. Value any swap as PV(receive leg) − PV(pay leg). For an interest rate swap, `V = N(s_t − s₀)ΣDF`.
5. Option value rises with σ and with benefits for puts / costs for calls, and moves with S, X, r and T as shown in the table. Time value decays to zero.
6. Put–call parity `S + p = c + PV(X)` and put–call–forward parity `PV(F) + p = c + PV(X)` hold by arbitrage.
7. Binomial model: `π = (1 + r − d)/(u − d)` and `c₀ = E_π[payoff]/(1 + r)`.
8. American calls on non-payers equal European calls. American puts carry an early-exercise premium.

## Connects To
- **ch01**: definitions, payoff diagrams and the first arbitrage examples.
- **ch03**: full Level II treatment of forward, FRA, futures, interest rate, currency and equity swap valuation.
- **ch04**: multi-period binomial trees, BSM, Black's model and the Greeks.
- **`cfa-fixed-income` ch03 / ch07**: spot and forward rates and discount factors used for FRA and swap pricing.
- **`hull-derivatives` ch05** (forward and futures prices, cost of carry). **ch07** (swaps). **ch11** (properties of stock options, bounds and parity). **ch13** (binomial trees).
- **`tuckman-fixed-income` ch13** (forwards and futures preliminaries, the futures–forward difference). **ch16** (swaps).
