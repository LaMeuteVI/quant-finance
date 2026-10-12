# Chapter 11: Credit Default Swaps
> **Source**: CFA Program Curriculum 2022, Level II, Reading 32 · Fixed Income | Brian Rose and Don M. Chance, PhD, CFA

## Core Idea
A credit default swap (CDS) separates credit risk from interest-rate risk:
- The **protection buyer** (short credit) pays a standardized coupon (1% IG, 5% HY) plus or minus an upfront payment.
- The **protection seller** (long credit) pays (1 − recovery) × notional after an ISDA-declared credit event.

Pricing reuses the CVA machinery. The **protection leg** is the PV of hazard-weighted expected losses. The **premium leg** is the PV of survival-contingent coupons. Their difference is the upfront payment. Between inception and maturity, the CDS gains or loses roughly Δspread × spread duration × notional. That P&L is what makes CDS useful for hedging, for directional and curve views, and for relative-value (basis, long/short, equity-vs-credit) trades.

## Learning Outcomes Covered
- Describe CDS (single-name, index, tranche) and the parameters that define a CDS product.
- Describe credit events, succession events and settlement protocols (physical vs cash settlement, auction).
- Explain the principles and factors behind the market pricing of CDS (hazard rate, LGD, premium vs protection leg, upfront).
- Describe the use of CDS to manage credit exposure and to express views on the level and shape of the credit curve.
- Describe the use of CDS to exploit valuation disparities among bonds, loans, equities and equity-linked instruments (basis trades, LBO trades, index arbitrage).

## Frameworks Introduced
- **Protection leg vs premium leg (upfront determination)**: `Upfront = PV(protection leg) − PV(premium leg)`.
  - When to use: to price a new CDS, to value an existing one, or to explain who pays at inception.
  - How:
    1. **Protection leg**: LGD × notional × PODₜ (from hazard rates, conditional on survival) × risk-free DFₜ, summed over t.
    2. **Premium leg**: fixed coupon × notional × POSₜ × DFₜ, summed over t. Coupons are paid only while the entity survives.
    3. If upfront > 0, the buyer pays the seller (spread > coupon). If upfront < 0, the seller pays the buyer (spread < coupon).
    4. Price per 100 = 100 − upfront %.
  - Why it works: at fair value, a hedged position (bond + protection) should earn the risk-free rate. The CDS "price" is whatever equalizes the two legs.
  - Failure mode: the linear rule `upfront ≈ (spread − coupon) × duration` treats duration as fixed. The CDS duration is a *risky annuity* (effective or spread duration) that shrinks as spreads widen and as time passes.
- **Settlement protocol**:
  - After an ISDA Determinations Committee (DC) declares a credit event, either party may settle, typically about 30 days later.
  - **Physical**: deliver a qualifying obligation and receive par × notional.
  - **Cash**: receive (1 − RR) × notional, with RR set by an **auction** on the **cheapest-to-deliver (CTD)** obligation. The auction result binds even if the realized recovery later differs.
  - Choice rule for a hedger holding bond X:
    - X price > CTD price → prefer **cash** (the CDS payout plus the sale of X exceeds par).
    - X is the CTD → indifferent.
- **Directional credit-exposure management**:
  - Buy protection to shed credit (a lender avoiding a sale of an illiquid loan or bond, a temporary hedge, or a **naked** short).
  - Sell protection to add credit without funding or duration exposure (it needs less capital than buying the bond and is often more liquid).
- **Long/short credit trade**: sell protection on the name or index expected to improve, and buy protection on the one expected to deteriorate. Variants:
  - Single names (peer vs peer, ESG leader vs laggard).
  - HY index vs IG index as a macro recession hedge (buy HY protection, sell IG protection).
  - Regional indexes (e.g., buy iTraxx protection, sell Asia protection if Asia is expected to outperform).
- **Curve trade**: buy protection at one maturity and sell it at another on the same reference entity or index.
  - **Steepener** (long-term risk rises relative to short): buy long-dated protection, sell short-dated. It is bullish on the near term.
  - **Flattener** (near-term stress): buy short-dated protection, sell long-dated. It is bearish on the near term.
  - Parallel-shift views: long tenors move more (higher duration), so size the legs by duration if you are expressing the relative move.
- **Basis trade** (bond spread vs CDS spread):
  - `Bond credit spread = Bond yield − market reference rate` (reference rate = risk-free + funding spread). `CDS–bond basis = CDS spread − bond spread`.
  - **Negative basis** (bond spread > CDS spread): buy the bond, buy protection, and hedge rates. You earn the differential if the spreads converge.
  - **Positive basis** (CDS spread > bond spread): the reverse (short the bond or sell it from inventory, sell protection).
  - Causes: differences of opinion or model, liquidity, repo/funding conditions, supply and demand, and embedded options or off-par prices that complicate the decomposition.
- **Equity-vs-credit and capital-structure trades**:
  - Expected LBO or leveraging event → **long the stock** (the buyout premium) **+ buy protection** (spread widens on the extra debt). Both legs win.
  - Acquirer issuing debt → buy protection on the acquirer. Target shares → long.
  - Index arbitrage: trade the index against the sum of its constituents when they diverge. This is viable only for the largest players after costs.

## Key Concepts
- **Credit derivative**: a derivative whose underlying is a borrower's credit quality. Four types: total return swaps, credit spread options, credit-linked notes and CDS. CDS are by far the most liquid.
- **Reference entity / reference obligation**: the borrower / the designated debt, usually senior unsecured. Coverage extends to all obligations **pari passu or senior** to the reference obligation.
- **Cheapest-to-deliver obligation**: the lowest-priced qualifying obligation of equal seniority. It sets the payoff. Subordinated debt cannot be delivered against a senior CDS.
- **Single-name / index / tranche CDS**:
  - Single-name: one entity.
  - Index: an equally weighted portfolio of single names.
  - Tranche: index losses covered only between attachment and detachment points.
- **Notional**: the amount of protection. Total CDS notional can exceed the entity's outstanding debt because buyers need not hold the debt.
- **CDS spread**: the annual premium that fairly compensates the seller. Conceptually equal to the bond credit spread.
- **Standard coupon and upfront premium**: fixed 1% (IG) or 5% (HY) coupons. The PV of (spread − coupon) is settled upfront.
- **Credit event**: bankruptcy, failure to pay (after a grace period, on any obligation), or restructuring (involuntary or coercive). Also moratorium or repudiation for sovereign and municipal debt.
  - Restructuring is **not** a credit event under the standard North American contract: US issuers restructure through bankruptcy.
  - Restructuring **is** a credit event elsewhere (e.g., the Greek restructuring).
- **Determinations Committee (DC)**: the regional ISDA panel of 15 (10 dealers, 5 buy-side). A **supermajority of 12** is needed to declare a credit event. The DC also rules on succession events.
- **Succession event**: a change in corporate structure (merger, spinoff, divestiture) that makes the obligor unclear. The CDS may be split across successors.
- **Hazard rate**: the probability of default in a period given survival to its start.
- **Protection leg / premium leg**: the seller's contingent payment / the buyer's survival-contingent coupon stream.
- **Credit curve**: CDS or credit spreads across maturities for one borrower. In practice the credit curve is set by the liquid CDS market.
- **On-the-run / off-the-run / roll**: Markit creates a new index series every 6 months. Maturities fall on the 20th of Mar/Jun/Sep/Dec, and the **March and September** dates are the most liquid index rolls. Moving to the new series is the roll.
- **Naked CDS**: protection bought without owning the reference debt. Naked sovereign CDS is banned in Europe.
- **Monetizing**: realizing CDS P&L before maturity by entering an offsetting contract, ideally with the same counterparty or via central clearing.

## Formulas & Reference Tables
- Payout on a credit event: `Payout = LGD × Notional = (1 − RR) × Notional`.
- One-period approximation: `CDS spread ≈ (1 − RR) × POD` (e.g., 2% × (1 − 60%) = 80bp).
- Survival with period hazards hᵢ: `POS_T = Πᵢ (1 − hᵢ)`. `Cumulative POD_T = 1 − POS_T`. Constant hazard: `POS_T = (1 − h)ᵀ`.
  - 2% for 10 years → POS = 0.98¹⁰ = 0.817, cumulative POD = **18.3%**.
  - 2% then 4% → POS = 0.98 × 0.96 = 94.08%, POD = 5.92%.
- Legs (discrete, annual):
  - `PV_prot = N × (1 − RR) × Σₜ h × POSₜ₋₁ × DFₜ`.
  - `PV_prem = C × N × Σₜ POSₜ × DFₜ = C × N × RPV01`.
- Upfront:
  - `Upfront = PV_prot − PV_prem = (s_par − C) × RPV01 × N` (exact when s_par is the par spread on the same curve).
  - Approximation: `Upfront % ≈ (Credit spread − Fixed coupon) × Duration`.
  - `PV(credit spread) = Upfront premium + PV(fixed coupon)`.
  - `Price per 100 = 100 − Upfront %`.
- Mark-to-market:
  - `Profit to protection buyer ≈ Δspread × Duration × Notional`.
  - `%ΔCDS price ≈ Δspread × Duration` (effective duration, because coupons are contingent on survival).
- Index CDS settlement: each name is 1/n of the notional (CDX IG n = 125). After a default, the index continues with notional × (1 − 1/n).
- Bond vs CDS basis: `Bond spread = Yield − MRR`. `Basis = CDS spread − Bond spread`. Negative basis → buy the bond + buy protection.

**Directional conventions (a classic trap)**

| Position | Credit exposure | Gains when |
|---|---|---|
| Buy single-name protection | Short credit | Spread widens / default |
| Sell single-name protection | Long credit | Spread tightens / no default |
| **Buy** CDX/iTraxx index (CFA usage) | **Long** credit (= sell protection) | Spreads tighten |
| **Sell** CDX/iTraxx index | Short credit (= buy protection) | Spreads widen |

**Main indexes**

| Index | Region | Quality | Names | Quoted in |
|---|---|---|---|---|
| CDX IG | North America | IG | 125 | Spread |
| CDX HY | North America | HY | 100 | Price |
| iTraxx Main (Europe) | Europe/Asia/Australia | IG | 125 | Spread |
| iTraxx Crossover | Europe | HY | up to 75 | Price |

**Market facts (2019 data in the reading):**
- Gross CDS notional ≈ **$7.6tn** (market value $199bn), versus $57.9tn in 2007.
- Just over 50% of CDS are centrally cleared (10% in 2010).
- More than 90% of activity is in five indexes: iTraxx Europe, iTraxx Crossover, iTraxx Senior Financials, CDX IG, CDX HY.

**Credit curve shapes**

| Shape | Implied hazard pattern | Typical cause |
|---|---|---|
| Flat (nearly) | Constant hazard. Not perfectly flat because of discounting. | Stable credit |
| Upward | Higher default risk in later years | Normal IG; refinancing wall later |
| Downward (inverted) | Higher default risk near term; survivors improve | Severe near-term stress or liquidity crunch |

## Mental Models
- **A CDS is a put on credit quality**: it pays par − recovery on a credit event and is marked to market before default, as with a put. It is called a swap, but its payoff is contingent like an option's.
- **Seller ≈ long the bond, buyer ≈ short the bond, both unfunded and without rate duration**: selling protection is like a floating-rate bond financed at the reference rate, which is why CDS isolate credit from rates.
- **"Duration" in a CDS is the risky annuity**: the PV of 1bp paid while the entity survives. It falls with time and with wider spreads, so linear P&L estimates overstate gains for large widenings.
- **Hedge with the CTD in mind**: a hedger is paid on the CTD recovery, not on the bond held. Holding a higher-priced bond → choose cash settlement. Holding a lower-priced bond than the auction CTD → basis risk against you.
- **Cumulative default compounds quickly**: a 2% annual hazard is an 18% ten-year default probability. Always convert hazard to cumulative probability before judging a long-dated credit.

## Worked Example
**Pricing a 5-year CDS from its two legs, and checking the rules of thumb** (constructed and verified).

Inputs:
- Constant annual hazard h = 2%, RR = 40%, risk-free flat at 3% (annual compounding), standard IG coupon C = 1%, notional 100.
- Annual payments. Default and payments occur only at year-end, and no premium accrues on default.

| t | PODₜ = h·POSₜ₋₁ | POSₜ | DFₜ | PV protection (0.6·POD·DF·100) | POS·DF |
|---|---|---|---|---|---|
| 1 | 2.0000% | 98.0000% | 0.970874 | 1.1650 | 0.9515 |
| 2 | 1.9600% | 96.0400% | 0.942596 | 1.1085 | 0.9053 |
| 3 | 1.9208% | 94.1192% | 0.915142 | 1.0547 | 0.8613 |
| 4 | 1.8824% | 92.2368% | 0.888487 | 1.0035 | 0.8195 |
| 5 | 1.8447% | 90.3921% | 0.862609 | 0.9548 | 0.7797 |
| Σ | 9.6079% | | | **5.2865** | **RPV01 = 4.3173** |

1. **Par spread** = PV_prot/(N × RPV01) = 5.2865/431.73 = **122.45bp**.
   - Rule of thumb h(1 − RR) = 120bp. The small gap comes from annual discreteness: here, exactly, s = (1 − RR) × h/(1 − h).
2. **Upfront** = 5.2865 − 1% × 100 × 4.3173 = **0.9692 per 100**, paid by the buyer. The spread exceeds the coupon, so the CDS price is 100 − 0.97 = **99.03**.
   - Check: (122.45 − 100)bp × 4.3173 = 0.9692. The "duration" in the industry formula is the risky annuity.
3. **Mark-to-market**: the spread widens by 100bp to 222.45bp (h → 3.575%). The buyer gains exactly **4.08** per 100, versus 1% × 4.32 × 100 = 4.32 by the linear rule. The linear rule overstates because RPV01 falls to 4.12.

Curriculum-style checks (all recomputed):
- HY name, spread 600bp, coupon 500bp, duration 8 → buyer pays ≈ 8% upfront.
- Kand: spread 700bp, coupon 5%, duration 7 → 14% upfront.
- IG seller pays 2% upfront on a 1% coupon with duration 4 → spread ≈ 100 − 2%/4 = **50bp**, price = 100 − (−2) = **102**.
- Buy $10m of protection with duration 4, spread 500 → 800bp: gain ≈ 0.03 × 4 × 10m = **$1.2m** (+12%).
- Sell £6m with duration 3.9, spread 150 → 100bp: gain ≈ 0.005 × 3.9 × 6m = **£117,000**.
- Hazards 0.22%, 0.35%, 0.50% → 3-year POD = 1 − 0.9978 × 0.9965 × 0.9950 = **1.07%**.

**Settlement preference.** A senior CTD trades at 30 (so RR = 30%). Investor Y holds €10m of another senior bond priced at 40, plus €10m of protection.
- Cash settlement: €7m CDS payout + €4m bond sale = **€11m**.
- Physical settlement: deliver the bonds for €10m.
- → Y prefers cash. An investor holding the CTD itself is indifferent (€7m + €3m = €10m).

## Anti-patterns
- **Assuming CDS eliminates credit risk**: basis risk remains (the contract's credit-event definition differs from the bond's actual loss, and the payout is on the CTD auction), and so does **counterparty risk** on the seller (2008). Central clearing mitigates but does not remove the latter.
- **Mixing single-name and index language**: "buying" the index is *long* credit (CFA convention). Think in "buy/sell protection" to avoid sign errors.
- **Assuming restructuring always triggers**: it does not under North American standard contracts. It must be involuntary or coercive elsewhere.
- **Using the raw spread − coupon difference as the upfront**: multiply by duration (700 − 500 = 200bp is not 2% upfront; it is ≈ 14% with duration 7).
- **Computing the bond spread against the CDS spread**: the bond spread is yield − reference rate. The Tollunt basis: (7% − 2.5%) − 4.25% = 25bp, not 7% − 4.25%.
- **Believing a convergence (basis/index) trade is riskless**: it depends on the model isolating credit correctly, on repo funding, on embedded options, on off-par prices and on transaction costs.
- **Reading an inverted CDS curve as "long bonds riskier"**: it signals near-term default risk. Survivors' hazard falls.

## Exam Focus & Traps
- **Seniority filter first, then lowest price**: the CTD is the cheapest *pari passu or senior* obligation. A subordinated bond at 20 is not deliverable against a senior CDS.
- **Failure to pay on *any* obligation (including subordinated) after the grace period is a credit event**, with or without bankruptcy.
- **The DC requires 12 of 15 votes.** Settlement is ≈ 30 days after the declaration. Physical settlement is less common than cash settlement.
- **In CDS models, RR usually applies only to principal** (payout = (1 − RR) × notional). R31's bond CVA models applied RR to exposure, coupon included. Do not mix the two conventions.
- **Upfront direction**:
  - Spread > coupon → the buyer pays. A 5% HY coupon on a 700bp name → buyer pays about 14%.
  - Spread < coupon → the seller pays. An IG name at 50bp on a 1% coupon → the seller pays and the price is > 100.
- **Unwinding**:
  - The original buyer sells protection. If spreads rose → gain, because the buyer receives a higher upfront than was paid.
  - The original seller buys protection. If spreads fell → gain, because the seller pays less than was received.
- **Holding to maturity with no default**: the spread converges to zero, as a bond pulls to par. The seller keeps all premiums. The buyer's "loss" is an insurance cost.
- **Index hedge arithmetic**:
  - Selling $500m of CDX IG protection = $4m long per name.
  - Buying $3m single-name protection on name A hedges 75% of A, leaving $1m net long.
  - After A defaults, the index notional falls to $496m.
- **Credit correlation**: higher default correlation makes index or basket protection **more expensive**. It is a key index-CDS pricing factor.
- **Index vs tranche**: to hedge many exposures *fully*, use an index CDS. A tranche hedges only a slice of losses.
- **Macro views**:
  - Europe weakens → buy iTraxx Crossover protection, sell iTraxx Main protection.
  - US strengthens relative to Canada → sell US protection, buy Canada protection.
  - Improving sector (EV makers) → sell protection on it, buy protection on the laggard.
- **Curve view**: short-term improvement or a steepening view → buy long-dated protection, sell short-dated (e.g., buy 20-year CDX protection, sell 2-year).
- **M&A trade**: the target's stock rises (go long the target), and the acquirer's leverage rises (buy protection on the acquirer).
- ⚠ **Correction (source solution to Practice Problem 14)**: the text says the Fund "sells protection on Delta" to profit from spread widening. A spread-widening view requires **buying** protection on Delta. The answer choice (long Zega + buy Delta protection) is right.
- ⚠ **Correction (source solution to Practice Problem 1)**: Bond 1 is described as "senior secured". It is a *senior unsecured* bond, as in the vignette.

## Key Takeaways
1. A CDS transfers credit risk. The buyer is short credit and the seller long, while the index "buyer" is long credit. Always reason in buy/sell protection.
2. Payout = (1 − RR) × notional, with RR set by an ISDA auction on the cheapest-to-deliver pari passu obligation. Holders of higher-priced bonds prefer cash settlement.
3. Credit events: bankruptcy, failure to pay and (outside North America) involuntary or coercive restructuring. The 15-member DC decides by a 12-vote supermajority, and also rules on succession events.
4. Price = protection leg − premium leg. With standardized 1%/5% coupons, the difference settles upfront: ≈ (spread − coupon) × duration, where "duration" is the risky annuity.
5. Mark-to-market P&L ≈ Δspread × duration × notional. Monetize by entering an offsetting CDS. At maturity with no default, the spread decays to zero.
6. Hazard rates compound: cumulative POD = 1 − Π(1 − hₜ). Flat hazard gives a nearly flat curve, rising hazard an upward curve, near-term stress an inverted curve.
7. Use CDS for hedging, naked views, long/short (names, sectors, regions, ESG), curve trades, basis trades (negative basis → long bond + buy protection) and equity-vs-credit trades around LBOs and M&A.

## Connects To
- **ch10**: the same CVA framework (exposure, LGD, hazard-based POD, risk-free discounting), term structure of credit spreads, and the curve trade suggested for an inverted credit curve.
- **ch06**: the Level I credit-analysis basics: seniority ranking, recovery rates by priority, and ratings.
- **ch15**: Level III credit strategies: CDS in portfolio construction, spread duration, index vs single-name hedging, and credit curve positioning.
- **`cfa-derivatives` ch06**: swap, forward and futures overlays at Level III, including credit derivative strategies.
- **`tuckman-fixed-income` ch19**: corporate bonds and CDS: hazard-rate curves, the CDS–bond basis, and upfront plus running-coupon conventions (with the accrued-premium detail).
- **`hull-derivatives` ch24–25**: credit risk (risk-neutral vs real-world PD) and credit derivatives (CDS valuation, CDS indexes, fixed coupons, basket and tranche products, credit correlation).
- **`cfa-portfolio-management` ch13**: measuring and managing market and credit risk exposures.
