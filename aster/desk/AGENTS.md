# Aster desk: workspace rules

This directory is the Aster desk. You (Aster, or any subagent working here) follow these rules. The policies in `policies/` are binding; this file is the map.

## Layout
```
config/        desk.yaml (universe, costs, gates)  risk_limits.yaml (HARD limits, protected)  .env (keys, never read aloud)
policies/      research_protocol, backtest_standard, data_policy, risk_policy, execution_policy, promotion_policy
templates/     hypothesis, research memo, backtest report, post-mortem, strategy file
src/aster/     data/ backtest/ validation/ ledger/ risk/ execution/ portfolio/ research/ strategies/ cli.py
tests/         must stay green: `uv run pytest`
research/      memos: research/YYYY-MM-DD-<role>-<slug>.md
backtests/     pipeline artifacts, one folder per trial (written by `desk backtest`, never by hand)
journal/       decisions.jsonl: hash-chained, append-only (written by code only)
reports/       daily/weekly reports: reports/YYYY-MM-DD-<kind>.md
memory/        ledger.db: hypotheses, trials, events, lessons
state/         paper account, day books, KILL switch file
data/          parquet + provenance manifests (gitignored)
```

## Commands (run from this directory, always through uv)
| Need | Command |
|---|---|
| Refresh market data | `uv run desk data fetch [--funding]` then `uv run desk data check` |
| What was already tried? | `uv run desk ledger list [--status rejected] [--text momentum]` |
| Register a hypothesis | `uv run desk ledger new --title ... --statement ... --mechanism ... --falsification ... --prediction '{"sharpe_ann_min":1.0}' --family ... --market crypto-spot --source <role> --strategy <name>` |
| Backtest (dev sample) | `uv run desk backtest --hypothesis H-... --strategy <name> --params '{...}' --notes "why this version"` |
| Advance a stage | `uv run desk ledger status H-... backtest_passed --reason "..."` (refused without passing evidence) |
| Holdout (once) | `uv run desk backtest --hypothesis H-... --strategy <name> --sample holdout` |
| Record a lesson | `uv run desk ledger lesson H-... "text"` |
| Paper trade one bar | `uv run desk trade run --hypothesis H-... --broker paper` |
| Paper review | `uv run desk paper review --hypothesis H-... [--record]` |
| Risk / kill | `uv run desk risk status`, `uv run desk kill on --reason "..."` |
| Overfitting across configs | `uv run desk pbo returns_matrix.csv` |
| Journal integrity | `uv run desk journal verify` |

Human-only, never attempt: `desk promote`, `desk kill off`, editing `risk_limits.yaml`, arming live (`ASTER_LIVE_ARMED`).

## Writing a strategy
1. Copy `templates/strategy_template.py` to `src/aster/strategies/<name>.py`; register it in `src/aster/strategies/__init__.py`.
2. Pure function of close prices -> target weights, causal (row t uses data <= t). No costs, no execution, no I/O inside.
3. Bump `version` (semver) for every change that alters weights. The ledger counts versions per hypothesis (max 5).
4. Add a unit test in `tests/` proving the rule fires when it should; `uv run pytest` must pass before the first backtest.
5. The pipeline runs the truncation look-ahead test automatically. A failure means the strategy is broken, not the test.

## Coding conventions
- Python 3.12, pandas/numpy, type hints, small pure functions. UTC tz-aware indexes everywhere.
- No new dependency without saying why in the commit message. No network calls in tests.
- Never weaken a test, a gate or a limit to make something pass. If a check is wrong, say so and propose the fix to Samuel.
- Every number in a report comes from an artifact (report.json, ledger, journal). If you cannot point to the file, do not write the number.

## Which skill when (library in ~/Desktop/Livres/Skills)
Start with `quant-orchestrator`. Backtest validation: `quant-backtest-hygiene` + `lopez-de-prado-afml` (ch. 7 CV, ch. 11-14 backtesting, DSR). Execution and practical algo: `chan-machine-trading`. Signal/forecast stats: `tsay-analysis-financial-time-series`, `diebold-mariano-forecast-accuracy`. Portfolio and IR logic: `grinold-kahn-apm`, `lopez-de-prado-ml-asset-managers`. Risk: `hull-risk-management`. Options/vol (crypto options, Deribit): `hull-derivatives`, `gatheral-volatility-surface`, `passarelli-option-greeks`. Pairs/stat-arb: `pairs-trading-partial-cointegration`. Formulas: `quant-verification`.
