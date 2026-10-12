# Chapter 19: Fundamentals of Credit Analysis (Fixed Income)

## Core Idea
Credit risk = default probability × loss severity, plus spread risk (downgrades and liquidity). Analyze an issuer with the **four Cs**: capacity, collateral, covenants, character. Use seniority and recovery analysis. Treat agency ratings with care, because they lag the market. High-yield, sovereign and municipal issuers each need their own tilt to the analysis.

## Frameworks Introduced
- **Components of credit risk**:
  - `Expected loss = PD × LGD`, where LGD = loss severity = 1 − recovery rate.
  - **Spread risk**: **downgrade (credit migration) risk** and **market liquidity risk**. The liquidity premium is larger for small issues and weaker issuers.
- **Capital structure and seniority**:
  1. First lien / first mortgage.
  2. Second lien.
  3. Senior unsecured.
  4. Senior subordinated.
  5. Subordinated.
  6. Junior subordinated.
  7. Equity.
  - **Pari passu**: claims at the same level are treated equally, regardless of maturity.
  - Why issue subordinated debt: it is cheaper than equity with no dilution, less restrictive than senior debt, and there is demand for its yield.
- **Recovery rates**:
  - They vary by seniority, by industry (declining industries recover less than industries in a cyclical downturn) and by the **credit cycle** (lower near troughs).
  - **Absolute priority is not always enforced** in reorganizations. Negotiated settlements often give junior claimants more than their strict entitlement.
- **Credit ratings**:
  - Agencies: Moody's, S&P, Fitch (plus DBRS, JCR).
  - Investment grade is **Baa3/BBB− or higher**; below that is high yield.
  - Outlooks (positive, stable, negative) and watch lists.
  - **Issuer ratings** (CFR/CCR) vs **issue ratings**.
  - **Notching**: issue ratings are adjusted from the senior unsecured baseline for seniority and structural subordination, one or two notches up or down. Cross-default clauses mean PD is shared across an issuer's debt.
- **Risks in relying on ratings**:
  - Ratings change over time.
  - Some risks are hard to capture (litigation, environmental, LBOs, buybacks).
  - Agencies make mistakes.
  - **Ratings lag market prices and spreads**.
- **The four Cs**:
  - **Capacity**:
    - Industry structure (Porter's five forces), industry fundamentals (cyclicality, growth).
    - Company fundamentals: competitive position, operating history, management's strategy.
    - Ratios:
      - *Profitability/cash flow*: EBITDA, FFO, FCF before and after dividends.
      - *Leverage*: debt/capital, debt/EBITDA, FFO/debt, FCF after dividends/debt.
      - *Coverage*: EBITDA/interest, EBIT/interest.
    - **Liquidity**: cash, working capital, operating cash flow, committed bank lines, versus debt maturities and capex due in the next 1–2 years.
  - **Collateral**: asset quality and marketability. A **capex/depreciation** ratio < 1 signals underinvestment. Watch the share of intangibles.
  - **Covenants**: protections and restrictions in the indenture.
  - **Character**: management strategy, track record, aggressive accounting or tax practices, fraud history, past treatment of bondholders.
- **Yield decomposition**: `corporate yield = real r_f + expected inflation + maturity premium + liquidity premium + credit spread`.
  - Spreads **widen** when the credit cycle or economy deteriorates, markets fall, or supply of bonds is heavy.
  - Spreads **narrow** in the opposite conditions.
  - Price impact of a spread change: ≈ −ModDur × Δspread + ½ × Convexity × Δspread².
- **High-yield specifics**:
  - Reasons for the rating: high leverage, weak operating history, limited FCF, poor management, weak competitive position, declining industry.
  - Focus on **liquidity**, detailed projections, the **debt structure and corporate structure** (holding-company vs operating-company debt), and **covenants**: change-of-control put, restricted payments, limits on liens and additional debt, maintenance covenants.
  - Take an **equity-like approach**, with recovery analysis.
- **Sovereign analysis**: the ability *and willingness* to pay. Willingness matters because of **sovereign immunity**: creditors cannot force payment. Five profiles:
  - **Institutional**: policy effectiveness, crisis track record, transparency, rule of law, repayment culture.
  - **Economic**: GDP per capita, growth, diversification.
  - **External**: reserve-currency status, external liquidity, external debt.
  - **Fiscal**: fiscal flexibility, debt burden and structure, access to funding.
  - **Monetary**: policy effectiveness, exchange-rate regime, central bank credibility.
  - Local-currency ratings are usually ≥ foreign-currency ratings.
- **Non-sovereign government (US munis, ≈ $3.9tn)**:
  - **GO bonds** are backed by taxing power: analyze the economy, tax base, per-capita debt, demographics, pensions.
  - **Revenue bonds** are backed by project cash flows: analyze usage, the economic base, and the **debt-service coverage ratio**.

## Key Concepts
- **Structural subordination**: holding-company creditors rank behind operating-company creditors on the subsidiary's assets.
- **Cross-default**: a default on one obligation triggers default on others.
- **FFO**: net income + D&A + deferred taxes + other non-cash items.

## Mental Models
- **Credit is asymmetric**: limited upside, large downside. Focus on what can go wrong.
- **Cash flow services debt, collateral limits losses, covenants control behavior, character predicts intent.**
- **Markets price credit before agencies do.** Watch spreads, not just ratings.

## Anti-patterns
- **Ignoring structural subordination** in holding-company debt.
- **Assuming absolute priority** in recovery estimates.
- **Treating ratings as real-time signals**.
- ⚠ **Correction vs the notes**: market liquidity risk is the risk that the transaction price **differs** from the indicated market price. The notes say "doesn't differ much".

## Worked Example
**Expected loss.** A BB bond has a 2% 1-year PD and a 40% recovery rate.
- EL = 2% × (1 − 0.4) = **1.2%** per year. That is a rough floor for the credit spread, before the risk and liquidity premia.

**Leverage and coverage screen.** EBITDA = 500, debt = 2,000, interest = 100, FFO = 380.
- Debt/EBITDA = **4.0×**. EBITDA/interest = **5.0×**. FFO/debt = **19%**. This is typical of high BB / low BBB.

**Spread shock.** ModDur = 6, spread widens 100bp → price ≈ **−6%**.

## Key Takeaways
1. EL = PD × LGD. Spread risk = downgrades + liquidity.
2. Seniority determines recovery, but absolute priority can be violated in reorganizations.
3. Ratings: IG ≥ BBB−/Baa3. Issue ratings are notched from the senior unsecured baseline. Ratings lag markets.
4. Four Cs: capacity (ratios, liquidity), collateral, covenants, character.
5. High yield → liquidity, structure, covenants, equity-like analysis. Sovereigns → willingness plus five profiles. Munis → GO vs revenue (DSCR).

## Connects To
- **Ch 11**: industry analysis.
- **Ch 14**: covenants and seniority.
- **Ch 16**: spreads.
- **Ch 18**: spread duration.
- **Hull Ch 24 / Ch 25** (`hull-derivatives`): hazard rates, CDS.
