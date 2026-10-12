# Patterns — Tuckman & Serrat, Fixed Income Securities

Calculation recipes, procedures and trade constructions. Chapter numbers in parentheses.

## Bootstrap discount factors from coupon bonds
**When to use**: extract d(t) from liquid bonds or par swaps on one payment cycle.
**How**: (1) use full prices; (2) sort by maturity; (3) solve `d(n/2) = [P_n − (c/2)Σᵢ₌₁ⁿ⁻¹ d(i/2)]/(100 + c/2)`; for swaps replace P with 100 and add the fictional notional; (4) read off `r(t) = 2[d(t)^(−1/2t) − 1]`, `f(t) = 2[d(t−.5)/d(t) − 1]`, `C(T) = 2[1 − d(T)]/A(T)`.
**Trade-offs**: exact fit to benchmarks, noisy for off-the-run bonds with idiosyncratic premia (ch01, ch02, ch21).

## Replicating-portfolio arbitrage (rich/cheap trade)
**When to use**: turn a rich/cheap signal into a hedged trade.
**How**: (1) pick T base bonds spanning all payment dates; (2) solve `F = C⁻¹c` backward from the last date; (3) cost = P′F; (4) buy target and sell replica if target price < cost; (5) convert price gap to bp spread (s ≈ 4.4bp for 6.5 cents on the ¾s Nov-2011); (6) test the gap against specialness, bid/ask and capital needed for divergence.
**Trade-offs**: profit = initial gap compounded at the repo rate, realized only at convergence; a special replica can erase it (ch01, ch03, ch17).

## Spread to a benchmark curve
**When to use**: express cheapness in bp, compare bonds of different maturity.
**How**: compute benchmark forwards f(1..T); solve s in `P = Σ CF/Π(1 + f/2 + s/2)`; for a sector use a spread curve s(t); use OAS for bonds with options (ch03, ch19).
**Trade-offs**: spread is portable across bonds, yield is not (coupon effect).

## P&L attribution and carry-roll-down scenarios
**When to use**: daily attribution, scenario tables, catching booking errors.
**How**: total = cash carry (coupon − financing) + carry-roll-down (`P(R^e, s) − P(R, s)`) + rate change + spread change, in fixed order. Choose R^e as realized forwards (return = f(1), net 0), unchanged curve (return driven by `f(T) − c`) or unchanged yield; show two columns.
**Trade-offs**: order of steps changes the split slightly; roll-down is a scenario, not a forecast (ch03).

## Roll-down screen for a forward-curve RV trade
**When to use**: choose legs and survive stop-losses.
**How**: (1) find the abnormal forward shape; (2) explain technicals plus macro and define both "outs"; (3) DV01-neutral legs; (4) price one year of roll-down per leg (sign of `c − f` of the expiring period); (5) switch to the leg with higher roll-down (25y6m vs 30y6m: +30.1 vs +7.1bp); (6) hedge the common factor in a slow-moving market and keep net roll-down positive (+16.3bp).
**Trade-offs**: liquid leg vs roll-down; hedge costs part of the carry; residual joint-move risk (ch02).

## DV01 hedge and bullet/barbell choice
**When to use**: hedge one risk factor; choose between duration-equal portfolios.
**How**: bump ±0.5bp both sides, `DV01 = −ΔP/(10,000Δy)`; `F_B = −F_A·DV01_A/DV01_B`; re-hedge as DV01s drift. Barbell: `V_L = V(D_bullet − D_S)/(D_L − D_S)`, compare convexity (129.8 vs 74.8) and yield give-up (2.663% vs 3.288%).
**Trade-offs**: barbell wins only if realized vol exceeds the vol that pays for the yield give-up; DV01 hedges ignore convexity and curve risk (ch04).

## Key-rate hedge (two-pass)
**When to use**: hedge a book of bonds with on-the-runs.
**How**: (1) compute key-rate '01s for 2/5/10/30y par shifts (sum ≈ DV01); (2) DV01-neutralize with `F ≈ F_pos·ΣKR01_pos/ΣKR01_hedge`; (3) read the residual profile; (4) neutralize the biggest bucket with its on-the-run, then re-neutralize total DV01 with one more bond; or solve the 4×4 system `M·F = −KR01`.
**Trade-offs**: exact solve gains little for much trading; zero total DV01 can hide a $39k/bp steepener (ch05).

## Partial '01 / bucket check of a swap or option hedge
**When to use**: swap books; verify a hedge (swaption vs 5x10 swap).
**How**: shift one fitting rate 1bp, refit, record P&L; hedge notional = `'01/(DV01 per 100/100)`; for buckets shift forwards in 0–2, 2–5, 5–10, 10–15 years and confirm the net bucket vector is near zero.
**Trade-offs**: partial '01s hedge nearly diagonally; buckets explain, they do not pick instruments (ch05, ch21).

## Regression hedge with residual-risk pricing
**When to use**: nominal vs TIPS, swap vs Treasury, illiquid tenor vs liquid neighbours.
**How**: regress Δy of the position (including extra component, e.g. nominal) on Δy of the hedge over a stable window; `F^R = −F^N(DV01^N/DV01^R)β̂`; hedged daily P&L vol `= |F^N|·DV01^N/100·σ̂`; check the 95% interval for β̂ against 1, rolling-window drift, out-of-sample errors; compare the vol with the expected convergence.
**Trade-offs**: minimizes in-sample variance only; β̂ moves with regime (0.75–1.29 rolling, 1.56 in 2000–02) (ch06).

## PCA butterfly / PC hedge
**When to use**: curve trade or large book needing a few uncorrelated factors.
**How**: shift each PC by 1 s.d. (Table 6.5 loadings), compute '01 per PC for the position and hedges, solve linear equations setting net Level and Slope exposure to zero; quote results as risk weights on the body DV01 (50.6% 2y and 61.3% 10y); check the unhedged PC3 loss.
**Trade-offs**: weights need not sum to 100%; PCs are regime dependent (ch06).

## Risk-neutral calibration, pricing and OAS
**When to use**: price any rate claim consistent with the curve.
**How**: (1) assume a short-rate tree and vol; (2) per date solve the probability (or drift/a_i in Ho-Lee, lognormal) that reprices the next zero; never round intermediate prices; (3) value backward `V = [pV_u + (1 − p)V_d + CF]/(1 + rΔt)`; (4) OAS: add a constant to discount rates only until model = market; (5) hedged, financed P&L ≈ OAS × time + OAS duration × convergence.
**Trade-offs**: OAS is conditional on the model's vol and drift; arbitrage-free fits cannot find rich/cheap among fitted bonds (ch07, ch09, ch10).

## Gauss+ daily routine
**When to use**: relative value and hedging across the swap curve.
**How**: (1) estimate α, σ, ρ from empirical PCs infrequently; (2) refit x₁, x₂, x₃ daily to 2y/10y/30y par swaps or by least squares; (3) set θ from views; (4) read residuals as rich/cheap; (5) add η(t) only for exotics or convexity adjustments.
**Trade-offs**: half-lives of r and m are weakly identified; refitting θ daily is internally inconsistent (ch11).

## Bond forward, forward drop and tailed futures hedge
**When to use**: price a bond forward, finance a long, hedge a forward with futures.
**How**: full forward `= [P₀ − PV(coupons)]×(1 + r·d/360)` at the bond's own term repo; drop = carry; forward yield from the full forward price; DV01 choice: forward DV01 + β × repo DV01; tail `N_fut = N_fwd/(1 + r·d/360)`; value existing long `= [P₀(d) − P]/(1 + r·d/360)`.
**Trade-offs**: GC instead of special repo misprices the forward; hedge repo leg with short-rate futures (ch12, ch13).

## Treasury futures basis analysis
**When to use**: CTD identification, basis trades, futures DV01.
**How**: `cf ≈` price at 6% yield; `P/cf` per basket bond; `F_T = min P_i/cf_i`; gross basis `P − cf·F`; net basis `GB − carry`; implied repo `≈ r + NB/P × 360/d`; tailed long-basis P&L `= G·ΔNB`; stress curve slope, bond-specific richening and futures cheapness; sell basis only with an option or limit hedge.
**Trade-offs**: net basis is option premium; option cheap at low yields; interim losses can exceed horizon P&L (ch14).

## ED / fed funds hedging and implied FOMC probability
**When to use**: hedge short-rate exposure, read policy pricing.
**How**: ED contracts = `N/($1mm) × period factor /(1 + r·d/360)`; bond bucket '01s ÷ $25; fed funds $41.67/bp per contract, `D/30` contracts for a D-day month; FOMC probability `p = (F − r₀)·D/(d_post·Δ)`; OIS for horizons beyond FF futures.
**Trade-offs**: assumes 0 or 25bp, effective = target, no premium; LIBOR–FF basis stays open (ch15).

## Swap valuation with two curves
**When to use**: value or unwind any swap under collateral.
**How**: (1) OIS discount curve from OIS swaps and FF futures; (2) projected LIBOR so every par LIBOR swap prices to zero (`Σ L̂·d = C·A`); (3) fixed PV − floating PV with floating = 1 + X·A; (4) shortcut `NPV = (c − C)·A_OIS`; (5) between resets floating = `(100 + 100·L₀d₀/360)/(1 + L·d/360)`; hedge fixed and floating legs separately.
**Trade-offs**: needs actual collateral at OIS; uncollateralized trades need CVA/FVA (ch16, ch17).

## CMS convexity correction
**When to use**: price swap-rate-linked payments.
**How**: forward swap rate per date, variance from normal swaption vol, add `Var·[1/C − T·(1 + C/2)^(−2T−1)/(1 − (1 + C/2)^(−2T))]`, PV and divide by annuity (3.25bp for 5y CMS, 60bp vol, flat 4%).
**Trade-offs**: grows with variance and tenor; ignores skew (ch16).

## Options pricing by numeraire
**When to use**: caps, swaptions, bond and futures options.
**How**: map product to underlying/numeraire/h₀ (caplet `τd(T+τ)`, swaption annuity, bond option `d(T)`); normal `ξᴺ = (S − K)N(d) + σ√T·n(d)`; ATM `0.3989σ√T`; callable = noncallable − call; price vol `= σ_bp·DV01/P`; mark smiles with SABR and calibrate to the backbone.
**Trade-offs**: flat-vol deltas wrong under skew; ED options approximate (ch18).

## Credit: spread, hazard and CDS conversion
**When to use**: quote, compare and convert credit instruments.
**How**: compare on OAS or CDS-equivalent spread; credit triangle `s ≈ λ(1 − R)`; solve λ so fee leg = contingent leg (R = 40%); `UF = (C(T) − C)× risky annuity`; reprice with 1bp curve shift for credit-adjusted DV01; negative basis: compute breakeven cost of capital.
**Trade-offs**: needs term funding; yield spread mixes options and coupon effects (ch19).

## MBS valuation and hedging
**When to use**: pass-throughs, IOs/POs, TBA.
**How**: payment `X = B·(y/12)/[1 − (1 + y/12)^(−12T)]`; SMM↔CPR; refinancing S-curve plus turnover, defaults, curtailments; Monte Carlo along risk-neutral paths with burnout, solve OAS; hedge with 5y and 10y Treasuries using empirical ratios (4% TBA: 0.66/1.15).
**Trade-offs**: OAS blends value and model error; roll vs repo depends on specialness (ch20).

## Flat-forward curve construction and hedge test
**When to use**: build a swap/futures pricing curve.
**How**: stub from deposit, ED rates adjusted for convexity and converted to continuous; flat forwards bootstrapped so each benchmark pins one segment; check by repricing; compute partial '01s by bump-and-refit; test locality (hedges only in nearby swaps).
**Trade-offs**: smoothing keeps benchmarks priced but spreads hedges across distant buckets (ch21).
