# Chapter 17: Arbitrage with Financing and Two-Curve Discounting
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 17 · Selected Securities and Topics (with contributions acknowledged to Jean-Baptiste Homé)

## Core Idea
Discounting is shorthand for arbitrage pricing, but only under specific **financing conditions**. For bonds, the law of one price holds only if every bond finances at the same repo rate and interim mispricings can be financed at that rate. For swaps, non-par swaps can be priced off a par curve only if they share one floating index, collateral earns that same index, and interim mispricings finance at it. Once fed funds (OIS) replaced LIBOR as the riskless investable and collateral rate, the single-curve method stopped being correct. The replacement is **two-curve pricing**: discount everything on the OIS curve, and project LIBOR from a separate curve built so that par LIBOR swaps price to zero.

## Frameworks Introduced
- **Financed long / short bond positions (repo accounting)**
  - A short is done through repo. You sell the bond for P₀, post that cash as collateral (you "buy the repo") and earn the repo rate r. It generates **no cash today**.
  - The long side has to be financed by "selling the repo", i.e., borrowing P₀ against the bond.
  - One-period short P&L = `P₀(1+r) − (P₁ + c)`. It profits if the bond's total return is below the repo rate.
  - Financed long P&L = `P₁ + c − P₀(1+r)`. It profits if total return exceeds repo.
  - No-arbitrage for a one-period bond: `P₀ = (1+c)/(1+r)`. The first forward rate must equal the term repo rate.
  - Multi-period financed long, flow from t−1 to t: `Pₜ + c − Pₜ₋₁(1 + rₜ₋₁)`.
- **Three-scenario anatomy of a relative-value arbitrage** (Tuckman's 3/4s of Nov-2011 example: cheap bond at 100.190 vs replicating portfolio at 100.255, a 6.5-cent mispricing, 6-month GC repo .149%)
  - **Scenario I, same repo and convergence**: the profit is the **future value of the initial mispricing at the repo rate**, not the mispricing itself (the initial cash flow is zero).
  - **Scenario II, the rich side trades special**: the replicating bonds repo at 0% vs GC .149%. The trade loses (−.00964) even though prices fully converge, because **specialness can explain apparent richness**.
  - **Scenario III, interim divergence**: the gap widens from 6.5 to 10 cents. Staying in the trade needs a cash injection (3.5 cents), because the repo lenders re-margin each leg at its new price. Without capital the trade is unwound at a loss.
  - When to use: before calling any bond "cheap" versus a fitted curve or replicating portfolio.
  - Failure mode: ignoring differential repo and the capital needed to survive divergence, which is how relative-value funds blow up.
- **Proposition 1 (bond arbitrage with financing)**: two portfolios with identical cash flows must have the same price if (a) both always finance at the same rate and (b) interim mispricings can be financed at that rate. The terminal profit is then `−δ₀(1+r₁)(1+r₂)···(1+r_T)`, where δ₀ is the initial richness of the long leg (negative when it is cheap). This holds **whatever the path of interim mispricings**.
- **Swap vs. financed bond equivalence**
  - Receiving fixed looks like a financed bond purchase, except for how it is financed.
  - The fixed leg's value PVₜ = 1 + NPVₜ. The **notional (1) finances at the floating index Lₜ**, while the **NPV finances at the collateral rate rₜ**.
  - Swap flow at t: `c + PVₜ − PVₜ₋₁ − Lₜ₋₁ − NPVₜ₋₁·rₜ₋₁`.
  - Bond flow at t: `c + Pₜ − Pₜ₋₁ − Pₜ₋₁·rₜ₋₁`.
- **Proposition 2 (swap arbitrage with financing)**: two cash-matched swap portfolios on one floating index must have equal value if the riskless investable rate **and** the collateral rate equal that floating index, and interim mispricings finance at that index. The terminal profit is `−δ₀(1+L₁)···(1+L_T)`. If collateral earns rₜ ≠ Lₜ, a residual `(F^A − F^B)(rₜ − Lₜ)` appears every period and replication fails (Tuckman's Scenario II: collateral at .25% vs LIBOR at .705%).
- **Arbitrage pricing of a LIBOR swap under fed funds collateral** (three-swap replication)
  1. Receive `c_L` vs LIBOR (collateral earns fed funds). This is the swap to price.
  2. Receive `c_FF` vs fed funds (an OIS swap). Its floating leg is worth par because fed funds is riskless and investable, so any OIS swap is priced off par OIS rates.
  3. Receive fed funds + X(T) vs LIBOR, the T-year **basis swap**, fair at zero upfront.
  - (2) + (3) with `c_FF = c_L − X(T)` has the same interim flows as (1), so `NPV_L = NPV_FF(c_L − X(T))`.
- **Two-curve pricing (Proposition 4)**
  1. Build the OIS discount curve (d(t), A(t) from forwards f(t)).
  2. Build **projected ("adjusted") LIBOR** L̂(t) iteratively so that the PV of the floating leg equals the PV of the fixed leg for every par LIBOR swap (Corollary 1). The basis swaps are used implicitly.
  3. Value any swap by discounting fixed flows and projected floating flows on the OIS curve.
  - Why it works: it reproduces the three-swap replication for every maturity.
  - Failure mode: it relies on collateral actually earning the OIS rate. Uncollateralized trades need a funding/credit adjustment (see `hull-derivatives` ch09).

## Key Concepts
- **Buying / selling the repo**: lending cash against bonds (the short seller's side) / borrowing cash against bonds (the financed long's side).
- **Special repo rate**: a below-GC repo rate on a bond in high demand to borrow. Its cost to shorts can offset apparent richness.
- **GC (general collateral) rate**: the repo rate on generic collateral, the default financing rate.
- **Interim mispricing**: a deviation of relative value before convergence. It must be financed with capital, which is the arbitrageur's real constraint.
- **Future value of mispricing**: the arbitrage profit rolled at realized financing rates. It is independent of the divergence path if interim cash finances at those same rates.
- **Collateral rate**: the interest paid on posted swap NPV collateral (CSA rate). In USD it is typically fed funds.
- **Riskless investable rate**: the rate whose floating leg is worth par. Post-crisis it is fed funds / OIS, not LIBOR.
- **OIS (overnight indexed swap)**: fixed vs compounded overnight rate. Its par curve is the discount curve.
- **LIBOR–OIS basis swap spread X(T)**: the fixed spread over fed funds that makes fed funds + X fair against LIBOR. Positive, and large in the crisis.
- **Projected (forward) LIBOR curve**: forward rates used only to generate floating cash flows, not to discount.
- **Two-curve discounting**: separate discount (OIS) and projection (index) curves.
- **Blended financing rate of a swap**: the notional finances at the floating index and the NPV at the collateral rate.

## Formulas & Reference Tables
- One-period short: `P₀(1+r) − (P₁+c) > 0 ⇔ (P₁+c−P₀)/P₀ < r`.
- One-period financed long: `P₁ + c − P₀(1+r)`. No-arbitrage `P₀ = (1+c)/(1+r)`, so `f(1) = r`.
- Arbitrage accumulation (Prop. 1): date-t cash `δₜ − δₜ₋₁(1+rₜ)`, cumulated to `−δ₀ Πₜ(1+rₜ)` at T.
- Swap arbitrage residual with collateral ≠ index: `(Fₜ₋₁^A − Fₜ₋₁^B)(rₜ − Lₜ)` per period.
- **OIS-collateralized LIBOR swap NPV** (Prop. 3): `NPV = [c(T) − X(T)]·A(T) + d(T) − 1`, with A(T) = Σ τᵢ d(tᵢ) and d(T) from the **OIS** curve (one period per year in the book's notation).
- Par LIBOR rate vs basis: `[C(T) − X(T)]·A(T) + d(T) = 1 ⇒ C(T) = X(T) + (1 − d(T))/A(T) = X(T) + OIS par rate(T)`, when the fixed and basis legs share payment conventions.
- **Useful corollary**: `NPV of receiving c = [c − C(T)]·A_OIS(T)`. A non-par swap is worth its off-market coupon times the **OIS** annuity.
- Projected LIBOR (Corollary 1): `Σₛ₌₁ᵗ L̂(s)·d(s) = C(t)·A(t)`, equivalently `= 1 + X(t)A(t) − d(t)`. Solve bootstrap-style for L̂(1), L̂(2), ….
- The PV of a LIBOR floating leg under OIS discounting is `1 + X(T)A(T) > 1`: **receiving LIBOR is worth more than par** because LIBOR > fed funds.

| Setting | Discount at | Project floating at | Floating leg PV | Non-par swap off par curve? |
|---|---|---|---|---|
| Pre-crisis textbook (LIBOR riskless, collateral at LIBOR) | LIBOR par-swap curve | same curve | par | Yes |
| LIBOR swap, collateral at fed funds, LIBOR taken riskless | LIBOR curve | LIBOR curve | par | **No** (NPV finances at FF ≠ LIBOR) |
| Post-crisis (FF riskless, collateral at FF) | **OIS curve** | **LIBOR projection curve** (from par LIBOR swaps or LIBOR-OIS basis) | `1 + X·A` | Only via the two-curve method |
| Fixed vs 1M LIBOR, collateral FF | OIS | 1M LIBOR projection (1M-FF basis) | `1 + X₁ₘ·A` | Two-curve |

**Valuation error of single-curve pricing** (Tuckman Tables 17.11–17.12, USD, 28-May-2010; error = rate a single-curve desk quotes minus the true rate for the same NPV, in bp):

| Term | LIBOR-OIS basis (May-2010) | Error, coupon +200bp over par | +100bp | Crisis basis | +200bp | +100bp |
|---|---|---|---|---|---|---|
| 2y | 48 | 1.2 | 0.6 | 100 | 2.1 | 1.1 |
| 5y | 38 | 2.3 | 1.2 | 60 | 4.2 | 2.1 |
| 10y | 30 | 3.6 | 1.8 | 45 | 5.8 | 2.9 |

The error grows with the **off-marketness** (a bigger NPV means more collateral mis-rated), with **term** (discounting at LIBOR instead of FF) and with the **basis**. Compare it with a bid-ask of 0.25–0.5bp. Rough check: `error ≈ (c − C)(1 − A_LIBOR/A_OIS)`.

## Mental Models
- **"The initial cash flow of a real arbitrage is zero."** The mispricing is harvested only at convergence, compounded at the financing rate. Everything in between is capital at risk.
- **Think of a received-fixed swap as a bond bought with two loans.** The notional is borrowed at the floating index and the NPV at the collateral rate. Pricing is consistent only when both rates are equal, or when you explicitly price the gap.
- **Cheapness net of repo.** A bond that looks rich on the curve may simply be "paying" its holder through specialness. Always compare the richness to the repo carry advantage over the horizon (see ch12).
- **Discount at what the collateral earns, project at what the index pays.** This single sentence is the two-curve method.
- **A non-par swap's value = off-market coupon × OIS annuity.** The LIBOR curve affects the value only through the par rate C(T).

## Worked Example
**A. Tuckman's financed arbitrage (checked).** Buy the cheap 3/4s at 100.190 financed at .149% for 6 months, short the replicating portfolio at 100.255 lending cash at the repo rate.
- Scenario I, both at .149%, converge: payoff = 0.065 × (1 + .00149/2) = **+0.06505**.
- Scenario II, replicating bonds special at 0%: 100.255 − 100.190 × (1.000745) = **−0.00964**. The special cost of 100.255 × .0745% ≈ 7.5 cents over-eats the 6.5-cent mispricing.
- Scenario III, the gap widens to 10 cents: 0.06505 + (100.40 − 100.50) = **−0.03495**. That is the cash infusion needed to stay in.

**B. Two-curve valuation (book Exercise 17.1, solved).** Annual 1y/2y par LIBOR swaps are 2% and 2.75%. OIS forwards are 1% (year 1) and 2% (year 2).
1. OIS discount factors: d(1) = 1/1.01 = 0.990099, d(2) = d(1)/1.02 = 0.970685. A(2) = 1.960784.
2. Projected LIBOR: L̂(1)·d(1) = 2%·d(1), so L̂(1) = **2.000%**. Then L̂(1)d(1) + L̂(2)d(2) = 2.75%·A(2), so L̂(2) = **3.515%**. Compare the OIS forward of 2%: the implied basis is about 150bp in year 2.
3. NPV of receiving 3% for 2y = (3% − 2.75%) × A(2) = **0.004902 per unit** (0.49 per 100). Direct check: 0.03·A(2) + d(2) − [L̂(1)d(1) + (1+L̂(2))d(2)] = 0.004902.
4. Implied LIBOR-OIS basis term structure (Exercise 17.2): X(1) = C(1) − (1−d(1))/A(1) = 2% − 1% = **100bp**. X(2) = 2.75% − 1.4950% = **125.5bp** (the 2y OIS par rate is 1.4950%).
Interpretation: LIBOR projections sit above OIS forwards by the (forward) basis. Discounting on OIS makes a received-fixed off-market swap worth `(c − C)·A_OIS`, slightly more than the single-curve `(c − C)·A_LIBOR`.

## Anti-patterns
- **Booking the initial mispricing as P&L**: realized profit is the financed future value, and only if you survive to convergence.
- **Ignoring repo specialness in RV screens**: a "rich" on-the-run may be fairly priced once its repo advantage is counted.
- **Sizing an RV trade without a capital buffer for divergence**: repo counterparties re-margin at market prices, so divergence forces cash calls or forced unwinds (the LTCM mechanism).
- **Discounting collateralized swaps on the LIBOR curve**: it misprices off-market swaps by basis points that exceed the bid-ask. The sign favors the collateral receiver.
- **Assuming the LIBOR floating leg is worth par under OIS discounting**: it is worth `1 + X·A`.
- **Using the OIS curve to project LIBOR fixings**: the projection must embed the LIBOR-OIS basis.
- **Applying CSA-based discounting to uncollateralized trades**: the funding rate then differs, so use FVA/CVA-style adjustments instead.

## Practitioner Notes
- **Industry standard since the crisis**: two-curve (OIS discounting + index projection) became the norm across dealers and CCPs. In USD, EUR and GBP the legacy LIBOR is now replaced by SOFR, €STR and SONIA RFRs. The same logic survives for any tenor basis (e.g., term vs overnight, or EURIBOR 6M vs €STR): discount at the collateral rate and project each index from its own curve.
- **Who benefits from ignoring the collateral rate?** The side that receives collateral gains. The **receiver of an above-par coupon** (and the payer of a below-par coupon) receives collateral. It borrows the NPV at fed funds while "investing" it through the swap at LIBOR, so it values the swap above the single-curve price. Hence `c₁ > c₂` in Tuckman's error tables.
- **Numbers the author commits to**: 2–10y LIBOR-OIS basis of 30–48bp in May 2010 (above the long-run history, below the crisis peaks of hundreds of bp). Single-curve errors run 0.6–3.6bp in normal times and up to ~6bp at crisis bases.
- **Arbitrage capital**: Tuckman stresses that the right rate for financing interim mispricings is often the **cost of capital**, not repo. That is why true arbitrage is limited and mispricings persist.
- **Curve-build order in practice**: OIS curve first (from OIS swaps, and FF futures at the front). Then the projection curve, solving for projected fixings such that par swaps (or basis swaps) reprice. See ch21 for fitting choices.
- ⚠ **Correction**: the text states the collateral return as `−NPVₜ₋₁(1 − rₜ₋₁)`. It should be `−NPVₜ₋₁(1 + rₜ₋₁)`, consistent with Table 17.6 and eq. (17.10).

## Key Takeaways
1. Real arbitrage starts with zero cash. The profit is the initial mispricing compounded at the financing rate, and it is realized only if interim divergences can be funded.
2. The law of one price for bonds requires equal repo rates. Special repo can fully justify apparent richness.
3. A swap's notional finances at its floating index and its NPV at the collateral rate. Single-curve discounting is exact only when these coincide.
4. With fed funds riskless and as the collateral rate: LIBOR swap = OIS swap at `c − X(T)` + basis swap, so `NPV = [c − X(T)]A_OIS + d_OIS − 1`.
5. Two-curve method: discount on OIS and project LIBOR so par LIBOR swaps reprice. Then a non-par swap is worth `(c − C)·A_OIS`.
6. Single-curve valuation errors scale with off-marketness × term × basis and exceed typical bid-asks.

## Connects To
- **ch01**: discount factors and the law of one price, assumed frictionless there and made rigorous here.
- **ch02**: forward rates. The one-period forward equals the term repo rate.
- **ch12**: repo mechanics, GC vs specials and specialness value, the inputs for Scenario II.
- **ch15**: LIBOR-OIS spread history and OIS / fed funds instruments.
- **ch16**: single-curve swap valuation, basis swaps and the fiction of notional exchange.
- **ch21**: building the OIS discount curve and the projection curve.
- **`hull-derivatives` ch09**: CVA/DVA/FVA, the adjustments needed when collateral terms differ from the CSA-OIS assumption.
- **`hull-derivatives` ch07 / ch34**: OIS discounting and swaps revisited.
- **`cfa-fixed-income` ch07–ch08**: arbitrage-free valuation and the swap curve as benchmark.
