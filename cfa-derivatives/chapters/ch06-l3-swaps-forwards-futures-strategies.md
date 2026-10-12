# Chapter 6: Swaps, Forwards, and Futures Strategies
> **Source**: CFA Program Curriculum 2023, Level III, Reading 9 · Derivatives & Risk Management | Barbara Valbuzzi, CFA

## Core Idea
Swaps, forwards and futures let a manager change a portfolio's exposure (duration, beta, currency, asset mix, volatility) **without trading the underlying securities**. That is faster and cheaper, and it avoids taxes, voting-right loss and market impact. The work is always the same: set a **target exposure**, measure the exposure of the existing portfolio and of one derivative unit, and solve for the notional or number of contracts that closes the gap. The same prices also tell you what the market expects (Fed moves, inflation, volatility).

## Learning Outcomes Covered
- Use interest rate swaps, FRAs, rate futures and bond futures to modify duration or lock in rates
- Use currency swaps (cross-currency basis swaps), forwards and futures to modify currency exposure
- Use equity swaps, total return swaps and index futures to modify beta or equitize cash
- Use volatility derivatives: VIX futures and options, variance swaps (valuation and settlement)
- Achieve targeted equity and interest rate exposures; manage tracking error
- Use derivatives for asset allocation, rebalancing and inferring market expectations (fed funds futures)

## Frameworks Introduced
- **Exposure-matching equation (universal hedge logic)**: `Exposure_portfolio + N × Exposure_per_derivative = Exposure_target`.
  - When to use: every sizing problem in this reading (swap notional, bond-futures BPVHR, equity futures N_f, cash equitization).
  - How: (1) measure the portfolio's exposure (money duration/BPV or dollar beta); (2) measure the exposure of one derivative unit; (3) set the target (0 for a full hedge); (4) solve for N; (5) sign tells you the side (+ buy/receive, − sell/pay); (6) round to whole contracts.
  - Failure mode: basis risk (the hedge instrument is an imperfect substitute), non-parallel curve moves, convexity, a change of CTD bond, and beta instability.
- **Duration management with an interest rate swap**: `N_S = [(MDUR_T − MDUR_P)/MDUR_S] × MV_P`.
  - A **pay-fixed** swap has **negative** duration (≈ floater duration − fixed-bond duration). Use it to shorten duration. A **receive-fixed** swap has positive duration. Use it to lengthen.
  - Convert a floating liability to fixed with pay-fixed/receive-floating (a synthetic fixed-rate bond). Convert fixed to floating with receive-fixed/pay-floating. Match tenor, notional and settlement dates to the underlying debt.
  - A pay-fixed swap gains value if rates rise and loses if rates fall. Unwinding before maturity crystallizes that MTM.
- **Bond-futures BPV hedge (BPVHR)**:
  - `BPV_P = MDUR_P × 0.0001 × MV_P`
  - `BPV_T = MDUR_T × 0.0001 × MV_P`
  - `BPV_CTD = MDUR_CTD × 0.0001 × MV_CTD`, with `MV_CTD = (CTD price/100) × contract size`
  - `BPV_F = BPV_CTD / CF`
  - `BPVHR = [(BPV_T − BPV_P)/BPV_CTD] × CF`. A full hedge sets BPV_T = 0, so `BPVHR = −(BPV_P/BPV_CTD) × CF`.
  - Why it works: the futures price tracks the CTD bond scaled by its conversion factor (ΔF ≈ ΔCTD/CF).
  - Failure mode: the CTD can switch, convexity, and non-parallel shifts. Use it only for small, parallel moves.
- **Equity beta adjustment**: `N_f = [(β_T − β_S)/β_f] × (S/F)`, with F = futures price × multiplier.
  - Full hedge: β_T = 0. **Cash equitization**: β_S = 0, so `N_f = (β_T/β_f) × (S/F)`.
  - For **asset reallocation**, treat the "sold" leg as β_T = 0 on the amount moved (sell futures) and the "bought" leg as β_S = 0 (starting from notional cash, buy futures). For bonds, use BPV_P = 0 for the amount added.
- **Synthetic asset allocation with swaps (total return/index swaps)**: receive an index return and pay MRR ± spread on the amount to add. Pay an index return and receive MRR on the amount to remove. The MRR legs net out across swaps.
  - Trade-offs: OTC counterparty risk (collateralized), illiquidity, no voting rights, tracking error vs. actual holdings. **Cash-flow risk**: you must pay the negative leg in cash while capital gains in the portfolio are unrealized.
- **Fed funds futures probability**: `P(hike) = (FFE_implied − FF_current)/(FF_after hike − FF_current)`, with `FFE_implied = 100 − futures price`. Use range **midpoints** for FF_current and FF_after hike.

## Key Concepts
- **Basis (spread) risk**: the hedge and the hedged position do not move one-for-one. It remains even with a "perfect" hedge ratio. Hedging corporates with rate swaps leaves **credit spread risk**.
- **FRA**: an OTC forward on a short rate. It settles the *discounted* difference between the contract rate and the realized rate on a notional. Use it to lock in a future borrowing/deposit rate.
- **Eurodollar-type rate futures**: price = 100 − annualized rate (IMM index). BPV = $1m × 0.01% × 90/360 = **$25** per contract. **Long** futures lock in a *deposit* rate; **short** futures lock in a *borrowing* rate. Use a strip of futures for short bonds (≤2–3 years).
- **Cheapest-to-deliver (CTD)**: the deliverable bond that maximizes (invoice amount − dirty cost) for the short. Long-duration, low-coupon bonds are CTD when yields are **above** the contract's notional yield (e.g., 6%). Short-duration, high-coupon bonds are CTD when yields are below it.
- **Conversion factor (CF)**: scales the futures price to each deliverable bond's price as if it had the notional coupon. CF < 1 when the coupon is below the notional coupon.
- **Bond basis** = cash price − (futures price × CF). A **negative** basis means **buy the basis** (buy the bond, short futures). A **positive** basis means **sell the basis** (sell the bond, buy futures). The basis converges to 0 at delivery.
- **Cross-currency basis swap**: exchange notional at inception at spot S₀, swap floating coupons in two currencies (the basis is quoted on the non-USD leg), and re-exchange the same notional at S₀ at maturity. It exists because covered interest parity does not hold exactly. Strong demand for USD funding makes the basis negative for the non-USD leg.
- **Equity swap types**: receive equity/pay fixed, receive equity/pay floating, receive equity/pay another equity. A **total return swap** includes dividends.
- **Cash equitization (cash overlay)**: buy index futures (or long call + short put, same strike and expiry) on idle cash to eliminate **cash drag** and tracking error.
- **VIX**: 30-day implied vol of S&P 500 options. It is not investable, so trade VIX futures (which converge to spot VIX at expiry) or VIX options (European, priced off VIX futures). The term structure is usually in **contango**, which means negative roll for longs. **Backwardation** signals near-term stress.
- **Variance swap**: exchange realized variance for a fixed variance strike. Zero cost at inception. It is long gamma and **convex in volatility**, so it is a tail hedge.
- **Vega notional**: the approximate P&L per 1 vol point. **Variance notional** = vega notional/(2 × strike).
- **Effective fed funds (FFE) rate**: the actual traded overnight rate that fed funds futures settle on (monthly average). It is **not** the target rate. **End-of-month dips** bias implied probabilities, so data providers smooth them.

## Formulas & Reference Tables
- Swap notional for target duration: `N_S = [(MDUR_T − MDUR_P)/MDUR_S] × MV_P`
- Principal invoice amount = `(Futures settlement price/100) × CF × Contract size` (+ accrued interest = total invoice)
- Delivery gain/loss for the short = invoice amount − cost of the bond (dirty). CTD = max of that (least negative).
- `BPVHR = [(BPV_T − BPV_P)/BPV_CTD] × CF`
- Rate-futures BPV = `Face × (Days/360) × 0.01%`
- Equity futures: `N_f = [(β_T − β_S)/β_f] × (S/F)`, with F = quoted price × multiplier
- Covered interest parity (CIP) forward: `F_f/d = S_f/d × (1 + i_f × ACT/360)/(1 + i_d × ACT/360)`
- Variance swap settlement: `Settlement_T = N_var × (σ²_realized − K²) = N_vega × (σ² − K²)/(2K)` (vol points squared; payoff > 0 means the **seller pays the buyer**)
- Realized variance: `σ² = 252 × Σ_{i=1}^{N−1} R_i² / (N − 1)`, with R_i = ln(P_{i+1}/P_i)
- Variance notional: `N_var = N_vega/(2 × K)`
- MTM of a variance swap at t: `VarSwap_t = N_var × PV_t(T) × [(t/T) × RealizedVol(0,t)² + ((T−t)/T) × ImpliedVol(t,T)² − K²]`
- Fed funds futures: price = 100 − expected average FFE. `P(move) = (FFE_implied − FF_mid,now)/(FF_mid,after − FF_mid,now)`

| Common use | Typical derivative |
|---|---|
| Modify risk/return (hedge or directional) | IRS, currency and equity swaps and futures, bond futures, variance swaps |
| Create desired payoffs | Forwards, futures, total return swaps |
| Asset allocation and rebalancing | Equity index futures, government bond futures, index swaps |
| Infer expectations (rates, inflation, vol) | Fed funds futures, CPI (inflation) swaps, VIX futures |

| Hedge instrument | Best for | Watch out for |
|---|---|---|
| Interest rate swap | Liability conversion, long-dated duration change, customization | OTC credit/collateral, MTM on unwind, spread risk |
| Rate futures / FRA | Locking a rate on a future short loan or deposit; bonds ≤2–3 yrs | Few maturities; far contracts illiquid |
| Bond futures (UST, Bund/Bobl/Schatz) | Duration of bond portfolios (most liquid) | CTD switch, CF, convexity, non-parallel moves |
| Equity index futures | Beta change, equitization, tactical allocation | Beta instability, roll, cash settlement only |
| Equity/total return swap | Market access, avoiding stamp duty/custody, keeping shares (tax basis) | Illiquid, collateral, no voting rights, cash-flow drain |
| VIX futures and ETPs | Directional implied-vol view, tail hedge | Contango roll cost; futures lag spikes in spot VIX |
| Variance swap | Realized-vs-implied view, convex tail hedge | Short side has unlimited convex losses |

| Bond futures | Underlying German bonds |
|---|---|
| Euro-Schatz (FGBS) | 1.75–2.25 yrs |
| Euro-Bobl (FGBM) | 4.5–5.5 yrs |
| Euro-Bund (FGBL) | 8.5–10.5 yrs |

**⚠ Correction**: the reading gives Schatz 21–27 months ✓ but Bund "10–30 years". Eurex's Bund deliverable basket is 8.5–10.5 years (10–30 years is the Buxl/US bond range). This does not affect any calculation.

## Mental Models
- **"Duration and beta are dollars, not percentages."** Always convert to money exposure (BPV, β × S) before sizing. The number of contracts is the money gap divided by the money exposure per contract.
- **Think of a pay-fixed swap as "short a fixed bond, long a floater."** That is why its duration is negative and why it profits when rates rise.
- **The futures price is the CTD bond in disguise.** Hedge the CTD's BPV, then scale by CF. Forgetting CF or using the CTD *price* instead of its BPV are the two classic sizing errors.
- **Variance is volatility with convexity built in.** A long variance swap earns more than the vega approximation when vol spikes and loses less when vol falls. Sellers demand a premium for this, so the strike sits above ATM implied vol (rule of thumb: the implied vol of the 90%-moneyness put).
- **Market-implied ≠ forecast.** Fed funds probabilities are current *pricing* (including risk premia and month-end noise). They have weak predictive power at longer horizons.

## Worked Example
**1. Cut bond duration with futures vs. a swap.** Portfolio MV €80m, MDUR 7.2, target 4.0. CTD: price 104.50, MDUR 8.10, CF 0.7250, contract €100,000.
- BPV_P = 7.2 × 0.0001 × 80m = €57,600. BPV_T = 4.0 × 0.0001 × 80m = €32,000.
- BPV_CTD = 8.10 × 0.0001 × (104.50/100 × 100,000) = €84.645.
- BPVHR = (32,000 − 57,600)/84.645 × 0.7250 = **−219.3**, so **sell 219** Bund futures.
- Swap alternative: a pay-fixed 5-year swap with MDUR_S = −4.5 gives N_S = (4.0 − 7.2)/(−4.5) × 80m = **€56.9m** notional.

**2. Variance swap MTM and settlement.** Buy $200,000 vega notional, 1-year, strike K = 18. After 3 months, realized vol = 25, fair 9-month strike = 22, r = 3%.
- N_var = 200,000/(2 × 18) = 5,555.56. PV = 1/(1 + 0.03 × 0.75) = 0.97800.
- Blended variance = 0.25 × 625 + 0.75 × 484 = 519.25, versus K² = 324.
- Value = 5,555.56 × 0.97800 × 195.25 = **+$1,060,853** to the buyer.
- At expiry with full-year realized vol 20: settlement = 5,555.56 × (400 − 324) = **+$422,222**. The vega approximation gives only 200,000 × 2 = $400,000.
- With realized vol 16: −$377,778 (approximation: −$400,000). This asymmetry is the convexity.

**3. Fed funds probability.** Range 3.00–3.25% (midpoint 3.125%). The futures price is 96.80, so FFE = 3.20%. P(+25bp) = (3.20 − 3.125)/(3.375 − 3.125) = **30%**.

## Anti-patterns
- **Sizing a swap to face value instead of duration**: the notional must be scaled by MDUR_P/MDUR_S.
- **Using the quoted index level as F**: multiply by the multiplier (a classic error gives 1,455 contracts instead of 6).
- **Equitizing the whole fund instead of the cash** (121 contracts instead of 6).
- **Ignoring the conversion factor or dividing by the CTD price**: the answer is off by the factor CF or by an order of magnitude.
- **Using a receive-fixed swap to hedge rising rates**: it adds duration.
- **Long VIX ETPs as a permanent hedge**: contango roll bleeds value daily, and the ETP lags spot VIX.
- **Funding swap outflows with unrealized gains**: a TRS overlay can force selling the very assets you wanted to keep.

## Exam Focus & Traps
- **Sign conventions**: N < 0 means sell or pay. Pay-fixed MDUR is negative. For a variance swap, a positive settlement means the **seller pays the buyer**. **⚠ Correction**: the reading says the buyer "will pay the difference between the variance strike and realized variance". Read it as the buyer *receives* (realized − strike), which may be negative.
- **Variance MTM**: weight realized² by t/T and implied² by (T−t)/T, subtract K², and discount **only the remaining period** (T − t). Classic wrong answers omit PV or swap the realized and implied terms.
- **Rate futures**: a short hedger (borrower) sells futures. Effective rate = loan rate − futures gain in bp (e.g., sold at 98.05, closed at 97.30: gain 75bp, loan 2.70% → 1.95%). A depositor buys futures.
- **Cross-currency basis swap**: principals are exchanged **at inception and maturity at the same S₀**. With a positive basis for "lending" USD (strong USD demand), the USD lender's **USD** receipts rise.
- **CTD choice**: compare invoice (F/100 × CF × size) with dirty cost. Pick the smallest loss.
- **Asset allocation with futures**: the equity sell leg uses the stock beta (e.g., 1.1), so the short hedges more than the notional amount. The buy leg starts from β_S = 0. Bond legs use BPV_P = 0.
- **⚠ Correction (Grant rebalancing example)**: the reading moves 0.034 × €106m = €3,604,000. The exact amount is €46m − €42.4m = **€3.6m**, which gives 123.4 → **sell 123** EURO STOXX 50 futures (the reading says 124). The Bund leg stays at **25**.
- Fed funds futures settle on the **average effective** rate for the month, not the target range. Month-end dips push the futures price up and implied probabilities down (example: 90% → 30%).
- Equity swaps: OTC, collateralized, relatively illiquid, **no voting rights**. A physically settled single-stock swap delivers shares against notional, while a cash-settled one pays the difference.

## Key Takeaways
1. Every overlay is an exposure-gap problem: (target − current money exposure)/(exposure per unit).
2. Use pay-fixed swaps or short bond futures to cut duration, and receive-fixed swaps or long futures to add it. BPVHR needs the CTD's BPV **and** its CF.
3. Equity futures change beta and equitize cash in minutes. Remember the multiplier and the stock beta.
4. Swaps implement multi-asset reallocations synthetically, but they carry OTC, liquidity and cash-flow costs.
5. Cross-currency basis swaps let you borrow where it is cheap and swap into the currency you need. The basis is a real cost or benefit.
6. Variance swaps give convex long-vol exposure, and VIX futures give pure implied-vol exposure. Budget for contango roll.
7. Derivative prices reveal market expectations (Fed moves, inflation, vol), but these are current pricing, not forecasts.

## Connects To
- **ch03**: pricing of forwards, futures and swaps (CIP, swap rate, MTM) behind these hedges.
- **ch05**: option strategies, a complement for asymmetric hedges (collars, protective puts, straddles, VIX calls).
- **ch07**: currency forwards and futures in portfolio currency management (hedge ratios, rolls, overlays).
- **`cfa-fixed-income` ch13–ch14**: duration targeting, LDI and yield-curve strategies that use these same instruments.
- **`hull-derivatives` ch03, ch07**: hedging with futures (hedge ratios, basis risk) and swaps (valuation, comparative advantage).
- **`tuckman-fixed-income` ch14, ch16**: note and bond futures (CTD, CF, delivery options) and swaps in depth.
- **`passarelli-option-greeks` ch03**: volatility concepts behind the VIX and variance swaps.
- **`cfa-asset-allocation-cme` ch07**: rebalancing policy that these overlays implement.
