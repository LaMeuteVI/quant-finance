# Cheatsheet — Yield-Curve Judgment (Ilmanen)

## Decision rules
| When | Do | Because |
|---|---|---|
| Curve slopes up and you expect a rise | Short only if expected rise > forward-implied (`f₁,ₙ − sₙ₋₁`) | Forwards are break-evens; carry beats a smaller rise (ch01) |
| Someone says "forwards show market expects hikes" | Ask for BRP and convexity | Forward = short rate + view + BRP + CB (ch01, ch02, ch06) |
| Rolling-yield differential is wide between maturities | Expect it to be kept; lean long duration when forward curve slopes up | Persistence factor 1.4–2.3 beyond 1y (ch02) |
| Flattener looks attractive on forward view | Compare view with break-even flattening | Concave curve: negative carry and rolldown (ch02, ch05) |
| Barbell vs bullet, curve highly concave | Favor bullet unless you expect flattening or a vol spike | Barbell gives up rolling yield; convexity small (ch05) |
| Comparing bonds across duration | Use rolling yield + ½·Cx·σ², then add view | Yield ignores rolldown and convexity (ch05, ch06) |
| Setting benchmark duration, short-horizon investor | Keep ≤ ~2y | Premium flat beyond 2y, vol keeps rising (ch03) |
| Cash benchmark = 1m bills | Extend to 3m/MM paper | 3m beat 1m in 99% of years (ch03) |
| Steep curve, stocks weak (inverse wealth > 1) | Read as premium; add duration | TS>0 and IW>1: +11.95%/yr (ch04) |
| Inverted curve and stocks strong | Cut duration hard | TS<0 and IW<1: −13.6%/yr (ch04) |
| Judging a bond-timing rule | Require out-of-sample, subperiods, costs | In-sample 11.15% vs out-of-sample 8.64% (ch04) |
| Scenario analysis | Always assign probabilities | Reveals implied bias/volatility; one scenario = zero vol (ch06) |
| Backing out expectations beyond ~7y duration | Treat as directional only | Error multiplied by duration (ch06) |

## Decision tree: what drives this curve shape?
Linear upward → expected parallel rise or linear BRP. Concave → flattening expected, high volatility, or BRP flattening after 2y. Convex → steepening expected. Humped/inverted long end → convexity bias (vol high) on top of BRP. Average over years → BRP.

## Thresholds and defaults
| Item | Value |
|---|---|
| Persistence factor | ~0.8 (<1y); 1.4–2.3 (>1y) (ch02) |
| Forecast MAE, 6m horizon | ~100bp for forwards, surveys, no-change (ch02) |
| US 1970–94 geometric premium over 1m | 3m 0.84; 1–2y 1.65; 3–4y 2.09; 5–10y 2.12; 20y 2.00 (ch03) |
| Sharpe, 3m → 20y | 1.92 → 0.22 (ch03) |
| Hit rate beyond 2y (annual) | 44–56% (ch03) |
| Curve upward-sloping | ~90% of time (ch01) |
| 20y return by 20y–1m spread | <0: −2.57%; 0–300bp: 9.44%; >300bp: 12.46% (ch03) |
| Four-predictor model | R² 10%, hit rate 61%, 12m corr 0.57 (ch04) |
| Scaled / 1/0 / always-bond Sharpe | 0.68 / 0.53 / 0.06 (ch04) |
| Beat-both frequency, 5y horizon | 92% (ch04) |
| Momentum band | ±5bp around 6m moving average (ch04) |
| Zero convexity | Cx ≈ Dur²/100 (ch05) |
| Convexity value | ½·Cx·σ²; 30y ~1% in 1990s (ch05) |
| Convexity bias matters | beyond ~5–10y (ch05) |
| Bullet vs barbell 1980–94 | bullet +105bp/yr (ch05) |
| 10s–30s barbell example | 11bp flattening vs 138bp parallel (ch05) |
| Duration-neutral barbell weight | w_long = Dur_bullet,h / Dur_long,h (ch05, ch06) |

## Trade-off matrix: hypotheses
| Hypothesis | Forwards mean | Best next-curve forecast | Empirical fit |
|---|---|---|---|
| PEH | expectations | implied forward curve | rejected (ch02) |
| Risk premium (E(Δs)=0) | premia | today's curve | better (ch02) |
| LEH vs UEH | equal returns vs equal expected spots | differ by CB | both can't hold (ch01) |

## Tells and smells
- Forward curve falls while spot still rises: spot slope flattening, rolldown shrinking (ch01).
- Par curve within 25bp while forwards span 200bp: local cheapness (ch01).
- Bill forwards imply +200bp vs surveys +100bp: abnormally high premium (ch06).
- Negative implied barbell volatility: dished curve, steepening expected (ch05).
- Yield and relative vol mixed up: error of ×10 (ch05).
- Premium quoted from a post-1981 sample: inflated (ch03).
- Forecast strength high but horizon is one month: expect 35–61% beat-both, not certainty (ch04).
- Cheapness from a fancier measure with noisy inputs: backtest first (ch06).
