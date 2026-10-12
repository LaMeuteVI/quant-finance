# Patterns — CFA Fixed Income (L1 2020, L2 2022, L3 2023)

Calculation recipes and procedures. `(ch NN)` = chapter.

## Price a bond between coupon dates
**When to use**: any trade settled off a coupon date.
**How**: (1) t = days since last coupon, T = days in period (day-count: act/act government, 30/360 corporate); (2) PV on the last coupon date with N remaining periods, r = YTM/m; (3) full = PV × (1+r)^(t/T); (4) AI = (t/T) × PMT; (5) flat = full − AI.
**Trade-offs**: AI ignores time value, so flat is slightly below par at YTM = coupon. (ch 03)

## Back out YTM, spot-rate value and Z-spread
**When to use**: relative value, arbitrage checks, spread decomposition.
**How**: YTM = IRR of flows (N = years × m). No-arbitrage value = Σ CF/(1+z_k)^k. Z-spread = constant Z solving Σ CF/(1+z_k+Z)^k = price. G-spread uses interpolated government YTM, I-spread interpolated swap rate.
**Trade-offs**: YTM can hide very different spot curves; Z-spread is option-free only. (ch 03, ch 15)

## Convert money-market quotes to a common basis
**When to use**: comparing T-bills, CP, CDs, time deposits.
**How**: discount-rate paper: P = 100(1 − DR × days/360); add-on rate AOR = (365/days) × (FV − P)/P (BEY). 360-day add-on × 365/360 = BEY. Periodicity: `APR_n = n[(1+APR_m/m)^(m/n) − 1]`.
**Trade-offs**: never compare a discount rate with an add-on rate. (ch 02, ch 03)

## Spots, forwards, par rates and swap rates
**When to use**: extract the market's implied path; bootstrap; build swap curve.
**How**: forward `(1+z_B)^B = (1+z_A)^A (1+f)^(B−A)`. Bootstrap from shortest par maturity: z₁ = par₁, then solve 1 = Σ par_N/(1+z_t)^t + (1+par_N)/(1+z_N)^N. Swap rate s_T = (1 − DF_T)/Σ DF_t. Upward curve: forward > spot > par.
**Trade-offs**: forwards cannot extend beyond the longest spot; breakeven = forward. (ch 03, ch 07)

## Rolldown versus matched-maturity horizon return
**When to use**: static, upward-sloping curve; horizon H.
**How**: buy maturity > H; at H reprice the remaining maturity at today's yield for that tenor; total = coupons + reinvestment + price at H. Compare with the maturity-matched bond. Decision vs views: if forecast yield < implied forward, the bond beats the one-period rate (excess ≈ −Dur_horizon × (forecast − forward)).
**Trade-offs**: a duration bet; fails if the curve rises to or above the forwards. (ch 07, ch 14)

## Duration, convexity and price change
**When to use**: option-free rate sensitivity.
**How**: ModDur = MacDur/(1+r); %ΔP ≈ −ModDur·Δy + ½·Con·Δy². Approx duration (PV₋ − PV₊)/(2·Δy·PV₀); approx convexity (PV₋ + PV₊ − 2PV₀)/(Δy²·PV₀). PVBP = (PV₋ − PV₊)/2 at ±1bp. Annualize duration ÷ m, convexity ÷ m². Spread move: ΔSpread ≈ −%ΔP/ModDur.
**Trade-offs**: full price; invalid for rate-contingent cash flows. (ch 05)

## Horizon-yield and duration-gap analysis
**When to use**: judging whether rates up or down hurt a holding period.
**How**: carrying value = price on constant-yield trajectory; capital gain = sale − carrying value; reinvest coupons at the new rate; gap = MacDur − horizon. Gap > 0 fears higher rates; gap < 0 fears lower; 0 = immunized against a one-time parallel shift.
**Trade-offs**: gap decays with time, so rebalance. (ch 05)

## Effective duration and convexity of an optioned bond
**When to use**: callables, putables, MBS, floaters, liabilities.
**How**: solve OAS at the market price on a calibrated tree; shift the benchmark par curve ±Δ, rebuild the tree, reprice at the same OAS → PV₋, PV₊; EffDur = (PV₋ − PV₊)/(2Δ·PV₀); EffCon = (PV₋ + PV₊ − 2PV₀)/(Δ²·PV₀). Report one-sided durations near the money.
**Trade-offs**: vendor convexity often ÷100; results depend on σ. (ch 05, ch 09)

## Calibrate a binomial interest rate tree
**When to use**: before valuing any bond with embedded options.
**How**: (1) bootstrap spots from par curve; (2) i₀ = 1-year rate; (3) per date set adjacent nodes ratio e^{2σ}; solve the lowest node so the next par bond prices at 100; repeat date by date; (4) check an option-free bond equals its spot value and does not move with σ.
**Trade-offs**: σ drives option value only; lognormal forbids negative rates. (ch 08)

## Value a callable or putable bond on the tree
**When to use**: option value, OAS, relative value.
**How**: backward induction V = [C + ½(V_H + V_L)]/(1+i); at call dates reset V to min(V, call price), at put dates to max(V, put price), testing ex-coupon; callable = straight − call, putable = straight + put; option value = difference of prices. Zero-vol check uses forward-rate discounting.
**Trade-offs**: callable falls and putable rises with σ; OAS of a callable shrinks as σ rises. (ch 09)

## OAS relative-value screen
**When to use**: comparing bonds across structures.
**How**: iterate constant spread on every tree rate until model = market price; compare with similar credit and structure at the same σ; lower OAS = rich, higher = cheap. Z-spread − option cost = OAS.
**Trade-offs**: never compare OAS across volatility assumptions. (ch 09, ch 15)

## Convertible bond metrics
**When to use**: classifying and pricing a convertible.
**How**: conversion value = share × ratio; minimum value = max(conversion value, straight value); market conversion price = bond price/ratio; premium per share = that − share price; busted / hybrid / equity-like by share price versus conversion price.
**Trade-offs**: floor moves with rates and spreads. (ch 01, ch 09)

## Prepayment projection (pass-through)
**When to use**: monthly MBS cash flows, average life.
**How**: CPR(t) = 6% × min(t,30)/30 × (PSA/100); SMM = 1 − (1 − CPR)^(1/12); payment = B·i/(1 − (1+i)^−n) at WAC/12; sched. principal = payment − B·WAC/12; prepay = SMM × (B − sched.); investor CF = B·(pass-through/12) + principal + prepay.
**Trade-offs**: sequential tranches protect one side; PAC both inside the collar, paid for by support. (ch 04)

## Loss allocation in a securitization
**When to use**: tranche risk, credit enhancement.
**How**: losses absorbed by excess spread, then OC/reserve, then the most junior tranche upward; tranche loss = min(par, max(0, total loss − enhancement below)); attachment point = all below it.
**Trade-offs**: credit tranching redistributes, never reduces, pool risk. (ch 04)

## Expected loss and credit price impact
**When to use**: comparing credits; spread P&L.
**How**: EL = PD × (1 − RR); price impact ≈ −MDur·ΔSpread + ½·Cvx·ΔSpread² (rescale convexity); migration drag = −ModDur_end × Σ p_i·Δs_i.
**Trade-offs**: ratings capture PD, not LGD. (ch 06, ch 10)

## Credit ratios and leverage by debt layer
**When to use**: single-name corporate credit.
**How**: EBITDA = op income + D&A; Debt/EBITDA, Debt/Capital, FFO/Debt, FCF-after-dividends/Debt, EBITDA/Interest, EBIT/Interest; leverage at each attachment (secured, through second lien, total, net); EV = market cap + debt − excess cash.
**Trade-offs**: levels, trends and peer comparison; adjust for pensions and leases. (ch 06)

## CVA table: fair value of a risky bond
**When to use**: price a credit, imply hazard, split spread.
**How**: VND on calibrated tree; per date: exposure (node-weighted value + coupon), LGD = EE(1 − RR), POD_t = h·POS_{t−1}, PV = LGD × POD × DF; CVA = Σ; fair value = VND − CVA; YTM on fair value minus benchmark = spread. Rule: spread ≈ h × (1 − RR). Floater: coupon uses prior-date probabilities; DM added to discount only.
**Trade-offs**: risk-neutral PODs exceed historical; POD and RR jointly identified by price only. (ch 10)

## Price a CDS and its upfront
**When to use**: new or existing CDS, mark-to-market.
**How**: protection leg = N(1−RR)Σ h·POS_{t−1}·DF_t; premium leg = C·N·RPV01, RPV01 = Σ POS_t·DF_t; upfront = prot − prem = (s − C)·RPV01·N ≈ (s − C) × duration; price = 100 − upfront; P&L ≈ Δs × duration × notional. Cumulative POD = 1 − Π(1 − h_t).
**Trade-offs**: linear rule overstates large widenings; spread > coupon: buyer pays. (ch 11)

## CDS trade constructions
**When to use**: expressing credit views.
**How**: slowdown = buy HY protection, sell IG; steepener = buy long-dated, sell short-dated protection sized BPV-matched (N_short = N_long × Dur_long/Dur_short); negative basis = buy bond + buy protection + hedge rates; LBO = long stock + buy protection.
**Trade-offs**: basis and counterparty risk, upfront coupons, CTD recovery. (ch 11, ch 15)

## Fixed-income expected return decomposition
**When to use**: ex-ante strategy evaluation.
**How**: E(R) ≈ coupon/price + rolldown (unchanged-curve price at horizon) − ModDur·Δy + ½Con·Δy² − Dur·ΔSpread + ½Con·ΔSpread² + currency (1+R_FC)(1+R_FX) − 1; rolling yield = carry; the rest are views.
**Trade-offs**: duration/convexity only, no financing or tax effects. (ch 12, ch 14, ch 15)

## Leverage and financing
**When to use**: sizing leveraged bond exposure.
**How**: r_P = r_I + (V_B/V_E)(r_I − r_B); futures leverage = (notional − margin)/margin; repo interest = loan × rate × days/360, loan = collateral × (1 − haircut); effective duration ≈ (Notional/Equity) × Dur_assets.
**Trade-offs**: margin calls and funding withdrawal make losses forced. (ch 02, ch 12, ch 14)

## Single-liability immunization
**When to use**: one known liability.
**How**: MV ≥ PV(L); portfolio MacDur = horizon (at the cash flow yield); minimize dispersion/convexity: Convexity = (MacDur² + MacDur + Dispersion)/(1+CFY)²; rebalance as duration drifts.
**Trade-offs**: twists and barbells break it; use aggregate cash flows, not averages. (ch 13)

## Multiple-liability match and overlay sizing
**When to use**: DB plan, insurer.
**How**: BPV_A = BPV_L, convexity_A > convexity_L (minimized). Futures N_f = (BPV_L − BPV_A)/(BPV_CTD/CF); swaps NP = (BPV_L − BPV_A)/(SwapBPV/100). Cash flow matching: start with the last liability, par = need/(1+c) rounded up. Pension: ABO, PBO from ±1% reprice; hedge ratio 0–100%.
**Trade-offs**: CTD error shifts the hedge; collateral drain; swaps over futures for margin. (ch 13)

## Pick a pension overlay by rate view
**When to use**: choosing swap, collar or receiver swaption.
**How**: rates ≤ swap rate → receive-fixed swap; moderately higher → zero-cost collar (long receiver, short payer); well above upper strike → long receiver swaption.
**Trade-offs**: collar loses above the payer strike. (ch 13)

## Add duration or curve exposure sized on PVBP
**When to use**: tactical rate or slope views.
**How**: ΔPVBP = (target Dur − current Dur) × MV/10,000; futures N = ΔPVBP/PVBP_fut; swaps notional = ΔPVBP/net PVBP per unit; steepener long short-end/short long-end BPV-matched; butterfly 2·mid − short − long; barbell w = (D_long − D_body)/(D_long − D_short); map active KRDs to swaps/futures.
**Trade-offs**: convexity costs yield and pays only on large moves (break-even ≈ ±25bp in the example). (ch 07, ch 14)

## Bond index replication
**When to use**: passive mandates.
**How**: stratify into cells; match duration, key rate durations, sector/quality spread duration, callable cell weights and issuer duration contributions; choose benchmark by liability duration.
**Trade-offs**: full replication impractical; ETFs trade at premium/discount to NAV. (ch 13)

## Spread-view return screen
**When to use**: choosing among credits.
**How**: E[excess] ≈ Spread₀ − EffSpreadDur × ΔSpread − POD × LGD; DTS = SpreadDur × Spread, spread move ΔP/P ≈ −DTS × (ΔSpread/Spread); VaR parametric σ_Y × z × √t with z = 1.65/2.33.
**Trade-offs**: assumes spreads and rates independent. (ch 15)
