# Chapter 6: Fundamentals of Credit Analysis
> **Source**: CFA Program Curriculum 2019/2020, Level I, Reading 47 · Fixed Income | Christopher L. Gootkind, CFA (Loomis Sayles)

## Core Idea
Credit risk is the risk of not being paid in full and on time; it is measured by **expected loss = default probability × loss severity**. Analysts assume willingness to pay (bonds are contracts) and concentrate on **ability to pay**: sustainable cash flow versus debt, framed by the four Cs, ratios, and where the bond sits in the capital structure. The market prices this as a spread whose price impact is ≈ −MDur × ΔSpread; the lower the quality, the more recovery, liquidity, covenants and structure matter.

## Learning Outcomes Covered
- Describe credit risk and credit-related risks (spread, migration, market liquidity) for corporate bonds
- Describe default probability and loss severity as the components of credit risk
- Describe seniority rankings; explain how priority of claims can be violated in bankruptcy
- Distinguish issuer vs issue ratings; describe notching
- Explain the risks of relying on rating agencies
- Explain the four Cs (Capacity, Collateral, Covenants, Character)
- Calculate and interpret credit ratios; evaluate issuer and bond credit quality vs industry
- Describe factors driving level and volatility of yield spreads
- Explain special considerations for high yield, sovereign and non-sovereign government debt

## Frameworks Introduced
- **Expected loss decomposition**: Expected loss = Default probability × Loss severity; Loss severity = 1 − Recovery rate.
  - When to use: comparing any two credits, especially below investment grade.
  - How: (1) estimate PD from rating/cash-flow analysis; (2) estimate recovery from seniority, collateral, cycle position and industry; (3) multiply. Express as % of principal so it is size-independent.
  - Failure mode: ratings mostly measure PD, so two bonds with the same rating can have very different expected loss. The market prices expected loss, and that explains price gaps at equal ratings.
- **The four Cs**: Capacity (ability to service debt), Collateral (quality/value of assets relative to debt and its seniority), Covenants (contract terms limiting/obligating management), Character (management quality and record).
  - When to use: structuring any single-name credit review.
  - How: Capacity = industry analysis (Porter's five forces, cyclicality, growth) then company analysis (competitive position, track record, strategy, ratios, liquidity). Collateral matters more as PD rises. Covenants: read the indenture. Character: strategy soundness, past restructurings, accounting aggressiveness, fraud history, prior treatment of bondholders.
  - Failure mode: it is a summary aid, not a checklist. Other authors add "capital" and "conditions".
- **Porter's five forces for credit**: threat of entry, supplier power, buyer power, substitutes, rivalry. High barriers, diversified suppliers/customers, no close substitutes and low rivalry mean stable cash flow, lower credit risk, more debt capacity.
- **Credit ratio triad**: profitability and cash flow (EBIT, EBITDA, FFO, FCF), leverage (Debt/EBITDA, Debt/Capital, FFO/Debt, FCF after dividends/Debt), coverage (EBITDA/Interest, EBIT/Interest). Judge on level, trend, peer comparison and volatility, never on a single year.
- **Notching**: issue ratings move up/down from the issuer rating (usually senior unsecured) for seniority and structural subordination. Notches are larger at lower ratings.
  - Why it works: investment-grade ratings stress timeliness of payment, while non-investment-grade ratings give additional weight to recovery.
- **Liquidity source ladder (high yield)**, strongest to weakest: cash, working capital, operating cash flow, bank facilities, equity issuance, asset sales. Compare with debt maturities and committed capex over the next 6-12 months.
- **Equity-like (enterprise value) approach for high yield**: EV = market cap + total debt − excess cash; compare EV/EBITDA against Debt/EBITDA. A narrow gap means a thin equity cushion under the bonds.
- **Sovereign credit framework** (S&P-style, five areas): institutional/political, economic, external, fiscal, monetary. Two questions: ability and willingness to pay.

## Key Concepts
- **Credit risk**: risk of loss from failure to make full, timely interest and/or principal payments.
- **Default probability (default risk)**: probability the borrower fails to meet contractual payments.
- **Loss severity (loss given default)**: fraction of value (including unpaid interest) lost on default; 1 − recovery rate.
- **Spread risk**: yield spread widens from downgrade (migration) and/or worse market liquidity; separate but often correlated.
- **Credit migration (downgrade) risk**: issuer's creditworthiness deteriorates, widening spreads and cutting prices.
- **Market liquidity risk**: risk that the transaction price differs from the quoted price; larger for small issuers (little debt outstanding) and lower quality; shows up as wide bid-ask spreads.
- **Capital structure**: mix of bank debt, bonds of all rankings, preferred and common equity across the group's entities.
- **Priority of claims**: first lien/first mortgage > second lien > senior unsecured > senior subordinated > subordinated > junior subordinated > preferred > common. If collateral value falls short of a secured claim, the shortfall becomes a senior unsecured claim.
- **Pari passu**: claims at the same level rank equally in right of payment regardless of size or maturity (a 30-year and a 6-month senior unsecured bond have the same claim).
- **Cross-default**: default on one obligation triggers default on all, so an issuer's bonds share one PD even though their recoveries differ.
- **Structural subordination**: holding-company debt is repaid from subsidiary dividends, which come only after subsidiary obligations; parent debt recovers less.
- **Credit curve**: spread by maturity for one issuer; typically upward sloping; inverted for distressed or high-premium bonds.
- **Affirmative vs negative (restrictive) covenants**: things the issuer must do (pay, file audited statements) vs may not do (excess payouts, extra secured debt). Maintenance covenants (leverage tests) appear mainly in bank loans.
- **Negative pledge**: if any creditor gets security, this bond must get it too.
- **Change of control put**: bondholders can sell back at about par on an acquisition; investment-grade versions usually also require a downgrade to high yield.
- **Restricted payments basket**: cap on cash to shareholders, growing with retained earnings/cash flow.
- **Restricted vs unrestricted subsidiaries**: restricted ones (usually larger) guarantee parent debt, putting it pari passu with subsidiary debt.
- **Top-heavy capital structure**: lots of secured bank debt relative to unsecured; little room for more secured borrowing, lower recovery for junior creditors.
- **General obligation (GO) vs revenue bonds**: GO backed by taxing authority; revenue bonds by a single project's income, hence riskier.

## Formulas & Reference Tables
- `Expected loss = PD × Loss severity`; `Loss severity = 1 − Recovery rate`
- `Operating margin = EBIT / Revenue`; `EBIT = operating income`
- `EBITDA = Operating income + D&A`
- `FFO = Net income (continuing ops) + D&A + deferred taxes + other non-cash items` (S&P; excludes working capital changes)
- `FCF before dividends ≈ CFO − Capex`; `FCF after dividends = CFO − Capex − Dividends` (buybacks treated as discretionary by some analysts)
- `Debt/Capital = Debt / (Debt + Equity)`; `Debt/EBITDA` (gross); `Net leverage = (Debt − Cash)/EBITDA`
- `FFO/Debt`, `FCF after dividends/Debt`
- `EBITDA coverage = EBITDA / Interest expense`; `EBIT coverage = EBIT / Interest expense` (more conservative)
- `Debt service coverage (DSC) = Revenue available after operating expenses / (Principal + Interest)` (revenue bonds)
- `Enterprise value = Market cap + Total debt − Excess cash` (excess cash = cash − negative working capital)
- `Corporate yield = Real risk-free rate + Expected inflation + Maturity premium + Liquidity premium + Credit spread`
- `Yield spread = Liquidity premium + Credit spread` (only the total is observable)
- `Price impact ≈ −MDur × ΔSpread` (small changes); `≈ −MDur × ΔSpread + ½ × Cvx × (ΔSpread)²` (larger changes). Use ΔSpread as a decimal and rescale convexity to the order of duration² (reported 0.235 becomes 23.5 for duration 5).

| Moody's / S&P / Fitch | Bucket |
|---|---|
| Aaa/AAA | Highest quality |
| Aa1-Aa3 / AA+ to AA- | High-quality grade |
| A1-A3 / A+ to A- | Upper-medium grade |
| Baa1-Baa3 / BBB+ to BBB- | Low-medium grade; Baa3/BBB- is the last investment-grade notch |
| Ba1 / BB+ and below | Speculative ("high yield", "junk") |
| Caa1-Caa3, Ca, C / CCC+ to CCC-, CC, C | Very weak; D (S&P/Fitch) = default |

Split ratings such as Baa3/BB+ are "crossovers". Short-term scales: Moody's P-1 to P-3; S&P A-1+, A-1, A-2, A-3; Fitch F-1 to F-3 (top grades map to single-A or higher long-term).

**Average recovery by seniority (Moody's ultimate recovery, N. American non-financials, 1987-2017 by default year)**: bank loans 80.4%, senior secured bonds 62.3%, senior unsecured bonds 47.9%, subordinated bonds 28.0%. Bad-year example: 2016 defaults recovered 46.9% (secured) and 29.2% (unsecured).

**Annual default rates, S&P 1998-2017 mean**: AAA 0.00%, AA 0.03%, A 0.07%, BBB 0.19%, BB 0.69%, B 3.82%, CCC/C 27.98%. Cumulative defaults (non-financials) at 1/3/10 years: BBB 0/0.08/0.27%; BB 0.10/2.46/3.33%; B 0.95/10.11/12.90%; CCC/C 27.15/41.43/44.70%.

**Three-year transition (S&P 1981-2017)**: AAA stays AAA 65.5%; BBB stays BBB 64.7% (0.87% defaults); BB 47.0% (3.96% default); B 41.5% (12.6% default); CCC/C 40.7% default.

**Indicative ratios by rating (Bloomberg Barclays US industrials, 2018)**: FFO/Debt about 41% for Baa vs 28% Ba vs 20% B vs 10% Caa; Debt/EBITDA 3.9x Baa, 4.1x Ba, 5.2x B, 9.3x Caa; Debt/Capital 49% Baa, 64% Ba, 69% B, 95% Caa. The small AAA sample distorts averages.

**Yields by rating (30 Sep 2018, US)**: AAA 3.63%, A 3.86%, BBB 4.35%, BB 5.14%, B 6.23%, CCC 8.87%. **Trailing 12-month returns 1996-2018**: average return and volatility rise with risk (Aaa 4.82%/3.43% to Caa 8.26%/11.00%); B is a mild anomaly (6.79% below Ba's 7.98%). **Asset classes 1988-2018**: investment-grade corporates 7.00%/4.71%, high yield 8.86%/6.79%, S&P 500 11.39%/12.91%.

**Sovereign rules of thumb (S&P framework)**: net general government debt below 30% of GDP is good, above 100% poor; interest below 5% of revenue good, above 15% poor. Stable or falling debt/GDP is strong. "Twin surpluses" (budget and current account) ease service.

## Mental Models
- **Bond = short a put on the firm**: bondholders get capped upside and full downside. So credit analysts study downside protection (cash flow, balance sheet, covenants) rather than upside growth, unlike equity analysts.
- **High grade = spread risk; low grade = default and recovery risk**: for investment-grade names PD is tiny, so focus on migration, spread duration and liquidity. Below BBB, shift to liquidity, recovery, structure and covenants.
- **Ratings lag, prices lead**: use spreads and equity as early warning; ratings confirm. A rating change is often already priced in.
- **Debt ranks by contract, cash flows by structure**: a parent can be a better credit than one subsidiary because of diversification, while parent debt is still structurally junior to subsidiary debt. Do not read credit quality off the lien chart alone.
- **Cycle amplifies everything**: at the credit-cycle trough recoveries are lowest, spreads widest and defaults highest. Secular decline (newspapers) hurts recovery more than a cyclical dip.
- **Industry sets the ratio yardstick**: compare ratios with the industry and rating medians; regulated monopolies and non-cyclicals carry more debt than cyclical, low-barrier commodity producers.

## Worked Example
**A. Ratios (Mallinckrodt, 2017, $m).** Operating income 420.1, D&A 808.3, revenue 3,221.6, CFO 727.3, capex 186.1, no dividends, interest expense 369.1, debt 313.7 + 6,420.9 = 6,734.6, equity 6,522.0.
- EBITDA = 420.1 + 808.3 = 1,228.4; operating margin = 13.0%
- Debt/EBITDA = 6,734.6 / 1,228.4 = 5.5x; Debt/Capital = 6,734.6 / 13,256.6 = 50.8%
- FCF after dividends = 727.3 − 186.1 = 541.2, so 541.2 / 6,734.6 = 8.0% of debt
- EBITDA/Interest = 3.3x; EBIT/Interest = 1.1x (2015: 1.4x, 2016: 0.7x)
- Read: leverage improved 2015-2017 (Debt/EBITDA 6.3x to 5.5x, Debt/Capital 55.0% to 50.8%), but EBIT coverage of about 1x means almost no cushion, and interest expense rose faster than earnings. The drop in FCF/Debt in 2017 was driven by a one-off disposal-related item. Versus J&J (Debt/EBITDA 1.4x, EBITDA/Interest 27.1x) it is far weaker; versus ArcelorMittal its margins are steadier but its metrics are worsening while Arcelor's are improving.

**B. Leverage by debt layer (Hexion, year-end 2017, $m).** EBITDA 365; first lien 2,607; secured bonds 225; second lien 574; senior unsecured 263; total 3,669; cash 115.
- Secured leverage = (2,607 + 225) / 365 = 7.8x
- Through second lien = 3,406 / 365 = 9.3x
- Total = 3,669 / 365 = 10.1x; net = (3,669 − 115) / 365 = 9.7x
- Read: the unsecured bonds attach at 9.3x and detach at 10.1x, which is deep in the capital structure at a cyclical chemicals company, so expect low recovery and a top-heavy structure.

**C. Spread shock.** A 10-year bond, MDur 7.9, Cvx 74.9, spread widens 50 bp: −7.9 × 0.005 + 0.5 × 74.9 × 0.005² = −3.95% + 0.09% = −3.86% (exact about −3.85%). For BT 2047 (MDur 17.14, Cvx 408.4), a +100 bp move: duration alone gives −17.14%, adding convexity gives −15.10%, and the actual price change was −14.89%.

**D. Expected loss.** BB, 10-year cumulative PD 3.33% with subordinated recovery 28% gives EL = 3.33% × 72% = 2.4%. With senior secured recovery 62.3%, EL = 3.33% × 37.7% = 1.26%. Same rating, roughly half the expected loss.

## Anti-patterns
- **Outsourcing to ratings**: they lag prices, can be wrong (subprime, Enron, WorldCom, Parmalat), and miss litigation, disasters and leveraging events such as LBOs, debt-funded M&A and buybacks.
- **Assuming a rating persists over the holding period**: over 3 years even AAA stays AAA only about 65% of the time and a B stays B about 41%.
- **Judging credit on a single-year ratio or a single measure**: EBITDA ignores capex and working capital; use FFO, FCF and coverage together, on trends and through the cycle.
- **Applying the same leverage yardstick across industries**: cyclical, high-operating-leverage issuers should carry less debt.
- **Treating net debt as deleveraging**: cash may not be used to repay debt, and can be trapped offshore; actual debt paydown is the better signal.
- **Ignoring goodwill and intangibles in collateral analysis**: goodwill is low quality and likely to be written down after sustained weak performance; also check capex vs depreciation and stock trading below book value.
- **Assuming the priority of claims is absolute**: negotiated plans often pay juniors and even equity to avoid litigation cost and value erosion. US law favours reorganization, UK law favours liquidation for senior creditors.
- **Reading covenants as boilerplate**: without them management can pay dividends, buy back stock and add secured debt at bondholders' expense. Check whether restricted-subsidiary definitions can be changed by a board vote.
- **Ignoring the quirks of the credit curve for premium and distressed bonds**: these can show flat or inverted spreads.

## Exam Focus & Traps
- Credit risk is measured by **expected loss**, not PD or severity alone. Interest rate risk is not a credit or credit-related risk.
- Second lien outranks senior unsecured (secured beats unsecured). Same-level claims are pari passu regardless of maturity.
- The subordinated bond of a BB issuer is notched about two notches lower; investment-grade notching is at most one notch and AAA need not be notched. Notching gets bigger as ratings fall.
- Issuer rating usually equals the senior unsecured rating; secured issues may be rated higher, subordinated and holding-company issues lower (Infor: B- issuer; B secured; CCC+ unsecured; CCC holdco).
- Same rating but very different prices: the lower-priced bond's rating probably lags the market (or its expected loss is higher), and not the reverse. A price that did not react to an upgrade was probably "priced in".
- Covenant tells: "buy back as much stock as it likes" is the absence of a covenant. A negative pledge is a covenant.
- Stock below book value signals possible asset impairment, so weaker collateral. Large goodwill signals lower asset quality.
- Capacity, not character, is assessed through industry and company fundamentals. Strategy soundness and accounting aggressiveness fall under Character.
- Spread volatility is greatest for lower-quality bonds. Spreads widen when equities fall, the credit cycle turns, dealers pull capital, or supply is heavy.
- Convexity scaling: rescale reported convexity before use, and keep ΔSpread as a decimal. Price impact in bp when spread is in bp.
- The credit curve slopes up for normal credits because uncertainty and transaction costs grow with maturity.
- Sovereign: ability and willingness (sovereign immunity); domestic-currency debt is usually rated at least as high as foreign-currency debt (about one notch higher); GO vs revenue bonds (revenue riskier; DSC key).
- ⚠ Correction (source): in the Mallinckrodt solution the 2016 operating margin is written "0.084" but 248.4/3,399.5 = 0.073 = 7.3%, which matches the table. The Hexion exhibit shows total debt as both 3,668 and 3,669 and net debt 3,553 vs 3,554 (rounding). The net leverage (9.7x) is unaffected.

## Key Takeaways
1. Price credit through expected loss: PD × (1 − recovery). Ratings mostly capture PD, so at equal ratings check recovery and seniority.
2. In investment grade, the driver is spread risk (migration, liquidity); the P&L effect is ≈ −MDur × ΔSpread, plus a convexity term for shocks of 50-100 bp or more.
3. In high yield, shift the weight to liquidity, projections and stress cases, debt structure per layer (Debt/EBITDA at each attachment point), holdco vs opco, covenants and EV cushion.
4. Do your own work: ratings lag prices, migrate, and miss event risk; use ratings as one input.
5. Use ratios on level, trend and peer/rating medians; never read Debt/EBITDA without EBITDA/interest, FCF after dividends/debt and industry cyclicality. Adjust debt for pensions and leases.
6. Never assume absolute priority in bankruptcy or that structurally junior debt sits in a weaker credit overall.
7. Credit curves normally slope upward; long bonds carry more spread duration, default uncertainty and bid-ask cost, but distressed and high-premium bonds can be inverted.
8. Sovereigns: ability plus willingness; watch debt/GDP trend, interest/revenue, external liquidity, currency status. Municipals: GO ~ tax base and pensions; revenue bonds ~ project and DSC.

## Connects To
- **ch01**: bond contract features, covenants and seniority definitions (indenture, secured/unsecured, embedded options) behind the covenant discussion here.
- **ch02**: primary/secondary markets and repo funding; market liquidity and dealer capital drive spread behaviour.
- **ch05**: modified duration and convexity provide the price-impact formula used for spread changes.
- **ch10**: Level II credit models turn PD, LGD and spread into pricing (structural/reduced-form models, credit-risk-adjusted valuation).
- **ch11**: credit default swaps monetise PD, LGD and spread views directly, and hedge spread risk.
- **ch15**: Level III credit strategies apply spread-duration, curve and issuer-selection decisions from this chapter.
- **`tuckman-fixed-income` ch19**: corporate bonds and CDS, with structural and reduced-form credit models and spread decomposition.
