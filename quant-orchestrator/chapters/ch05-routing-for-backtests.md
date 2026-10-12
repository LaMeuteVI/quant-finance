# Chapter 5: Routing for Backtests

> Quant Orchestrator, Chapter 5.

## Core Idea

For backtests (validation, DSR, PBO, MinTRL, walk-forward, purged CV), the routing is: (1) quant-backtest-hygiene for the 10 mandatory checks; (2) lopez-de-prado-afml ch07-14 for the methodology; (3) diebold-mariano-forecast-accuracy for the forecast comparison; (4) grinold-kahn-apm ch17 for the performance attribution. The agent should always run the 10 checks before any backtest is published.

## Key Takeaways

1. The routing is the institutional protocol.
2. Always start with the institutional baseline.
3. Always end with the validation.

## Connects To

See the SKILL.md "Related Skills" for the full map.
