# Chapter 20: Mortgages and Mortgage-Backed Securities
> **Source**: Tuckman & Serrat, *Fixed Income Securities* (3rd ed.), Chapter 20

## Core Idea
A fixed-rate mortgage is a non-prepayable amortizing loan plus a short position in an American call (the borrower's prepayment option) whose strike is the declining scheduled balance. Because prepayment is driven by behavior (refinancing, turnover, default, curtailment) and depends on the path of rates (burnout), MBS are valued by Monte Carlo with an empirical prepayment model, and summarized by OAS. The price-rate curve shows negative convexity at low rates, and IOs have negative duration.

## Frameworks Introduced
- **Level-payment mortgage and amortization table**: payment X solves PV(payments at the monthly-compounded mortgage rate) = original balance.
  - When to use: scheduled cash flows, balance after k payments, interest/principal split.
  - How: X = B(0)·(y/12)/[1 − (1+y/12)^−12T]. Interest at month n+1 = B(n)·y/12; principal = X − interest; B(n+1) = B(n) − principal. Shortcut: balance after k payments = PV of the remaining payments at the ORIGINAL mortgage rate.
  - Failure mode: the shortcut is a convention (flat curve, unchanged rates). Market value uses the current curve plus spread, and the prepayment option.
- **Prepayment option as American call**: the strike is the current scheduled balance; the borrower "should" prepay when PV of remaining payments > balance (rates down).
  - Difference from corporate calls: borrowers prepay inefficiently (costs, inattention, lock-in), so an MBS can trade well above par, unlike an efficiently called bond.
- **SMM / CPR conversion**: CPR = 1 − (1 − SMM)^12; SMM = 1 − (1 − CPR)^(1/12). Every month has its own CPR even though CPR is annualized.
- **Four-component prepayment model** (in order of importance): refinancing, turnover, defaults (and modifications), curtailments. Each is modeled separately and calibrated to history.
  - Refinancing: incentive I = (WAC − R)·WALS·A − K, then CPR = S-curve of I. Turnover adds a base level with seasonality and a seasoning ramp.
  - CPR(I) = T + 1/(a + e^(−bI)); a, b vary with credit (SATO, FICO, LTV), home-price appreciation, geography, and history (burnout).
- **Monte Carlo MBS valuation (path-dependent)**: (1) simulate risk-neutral short-rate paths; (2) compute scheduled cash flows and prepayments on each path, using path history; (3) discount each path backward; (4) average across paths. Bump the initial curve and revalue for sensitivities.
  - Why not a tree: burnout and media effects make cash flows path dependent, and trees do not remember the path.
  - Drawback: hard to value early-exercise claims (mortgage options, callable CMOs) because the continuation value is unavailable along a path.
- **OAS for MBS**: the constant spread added to the simulated short-rate paths that equates model value to market price. Hedged return is about short rate + OAS if the model is right.
- **Dollar roll vs MBS repo**: two ways to finance a pool. Roll = sell front-month TBA, buy back-month TBA.
- **Empirical TBA hedge ratios** (regression deltas vs 5y/10y Treasuries, Chapter 6 tools).

## Key Concepts
- **Agency / conforming loan**: eligible for securitization by FNMA, FHLMC or GNMA; creditworthy (typical FICO > 660, LTV < 80%, full documentation) and size-limited.
- **Non-agency**: jumbo (larger balance), Alt-A (one deviation), subprime (several deviations; about 80% were ARMs with teaser rates).
- **Pass-through**: pool cash flows (interest, scheduled principal, prepayments) are passed to investors after servicing and guarantee fees.
- **Servicer / guarantor**: servicer collects and forwards payments (20-50 bp fee); guarantor pays investors on default and pursues recovery. Coupon = WAC minus these fees.
- **WAC, WAM, factor**: WAC = loan-size-weighted mortgage rate; WAM = weighted-average maturity; factor = current/original principal.
- **Seasoning**: age of the loans. A pool issued at WAM 335 with "30-year" loans has slightly seasoned loans.
- **Specified pool vs TBA**: specified pools trade with known characteristics (price = TBA + pay-up); TBA is a liquid forward on a generic pool with a delivery option, where the seller delivers the cheapest pools.
- **Current coupon / current mortgage rate**: current coupon is the TBA coupon trading closest below par; current mortgage rate is the interpolated coupon that would price at par.
- **Curtailment**: partial prepayment.
- **Burnout**: CPR becomes less responsive to incentive as the most prepayment-prone borrowers leave the pool.
- **Media effect**: a new low in rates triggers refinancing by borrowers with low propensity.
- **Lock-in effect**: borrowers with below-market rates do not move, which reduces turnover.
- **SATO**: spread at origination, a credit proxy (high SATO pools prepay more slowly).
- **PAC / companion bond**: CMO tranches where the PAC gets a scheduled principal path and companions absorb prepayment variability.
- **IO / PO**: interest-only and principal-only strips. **CMM**: constant-maturity mortgage rate product, a convexity-free way to trade mortgage rates. **MSR**: mortgage servicing rights, IO-like.

## Formulas & Reference Tables
- `X = B(0)·(y/12) / [1 − (1 + y/12)^(−12T)]`  — monthly payment (y = annual mortgage rate, T = years).
- `Interest(n+1) = B(n)·y/12`;  `Principal(n+1) = X − B(n)·y/12`.
- `B(k) = X·[1 − (1+y/12)^−(12T−k)]/(y/12)`.
- `CPR = 1 − (1 − SMM)^12`.
- `I = (WAC − R)·WALS·A − K`: WALS = weighted-average loan size, A = annuity factor (PV of $1/yr at remaining maturity), K = refinancing cost; R lagged 1-2 months.
- `CPR(I) = T + 1/(a + e^(−bI))`: S-curve; T = turnover.
- `P₀ = E[ Σ CF_t / Π(1+r_i) ]`: Monte Carlo value = average over paths of path PV.
- `Roll value = (proceeds from selling front TBA + interest to back settlement − cost of back TBA on the reduced balance) − (coupon + principal paydown if held)`. Roll > 0: "above carry"; = 0: "breakeven".
- TBA pricing: prices in 32nds, "+" = 1/64.

| Product | Price behavior when rates fall |
|---|---|
| Non-prepayable mortgage | up, positive convexity |
| Fixed-CPR mortgage | up, positive convexity, lower DV01 than CPR 0 |
| Pass-through | up, then flattens; negative convexity |
| PO | up strongly (discount bond + discounting + accelerated par redemption) |
| IO | down (cash flows vanish); negative DV01 |

TBA hedge ratios (Dec 2010, face of Treasuries per 100 TBA, 10y / 5y): 3%: 0.93/1.64; 4%: 0.66/1.15; 5%: 0.43/0.75; 6%: 0.28/0.50; 6.5%: 0.23/0.40. They fall with coupon because higher coupons prepay faster and behave like shorter securities.

## Mental Models
- **"Interest lives off principal."** Early payments are mostly interest, later mostly principal. Prepaying principal kills future interest, which is why IOs lose value as rates fall.
- **Mortgage = bullet-like cash flows minus a call the holder of the loan has sold.** Think callable bond, but with a lazy caller, so the price can rise above par.
- **Path dependence means simulation.** If cash flows depend on history (burnout), use Monte Carlo, not a tree.
- **OAS is part value, part model error.** Trust it only when it mean-reverts and is uncorrelated with rates.
- **A specified pool is a TBA plus a pay-up.** Pools that prepay worse than the cheapest-to-deliver (low balance, high SATO, seasoned, geography) earn pay-ups.
- **Servicers are long an IO; originators in the pipeline are long rate risk.** The first hedges by buying convexity, the second by selling TBAs.

## Worked Example
1. Payment and first rows (verified): B = $100,000, y = 4%, 360 months. X = $477.42. Month 1 interest = 100,000 × 0.04/12 = $333.33, principal $144.08, balance $99,855.92. After 60 payments the PV of the 300 remaining payments at 4% is $90,447.5 (book rounds to $90,448), i.e. 90.4% of original.
2. CPR/SMM: SMM 0.5% gives CPR = 1 − 0.995^12 = 5.84%. The inverse for CPR 6% is SMM = 0.514%.
3. Pool with fixed 6% CPR (same loan, verified by simulation): month 1 total = 333.33 interest + 144.08 scheduled principal + 0.514% × (100,000 − 144.08) = 513.56 prepayment. After 60 months 66.4% of the balance remains, versus 90.4% with no prepayments. This is the same kind of drop as the FNMA 3.5% 2004 pool (factor about 68% after about 5 years). Weighted-average life is about 10.1 years versus about 18.0 years for a non-prepayable loan (recomputed), which is why a higher CPR acts like a shorter security (lower DV01).
4. Dollar roll (book example, recomputed): FNMA 5% July/Aug TBAs at 102.50 and 102.15; accrued 12/30 × 5%/12 × 100 = 0.167; paydown 2%; short rate 1%; $10mm balance. Sell July: $10,266,670. Interest 31 days at 1%: $8,841. Buy August on 98% balance: $10,027,037. Net = $248,477 (book shows $248,475 after rounding). Holding instead earns coupon + paydown = $241,667. Roll value about $6,808 (above carry). Interpretation: the forward drop exceeds carry, consistent with the delivery option, so it is not automatically a value opportunity.
5. Current mortgage rate: TBA 4% at 98-30+ (98.953) and 4.5% at 101-31+ (101.984). Linear interpolation to par gives about 4.17%; the current coupon is 4%.
6. Single Monte Carlo path (book Table 20.5): cash flows 25, 30, 35, 12, 11.32 at dates 1-5, discount rates 5%, 5%, 4%, 3%, 4% roll backward to a path value of about 100.9; average over all paths for the MBS price.

## Anti-patterns
- **Valuing an MBS as PV of scheduled payments with no prepayment model**: ignores a large short option; misprices duration and convexity.
- **Assuming efficient (call-optimal) prepayments**: borrowers are not optimizers; use empirical models and expect prepayments beyond the incentive (turnover, default).
- **Using a recombining tree with burnout**: the tree loses path history.
- **Hedging an IO-like servicing book with TBAs or swaps**: severe convexity mismatch, plus mortgage-swap basis risk for swaps.
- **Reading a large OAS as a free lunch**: it may be model misspecification. Check mean reversion, correlation with rates, and technical explanations.
- **Zero-volatility spread as the main measure**: forward rates are not expected rates, and price equals the discounted expected cash flow, not the cash flow discounted along the mean path.
- **Buying the TBA mean-reversion of OAS blindly in a credit crisis**: OAS hit about 100 bp cheap in 2007-2009, and credit deterioration was a genuine driver.

## Practitioner Notes
- Loan and pool coupons: coupon and age are the dominant pricing variables, but FICO, LTV, loan size and geography drive prepayment differences. High-balance pools are worth less because they use the prepayment option better.
- TBA is the liquid market; front contracts near par are the most active. Specified pools trade at a pay-up to TBA, and the pay-up grows as the delivery option becomes more valuable.
- Dollar roll: financing advantages over repo depend on the roll trading special (above carry). Differences from repo: you may not get back the same pool, and you forgo the month's payments (reflected in prices) and avoid the prepayment exposure. A roll trading above carry implies financing below the repo rate.
- Mortgage rate model: commonly a regression of the 30-year mortgage rate on the 10-year swap rate; simplistic but common.
- Empirical hedges: combine 5- and 10-year (or 7-year) Treasuries, since a single point does not capture curve exposure.
- Subprime facts: originations peaked 2004-2006; delinquencies on ARMs reached 25% by May 2008; by Sept 2010 principal exceeded home value for 23% of mortgages (California 32.8%, Florida 46.4%).
- Market size (2010): about $14tn US mortgage debt, $7.5tn securitized, $5.4tn agency. New issuance after the crisis was almost all agency.
- Servicing fee 20-50 bp; turnover typically under 10% of total prepayments; seasoning ramp to base turnover in about 30 months; curtailments can reach CPR of about 5% near maturity.

## Key Takeaways
1. Payment = PV-annuity inverse; balance = PV of the remaining payments at the original rate; interest is computed on beginning balance only.
2. A mortgage is a bond minus an American call on the scheduled balance; prepayments include sales, defaults and curtailments, not only refinancing.
3. Convert monthly SMM to annual CPR with 1 − (1 − SMM)^12.
4. Model prepayments empirically: S-curve of refinancing incentive plus turnover (seasonality, seasoning), defaults, curtailments, with burnout and credit/housing dependence.
5. Burnout makes cash flows path dependent, so use Monte Carlo; it handles path dependence but not early-exercise options well.
6. Use OAS for relative value only when it mean-reverts and is uncorrelated with rates; otherwise it is a blend of value and model error.
7. Pass-throughs are negatively convex at low rates; PO gains hugely when rates fall; IO loses (negative duration). Servicers behave like IO holders.
8. TBA hedge ratios fall with coupon; hedge curve exposure with more than one Treasury.

## Connects To
- **ch07**: OAS and risk-neutral pricing on trees (Monte Carlo analog here).
- **ch09-ch11**: term structure models that generate the simulated rate paths.
- **ch12**: repo financing (contrast with dollar roll).
- **ch13**: forward drop and forward pricing logic for TBAs and rolls.
- **ch18**: callable bonds and embedded options (efficient vs inefficient exercise).
- **ch06**: empirical hedge ratios by regression.
- **ch19**: default and recovery modeling for credit-sensitive securities.
- **`cfa-fixed-income` ch04 / ch09**: CFA treatment of MBS and prepayment measures (CPR, PSA) (ch04); OAS and negative convexity (ch09).
- **`hull-derivatives` ch33**: agency MBS and prepayment modelling in a forward-rate framework.
