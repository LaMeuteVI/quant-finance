# Chapter 16: Basel II.5, Basel III, and Other Post-Crisis Changes
> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed., Wiley 2012 | Ch. 16, pp. 353–372

## Core Idea
The 2007–2009 crisis exposed three specific design errors: market-risk capital was calibrated on a 2003–2006 low-volatility sample; credit risk could be moved to the trading book for a capital discount; and internal model discretion (PD/LGD/EAD) was unchecked. Basel II.5 fixed market risk and credit arbitrage; Basel III rebuilt the capital stack, added a leverage ratio and two liquidity ratios, and made CVA a market risk.

## Frameworks Introduced

- **Basel II.5 stressed VaR (implemented 31 Dec 2011)**: capital = `max(VaR_{t−1}, m_c·VaR_avg) + max(sVaR_{t−1}, m_s·sVaR_avg)`, with `m_c, m_s ≥ 3`, 10-day 99%, both legs averaged over the previous 60 days. Stressed window = a 250-day (12-month) period chosen to be particularly stressful *for the bank's own current portfolio*.
  - *When to use*: reproducing pre-FRTB IMA capital; designing a stressed-window selection procedure.
  - *Why it works*: it removes the low-vol dependency of the unstressed leg.
  - *Failure mode*: the "stressed period" is discretionary and portfolio-specific — two banks can report different multipliers from identical data. This is exactly the arbitrage FRTB closes with a mandated 2007-onward search period.

- **Incremental Risk Charge (IRC, 2009; superseded the 2005 IDRC)**: one-year 99.9% VaR of credit-sensitive trading-book instruments, covering **both** credit-migration and default risk, with capital = max(trading-book charge, banking-book charge). Constant-level-of-risk: after the liquidity horizon (min 3 months) a deteriorated position is assumed replaced.
  - *Failure mode*: constant-level-of-risk understates a book that cannot be rebalanced — the assumption directly violated in 2008. FRTB abolished it (ch 17).

- **Comprehensive Risk Measure (CRM)**: a single charge replacing IRC + SRC for correlation-dependent instruments (ABS, CDO). Standardised charges by external rating (Table 16.1). Internal-model version must capture cumulative multi-default, spread risk, implied-correlation volatility, the spread/correlation relationship, recovery-rate volatility, hedge slippage and rebalancing cost, plus a rigorous stress programme, and is floored at the standardised charge.

- **Basel III capital stack**: Tier 1 equity + Additional Tier 1 + Tier 2. **Tier 3 eliminated.** Minimum ratios: CET1 4.5%, Tier 1 6%, total 8% — plus a **capital conservation buffer of 2.5% of RWA in CET1** (→ 7% / 8.5% / 10.5% in normal times), and a **countercyclical buffer of 0–2.5%** set by national authorities.
- **Dividend restrictions**: below the buffer stack, minimum retained earnings rise in 20% steps — 100% / 80% / 60% / 40% / 0% as CET1 crosses 4.00–5.125 / 5.125–5.75 / 5.75–6.375 / 6.375–7.00 / >7.00% RWA (with a 2.5% countercyclical buffer the grid shifts to 4.50/5.75/7.00/8.25/9.50%).
- **Leverage ratio**: `LR = Tier 1 capital / exposure`, exposure = on-balance-sheet + derivative RC + add-on + SFT + off-balance-sheet items, no risk weighting. Minimum 3% (Basel, effective 1 Jan 2018).
- **LCR** (1 Jan 2015 → 2019 phasing, HQLA / net cash outflows over 30 days, ≥ 100%) and **NSFR** (`ASF / RSF ≥ 100%`).
- **G-SIB surcharge**: additional Tier 1 of 1%, 1.5%, 2%, 2.5% or 3.5% of RWA, effective January 2016; TLAC 16–18% rising to 18–20% of RWA.
- **CoCo (contingent convertible bond)**: automatically converts to equity when the trigger is hit — typically CET1/RWA below 7%, or MPT below 22.5%. Conversion is a **bail-in**.

## Key Concepts
1. **Stressed VaR** — VaR calibrated on a mandated 250-day stress window rather than the trailing 1–4 years.
2. **Constant level of risk** — the IRC's assumption that deteriorated positions are replaced at the liquidity horizon.
3. **Correlation book** — ABS/CDO tranches sensitive to inter-asset default correlation, where correlation spikes to 1 in stress.
4. **Securitisation vs resecuritisation charges** — CRM charges roughly double for resecuritisation (e.g. 1.6% → 3.2% at AAA–AA−), reflecting the crisis experience.
5. **Capital conservation buffer** — 2.5% of CET1 above the 4.5% minimum, giving 7% effective CET1.
6. **Countercyclical buffer** — national 0–2.5%, released in booms, drawn down in stress.
7. **Leverage ratio** — non-risk-weighted backstop against model and RWA discretion.
8. **G-SIB / SIFI / D-SIB** — systemic buckets with escalating surcharges and disclosure.
9. **TLAC** — total loss-absorbing capacity, 16–20% of RWA and ≥ 2× the Tier 1 leverage minimum.
10. **NSFR stable-funding weights** — retail deposits 90–100%, wholesale 50%, capital 100%; RSF 0–100% by residual maturity and rating.
11. **CVA as market risk** — Basel III moved counterparty-spread CVA risk into market risk capital.
12. **Volcker rule** — proprietary trading restricted; some high-risk trading spun into separately capitalised affiliates.
13. **SEF / OTF** — swap execution facilities (US) vs organised trading facilities (EU, less dogmatic).
14. **Unintended consequences** — Basel I's 100% risk weight discouraged lending to high-quality corporates; every rule creates a second-order behaviour.

## Formulas & Reference Tables

Basel II.5 capital: `K = max(VaR_{t−1}, m_c·VaR_avg) + max(sVaR_{t−1}, m_s·sVaR_avg)`, `m_c, m_s ≥ 3`.

NSFR: `NSFR = ASF / RSF ≥ 100%`. Recomputed Example 16.1: ASF = `40×0.9 + 48×0.5 + 4×1.0 + 8×1.0 = 72.0`; RSF = `5×0 + 5×0.05 + 20×0.65 + 60×0.85 + 10×1.0 = 74.25`; **NSFR = 0.970 (97.0%) → breach**.

Table 16.1 — CRM standardised capital charge (book, 2011 revisions)

| External assessment | AAA–AA− | A+ to A− | BBB+ to BBB− | BB+ to BB− | < BB− or unrated |
|---|---|---|---|---|---|
| Securitisation | 1.6% | 4% | 8% | 28% | Deduction |
| Resecuritisation | 3.2% | 8% | 18% | 52% | Deduction |

Leverage ratio: `Tier 1 / (on-BS + deriv RC+add-on + SFT + off-BS) ≥ 3%`.

## Mental Models
- **Regulators regulate the last crisis, and only the last crisis.** Basel II.5 targets 2008; FRTB targets 2007–2009 correlation spikes; each rule is a scar from the previous failure.
- **The buffer is the real capital ratio.** Anyone quoting "4.5% CET1" is describing a bank that is 2.5 percentage points from mandatory dividend restrictions.
- **Leverage ratio is a discipline device, not a risk measure.** It will bind on low-RWA business models (mortgages, sovereigns), which is precisely where RWA discretion is largest.
- **Liquidity rules are balance-sheet-shape rules.** NSFR forces term funding; LCR forces liquid assets. Both shrink carry trades.

## Code Examples
`⚠ reconstructed` — NSFR and dividend-restriction grids.

```python
def nsfr(funding, assets):
    """funding/assets: dicts of amount -> ASF / RSF weight."""
    ASF = sum(a * w for a, w in funding.items())
    RSF = sum(a * w for a, w in assets.items())
    return ASF, RSF, (ASF / RSF if RSF else float("nan"))

ASF, RSF, r = nsfr({40: 0.9, 48: 0.5, 4: 1.0, 8: 1.0},
                   {5: 0.0, 5: 0.05, 20: 0.65, 60: 0.85, 10: 1.0})
print(ASF, RSF, round(r, 4))          # 72.0 74.25 0.9697  -> breach

def min_retained(cet1_ratio, ccb=0.0):
    lo = 4.5 + ccb
    for edge, ret in [(lo + 1.125, 1.00), (lo + 2.25, 0.80),
                      (lo + 3.375, 0.60), (lo + 4.50, 0.40)]:
        if cet1_ratio < edge:
            return ret
    return 0.0

print(min_retained(0.06, 0.0), min_retained(0.06, 0.025))   # 0.80 / 1.00
```

## Worked Example

**Basel II.5 versus Basel I/II.5-previous market risk.** Take a bank with average 10-day 99% VaR of 100 and previous-day VaR of 95, `m_c = 3`. Under the 1996 Amendment the first leg is `max(95, 3×100) = 300`. If the stressed window is genuinely worse — `sVaR_avg = 180`, `sVaR_{t−1} = 175`, `m_s = 3` — the second leg is `max(175, 540) = 540`. **Total 840 versus 300 pre-Basel II.5: a 2.8× increase**, and with `m_c = m_s` the rule is at least a doubling because `sVaR ≥ VaR` by construction. That is the entire economic content of the 2011 market-risk reform, and the reason FRTB went further.

**Recomputed NSFR (Example 16.1).** ASF = 72.0, RSF = 74.25, NSFR = 97.0% < 100% → the bank fails the Basel III stable-funding test despite a balanced balance sheet. A bank with too much short-term wholesale funding relative to its long-dated assets fails even with no marked risk.

## Anti-patterns
- Treating the Basel II.5 stressed period as a fixed historical window (2008) rather than a portfolio-specific selection — that is what the 2013 clarification prohibited.
- Applying constant level of risk to a book that cannot be rebalanced within the liquidity horizon.
- Computing liquidity ratios on average balances in benign periods.
- Quoting Basel III minimums without the conservation and countercyclical buffers.
- Assuming the stressed VaR and VaR legs are independent — Basel II.5 **adds** them.
- Believing higher capital requirements raise expected bank ROE. The chapter's own point: extra equity lowers risk, so ROE falls versus the 1990–2006 period.

## Practitioner Notes
- The book's stress windows, buffers and surcharges are **2012-vintage and superseded**. The binding rules as of 2026 are Basel III "endgame" (`BCBS d424`, Dec 2017, output floors and revised IRB, EU phase-in 2025–2032), **CRR3** in the EU, UK implementation diverging post-Brexit, and the **2019 FRTB deferral to 1 January 2027/2028** in the EU. Use this chapter for the *logic* of the fixes and the historical calibration data, never for live limits.
- CVA is now explicitly a market-risk capital item; see ch 20 for the mechanics and ch 21 for credit VaR on the underlying exposures.
- The Dodd-Frank list of 20 provisions (Section 16.4) is a useful checklist of post-crisis policy levers: resolution authority, living wills, FSOC/OFR systemic monitoring, 5% securitisation retention (10% in Germany), rating-agency liability, ability-to-repay underwriting, SIFI designation.

## Key Takeaways
1. Basel II.5 = stressed VaR (10-day 99%, 250-day stress window) + IRC (1y 99.9%, incl. migration) + CRM for the correlation book; effective 31 Dec 2011.
2. Basel III raised the effective CET1 requirement from 4.5% to 7% and eliminated Tier 3.
3. The dividend grid is the enforcement mechanism: below 7.0% CET1 (no countercyclical buffer) banks must retain 40–100% of earnings.
4. The 3% leverage ratio caps RWA discretion; the G-SIB surcharge adds up to 3.5% CET1 on top.
5. LCR ≥ 100% and NSFR ≥ 100% convert liquidity risk into balance-sheet constraints.
6. CVA enters market risk capital, closing a gap where counterparty-spread risk sat outside the market-risk framework.
7. Every post-crisis rule is a scar; anticipate the next one by looking at what broke last.
8. Unintended consequences are systematic, not incidental — track where capital can be arbitraged next.

## Connects To
- **ch 15**: the Basel I/II machinery these rules replace — read together to see each fix mapped to its failure.
- **ch 17**: FRTB is the successor to the stressed VaR leg described here; see the practitioner-update box there.
- **ch 20**: CVA as market risk, and the DVA/capital-interaction questions Basel III raised.
- **ch 23**: operational risk capital under Basel II (BIA/SA/AMA) versus the post-crisis expectations.
- **ch 24**: LCR/NSFR in full, plus the mismatch that drives fire-sale risk.
- **ch 26**: economic capital and RAROC — the internal counterpart to all of these buffers.
- **`frtb-market-risk-bcbs457`**: the binding 2019 market-risk standard.
- **`cfa-fixed-income` / `cfa-portfolio-management`**: buffer-driven de-risking mechanics for institutional portfolios.
