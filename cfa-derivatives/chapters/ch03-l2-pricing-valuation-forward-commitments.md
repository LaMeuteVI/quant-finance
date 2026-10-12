# Chapter 3: Pricing and Valuation of Forward Commitments
> **Source**: CFA Program Curriculum 2021, Level II, Reading 33 · Derivatives | Adam Schwartz, PhD, CFA (L2 errata applied: Example 16)

## Core Idea
Forwards, futures and swaps are priced by **carry arbitrage**: buy (or short) the underlying, finance at the risk-free rate, and offset the price risk with the forward. The forward **price** F₀ is the future value of the underlying adjusted for carry cash flows, and it makes the contract's value zero at inception. The **value** of an existing contract is the present value of the difference between today's forward price and the original one. A swap is priced and valued the same way, as a portfolio of bonds (interest rate, currency) or equity plus a bond (equity swap).

## Learning Outcomes Covered
- Describe the carry arbitrage model with and without underlying cash flows.
- Price equity forwards/futures and value them (no-arbitrage).
- Price interest rate forwards/futures (FRAs) and value them.
- Price fixed-income forwards/futures (accrued interest, conversion factor) and value them.
- Price and value interest rate swaps.
- Price and value currency swaps.
- Price and value equity swaps.

## Frameworks Introduced
- **Carry arbitrage model** (cost-of-carry / cash-and-carry): F₀ = FV(S₀ + CC₀ − CB₀).
  - When to use: any forward or futures on an asset you can buy or short (stock, index, bond, currency).
  - How: (1) write the underlying's carry costs CC (storage, insurance) and carry benefits CB (dividends, coupons, foreign interest); (2) compound the time-0 net cost S₀ + CC₀ − CB₀ to T at r; (3) if the market F₀ is higher, do **carry arbitrage** (sell forward, borrow, buy asset); if lower, do **reverse carry** (buy forward, short asset, lend proceeds). Profit at T equals the mispricing; PV at 0 = the forward's value to the arbitrageur.
  - Why it works / failure mode: the arbitrageur follows two rules, use none of your own money and take no price risk. It fails for non-storable/non-shortable underlyings, and when frictions, credit risk or a rate-correlated underlying exist. Expectations of S_T do **not** enter F₀.
- **Value of a forward = PV of the difference in forward prices**: V_t(long) = PV[F_t − F₀].
  - When to use: mark-to-market of a forward, FRA, bond forward or swap.
  - How: price a fresh forward F_t with the same expiry, then discount (F_t − F₀) from T to t. Equivalent check, no carry: V_t = S_t − F₀/(1+r)^(T−t). With carry, replace S_t by S_t + CC_t − CB_t.
  - Failure mode: forgetting to discount, or using S_t − F₀ (ignores financing).
- **FRA pricing by forward-rate no-arbitrage**: [1 + L_h·t_h][1 + FRA₀·t_m] = [1 + L_T·t_T].
  - When to use: fixing the rate on an X × Y FRA, or reading forward rates off a Libor/MRR curve.
  - How: pick the two spot rates that bracket the period (L_h to FRA expiry, L_T to underlying maturity), solve for FRA₀. Sanity check: the arithmetic-average approximation is slightly high.
- **Swap = pair of bonds (offsetting-portfolio method)**: a receive-fixed swap = long fixed bond + short floating bond. The floating bond is worth par on any reset date, so the swap rate is the fixed coupon that prices a bond at par: r_FIX = (1 − PVₙ)/ΣPVᵢ.
  - When to use: pricing any vanilla swap from a discount-factor curve; valuing it later.
  - How: convert each spot rate to a discount factor PVᵢ = 1/[1 + R_spot,i × NADᵢ/NTD]; sum them; apply the formula; annualize by NTD/NAD.
- **Currency swap = long bond in currency a, short bond in currency b**: swap rates are solved separately in each currency; notionals are tied by the spot rate NA_a = S₀ × NA_b.
- **Equity swap = equity notional + fixed bond**: after a reset, V = V_FIX − (S_t/S_{t−1})·NA_E − PV(Par − NA_E). The equity leg is "reset to par" on each reset date, exactly like a floating bond.

## Key Concepts
- **Forward price (F₀) vs forward value (V_t)**: price is the fixed contract term (zero-value at inception); value is the current mark, positive or negative.
- **Convergence property**: F_T = f_T = S_T at expiration. Before then the forward may be above (carry costs exceed benefits) or below spot (dividends exceed financing).
- **Basis**: futures spot price minus futures price; it converges to zero at expiry.
- **Futures value**: v_t = Nf × (f_t − f_{t−1}) intraday; zero after daily settlement, because the price is reset to the settlement price.
- **Carry benefits (CB) / carry costs (CC)**: dividends, coupons, foreign interest / storage, insurance, waste. Benefits lower F₀, costs raise it. Financing at r is already inside FV().
- **Law of one price / value additivity**: identical payoffs must trade at one price; a portfolio's value is the sum of its parts.
- **Carry vs reverse carry arbitrage**: F₀ > FV(S₀) → carry (sell forward, buy spot); F₀ < FV(S₀) → reverse carry (buy forward, short spot, lend).
- **FRA (X × Y)**: X = months until FRA expiry, Y = months until the underlying deposit matures; the reference rate has (Y − X) months. Long = pay fixed, receive floating, gains when rates rise.
- **Advanced set, advanced settled (FRA)**: rate set and cash settled at expiry h, so the payoff is discounted for the m days of the deposit: NA·(L_m − FRA₀)·t_m/(1 + D_m·t_m). Swaps and rate options are set in advance and settled in arrears.
- **Accrued interest (AI)**: AI = (NAD/NTD)(C/n), NAD = days **since** the last coupon (not until the next). Clean (quoted) price + AI = dirty (full) price.
- **Conversion factor (CF)**: scales each deliverable bond to a hypothetical 6% yield; the quoted futures price Q₀ times CF gives the adjusted price F₀ for a deliverable.
- **Cheapest-to-deliver (CTD)**: after the CF adjustment the deliverable that costs the short the least to buy.
- **Swap rate (fixed rate)**: the price of a swap; sets the fixed leg equal to the floating leg's PV so V = 0.
- **Notional principal exchange**: none in interest rate and equity swaps; at inception and maturity in currency swaps.
- **Market reference rate (MRR)**: the benchmark floating rate (Libor legacy; SOFR/SONIA successors). The formulas do not change.

## Formulas & Reference Tables
Notation: r = annual-compounded rate, r_c = continuously compounded, T = time to expiry (years), t = valuation date, NA = notional.

**Forward / futures price and value**
- `F₀ = S₀(1 + r)^T` (no carry). Continuous: `F₀ = S₀·e^(r_c·T)`.
- `F₀ = FV(S₀ + CC₀ − CB₀)` (discrete). Continuous: `F₀ = S₀·exp[(r_c + CC − CB)·T]` with CC, CB expressed as continuous rates.
- Dividend stock: `F₀ = S₀(1+r)^T − D(1+r)^(T−t_D)` where the dividend D is received at t_D.
- Payoff at expiry: long `V_T = S_T − F₀`; short `−V_T = F₀ − S_T`.
- Long forward mid-life: `V_t = (F_t − F₀)/(1+r)^(T−t)` (2a) `= S_t − F₀/(1+r)^(T−t)` (2b, no carry). Short value = −V_t.
- Value of an at-market forward when a new dividend is announced: F_t falls, so the long's V_t falls.
- Futures: `v_t = Nf(f_t − f_{t−1})`; after marking to market v_t = 0.

**Interest rate (FRA)**
- Deposit: `TA = NA[1 + L_m·t_m]`, `t_m = m/360`, ACT/360, add-on.
- FRA rate: `FRA₀ = {[1 + L_T·t_T]/[1 + L_h·t_h] − 1}/t_m`. Number of FRA rates from n spot rates = n(n−1)/2 (4 rates → 6 FRAs).
- Settlement at h: long `NA·(L_m − FRA₀)·t_m/(1 + D_m·t_m)`; short = negative of long. Usually D_m = L_m, but it may differ.
- Value at g (before expiry): long `V_g = NA·(FRA_g − FRA₀)·t_m/[1 + D_{T−g}·t_{T−g}]`, where FRA_g comes from the same formula with the **remaining** days: h − g and T − g. Short = −V_g.

**Fixed-income forward/futures**
- `S₀ = B₀ + AI₀`; `F₀ = Q₀ × CF = FV[B₀ + AI₀ − PV_CI] = FV(S₀) − AI_T − FV_CI`.
- `Q₀ = (1/CF)·{FV[B₀ + AI₀] − AI_T − FV_CI}`. Note that AI at expiry is subtracted; coupons in the window are removed at future value.
- Bond forward value: `V_t = PV[F_t − F₀]`, times par × number of contracts (prices are in % of par).

**Swaps**
- Discount factor: `PVᵢ = 1/[1 + R_spot,i·(NADᵢ/NTD)]`.
- Fixed bond value: `V_FIX = C·ΣPVᵢ + PVₙ` (par = 1). Swap value (receive fixed): `V_swap = V_FIX − V_FLT`. V_FLT = 1 on reset dates.
- Swap rate: `r_FIX = (1 − PVₙ)/ΣPVᵢ` (per period). Annualize: × NTD/NAD. Fixed payment: `FS = NA × AP × r_FIX`.
- Net periodic flow: pay-fixed receives `NA·AP·(r_FLT − r_FIX)`.
- Value at t (payment date), receive-fixed: `V = NA·Σ(FS₀ − FS_t)·PVᵢ = NA·AP·(r_FIX,0 − r_FIX,t)·ΣPVᵢ`, ΣPVᵢ over the remaining n payments. Pay-fixed value = −V. Here r_FIX,t is the **current market swap rate for the remaining tenor**.
- Currency swap: `NA_a = S₀·NA_b` (S₀ in units of a per 1 b); `r_a = (1 − PVₙ,a)/ΣPV_a`, `r_b = (1 − PVₙ,b)/ΣPV_b`; value to the receiver of currency a in units of a: `V_CS = NA_a[r_a·ΣPV_a + PVₙ,a] − S_t·NA_b[r_b·ΣPV_b + PVₙ,b]` with periodic rates, current PV factors and current spot S_t. The counterparty's value is −V_CS.
- Equity swap: cash flow (receive equity, pay fixed) `NA_E(R_E − r_FIX·AP)`; price `r_FIX = (1 − PVₙ)/ΣPVᵢ` (same as the interest rate swap); mid-life `V_EQ,t = V_FIX(C₀) − (S_t/S_{t−1})NA_E − PV(Par − NA_E)` (receive-fixed, pay-equity). Break-even equity level: S_t = 100 × V_FIX/NA_E (if S_{t−1} = 100).

| Position | Gains when | Replicating portfolio | Value formula sign |
|---|---|---|---|
| Long forward | S / F_t rises | Long asset, borrowed funds | PV(F_t − F₀) |
| Long FRA (pay fixed) | rates rise | Long long-dated, short short-dated deposit | PV(FRA_g − FRA₀) |
| Pay-fixed swap | rates rise | Long floating bond, short fixed bond | NA(FS_t − FS₀)ΣPV |
| Receive-fixed swap | rates fall | Long fixed bond, short floating bond | NA(FS₀ − FS_t)ΣPV |
| Receive-equity, pay-fixed | equity rises, rates rise | Long equity, short fixed bond | (S_t/S_{t−1})NA_E − V_FIX |

## Mental Models
- **The forward is a loan in disguise**: F₀ is what you would owe if you bought spot with borrowed money. Carry benefits reduce the debt, carry costs increase it.
- **Price is a promise, value is a mark**: at inception V = 0 for both sides. Afterwards only the *difference* between new and old forward prices matters, discounted.
- **Swap = bonds**: to price, force a par bond; to value, reprice the remaining fixed leg against today's swap rate. Floating legs always reset to par.
- **Current rate is a fresh swap**: value = PV of (old fixed − new fixed) × ΣPV. The annuity ΣPV is the value of 1 per period (PV01 per bp × 10,000).
- **Currency swap risk has two sources**: interest rates in each currency and the spot rate; FX moves shift the value of the foreign bond leg one-for-one.
- **Equity swap resets like a floating leg**: equity leg value between resets = (S_t/S_{t−1}) × notional; just after a reset it is exactly notional.

## Worked Example
**A. Equity forward with a dividend (recomputed).** S₀ = 1,000, r = 5% annual, 3-month forward, a dividend of 10 is paid in 2 months.
- F₀ = 1,000(1.05)^0.25 − 10(1.05)^(1/12) = 1,012.2722 − 10.0407 = **1,002.23**. Dividend paid in month 1 instead: 1,012.2722 − 10(1.05)^(2/12) = 1,002.19 (lower, because the dividend earns more interest).

**B. Interest rate swap pricing and valuation.** Discount factors 0.990099, 0.977876, 0.965136, 0.951529, 0.937467 (annual, 30/360); ΣPV = 4.822107.
- r_FIX = (1 − 0.937467)/4.822107 = **1.2968%**.
- Two years after entering a 7-year €100m receive-fixed swap at 2.0%, five payments remain and the market rate is about 1.30%: V = 100m × (0.020 − 0.013) × 4.822107 = **+€3.375m** to the receiver (−€3.375m to the payer). With the unrounded 1.2968%, V = €3.391m; the exam answer uses the rounded 1.3%.

**C. Currency swap (Example 15/16, with the L2 errata).** A$100m vs US$87.719m at A$1.14/US$; 1 year, quarterly.
- Rates: A$ periodic (1 − 0.972763)/3.933870 = 0.692381% (2.7695% annual); US$ periodic (1 − 0.997506)/3.995009 = 0.062422% (0.2497% annual). Quarterly payments about A$692,375 and US$54,759.
- After 60 days: S_t = A$1.13/US$, new ΣPV: A$ 3.967683 (PV_n 0.986031), US$ 3.994841 (PV_n 0.998336).
- V_CS (receiver of A$, the dealer) = 100m[0.00692375 × 3.967683 + 0.986031] − 1.13 × 87,719,298 × [0.00062425 × 3.994841 + 0.998336] = **A$2,145,167** (recomputed 2,145,167; the pre-erratum figure was 2,145,203, and unrounded rates give 2,145,213). The US firm's value = −A$2,145,167 ÷ 1.13 = **−US$1,898,378**.
- Interpretation: the A$ strengthened and A$ rates fell, so the A$ payer's liability grew.

**D. Equity swap.** Receive-fixed 1.5%, pay-equity, notional 10m, 5 annual resets, first reset not yet reached, flat 1.2% curve, S₀ = 100, S_t = 105.
- PV factors 1/(1 + 0.012t) at t = 0.5, 1.5, 2.5, 3.5, 4.5 → V_FIX = 10,216,019.
- V_EQ = 10,216,019 − 1.05 × 10,000,000 = **−283,981**. Break-even equity level = 102.16.

## Anti-patterns
- **Adding expected growth or a risk premium to F₀**: forward prices reflect carry, not forecasts.
- **Using S_t − F₀ for forward value**: omits financing; use S_t − PV(F₀).
- **Compounding dividends to the wrong date**: the dividend compounds only from its payment date to T; the stock compounds over the full T.
- **Using days until the next coupon for accrued interest**: use days *since* the last coupon.
- **Forgetting to subtract AI_T in bond futures**: futures settle on the clean price.
- **Not discounting the FRA settlement** by 1 + D·t_m.
- **Valuing a swap with the original PV factors/annuity or original tenor**: use today's curve and the remaining payments; annuity ΣPV is over the remaining n only.
- **Mixing units in equity swaps**: the equity return is per period; the fixed rate is quoted annually (× AP).
- **Applying the swap valuation formulas between payment dates without adjusting**: the reading covers valuation on payment dates only.

## Exam Focus & Traps
- **Sign of the FRA**: long FRA = pay fixed/receive floating = profits when rates rise. Settlement is at h, discounted at D_m.
- **Which formula when**: price a forward → FV(S + CC − CB); value it → PV(F_t − F₀). Futures value after settlement = 0.
- **FRA X × Y**: rate spans (Y − X) months; you need L_X and L_Y. Number of FRAs from four spots is 6.
- **CF-adjusted price**: Q₀ = (F₀ + …)/CF; F₀ = Q₀ × CF. Distractors: dropping AI_T, dropping the exponent T (Q17 wrong answers 148.89 and 149.78).
- **Carry arbitrage direction**: forward too high → sell the forward, buy the asset. Practice Q1: overpriced by 0.5360, arbitrage profit is PV = 0.5356.
- **Swap value sign**: receive-fixed gains when swap rates fall; pay-fixed loses (Q20: −JPY2,980,500 for a payer after rates fell below 0.10%).
- **Swap-rate slip**: numerator uses the *last* PV factor; denominator sums all n (dropping the last gives 0.72% instead of 0.55% in Q19).
- **Currency swap**: check which currency is "a" (the numerator of the quote). The value for the receiver of a is V_CS; the other party's is −V_CS, converted at S_t.
- **Equity swap**: the equity leg is at S_t/S_{t−1} × NA_E, not S_t/S₀, once a reset has passed; before the first reset S_{t−1} = S₀.
- **Continuous compounding** requires exp with r_c, CB and CC as continuous rates (Nikkei example: 16,047.86).
- **Rounding**: the reading rounds intermediate rates; choose the closest answer.

## Key Takeaways
1. F₀ = FV(S₀ + CC₀ − CB₀); forward prices never depend on your view of S_T.
2. Value = PV of (new forward price − old forward price); at expiry a forward is S_T − F₀; a futures contract is worth zero after marking to market.
3. An FRA rate is a forward rate from two spot rates; settlement is advanced and discounted; long FRA = pay fixed.
4. Bond futures: F₀ = FV(B₀ + AI₀) − AI_T − FV_CI; quoted Q₀ = F₀/CF.
5. Swap rate = (1 − PVₙ)/ΣPVᵢ; the value of an existing swap = NA × Δ(fixed rate) × remaining annuity.
6. Currency swaps: tie notionals by S₀, solve each currency's rate separately, value with current curves and spot.
7. Equity swap prices like a fixed-for-floating interest rate swap; mid-life value swaps the floating bond for the equity value scaled by S_t/S_{t−1}.
8. Assumptions (no frictions, full short-sale proceeds, known r) are the limits of the whole framework.

## Connects To
- **ch01**: definitions of forwards, futures, swaps and margin that this chapter prices.
- **ch02**: the basic no-arbitrage/replication idea and forward pricing intuition; this chapter adds numerical carry models, FRAs and swap valuation.
- **ch04**: options on the same underlyings; forward-based inputs (put–call–forward parity) feed the option models.
- **ch06**: L3 use of swaps, forwards and futures in strategies, where these valuations are the inputs (duration, notional adjustments).
- **`cfa-fixed-income`** (yield curves, spot/forward rates): spot-to-discount-factor and forward-rate mechanics behind FRAs and swaps.
- **`hull-derivatives`**: continuous-compounding treatment, FRA valuation, day-count details.
