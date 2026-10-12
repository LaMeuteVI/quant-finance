# Chapter 16: Introduction to Fixed-Income Valuation (Fixed Income)

## Core Idea
A bond's price is the PV of its promised cash flows, discounted either at one market rate (YTM) or at the spot rate for each date. Quote conventions (flat vs full price, periodicity, money-market bases) must be handled carefully. The term structure (spot, par and forward curves) and spreads (G-, I-, Z-spread, OAS) break a yield into its macro component (the benchmark) and its issuer-specific component (the spread).

## Frameworks Introduced
- **Price with one discount rate**: `PV = Σ PMT/(1 + r)ᵗ + FV/(1 + r)ᴺ`.
  - Coupon < r → **discount**. Coupon > r → **premium**. Coupon = r → **par**.
- **YTM**: the IRR of the cash flows. It assumes the bond is held to maturity, there is no default, and coupons are reinvested at the YTM.
- **Price–yield properties**:
  1. Price and yield move inversely.
  2. Lower coupon means greater % price sensitivity (**coupon effect**).
  3. Longer maturity means greater sensitivity (**maturity effect**), usually.
  4. **Convexity**: the price rises more when yields fall than it drops when yields rise by the same amount.
  5. **Constant-yield price trajectory**: the price pulls to par as the bond approaches maturity.
- **Spot-rate pricing**: `PV = Σ PMT/(1 + Zₜ)ᵗ + FV/(1 + Z_N)ᴺ`. Each cash flow is discounted at its own zero rate.
- **Flat price, accrued interest, full price**:
  - `PV_full = PV_flat + AI`, with `AI = (t/T) × PMT`.
  - `PV_full = PV × (1 + r)^{t/T}`.
  - Quotes use the flat price, so the price doesn't jump on coupon dates.
  - Day-count conventions: actual/actual (governments), 30/360 (corporates).
- **Matrix pricing**: price illiquid bonds by interpolating the yields of comparable bonds (similar tenor, coupon and credit). It is also used to set the spread on new issues.
- **Periodicity conversion**: `(1 + APR_m/m)^m = (1 + APR_n/n)^n`. US bonds use periodicity 2 (semiannual bond basis).
- **Yield measures**:
  - **Street convention** (ignores weekends and holidays) ≥ **true yield**.
  - **Government-equivalent yield**: restates a 30/360 yield on an actual/actual basis.
  - **Current yield** = annual coupons / flat price.
  - Callable bonds: yield-to-first-call, second call, …, maturity. The minimum is the **yield-to-worst**.
  - Or value the option separately to get an option-adjusted yield.
- **FRNs**:
  - Coupon = reference rate + **quoted margin (QM)**.
  - Priced by discounting at reference rate + **discount margin (DM)**: `PV = Σ [(RR + QM)/m × FV]/(1 + (RR + DM)/m)ᵗ + FV/(1 + (RR + DM)/m)ᴺ`.
  - DM > QM means the price is below par.
- **Money market instruments**:
  - Annualized but not compounded. They use 360- or 365-day years and either a discount or an add-on basis.
  - **Discount basis**: `PV = FV × (1 − Days/Year × DR)` (T-bills, CP).
  - **Add-on basis**: `PV = FV/(1 + Days/Year × AOR)` (CDs, repo, interbank).
  - **Bond equivalent yield** = the 365-day add-on rate.
- **Term structure**:
  - **Spot (zero/strip) curve**: YTMs of zero-coupon bonds.
  - **Par curve**: the coupon rates that price each maturity at par.
  - **Forward rates**: `(1 + z_A)^A × (1 + IFR_{A,B−A})^{B−A} = (1 + z_B)^B`. Notation "2y5y" = a 5-year rate starting in 2 years.
  - The forward rate is the **break-even reinvestment rate**.
- **Yield spreads**:
  - YTM = benchmark (macro: inflation, growth, policy) + spread (micro: credit, liquidity, tax).
  - **G-spread**: over an actual or interpolated government bond.
  - **I-spread**: over the swap rate of the same tenor.
  - **Z-spread**: the constant spread over the *spot* curve that reprices the bond.
  - **OAS = Z-spread − option value (in bp)**: for callable bonds, OAS < Z-spread.

## Key Concepts
- **Market discount rate / required yield**.
- **On-the-run benchmark yield curve** vs **swap curve**.
- **Accrued interest** does not depend on the market rate.

## Mental Models
- **Price = PV of cash flows; everything else is convention.** Convert the quote to the full price and one periodicity before comparing.
- **Spot rates for pricing, forward rates for break-evens, par rates for new issues.**
- **Spreads separate "the market" from "the issuer".**

## Anti-patterns
- **Comparing yields with different periodicities or day counts**.
- **Using YTM for callable bonds**: use yield-to-worst or OAS.
- **Treating the money-market discount rate as a yield**: it understates the true return.
- ⚠ **Typo in the notes**: the YTM in the 105-price example is **3.634%**, not 3.364%.

## Worked Example
**Price and YTM (from the notes, verified).**
- A 5-year 4% annual bond at a 6% market rate: PV = 4 × [1 − 1.06⁻⁵]/0.06 + 100/1.06⁵ = **91.575**, a discount.
- A 4-year 5% bond priced at 105: solve 105 = Σ 5/(1 + r)ᵗ + 100/(1 + r)⁴, giving **r = 3.634%**.

**Forward rate.** z₁ = 2%, z₂ = 3%.
- (1.03)² / 1.02 − 1 = **4.01%**. That is the 1y1y implied forward rate.

**Periodicity.** 6% with semiannual compounding = (1.03)² − 1 = **6.09%** effective annual.

## Key Takeaways
1. Price = PV of cash flows. Coupon vs YTM decides premium, discount or par.
2. YTM assumes the bond is held to maturity, no default, and reinvestment at the YTM.
3. Full price = flat price + accrued interest. Convert periodicity before comparing.
4. Money market: discount basis vs add-on basis, 360 vs 365 days.
5. Spot → forward: (1 + z_A)^A (1 + f)^{B−A} = (1 + z_B)^B. Spreads: G, I, Z, OAS.

## Connects To
- **Ch 14**: bond features.
- **Ch 18**: duration and convexity.
- **Ch 19**: credit spreads.
- **Hull Ch 4** (`hull-derivatives`): bootstrapping zero curves.
