# Chapter 2: Routing for Forecasts

> Quant Orchestrator, Chapter 2.

## Core Idea

For forecasts (time series, GARCH, VAR, vol surface, vol-of-vol), the routing is: (1) tsay-analysis-financial-time-series for the time-series foundation; (2) gatheral-volatility-surface for the vol surface; (3) diebold-mariano-forecast-accuracy for the comparison test. The agent should use DM/SPA/Clark-West for the comparison, not the naive paired t-test.

## Key Takeaways

1. The routing is the institutional protocol.
2. Always start with the institutional baseline.
3. Always end with the validation.

## Connects To

See the SKILL.md "Related Skills" for the full map.
