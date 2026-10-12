# Chapter 8: Securitization and the Financial Crisis of 2007–8

## Core Idea
Securitization pools loans and tranches their cash flows through a waterfall. Re-securitizing tranches (ABS CDOs) created "AAA" paper that was extremely sensitive to default correlation. Combined with misaligned incentives across the originate-to-distribute chain, this produced the 2007–8 crisis.

## Frameworks Introduced
- **ABS structure**: a portfolio of income-producing assets sits in an SPV and is split into **senior**, **mezzanine** and **equity** tranches. Example: $80m senior (SOFR/LIBOR + 60bp), $15m mezzanine (+250bp), $5m equity (+2,000bp).
- **Waterfall**: interest and principal are paid to senior first, then mezzanine, then equity. **Losses hit equity first, then mezzanine, then senior.**
- **ABS CDO (re-securitization)**: the mezzanine tranches of many ABSs are pooled and re-tranched. The "senior" tranche of an ABS CDO can be wiped out by moderate losses in the underlying mortgage pool. It is very thin and highly correlated.
- **Incentive chain failure**: originator (lend and sell), rating agency (paid by the issuer), investor (yield hunger), trader (short-term bonus). No one bears the full default risk.

## Key Concepts
- **SPV (special purpose vehicle)**: a bankruptcy-remote entity that holds the assets.
- **Tranche**: a slice of the cash-flow/loss distribution with defined attachment and detachment points.
- **Subprime mortgage**: a riskier-than-prime mortgage, often with a **teaser rate** that resets higher after 2–3 years.
- **Liar loans / NINJA loans**: mortgages with little or no verification of income or assets.
- **Negative equity**: the mortgage balance exceeds the house value. This triggers strategic default.
- **Originate-to-distribute model**: banks originate loans only to sell them. This weakens underwriting incentives.
- **Regulatory arbitrage**: structures designed to cut capital requirements rather than risk.
- **Basel III / Dodd-Frank responses**: more capital, liquidity ratios, central clearing, the Volcker rule, skin-in-the-game (retention) rules.

## Mental Models
- **Tranche losses are non-linear in pool losses**: a mezz tranche with a 5–20% attachment range goes from zero loss to total loss as pool losses move from 5% to 20%. An ABS CDO of such tranches amplifies this again.
- **Correlation is the key risk parameter** for senior tranches. With low correlation seniors are safe. When everything defaults together, they are not.
- Ask "**who bears the risk if this goes wrong, and do they control the underwriting?**"

## Anti-patterns
- **Relying on ratings for structured products**: an AAA ABS CDO tranche is not an AAA corporate bond. It has a totally different tail behavior.
- **Compensation on short-term P&L** for products with long-tailed risks.
- **Assuming house prices always rise**: the assumption embedded in lending standards from 2000–2006.

## Worked Example
**Hull's ABS → ABS CDO structure (Fig 8.3, Table 8.1).**
- Each ABS has senior 80%, mezzanine 15% (the 5–20% loss range) and equity 5%.
- The ABS CDO pools the ABS mezzanine tranches and splits them into senior 65%, mezzanine 25% and equity 10%.

| Loss on underlying | ABS mezz loss | ABS CDO equity | ABS CDO mezz | ABS CDO senior |
|---|---|---|---|---|
| 10% | 33.3% | 100% | 93.3% | 0% |
| 13% | 53.3% | 100% | 100% | 28.2% |
| 17% | 80.0% | 100% | 100% | 69.2% |
| 20% | 100% | 100% | 100% | 100% |

- The ABS CDO senior ("AAA") is safe only if underlying losses are ≤ 10.25%. That is when ABS mezz losses of 5.25/15 = 35% just exhaust the CDO equity + mezz.
- At 17% losses, the ABS mezz tranches lose 12/15 = 80%. The CDO senior loses (80 − 35)/65 = **69.2%**.

## Key Takeaways
1. Securitization transfers credit risk. Re-securitization concentrates correlation risk.
2. Waterfalls make tranche risk highly non-linear in pool losses.
3. The crisis was an incentive failure along the originate-to-distribute chain, not only a model failure.
4. Regulation responded with capital and liquidity rules, central clearing and risk retention.

## Connects To
- **Ch 24**: default correlation, the Gaussian copula.
- **Ch 25**: CDOs, synthetic CDOs, tranche valuation.
- **Ch 2 / Ch 9**: post-crisis OTC reforms, CCPs and XVAs.
- **Ch 37**: lessons on risk management and incentives.
