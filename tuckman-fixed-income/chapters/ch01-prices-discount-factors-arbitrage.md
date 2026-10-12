# Chapter 1: Prices, Discount Factors, and Arbitrage
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 1 (Part One: The Relative Pricing of Securities with Fixed Cash Flows)

## Core Idea
Bond prices embed **discount factors** d(t), the market price today of one unit of currency paid at t. Extract d(t) from a set of liquid bonds, and the **law of one price** prices any other bond with the same cash-flow dates. Pricing with discount factors is **mathematically identical** to pricing by **arbitrage** (the cost of a replicating portfolio), so discounting is shorthand for arbitrage pricing. In practice bonds are *not* commodities. Liquidity, financing (repo specialness), taxes and supply make individual issues trade rich or cheap. The US **STRIPS** market shows it: P-STRIPS inherit the idiosyncratic pricing of their parent bond.

## Frameworks Introduced
- **Bootstrapping discount factors from coupon bonds**
  - When to use: you have bonds whose payments all fall on one cycle (e.g., May/November 30) and want d(t) on each date.
  - How:
    1. Write one pricing equation per bond: full price = Σ cash flow × d(date).
    2. Sort by maturity. The shortest bond has one unknown: `P₁ = (100 + c₁/2)·d(.5)`.
    3. Solve sequentially. Each new bond adds exactly one new unknown, the d(t) at its maturity.
  - Why it works: with one bond maturing per date the cash-flow matrix is triangular.
  - Failure mode: using flat (clean) prices instead of **full** prices, or mixing bonds on different payment cycles (the dates no longer line up).
- **Law of one price**: absent confounding factors (liquidity, financing, taxes, credit risk), identical cash flows sell for the same price. So `PV = Σ CFₜ·d(t)` using the base-bond d(t)'s.
  - Tells you which bonds are **rich** (price > PV) or **cheap** (price < PV) *relative to the base bonds*. It is not an absolute judgment.
- **Arbitrage pricing via a replicating portfolio**
  - When to use: to turn a rich/cheap signal into a trade, or to price a bond with no model assumptions.
  - How:
    1. Choose T base bonds that **span** the T payment dates (at least one base bond pays on every date, including the last).
    2. Solve `C·F = c` for face amounts F, where column j of C holds bond j's cash flows per unit face on each date and c holds the target bond's cash flows.
    3. Replicating cost = `P′·F`.
    4. If target price < cost, buy the target and short the replica. If target price > cost, do the reverse.
  - The solution: `F = C⁻¹·c`. With one base bond maturing per date, solve backwards from the last date (it is triangular).
  - Why it works: the replica's cash flows match the target's on every date, so the net position owes nothing in the future and the price gap is a riskless profit.
  - Failure modes:
    - Bid/ask on the bonds (mid prices overstate the profit).
    - Bid/ask in the financing (repo) market for the shorts.
    - Bonds are not fungible, so an apparent mispricing can be a fair premium for liquidity or financing.
- **Equivalence of discounting and arbitrage (Appendix B)**: with d = (C′)⁻¹·P and F = C⁻¹·c, the price by discounting is `c′d = c′(C′)⁻¹P` and by replication `P′F = P′C⁻¹c`. These are the same scalar (one is the transpose of the other). **Discounting = arbitrage pricing.**
- **STRIPS test of idiosyncratic pricing**: C-STRIPS are fungible across bonds and P-STRIPS are not. A P-STRIPS can only reconstitute the bond it came from, so it carries that bond's richness or cheapness.
  - Diagnostic: price each bond with (a) C-STRIPS d(t) for all flows, then (b) C-STRIPS for coupons plus *its own* P-STRIPS for principal. If (b) fits much better, the bond's premium sits in its principal STRIPS.
  - The book's result (15 long Treasuries, May 2010): method (b) beat method (a) for every bond. The on-the-run 10-year 3½s of 5/15/20 was mispriced by **2.076** under C-STRIPS alone but only −0.086 using its P-STRIPS.

## Key Concepts
- **Face / principal / par amount, coupon rate, maturity**: define a fixed-rate government bond. US coupons are semiannual: each payment is `½ × coupon × face`.
- **Coupon frequency by market**: annual for France and Germany; semiannual for the US, Italy, Japan and the UK.
- **Business-day rule**: a payment falling on a non-business day is paid the next business day.
- **T+1 settlement**: standard for US Treasuries.
- **Mid-market price**: the average of bid (dealer buys) and ask (dealer sells).
- **Full (invoice, dirty) price**: what the buyer pays. It equals the **flat (quoted, clean) price** plus **accrued interest**.
- **Discount factor d(t)**: PV of 1 unit paid at t. It falls with t (time value of money).
- **Rich / cheap**: priced above / below the value implied by base-bond discount factors.
- **Arbitrage**: a trade with profit and no chance of loss. Practitioners use the word loosely for trades with large expected profit relative to risk.
- **Short sale**: selling a bond you do not own. The short receives the price and must pay all coupons and principal (mechanics in ch12, via repo).
- **Replicating portfolio**: bonds whose combined cash flows equal the target's on every date.
- **Spanning set**: T bonds with at least one paying on each of T dates, so that C is invertible.
- **STRIPS (Separate Trading of Registered Interest and Principal of Securities)**: Treasury zero-coupon bonds created by stripping a coupon bond. **C-STRIPS** (TINTs, INTs) come from coupons and **P-STRIPS** (TPs, Ps) from principal. STRIPS prices are essentially discount factors.
- **Reconstitution**: delivering STRIPS back to the Treasury to rebuild the bond. Any C-STRIPS of the right date works, but only the bond's own P-STRIPS.
- **On-the-run**: the most recently auctioned issue at a maturity point. It trades rich for liquidity and financing (special repo) reasons.
- **Day-count conventions**: actual/actual (government bonds), actual/360 (money markets, discount securities, swap floating legs), 30/360 (corporates, swap fixed legs).

## Formulas & Reference Tables
- Bootstrapping (semiannual coupon c in %, per 100 face): `P_n = Σᵢ₌₁ⁿ⁻¹ (c/2)·d(i/2) + (100 + c/2)·d(n/2)`, so `d(n/2) = [P_n − (c/2)·Σᵢ₌₁ⁿ⁻¹ d(i/2)] / (100 + c/2)`.
- Law of one price: `PV = Σₜ CFₜ·d(t)`. Richness = `Price − PV` (>0 rich, <0 cheap).
- Replication: `C·F = c ⇒ F = C⁻¹·c`. Replicating cost = `P′F`.
- Discount factors from a spanning set: `d = (C′)⁻¹·P`. Equivalence: `c′d = P′F`.
- Full price identity: `P = p + AI = PV` (P full, p flat, AI accrued interest).
- Accrued interest: `AI = (c/2) × (days since last coupon / days in coupon period)` under actual/actual, semiannual.
- 30/360 day count between D₁ = (y₁,m₁,d₁) and D₂: `360(y₂−y₁) + 30(m₂−m₁) + (d₂−d₁)` days, divided by 360.
- Treasury price quotes in 32nds: `102-26 = 102 + 26/32 = 102.8125`.

| Convention | Day count | Typical market |
|---|---|---|
| Actual/actual | actual days / actual days in period | Government bonds (UST, most sovereigns) |
| Actual/360 | actual days / 360 | Money markets, T-bills, swap floating legs |
| 30/360 | 30-day months / 360 | Corporate bonds, swap fixed legs |

| US Treasury bootstrapped d(t), 28-May-2010 (verified) | d(t) |
|---|---|
| 30-Nov-2010 (0.5y) | 0.99925 |
| 31-May-2011 (1.0y) | 0.99648 |
| 30-Nov-2011 (1.5y) | 0.99135 |
| 31-May-2012 (2.0y) | 0.98532 |
| 30-Nov-2012 (2.5y) | 0.97520 |
| 31-May-2013 (3.0y) | 0.96414 |
| 30-Nov-2013 (3.5y) | 0.94693 |
| 31-May-2014 (4.0y) | 0.93172 |
| 30-Nov-2014 (4.5y) | 0.91584 |

These come from the 1¼s Nov-10 (100.550), 4⅞s May-11 (104.513), 4½s Nov-11 (105.856), 4¾s May-12 (107.966), 3⅜s Nov-12 (105.869), 3½s May-13 (106.760), 2s Nov-13 (101.552), 2¼s May-14 (101.936) and 2⅛s Nov-14 (100.834), all full prices.

## Mental Models
- **Think of every bond as a bundle of zeros.** Its value is the sum of its cash flows priced at d(t). Everything else in the book (rates, yields, spreads, DV01) is a re-expression of d(t).
- **"Rich/cheap" is always relative to a chosen base set.** Change the base bonds and the verdict can change. State the benchmark.
- **Use arbitrage logic, not model logic.** A replicating portfolio makes no assumption about rate dynamics, only that cash flows match.
- **Before trading an apparent mispricing, ask why it exists.** Candidates: on-the-run liquidity premium, repo specialness, tax effects (high- vs low-coupon), limited supply, bid/ask. The residual is often compensation, not free money.
- **Track flat prices, settle on full prices.** The full price jumps down by the coupon on every coupon date even when markets are unchanged. The flat price moves smoothly, which is why screens quote it.

## Worked Example
**1. Law of one price and an arbitrage (Tuckman Tables 1.3–1.5, verified).**
- Target: the ¾s of 30-Nov-2011, flows of 0.375, 0.375 and 100.375 on 0.5, 1.0 and 1.5 years. Market price **100.190**.
- PV with bootstrapped d(t): `0.375×0.99925 + 0.375×0.99648 + 100.375×0.99135 = 100.255`. So the bond is **6.5 cents cheap**.
- Replicating portfolio (solve backwards from the last date):
  - 30-Nov-11: F₃ × 1.0225 = 100.375 ⇒ **F₃ = 98.166** face of the 4½s Nov-11.
  - 31-May-11: F₂ × 1.024375 + 98.166 × 0.0225 = 0.375 ⇒ **F₂ = −1.790** face of the 4⅞s May-11.
  - 30-Nov-10: F₁ × 1.00625 − 1.790 × 0.024375 + 2.209 = 0.375 ⇒ **F₁ = −1.779** face of the 1¼s Nov-10.
  - Replica cost = −1.779×1.00550 − 1.790×1.04513 + 98.166×1.05856 = **100.255**, equal to the PV, as the equivalence proposition says.
- Trade: buy the ¾s at 100.190 and sell the replica at 100.255, for **+0.065 per 100** with no future obligations. On $500mm face that is **$325,000**. It must survive bid/ask on four bonds and repo costs on the shorts.
- In the same table the ⅞s May-11 is **2.8 cents rich** (PV 100.521 vs price 100.549) and the ¾s May-12 is 5.9 cents cheap.

**2. Arbitrage price of the on-the-run 10-year (end-of-book Exercise 1.5, verified).**
- Inputs: the 0s of 15-May-2020 at 69.21 and the 8¾s of 15-May-2020 at 145.67. Both mature on the same date as the 3½s.
- Every bond with those dates is a combination of the zero and the 8¾s, so `P(3½s) = P(0) + (3.5/8.75)·[P(8¾s) − P(0)] = 69.21 + 0.4 × 76.46 = **99.794**`.
- The market traded the on-the-run 3½s near 101.9. The gap of roughly 2 points is the on-the-run premium, consistent with the 2.16 P-STRIPS minus C-STRIPS gap at that date.

**3. Accrued interest (verified).**
- The 3⅝s of 15-Aug-2019, settling 1-Jun-2010. The last coupon was 15-Feb, and the period is 181 days, of which 106 have elapsed.
- AI = 106/181 × 1.8125 = **1.0615** per 100.
- Quoted 102-26 = 102.8125, so the full price = **103.8740**. For $10,000 face the buyer pays $10,387.40.
- On 30/360, 1-Jun to 15-Aug counts 74 days, vs 75 actual.

## Anti-patterns
- **Discounting flat prices**: PV must equal the *full* price. Using the flat price mis-states every d(t).
- **Taking mid-price mispricings at face value**: bid/ask on the bonds and on repo (for the shorts) can erase cents-level edges.
- **Assuming Treasuries are fungible collections of cash flows**: on-the-runs, cheapest-to-deliver issues, specials and high-coupon off-the-runs all carry idiosyncratic premia.
- **Pricing a bond off C-STRIPS alone**: the bond's own P-STRIPS carries its richness. A C-STRIPS-only fit misses the on-the-run 10-year by more than 2 points.
- **Choosing a non-spanning replicating set**: T bonds all maturing *before* the last payment date leave C singular, so replication is impossible.
- **Believing the accrued convention changes value**: it doesn't. If a convention favors sellers, the flat price adjusts down. Only the invoice price matters.

## Practitioner Notes
- Desks bootstrap on a single coupon cycle because it keeps the system triangular. Real curve builders fit smooth curves across all issues instead (ch21).
- A replicating portfolio for a bond maturing on a date shared with a base bond is dominated by that base bond (98% of the ¾s replica is the same-maturity 4½s). The other bonds only patch the early coupons. Expect the P&L to be driven by the same-maturity pair.
- STRIPS rich/cheap analysis is a standard Treasury relative-value tool. **P-STRIPS minus C-STRIPS** of the same date measures the parent bond's premium. The book found the on-the-run 10-year at **2.16** per 100, the widest point on the curve.
- Scale matters. 6.5 cents looks trivial, but on typical position sizes ($500mm) it is $325k, which is why RV desks care about cents.
- Sign convention: in the replication table a negative face means short, and the "cost" of a short is negative, i.e., proceeds.

## Key Takeaways
1. Extract d(t) from full prices of liquid bonds by bootstrapping. Every fixed cash flow is then priced as `Σ CF·d(t)`.
2. The law of one price and arbitrage pricing give the *same* number. Discounting is shorthand for replication.
3. To trade a mispricing, build the replica with `F = C⁻¹c` from a spanning set, then buy cheap and sell rich.
4. Real bonds carry idiosyncratic value (liquidity, repo, taxes). An observed deviation is often a premium, not an arbitrage.
5. C-STRIPS are fungible and P-STRIPS are not, so P-STRIPS reveal bond-specific richness (the on-the-run 10-year ≈ +2 points).
6. Full = flat + accrued. Price with full, quote with flat, and know the day count (act/act, act/360, 30/360).

## Connects To
- **ch00**: why swaps, being fungible, replaced government bonds as benchmarks.
- **ch02**: converting d(t) into spot, forward and par rates.
- **ch03**: expressing rich/cheap as spreads and yields; the flat price's pull to par.
- **ch12**: repo, specials and the on-the-run financing advantage.
- **ch21**: fitting smooth curves across all bonds.
- **`cfa-fixed-income` ch03**: bond pricing with spot rates, flat/full price and accrued interest.
- **`hull-derivatives` ch04**: zero rates, bootstrapping and day counts.
