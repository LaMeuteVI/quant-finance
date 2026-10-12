# Cheatsheet — Tuckman desk decision rules

## Decision rules
| When | Do | Because |
|---|---|---|
| Bond looks cheap vs a fitted curve | Check repo specialness, on-the-run premium, bid/ask, capital for divergence before trading | Profit = gap compounded at repo, realized only at convergence; special repo explained the whole 6.5c gap (ch01, ch17) |
| Comparing bonds across coupons/maturities | Use spread to curve (or OAS), never YTM | Coupon effect: on an upward curve zero > par > high-coupon yield (ch03) |
| Hedging one instrument with another | DV01 ratio, then scale by regression β̂ if yields move unequally | Equal DV01 assumes parallel moves (ch04, ch06) |
| DV01 is zero but book is a curve trade | Report key-rate, partial or bucket '01s; hedge largest bucket first | Zero DV01 hid a 5s–30s steepener of ~$39k/bp (ch05) |
| Swap/bond+swap book | Partial '01s on fitting instruments; hedge fixed and floating legs separately | Nearly diagonal hedges; floating DV01 ≈ time to next payment (ch05, ch16) |
| Hedging nominal with real (or swap with Treasury) | Regress nominal on real; check rolling β̂ | Reverse regression is biased by inflation; β̂ moved 0.75–1.56 (ch06) |
| Illiquid tenor client trade (20y) | Hedge with liquid neighbours (10y, 30y) at regression risk weights | Avoids paying the 20y bid/ask; weights need not sum to 100% (ch06) |
| Two RV expressions of one view | Pick higher roll-down; hedge the global factor with a slow-moving market | Roll-down funds patience against stop-losses (ch02) |
| Pricing derivatives/interpolating | Arbitrage-free model (fit the curve) | Matches underlyings by construction (ch09) |
| Searching for rich/cheap | Equilibrium or partial-fit model | A fully fitted model calls everything fair (ch09) |
| Quoting caps/swaptions | Normal (bp) vol, Black-style formulas, SABR for strike | ATM payer = receiver; lognormal fails at low strikes (ch18) |
| Exotics (Bermudan) | LMM calibrated to many vols | Fits curve automatically, correlations from history (ch11) |
| Swap relative value | Gauss+, don't over-calibrate vol | Humped vol, PCs matched (ch11) |
| Collateralized swap valuation | Discount on OIS, project LIBOR separately | Notional finances at index, NPV at collateral rate (ch17) |
| Long a special bond | Lend it special, don't finance at GC | Specialness is a dividend to the owner (ch12) |
| Hedging a forward with futures | Tail `N/(1 + rd/360)`; repo risk via short-rate futures | Daily settlement; spot DV01 overstates forward DV01 (ch13) |
| Selling Treasury basis | Stress slope, bond-specific moves, futures cheapness; size to interim loss | Net basis = option; interim loss $455k exceeded modelled scenarios (ch14) |
| Using ED strip as forwards | Apply convexity adjustment ≥ 2–3 years | r_fut − r_fwd = σ²t²/2 + σ²βt/2; 13bp at 5y, 51bp at 10y (ch13) |
| Distressed bond | Credit-adjusted DV01 | Duration 6.3 → 3.95 with R = 40% (ch19) |
| Negative-basis trade | Compute breakeven cost of capital; lock term funding | Pays 31.34 in all states; funding is the risk (ch19) |
| MBS cheap on OAS | Check mean reversion and rate correlation of OAS | OAS = value + model error (ch20) |
| Curve for hedging | Flat forwards; test hedge locality | Smooth forwards spread hedges across buckets (ch21) |
| Judging a bank/dealer | Compare asset maturity to funding stability | Repo/CP vanish in days (ch00, ch12) |

## Decision trees
- **Model choice**: quote/interpolate options → time-dependent σ(t); value and hedge → mean reversion; negative rates matter or far OTM → CIR/lognormal/BK; near-the-money in stable regimes → normal closed forms; swap RV → Gauss+; exotics → LMM (ch10, ch11).
- **CTD**: yield > 6% → longest duration; yield < 6% → shortest duration; steeper curve cheapens long bonds; flatter cheapens short; own richening/cheapening shifts it (ch14).
- **Hedge instrument**: bond book → key rates; swap book → partial '01s; risk report → buckets; stat factors → PCA (ch05, ch06).

## Thresholds and defaults
| Item | Number |
|---|---|
| Recovery convention | 40% |
| CDS standard coupons / dates | 100 or 500bp; 20 Mar/Jun/Sep/Dec |
| Sharpe ratio plausible for bonds | ~9–10% (λ ≈ 9bp/yr at 100bp vol) |
| Long-run rate expectation | ~5% (3% real + 2% inflation) |
| Futures notional coupon | 6% (cf = 1) |
| ED value / FF value | $25 / $41.67 per bp |
| TMPG fail charge | max(3% − FF target, 0) |
| LIBOR–OIS | 8bp normal; 30–48bp May 2010; 365bp Oct 2008 |
| PCs | 3 explain > 99%; level ~95% of total |
| Swap hedge error single curve | 0.6–3.6bp normal, up to ~6bp crisis |
| Model 1 convexity (113bp vol) | 10y −18.8bp, 30y −135bp |
| MBS | TBA 4% hedge 0.66 (10y) / 1.15 (5y); servicing fee 20–50bp |

## Tells and smells
- Rich/cheap measured in cents on one bond only: base set unstated.
- Significant α in a change-on-change regression: specification or data problem.
- In-sample R² 99.8% but crisis errors −5bp: unstable hedge.
- Jagged fitted drift year to year: supply/demand noise in "expectations".
- Hedge ratios for a 5.5y swap spread over 4, 7, 12, 25y: curve artefact.
- Convex position "free": priced convexity lowers the forward by exactly ½Cσ².
- Calibrated Gaussian priced options near zero rates: negative-rate bias.
- Bid-ask at 0.25–0.5bp while single-curve error is larger.
- Large MBS OAS in a credit crisis: credit, not mispricing.
- 100% of financing in overnight repo or CP: run risk.
