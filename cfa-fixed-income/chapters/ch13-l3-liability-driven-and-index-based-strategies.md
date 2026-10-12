# Chapter 13: Liability-Driven and Index-Based Strategies
> **Source**: CFA Program Curriculum 2023, Level III, Reading 12 · Fixed-Income Portfolio Management | James F. Adams, PhD, CFA, and Donald J. Smith, PhD

## Core Idea
"Passive" fixed income is not buy-and-hold. **Immunization** hedges a known liability by replicating a zero-coupon bond: match the Macaulay duration (one liability) or the money duration/BPV (several liabilities), fund at least the PV of the liabilities, and control dispersion/convexity against yield-curve twists. The same money-duration arithmetic sizes the futures and swap overlays that close a pension plan's duration gap. **Index-based** investing faces a different problem: bond indexes are too large and illiquid to replicate fully, so managers match the index's primary risk factors (enhanced indexing) and choose a benchmark whose duration fits the investor's liabilities.

## Learning Outcomes Covered
- Describe LDI vs asset-driven liabilities (ADL), and classify liabilities as Types I–IV.
- Evaluate single-liability immunization: duration match, cash flow yield, dispersion, convexity, structural risk, rebalancing.
- Compare multiple-liability strategies: cash flow matching, duration matching, derivatives overlay, contingent immunization.
- Describe laddered portfolios (construction, benefits, limitations) against bullets and barbells.
- Evaluate liability strategies under rate scenarios. Size futures and swap hedges. Choose among swap, receiver swaption and swaption collar.
- Explain the risks of LDI: model, spread, counterparty, collateral and asset liquidity risk.
- Discuss the challenges of bond indexing, the primary risk factors, full replication vs enhanced indexing vs ETFs, mutual funds and TRS.
- Select and justify a fixed-income benchmark.

## Frameworks Introduced
- **Asset–liability management (ALM): LDI vs ADL**
  - **LDI**: the liabilities are given and the assets are managed against them (insurers, DB plans, a retiree's budget). This is far more common.
  - **ADL**: the assets are given (they come from the business) and the liability structure is chosen. Examples: a leasing firm funds itself short to match short leases. A cyclical manufacturer prefers floating-rate debt, because central banks cut rates when revenue is weak.
- **Liability classification (Exhibit 1)**:

| Type | Amount | Timing | Examples | Rate-sensitivity measure |
|---|---|---|---|---|
| I | Known | Known | Option-free bond | MacDur, ModDur, money duration, PVBP |
| II | Known | Uncertain | Callable/putable bond, term life policy, deposits redeemable early | Effective duration (model) |
| III | Uncertain | Known | FRN, inflation-linked bond | Effective duration (model) |
| IV | Uncertain | Uncertain | P&C insurance, DB pension, prepayable mortgages, CoCos | Effective duration (model) |

- **Single-liability immunization (three conditions)**:
  1. Initial market value of assets ≥ PV of the liability.
  2. Portfolio **Macaulay duration = investment horizon**.
  3. **Minimize portfolio convexity** (equivalently dispersion) to limit structural risk.
  - How it works: at the Macaulay duration date, the price effect and the coupon-reinvestment effect of a one-time rate shift offset. Immunization is really **zero replication**. You manage coupon bonds so that they track a (possibly hypothetical) zero maturing on the liability date, and you **rebalance** because duration does not decline one-for-one with calendar time.
  - The target return is the portfolio **cash flow yield** (the IRR of the aggregate cash flows), *not* the market-value-weighted average YTM. With an upward-sloping curve the cash flow yield is higher than the average YTM, and the true portfolio duration and convexity are higher than their weighted averages.
  - Failure mode: immunization holds when Δ(cash flow yield of the portfolio) = Δ(YTM of the replicated zero). A **parallel shift is sufficient but not necessary**. Some steepeners and flatteners also work. **Twists** (a steepening pivot at the horizon, or a butterfly) break it, and a barbell is hit hardest.
- **Multiple-liability immunization via duration matching (three conditions)**:
  1. MV(assets) ≥ MV(liabilities).
  2. **BPV(assets) = BPV(liabilities)**. Match *money* duration, because the market values and cash flow yields of assets and liabilities differ.
  3. **Dispersion and convexity of the assets > those of the liabilities**, but as low as possible subject to that constraint. The first-order condition of the optimization gives equal BPV. The second-order condition gives higher dispersion.
- **Menu of multiple-liability approaches**:

| Approach | Mechanics | Pros | Cons / risks |
|---|---|---|---|
| **Cash flow matching** (dedication) | Hold-to-maturity portfolio of high-quality bonds whose coupons and principal cover each outflow. Build it from the **last liability backward**, deducting the coupons of longer bonds. | No duration rebalancing. Can support **accounting (in-substance) defeasance**, removing both assets and debt from the balance sheet. Buying back illiquid debt is costly. | **Cash-in-advance constraint** (funds must be there on or before each date). Idle cash is exposed to reinvestment risk, which is bad for level-annuity liabilities. Expensive (government bonds). |
| **Duration matching** | Match BPV, with asset convexity > liability convexity. Rebalance by trading bonds or derivatives. | Cheaper (can use IG corporates). Flexible. | Structural (twist) risk, rebalancing costs, spread risk. Usually no accounting defeasance ("effective defeasance" only). |
| **Derivatives overlay** | Keep the chosen asset portfolio (e.g., short, liquid bonds) and add futures or swaps to hit the liability BPV. | Cheap, fast rebalancing. Leaves the cash portfolio intact (regulatory liquidity). | CTD and futures-BPV model risk, Treasury–corporate spread risk, margin and collateral risk. |
| **Contingent immunization** | Manage actively while the **surplus** (MV assets − PV liabilities) stays above a threshold. If it falls to the trigger, revert to passive immunization. | Can lower the cost of retiring the liabilities. | Needs a sizeable surplus. **Asset liquidity risk** when positions must be unwound near the trigger. |

- **Laddered portfolio**: roughly equal par amounts spread across maturities. Compared with a bullet and a barbell of equal duration:
  - Convexity: barbell > ladder > bullet.
  - Reinvestment risk: the ladder has much less than the barbell.
  - Benefits: diversification over time (a dollar-cost-averaging analogy between reinvestment and price risk); maturing rungs rolled to the back of the ladder, usually at higher yields; duration maintained automatically; **liquidity**, because a soon-to-mature, low-duration bond is always available as cash or repo collateral.
  - Can be built with **fixed-maturity (target-date) corporate bond ETFs**, which are more liquid than the bonds themselves.
  - Limitations: a bond mutual fund gives more default diversification, lower acquisition cost and faster liquidation than a small ladder of corporates.
  - Works best in a stable, upward-sloping curve.
- **DB pension LDI workflow**:
  1. Model the liabilities (ABO or PBO).
  2. Compute their effective duration by shifting r (and w) up and down.
  3. Compute the asset BPV, typically giving equity and alternatives zero duration.
  4. Measure the **duration gap**.
  5. Choose a **hedging ratio** (0% = unhedged, 100% = immunized; partial hedges are the norm).
  6. Choose the instrument: futures, a receive-fixed swap, a receiver swaption or a swaption collar.
  - **Strategic hedging** moves the ratio within a permitted band (e.g., 25–75%) based on the rate view. Performance is measured against a fixed-ratio benchmark (e.g., 50%).
- **Choosing the overlay by rate view (Exhibit 26, swap rate 4.16%, receiver strike 3.50%, payer strike 5.00%)**:
  - Expect rates ≤ the swap rate (4.16%) → **receive-fixed swap**. It has the largest gains when rates fall and zero premium, but it loses immediately above 4.16%.
  - Expect rates moderately higher → **zero-cost swaption collar** (long receiver at 3.50%, short payer at 5.00%). There is no loss between the strikes, and losses start above 5.00%.
  - Expect rates well above the upper strike → **long receiver swaption**. The loss is capped at the premium. Breakeven vs the collar is the rate at which the loss on the written payer exceeds the premium (≈5.07% in the example).
- **Primary indexing risk factors (Volpert)**, matched to minimize tracking error:
  1. **Portfolio modified adjusted (option-adjusted/effective) duration**, plus convexity for large moves.
  2. **Key rate durations** (non-parallel shifts).
  3. **Percent in sector and quality** (matches index yield).
  4. **Sector and quality spread duration contribution**.
  5. **Sector/coupon/maturity cell weights of callables** (critical for MBS refinancing).
  6. **Issuer exposure** (event risk), measured by duration contribution, not market-value weight.
  - Alternative: the **present value of distribution of cash flows** method. Bucket the index cash flows into semiannual vertices (callables weighted by call probability), compute each vertex's share of PV, sum time × share = index duration, then match the PV share at each vertex.
- **Passive implementation spectrum**:
  - **Pure indexing / full replication**: minimal tracking error, but impractical for broad indexes (monthly rebalancing, thousands of illiquid bonds).
  - **Enhanced indexing / stratified sampling (cell approach)**: match cells and risk factors with fewer bonds. This also suits ESG screens (business-involvement exclusions plus a minimum ESG rating).
  - **Active**: deliberate factor deviations.
  - **Enhancements** that offset costs: lower costs, issue selection, yield-curve positioning, sector/quality tilts, call exposure positioning.
- **Benchmark selection**:
  - Requirements: clear and transparent rules, investability, daily valuation, available return history, turnover.
  - Bond-specific problems: (1) duration drifts down as bonds age; (2) composition follows issuers (for example, the US Agg securitized share rose to 43.7% in 2008, and governments rose after the crisis).
  - Choose on the desired **duration profile** (the portfolio's "beta") and risk appetite. Blend sub-benchmarks when needs differ (short claims + long obligations). **Smart beta** offers rules-based factor capture at lower fees.

## Key Concepts
- **Immunization**: structuring and managing a bond portfolio to minimize the variance of the realized return over a known horizon.
- **Cash flow yield**: the IRR on the portfolio's aggregate cash flows. It is the rate that immunization locks in.
- **Dispersion**: the PV-weighted variance of cash-flow times around Macaulay duration. It measures how spread out the payments are.
- **Structural risk**: the risk that twists or non-parallel shifts move the portfolio's cash flow yield differently from the replicated zero's yield. It is minimized by minimizing dispersion (bullet toward the horizon).
- **Money duration / BPV**: money duration = ModDur × market value, and BPV = money duration × 0.0001 (also called PVBP, PV01, DV01).
- **Accounting (in-substance) defeasance**: extinguishing debt for accounting purposes by dedicating high-quality securities that cover it.
- **Cash-in-advance constraint**: in cash flow matching, funds must be available on or before each liability date. Securities are not sold to pay them.
- **Surplus**: MV(assets) − PV(liabilities). It is the cushion that permits contingent immunization.
- **ABO (accumulated benefit obligation)**: PV of benefits based on *current* wage and years worked. It is the legal liability if the plan were closed.
- **PBO (projected benefit obligation)**: PV of benefits based on the *projected final* wage. It is the reported liability used for funded status.
- **Longevity risk**: retirees live longer than modeled, so liabilities rise.
- **Hedging ratio**: the share of the liability BPV gap closed with derivatives.
- **Receiver swaption / payer swaption**: the right to enter a swap receiving fixed / paying fixed.
- **Swaption collar**: long receiver + short payer swaption, usually structured at zero cost.
- **CSA (Credit Support Annex)**: the ISDA collateral terms (zero or positive threshold, one-way or two-way, independent amount, minimum transfer amount).
- **Tracking error**: the standard deviation of active return (portfolio − benchmark). With normal returns, about two-thirds of periods fall within ±1 TE.
- **Matrix (evaluated) pricing**: estimating an illiquid bond's yield from benchmark yields plus spreads of comparable bonds. It is a source of index-vs-portfolio deviation.
- **Total return swap (TRS)**: the receiver gets the index total return and pays MRR + spread. It exposes the investor to counterparty risk.

## Formulas & Reference Tables
- **Portfolio Macaulay duration**: `MacDur = Σ tᵢ·wᵢ`, with `wᵢ = PV(CFᵢ)/ΣPV`, discounted at the cash flow yield per period. Annualize by dividing by the periodicity (2).
- **Dispersion**: `Dispersion = Σ (tᵢ − MacDur)²·wᵢ`. Annualize by dividing by periodicity² (4).
- **Convexity**: `Convexity = Σ tᵢ(tᵢ+1)·wᵢ / (1+y)²`, with y = cash flow yield per period. Annualize by dividing by 4.
- **Immunized portfolio convexity (Eq. 1)**: `Convexity = (MacDur² + MacDur + Dispersion)/(1 + CFY)²`. All inputs are in periods, and CFY is per period. With MacDur and CFY fixed, convexity rises one-for-one with dispersion.
- **Money duration**: `MoneyDur = [MacDur/(1 + CFY/m)] × MV`. **BPV** = MoneyDur × 0.0001.
- **Hedge identity (Eq. 7)**: `Asset BPV·ΔyA + Hedge BPV·ΔyH ≈ Liability BPV·ΔyL`. Convexity is ignored. The equation implicitly assumes ΔyA = ΔyH = ΔyL, which is where the risk sits.
- **Futures overlay (Eq. 2–3)**: `Asset BPV + Nf × Futures BPV = Liability BPV`, so `Nf = (Liability BPV − Asset BPV)/Futures BPV`. Nf > 0 → buy futures. Nf < 0 → sell futures.
- **Futures BPV (Eq. 4)**: `Futures BPV ≈ BPV_CTD / CF_CTD`, where CF = conversion factor.
- **Swap overlay (Eq. 6)**: `Asset BPV + NP × (Swap BPV/100) = Liability BPV`, where Swap BPV is quoted per 100 of notional. A receive-fixed swap = long fixed bond + short FRN, so it has *positive* duration. The payer (dealer side) has negative duration.
- **Effective duration (Eq. 5)**: `EffDur = (PV₋ − PV₊)/(2 × ΔCurve × PV₀)`.
- **ABO**: `ABO = [m·G·W₀/(1+r)ᵀ] × [1/r − 1/(r(1+r)ᶻ)]`.
- **PBO**: `PBO = [m·G·W₀·(1+w)ᵀ/(1+r)ᵀ] × [1/r − 1/(r(1+r)ᶻ)]`.
  - Variables: m = benefit multiplier, G = years already worked, T = years to retirement, Z = years in retirement, W₀ = current wage, w = wage growth, r = high-quality corporate discount rate (flat curve).
  - PBO = ABO × (1+w)ᵀ, so PBO > ABO when w > 0.
  - A higher Z raises both. A higher T lowers ABO, and lowers PBO when w < r.
- **Futures P&L**: 10-year T-note futures are quoted in 32nds. 1/32 = USD 31.25 per USD 100,000 contract.
- **Swap mark-to-market for a rate move**: `PV = Σₜ₌₁ⁿ [(K − S)/2 × NP]/(1 + S/2)ᵗ`, where K = contract fixed rate, S = new market swap rate, n = 2 × years.
- **Tracking error**: `TE = σ(R_P − R_B)`.

## Mental Models
- **Immunization = synthetic zero-coupon bond.** Ask "does my portfolio's cash flow yield move one-for-one with the zero's yield?" rather than "is the shift parallel?"
- **Single liability: minimize convexity. Multiple liabilities: exceed the liabilities' convexity, then minimize.** The two rules look contradictory but are consistent. The benchmark in the first case is a zero (dispersion 0). In the second it is a liability stream with its own dispersion.
- **Match money, not percentages.** When MVs differ, equal modified durations still leave a BPV gap. Always size hedges on BPV.
- **The CTD is the futures contract's duration.** With yields below the 6% notional coupon, the CTD is the shortest-duration eligible note. The "10-year" contract behaved like a ~6.5-year one, which is why the Ultra 10-year exists. Getting the CTD wrong changed the hedge by 400 contracts in the example.
- **A pension plan is a short-rates-down position.** Liabilities are long-duration and assets are equity-heavy, which gives a negative duration gap. Fixes are receive-fixed swaps, receiver swaptions or longer bonds (STRIPS). The irony: the choice of overlay still depends on a rate view.

## Worked Example
**1) Futures overlay for multiple liabilities (USD version of the reading's example; verified).**
- Liabilities: PV USD 200,052,250, MacDur 6.0004, CFY 3.7608% s.a.
  - ModDur = 6.0004/1.018804 = 5.8897.
  - Money duration = 1,178,237,935. **Liability BPV = 117,824**.
- Assets: short bonds with MV 222,750,000, MacDur 0.8532, CFY 1.9804%. **Asset BPV = 18,819**.
- Case 1: the CTD is the 6.5-year note (BPV 56.8727, CF 0.8226).
  - Futures BPV = 69.1377.
  - `Nf = (117,824 − 18,819)/69.1377 = 1,432` long.
- Case 2: the CTD is the 10-year note (BPV 81.6607, CF 0.8516).
  - Futures BPV = 95.8909.
  - Nf = 1,032.
- Result: a synthetic barbell (short cash bonds plus the futures point on the curve).
- Contingent immunization: the surplus of USD 22.7m permits over-hedging (> 1,432 contracts if yields are expected to fall) or under-hedging. A move from 121-03 to 119-22 is 45/32 = USD 1,406.25 per contract, or USD 2.01m on 1,432 longs.

**2) DB pension: ABO/PBO duration and the swap notional (verified).**
- Inputs: m = 2%, G = 25, T = 10, Z = 17, W₀ = 50,000, r = 5%, w = 0.9r = 4.5%.
- ABO = **173,032**. PBO = **268,714**.
- Shift r by ±1% (with w = 0.9r): ABO₊ = 146,261 and ABO₋ = 205,467, so **ABO duration = 17.1**. PBO₊ = 247,477 and PBO₋ = 292,644, so **PBO duration = 8.4**.
- The higher w in the down-rate scenario offsets the discounting, which is why the PBO duration is so much shorter.
- Scale to 10,000 employees: PBO = USD 2.687bn, PBO BPV = 2.687bn × 8.4 × 0.0001 = **USD 2,257,080**.
- Assets: USD 2.7bn, 50/40/10 equity/bonds/alts, bond duration 5.5, equity and alts at 0. **Asset BPV = 2.7bn × 0.40 × 5.5 × 0.0001 = USD 594,000**.
- Surplus = USD 13m. It is wiped out by about 13m/2.257m ≈ **5.8 bp** of lower discount rates.
- Hedge 100% with a 30-year receive-fixed swap (BPV 0.1673 per 100): `NP = (2,257,080 − 594,000)/0.001673 = USD 994.07m`. A 50% hedge needs USD 497m.
  - With futures instead: 17,343 contracts. A 5bp rise produces a daily variation margin of USD 8.3m, which is why swaps are preferred.
- Swap MTM on the 497m (50% hedge): the fixed-leg annuity is USD 149,100 per half-year per 0.06% move.
  - Swap rate falls to 4.10%: gain **USD 5.12m**.
  - Swap rate rises to 4.22%: loss **USD 5.05m**. The asymmetry comes from convexity and discounting.
  - The written 5% payer loses USD 5.33m at 5.07%, above the USD 4.97m receiver premium. So above ≈5.07% the plain receiver swaption beats the collar.

## Anti-patterns
- **Targeting the weighted-average YTM or weighted-average duration**: with a sloped curve both understate the true (cash-flow-based) figures, which introduces model risk. Use the aggregate cash flows.
- **Picking the immunizing portfolio with the "higher yield / closer duration"** when the differences are 1bp or 0.03 years. For a single liability, the decision variable is the **lowest convexity**.
- **Choosing the lowest-convexity portfolio for multiple liabilities when its convexity is below the liabilities'**: this violates the dispersion condition.
- **Matching modified duration when market values differ**: match BPV.
- **Treating immunization as buy-and-hold**: duration drifts with time and yields, so you must rebalance. In practice, rebalance when the BPV gap justifies the transaction costs.
- **Estimating portfolio dispersion as the average of bond dispersions**: a portfolio of zeros has zero average dispersion but large true dispersion. Use convexity, which aggregates correctly as a weighted average.
- **Ignoring collateral capacity**: a large pension overlay can exhaust cash or eligible collateral. Futures need daily margin. CSAs give a few days' grace and minimum transfer amounts.
- **Full replication of a broad bond index**: it is infeasible and costly. Use stratified sampling or ETFs.

## Exam Focus & Traps
- **Sign of Nf**: (Liability BPV − Asset BPV)/Futures BPV. A negative result means *sell* futures (assets too long, as in Example 6: −119 contracts).
- **Over- or under-hedge**: compute the full-hedge Nf and compare it with the position held. More longs than needed means over-hedged, a view that yields will **fall** (Example 7: 160 held vs 123.3 needed).
- **Classification traps**:
  - Deposits redeemable early are Type II (known amount, uncertain timing).
  - Prepayable mortgages are Type IV (prepayment and default).
  - Fixed-rate government bonds are Type I.
  - FRNs and linkers are Type III.
  - CoCos and P&C insurance are Type IV.
- **Cash flow matching arithmetic**: start with the **last** liability. Par = remaining need/(1 + coupon) for annual bonds, rounded **up** to the minimum denomination. Subtract later bonds' coupons from earlier needs.
- **Parallel shift is sufficient, not necessary.** Twists (steepening pivot at the horizon, butterflies) are the structural risk. A barbell loses in a steepening twist and gains in a flattening twist.
- **Receive-fixed swap duration is positive.** For the payer it is negative.
- **Strategic hedging**: raise the hedge ratio when you expect lower rates. Lower it when you expect higher rates.
- **Swap vs Treasury futures spread risk**: corporate–swap spreads are usually less volatile than corporate–Treasury spreads, because both MRR and corporates carry credit risk. That favors swaps for hedging corporate-discounted liabilities.
- **Counterparty risk** on an uncollateralized swap requires both the counterparty's default *and* the swap being an asset to you. On an option, credit risk is one-way: the buyer bears the writer's risk.
- **Replicating a callable liability's option**: to neutralize the call embedded in your own callable debt, **write a receiver swaption** (Example 9). Remaining risks: collateral exhaustion and the corporate–swap spread.
- **Laddered portfolio "most desirable aspect"**: liquidity management.
- **Benchmark**: a custom benchmark valued weekly fails the daily-valuation criterion. A young workforce (long horizon) should not get a short-duration high-yield benchmark.
- **ETF vs mutual fund**: bond ETFs trade intraday and can sit at persistent discounts or premiums to NAV, because the underlying bonds are illiquid. Mutual funds trade once a day at NAV. A TRS needs *less* cash up front, not more.

## Key Takeaways
1. Single liability: MV ≥ PV(liability), MacDur = horizon, minimize convexity, then rebalance.
2. Multiple liabilities: MV ≥ PV, BPV_A = BPV_L, and convexity_A > convexity_L but minimized.
3. Immunization locks in the **cash flow yield** and fails only when the portfolio's yield change differs from the replicated zero's.
4. Overlays: `Nf = (BPV_L − BPV_A)/(BPV_CTD/CF_CTD)`, and `NP = (BPV_L − BPV_A)/(SwapBPV/100)`. Know the CTD.
5. DB plans usually run large negative duration gaps. Pick a hedge ratio (often partial), then pick swap, receiver swaption or collar according to the rate view and collateral capacity.
6. LDI risks: model (ABO vs PBO, zero equity duration, futures BPV approximation), spread, counterparty and collateral, asset liquidity (contingent immunization).
7. Bond indexing: match the risk factors (duration, KRDs, sector and quality spread duration, call weights, issuer duration) with stratified sampling. Full replication is impractical.
8. Choose the benchmark by duration profile and risk tolerance, and remember that index duration drifts and composition follows issuers.

## Connects To
- **ch05**: Macaulay/modified/money duration, convexity, horizon vs duration (the L1 base of immunization).
- **ch09**: effective duration and embedded options (Types II–IV).
- **ch12**: the overview of liability-based vs total-return mandates and the classification of fixed-income mandates.
- **ch14**: yield-curve strategies. Bullet vs barbell convexity and the key-rate and futures tools reused here.
- **ch15**: credit strategies. Spread duration, which feeds the spread-risk leg of LDI.
- **`cfa-derivatives` ch06**: swaps, futures and forwards strategies (futures BPV, CTD, swaptions).
- **`tuckman-fixed-income` ch04–05**: DV01 hedging and multi-factor (key-rate) hedges. **ch14**: note and bond futures, CTD and conversion factors. **ch16**: swaps.
- **`cfa-wealth-institutional-management` ch04**: institutional investors (DB plans, insurers) and their liability profiles.
- **`cfasi-fixed-income-guides`**: practitioner view of passive bond funds and ETFs.
