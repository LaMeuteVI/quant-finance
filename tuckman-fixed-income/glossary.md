# Glossary — Tuckman & Serrat, Fixed Income Securities

Alphabetical. Format: **Term** — definition (chapter).

**Accrued interest (AI)** — coupon earned since the last payment date; full (invoice) price = flat (quoted) price + AI (ch01, ch03).
**Annuity factor A(T)** — PV of 1 per period over the life, Σd(t); turns a rate gap into a price gap: P = 1 + ((c − C)/2)·A (ch02, ch16, ch17).
**Arbitrage pricing** — price = cost of a replicating portfolio; equals discounting with d(t) (ch01); dynamic replication for contingent claims (ch07).
**Asset swap spread (par-par / market value)** — spread over LIBOR earned on 100 (par) or on P (market value) when a bond is swapped to floating; s_Mkt = 100·s_PAR/P (ch19).
**Backbone (vol)** — how ATM bp vol moves with the forward level; the right calibration target for skew-model deltas (ch18).
**Barbell / bullet** — two-maturity vs one-maturity portfolio of equal duration; barbell has more convexity, less yield (ch04).
**Basis (futures)** — gross basis = P − cf·F; net basis = forward price − cf·F = gross basis − carry = value of the quality option (ch14).
**Basis swap (LIBOR–OIS)** — fed funds + X vs LIBOR; X(T) is the spread that anchors the LIBOR projection curve (ch16, ch17).
**Black-Karasinski (BK)** — d ln r = k(t)[ln θ(t) − ln r]dt + σ(t)dw; lognormal, mean-reverting, time-dependent; variable Δt keeps the tree recombining (ch10).
**Bootstrapping** — fitting a curve one benchmark at a time, each new instrument pinning one new discount factor or forward (ch01, ch02, ch21).
**Bucket '01 (forward bucket)** — −ΔP for a 1bp shift of all forwards in one maturity region (ch05).
**Burnout** — prepayment speed becomes less sensitive to incentive as prone borrowers leave the pool; makes MBS cash flows path dependent (ch20).
**Carry / cash carry** — coupon income minus financing cost; forward drop = carry (ch03, ch13).
**Carry-roll-down** — Tuckman's term: P&L from time passing under a chosen "no change" scenario, excluding cash carry (ch03).
**CDS (credit default swap)** — fee leg (coupon + accrual on default) against a contingent leg paying (1 − R); upfront = (market − standard coupon) × risky annuity (ch19).
**CDS-bond basis** — CDS spread vs bond-implied credit spread; not an arbitrage (funding, delivery option) (ch19).
**Cheapest-to-deliver (CTD)** — basket bond with min P/cf at delivery (min net basis before); F_T = min P_i/cf_i (ch14).
**CIR** — dr = k(θ − r)dt + σ√r dw; bp vol σ√r, positive rates if 2kθ ≥ σ² (ch10).
**Clearing (CCP)** — central counterparty facing both sides; mutualizes counterparty risk through a margin/capital waterfall (ch16).
**CMS (constant-maturity swap)** — leg pays a fixed-tenor swap rate; fair rate = forward swap rate + convexity correction (ch16).
**Constant-hazard model** — constant default intensity λ: survival e^(−λT); credit triangle s ≈ λ(1 − R) (ch19).
**Conversion factor (cf)** — price per 1 face at a 6% yield (notional coupon), maturity rounded down to a quarter; equals 1 for a 6% bond (ch14).
**Convexity (bond)** — (1/P)·d²P/dy²; zero: T(T + .5)/(1 + y/2)²; positive convexity = long volatility (ch04).
**Convexity effect (term structure)** — Jensen term −½Cσ² lowering forwards; grows with maturity² (ch08, ch09).
**Convexity correction (futures)** — futures rate − forward rate ≈ σ²t²/2 + σ²βt/2 in a normal model (ch13).
**CPR / SMM** — annualized / monthly prepayment rates; CPR = 1 − (1 − SMM)^12 (ch20).
**Credit event** — bankruptcy, failure to pay, acceleration, repudiation, restructuring; triggers CDS settlement (ch19).
**Curve risk** — exposure to non-parallel curve moves; invisible to a single DV01 (ch05).
**CV01** — swap value change for a 1bp change of its fixed coupon; proportional to the annuity (ch05).
**Daily settlement** — futures P&L paid each day and contract re-struck; makes futures < forward for bonds (ch13).
**Day count** — act/act (govt bonds), act/360 (money market, floating legs), 30/360 (corporates, swap fixed legs) (ch01, ch16).
**Defined benefit / contribution (DB/DC)** — pension where sponsor / beneficiary bears investment risk (ch00).
**Discount factor d(t)** — price today of 1 unit paid at t; d(t) = (1 + r(t)/2)^(−2t) (ch01, ch02).
**Dollar roll** — selling front-month TBA and buying back-month TBA; a financing alternative to MBS repo, "above carry" if it trades special (ch20).
**Duration (effective / modified)** — −(1/P)dP/dy, quoted per 100bp; DV01 = P·D/10,000 (ch04).
**DV01** — −ΔP/(10,000Δy), price gain per 1bp fall in rates; hedge ratio F_B = −F_A·DV01_A/DV01_B (ch04).
**ED (Eurodollar) futures** — 3-month USD LIBOR futures, price 100 − 100L, $25 per bp, tailed hedges (ch15).
**End-of-month option** — short's right to switch bond at the fixed final settlement price (ch14).
**Equilibrium vs arbitrage-free model** — equilibrium derives the curve (Vasicek, CIR); arbitrage-free fits it (Ho-Lee, BK) (ch08, ch09).
**Fail (Treasury)** — undelivered security; TMPG charge max(3% − FF target, 0) caps specialness (ch12).
**Fed funds / OIS** — uncollateralized overnight rate; OIS swaps fixed vs compounded fed funds, the post-crisis discount curve (ch15, ch17).
**Flat forwards** — piecewise-constant continuously compounded forwards; robust, local curve interpolation (ch21).
**Flattening / steepening** — long rates falling more than (or short rates rising more than) the other end / the reverse (ch02).
**Forward drop** — spot minus forward price = carry (ch13).
**Forward measure** — measure making f(T, T+τ) a martingale; V_t = d_t(T+τ)·E^(T+τ)[V] (ch11, ch18).
**Forward price (bond)** — FV of full spot price at the term repo rate less FV of interim coupons (ch13).
**Forward rate f(t)** — six-month rate from t − .5 to t: 1 + f/2 = d(t − .5)/d(t) (ch02).
**FRA** — pays PV at fixing of N·τ(K − L); FRA rate = forward rate (ch15).
**Full / flat / dirty / clean price** — invoice price vs quoted price excluding accrued (ch01).
**Gauss+** — three-state, two-shock Gaussian cascade (r → m → l → θ), zero vol on r, humped vol structure (ch11).
**General collateral (GC)** — repo on any acceptable bond in a class; the base repo rate (ch12).
**Gross / net basis** — see Basis (ch14).
**Haircut** — percentage by which a repo loan is below collateral value (ch12).
**Ho-Lee** — dr = λ_t dt + σ dw; time-dependent drift fits the curve; parallel shifts, flat vol (ch09).
**Hazard rate λ** — instantaneous default intensity (ch19).
**Implied repo rate** — repo rate that makes cash-and-carry on a bond break even; highest implied repo identifies the CTD (ch14).
**Interim mispricing** — widening of a relative-value gap before convergence; requires capital (ch17).
**IO / PO** — interest-only / principal-only MBS strips; IO has negative duration (ch20).
**Jensen's inequality** — E[1/(1 + r)] > 1/(1 + E[r]); source of convexity effect (ch08).
**Key rate / key-rate '01** — par-yield tent shifts (2/5/10/30y) summing to a parallel 1bp shift; DV01_k = −(1/10,000)∂P/∂y_k (ch05).
**Law of one price** — identical cash flows, identical price, absent liquidity, financing, tax and credit effects (ch01).
**LIBOR market model (LMM)** — observable forward rates as factors; inputs vols and correlations; drifts derived by no-arbitrage (ch11).
**LIBOR–OIS spread** — price of three-month funding security; ~8bp pre-2007, 365bp peak Oct 2008 (ch15, ch17).
**Local hedge** — DV01 hedge accurate only near the current rate; convexity mismatch remains (ch04).
**Locality (curve)** — shifting one benchmark moves only nearby segments and hedges (ch21).
**Mean reversion (k, θ)** — pull of r toward θ; half-life ln 2/k; cuts long-maturity vol and convexity (ch09).
**Mid-curve option** — option on a forward starting after expiry; reveals forward volatility (ch11).
**Model 1 / 2 / 3 / 4** — normal no drift / constant drift / time-dependent vol / lognormal (ch09, ch10).
**Net basis** — see Basis (ch14).
**Numeraire** — asset whose value normalizes prices; chosen so the underlying is a martingale (ch18).
**OAS (option-adjusted spread)** — constant spread over risk-neutral short rates, discounting only, matching market price; > 0 = cheap (ch07).
**On-the-run (OTR)** — latest auctioned issue; trades rich (liquidity, specialness) (ch01, ch12).
**OIS discounting** — discount at the collateral rate; project LIBOR from a separate curve (ch17).
**P&L decomposition** — cash carry + carry-roll-down + rate change + spread change (ch03).
**Par rate C(T)** — coupon pricing a T-year bond/swap fixed leg at par: C = 2(1 − d(T))/A(T) (ch02).
**Partial '01** — value change for a 1bp fall of one fitting-instrument rate with the curve refitted (ch05, ch21).
**Pass-through / TBA** — MBS pool cash flows passed to investors; TBA = forward on a generic pool with delivery option (ch20).
**PCA (principal components)** — eigenvectors of the rate covariance matrix: level, slope, short-rate; 3 PCs explain > 99% (ch06).
**Prepayment model** — refinancing S-curve CPR = T + 1/(a + e^(−bI)), turnover, defaults, curtailments (ch20).
**PV01 / DV01 / CV01** — value change for a 1bp fall in all fitting rates / in a security's yield / in a swap coupon (ch05).
**Quality option** — short's right to choose which basket bond to deliver (ch14).
**Realized forwards** — scenario where today's forwards become tomorrow's spot rates; every bond earns f(1) (ch03).
**Receiver / payer** — receives / pays fixed; receiver is long the fixed "bond" (ch02, ch16).
**Recombining tree** — N + 1 terminal nodes vs 2^N non-recombining (ch07).
**Regression hedge** — F^R = −F^N·(DV01^N/DV01^R)·β̂ with β from change-on-change OLS (ch06).
**Repo / reverse repo** — sale plus repurchase at P₀(1 + r·d/360); repo borrows cash, reverse lends it (ch12).
**Reset risk** — floating-leg DV01 ≈ time to next payment, a sawtooth between fixings (ch16).
**Rich / cheap** — price above / below value implied by a base curve or hedge set (ch01).
**Right-way risk (repo)** — borrower default tends to raise government collateral value (ch12).
**Risk-neutral probabilities** — probabilities repricing all underlying bonds; derivative = expected discounted value (ch07).
**Risk premium (λD)** — extra expected return proportional to duration; Sharpe S = λ/σ (ch08).
**Roll-down** — P&L from ageing along an unchanged curve; sign[ΔP] = sign[c − f(T)] (ch02, ch03).
**SABR** — stochastic-vol model (σ₀, α, β, ρ); β, ρ set skew, α smile (ch18).
**Shadow rate** — unconstrained model rate with observed rate floored at zero (ch09).
**Short convexity** — hedged book losing both ways; short volatility (ch04).
**Spot rate r(t)** — rate from today to t; geometric average of forwards (ch02).
**Spread (to a curve)** — constant added to every benchmark forward reproducing the market price; spread curve s(t) for sectors (ch03).
**Special / specialness** — repo rate below GC on a bond in demand; special spread = GC − special (ch12).
**STRIPS (C-/P-)** — zero-coupon Treasuries; C fungible, P tied to its parent bond's richness (ch01).
**Stub** — period from settlement to the first futures start (ch15, ch21).
**Swap** — fixed bond vs floating note on a never-exchanged notional; exposure = NPV (ch16).
**Swaption** — option on a swap; receiver = put on forward swap rate; value A₀·πᴺ (ch18).
**Tail** — hedge reduction N/(1 + r·d/360) because futures gains arrive early (ch13, ch14, ch15).
**TED spread (Tuckman)** — spread subtracted from stub and ED futures rates to price a Treasury (ch15).
**Term repo** — repo to a fixed date, clustered on futures expiries (ch12).
**Three-pillar pension system** — public PAYG, occupational, private DC (ch00).
**Time-dependent volatility σ(t)** — fits option prices across expiries; no mean reversion = parallel shifts (ch10).
**TIPS / JGBi** — inflation-linked bonds; TIPS principal floored at par, JGBi not (ch00).
**Total return / net return** — (P₁ + c − P₀)/P₀, minus financing cost; divide by initial price (ch03).
**Vasicek** — dr = k(θ − r)dt + σdw; declining vol term structure; θ = r∞ + λ/k (ch09).
**Volatility, bp vs yield** — bp vol = σ_y × r; CIR σ√r; not comparable across families (ch10).
**Yield-to-maturity** — single rate y solving P = Σ(c/2)/(1 + y/2)^t + …; a quote, not relative value (ch03).
**Yield spread / bond spread** — YTM minus benchmark rate / spread to forward curve (ch19).
**Zero-volatility spread** — spread to forwards ignoring optionality; wrong for options (ch20).
