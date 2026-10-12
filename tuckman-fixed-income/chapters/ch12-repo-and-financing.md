# Chapter 12: Repurchase Agreements and Financing
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 12 · Part Four, Selected Securities and Topics

## Core Idea
A repo is a sale of a security with an agreed repurchase at a fixed higher price. It is one contract with three uses: secured cash investment, financing a long position, and borrowing a bond to deliver on a short. The price of the contract, the repo rate, splits into a **general collateral (GC)** rate for "any acceptable bond" and a **special** rate for a specific bond that is in demand to borrow. The **special spread** (GC minus special) is the financing value of owning that bond. In the US it is driven mainly by the auction cycle and it is capped by the cost of failing. Repo is cheap, secured funding, but it is also the funding that disappears first in a crisis (Bear Stearns, Lehman/JPM tri-party).

## Frameworks Introduced
- **Repo mechanics (sale + repurchase)**:
  - At the start, A sells the bond to B for the invoice (full) price P₀ and agrees to buy it back at the terminal date for `P₀ × (1 + r_repo × d/360)`. Money-market convention is act/360.
  - A is the **repo** side: A "repos out" or "sells the repo", borrows cash and delivers collateral.
  - B is the **reverse repo** side: B "reverses in" or "buys the repo", lends cash and receives the bond.
  - The same trade is a repo for one side and a reverse for the other. Always say whether *cash* or *securities* is being borrowed or lent.
- **Three motives for repo**:
  | Motive | Who | Side | Collateral | Rate |
  |---|---|---|---|---|
  | Cash management (secured, liquid investment) | MMFs, municipalities, insurers, pensions, corporates | Lends cash (B) | General collateral: any bond in an agreed class | GC (highest for that collateral class) |
  | Long financing | Dealer inventory, prop positions, customer financing (back-to-back repo) | Borrows cash (A) | The bond being financed | GC, or below GC if the bond is special |
  | Short covering | Hedgers, relative-value traders | Borrows the bond (B), lends cash | A specific bond | Special rate ≤ GC |
- **Credit protection of the cash lender**:
  - **Haircut**: lend less than the collateral value. Example: lend €106mm against €111.772mm of bunds, a 5.16% haircut. The haircut must be funded with the borrower's own capital.
  - **Margin calls / repricing**: if collateral value falls, the borrower posts the shortfall; if it rises, the borrower may withdraw collateral.
  - **Right-way risk**: when a dealer borrower defaults, a flight to quality tends to *raise* the value of government collateral, which helps the lender.
- **Rolling a repo**:
  - At maturity, either renew with the same counterparty or unwind and re-repo with a new lender (back-to-back, Fig. 12.3).
  - Cash raised on the new leg depends on the current bond price. Cash owed on the old leg is fixed. The roll therefore produces a cash surplus or deficit, which the P&L of the hedge on the inventory offsets.
- **Funding-stability spectrum (liquidity management)**:
  - From most stable to least: equity → long-term debt → term repo → overnight repo → short-term unsecured (CP) → customer cash and unencumbered securities (prime brokerage).
  - More stable funding costs more.
  - Losses usually start a dealer's trouble, but *loss of financing* is the killing blow: repo lenders stop rolling, the dealer must fire-sell inventory, and it may no longer be an acceptable derivatives counterparty.
  - **Systemic tension**: borrowers (and their regulators) want longer repo terms, lenders (and theirs) want shorter ones. The system as a whole cannot do both.
- **Special spread economics**:
  - The special rate for bond X to date T is set by the supply and demand *to borrow* X. That differs from the supply and demand *to own* X, because some holders never lend.
  - A bond can trade rich in the cash market without trading special, and vice versa.
  - In the US the dominant driver is the **auction cycle**: OTR bonds trade most special, then old, then double-old.
- **Fail-cost bound on specialness**:
  - Before May 2009 there was no fail penalty. Failing costs only the interest forgone on the unpaid sale proceeds, which is the same as borrowing the bond at a 0% special rate.
  - So the special rate floor was 0%, and the special spread was capped at the GC rate.
  - From May 1, 2009, the TMPG fails charge = `max(3% − fed funds target, 0)` per annum. The special rate can go as low as about −penalty, so the spread can reach about GC + penalty (≈3% when policy rates are near zero).
  - **⚠ Precision**: the book calls the new cap simply "the penalty rate". Strictly it is GC + penalty, and that equals the penalty only when GC ≈ 0, which was the case in 2009.
- **Financing value of a special bond**:
  - It is the PV of lending the bond, borrowing cash at the special rate, and investing that cash at GC, over the period the bond is expected to stay special.
  - Take the horizon from the repo trader's view or from the market's forward special spreads.
  - Convert to yield by dividing by DV01.

## Key Concepts
- **Repo rate**: the simple act/360 interest rate implied by the repurchase price relative to the initial invoice price.
- **Overnight / term / open repo**: overnight = to the next business day ("overnight", not "one-day", because the tri-party unwind happens intraday). Term = any maturity longer than one day. Open = an overnight repo that renews automatically until either party cancels.
- **General collateral (GC)**: repo where the cash lender accepts any security in a defined class. "The" GC rate is the overnight US Treasury GC rate.
- **Special collateral / specials trade**: repo requiring delivery of a specific issue. A bond **trades special** when its repo rate is materially below GC.
- **Special spread (specialness)**: `GC rate − special rate` for the same term.
- **Haircut**: the percentage by which the loan is smaller than the collateral's market value.
- **Right of substitution**: in term repo, the cash borrower may swap collateral for bonds of comparable value and quality, for example when it needs to sell the bond being financed.
- **Tri-party repo**: repo settled through a clearing bank (JPM, BNY Mellon). Investors' loans are overnight, but historically the clearing bank advanced the cash intraday to the dealer, so it carried the dealer's entire tri-party book each day.
- **Unencumbered securities**: securities not yet pledged. For prime brokers, customer cash and unencumbered securities are the least stable funding source.
- **Fail**: failure to deliver a sold security on settlement. The seller does not receive cash until delivery.
- **On-the-run (OTR) / old / double-old**: the most recent, second and third most recent issues at a given maturity. Everything else is off-the-run (OFR). "The bond" is the historical nickname of the OTR 30-year.
- **Re-opening**: an auction that adds to an existing issue. Re-opened issues get less special than new issues.
- **Fed funds–GC spread**: the unsecured interbank rate minus Treasury GC, about 16bp on average in late 2009–mid 2010. It widens when Treasuries are scarce (late-1990s surpluses) and in flight-to-quality stress (GC < 0.50% with fed funds at 2.25% after Bear Stearns).
- **Forward special spread**: the special spread implied between two term dates.

## Formulas & Reference Tables
- Repurchase price: `P_T = P₀ × (1 + r × d/360)`, with P₀ the initial invoice (full) price, r the repo rate and d the actual days.
- Haircut: `h = 1 − Loan/CollateralValue`. Equity required = `h × CollateralValue`.
- Special spread: `s = r_GC − r_special`.
- Forward special spread (simple-interest approximation): `d₁ × s₁ + (d₂ − d₁) × s_fwd ≈ d₂ × s₂`, so `s_fwd ≈ (d₂s₂ − d₁s₁)/(d₂ − d₁)`.
- Financing value of specialness per 100 market value: `V = 100 × s_term × d/360`. Per 100 face: `V × P/100`. In yield: `V_face / DV01` (bp).
- TMPG fails charge (from May 1, 2009): `penalty = max(3% − FF_target, 0)` per annum. Daily cost of failing on face F: `F × penalty/360`.
- Bound on specialness: before 2009, `r_special ≥ 0`, so `s ≤ r_GC`. After, `r_special ≳ −penalty`, so `s ≲ r_GC + penalty`.

**Table 12.1 (overnight, May 28, 2010, GC 0.23%)**: the pattern is the lesson.
| Issue | Repo | Spread |
|---|---|---|
| OTR 10y (3½s May-20) | 0.09% | 14bp |
| Old 10y | 0.21% | 2bp |
| Dbl-old 10y | 0.21% | 2bp |
| OTR 30y | 0.18% | 5bp |
| Old / Dbl-old 30y | 0.20% / 0.21% | 3 / 2bp |

**Table 12.2 (term structure of OTR 10y specialness, May 28, 2010)**:
| Term | Days | Special | GC | Term spread | Fwd spread |
|---|---|---|---|---|---|
| O/N | 4 | 0.09% | 0.23% | 0.14% | 0.14% |
| 1W | 7 | 0.00% | 0.23% | 0.23% | 0.35% |
| TYM0 (6/30) | 33 | −0.10% | 0.22% | 0.32% | 0.34% |
| 2M | 61 | −0.05% | 0.23% | 0.28% | 0.23% |
| 3M | 94 | 0.00% | 0.25% | 0.25% | 0.20% |
| TYU0 (9/30) | 125 | 0.04% | 0.26% | 0.22% | 0.13% |
| TYZ0 (12/31) | 217 | 0.17% | 0.30% | 0.13% | 0.01% |

Term repo dates cluster on **futures expiries** because OTR basis traders (ch14) need to finance or borrow to those dates.

## Mental Models
- **Repo is one contract, three stories.** Ask who initiated it and why. The cash investor wants GC and safety. The financer wants the lowest rate. The short wants *that* bond and pays for it by accepting a below-GC rate on its cash.
- **Specialness is a dividend paid to the owner of the bond.** Owning a special bond lets you borrow at below GC. That stream of "repo dividends" is part of why OTRs trade rich, and it shows up directly in the forward price (ch13) and in futures basis (ch14).
- **Think of specialness as a short squeeze with a cap.** Demand to short builds through the auction cycle. The spread can go no further than the point where failing is cheaper than borrowing.
- **Borrow–lend demand is not buy–sell demand.** Richness (cash market) and specialness (repo market) are related but separate. Don't infer one from the other without checking the lendable supply.
- **Funding stability costs carry.** Overnight repo is cheapest precisely because the lender can leave tomorrow. Price the option you give your lenders.

## Worked Example
**1. Repo cash flows with haircut and margin call (bunds, act/360).**
- A repos €100mm face DBR 4s Jan-2037 on May 31, 2010, at an invoice price of €111.772mm, repo rate 0.23%, 92 days.
- Repurchase price = 111,772,000 × (1 + 0.0023 × 92/360) = **€111,837,697.10**.
- With a haircut the lender advances only €106mm, so h = 1 − 106/111.772 = **5.16%**, and A funds €5.772mm of the position from its own capital.
- If the bunds fall to €110mm, A posts €1.772mm more collateral. The lender again holds €111.772mm of value against a €106mm loan.

**2. Forward special spread (Table 12.2, June 30 → July 28).**
- 33 × 0.32% + 28 × s_fwd ≈ 61 × 0.28%, so s_fwd ≈ (17.08 − 10.56)/28 = **0.233% ≈ 0.23%**.
- The forward spreads rise into the June re-opening and fall to about 1bp for Sep-30→Dec-31. The market expects the 3½s to lose specialness within about a month of the August new issue.

**3. Financing value of the OTR 10-year (3½s May-2020, price 101.90, DV01 ≈ 0.085).**
- The bond is assumed special only until Sep 30 (125 days, term spread 0.22%): V = 100 × 0.22% × 125/360 = **0.0764 per 100 market value**.
- Per 100 face: 0.0764 × 1.019 = **0.0778**. In yield: 0.0778/0.085 ≈ **0.9bp**.
- The bond traded about 2 points rich to the C-STRIPS curve (ch01), so almost all of the premium is *liquidity*, not financing.

**4. Cost of failing.** Failing on $100mm with the penalty at 3% (fed funds ≈ 0) costs 100,000,000 × 3%/360 = **$8,333 per day**, on top of the forgone interest.

## Anti-patterns
- **Saying "I lent in repo" without saying lent *what***: the cash side and the bond side use opposite words. Specify cash or securities.
- **Treating repo as stable funding because it is secured**: it rolls mostly overnight, so it can vanish at the speed of its maturity. Bear Stearns replaced CP with repo and still lost its funding in one week in March 2008.
- **Financing lower-quality collateral in repo because rates and haircuts look cheap**: pre-2007 this led to margin calls, higher haircuts and lost financing, then collateral liquidation and failure.
- **Assuming the cash lender can actually liquidate collateral**: many MMFs and other investors found in 2008 that they lacked the expertise or operations to do it.
- **Valuing a special bond's premium as pure financing value**: in the 3½s example specialness explains about 8 cents of a 2-point premium.
- **Projecting specialness forever**: forward special spreads usually converge to about 0 soon after the next new issue. Use the term structure, not today's overnight spread.
- **Assuming the special rate can't go negative**: that was true only when fails were free. It has not held since the 2009 TMPG fails charge.

## Practitioner Notes
- **Desk conventions**: repo is quoted as a simple act/360 rate on the full (invoice) price. Term dates quoted for OTRs typically include fixed tenors plus futures expiry dates (TYM0/TYU0/TYZ0), for basis trades.
- **Shorts**: the P&L of a naked short via reverse repo is roughly (repo interest earned on the cash) − (total return on the bond). The short wins only if the bond returns less than the (special) repo rate. Borrowing a very special bond therefore erodes short P&L.
- **Holders of special bonds should not finance them GC**: a desk long a special issue should lend it in the specials market and borrow cash below GC.
- **Auction-cycle pattern (US 10-year, 1997–2010)**: specialness is small right after an auction because shorts can stay in the old OTR and the re-opening adds supply. It builds as shorts migrate to the OTR, and spikes before the next auction as the market shorts the OTR to hedge purchases of the new issue. Spreads of hundreds of bp are common and very volatile day to day. 5-year behaves like 10-year. Shorter tenors are less special because issuance is frequent. The 30-year has been muted since the 2001 halt, except around its 2005–06 reintroduction.
- **Other markets**: in Germany, deliverability into highly liquid futures drives liquidity more than issue age. In Japan it is a mix of the auction cycle and deliverability.
- **Fails spike in stress**: 10-year OTR fails reached $5.311 trillion in the week of Oct 22, 2008, vs a $165bn pre-crisis average. That pushed regulators to impose the fails charge. In June 2009 specialness hit the new cap.
- **Tri-party lesson**: the clearing bank bore the intraday risk of the whole book. By mid-August 2008 JPM had phased in haircuts on intraday advances to Lehman and then demanded $5bn of extra cash collateral. Collateral fights intensify precisely as default nears. At the time of writing, the industry was working to remove this intraday exposure.

## Key Takeaways
1. A repo is a secured loan written as a sale plus repurchase. The repurchase price is `P₀(1 + r·d/360)` on the invoice price.
2. GC repo serves cash investors and most financing. Specials serve shorts. The special spread is the price of borrowing a specific bond.
3. Haircuts and margin calls protect cash lenders, but they use the borrower's capital and can trigger liquidity spirals when raised in stress.
4. Repo is cheap but among the least stable funding sources. A run on repo financing is how dealers die (Bear, Lehman).
5. US specialness follows the auction cycle: OTR > old > double-old. It is lowest after auctions and peaks just before them.
6. Specialness is bounded by the cost of failing: 0% special rate pre-2009, and about −(3% − fed funds) after the TMPG fails charge.
7. Value specialness as `100 × s × d/360` over the expected special period and divide by DV01 for yield. It is often a small part of an OTR's premium.

## Connects To
- **ch00**: institutional background on repo, tri-party and liquidity risk.
- **ch01**: the 3½s richness to C-STRIPS, which this chapter decomposes into liquidity vs financing.
- **ch02**: the forward-rate approximation used for forward special spreads.
- **ch13**: forward price = spot + financing cost − coupon. The repo rate, special or GC, sets forward drop and carry.
- **ch14**: implied repo rate vs actual (special) repo drives the note/bond futures basis. OTR basis trades cluster term repo at futures expiries.
- **ch15**: fed funds, GC and OIS as short-term rate benchmarks. Fed funds–GC spread.
- **ch17**: arbitrage with financing and the funding cost of positions.
- **`cfa-fixed-income` ch02**: repo mechanics, haircuts and repo-rate determinants at CFA level.
- **`hull-derivatives` ch04**: the repo rate among the market's reference rates.
- **`hull-derivatives` ch05**: cost-of-carry forward pricing, where the financing rate is the repo rate.
