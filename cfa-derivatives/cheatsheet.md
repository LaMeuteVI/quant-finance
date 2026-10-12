# Cheatsheet — CFA Derivatives (L1 · L2 · L3)

## Decision rules
| When | Do | Because |
|---|---|---|
| Pricing any derivative | Replicate, discount at r, use risk-neutral weights | Risk premium is already in spot; using r + λ double counts (ch02, 04) |
| Forward price needed | F₀ = FV(S₀ + CC − CB) | Carry, not your forecast of S_T, sets F₀ (ch02, 03) |
| Forward already traded | Value = PV(F_t − F₀) = S_t − PV(carry) − F₀/(1+r)^(T−t) | Price is a fixed term, value is a mark (ch03) |
| Option exercise could be early | Use a tree, max(continuation, exercise) at every node | Closed forms and the multi-period expectation ignore interior exercise (ch04) |
| American call, no payouts | Never exercise; sell it | C₀ = c₀ ≥ S − PV(X) > S − X (ch02, 04) |
| American put deep ITM | Exercise may be optimal | Gain capped at X, interest on X beats remaining time value (ch02, 04) |
| Underlying is a spot with carry | BSM with γ (δ or r_f) | Carry enters e^(−γT) and d1 (ch04) |
| Underlying is futures/forward/FRA/swap rate | Black; caplet discounts to payment date, swaption uses AP·PVA | No carry cost; T = option expiry, not tenor (ch04) |
| Book is delta-hedged | Fix gamma/vega with options first, delta with stock last | Stock has zero gamma (ch04) |
| Strategy choice | State direction AND implied-vol view vs your forecast | A premium is a vol forecast (ch05) |
| Bullish, expect IV to fall | Write puts / bull put; to rise: buy calls | Exhibit 32 matrix (ch05) |
| Rich OTM put skew | Sell puts, buy bear put spreads, collars near zero cost | You sell the expensive wing (ch05) |
| Hedge short stock | Buy call (caps loss, long vega) over writing put (cushion only) | Write-put keeps unlimited loss (ch05) |
| Event straddle | Skip if IV already jumped | Breakevens widen to the new IV (ch05) |
| Cut bond-portfolio duration | Short bond futures (BPVHR) or pay-fixed swap | Pay-fixed has negative duration (ch06) |
| Size any overlay | (Target − current money exposure) / exposure per unit | Duration and beta are dollars, not percentages (ch06) |
| Futures-based hedge of bonds | Hedge CTD BPV, then multiply by CF | ΔF ≈ ΔCTD/CF (ch06) |
| Equitize cash / change beta | N_f = (β_T − β_S)/β_f × S/F, F includes multiplier | Whole-fund sizing is the classic error (ch06) |
| Hedge foreign bonds | ~100% hedged | Bond returns correlate with FX through rates (ch07) |
| Hedge foreign equities | Partial (band, 50% regret-min) is defensible | Safe-haven currencies diversify risky assets (ch07) |
| Selling base at premium / buying at discount | Hedge: roll yield is positive | Trades with the forward rate bias (ch07) |
| Cheaper FX hedge wanted | OTM, collar, put spread, seagull, barrier | Each step surrenders protection or upside; name the residual (ch07) |

## Decision tree: which model / instrument
1. Linear payoff, both obliged? Forward (OTC, one date), futures (daily MTM), swap (strip) → carry arbitrage / par-bond method.
2. Right not obligation? European, closed form needed → BSM (spot), Black (futures/rates). Early exercise, discrete dividends, rate lattice → binomial.
3. Hedge need: rate on one future period → FRA / rate futures; duration shift → swap or bond futures; beta → index futures; FX → forward first, options for convexity.

## Trade-off matrix
| Choice | Gain | Give up |
|---|---|---|
| Futures vs forward | Credit protection, liquidity | Margin funding, standardization (ch01) |
| Swap vs futures overlay | Customization, tenor | OTC credit, no voting rights, cash-flow drain (ch06) |
| Covered call | Premium, sells right tail | Upside above X; full downside (ch05) |
| Protective put | Floor at X (deductible S₀ − X) | Premium, theta bleed (ch05) |
| Collar | Zero-cost floor | Upside above X₂ (ch05) |
| Long calendar | Positive theta, long vega | Short gamma, big move kills it (ch05) |
| Variance swap vs vega | Convex tail payoff | Short side unlimited loss (ch06) |
| Forward hedge vs option hedge | No premium | Forfeits upside, MTM cash outflows (ch07) |

## Thresholds and defaults
| Item | Value |
|---|---|
| Futures margin | Initial typically <10%; call restores to INITIAL margin |
| Binomial no-arbitrage | d < 1 + r < u; π = (1 + r − d)/(u − d) |
| ATM delta | call ≈ +0.5, put ≈ −0.5; call − put = e^(−δT) |
| Annualize vol | daily × √252; monthly × √12; 21-day horizon = σ × √(21/252) |
| Rate-futures BPV | $25 per $1m 3-month contract; price = 100 − rate |
| Bond-futures notional coupon | 6% (CTD: low coupon/long duration when yields > 6%) |
| Variance notional | N_vega/(2K); strike ≈ above ATM IV |
| FX quotes | P/B; base hierarchy EUR > GBP > AUD > NZD > USD; spot T+2 |
| Regret-minimizing hedge | 50% hedge ratio |
| Min-variance hedge | h* = ρσ(R_DC)/σ(ΔS); ≈100% direct, can exceed 100% |
| n spot rates → FRAs | n(n−1)/2 |

## Tells and smells
- Forward "cheaper than expected spot" argument: forward is not a forecast.
- Swap notional equal to portfolio face: duration scaling missing.
- Contract count of 1,455 instead of 6: multiplier forgotten.
- "Zero-cost" structure advertised as free: residual exposure unnamed (1×2 put spread, short seagull).
- Event straddle bought after IV spike; permanent long VIX ETP hedge (contango bleed).
- Carry or EM book reported with Sharpe/VaR only: negative skew hidden.
- Hedge ratio drift on volatile assets: static hedge; rebalance by forward, not spot.

## Exam traps
| Trap | Correct |
|---|---|
| Margin call amount | Initial − balance, not maintenance − balance |
| Covered call breakeven | S₀ − c₀ (not X + c₀); protective put BE S₀ + p₀ |
| Protective put max loss | S₀ − X + p₀ (add premium) |
| Forward mid-life value | S_t − F₀/(1+r)^(T−t); discount F₀, not S_t |
| Benefits vs costs | γ lowers F₀, θ raises it |
| Futures value after settlement | Zero |
| Swap rate | Numerator last DF only; denominator sums all n |
| Swap value sign | Receive-fixed gains when rates fall; use remaining annuity and current rate |
| Long FRA | Pays fixed, gains when rates rise; settlement discounted by 1 + D·t |
| Accrued interest | Days since last coupon; subtract AI_T in bond futures |
| N(d1) vs N(d2) | d1 = delta/shares; d2 = RN prob ITM/bonds; put bond leg is N(−d2) |
| Binomial | π uses u, d, r only; true probability and strike irrelevant |
| Gamma/vega parity | Call = put gamma and vega; stock cannot change gamma |
| Smile vs skew | Smile = both wings high; skew = OTM puts high only |
| Daily-return vol | × √252, not √(252/21) |
| Variance swap sign | Positive settlement: seller pays buyer; MTM discounts only (T − t) |
| Pay-fixed swap duration | Negative; use to shorten |
| Carry trade | Borrow low-yield, invest high-yield; wants wide spread and low implied vol |
| Bid or offer | Selling base: bid; buying base: offer; mark forwards at same remaining date, discount at cash-flow currency rate |
| Arbitrage definition | Zero risk AND zero capital; merger arbitrage is not |
