# Cheatsheet — Hull Decision Rules

## Which pricing tool?
| Product | Default tool | Watch out for |
|---|---|---|
| Forward/futures | F = S₀e^{(r+u−q)T} | Consumption assets: only an upper bound |
| European equity/FX/index option | BSM with q (FX: q = r_f) | Smile: use the surface point's volatility |
| Option on futures or with a clean forward | Black: e^{−rT}[FN(d₁) − KN(d₂)] | American futures options ≠ American spot options |
| American option | CRR tree + control variate | Dividends: use the S − PV(D) tree |
| Path-dependent / multi-asset | Monte Carlo + antithetic variates / control variates | Report the standard error; LSM for American features |
| Cap / floor | Black per caplet (forward measure) | Lognormal fails near 0 → normal model |
| European swaption | Black on the swap rate × annuity | Bermudan → Hull–White/LMM |
| CMS / in-arrears / quanto | Forwards + Ch 30 adjustment | Adjustment sign and size |
| Credit-risky derivative | f_nd − CVA + DVA | Wrong-way risk, netting set |

## Hedging decision rules
- Exposure **gains when the price rises** → **short hedge**. It **loses when the price rises** → **long hedge**.
- Hedging asset ≠ exposure asset → use **h* = ρσ_S/σ_F**, not 1.
- Hedge ends before the last liquid contract → pick the **next delivery month after the hedge**. No contract long enough → **stack and roll**, and secure funding lines.
- Option book: **delta daily**. Gamma/vega via traded options (**2 options** for both). Watch **limits**, not perfection.
- **Long gamma ⇔ negative theta.** You profit if realized volatility > implied volatility.
- Deep ITM American put, short time to expiry → consider **early exercise**. American call on a non-dividend stock → **never early**. With dividends → only **just before the ex-date**, if D > K[1 − e^{−r(T−t)}].

## Strategy selector (options)
| View | Volatility view | Strategy |
|---|---|---|
| Moderately up | Low/neutral | Bull spread, covered call |
| Moderately down | Low/neutral | Bear spread |
| Neutral | Low | Butterfly, calendar, short straddle (risky) |
| Neutral | High | Long straddle / strangle |
| Big move, skewed down/up | High | Strip / strap |
| Own stock, want a floor | — | Protective put, collar |

## Thresholds & defaults
- Trading days ≈ **252**/year for volatility. √T scaling.
- EWMA **λ = 0.94** (daily). GARCH is stable only if **α + β < 1**.
- VaR: **99% 10-day** (Basel) → **97.5% ES** (FRTB). z(99%) = 2.326, z(95%) = 1.645.
- Basel back-test (250 days, 99%): **0–4 green, 5–9 yellow, ≥10 red**.
- Recovery ≈ **40%** as a convention (it varies with the cycle). s ≈ λ(1 − R).
- T-bond futures CF yield: **6%**. Yields above 6% favor low-coupon, long bonds for CTD.
- Barrier discrete-monitoring shift: **H·e^{±0.5826σ√Δt}**.
- US stock option: **100 shares**, expiration on the **3rd Friday**.
- Naked option margin: max(premium + 20%S − OTM, premium + 10%S (calls) or 10%K (puts)) × 100.

## Tells & smells
- A **"riskless" profit on a desk that should only carry risk** → model or booking error (Kidder Peabody).
- **Hedge losing cash while the "economics are fine"** → funding/liquidity risk (Metallgesellschaft, LTCM).
- **AAA tranche yielding more than AAA bonds** → hidden correlation risk (ABS CDO).
- **Everyone running the same trade** → crowded exit risk (1987, LTCM).
- **Treasury reporting profits** → the hedger may have become a speculator (Orange County, P&G).
- **Low implied volatility for OTM puts relative to ATM on equities** → check the data. The equity skew is normally downward.
