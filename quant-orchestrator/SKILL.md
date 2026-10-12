---
name: quant-orchestrator
description: "The meta-skill for routing any quant question to the right combination of skills. Use when facing a new research question, a backtest problem, a strategy proposal, a regulatory question, or a forecast task. Provides the decision tree: 'Is this a forecast, a strategy, a risk-model, or a regulatory question?' → which skill to consult first → which to consult for the methodology → which for the cross-check. This is the entry point for the agent. Without it, the agent has a library but no librarian."
---

<!-- argument-hint: [task type or question] -->

# Quant Orchestrator

**Source**: The institutional routing protocol for the 13 quant skills in this library. | **Domain**: Fondamentaux | **Chapters**: 6 | **Generated**: 2026-10-12

## How to Use This Skill

- **At the start of any new quant task**: read this SKILL.md and route to the right skill(s).
- **For a specific task type** (e.g. "momentum strategy", "VaR backtest", "GIPS report"): use the decision tree in ch01.

## The Decision Tree

```
Is this a research question (alpha generation, factor mining)?
  ├─ Yes → grinold-kahn-apm + lopez-de-prado-afml + lopez-de-prado-ml-asset-managers
  └─ No → Is it a forecast (time series, vol surface, GARCH)?
              ├─ Yes → tsay-analysis-financial-time-series + diebold-mariano-forecast-accuracy
              └─ No → Is it a risk model (VaR, ES, FRTB)?
                        ├─ Yes → hull-risk-management + frtb-market-risk-bcbs457
                        └─ No → Is it a derivative or vol surface?
                                  ├─ Yes → gatheral-volatility-surface + hull-derivatives
                                  └─ No → Is it a strategy execution / implementation?
                                            ├─ Yes → chan-machine-trading + lopez-de-prado-afml ch10-11
                                            └─ No → Is it a backtest validation?
                                                      ├─ Yes → quant-backtest-hygiene + lopez-de-prado-afml ch14
                                                      └─ No → Is it a regulatory question?
                                                                ├─ Yes → frtb-market-risk-bcbs457 + cfa-l3-2024-update + cfa-ethics-gips
                                                                └─ No → Is it a CFA / GIPS / PM framework question?
                                                                          ├─ Yes → cfa-l3-2024-update
                                                                          └─ No → Default: grinold-kahn-apm (the institutional baseline)
```

## Chapter Index

| # | Title | File |
|---|---|---|
| 1 | The Decision Tree | [ch01](./chapters/ch01-the-decision-tree.md) |
| 2 | Routing for Forecasts | [ch02](./chapters/ch02-routing-for-forecasts.md) |
| 3 | Routing for Strategies | [ch03](./chapters/ch03-routing-for-strategies.md) |
| 4 | Routing for Risk Models | [ch04](./chapters/chapters/ch04-routing-for-risk-models.md) |
| 5 | Routing for Backtests | [ch05](./chapters/ch05-routing-for-backtests.md) |
| 6 | Routing for Regulatory Questions | [ch06](./chapters/ch06-routing-for-regulatory-questions.md) |

## Related Skills (all 13 quant skills)

- `grinold-kahn-apm` (gestion-de-portfeuille) — Active management; the institutional baseline.
- `lopez-de-prado-afml` (gestion-de-portfeuille) — ML for finance; the methodological backbone.
- `lopez-de-prado-ml-asset-managers` (gestion-de-portfeuille) — Companion to AFML.
- `hull-risk-management` (finance-de-marche) — Risk management; the institutional complement.
- `hull-derivatives` (finance-de-marche) — Options/futures/swaps pricing.
- `gatheral-volatility-surface` (finance-de-marche) — Vol surface and exotic options.
- `frtb-market-risk-bcbs457` (finance-de-marche) — The binding FRTB standard.
- `chan-machine-trading` (finance-de-marche) — Practical algo trading.
- `tsay-analysis-financial-time-series` (fondamentaux) — Time-series foundation.
- `diebold-mariano-forecast-accuracy` (fondamentaux) — Forecast comparison.
- `cfa-l3-2024-update` (gestion-de-portfeuille) — CFA 2024 L3 PM refresh.
- `quant-backtest-hygiene` (fondamentaux) — The 10 mandatory checks.
- `quant-verification` (fondamentaux) — The verification protocol.
- `pairs-trading-partial-cointegration` (fondamentaux) — Pairs trading reference.
- `tian-commodity-price-jumps` (fondamentaux) — Commodity jumps reference.

## Scope & Limits

- **Coverage**: 6 chapters on the routing protocol.
- **What this skill is**: a meta-skill. It does *not* contain quant knowledge; it routes to the skills that do.
- **What this skill is NOT**: a methodology. The methodologies are in the source skills.
