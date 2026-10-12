# Chapter 19: Corporate Bonds and Credit Default Swaps
> **Source**: Bruce Tuckman & Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 3rd ed. (Wiley, 2011), Chapter 19 · Selected Securities and Topics

## Core Idea
Credit risk is priced through a **spread that must pay for expected default loss (s ≈ λ(1−R)) plus a risk premium**. Analysts measure it four ways (yield spread, bond spread/OAS, par-par asset swap spread, market-value asset swap spread) and trade it two ways (cash bonds, CDS). The CDS/bond **basis** is not an arbitrage: a bond needs funding, a CDS does not, and the CDS buyer holds a delivery option. A **hazard rate** (constant default intensity λ) links everything: CDS quotes, upfronts, bond prices, and a credit-adjusted DV01.

## Frameworks Introduced
- **Four credit-spread measures** (same bond, different questions)
  - **Yield spread** = bond yield − par swap (or government) rate of similar maturity. Weak: it mixes cash-flow structure (coupon effect) and embedded-option value into "credit".
  - **Bond spread / OAS**: assume no default, find the spread over the benchmark curve (forward rates) that reprices the bond. Use plain Chapter 3 spread for straight bonds, OAS for callables.
  - **Par-par asset swap spread** `s_PAR`: buy the bond at P, finance 100 in repo, pay bond coupon c on a swap, receive LIBOR + s_PAR on 100 notional plus an upfront P−100. Spread is earned on **100**.
  - **Market-value asset swap spread** `s_Mkt = 100·s_PAR / P`: same cash flows, spread earned on **P**. The choice between the two is about collateral/counterparty exposure, not economics.
  - When to use: OAS for a like-for-like credit comparison across bonds; asset swap spread when the trade is "bond + swap + financing" or when comparing to CDS.
  - Failure mode: an asset swap keeps the credit risk. If the bond defaults, P&L ≈ `100R − P'` (P' is the pre-default price), so it also carries interest-rate risk in default, because the swap's NPV `100 − P` must be unwound.
- **Constant-hazard default model** (the workhorse)
  - Default probability over dt is λdt; survival `CS(T) = e^(−λT)`; cumulative default `CD(T) = 1 − e^(−λT)` (proof: `V(t+dt) = V(t)(1−λdt)` ⇒ `V′ = −λV`).
  - **Credit triangle**: hedged expected return equals r if `s = λ(1−R)`. In cumulative-default form `s = −((1−R)/T)·ln[1 − CD(T)]`.
  - Use it for a first-pass "is the market spread paying for realized defaults?" test and for CDS conventions.
- **CDS legs and fair hazard rate** (Bloomberg CDSW-style convention)
  - **Fee leg**: coupon paid quarterly, Act/360, until default or maturity, plus **accrued coupon at default** (default assumed mid-period).
  - **Contingent leg**: `(1−R)` × probability of default in each period × discount factor.
  - Fair CDS: find λ* so fee leg = contingent leg (R = 40% by convention), then `UF = (C(T) − C) × risky annuity`.
  - Failure mode: this is a *quoting* convention. A desk's own valuation need not use flat hazard or mid-period defaults.
- **Standardized CDS** (post-crisis "Big Bang" style)
  - Fixed coupon **100 or 500bp**, upfront adjusts; maturities on pseudo-IMM dates (20 Mar/Jun/Sep/Dec), ~5y and 10y liquid.
  - Upfront is paid to the protection **seller**; buyer also pays accrued since the last coupon date. Trades unwind by an offsetting trade at the new upfront, with no residual coupon mismatch.
  - Settlement: **physical** (deliver any eligible senior-or-better bond for 100, so a cheapest-to-deliver option exists) or **cash via auction** (payment `100(1−R)`; e.g., Lehman secured ≈ 9, WaMu senior 57 in Oct 2008).
- **CDS-bond basis** (three definitions, none an arbitrage)
  1. **Hazard-implied basis**: solve the bond-implied hazard from its price, then compute the CDS coupon that hazard implies (`C_Bond`), and compare with the CDS quote.
  2. **CDS − par asset swap spread**: popular pre-standardization. Appendix B shows `s_CDS − s_PAR = −[h·k + (1−h)·ρ*]` (minus weighted financing cost over LIBOR). It reduces to `L − r` if h=0 and ρ*=r−L, to 0 only if repo = LIBOR too.
  3. **Negative basis trade** (buy bond + buy CDS): locks in cash flows immune to default; profitable if the **breakeven funding cost** exceeds your cost of capital and financing stays available to term.
- **Credit-adjusted DV01/duration**: price the bond as `100c/2·Σ CS(tᵢ)d(tᵢ) + 100·CS(T)d(T) + 100R·Σ[CS(tᵢ₋₁)−CS(tᵢ)]d(tᵢ)` under the hazard curve, shift the benchmark curve 1bp, and reprice. Use for distressed bonds: yield-based duration overstates rate risk because default brings early, partial principal.

## Key Concepts
- **Indenture**: the bond contract with payment terms, priority and covenants, enforced by a trustee.
- **Strict priority**: secured, then senior unsecured, then subordinated; courts and negotiation often deviate (Lehman recoveries ranged ≈13%–52% by entity and class).
- **Investment grade**: Baa/BBB− or better; below is speculative/high yield.
- **Recovery rate**: fraction of principal ultimately returned; historical senior unsecured average ≈ 43.5% (IG) and 37.5% (speculative); industry convention **40%**.
- **Commercial paper / MTN**: CP is short discount paper, SEC-exempt if < 270 days; MTNs are customized issues sold under shelf registration.
- **Bond spread vs yield spread**: spread to the *curve* (cash-flow matched) vs to a single-maturity rate.
- **Asset swapper**: the investor who buys the bond and swaps it to floating.
- **Hazard rate λ**: instantaneous default intensity; CDS-implied λ is a market-consistent measure, not a physical probability.
- **CS(t) / CD(t)**: cumulative survival / default probability.
- **Fee leg / contingent leg**: PV of premium (incl. accrual) and PV of protection payment.
- **Upfront (UF)**: cash exchanged to convert the standard coupon to the market coupon.
- **Credit event**: bankruptcy, failure to pay, acceleration, repudiation/moratorium, restructuring (some contracts drop or restrict restructuring because it makes long debt cheapest to deliver).
- **CDS index (iTraxx, CDX)**: portfolio CDS on 125 names; defaulted name drops out with no replacement, shrinking notional. On-the-run rolls semi-annually.
- **Negative basis**: bond cheap to CDS (CDS spread < bond-implied), typical when funding is scarce; IG basis fell from ~0 to about −250bp in the 2007–09 crisis.
- **Burden of proof for "risk premium"**: spreads exceed realized-default-implied spreads, especially IG.

## Formulas & Reference Tables
| Item | Formula |
|---|---|
| Par asset swap spread | `s_PAR = (c·A_Fixed + 100·d − P) / (100·A_Float)` (d = discount factor to maturity; A = swap-curve annuities) |
| Market-value asset swap | `s_Mkt = (c·A_Fixed + 100·d − P) / (P·A_Float) = 100·s_PAR / P` |
| Bond spread (2-period ex.) | `P = c/(1+f₁+s) + (100+c)/((1+f₁+s)(1+f₂+s))` |
| Floating-note effective spread | `s_Eff = s_Float + (100 − P) / (100·A_Float)` |
| Hedged expected return | `(1−λdt)(r+s)dt − λdt(1−R) = r dt ⇒ s = λ(1−R)` |
| Cumulative default | `CD(T) = 1 − e^(−λT)`, `CS(T) = e^(−λT)` |
| Spread from cumulative default | `s = −[(1−R)/T]·ln[1−CD(T)]` |
| Fee leg (per unit notional) | `V_Fee = (C/4)ΣCS(tᵢ)d(tᵢ) + ½(C/4)Σ[CS(tᵢ₋₁)−CS(tᵢ)]d(tᵢ)` (actual Act/360 accruals in practice) |
| Contingent leg | `V_Cont = (1−R)Σ[CS(tᵢ₋₁)−CS(tᵢ)]d(tᵢ)` |
| Upfront (to seller) | `UF = (C(T) − C) × [ΣCS(tᵢ)d(tᵢ)/4 + ½Σ(...)d(tᵢ)/4]` = coupon difference × **risky annuity** |
| Bond-implied CDS coupon | `C_Bond = (1−R)Σ[CS(tᵢ₋₁)−CS(tᵢ)]d(tᵢ) / {ΣCS(tᵢ)d(tᵢ)/4 + ½Σ[…]d(tᵢ)/4}` |
| Negative-basis breakeven | `31.34 + (I(K)/4)(1+K)⁵ + I(K)Σ_{j=0..4}(1+K)^j = 0`, `I(K) = coupon − repo cost − K·equity − CDS fee` |
| Asset-swap P&L on default | `100R − P′` |
| Basis (Appendix B) | `s_CDS − s_PAR = −[h·k + (1−h)ρ*]` |

**Historical anchors** (Moody's, 1970–2009 cumulative default by original rating): 5y Aaa 0.1%, A 0.7%, Baa 1.9%, Ba 11.9%, HY 21.4%; 10y Baa 4.9%, Ba 20.0%, HY 34.0%; 20y HY 49.6%.
Realized-default-implied 5y spreads (bp): IG 2–20; B 89–641; HY 60–450. Widest market spreads: IG 619, B 1,825, Caa 2,992, HY 1,857; tightest: IG 82, B 239, Caa 395, HY 256. Market spreads exceed realized-default spreads almost always, by most for IG.

## Mental Models
- **Credit triangle**: spread ≈ hazard × loss-given-default. Given any two of (CDS spread, λ, R), the third follows. It is the quick sanity check on any quote.
- **Two legs, one hazard**: a CDS is an annuity (risky, survival-weighted) against a lump payment (1−R) weighted by default timing. Every "spread ↔ upfront" conversion is coupon difference × risky annuity.
- **Asset swap = spread in the numerator; OAS = spread in the denominator**. The asset swap explains the price gap as an extra cash flow, the OAS as extra discounting. Hence `s_Mkt > OAS > s_PAR` for discount bonds in the example.
- **Funding is the missing leg of the basis**: a bond position needs term financing, which is expensive and can vanish in stress; a CDS position needs only collateral. So negative basis = price of funding stress (and of the delivery option on the other side).
- **Distressed ≠ long**: with high λ, the bond behaves like a short, recovery-type instrument, so credit-adjusted duration is much shorter than yield duration.
- **Rating changes are the path to default**: most defaults come from a sequence of downgrades, and default, recovery and upgrade/downgrade ratios are all systematically correlated (systemic factor).

## Worked Example
**A. Spread measures** (recomputed). Two-year 4.25% annual bond at price 90; forwards 1% and 2%.
- OAS: solve `90 = 4.25/(1.01+s) + 104.25/((1.01+s)(1.02+s))` ⇒ **s = 8.525%** (check: `90(1.01+s)(1.02+s) = 108.947 = 4.25(1.02+s)+104.25`).
- Par asset swap: `A = 1/1.01 + 1/(1.01×1.02) = 1.9614`; `100·s_PAR·A = 4.25/1.01 + 104.25/(1.01×1.02) − 90` ⇒ **s_PAR = 7.855%**; `s_Mkt = 7.855×100/90 = 8.728%`.
- Bond yield 10.013%, par swap 1.495%, yield spread 8.518%. Return check: `90[1+(1%+8.728%)(1.02)+(2%+8.728%)] = 108.585 = 4.25(1.02)+104.25`.
- Interpretation: the credit-risky bond's spread ranges 7.9%–8.7% depending on definition; use one definition consistently.

**B. CDS upfront** (Deutsche Bank 5y EUR CDS, 21-Mar-2011, standard coupon 100bp, quote 95.33bp, R=40%). Solving fee = contingent on the actual Act/360 schedule (21 quarterly periods to 20-Jun-2016) gives **λ ≈ 1.61%** (book 1.611%; leg value 4.546% of face; my recompute 1.612%). Risky annuity ≈ 4.75 (per unit notional); `UF = (0.9533% − 1.00%) × 4.75 × €10m ≈ −€22,270`. The buyer *receives* it because the quote is below the 100bp coupon, and also pays €278 (1 day) accrued. Credit-triangle check: `95.33bp / 0.6 = 1.589%`, within 2bp of λ*. Note ≈99.8% of fee-leg value is the survival-weighted coupon; the accrual-on-default term is only ≈0.009%.

**C. Negative basis** (KB Home 5¾s Feb-2014, 10-Nov-2008): price 68.66; par asset swap spread 9.23%; CDS 664bp running. Per 100 notional, 50% haircut, repo 2%, capital cost K: initiation 0; interim cash flow `5.75 − 0.6866 − 6.64 − 34.33K = −1.5766 − 34.33K`; at maturity or default **+31.34** in every state. Breakeven K (solving the 5-year condition) ≈ **9.57%** (book "about 9.6%"). Any investor with cost of capital below ~9.6% and term funding locked wins in both states; the risk is financing being withdrawn or marked.

**D. Credit-adjusted DV01**. 10y, 6% semiannual, flat 4% benchmark, price 57.62, R=40%. Yield 14.0%, yield DV01 0.0365, duration 6.33 (book 6.34). Implied hazard **≈ 23%** (23.0% semiannual-compounded discounting). Shifting the benchmark 1bp gives DV01 ≈ 0.0228, **duration ≈ 3.95** — early recovery of principal cuts the rate sensitivity by ~40%.

## Anti-patterns
- **Quoting yield spread on callable or off-market-coupon bonds**: embedded options and coupon effect are counted as credit.
- **Treating CDS − asset swap spread as riskless arbitrage**: it needs default-payoff NPV = 0, financing at LIBOR, h = 0, and no delivery option; none holds.
- **Using historical average default/recovery as forecasts**: annual default rates range from <0.5% to 4% (overall) and <1% to >15% (HY); recovery is correlated with default and depends on the issuer's own capital structure (a fixed 40% is a convention, not a truth).
- **Using yield duration for distressed credits**: overstates DV01 (6.34 vs 3.95 in the example).
- **Running a negative basis trade with short-term funding**: haircut/repo withdrawal converts a "locked" trade into a mark-to-market and liquidity trade.
- **Assuming all deliverables are equal in CDS**: the cheapest-to-deliver (especially after restructuring) makes CDS protection worth more than a single-bond hedge.
- **Reading a rating as a stable statistic**: ratings are constantly adjusted; agencies were paid by issuers and kept IG on Enron/WorldCom until shortly before default.

## Practitioner Notes
- **Numbers to remember**: R = 40%; standard coupons 100/500bp; roll dates the 20th of Mar/Jun/Sep/Dec; 5y CDS maturity is really ~5y3m for the first days after a roll; iTraxx/CDX = 125 names; index maturity 63 months at issue, 57 at off-the-run.
- **Quote conventions**: high-yield/distressed names trade in upfront points (HOV 5y: 55.5 upfront + 500bp on 10-Nov-2008); investment grade trades in spread, converted to upfront; a quoted-spread view is easier to compare across credits.
- **Term structure of credit inverted** in the crisis: iTraxx Main 10y−5y and 5y−3y turned negative after Sept 2008 (default risk concentrated near term). Do not assume upward-sloping CDS curves in stress.
- **Basis reading**: bonds cheap to CDS when funding is hard (crisis IG basis about −250bp); bonds rich to CDS when shorting is expensive. In the Deutsche floater example the bond-implied hazard was 0.62% vs 1.61% for CDS, i.e., `C_Bond` ≈ 36.5bp vs 95.33bp quoted: bond "rich" to CDS by this metric, though the CDS delivery option flatters that reading.
- **Sovereign spreads** (Dec 2010): 5y bond spreads to OIS were Germany 2bp, France 22bp, Italy 144bp, Spain 244bp, Portugal 325bp, Ireland 486bp, Greece 962bp; against LIBOR the best names are negative because LIBOR embeds bank credit.
- **Rating policy**: Dodd-Frank ordered rating references out of US rules while Basel III kept them; ABS registrations briefly froze in July 2010 when agencies declined liability, and the SEC suspended the rating requirement.

## Key Takeaways
1. Compare credits on OAS/bond spread or on CDS-equivalent spreads, never on raw yield spreads with options or odd coupons.
2. `s ≈ λ(1−R)` is the anchor identity; with R=40%, spread/0.6 ≈ hazard.
3. Par and market-value asset swap spreads are the same economics: `s_Mkt = 100·s_PAR/P`; par swaps move collateral risk to whoever is on the wrong side of P−100.
4. A CDS is priced with a hazard curve: fee leg (with accrual) = contingent leg; upfront = (market − standard coupon) × risky annuity.
5. The CDS-bond basis is not an arbitrage; funding cost and delivery option explain persistent, sometimes extreme (−250bp) gaps.
6. Negative basis trades pay the same in default and non-default (31.34 in the example) but require term financing; compute breakeven cost of capital before entering.
7. Credit-adjust DV01/duration with a hazard rate for anything trading at a distressed price.
8. Realized default losses have been well below market spreads for IG; treat the excess as premium/illiquidity, but expect episodic realized shocks (2007–09).

## Connects To
- **ch03**: bond spread definitions, coupon effect; OAS foundation.
- **ch07**: OAS and option-adjusted return logic.
- **ch12**: repo haircuts and term-funding risk, essential to the basis trade.
- **ch15**: TED/LIBOR–OIS spreads and short-term funding cost.
- **ch16**: swap annuities, fictional-notional trick, collateral and counterparty risk in swaps.
- **ch17**: two-curve (OIS) discounting; discount curve for CDS legs and asset swaps.
- **ch18**: callable corporate bonds valued with OAS.
- **ch20**: another security whose price depends on an intensity/prepayment model.
- **`cfa-fixed-income` ch11**: CDS valuation, upfront and market conventions (CFA framing).
- **`cfa-fixed-income` ch10**: credit analysis models (structural/reduced-form) behind λ.
- **`cfa-fixed-income` ch06**: fundamentals of credit analysis (seniority, covenants, recovery).
- **`hull-derivatives` ch25**: credit derivatives and hazard-rate valuation.
