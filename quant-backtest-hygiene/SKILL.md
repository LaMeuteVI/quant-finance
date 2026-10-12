---
name: quant-backtest-hygiene
description: "The institutional checklist for validating a quantitative trading strategy. Use before any backtest is published, capital is allocated, or a strategy is presented to a PM. Covers 10 mandatory checks: point-in-time data, survivorship bias, corporate actions, look-ahead bias, walk-forward with purged CV and embargo, stationarity of the spread, transaction costs and market impact, capacity constraint, OOS performance via DSR/PBO/MinTRL, and live paper trading with scale-in. Without these checks, every backtest is fiction."
---

<!-- argument-hint: [check name or strategy type] -->

# Quant Backtest Hygiene

**Source**: The institutional checklist, compiled from Grinold & Kahn, López de Prado, Hull, Chan, and the regulatory practice. | **Domain**: Fondamentaux | **Chapters**: 10 | **Generated**: 2026-10-12

## How to Use This Skill

- **Before publishing a backtest** or allocating capital, run every check in this skill.
- **For a specific check** (e.g. "look-ahead bias", "transaction cost"): use the `argument-hint` to jump to the relevant chapter.
- **For a strategy type** (e.g. "momentum", "pairs trading"): the chapters apply to all strategy families.

## The 10 Mandatory Checks

| # | Check | What it catches | Cost to fix |
|---|---|---|---|
| 1 | Point-in-time (PIT) data | Look-ahead from data revisions | High (requires Bloomberg PIT) |
| 2 | Survivorship bias | Backtest only includes survivors | High (requires CRSP delisted) |
| 3 | Corporate actions | Splits, dividends, M&A mis-priced | Medium |
| 4 | Look-ahead bias | Future data in features or labels | Low (code review) |
| 5 | Walk-forward + purged CV + embargo | Single split leakage, in-sample overfit | Low (purged k-fold) |
| 6 | Spread stationarity (ADF, KPSS) | Spurious cointegration | Low (ADF test) |
| 7 | Transaction costs + market impact | Net IR under-costs strategy | Medium (Almgren-Chriss) |
| 8 | Capacity constraint | Strategy un-tradeable at AUM | Medium (square-root law) |
| 9 | DSR / PBO / MinTRL | Multiple testing, overfit backtest | Low (DSR formula) |
| 10 | Live paper + scale-in | Operational failure, slow leak | Low (live paper) |

A backtest that fails any of these checks is **not a strategy** — it is a hypothesis that must be re-tested.

## Chapter Index

| # | Title | File |
|---|---|---|
| 1 | Point-in-Time Data | [ch01](./chapters/ch01-point-in-time-data.md) |
| 2 | Survivorship Bias | [ch02](./chapters/ch02-survivorship-bias.md) |
| 3 | Corporate Actions | [ch03](./chapters/ch03-corporate-actions.md) |
| 4 | Look-Ahead Bias | [ch04](./chapters/ch04-look-ahead-bias.md) |
| 5 | Walk-Forward with Purged CV | [ch05](./chapters/ch05-walk-forward-with-purged-cv.md) |
| 6 | Spread Stationarity | [ch06](./chapters/ch06-spread-stationarity.md) |
| 7 | Transaction Costs and Market Impact | [ch07](./chapters/ch07-transaction-costs-and-market-impact.md) |
| 8 | Capacity Constraint | [ch08](./chapters/ch08-capacity-constraint.md) |
| 9 | DSR / PBO / MinTRL | [ch09](./chapters/ch09-dsr-pbo-mintrl.md) |
| 10 | Live Paper + Scale-In | [ch10](./chapters/ch10-live-paper-and-scale-in.md) |

## Related Skills

- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — the full AFML curriculum; the DSR/PBO/MinTRL is in ch14.
- **`grinold-kahn-apm`** (gestion-de-portefeuille) — the transaction cost and capacity frameworks are in ch16.
- **`hull-risk-management`** (finance-de-marche) — the model risk framework; ch25.
- **`diebold-mariano-forecast-accuracy`** (fondamentaux) — the DM test for forecast comparison.
- **`pairs-trading-partial-cointegration`** (fondamentaux) — the cointegration reference.
- **`tian-commodity-price-jumps`** (fondamentaux) — the jumps reference.

## Scope & Limits

- **Coverage**: 10 mandatory checks, with the standard institutional responses.
- **What this skill is**: a checklist. Each chapter is ~200-400 tokens; the depth is in the cross-references to the source skills.
- **What this skill is NOT**: a methodology. The methodology is in the source skills (AFML, APM, Hull). This skill is the *discipline* of applying the methodology.
