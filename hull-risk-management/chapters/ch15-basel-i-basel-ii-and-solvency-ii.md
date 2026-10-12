# Chapter 15: Basel I, Basel II, and Solvency II
> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed., Wiley 2012 | Ch. 15, pp. 325–352

## Core Idea
Regulation exists to force banks to hold capital commensurate with risk, because deposit insurance alone destroys the disciplining pressure that would otherwise stop banks from levering up. The chapter traces the arc 1988 Basel I → 1996 Amendment (market risk) → Basel II (three pillars, IRB) → Solvency II, and ends on the structural logic that will later produce Basel II.5/III and FRTB (chs 16–17).

## Frameworks Introduced

- **Basel I credit-equivalent amount**: `CEA = Σ_i [ max(V_i, 0) + a_i·L_i ]`, where `V_i` is the mark-to-market value of trade `i`, `a_i` the add-on factor (0–7% by maturity and product), `L_i` the principal. Capital = 8% × risk-weighted assets, risk weight set by external rating (0%, 20%, 50%, 100%).
  - *When to use*: reproducing legacy Basel I / CEM-style EAD, or bounding a netting dispute.
  - *Why it works*: forces recognition of both current positive replacement cost and potential future exposure.
  - *Failure mode*: the add-on ignores the distribution of `V`, so two identical trades with `V = +10m` and `V = −10m` get identical capital. Regulators responded in 2014 with SA-CCR (`EAD = 1.4·(RC + PFE)`).

- **Basel I netting formula (1995 amendment)**: `CEA_net = max(Σ V_i, 0) + (0.4 + 0.6·NRR)·Σ a_i L_i`, with net replacement ratio `NRR = max(Σ V_i, 0) / Σ max(V_i, 0)`.
  - *When to use*: quantifying the capital benefit of an enforceable ISDA master agreement.
  - *Failure mode*: only correct if the netting set is enforceable and the replacement cost is floored at zero for the whole set.

- **1996 Amendment market-risk capital (IMA)**: `K = max(VaR_{t−1}, m_c · VaR_avg) + SRC` (eq. 15.3), `m_c ≥ 3`, `VaR` = 10-day 99%. Equivalent to `m_c·√10 = 9.49` × average 1-day 99% VaR at `m_c = 3`. SRC model multiplier ≥ 4 with a floor of 50% of the standardised SRC.
  - *When to use*: legacy VaR-to-capital translation, backtesting design.
  - *Failure mode*: `√10` scaling assumes IID returns — it understates capital in crises and for illiquid books.

- **Basel II IRB capital formula**: `K = EAD × LGD × (WCDR − PD) × MA` (eq. 15.9), `RWA = 12.5 × K`.
  - `WCDR = N( [ N⁻¹(PD) + √ρ·N⁻¹(0.999) ] / √(1−ρ) )` (eq. 15.6) — the one-factor Gaussian "worst-case default rate" at the 99.9% quantile, `N` = standard normal CDF, `N⁻¹` = inverse CDF. Verified: reproduces the book's Table 15.5 exactly.
  - Corporate/sovereign/bank correlation (eq. 15.8, `CRE32.21`): `ρ = 0.12(1 − e^{−50·PD}) + 0.24(1 − e^{−50·PD})/(1 − e^{−50})`.
  - Retail correlation (eq. 15.11, `CRE32.23`): `ρ = 0.03 + 0.13·e^{−35·PD}`; residential mortgages `ρ = 0.15`; qualifying revolving `ρ = 0.04`.
  - Maturity adjustment (eq. 15.10): `MA = [1 + (M − 2.5)·b] / (1 − 1.5·b)`, `b = [0.11852 − 0.05478·ln(PD)]²`, `M` = remaining maturity in years. `MA = 1` when `M = 1`.
  - *When to use*: any PD/LGD-driven credit capital or RWA calculation; building internal rating models.
  - *Failure mode*: Gordy's asymptotic (eq. 15.6) is **not** the Basel KIRB formula. The binding Basel form is `N([(1−ρ)N⁻¹(PD) + ρ·N⁻¹(0.999)] / √(ρ² + (1−ρ)²))`, which is materially *lower* (e.g. at PD = 1%, ρ = 0.1417: KIRB WCDR = 3.66% vs 10.5% under eq. 15.6). Use the KIRB form for regulatory reporting and eq. 15.6 for conservative internal stress. ⚠ Correction.

- **Basel II three pillars**: Pillar 1 minimum ratios; Pillar 2 supervisory review (4 principles: internal ICA + capital plan; supervisor evaluates ICA; supervisors expect banks to operate above the minimum and can require more; early intervention); Pillar 3 market discipline (scope of application; terms of capital instruments; Tier 1 components; total Tier 2; capital requirements by risk type; risk-management structure).

- **Basel II standardised approach credit**: 20 buckets, external ratings → risk weights, 125% risk weight if the rating criterion is breached.

- **Solvency II**: MCR (absolute floor, typically 25–45% of SCR; breach can block new business or force liquidation) and SCR (above SCR, a restoration plan is required). Same three-pillar architecture as Basel II.

## Key Concepts
1. **Systemic risk** — one institution's default cascading through bilateral OTC exposures into system failure; the reason banks are bailed out and therefore under-regulated ex ante.
2. **Deposit insurance moral hazard** — insurance makes depositors less discriminating, so capital regulation is the necessary complement.
3. **Banking book vs trading book** — held-to-maturity at historical cost (credit-risk capital) vs marked-to-market daily (market-risk capital). The book assignment is the single largest regulatory-arbitrage lever in the whole framework.
4. **Regulatory arbitrage** — deliberately choosing the asset form (loan vs bond, banking book vs trading book, jurisdiction) that minimises risk-weighted assets without changing economic risk.
5. **Expected loss (EL)** — `EL = Σ EAD_i·LGD_i·PD_i`; must be covered by pricing, not by capital.
6. **Unexpected loss (UL)** — what capital must absorb: `Σ EAD_i·LGD_i·(WCDR_i − PD_i)`.
7. **PD floor** — 0.03% for bank and corporate exposures under both F-IRB and A-IRB.
8. **LGD supervisory values** — 45% senior, 75% subordinated (F-IRB); reduced by eligible collateral under the comprehensive approach.
9. **EAD** — supervisory (F-IRB) or model-based with approval (A-IRB); typically Monte Carlo over the next year with netting and collateral.
10. **Maturity adjustment** — recognising that a longer-dated exposure also carries one year's downgrade risk on top of default risk.
11. **Backtesting** — 250 one-day VaR exceptions; ≥ 5 exceptions forces `m_c` up. Probability of ≥ 5 exceptions under a correctly specified 99% VaR = **10.78%** (recomputed: `1 − Binom(250, 0.01) ≤ 4`). So the effective regulator confidence level on the backtest is ~10%, not 5%.
12. **Credit substitution vs double default** — credit substitution overstates risk (requires both guarantor and borrower to default); the Basel II alternative is `K = K_unguaranteed × (0.15 + 160·PD_g)`.
13. **Operational risk capital (Basel II)** — BIA: 15% × 3-year average positive gross income; SA: line-specific gross-income coefficients; AMA: 99.9% one-year loss minus expected loss, with insurance credit.
14. **Guarantee treatment** — a claim on a guarantor is risk-weighted as if made to the guarantor.

## Formulas & Reference Tables

| Basel I add-ons | Maturity | `a` |
|---|---|---|
| FX forwards/swaps/options | ≤ 1y / ≤ 1y / ≤ 1y | 1.6% / 1.6% / 1.6% |
| Interest rate | ≤ 1y / 1–5y / > 5y | 0.5% / 1.0% / 1.5% |
| Interest rate options | ≤ 1y / 1–5y / > 5y | 0.6% / 1.2% / 1.8% |
| Equity | ≤ 1y / 1–5y / > 5y | 1.0% / 2.0% / 3.0% |
| Commodity | other / metals / electricity | 1.8% / 3.0% / 6.0% |

Table 15.5 (verified, exact): one-year 99.9% `WCDR` from eq. (15.6), `N⁻¹(0.999) = 3.0902`

| `ρ` \ PD | 0.1% | 0.5% | 1% | 1.5% | 2% |
|---|---|---|---|---|---|
| 0.0 | 0.1% | 0.5% | 1.0% | 1.5% | 2.0% |
| 0.2 | 2.8% | 9.1% | 14.6% | 18.9% | 22.6% |
| 0.4 | 7.1% | 21.1% | 31.6% | 39.0% | 44.9% |
| 0.6 | 13.5% | 38.7% | 54.2% | 63.8% | 70.5% |
| 0.8 | 23.3% | 66.3% | 83.6% | 90.8% | 94.4% |

Table 15.7 (retail, verified exactly with `ρ = 0.03 + 0.13e^{−35PD}`): WCDR = 2.1% / 6.3% / 9.1% / 11.0% / 12.3% at PD = 0.1% / 0.5% / 1% / 1.5% / 2%.

⚠ **Note on the book's Table 15.6** (corporate): the printed WCDR values 3.4% / 9.8% / 14.0% / 16.9% / 19.0% are reproduced *exactly* by eq. (15.6) using `ρ = 0.12 + 0.12·e^{−50·PD}` (0.2341 / 0.2135 / 0.1928 / 0.1767 / 0.1641; back-solved from the table: 0.2331 / 0.2140 / 0.1924 / 0.1772 / 0.1639). They are **not** reproduced by eq. (15.8) as printed, which gives 0.3% / 3.8% / 10.5% / 18.0% / 25.5%. Bind on `CRE32.21` and the KIRB conditional formula, not on Table 15.6.

## Mental Models
- **Deposit insurance without capital rules ⇒ more risk, not less.** Use it whenever arguing that regulation is unnecessary.
- **Book assignment is a free option.** Use trading book when IRC/IDR is weak, banking book when the credit capital is low. Expect the regulator to close the gap (it did, twice).
- **Correlation is the whole story in credit capital.** At `ρ = 0` capital ≈ EL (nothing to hold); at `ρ = 0.8` a 1% PD book needs a 83.6% worst-case default rate. Diversification benefit is entirely a function of assumed correlation.
- **Twelve-point-five.** Every IRB result multiplies by 12.5 because 1/0.08 = 12.5 — RWA is the capital grossed up to a 8% ratio. This is a units conversion, not risk.

## Code Examples
`⚠ reconstructed` — reproduce the Basel I netting benefit and the IRB RWA chain.

```python
from math import exp, log, sqrt
from statistics import NormalDist as ND
N, Ninv, Z99 = ND().cdf, ND().inv_cdf, ND().inv_cdf(0.999)

def basel_i_cea(trades, netting=True):
    """trades: list of (V_i, addon_i). Basel I CEA with/without netting."""
    V = [v for v, _ in trades]; A = [a for _, a in trades]
    if not netting:
        return sum(max(v, 0.0) for v in V) + sum(A)
    nrr = max(sum(V), 0.0) / sum(max(v, 0.0) for v in V)  # guard divide-by-zero
    return max(sum(V), 0.0) + (0.4 + 0.6 * nrr) * sum(A)

def wcdr_hull15_6(PD, rho):
    """Gordy asymptotic one-factor WCDR, eq (15.6)."""
    return N((Ninv(PD) + sqrt(rho) * Z99) / sqrt(1 - rho))

def rho_corporate(PD):   # Basel CRE32.21
    return 0.12 * (1 - exp(-50 * PD)) + 0.24 * (1 - exp(-50 * PD)) / (1 - exp(-50))

def rho_retail(PD):      # Basel CRE32.23
    return 0.03 + 0.13 * exp(-35 * PD)

def wcdr_kirb(PD, rho):  # the binding Basel KIRB conditional form
    return N(((1 - rho) * Ninv(PD) + rho * Z99) / sqrt(rho ** 2 + (1 - rho) ** 2))

def maturity_adj(PD, M):
    b = (0.11852 - 0.05478 * log(PD)) ** 2
    return (1 + (M - 2.5) * b) / (1 - 1.5 * b)

def capital_rwa(EAD, PD, LGD, M, retail=False, rho=None):
    r = rho if rho is not None else (rho_retail(PD) if retail else rho_corporate(PD))
    ma = 1.0 if retail else maturity_adj(PD, M)
    K = EAD * LGD * (wcdr_kirb(PD, r) - PD) * ma     # use wcdr_hull15_6 for conservative internal
    return K, 12.5 * K

print(basel_i_cea([(-60, 5), (70, 75), (55, 30)]))      # 143.32  (no netting: 235)
print(capital_rwa(100, 0.001, 0.6, 2.5))                # (3.19, 39.3) with eq 15.6 WCDR
```

## Worked Example

**(a) Basel I netting benefit (recomputed, matches the book).** Portfolio: 3y IRS principal 1,000, value −60, add-on 5; 6y FXF 1,000 / +70 / 75; 9m equity option 500 / +55 / 30.
`max(ΣV,0) = 65`; `Σmax(V,0) = 125` → `NRR = 0.52`; `Σa_iL_i = 110`.
`CEA_net = 65 + (0.4 + 0.6×0.52)×110 = 65 + 0.712×110 = 143.32`. Without netting: `125 + 110 = 235`.
At a 0.2 risk weight: RWA `28.66` vs `47.00`; capital at 8%: `2.29` vs `3.76`. **Netting cuts counterparty capital by 39%** — the entire economic content of the ISDA master agreement.

**(b) Basel II IRB RWA (recomputed, matches Example 15.7).** $100m of A-rated corporate loans, `PD = 0.1%`, `LGD = 60%`, `M = 2.5`.
`b = [0.11852 − 0.05478·ln(0.001)]² = 0.2469`; `MA = 1/(1 − 1.5×0.2469) = 1.588`.
Using the book's Table 15.6 `WCDR = 3.4%`: `RWA = 12.5 × 100 × 0.6 × (0.034 − 0.001) × 1.588 = 39.31`.
Interpretation: same loan book → **Basel I $100m RWA, Basel II SA $50m, Basel II IRB $39.3m**. The whole point of IRB is that the bank's own PD model, plus correlation and MA, produce a capital number far below the ratings-based one.

## Anti-patterns
- Multiplying by 12.5 and forgetting the 8% — RWA and capital are not the same number.
- Using a rating-based risk weight for an internally rated obligor, then calling the result "Basel II IRB".
- Treating `WCDR` as a "1-in-1000-year default rate that will occur" — it is a *cross-sectional worst case in a correlated portfolio*, not a time-series frequency.
- Applying `√10` to a 10-day stressed window, or to a portfolio with fat tails (this is precisely the flaw FRTB fixes — see ch 17).
- Assuming `MA > 1` is conservative. For long-maturity exposures `MA` scales up capital, but the offsetting fact — that the exposure amortises — is ignored in a static calc.
- Setting ρ = 0 for a large single-sector portfolio to make capital look small.

## Practitioner Notes
- Every IRB input is a *supervisory* claim. Validation duties: backtest PD against realised defaults with a binomial/G-test over the rating migration matrix (see ch 19); verify LGD against realised recoveries haircut for collateral haircuts and workout time; stress EAD on a stressed-Markov path.
- The 12.5 multiplier means `RWA` is only as good as `PD`. A 1% PD error on a large A-rated book moves more capital than the entire market-risk charge.
- Basel II was live during 2007–2009; the crisis predates full implementation (US banks lagged), so don't attribute procyclicality to IRB alone — low-vol calibration of market VaR was the bigger proximate cause.

## Key Takeaways
1. Capital regulation exists because deposit insurance breaks depositor discipline; the tool is the 8% × RWA identity.
2. Basel I = current exposure + add-on; netting is worth ~39% of counterparty capital when the replacement ratio is 0.52.
3. Basel II credit capital = `EAD × LGD × (WCDR − PD) × MA`, grossed up by 12.5.
4. Correlation `ρ` drives the entire tail: WCDR goes from PD at `ρ=0` to ~84% for a 1% PD book at `ρ=0.8`.
5. Backtest tolerance is 5 exceptions in 250 — a 10.78% event under a correct model, i.e. a ~10% confidence standard.
6. Basel II's three pillars are a control system, not a formula: minimum capital, supervisory review, market discipline.
7. Solvency II reuses the same architecture with MCR/SCR; the MCR ≈ 25–45% of SCR is the binding early-warning level.
8. Regulatory arbitrage between the banking and trading books was structural, not accidental — expect it and price it into any strategy that depends on bank balance-sheet capacity.

## Connects To
- **ch 16**: Basel II.5 and Basel III are the post-crisis repair of exactly the vulnerabilities identified here (VaR calibration, trading-book arbitrage, credit-model discretion).
- **ch 17**: FRTB replaces the Basel I/II.5 10-day 99% VaR machinery (eq. 15.3) with stressed expected shortfall at variable liquidity horizons.
- **ch 19**: estimating the `PD` input that drives eq. (15.9) — Merton model, hazard rates, transition matrices.
- **ch 21**: credit VaR applied to bonds and credit derivatives, building on the `WCDR` machinery.
- **ch 25**: model risk — IRB models are exactly the kind of internally estimated model whose failure ch 25 catalogues.
- **`frtb-market-risk-bcbs457` ch on ES**: the binding 2019 market-risk standard that supersedes the framework in this chapter.
- **`hull-derivatives`**: netting sets, collateral, and ISDA/CSA mechanics behind the `NRR` formula.
