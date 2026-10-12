# Cheatsheet — Risk Management and Financial Institutions (Hull)

## When to do X, do Y, because Z

- **When you report a risk number**, use **ES at 97.5%** (FRTB), not VaR. **Because** ES is coherent and is the binding FRTB standard.
- **When you backtest a VaR model**, use the **traffic-light framework**. **Because** the 95% CI for 99% VaR is too wide for fine-grained model selection.
- **When you test the exception rate formally**, use the **Kupiec POF test**. **Because** it is the regulatory standard.
- **When you price counterparty risk**, compute the **CVA**. **Because** it is the market value of the counterparty's default risk.
- **When you execute a large order**, use the **Almgren–Chriss trajectory**. **Because** it balances impact and delay.
- **When you report a model output**, have it **independently validated**. **Because** the model's owner is not a reliable test of the model.
- **When you size a portfolio**, compute the **component VaR**. **Because** the aggregate number hides the concentration of risk.
- **When you measure tail dependence**, use the **Student-t copula**. **Because** the normal copula understates joint tail risk.

## Thresholds & defaults

| Quantity | Default | Range | Source |
|---|---|---|---|
| VaR confidence | 99% | 95% to 99.9% | ch12 |
| ES confidence (FRTB) | 97.5% | 97.5% (FRTB) | ch17, frtb-market-risk-bcbs457 |
| Backtest window | 250 days | 1 year | ch12 |
| Traffic-light (99% VaR) | green 0–4, yellow 5–9, red 10+ | | ch12 |
| Kupiec POF critical | 3.84 (95%) | 6.63 (99%) | ch12 |
| CVA discount rate | OIS | | ch20 |
| Liquidity horizon (FRTB) | 10 to 120 days | asset-class specific | ch17, frtb-market-risk-bcbs457 |
| IMA multiplier (FRTB) | 1.0 to 1.84 | | ch17, frtb-market-risk-bcbs457 |
| Stressed window (FRTB) | 12 weeks | | ch17 |

## Tells & smells

- **The exception count is in the yellow zone (5–9)** → the model is in a "warning" zone; investigate.
- **The exceptions are clustered in time** → regime change; the model needs to be re-validated.
- **The VaR changes sharply after a small change in `V`** → the model is over-fit to the recent window.
- **The CVA is large relative to the credit spread** → the wrong-way risk; investigate.
- **The model output is "obviously right"** → the model has not been independently validated.
- **The supervisor has imposed a capital add-on** → the model is in a red zone; remediation is required.

## Citation table (2026 institutional standards)

| Item | Threshold | Source |
|---|---|---|
| FRTB ES confidence | 97.5% | BCBS 457 (Jan 2019) |
| IMA backtest multiplier | 1.0 (green) to 1.84 (red) | BCBS 457 |
| Capital conservation buffer | 2.5% | Basel III |
| G-SIB surcharge | 1% to 3.5% | FSB |
| Liquidity Coverage Ratio (LCR) | 100% | Basel III |
| Net Stable Funding Ratio (NSFR) | 100% | Basel III |
| CVA capital charge (FRTB) | BA-CVA or SA-CVA | BCBS 457 |
| Default Risk Charge (DRC) | FRTB SA DRC formula | BCBS 457 |
| Residual Risk Add-on (RRAO) | 1% of notional | BCBS 457 |
| Model risk capital add-on | supervisor-set | SR 11-7, BCBS 239 |
