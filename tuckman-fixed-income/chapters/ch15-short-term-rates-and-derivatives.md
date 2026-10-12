# Chapter 15: Short-Term Rates and Their Derivatives
> **Source**: Tuckman & Serrat, *Fixed Income Securities* (3rd ed.), Chapter 15, "Short-Term Rates and Their Derivatives" | Bruce Tuckman, Angel Serrat

## Core Idea
Most short-term rates are spreads over two benchmarks, LIBOR and the fed funds rate, and each has a matched hedging pair: FRAs and Eurodollar (ED) futures for LIBOR, overnight index swaps (OIS) and fed funds (FF) futures for fed funds. The chapter turns these into working tools: the tailed ED hedge, the TED spread and bucket 01s to hedge bonds against ED strips, FF-futures hedge ratios by month length, market-implied FOMC probabilities, and the LIBOR-OIS spread as a stress gauge. (Written in the LIBOR era, 2010; the mechanics carry over to SOFR futures and SOFR OIS.)

## Frameworks Introduced
- **FRA as a present-valued forward swap**: an FRA pays on the settlement date the PV, at the realised LIBOR L, of `N × (τ)(K − L)`. Locking K on a forward loan replicates the forward rate, so FRA rate = forward rate.
  - When to use: customised forward-rate hedges (non-IMM dates).
  - How: the fixed receiver has `N(1+τL) + N τ(K−L)/(1+τL)` at start, which rolled at L gives `N(1+τK)` at end (an exact lock).
- **Eurodollar futures hedge with tail**: ED futures pay $25 per bp on a $1mm 90-day deposit; daily settlement means the hedge must be reduced by the present-value factor to the delivery date (the tail).
  - When to use: locking a 90-day lend or borrow rate at an IMM date.
  - How: contracts = `unadjusted / (1 + r × d/360)` with d = days from trade to the contract's delivery; re-tail as time passes (the tailed hedge grows back to the full amount).
- **TED spread**: the single spread s such that discounting a security's cash flows at (stub rate and ED futures rates) − s reproduces its full price.
  - When to use: rich/cheap of short-term Treasuries (up to about 2 to 3 years) against LIBOR; sign convention gives positive spreads for Treasuries.
  - How: build periods (stub from settlement to first ED deposit start, then each ED period to the next contract start), compound the period rates less s, solve for s.
  - Failure modes: uses futures not forwards (convexity, small at the short end); the ED rate is applied over partial periods; contract start dates do not align with the deposit dates.
- **Bucket 01 hedge with ED futures**: (1) shift one futures (or stub) rate down 1bp holding s fixed; (2) revalue the bond; (3) divide the change by $25 to get contracts; (4) repeat for every bucket. This automatically includes the tail.
- **Fed funds futures hedge sizing**: contracts per $5mm = `days of exposure / (days in month)`-scaled; one contract per $5mm inside a 30-day month; `31/30`, `29/30`, `28/30` for other months; for part of a month, a hedge that must be decayed over time.
- **Implied FOMC probability extraction**: from month-average futures rates, solve for the probability p of a 25bp move at each meeting, chaining forward expected rates.
- **OIS floating leg = compounded fed funds**: notional accumulates daily at effective FF (actual/360, weekends at Friday's rate); the swap replicates rolling overnight lending.
- **LIBOR-OIS spread as stress index**: price of locking three-month funding rather than rolling overnight; wide = credit/liquidity fear.

## Key Concepts
- **LIBOR fixing**: BBA survey of 16 banks per currency and term, drop the top 4 and bottom 4, average the middle 8; quoted actual/360, T+2 settlement.
- **Forward rate agreement (FRA)**: OTC contract exchanging fixed for LIBOR on a future 3-month period, settled at the period start with the PV of the difference.
- **Eurodollar futures**: quarterly cash-settled futures on 3-month USD LIBOR; price = `100 − 100 × rate`; $25 per bp; expire two London business days before the third Wednesday (IMM date).
- **Contract colours**: fronts (first four), reds, greens, blues, golds, and so on for later years.
- **Cash settlement vs physical settlement**: cash settled contracts (ED, FF) pay final settlement only; note/bond futures deliver bonds.
- **Euribor and TIBOR futures**: analogous contracts on EUR panel (over 50 banks, trimmed 15% each tail) and yen panel (18 banks) rates; TIBOR-LIBOR spread positive because the TIBOR panel was seen as riskier.
- **Stub**: period from bond settlement to the start of the first ED deposit; hedged with FF futures or short-dated instruments.
- **Basis risk**: mismatch between the hedged exposure's rate and the hedge instrument's rate (borrowing spread over FF).
- **Fed funds effective rate**: volume-weighted average rate of overnight interbank borrowing, published daily; targeted by the FOMC, typically within a couple of bp of target before Dec 2008.
- **Fed funds futures**: contract on the monthly average of daily effective rate; $5mm, 30-day, $41.67 per bp; settles at `100 − 100 × average` (average rounded to 0.1bp).
- **Overnight index swap (OIS)**: fixed rate versus compounded fed funds effective (EONIA in EUR, TONAR in JPY, SONIA in GBP); annual payments beyond one year; liquid to 2 to 3 years.
- **LIBOR-OIS spread**: 3M LIBOR minus 3M OIS; about 8bp USD and 6bp EUR before July 2007; peak 365bp on Oct 10, 2008.
- **Turn**: year-end funding effect on fed funds; largely a non-event after 2000.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Deposit proceeds | `1 + L × d/360` (actual/360) |
| FRA settlement (at start, payer of fixed K) | `N × (d/360)(K − L) / (1 + L × d/360)` |
| ED contract price | `100 − 100 × L` ; bp value = `$1,000,000 × 0.0001 × 90/360 = $25` |
| ED final settlement | `100 − 100 × 3M LIBOR at expiry` |
| ED tailed hedge | `N_ED = N_unadj / (1 + r × d/360)` |
| TED spread | solve `P_full = Σ CF_j × DF_j(s)`, with `DF` compounding `(r_k − s) × d_k/360` over each period |
| ED contracts for bucket k | `Bucket01_k / $25` |
| Rough ED hedge size | `Full price ($) / $1mm` per period (adjusted for period length, tail) |
| FF contract | `$5mm × 0.0001 × 30/360 = $41.67` per bp; settle `100 − 100 × avg effective` |
| FF hedge over a full month of D days | `D/30` contracts per $5mm |
| FF hedge of exposure running to month-end (30-day month) | `1` contract per $5mm at any date: exposure and contract sensitivity both shrink as days pass |
| FF hedge for the first j days of a 30-day month | `j/30` contracts per $5mm before the month starts; `(j−m)/(30−m)` on day m (m days elapsed) |
| FOMC probability | `average = (d_pre × r_0 + d_post × [(1−p) r_0 + p (r_0+Δ)]) / D`, so `p = (F − r_0) × D / (d_post × Δ)` |
| OIS floating payment | `N × [Π(1 + r_i × d_i/360) − 1]` |
| OIS fixed payment | `N × K × d/360` |
| Bond DV01 from bucket sum | `ΔP&L (TED spread change) ≈ Δs (bp) × ΣBucket 01` |
| Cash-flow of short FF stub via ED | `contracts_FF = contracts_ED × 25 / 41.67` |

## Mental Models
- **FRA = forward swap with settlement moved forward**: paying PV at the fixing date removes the reset-to-payment gap, which is why the FRA rate equals the forward rate exactly.
- **ED futures rate = forward rate + futures-forward (convexity) adjustment**: negligible in the front strip, material after 2 to 3 years; that is the reason the TED methodology is short-dated.
- **Tail intuition**: profits realised daily can be reinvested, so you need fewer contracts; the higher rates and the longer the horizon, the bigger the tail.
- **Hedge a bond as a strip of forward buckets**: a 1.6-year bond is roughly one ED contract per $1mm of price in each 3-month bucket, scaled down for partial buckets and tailed.
- **FF futures as a monthly average**: a 1bp change over the last 17 of 30 days moves the final rate by 17/30bp, so a one-per-$5mm hedge automatically decays as it should within the month.
- **Futures price = expectation only if you ignore risk premium**: implied FOMC probabilities embed term premium; treat them as upper-bound market pricing, not pure forecasts.
- **LIBOR-OIS as a price of liquidity insurance**: pay 20bp to fund for three months and you survive a run.

## Worked Example
**Tailed ED hedge (from the chapter).** A firm receives $100mm on 3/19/2012 and wants to lock a 90-day rate at 1.99% (EDH2 at 98.01).
- Unadjusted: buy 100 EDH2; P&L per 150bp move `= 100 × 150 × $25 = $375,000` (checked).
- Days trade to delivery: 661. Tail: `100/(1 + 0.0199 × 661/360) = 96.47` contracts (checked), so the tail is 3.53; buy 96.
- Result: with the immediate-jump scenario, total proceeds are $100.486mm at either 0.49% or 3.49% (table 15.7), versus $100.501mm and $100.470mm untailed. Tailing removes the asymmetry.

**Fed funds futures hedge (June 2010).** Bank lends $5mm overnight; buys one June FF contract at 99.780 (0.22%).
- Realised average 0.17667% (0.177% rounded): interest `5,000,000 × 30/360 × 0.17667% = $736.11`; hedge P&L `$41.67 × 4.3 = $179.18`; total $915.29 versus locked `$916.67` at 0.22% (checked). The $1.38 gap is the rounding of the settlement average.

**Implied FOMC probability (April 15, 2004).** Target 1.00%, May FF 1.02%, meeting May 4 (4 days pre, 27 post).
`1% + (27/31) × p × 0.25% = 1.02%` gives `p = 9.185%` (checked); expected post-meeting rate `= 1.023%`. For August: `1.105% + (21/31) × p × 0.25% = 1.22%` gives `p = 67.9%` (checked). Actual outcomes: 25bp at each of the next five meetings.

**OIS floating payment (June 1 to 14, 2010, $100mm).** Compounding the rates of the 10 accrual steps gives `$7,278.01` (checked), versus fixed 0.2%: `100mm × 14 × 0.2%/360 = $7,777.78`.

**TED spread trade.** Short $100mm of the 1 3/8s of 3/15/2012 at a 50bp TED spread; bucket 01 total $18,190. Spread falls to 38bp: expected P&L `12 × 18,190 = $218,280` (checked); realised: price move + hedge `= 201,558` plus repo carry 21,729 = `$223,287` (checked; column sum verifies).

## Anti-patterns
- **Reading ED price as a zero-coupon bond price**: it is a quoting convention for a 90-day rate only.
- **Ignoring the tail on long-dated ED strips**: an unhedged asymmetry that grows with rates and horizon.
- **One FF contract per $5mm in all months**: months with 28, 29, 31 days need 0.933, 0.967 and 1.033.
- **Hedging a corporate's spread with FF or ED futures and calling it perfect**: only the benchmark leg is hedged; credit spread and LIBOR-FF basis stay open (use a basis swap).
- **Extracting only one probability per meeting**: one futures price identifies one number (assumed 0 or 25bp); richer distributions need options.
- **Using the stub with FF futures without a LIBOR-FF basis check**: the FF stub hedge is internally inconsistent when the base curve is LIBOR.
- **Treating implied probabilities as pure forecasts**: risk premium and effective-target differences bias them.

## Practitioner Notes
- ED futures, then FRAs, were the workhorse for LIBOR hedges; ED is more liquid, FRAs are flexible in dates.
- Bloomberg-style TED screens use the definition here (spread-adjusted TED); it flags rich/cheap short Treasuries and spreads between two Treasuries, with the ED bucket hedge neutralising the curve.
- Hedge the stub with FF or T-bill-type instruments; reduce the first-month FF hedge gradually and switch to FF contracts when the front ED expires.
- Fed funds futures liquid to about 4 to 8 months; OIS to 2 to 3 years and is more accurate for rolling FF risk (compounding, customisable dates).
- Meeting-to-meeting OIS and IMM-to-IMM OIS (paired with ED) are the standard trades to hedge policy moves or the LIBOR-fed funds spread.
- The effective rate averaged within about two basis points of target through 2010; deviations occurred during crises (post 9/11, Lehman) and on year-end turns in the late 1990s.
- Repo GC generally sits somewhat under fed funds; an OIS overlay hedges the repo rate imperfectly (repo-FF spread moves).
- P&L attribution of a hedged trade: spread change × bucket-01 total + repo carry.

## Key Takeaways
1. FRA rate = forward rate because the FRA pays the PV of the rate difference at the fixing date.
2. ED price = 100 − rate, $25 per bp; tail the hedge by `1/(1 + r d/360)`; re-tail as time passes.
3. TED spread is subtracted from the ED base curve; positive for Treasuries; hedge with a bucket-by-bucket 01 strip in ED contracts (about one per $1mm price, scaled by period length).
4. FF futures settle on the monthly average effective rate; one contract per $5mm in a 30-day month, scaled by D/30, decaying when hedging a partial month.
5. OIS floating leg compounds effective FF daily; OIS beats FF futures for accuracy, tenor and date flexibility.
6. Implied FOMC probabilities come from solving the day-weighted monthly average for p; assumptions: rate changes only at meetings, 0 or 25bp, effective = target, no risk premium.
7. LIBOR-OIS is the market price of three-month funding security: about 8bp normal, 365bp peak in Oct 2008.
8. Basis, tail and stub mismatches (LIBOR vs FF) are the residual risks; quantify them.

## Connects To
- **ch13**: futures vs forwards and the tail; the origin of the ED tail rule.
- **ch12**: GC repo and specialness; the repo-fed funds relationship.
- **ch05**: forward bucket 01s, the analogue of the ED bucket hedge.
- **ch08**: risk premium and convexity in forward rates (limits of implied expectations).
- **ch16**: swaps, LIBOR-fed funds basis swaps, OIS discounting.
- **ch17**: two-curve discounting, LIBOR-OIS in valuation.
- **ch21**: rigorous curve construction when the TED shortcut is not acceptable.
- **`ilmanen-yield-curve` ch02**: market rate expectations vs forward rates, risk premia in short rates.
- **`hull-derivatives` ch06**: Eurodollar futures and the convexity adjustment.
- **`cfa-derivatives` ch03**: FRA and forward rate pricing at exam level.
