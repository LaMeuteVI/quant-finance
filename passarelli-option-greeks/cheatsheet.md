# Cheatsheet — Passarelli Desk Decision Rules

## Decision rules
| When | Do | Because |
|---|---|---|
| Expect vol up | Buy options; expect vol down: sell | every option trade is a volatility trade (ch01, ch04) |
| Bullish, slow or capped move | Bull call vertical, short strike = target | vertical wins on slow moves, keeps delta (ch09) |
| Fast, big move expected | Outright option | uncapped, more delta (ch09) |
| Short option stop | `ΔS = ΔV/(abs(Δ)+Γ/2)`, price at the offer | delta alone understates the loss (ch05) |
| Short position gets tested | Ask "Would I do it now?" | strips sunk cost (ch05, ch17) |
| Short option worth 0.05–0.10 | Roll, don't wait for the nickel | greeks no longer help (ch05) |
| ITM call, day before ex-date | Exercise if `D − Int > put bid` | selling the put cheaply otherwise (ch08) |
| Long ATM held past 3 weeks left | Exit or re-plan | theta accelerates (ch04) |
| Position stock at short strike of a vertical | Re-underwrite | it flipped to short gamma/vega (ch09) |
| Iron condor tested, you have a view | Buy back the tested short | converts to long strangle in your direction (ch10) |
| No view on a tested condor | Close | "no opinion, no position" (ch10) |
| IV above RV by 5+ pts, no news | Sell vol | convergence plus theta (ch14, ch15) |
| IV below RV, low in 12m range | Buy vol | gamma/theta bargain (ch14) |
| Long calendar | Back IV in lower third of range, no events | back vega dominates (ch11) |
| Backspread | Underhedge delta | gamma flips sign below the short strike (ch16) |
| Hedge short gamma | Hedge partially; long gamma: scalp | each hedge locks loss (short) or gain (long) (ch13) |
| Conversion pricing | Use own borrow rate; reversal: rebate rate | rate is personal (ch06) |

## Decision tree: choose the structure (ch17)
1. Direction + target? Yes: delta product. No: straddle/strangle or wing spread.
2. Hold short, IV cheap, event near: long front-month option.
3. Hold weeks, IV fair, no event: debit vertical.
4. Range view, IV rich: iron condor or short strangle, wing it.
5. IV event only: delta-neutral rush or crush.

## Trade-off matrix
| Structure | Gamma | Theta | Vega | Wants |
|---|---|---|---|---|
| Long option | + | − | + | move, rising IV |
| Naked short | − | + | − | quiet, flat IV |
| Vertical at long strike | + | − | + | move to short strike |
| Vertical at short strike | − | + | − | stillness |
| Long ATM calendar | − | + | + | stillness, firm back IV |
| Iron condor | − | + | − | range |
| Long condor (guts) | + | − | + | catalyst |
| Backspread above short strike | + | − | + | movement |
| Ratio vertical at short strike | − | + | − | pin |

## Thresholds and defaults
| Item | Number |
|---|---|
| 1-day σ | IV/16 (256 days) |
| 1σ strikes for condors | ~68% inside |
| IV range window | 6 months (12 if volatile) |
| Calendar buy trigger | back IV in lower 1/3 of 12m range |
| IV-RV gap that persists | 1–3 pts; 7–10 pts converge |
| Rho / price on 2-year ATM | 5–8%; <1% for 1–2 months |
| Iron condor payout/risk | usually below 1:3 |
| Theta convention | calendar day, 7-day week |
| Vega, rho | per 1 vol point, per 1 rate point |
| Underlying scaling | Δ unchanged, Γ ÷ λ, θ, vega, ρ × λ |
| Put+call delta | ≈ 1.00 (1.07–1.08 near ex-date or ITM American) |
| Market starting size | 1–2 lots until rational |

## Tells and smells
- Theo outside bid-ask: bad input (rate, dividend, days), not a free trade (ch02).
- Friday cheapening: weekend taken out, not an IV drop (ch02).
- Heavy ITM call volume pre-ex-date: dividend arbitrage, not a signal (ch08).
- Call/put gap widening with maturity: rates, borrow, dividends (ch07).
- IV rising with RV flat and no news: clean sell tell (ch14).
- RV falling after a spike: mesa leaving the window (ch14).
- Neutral position with growing delta: no longer neutral (ch10).
- Credit/debit label: judge by greeks and where the stock sits (ch09, ch16).
- Hoping and praying: high HAPI, take the loss (ch17).
- Dime strangle, zero-credit far wings: all risk, no reward (ch10, ch15).
