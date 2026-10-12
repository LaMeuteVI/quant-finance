# Chapter 4: Routing for Risk Models

> Quant Orchestrator, Chapter 4.

## Core Idea

For risk models (VaR, ES, FRTB, CVA, market risk), the routing is: (1) hull-risk-management for the institutional framework; (2) frtb-market-risk-bcbs457 for the binding regulatory standard; (3) gatheral-volatility-surface for the vol surface input; (4) hull-derivatives for the option pricing input. The agent should always use ES, not VaR, for the 2026 standard.

## Key Takeaways

1. The routing is the institutional protocol.
2. Always start with the institutional baseline.
3. Always end with the validation.

## Connects To

See the SKILL.md "Related Skills" for the full map.
