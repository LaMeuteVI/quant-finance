# Chapter 1: Introduction and Scope of FRTB (BCBS 457)

> BCBS 457 — Minimum Capital Requirements for Market Risk, January 2019, MAR10–MAR12.

## Core Idea

The **Fundamental Review of the Trading Book (FRTB)** is the Basel Committee's 2019 standard for market risk capital. It replaced the 2006 Basel II market risk framework (the 99% 10-day VaR + stressed VaR) with a more risk-sensitive approach based on **Expected Shortfall (ES) at 97.5%** for the Internal Models Approach (IMA), and a **Standardised Approach (SA)** with explicit sensitivities, default risk, and residual risk add-ons. The framework is binding for internationally active banks and is the reference for all 2026 trading book capital calculations.

## Frameworks Introduced

- **The Two Approaches**: IMA (Internal Models Approach) and SA (Standardised Approach). Banks must use the higher of the two capital requirements.
- **The Boundary between Trading Book and Banking Book** (MAR25): instruments held for trading intent (short-term resale, arbitrage, hedging) belong to the trading book; otherwise banking book. Strict limits on switching.
- **The Market Risk Capital Requirement**: `Capital = max(IMA_capital, SA_capital)` for the bank as a whole.
- **The Trading Desk Definition** (MAR12): a group of traders or accounts following a defined trading strategy.
- **The Risk Factor Classification**: delta, vega, curvature, default, residual; bucketed by asset class.

## Key Concepts

- **FRTB (Fundamental Review of the Trading Book)** — the 2019 binding standard.
- **IMA (Internal Models Approach)** — ES at 97.5% + DRC + IMA backtest multiplier.
- **SA (Standardised Approach)** — sensitivities-based method + default risk charge + residual risk add-on.
- **ES (Expected Shortfall)** — the tail-average risk measure; replaces VaR.
- **DRC (Default Risk Charge)** — the FRTB capital charge for default risk; not captured by ES.
- **RRAO (Residual Risk Add-On)** — for instruments with non-modellable risk (e.g. exotic options).
- **IMA backtest multiplier** — between 1.0 (green) and 1.84 (red) based on the backtest exception count.
- **P&L attribution test (PLAT)** — the IMA validation test; the bank's risk-theoretical P&L must match the actual P&L.
- **Boundary rules (MAR25)** — the trading book / banking book classification.

## Key Takeaways

1. FRTB replaced VaR with ES at 97.5% for IMA.
2. SA is a sensitivities-based method, not VaR.
3. The capital is `max(IMA, SA)` for the bank.
4. The default risk and residual risk are explicit add-ons.

## Connects To

- ch02 (SA: Sensitivities-Based Method), ch03 (SA: Default Risk), ch04 (SA: Residual Risk), ch05 (IMA), ch06 (IMA Backtesting), `hull-risk-management` ch17 (FRTB preview).
