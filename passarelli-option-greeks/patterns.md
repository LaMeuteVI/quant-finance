# Patterns — Passarelli, Trading Option Greeks

## Daily Greek P&L Attribution
**When to use**: every day, for every position, and post-trade to explain the result.
**How**: 1) Per share: `ΔV ≈ Δ·ΔS + ½Γ·ΔS² + θ·days + vega·ΔIV(pts) + ρ·Δr(pts)`. 2) Multiply by `contracts × 100`. 3) Compare with the full revaluation. 4) Investigate any gap above 10–20%.
**Trade-offs**: constant-gamma assumption fails on large moves; greeks are model values. (ch02, ch12)

## Expected-Move Ladder (rule of 16)
**When to use**: sizing strikes, stops, hedge triggers; asking whether the options price a move you believe.
**How**: 1) 1-day σ = IV/16. 2) n trading days: σ = (IV/16)√n. 3) Dollar range ≈ `S × (1 ± σ)` (68%). 4) Use trading days, not calendar days. 5) Compare with the HV of the stock.
**Trade-offs**: normal approximation; ignores drift and skew; √256 vs √252 is a rounding choice. (ch03, ch10)

## Strike and Expiry Choice by Greek Priority
**When to use**: buying a call or put for a directional view.
**How**: 1) Rank greeks by thesis (long: delta, theta, vega, gamma, rho). 2) ITM = stock substitute; ATM = max Γ, θ, vega; OTM = magnitude bet. 3) Build a price-time matrix. 4) Average daily theta `= (V_now − V_exit at same S) / days held`. 5) Exit before the final 2–3 weeks.
**Trade-offs**: OTM wins big but expires worthless ~5 times in 6; ATM pays the highest rent. (ch04)

## Pain-Point Stop on a Short Option
**When to use**: any naked call, naked put, covered call or put.
**How**: 1) Choose the exit option price. 2) Use the offer when covering a short. 3) `ΔV = exit − current`. 4) `ΔS = ΔV / (|Δ| + Γ/2)`. 5) Add vega: adverse moves raise IV. 6) Re-test daily with Would I Do It Now?
**Trade-offs**: wide spreads and gaps defeat tight stops; the double whammy hits short puts hardest. (ch05)

## Covered Call Month and Strike Grid
**When to use**: choosing among call writes against owned stock.
**How**: 1) Compute theta/day, IV, net delta `1 − Δcall`, break-even `S₀ − premium`, indifference point `K + premium` for each candidate. 2) Neutral view: favor theta and lower IV. 3) Compare static return `(premium/S) × 365/days`. 4) Roll when the short is worth 0.05–0.10.
**Trade-offs**: premium cushions only a few percent; the stock is the real risk. (ch05)

## Synthetic Conversion Check
**When to use**: pricing a call vs put, spotting IV mismatches, flattening inventory.
**How**: 1) Synthetic stock price = `K + Call − Put`. 2) Fair = `Stock + Interest − Dividends`, `Interest = K·r·days/365`. 3) Conversion edge = (synthetic − stock) − interest + dividends. 4) Use own borrow rate (conversion) or rebate rate (reversal). 5) Near expiry, roll via jelly roll or box to avoid pin risk.
**Trade-offs**: American exercise breaks parity; edge is pennies, only viable at market-maker costs. (ch06)

## Box Valuation
**When to use**: lending or borrowing via options; checking spread parity.
**How**: 1) Box = call vertical + put vertical on the same strikes. 2) Fair `= W − W·r·days/360`, `W = K₂ − K₁`. 3) Compare traded value.
**Trade-offs**: American boxes carry early-exercise value; retail costs exceed the edge. (ch06, ch09)

## Implied Rate Back-Out
**When to use**: calls look cheap and puts rich (or the reverse) with a gap growing with maturity.
**How**: 1) Fix stock, strike, IV, dividend. 2) Solve the rate per month so both theo values fall in the markets. 3) Rising implied rates = market prices hikes.
**Trade-offs**: borrow cost and dividends mimic rate effects. (ch07)

## Ex-Date Exercise Check
**When to use**: the afternoon before every ex-date, for every long ITM call.
**How**: 1) `D − Interest` vs put bid. 2) Greater: exercise. Smaller: hold, or sell the put. 3) Exercise rather than leg out.
**Trade-offs**: tiny edge, large cost of forgetting; skating pays only at very low costs. (ch08)

## Dividend Input Discipline
**When to use**: pricing any option that spans an ex-date.
**How**: 1) Enter the schedule (date, amount). 2) Project known raise patterns. 3) Update at each declaration. 4) Fix a wrong date: `ΔIV ≈ Δtheo/vega`.
**Trade-offs**: erratic payers need scenarios, especially on LEAPS. (ch08)

## Vertical Spread Selection
**When to use**: directional view with a price target and no strong vol view.
**How**: 1) Short strike = target. 2) Debit = delta bet, credit = income; same strikes give the same risk. 3) Check where the stock sits (long strike: long vol; between: pure delta; short strike: short vol). 4) After a big favorable move, buy back the short leg and keep the wing.
**Trade-offs**: wins on slow moves, loses to the outright on fast moves; re-underwrite when the stock reaches the short strike. (ch09)

## Takeover-Rumor Vertical
**When to use**: rumor with IV already bid.
**How**: 1) Buy a call spread bracketing the stock, with the short strike at the rumored cash price. 2) Vega near zero at entry. 3) On announcement the stock pins and the short call earns vega and theta.
**Trade-offs**: capped upside if the bid is raised. (ch09)

## Wing-Spread Strike Selection
**When to use**: neutral income iron condor or butterfly.
**How**: 1) σ-to-expiry `= IV/16 × √(trading days) × S`. 2) Short strikes near ±1σ for ~68%. 3) Screen: range-bound chart, no trend (ADX, MACD), no events. 4) Check payout/risk (`C/(w − C)`, usually below 1:3). 5) Prefer ETFs and indexes.
**Trade-offs**: too close = tiny range; too far = no credit; 1σ condors lose long term unless you expect realized < implied. (ch10)

## Safe Landing for a Threatened Iron Condor
**When to use**: stock approaches a short strike.
**How**: 1) No opinion: close. 2) Buy back the cheap safe-side short; keep the worthless wing. 3) Believe the move: buy back the tested short, leaving a long strangle or long call. 4) Neutral: roll the tested spread out (ch17).
**Trade-offs**: locks in a loss; inaction only with a proven edge. (ch10, ch17)

## Long-Vol Condor (Buy the Guts)
**When to use**: pre-catalyst, expecting IV to rise.
**How**: 1) Sell wings, buy guts, centered on the stock. 2) Delta/gamma flat, vega +, theta −. 3) Break-even days `= vega × ΔIV / |θ|`. 4) Exit before the news.
**Trade-offs**: needs a short holding period; four-leg costs. (ch10)

## Calendar Entry Checklist
**When to use**: income calendar at the strike.
**How**: 1) Forecast a range through front expiry. 2) Back-month IV in the lower third of its 12-month range. 3) No pending event. 4) Value at front expiry with a model. 5) Hedge drift with stock. 6) Prefer OTM.
**Trade-offs**: rising IV is not really wanted (front IV rises more). (ch11)

## Rolling for a "Free" Call
**When to use**: long-dated call financed by monthly short calls.
**How**: 1) Buy 6–12 months. 2) Sell the next month after each expiry (or buy the short at 0.05–0.10 and sell the next). 3) Free when `Σ credits ≥ cost`. 4) Bearish: sell the long. Bullish: hold.
**Trade-offs**: monthly short-gamma risk. (ch11)

## Term-Structure Trade
**When to use**: front IV far from back IV.
**How**: 1) Long calendar when front is rich; short calendar when front is cheap. 2) Compute P&L leg by leg: `Σ vegaᵢ × ΔIVᵢ`. 3) Back vega ≈ 2× front vega.
**Trade-offs**: back IV follows front IV (dealer hedging); events keep back IV rising. (ch11)

## Rush-and-Crush Trade
**When to use**: binary event with a clean IV history.
**How**: 1) Sell: delta-neutral ATM short just before the news, exit next morning; vega is the prize. 2) Buy: delta-neutral long days before, exit before the news; need `ΔIV ≥ |θ|·days/vega`. 3) Attribute P&L by greek.
**Trade-offs**: big gaps eat short vega; buying too early costs theta. (ch12)

## Gamma Scalping
**When to use**: expecting realized vol above the IV priced.
**How**: 1) Long ATM options, hedge to zero. 2) Sell as it rises, buy as it falls; each hedge banks `½ΓΔS²`. 3) Compare daily scalps with theta. 4) Break-even move `≈ √(2Θ$/(Γ·100))`. 5) Go home flat.
**Trade-offs**: weekends cost theta; trends and quiet tapes lose. Short gamma: hedge partially. (ch13)

## Vol-Chart Reading
**When to use**: choosing between buying and selling vol.
**How**: 1) Overlay IV and 30-day RV for 6–12 months. 2) Locate one of nine patterns. 3) Buy when IV is below RV and low in its range; sell when IV exceeds RV by 5+ points with no news. 4) Check for mesas and regime changes; use peers if history fails.
**Trade-offs**: gaps of 1–3 points persist; a statistical edge, not a certainty. (ch14)

## Straddle / Strangle Management
**When to use**: pure vol positions.
**How**: 1) Long: choose the cheapest-IV expiry, scalp or leg out (sell calls on rallies, puts on dips). 2) Short: IV above RV and 12-month norm, monitor delta, stop on delta, close before expiry. 3) Cap tail by adding wings. 4) Never sell dime strangles.
**Trade-offs**: strangle trades nominal for percentage return and wider break-evens. (ch15)

## Ratio Spread Reading
**When to use**: any 1:2 or 1:3 position.
**How**: 1) Map delta, gamma, theta, vega at several stock prices. 2) Find which face shows now and at your stop. 3) Hedge delta partially; expect gamma to flip. 4) Ratio vertical: buy back part of the short side if vol rises.
**Trade-offs**: credit is not risk; vega sign flips where IV moves against you. (ch16)

## Skew Risk Reversal
**When to use**: call-vs-put IV gap far from its normal level.
**How**: 1) Compare current gap to usual (10% OTM call about 4 points below put). 2) Trade only the excess. 3) Short stock `100·N·(Δcall + |Δput|)`.
**Trade-offs**: wrong-way vega versus price. (ch16)

## Greeks-Driven Strategy Selection
**When to use**: before any entry.
**How**: 1) View: direction, size, timing. 2) Holding period sets theta tolerance. 3) IV vs RV and history; catalyst? 4) Convexity wanted? 5) Choose outright vs spread, then strike and expiry. 6) Check net portfolio greeks and up/down risk.
**Trade-offs**: spreads remove vega and gamma you may want. (ch17)
