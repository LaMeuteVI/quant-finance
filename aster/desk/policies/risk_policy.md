# Risk policy

## Layers of protection (outermost is the strongest)
1. **Capital segregation (exchange)**: live trading runs on a dedicated sub-account funded only with money Samuel accepts to lose entirely. API key: trade-only, withdrawals disabled, IP-whitelisted. This is the only limit no software bug can bypass.
2. **Coded risk gate** (`src/aster/risk/gate.py`): every order, every mode. Limits in `config/risk_limits.yaml` (protected file).
3. **Kill switch** (`state/KILL`): latches automatically on daily-loss or drawdown breach, or manually (`desk kill on`). While active, only exposure-reducing orders pass. Clearing it is human-only.
4. **Stage gate** (`execution/router.py`): only hypotheses in paper/live stages can trade; live needs a human promotion.
5. **Watchdog** (cron `aster-risk-watchdog`): alerts when the kill switch is on or losses reach 75% of a limit.
6. **Agent rules** (SOUL.md): the weakest layer; never relied upon alone.

## Limits (see risk_limits.yaml for current values)
Daily loss, drawdown from peak, gross and net leverage, per-asset concentration, order notional, orders per day, allowed symbols, shorts, price sanity (deviation from market, staleness). In live mode all % limits use min(equity, capital_cap_usd).

## Reporting (every daily report)
Equity, daily P&L, drawdown from peak, gross/net exposure, per-asset weights, orders sent/rejected and reasons, kill status, realised vs modelled slippage, funding paid.

## Strategy-level risk
- Size by volatility target, not by conviction. Default book target vol 30-40% annualized for crypto spot; never above what the max drawdown limit can absorb (rule of thumb: expected worst drawdown ~ 2-3x annual vol for trend strategies).
- Kelly: never more than 0.25 Kelly on estimated inputs (`portfolio/sizing.py::fractional_kelly`).
- Correlation: in crises, crypto correlations go to 1. Treat a book of 5 coins as ~1.5 independent bets in stress.
- Venue risk: no more than the sub-account cap on any single exchange; withdraw profits above cap (human action).
- Stablecoin risk: monitor the quote asset peg; a depeg > 1% is a kill-switch event.

## Incident procedure
1. Kill switch on (`desk kill on --reason ...`) if anything is unexplained: unexpected position, rejected orders piling up, data outage, exchange incident, journal verification failure.
2. Report to Samuel with journal excerpts and `desk risk status`.
3. Post-mortem in `reports/`, lesson in the ledger. Only Samuel clears the kill switch.
