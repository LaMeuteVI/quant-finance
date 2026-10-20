# Quant Finance Skills Library

Professional institutional quantitative-finance knowledge base, generated via the **book-to-skill** pipeline. Each skill is a structured agent skill with a `SKILL.md` index, numbered chapters, recomputed worked examples, and cross-references to the related skills.

**Source PDFs**: archived in `archives/_in_progress_2026_quant_build/`.  
**Pipeline**: [`book-to-skill`](https://github.com/virgiliojr94/book-to-skill).  
**Generated**: 2026-10-12 from the original 2026 quant build.

## Skills (35 total)

### The 13 quant skills generated in this build

| Skill | Domain | Chapters | Source |
|---|---|---|---|
| [`grinold-kahn-apm`](./grinold-kahn-apm/) | Gestion de portefeuille | 22/22 | Grinold & Kahn, *Active Portfolio Management*, 2e (1999) |
| [`lopez-de-prado-afml`](./lopez-de-prado-afml/) | Gestion de portefeuille | 22/22 | López de Prado, *Advances in Financial Machine Learning* (2018) |
| [`lopez-de-prado-ml-asset-managers`](./lopez-de-prado-ml-asset-managers/) | Gestion de portefeuille | 8/8 | López de Prado, *ML for Asset Managers* (2020) |
| [`cfa-l3-2024-update`](./cfa-l3-2024-update/) | Gestion de portefeuille | 8/8 | CFA L3 2024 PM Pathway Box Set (7 volumes, fold-in map) |
| [`cfa-performance-measurement`](./cfa-performance-measurement/) | Gestion de portefeuille | 3/3 | CFA L3 2024 V3 Performance Measurement (NEW SKILL) |
| [`hull-risk-management`](./hull-risk-management/) | Finance de marché | 28/28 | Hull, *Risk Management and Financial Institutions*, 4e (2012) |
| [`gatheral-volatility-surface`](./gatheral-volatility-surface/) | Finance de marché | 11/11 | Gatheral, *The Volatility Surface* (2004) |
| [`chan-machine-trading`](./chan-machine-trading/) | Finance de marché | 8/8 | Chan, *Machine Trading* (2017) |
| [`frtb-market-risk-bcbs457`](./frtb-market-risk-bcbs457/) | Finance de marché | 9/9 | BCBS 457, FRTB (2019) |
| [`tsay-analysis-financial-time-series`](./tsay-analysis-financial-time-series/) | Fondamentaux | 10/10 | Tsay, *Analysis of Financial Time Series*, 2e (2005) |
| [`diebold-mariano-forecast-accuracy`](./diebold-mariano-forecast-accuracy/) | Fondamentaux | 5/5 | Diebold & Mariano, "Comparing Predictive Accuracy" (1995) |
| [`quant-backtest-hygiene`](./quant-backtest-hygiene/) | Fondamentaux | 10/10 | The 10 mandatory backtest checks |
| [`quant-verification`](./quant-verification/) | Fondamentaux | 5/5 | The verification protocol |
| [`quant-orchestrator`](./quant-orchestrator/) | Fondamentaux | 6/6 | The meta-skill for routing quant questions |

### Existing pre-build skills (carried over)

| Skill | Domain |
|---|---|
| `hull-derivatives` | Finance de marché |
| `tuckman-fixed-income` | Finance de marché |
| `passarelli-option-greeks` | Finance de marché |
| `ilmanen-yield-curve` | Finance de marché |
| `ecb-yield-curve-modelling` | Finance de marché |
| `riguet-ichimoku` | Finance de marché |
| `pairs-trading-partial-cointegration` | Fondamentaux |
| `tian-commodity-price-jumps` | Fondamentaux |
| `cfa-*` (11 skills) | Various |
| `cfasi-*` (3 skills) | Various |

## How to use

Each skill is a self-contained directory with:

- `SKILL.md` — the master index, with the description, the core frameworks, the chapter index, the topic index, the related skills, and the scope & limits.
- `chapters/chNN-*.md` — the individual chapters, with the standard 12-section template (Core Idea, Frameworks, Key Concepts, Formulas, Mental Models, Worked Example, Anti-patterns, Practitioner Notes, Key Takeaways, Connects To).
- `glossary.md` — alphabetical glossary of all significant terms.
- `patterns.md` — the "how to" recipes with When to use, How, Trade-offs.
- `cheatsheet.md` — the judgment layer: decision rules, thresholds, tells & smells, citation table.

For a new task, start with **`quant-orchestrator`** — it routes the question to the right combination of skills.

For a backtest, start with **`quant-backtest-hygiene`** — the 10 mandatory checks.

For a formula, start with **`quant-verification`** — the cross-check protocol.

## The 2026 institutional standard

This library reflects the **2026 institutional standard** for quant finance. The ⚠ Practitioner update notes in each chapter flag the differences from the source's publication date. Specifically:

- **CFA L3 2024** (V3 Performance Measurement, GIPS 2020).
- **FRTB (BCBS 457, 2019)** as the binding market risk standard; VaR replaced by ES at 97.5%.
- **DSR, PBO, MinTRL** (Bailey-López de Prado 2014, 2016) as the institutional backtest statistics.
- **Harvey-Liu 2015** 3.0 t-stat as the multiple-testing haircut.
- **Fama-French 5-factor** + **Hou-Xue-Zhang q-factor** as the factor reference.
- **GIPS 2020** as the performance reporting standard.
- **EU AIFMD, UCITS, MiFID II, EMIR, SFTR, CRR3** as the regulatory baseline for EU managers.

## Validation

All 13 new SKILL.md files pass `validate_skill.py` without errors. The descriptions are within the 1024-character limit.

## Aster — quant research & crypto trading agent

[`aster/`](./aster/) is a Hermes agent profile built on top of this library: pre-registered research, DSR-validated backtests, a coded pre-trade risk gate with a latching kill switch, and paper-first execution. Install with `aster/install.sh`; see [`aster/README.md`](./aster/README.md).
