# Chapter 14: Fixed-Income Securities — Defining Elements (Fixed Income)

## Core Idea
A bond is a contract between an issuer and its bondholders, set out in the indenture. Its core features determine the scheduled cash flows:
- issuer,
- maturity,
- par value,
- coupon and frequency,
- currency.

Credit risk is shaped by collateral, credit enhancements and covenants. Principal and coupon structures, plus embedded options (call, put, conversion), change the cash flows, the risk and the yield.

## Frameworks Introduced
- **Basic features**:
  - **Issuers**: supranational, sovereign, non-sovereign government, quasi-government, corporate (financial/non-financial), special legal entities (SPVs).
  - **Credit quality**: investment grade vs non-investment grade (high yield).
  - **Maturity/tenor**: money market (≤ 1y) vs capital market (> 1y); perpetual bonds.
  - **Par value**: prices are quoted as % of par (95 = 950 on 1,000 par).
  - **Coupon**:
    - fixed (plain vanilla),
    - floating (FRN = reference rate + fixed spread),
    - zero-coupon (issued at a discount).
  - **Currency**: domestic, foreign, **dual-currency** (coupons in one currency, principal in another), **currency-option** bonds.
  - **Current yield** = annual coupon / price. **YTM** = IRR if held to maturity.
- **Indenture and trustee**:
  - The indenture specifies the issuer's legal identity, source of repayment, collateral, credit enhancements and covenants.
  - The **trustee** monitors compliance, keeps records, manages collateral, processes payments and represents bondholders.
- **Issuer structure**:
  - Subsidiary vs parent guarantee. **Holding-company** debt is structurally subordinated to operating-company debt.
  - **Repayment sources**:
    - Supranationals: loan repayments and paid-in capital.
    - Sovereigns: "full faith and credit" (taxes, money creation).
    - Non-sovereigns: general taxes, project cash flows or special fees.
    - Corporates: operating cash flow.
    - ABS: the cash flows of the pool.
- **Collateral and seniority**:
  - Secured > senior unsecured > subordinated (junior).
  - Collateral trust bonds are backed by financial assets.
  - **Equipment trust certificates** are backed by assets such as aircraft or rigs, which a trustee holds and leases to the issuer.
  - **Covered bonds**: the cover pool stays on the bank's balance sheet, so investors have **dual recourse** (bank + pool). ABS investors have recourse to the SPV only.
  - **SPVs are bankruptcy-remote**.
- **Credit enhancements**:
  - **Internal**:
    - subordination (tranching),
    - overcollateralization,
    - reserve accounts (cash reserve fund, excess spread account; "turboing" uses excess spread to pay down senior principal).
  - **External**:
    - bank guarantees,
    - surety bonds (monoline insurers; capped at the penal sum),
    - letters of credit.
    - These carry third-party (guarantor) risk. **Cash collateral accounts** avoid it because the cash is invested upfront.
- **Covenants**:
  - **Affirmative** (must do): comply with laws, maintain assets, pay taxes, maintain the business.
  - **Negative** (must not):
    - limits on debt and leverage,
    - negative pledge,
    - limits on prior claims,
    - limits on distributions and buybacks,
    - limits on asset sales and investments,
    - limits on M&A.
- **Markets**:
  - National market: **domestic** bonds (domestic issuer) vs **foreign** bonds (foreign issuer, local currency — Yankee, Samurai).
  - **Eurobonds**: issued outside any single jurisdiction, lightly regulated, bearer form common.
  - **Global bonds**: issued in the Eurobond market and at least one domestic market at the same time.
- **Taxes**:
  - Coupons are taxed as ordinary income. Capital gains are taxed differently (long vs short term).
  - Original-issue discount (OID) rules apply to bonds bought at a discount.
- **Principal repayment structures**:
  - **Bullet**.
  - **Fully amortizing**.
  - **Partially amortizing** (with a balloon payment).
  - **Sinking fund**: retires part of the issue periodically, by lottery at par or by open-market purchase. It lowers credit risk and adds reinvestment risk.
- **Coupon structures**:
  - FRNs, with caps and floors.
  - **Inverse floaters**: the coupon falls as rates rise.
  - **Step-up** coupons.
  - **Credit-linked** coupons: the coupon rises on a downgrade, which can accelerate distress.
  - **Payment-in-kind (PIK)**: interest paid in more bonds.
  - **Deferred** coupons.
  - **Index-linked** bonds: inflation-linked "linkers" such as TIPS, with the principal indexed to CPI.
- **Contingency provisions (embedded options)**:
  - **Callable**: the issuer's option. Price and yield are higher to compensate. American, European or **Bermudan** exercise, with call protection and a call price. Make-whole calls also exist.
  - **Putable**: the investor's option, so the yield is lower.
  - **Convertible**: the investor can exchange the bond for shares.
    - Conversion ratio = par / conversion price.
    - Conversion value = share price × ratio.
    - Conversion premium = bond price − conversion value.
    - Related instruments: warrants and **contingent convertibles (CoCos)**, which convert automatically when a trigger is hit (bank capital).

## Key Concepts
- **Tenor**: time remaining to maturity.
- **Penal sum**: the maximum payout of a surety bond or guarantee.
- **Excess spread**: asset cash flow − interest paid to bondholders.

## Mental Models
- **Read the indenture to understand the risk**: who pays, from what, secured by what, and what the issuer cannot do.
- **The option holder gets the value**: a callable bond has a higher yield (the investor is short the call); a putable bond has a lower yield (the investor is long the put).
- **Internal enhancement avoids third-party risk; external enhancement adds it.**

## Anti-patterns
- **Assuming parent support for subsidiary debt** without an explicit guarantee.
- **Counting a surety bond as risk-free**: the monoline itself can fail (2008).
- **Ignoring reinvestment risk** from sinking funds and calls.

## Worked Example
**Current yield and conversion.**
- A 6% coupon bond on 1,000 par trades at 1,010. Current yield = 60/1,010 = **5.94%** (from the notes).
- A convertible bond has par 1,000 and conversion price $40, so the conversion ratio = **25 shares**.
- With the stock at $36: conversion value = $900. If the bond trades at $980, the conversion premium = **$80**.

## Key Takeaways
1. The core features (issuer, maturity, par, coupon, currency) fix the cash flows.
2. The indenture plus trustee, collateral, enhancements and covenants shape credit risk.
3. Covered bonds give dual recourse. ABS rely on a bankruptcy-remote SPV.
4. Repayment structures: bullet, amortizing, sinking fund. Coupons: fixed, FRN, zero, step-up, PIK, linkers.
5. A call raises the yield; a put lowers it. Convertibles add equity upside, and CoCos convert on a trigger.

## Connects To
- **Ch 15**: issuance and markets.
- **Ch 16**: pricing and yields.
- **Ch 17**: ABS structures.
- **Ch 18**: interest rate risk.
- **Ch 19**: credit analysis.
