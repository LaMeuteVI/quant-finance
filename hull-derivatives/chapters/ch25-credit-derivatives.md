# Chapter 25: Credit Derivatives

## Core Idea
Credit derivatives separate credit risk from funding.
- A **CDS** is insurance on one name's default. Value it as PV(expected payoff) = PV(expected premiums) under risk-neutral hazard rates.
- **Indices, baskets and synthetic CDOs** extend this to portfolios. Their tranche values hinge on default correlation, usually handled with the one-factor Gaussian copula.

## Frameworks Introduced
- **CDS mechanics**:
  - The buyer pays a spread s per year on notional, quarterly in arrears, plus accrual up to the default date.
  - On a credit event the seller pays notional × (1 − R).
  - R is set by an **ISDA auction** on the cheapest-to-deliver bond; physical settlement is also possible.
- **CDS valuation (risk-neutral)**:
  - Premium leg: Σ s × survival probability × discount factor, plus the accrual term.
  - Protection leg: Σ (1 − R) × default probability × discount factor.
  - The breakeven s sets the two equal.
  - Shortcut: `s ≈ λ(1 − R)`.
- **Implied hazard rates**: bootstrap λ from CDS quotes at several maturities, the same way a zero curve is bootstrapped.
- **Credit indices**: CDX NA IG (125 names) and iTraxx Europe (125 names). They roll every 6 months. The index spread is ≈ the average of the constituent spreads.
- **Fixed coupons + upfront**: standard coupons (e.g., 100 or 500bp; 40bp in the index example below). The price is `100 − 100 × duration × (spread − coupon)`, so an upfront payment settles the difference.
- **CDS forwards / options**: they knock out if default happens before the start date.
- **Basket CDS (kth-to-default)**: pays on the k-th default in the basket.
  - Higher correlation → first-to-default is **cheaper**, and later defaults (k large) are **more expensive**.
- **Total return swap (TRS)**:
  - One side pays the total return on a bond portfolio (coupons + price change).
  - The other side receives SOFR + spread.
  - It works as financing; the spread compensates for the joint default risk of the payer and the reference assets.
- **CDOs**:
  - **Cash CDO**: bonds in an SPV, split into tranches.
  - **Synthetic CDO**: tranches defined on losses of a CDS reference portfolio.
  - Standard iTraxx tranches: 0–3%, 3–6%, 6–9%, 9–12%, 12–22%.
- **One-factor Gaussian copula for tranches**:
  - Conditional on the factor F, defaults are independent. Default probability given F: `Q(t|F) = N[(N⁻¹(Q(t)) − √ρF)/√(1 − ρ)]`.
  - Integrate over F with Gauss–Hermite quadrature to get the expected tranche loss, then the breakeven spread.
- **Implied correlation**: market practice analogous to implied volatility.
  - **Compound correlation**: a separate correlation per tranche.
  - **Base correlation**: a correlation for each 0–X% tranche, monotonic, so it can be interpolated.
- **Alternatives to the standard model**: heterogeneous names, t-copula, random factor loadings, implied copula, dynamic models.

## Key Concepts
- **Reference entity / reference obligation**; **credit event**: bankruptcy, failure to pay, restructuring.
- **Notional of CDS vs bonds**: CDS notional can exceed the bonds outstanding.
- **CDS–bond basis**: CDS spread − bond yield spread. It is usually positive.
- **Unfunded vs funded protection**; **credit-linked notes**.
- **Business Snapshot 25.1**: banks transfer credit risk, but a lot ends up with insurers, hedge funds and other banks. The question to ask is *who really bears it?*

## Mental Models
- **CDS spread ≈ λ × LGD** is the annual expected loss rate under risk-neutral probabilities.
- **Correlation redistributes risk across tranches**. Higher ρ makes equity **safer** (more chance of zero losses) and senior **riskier** (more chance of big losses).
- **A kth-to-default basket behaves like a tranche** of a small portfolio.

## Anti-patterns
- **Pricing tranches with one flat correlation across all tranches**: it cannot fit the market (correlation smile). Use base correlation.
- **Ignoring counterparty risk of the protection seller**: this is wrong-way risk (AIG sold massive protection).
- **Treating TRS financing as risk-free**: the financier is exposed if the asset value drops *and* the counterparty defaults.

## Worked Example
**5-year CDS spread (Section 25.2).** Hazard rate λ = 2% per year, R = 40%, r = 5%, annual payments.
- Survival probabilities: e^{−0.02t}. Default probability in year 3 = 0.9608 − 0.9418 = 0.0190.
- PV of expected payoffs = **0.0506** per $1 of notional.
- Setting the premium leg (incl. accrual) equal to the payoff leg gives the mid spread **s = 0.0123 (≈ 123bp)**.
- Check: λ(1 − R) = 2% × 0.6 = 120bp.

**Index trade (Example 25.1).** iTraxx is quoted at 34bp with a 40bp coupon (actual/360). In actual/actual terms these are 0.345% and 0.406%. Duration = 4.447 years.
- Price = 100 − 100 × 4.447 × (0.00345 − 0.00406) = **100.27**.
- So the protection seller pays the buyer 0.27% upfront.

## Key Takeaways
1. CDS spread = the breakeven between premium PV and protection PV under risk-neutral λ. Approximately s ≈ λ(1 − R).
2. Bootstrap hazard curves from CDS quotes. Indices trade with fixed coupons plus upfront payments.
3. Correlation moves value between equity and senior tranches in opposite directions.
4. The one-factor Gaussian copula plus base correlation is the market's quoting model.
5. Counterparty risk on protection sellers is wrong-way risk.

## Connects To
- **Ch 24**: hazard rates, recovery, the Gaussian copula.
- **Ch 8**: cash CDOs and the crisis.
- **Ch 9**: CDS used to hedge CVA.
- **Ch 7**: CDS introduced as a type of swap.
