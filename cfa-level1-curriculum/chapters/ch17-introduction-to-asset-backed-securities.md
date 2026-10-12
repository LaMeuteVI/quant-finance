# Chapter 17: Introduction to Asset-Backed Securities (Fixed Income)

## Core Idea
Securitization sells a pool of loans to a bankruptcy-remote **SPV**, which funds the purchase by issuing tranched securities. Investors take on the pool's risk rather than the originator's. **Credit tranching** reallocates default risk and **time tranching** reallocates prepayment risk. The main products are RMBS (pass-throughs, CMOs), CMBS, non-mortgage ABS (auto loans, credit cards) and CDOs.

## Frameworks Introduced
- **Benefits of securitization**:
  - Disintermediation: investors are exposed to the pool, not to the bank.
  - Tailored risk and return through tranching.
  - Lower funding costs.
  - Frees bank capital for new lending.
  - Deeper, more liquid markets.
- **Risks**: credit risk of the pool, and **prepayment risk** — **contraction risk** (rates fall, prepayments speed up, proceeds are reinvested at lower rates) vs **extension risk** (rates rise, prepayments slow, the investor is locked into a below-market coupon for longer).
- **Parties**: seller/originator/depositor, SPV/issuer, servicer, trustee, rating agencies, lawyers and accountants, guarantors, underwriters.
- **Documentation**: purchase agreement (representations and warranties on the assets) and prospectus (structure, waterfall, credit enhancements).
- **Why the SPV matters**:
  - A **true sale** at arm's length puts the assets beyond the reach of the originator's creditors.
  - So the ABS can be rated above the originator. For example, a BB-rated firm can issue AAA senior tranches.
  - A secured corporate bond gains less, because absolute priority is not always enforced in reorganization.
- **Residential mortgage loans**:
  - **LTV** = loan / property value. A lower LTV means more borrower equity and a lower default risk.
  - Prime vs subprime borrowers.
  - Rate types: fixed, **ARM**, initial-period fixed (rollover/renegotiable vs hybrid), convertible.
  - Amortization: full, partial (balloon) or interest-only.
  - **Prepayment option** vs **prepayment-penalty** mortgages.
  - **Recourse vs non-recourse**. Non-recourse mortgages invite **strategic default** when the loan is underwater.
- **RMBS**:
  - **Agency** RMBS: federal agency (GNMA, full faith and credit) or GSE (Fannie Mae, Freddie Mac). The loans must be **conforming**.
  - **Non-agency** RMBS: private issuers, credit enhancement needed.
- **Mortgage pass-throughs**:
  - Pass-through rate = mortgage rate − servicing and other fees.
  - The pool is described by its **WAC** (weighted average coupon) and **WAM** (weighted average maturity).
- **Prepayment measures**:
  - `SMM = prepayment in month / (beginning balance − scheduled principal)`.
  - `CPR = 1 − (1 − SMM)¹²`.
  - **PSA benchmark**: 100 PSA ramps the CPR up 0.2% per month to 6% at month 30, then flat. 200 PSA is twice as fast.
- **CMOs**:
  - **Sequential-pay**: principal goes to tranche A first, then B, and so on. Earlier tranches carry more contraction risk; later ones more extension risk.
  - **PAC (planned amortization class)**: a predictable schedule within a band of prepayment speeds.
  - **Support (companion)** tranches absorb both contraction and extension risk. They carry the **highest** prepayment risk.
- **CMBS**:
  - Loans are usually **non-recourse**. Credit metrics: **LTV** and **DSC = NOI / debt service**.
  - The equity (residual) tranche is often unrated.
  - **Call protection**:
    - At the structure level: sequential tranching.
    - At the loan level: **prepayment lockout**, **prepayment penalty points**, **yield maintenance charges**, **defeasance** (replacement with a portfolio of government bonds).
  - **Balloon risk**: failure to refinance at maturity leads to a workout period at a default interest rate. It is a form of extension risk.
- **Non-mortgage ABS**:
  - **Auto loans**: amortizing. Credit enhancement via subordination, overcollateralization and reserve (excess spread) accounts.
  - **Credit card receivables**: non-amortizing, with a **lockout (revolving) period** during which principal is reinvested. **Early amortization triggers** protect investors.
- **CDOs**: an SPV plus a **collateral manager** that actively manages the portfolio.
  - Types: CBO (bonds), **CLO** (leveraged loans), structured-finance CDO (ABS/RMBS/CMBS), **synthetic** CDO (CDS).
  - Tranches: senior / mezzanine / subordinated / equity. The equity tranche and the manager keep the excess return.

## Key Concepts
- **Credit tranching (subordination)** vs **time tranching** (different expected maturities).
- **Conforming vs non-conforming** loans.
- **Underwater mortgage**: the loan exceeds the property value.
- **Average life**: the weighted average time to receive principal. It is the key metric for MBS tranches.

## Mental Models
- **Every MBS investor is short a prepayment (call) option** held by homeowners. That creates negative convexity.
- **The waterfall decides who bears what**: junior tranches take the first losses, support tranches take the prepayment variability.
- **Match the CMBS call protection mechanism to your view on rates**: defeasance and yield maintenance protect best.

## Anti-patterns
- **Treating AAA ABS as risk-free**: correlation and model risk (the 2007–8 crisis; see Hull Ch 8).
- **Ignoring extension risk when rates rise**: long-duration surprises.
- ⚠ **Precision vs the notes**: a CDO is backed by a pool of *debt obligations* (bonds, loans, ABS or CDS), not only by ABS.

## Worked Example
**Subordination (Mediquip / MET from the notes).** A $200m pool is split into Class A $180m (senior), Class B $14m and Class C $6m.
- Losses up to $6m: C absorbs them all.
- $6–20m: B absorbs them after C is wiped out.
- Above $20m: A starts losing.
- With $15m of losses: **C loses 100%**, **B loses 9/14 = 64%**, **A loses 0%**.

**Prepayment speed.** SMM = 0.5% → CPR = 1 − 0.995¹² = **5.84%**.

## Key Takeaways
1. A true sale to a bankruptcy-remote SPV separates pool risk from originator risk.
2. Prepayment risk comes as contraction risk (rates ↓) and extension risk (rates ↑).
3. SMM ↔ CPR; PSA is the benchmark prepayment speed.
4. Sequential CMOs time-tranche the pool. PAC tranches are protected; support tranches absorb the variability.
5. CMBS: non-recourse loans, DSC/LTV metrics, strong loan-level call protection, balloon risk.

## Connects To
- **Ch 14**: credit enhancements and SPVs.
- **Ch 18**: effective duration and negative convexity.
- **Ch 19**: credit analysis.
- **Hull Ch 8 / Ch 33** (`hull-derivatives`): the crisis, agency MBS, IO/PO.
