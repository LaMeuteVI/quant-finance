---
name: chan-machine-trading
description: "Knowledge base from Ernest Chan, Machine Trading: Deploying Computer Algorithms to Conquer the Markets (Wiley 2017). Use when designing and deploying automated trading strategies, applying factor models (Fama-French, AQR, Barra) to algorithmic strategies, computing half-lives of mean reversion for pairs trading, applying ARMA/GARCH/cointegration to time-series models, using machine learning (random forest, gradient boosting, neural networks) in trading, trading volatility (dispersion, vol risk premium, gamma scalping), working with intraday data and market microstructure (order flow imbalance, Kyle's lambda, market impact), or trading Bitcoin/crypto. Covers 8 chapters on basics, factor models, time-series analysis, AI techniques, options strategies, intraday and microstructure, Bitcoin, and the human side of algo trading."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Machine Trading (Chan)

**Source**: Ernest Chan, *Machine Trading: Deploying Computer Algorithms to Conquer the Markets*, Wiley 2017 (formerly *Quantitative Trading* 2nd ed.) | **Domain**: Finance de marché | **Chapters**: 8 | **Generated**: 2026-10-12

## How to Use This Skill

- **Without args**: read this SKILL.md for the framework overview.
- **With a topic or framework name** (e.g. "factor model", "pairs trading", "vol trading", "HFT"): jump to the relevant chapter.
- **With a chapter number**: open `chapters/chNN-*.md`.

## Core Frameworks & Mental Models

1. **The Four Strategy Families** (ch01): mean-reversion, momentum, HFT, event-driven.
2. **Factor Models** (ch02): Fama-French 3/5-factor, Carhart 4-factor, AQR factors, Barra risk model.
3. **Time-Series Models** (ch03): ARMA, GARCH, cointegration, OU process, half-life of mean reversion.
4. **AI/ML Techniques** (ch04): supervised (RF, XGBoost, NN), unsupervised (PCA, k-means), reinforcement learning.
5. **Options Strategies** (ch05): dispersion, vol risk premium, gamma scalping, covered calls, protective puts.
6. **Market Microstructure** (ch06): order flow imbalance, Kyle's lambda, square-root law of impact, HFT.
7. **Bitcoin/Crypto** (ch07): 24/7 trading, stat arb across exchanges, on-chain analysis.
8. **Algo as Co-Pilot** (ch08): systematic vs discretionary, the algo as teacher and risk manager.

## Chapter Index

| # | Title | Key Frameworks | File |
|---|---|---|---|
| 1 | The Basics of Algorithmic Trading | Four strategy families | [ch01](./chapters/ch01-the-basics-of-algorithmic-trading.md) |
| 2 | Factor Models | Fama-French, AQR, Barra | [ch02](./chapters/ch02-factor-models.md) |
| 3 | Time-Series Analysis | ARMA, GARCH, cointegration, OU | [ch03](./chapters/ch03-time-series-analysis.md) |
| 4 | Artificial Intelligence Techniques | ML for trading, purged CV, DSR | [ch04](./chapters/ch04-artificial-intelligence-techniques.md) |
| 5 | Options Strategies | Dispersion, vol risk premium, gamma | [ch05](./chapters/ch05-options-strategies.md) |
| 6 | Intraday Trading and Market Microstructure | Order flow, Kyle's lambda | [ch06](./chapters/ch06-intraday-trading-and-market-microstructure.md) |
| 7 | Bitcoins | Stat arb, on-chain, funding rate | [ch07](./chapters/ch07-bitcoins.md) |
| 8 | Algorithmic Trading Is Good for Body and Mind | Algo as co-pilot | [ch08](./chapters/ch08-algorithmic-trading-is-good-for-body-and-mind.md) |

## Topic Index

- **AQR factors** → ch02
- **Arbitrage (ETF, statistical)** → ch01, ch07
- **Backtesting** → ch01, ch04
- **Barra risk model** → ch02
- **Bitcoin** → ch07
- **Cointegration** → ch03
- **Covered call** → ch05
- **Cross-sectional regression** → ch02
- **Crypto** → ch07
- **Dispersion** → ch05
- **DSR** → ch04 (cross-ref lopez-de-prado-afml)
- **Execution algorithm** → ch01
- **Fama-French 3/5-factor** → ch02
- **GARCH** → ch03
- **Gamma scalping** → ch05
- **Gradient boosting** → ch04
- **HFT** → ch01, ch06
- **Half-life of mean reversion** → ch03
- **Information Ratio** → ch02
- **Intraday trading** → ch06
- **Kyle's lambda** → ch06
- **Mean reversion** → ch01, ch03
- **Market impact (square-root)** → ch06
- **Market microstructure** → ch06
- **Momentum** → ch01
- **Order flow imbalance** → ch06
- **Pairs trading** → ch01, ch03
- **Protective put** → ch05
- **Purged CV** → ch04 (cross-ref lopez-de-prado-afml)
- **Random forest** → ch04
- **Regime switching** → ch03
- **Sharpe Ratio** → ch02
- **Skew trading** → ch05
- **Stablecoin** → ch07
- **Statistical arbitrage** → ch01, ch07
- **Theta decay** → ch05
- **Time-series regression** → ch02
- **Vega** → ch05
- **Vol risk premium** → ch05
- **Vol targeting** → ch03

## Related Skills

- **`grinold-kahn-apm`** (gestion-de-portefeuille) — the institutional active management framework.
- **`lopez-de-prado-afml`** (gestion-de-portefeuille) — the modern ML-backtest discipline; DSR, PBO, MinTRL.
- **`hull-derivatives`** (finance-de-marche) — the options/futures/swap pricing book.
- **`gatheral-volatility-surface`** (finance-de-marche) — the vol surface for vol trading.
- **`hull-risk-management`** (finance-de-marche) — ch10 (Volatility), ch12 (VaR/ES).
- **`tsay-analysis-financial-time-series`** (fondamentaux) — the time-series foundation.
- **`pairs-trading-partial-cointegration`** (fondamentaux) — the partial cointegration paper.
- **`tian-commodity-price-jumps`** (fondamentaux) — the commodity jumps paper.

## Scope & Limits

- **Coverage**: 8 chapters of the 2017 book (renamed from *Quantitative Trading* 2e).
- **Edition year**: 2017 — supplemented by post-2017 developments (LSTM, Transformers, the institutional adoption of LdP's purged CV/DSR/PBO).
- **What the source does NOT cover**:
  - The institutional active management (see `grinold-kahn-apm`).
  - The risk management / VaR (see `hull-risk-management`).
  - The volatility surface in detail (see `gatheral-volatility-surface`).
  - The ML-based backtest statistics (see `lopez-de-prado-afml`).
  - The time-series foundation (see `tsay-analysis-financial-time-series`).
- **OCR / extraction quality**: pdftotext output is clean; no reconstruction needed.
- **Translation**: English.
