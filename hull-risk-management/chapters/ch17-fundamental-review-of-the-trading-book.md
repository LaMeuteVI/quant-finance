# Chapter 17: Fundamental Review of the Trading Book
> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed., Wiley 2012 | Ch. 17, pp. 373–380

## Core Idea
FRTB ends the twenty-year use of 10-day 99% VaR for market-risk capital and replaces it with **expected shortfall at 97.5%**, computed over **a stressed period** and over **risk-specific liquidity horizons** (10/20/60/120/250 days). It also tightens trading-vs-banking-book assignment and splits credit trades into credit-spread risk (market risk) plus jump-to-default risk (a separate IDR charge).

> ⚠ **Practitioner update — this chapter is SUPERSEDED**
> The chapter describes the **FRTB consultative drafts as of December 2014** (May 2012 first paper, October 2013 revised paper, December 2014 "Outstanding Issues" paper — the book cites all three and its Table 17.1 is labelled "December 2014 consultative document"). **The binding standard is BCBS d457, *Minimum capital requirements for market risk*, January 2019**, which was superseded in the EU by CRR3 (Regulation (EU) 2024/1623) and, in the UK, by the post-Brexit PRA regime. FRTB implementation in the EU has been deferred to **1 January 2028**. Treat everything in this chapter as design rationale and architecture, not as a rule set.
>
> **What changed between the draft described here and BCBS d457 (2019)** — *2019 status, not from the book*:
> - **ES multiplier framework retained.** Stressed ES is still scaled against its 60-business-day average with a multiplier of at least **3**, and the non-stressed (recent-window) leg is subject to a **1.5** multiplier plus backtest-driven add-ons. The book only describes the Basel II.5-style `m_c, m_s ≥ 3` pair on both legs.
> - **Curvature risk is new.** Risk-neutral P&L attribution (PLA) became mandatory, with a **vega risk curvature multiplier** of **0.5** applied to the sum of the two worst vega sensitivities in each risk class and each bucket. This is a genuine addition, not present in the drafts summarised here.
> - **Non-modellable risk factors (NMRF) get their own add-on.** The final standard requires a separate NMRF capital add-on; the 2012–2014 drafts relied on the *default risk capital* concept.
> - **The default risk charge (DRC) replaced both the IRC and the book's IDR.** DRC is a one-year 99.9% VaR on default risk (not jump-to-default only), computed separately for non-securitisation positions and for securitisation positions, and **securitisation DRC cannot be offset against non-securitisation DRC**. Constant level of risk was abolished, as the book notes.
> - **Credit spread risk on securitisations changed substantially.** The correlation structure (`ρ_kl`) for the tranche/residual decomposition, the treatment of basis between cash and synthetic tranches, and the jump-to-default elements were all revised. The book's statement that "credit trades are handled simply by separating spread risk from jump-to-default risk" no longer describes the final rules.
> - **Market risk standardised approach was redesigned.** The book's bucket formula with Basel-set weights `w_i` and correlations `ρ_ij` became a full delta + vega + curvature charge with prescribed intra-bucket and inter-bucket correlations and limited offsetting.
> - **Low-risk-offshore trading books** (LRTS) were retained and simplified for jurisdictions with low-risk offshore markets: Basel consolidated, with long and short positions not offsetting for certain instrument types. Basel III did not revise the standard approach.
> - **Stress-period definition.** The book notes a 2013 proposal requiring the search to go back at least to 2005; the final standard requires the most severe 12-month stress period starting from **2007** onward.
>
> **Binding rules live in the `frtb-market-risk-bcbs457` skill. Use this chapter for the architecture and the failure modes only.**

## Frameworks Introduced

- **Expected shortfall (ES) replacing VaR**: capital based solely on `ES` at **97.5%** measured over a **12-month stressed period**, chosen to be particularly severe for the bank's current portfolio.
  - *When to use*: any modern market-risk number, internal or regulatory.
  - *Why it works*: ES is coherent (subadditive) where VaR is not, and it prices the tail rather than stopping at a quantile.
  - *Failure mode*: under normality the two are nearly identical (`99% VaR = μ + 2.326σ` vs `97.5% ES = μ + 2.338σ`, both verified) — the gain is entirely in the tail. If your historical sample has no tail, switching from VaR to ES changes nothing.

- **Liquidity horizons (book's Table 17.1)**: each market variable is assigned a horizon of 10, 20, 60, 120 or 250 days; shocks are taken over that horizon in stressed conditions. Large-cap equity 10d; small-cap equity 20d; IG corporate credit spread 60d; non-IG corporate credit spread 120d; structured-product credit spread 250d.

- **Aggregated ES formula (eq. 17.1)**: `ES = √ES₁ + √( Σ_{j=2..5} [ (ES_j − ES_{j−1}) · (LH_j − LH_{j−1}) / 10 ] )`, where `ES₁…ES₅` are five separate ES calculations in which only variables at or beyond each liquidity-horizon bucket are shocked, and each `ES_j` is obtained by √-time-scaling the 10-day result.
  - *Failure mode*: the overlapping-window construction means successive trials are **not independent**. This does not bias the estimate but shrinks the effective sample size and inflates estimator variance — the book says so explicitly.

- **Partial ES and diversification cap**: ES is computed for the whole portfolio *and* per risk category (GIRR, equity, FX, commodity, credit); the capital charge is a Basel-set weighted average of the total ES and the **sum of partial ESs** (which is always ≥ the total ES, since it eliminates diversification across categories).

- **Backtesting under FRTB**: cannot back-test a 10-day ES directly and cannot back-test stressed measures at all. Back-test a **1-day VaR** over the most recent 12 months at both 99% and 97.5%; the exceptions set the multipliers.

- **Trading vs banking book discipline (book)**: intent to trade is no longer sufficient — the bank must be able to trade *and* manage the risk on a trading desk, with day-to-day value changes hitting equity. Assignment is made at **initiation**; transfers only in extraordinary circumstances; **any capital benefit from a transfer is disallowed**.

- **Splitting credit trades (book)**: (1) **credit spread risk** → treated like other market risks under the new ES machinery; (2) **jump-to-default risk** → separate **IDR** charge, a one-year 99.9% VaR over all default-risk instruments *including equities*, computed like Basel II banking-book credit capital, with anti-double-counting so the IDR loss is incremental to mark-to-market spread loss.

## Key Concepts
1. **Expected shortfall** — the average loss in the tail beyond the confidence quantile; coherent, unlike VaR.
2. **Stressed period** — a 250-day window chosen to be maximally adverse for the *current* portfolio, not a fixed historical window.
3. **Liquidity horizon** — the time needed to exit or hedge a risk in stress; it sets the shock window.
4. **Overlapping windows** — cheap to implement, statistically inefficient (correlated trials).
5. **Partial ES / diversification cap** — prevents a bank from gaming cross-risk-class diversification.
6. **NMRF** (2019 addition) — risk factors with insufficient data to model; get an add-on.
7. **Curvature risk** (2019 addition) — the convexity of vega; requires PLA.
8. **DRC** — default risk charge, the 2019 successor to IRC/IDR.
9. **Constant level of risk** — the assumption FRTB removes.
10. **Anti-double-counting** — spread loss and default loss must not overlap.
11. **CVA as a stand-alone charge** — the book concludes CVA counterparty-spread risk stays outside the ES framework (Basel III/FRTB kept it as a separate capital charge).

## Formulas & Reference Tables

Eq. (17.1): `ES = √ES₁ + √( Σ_{j=2}^{5} [ (ES_j − ES_{j−1})·(LH_j − LH_{j−1}) / 10 ] )`, where `LH_j` is the liquidity horizon for category `j`.

Table 17.1 — book (Dec 2014 draft) liquidity horizons

| Market variable | Horizon (days) |
|---|---|
| Interest rate (EUR, USD, GBP, AUD, JPY, SEK, CAD) | 10 |
| Interest rate (other) | 20 |
| Interest rate ATM vol | 60 |
| Credit spread: sovereign IG / sovereign non-IG | 20 / 60 |
| Credit spread: corporate IG / corporate non-IG | 60 / 120 |
| Credit spread: structured product | 250 |
| Equity price: large cap / small cap | 10 / 20 |
| Equity price ATM vol: large cap / small cap | 20 / 120 |
| FX: liquid pairs / other pairs / FX vol | 10 / 20 / 60 |
| Energy / precious metal / other commodity price | 20 / 20 / 60 |
| Energy / precious metal / other commodity ATM vol | 60 / 60 / 120 |

Normal-distribution equivalence (both figures verified): `VaR_99 = μ + 2.3263σ`; `ES_97.5 = μ + 2.3378σ`; `ES_99 = μ + 2.6652σ`.

## Mental Models
- **A risk that cannot be exited in 10 days should not be capitalised as if it can.** Liquidity horizons are the whole economic content of FRTB.
- **ES only beats VaR in the tail.** Under normality the two differ by 0.5%. If your sample has 250 obs, you have roughly 6 tail points at 97.5% — the estimator is noisy whatever you use.
- **Diversification across risk classes is capped, not free.** Summing partial ESs removes cross-category offsetting on purpose.
- **The stress window is a discretionary surface until the regulator pins it.** Any bank-specific stressed-period choice is a place where two desks' numbers will disagree.

## Code Examples
`⚠ reconstructed` — five-bucket ES aggregation and the √-time-scaling logic of eq. (17.1).

```python
import numpy as np

def aggregate_es(es_by_bucket, lh):
    """es_by_bucket: ES_j computed with categories >= j shocked (10-day basis).
       lh: liquidity horizons [10,20,60,120,250] in days."""
    es = np.asarray(es_by_bucket, dtype=float)
    lh = np.asarray(lh, dtype=float)
    total = np.sqrt(es[0])                      # sqrt(ES_1)
    for j in range(1, len(es)):
        total += np.sqrt((es[j] - es[j - 1]) * (lh[j] - lh[j - 1]) / 10.0)
    return total

# sanity: all variables on the 10-day bucket -> total = sqrt(ES_1)
print(round(aggregate_es([50, 50, 50, 50, 50], [10, 20, 60, 120, 250]), 3))

# normal-distribution checks quoted in the chapter
from statistics import NormalDist as ND
print(round(ND().inv_cdf(0.99), 4), round(ND().pdf(ND().inv_cdf(0.975))/0.025, 4))
```

## Worked Example

**Eq. (17.1) aggregation (recomputed).** A desk shocks 10-day changes and gets `ES₁…ES₅ = 40, 42, 46, 52, 60` (in $m) with horizons `[10, 20, 60, 120, 250]`.
`√ES₁ = √40 = 6.325`.
Bucket 2: `√[(42−40)(20−10)/10] = √2 = 1.414`.
Bucket 3: `√[(46−42)(60−20)/10] = √16 = 4.000`.
Bucket 4: `√[(52−46)(120−60)/10] = √36 = 6.000`.
Bucket 5: `√[(60−52)(250−120)/10] = √104 = 10.198`.
**Total ES = 27.94 $m.**
Interpretation: the illiquid buckets contribute 21.6 of 27.94 (77%) despite only moving from 40 to 60 in the underlying ESs. That is FRTB in one line — the capital is set by what you cannot trade, not by what you can.

## Anti-patterns
- Running FRTB ES on a single current (non-stressed) window.
- Using one-day shocks scaled by √10 for factors with a 120- or 250-day horizon.
- Treating overlapping historical trials as independent — this silently understates estimation uncertainty.
- Believing a market-risk model is "validated" because the historical backtest shows no exceptions; a model calibrated on calm data will pass on calm data.
- Assuming the total ES is the right capital number and ignoring the partial-ES diversification cap.
- Keeping credit spread and jump-to-default in one model and then double counting, or worse, dropping jump-to-default entirely.
- Re-designating instruments from banking book to trading book opportunistically (the book explicitly disallows the capital benefit).

## Practitioner Notes
- **Validation duties for an FRTB-style engine**: (a) demonstrate the stress-period selection procedure is documented, reproducible and genuinely adverse for the current portfolio; (b) prove the overlap-induced autocorrelation has not invalidated confidence intervals on the tail average; (c) attribute P&L by risk factor (the 2019 PLA requirement) and reconcile attribution residuals back to `>0` tolerance; (d) run the mandated sensitivity/stress tests for NMRF and curvature in the 2019 standard.
- FRTB's economics punish specific strategies: carry in off-the-run credit, illiquid structured credit, and basis trades in slow-moving indices. Expect flow consequences, not just capital consequences.
- Deferred EU implementation (1 Jan 2028) means many European desks still run Basel II.5 today — do not assume a reported number is FRTB; **ask which standard the number is under**.

## Key Takeaways
1. FRTB replaces 10-day 99% VaR with **97.5% ES on a 12-month stressed period** and variable liquidity horizons.
2. Five bucket-level ESs aggregate via eq. (17.1); √-time-scaling is assumed for the 40-, 60- and 130-day legs.
3. Overlapping windows are cheaper but statistically inefficient — noise, not bias.
4. Capital is the **weighted average of total ES and the sum of partial ESs**, so cross-risk-class diversification is capped.
5. Back-testing is on **1-day VaR at 99% and 97.5% over 12 months**; stressed measures cannot be back-tested at all.
6. Trading-book status now requires active desk-level risk management, is fixed at initiation, and transfers bring **no capital benefit**.
7. Credit trades split into spread risk (market risk) and jump-to-default risk (IDR/DRC), with constant level of risk abolished.
8. ⚠ The binding standard is **BCBS d457 (January 2019)** with curvature risk, NMRF add-ons, DRC, and a redesigned standardised approach — all absent from this chapter. See `frtb-market-risk-bcbs457`.

## Connects To
- **ch 16**: Basel II.5 stressed VaR and IRC, the two components FRTB inherits and restructures.
- **ch 15**: eq. (15.3) `max(VaR_{t−1}, m_c·VaR_avg) + SRC` — the formula FRTB deletes.
- **ch 20**: CVA, explicitly kept as a stand-alone charge under FRTB.
- **ch 25**: model risk — the single most important chapter for anyone running a FRTB engine.
- **ch 28**: mistakes to avoid, including model risk and stress-testing errors.
- **`frtb-market-risk-bcbs457`**: the binding 2019 standard — mandatory reading before implementing any of the above.
- **`hull-derivatives`**: P&L attribution and vega/gamma/curvature decomposition of a book.
- **`gatheral-volatility-surface`**: the ATM-vol risk factors and liquidity horizons that surface risk feeds.
