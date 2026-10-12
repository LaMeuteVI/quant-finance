# Chapter 5: Multi-Factor Risk Metrics and Hedges
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 5 (Part Two: Measures of Interest Rate Risk and Hedging) · Examples: C-STRIP of 5/15/2040, market-maker book hedged with on-the-run 2/5/10/30-year Treasuries, 2.12% 5-year EUR swap, EUR 5x10 payer swaption, all as of 28-May-2010

## Core Idea
One-factor DV01 silently assumes that the 6-month rate and the 30-year rate move by the same amount, so it will happily hedge a 30-year bond with a bill. Curve risk (rates at different terms moving by different amounts) is measured by splitting the total DV01 into exposures to several regions of the curve, each tied to a liquid hedging instrument. Three standard decompositions exist: key-rate '01s (bond desks, par-yield shifts), partial '01s (swap desks, shifts of the curve-fitting inputs) and forward-bucket '01s (intuitive picture of where the risk sits, shifts of forward rates). The more hedging securities you use, the fewer assumptions you need about co-movement of rates, and the higher the cost.

## Frameworks Introduced
- **Curve risk**: the risk that rates along the term structure move by different amounts (steepening, flattening, butterfly).
  - When to use: any portfolio that is not a single-maturity position, any relative-value book, any benchmarked mandate.
  - Why it matters: a manager with the benchmark's duration but concentrated in 30-year bonds matches the index for parallel moves, underperforms if the curve steepens, outperforms if it flattens.
- **Key-rate shifts (Ho, 1992)**: choose key rates (popular US choice: 2-, 5-, 10-, 30-year **par yields**). A 1bp move of a key rate moves par yields by 1bp at its own term, declining linearly to zero at the adjacent key-rate terms; constant 1bp below the shortest key term (2y shift) and beyond the longest (30y shift).
  - Design property: the four shifts sum to a **parallel 1bp shift**, so key-rate '01s decompose a DV01 and key-rate durations decompose a duration.
  - Assumptions (strong): a rate is affected only by its two neighbouring key rates, and linearly. In reality a move in the 2y alone would also change the 7y to keep sensible curvature. Tractability is judged to outweigh these flaws.
- **Key-rate '01 and key-rate duration**: `DV01ₖ = −(1/10,000)·∂P/∂yₖ`; `Dₖ = −(1/P)·∂P/∂yₖ` (per 100bp, i.e. ×10,000 on the per-bp change).
  - How: 1) build the base pricing curve (spot/discount curve consistent with par yields); 2) apply each key-rate shift to par yields, re-derive the implied spot curve, reprice; 3) `DV01ₖ = −(P_shifted − P_base)/(shift in bp)`; 4) sum across key rates and compare with yield-based DV01 (close, not equal).
- **Key-rate hedge (solve the linear system)**: choose face amounts F₂, F₅, F₁₀, F₃₀ of the on-the-run key bonds so that every net key-rate '01 is zero: `Σⱼ (KR01ᵢⱼ/100)·Fⱼ + Position KR01ᵢ = 0` for each key rate i.
  - Quick version used on desks: hedge the biggest exposure bucket by bucket with `F ≈ −KR01 to hedge / (KR01 of on-the-run per 100 face/100)`, then re-neutralize total DV01 with one more bond (the "alternate hedge").
- **Partial '01s**: change in value for a 1bp **decline** of one fitted rate (LIBOR/deposit, futures, par swap rates used to build the curve), other fitted rates unchanged, **curve refitted**.
  - When to use: swap books, or bonds plus swaps, when the hedging instruments are the curve-building instruments.
  - Advantage: a fitting security's entire '01 lands in its own partial '01 (shifts are defined on the instrument rates themselves), so hedges are nearly diagonal and trivial to compute.
  - Practice: trade enough fitting securities to reach an acceptable partial-'01 profile, not all of them.
- **PV01**: change in value when all fitting-security rates fall 1bp (DV01 analogue, with the curve-fitting methodology defining all other rates). Partial '01s decompose PV01, with a day-count caveat (see Practitioner Notes).
- **CV01**: change in a swap's value for a 1bp drop of its fixed coupon; proportional to the annuity factor. Equals PV01 for par swaps (annuity factor = 100 × DV01 of a par swap), hence the frequent confusion.
- **Forward-bucket '01s**: split the curve into buckets (example: 0-2, 2-5, 5-10, 10-15, 20-30 years), shift all forward rates inside one bucket by 1bp (semiannual forwards in the example), reprice; `'01 = −(P_shifted − P_base)`. Shifting all buckets gives the DV01-like "All" column.
  - When to use: to *understand* where a position's curve risk lives (most intuitive), less for picking hedge trades.
  - Bucket design: a financing desk wants many narrow short buckets and few long ones; a swap market-maker wants more, narrower buckets across the curve and, in Europe, beyond 30 years.
- **Portfolio volatility from multi-factor exposures**: with key-rate '01s and a covariance matrix of key-rate changes, `σ²_P = Σᵢ Σⱼ KR01ᵢ KR01ⱼ ρᵢⱼ σᵢ σⱼ`. Two-factor case below.

## Key Concepts
- **Curve risk**: exposure to non-parallel moves; invisible to a single DV01.
- **Key rate**: one of a small set of benchmark par yields (2-, 5-, 10-, 30-year) from which all other rates are derived by a fixed rule.
- **Key-rate shift**: the piecewise-linear 1bp par-yield "tent" attached to one key rate.
- **Key-rate duration profile**: the vector of Dₖ; the Lehman Aggregate at end-2004 had 0.145 / 0.655 / 1.151 / 1.239 / 0.800 / 0.349 at 6m/2/5/10/20/30y, total 4.339 (over half at 5y and 10y).
- **Replicating-portfolio reading**: a 30-year zero equals long a 30-year par bond, plus smaller shorts in 10-, 5- and 2-year par bonds (the par bond's coupons create short-term exposures to be offset).
- **Implied spot-rate shift**: the spot-curve move implied by a par-yield shift; steeper than the par shift and can be negative at the far end.
- **Partial '01**: '01 to one curve-fitting input rate with the curve refitted.
- **PV01**: value change for a 1bp fall in all fitting-security rates.
- **CV01**: value change of a swap for a 1bp coupon decline (annuity-factor based).
- **Forward bucket**: a maturity region whose forward rates are shifted together.
- **Forward-bucket '01**: `−ΔP` for a 1bp shift of the forwards in one bucket.
- **Spot-starting vs forward-starting swap**: 5x10 swap = 10-year swap starting in five years; settles T+2.
- **Payer swaption**: right to pay fixed on a swap at a future date; negative '01 (gains as rates rise).
- **Steepener**: position that profits if long-term yields rise relative to short-term yields (loses if the curve flattens).

## Formulas & Reference Tables
- Key-rate '01: `DV01ₖ = −(1/10,000)·∂P/∂yₖ` (5.1)
- Key-rate duration: `Dₖ = −(1/P)·∂P/∂yₖ` (5.3)
- Sum property: `Σₖ DV01ₖ ≈ DV01 (parallel par shift)`; not exactly yield-based DV01 (which shifts the security's own yield). E.g. the sum of 30-year spot changes across the four shifts is 1.08bp, so a 30y zero's key-rate sum is about 1.08 × its yield-based figure.
- Hedge ratio from sums (initial DV01 hedge): `F_hedge = F_pos × (ΣKR01_pos)/(ΣKR01_hedge)`.
- Key-rate hedge system (4 equations, 4 unknowns, per 100 face ÷ 100): `M·F = −KR01_position`, with M lower-triangular-dominant because on-the-run bonds load mainly on their own key rate.
- Two-factor portfolio: `ΔP = KR01₁·ΔC₁ + KR01₂·ΔC₂` (5.13) and `σ²_P = KR01₁²σ₁² + KR01₂²σ₂² + 2·KR01₁·KR01₂·ρ·σ₁σ₂` (5.14). One-factor special case: DV01 × rate vol.
- Appendix (two-period fixed leg, fictional notional): `P = c/(1+f₁) + (1+c)/[(1+f₁)(1+f₂)]` (5.15)
  - `−∂P/∂f₁ = c/(1+f₁)² + (1+c)/[(1+f₁)²(1+f₂)]` (5.16); `−∂P/∂f₂ = (1+c)/[(1+f₁)(1+f₂)²]` (5.17)
  - If f₁ = f₂ the first bucket's '01 exceeds the second (f₁ discounts more cash flows). If c = 0, bucket 2 risk < bucket 1 risk iff `f₁ < f₂` (upward slope lowers later-bucket risk).

**Key-rate profile of the 15-May-2040 C-STRIP (per 100 face, price 26.22311)**

| Shift | Shifted value | KR '01 | KR duration |
|---|---|---|---|
| 2-year | 26.22411 | −.0010 | −.38 |
| 5-year | 26.22664 | −.0035 | −1.35 |
| 10-year | 26.25763 | −.0345 | −13.16 |
| 30-year | 26.10121 | +.1219 | 46.49 |
| Total | | .0829 | 31.60 |

**Key-rate '01 per 100 face of the hedging bonds (28-May-2010)**

| Bond | 2y | 5y | 10y | 30y | Sum |
|---|---|---|---|---|---|
| .75s 5/31/12 | .0199 | 0 | 0 | 0 | .0199 |
| 2.125s 5/31/15 | 0 | .0480 | 0 | 0 | .0480 |
| 3.5s 5/15/20 | 0 | −.0001 | .0870 | 0 | .0869 |
| 4.375s 5/15/40 | 0 | .0001 | .0010 | .1749 | .1760 |

**Forward-bucket '01s (EUR, per 100 notional, 28-May-2010)**

| Security | 0-2 | 2-5 | 5-10 | 10-15 | All |
|---|---|---|---|---|---|
| 5x10 payer swaption (4.044%) | .0010 | .0016 | −.0218 | −.0188 | −.0380 |
| 5-year swap (2.12%) | .0196 | .0276 | 0 | 0 | .0472 |
| 10-year swap (2.943%) | .0194 | .0269 | .0394 | 0 | .0857 |
| 15-year swap (3.29%) | .0194 | .0265 | .0383 | .0323 | .1164 |
| 5x10 swap (4.044%) | 0 | 0 | .0449 | .0366 | .0815 |

## Mental Models
- **Hedge count = assumptions avoided**: one hedge instrument needs a full assumption about how rates co-move; one per cash flow needs none but is prohibitively costly. Key rates, partial '01s and buckets sit in the sensible middle.
- **Bond desk = key rates, swap desk = partial '01s, risk manager = buckets**: pick the decomposition by what the hedge instruments are (on-the-runs, curve-fitting swaps) and who has to read the report.
- **A zero is not a par bond of the same maturity**: coupons of the par bond create exposure at shorter terms, so a zero carries *negative* short key-rate '01s (the 10y par shift pushes the 30y spot rate down about 0.45bp, raising the zero's price).
- **Sum of exposures is the old DV01; the shape is the new information**: always check the row sums to zero after hedging (DV01-neutral), then look at the profile for the hidden curve trade.
- **Bucket '01 drivers** (four effects): a swap is exposed only up to its maturity; wider buckets have bigger '01s; later shifts touch fewer coupons; higher forward rates lower '01. Combine them to predict the shape before computing.
- **Options add curve risk at the front end**: a 5x10 payer swaption has small positive '01 in the 0-5y buckets because those forwards discount its payoff at expiry.

## Worked Example
Market maker on 28-May-2010 (figures from the chapter, recomputed).

1. Position: short $100mm 0s of 5/15/40 (C-STRIP) hedged with $47.077mm long 4.375s of 5/15/40, because `0.0829/0.1760 × 100 = 47.10` (sums of KR01). Short $40mm 3.5s of 5/15/20 hedged with $72.446mm long 2.125s of 5/31/15, `0.0869/0.0480 × 40 = 72.42`. Both DV01-neutral.
2. Hidden risk. Key-rate '01 profile of the book in dollars (2y / 5y / 10y / 30y) is +1,000 / +38,377 / +198 / −39,578, summing to 0: a large 5s-30s steepener (makes money if the 30y rate rises versus the 5y). Check the 5y figure: `72.446×.0480/100 − 40×(−.0001)/100 − 100×(−.0035)/100 + 47.077×.0001/100 = 0.03836` ($38,361; the table's $38,377 differs by rounding).
3. Exact hedge: solve the 4×4 system (5.8 to 5.11): F₃₀ = +$22.63mm, F₁₀ = −$0.49mm, F₅ = −$80.00mm, F₂ = −$5.03mm by my solve (the book prints −$5.190mm; the book's own 2y equation `1000/(0.0199/100)` gives 5.03, so treat the printed 5.19 as a rounding/typo issue, immaterial to the profile).
4. Shortcut: sell `38,377/0.048% = $79.95mm` of the 5y and buy `39,578/0.1749% = $22.63mm` of the 30y.
5. Alternate desk hedge: sell $80mm of the 5y, then buy F₃₀ with `F₃₀ × 0.1760/100 = 80 × 0.0480/100` so F₃₀ = $21.82mm. Net profile +1,031 / −2 / +415 / −1,447 dollars, a tiny residual 2s-30s steepener. Good enough; the exact hedge gains little for a lot of trading.

Payer swaption (per 100 notional): forward-bucket '01 total −.0380.
- Hedge #1, long 10y swaps: `0.0380/0.0857 = 44.34%`; net buckets +.0096 / +.0135 / −.0043 / −.0188, still heavily exposed to flattening.
- Hedge #2, long 5x10 swaps: `0.0380/0.0815 = 46.6%` (book prints 46.66%); net ≈ .0010 / .0016 / −.0009 / −.0017, almost flat.
- Hedge #3, long 15y swaps to kill the 5-15y buckets (about 57.6% of 15y), short 5y swaps to kill the front end; net within ±.0002 of zero in every bucket. Use it when forward swaps are hard to execute.

Portfolio volatility example (my numbers): KR01₁ = $10,000 (5y), KR01₂ = −$4,000 (30y), σ₁ = 100bp, σ₂ = 80bp, ρ = 0.8: `σ_P = √(10⁴²·100² + 4000²·80² + 2·10⁴·(−4000)·0.8·100·80) = $768,375`, versus $600,000 if one wrongly used the net DV01 ($6,000) × 100bp.

## Anti-patterns
- **Hedging with one instrument and calling the book flat**: a zero total DV01 can coexist with a large steepener (here a 5s-30s of about $39k/bp).
- **Reading key-rate '01s as yield-based numbers**: key-rate shifts move par yields, yield DV01 moves the security's own yield; sums match only approximately.
- **Assuming an on-the-run bond has a pure key-rate profile**: only a bond maturing exactly at the key term and priced at par does; the 3.5s of 2020 still carries −.0001 at 5y.
- **Zeroing every partial '01**: too costly; target an acceptable profile.
- **Mixing day counts then summing partial '01s**: LIBOR-type rates are act/360, swap fixed legs 30/360; a 1bp move in each is not one consistent 1bp, so partial '01s do not sum exactly to PV01.
- **Using a single DV01 × single volatility for risk**: the 10y par rate is usually more volatile than the 30y; one number hides term structure of volatility and imperfect correlation.
- **Using bucket '01s to choose hedges directly**: they show where risk is, not which instrument to trade.

## Practitioner Notes
- Key-rate sets are chosen by liquidity: recently issued near-par governments (2-, 5-, 10-, 30-year in the US); swap books use more fitting instruments (deposit, futures, swaps), so partial '01 reports are larger.
- Converting all rates to one day count makes partial '01s sum exactly to PV01 but breaks the property that a fitting security's '01 equals its '01 to its own quoted rate; desks usually keep the market-quoted bases.
- Swap-based managers (insurers, pensions hedging credit or mortgage assets, multi-desk supervisors, government relative-value investors hedging curve with swaps) must also monitor spread risk between bonds and swaps, which these metrics do not capture.
- Volatility from key-rate '01s needs n vols and n(n−1)/2 correlations; with partial '01s or buckets that explodes, so key rates are the practical choice for risk aggregation.
- Typical quick desk hedge: neutralize the largest bucket with the on-the-run, then fix total DV01 with a second bond (the "alternate hedge").
- Forward-bucket design should follow the desk's business (narrow short buckets for financing desks).

## Key Takeaways
1. Total DV01 hides curve risk; always report '01s by region (key rates, partial '01s or forward buckets).
2. Key-rate shifts are 1bp par-yield tents that sum to a parallel 1bp shift, so the profile decomposes DV01 and duration.
3. A zero has negative key-rate '01s at shorter terms; a long-dated zero is not a par bond of the same maturity.
4. Hedge in two passes: DV01-neutralize with sums, then read the profile and flatten the biggest bucket exposure with on-the-runs.
5. Use partial '01s when the curve is built from swap instruments: hedges are almost diagonal.
6. Use forward-bucket '01s to explain and visualize risk, and to check that a hedge (e.g. swaption vs 5x10 swap) really removes it.
7. Bucket '01s depend on maturity, bucket width, position along the curve and forward level.
8. Portfolio volatility needs correlations: `σ²_P = ΣΣ KR01ᵢKR01ⱼρᵢⱼσᵢσⱼ`; ignoring them misstates risk.

## Connects To
- **ch04**: one-factor DV01, duration, convexity and the hedge ratio that this chapter generalizes.
- **ch02**: par, spot, forward rates and the annuity factor behind CV01.
- **ch03**: forward-rate based P&L decomposition (carry, roll-down) that buckets refine.
- **ch06**: empirical (regression and PCA) hedges, the statistical alternative to the assumed key-rate shapes.
- **ch16**: swap DV01, PV01 and CV01 details.
- **ch18**: swaption pricing and delta hedging behind the bucket '01s of the payer swaption.
- **ch21**: curve construction, which defines the fitting securities for partial '01s.
- **`cfa-level1-curriculum` ch18**: key rate duration as it appears in the CFA curriculum.
