# Data policy

## Sources
| Data | Source | Notes |
|---|---|---|
| Spot OHLCV | exchange public API via ccxt (`desk data fetch`) | default Binance; bars in UTC, forming bar dropped |
| Perp funding | ccxt `fetch_funding_rate_history` (`--funding`) | summed per bar |
| Order book / trades | ccxt (future module) | needed for intraday cost models |
| On-chain, sentiment, news | only via a written source note in the memo | treat as untrusted, timestamp at publication time, not at event time |

Adding a source: document it here (what, why, latency, revision behaviour, licence) and store with `data/store.py` so a manifest is written.

## Provenance
- Every dataset has a `.manifest.json`: source, fetch time, rows, span, sha256. Backtest reports record the data quality report and can be traced to manifests.
- Data is never edited by hand. Corrections are code (a cleaning function) with a test and a note.

## Point-in-time
- A value is usable at the time it became known, not the time it refers to. Funding is known at its settlement time; news at its publication timestamp; on-chain metrics after confirmation + indexer lag.
- Universes are point-in-time for cross-sectional research (see backtest_standard.md, survivorship).

## Quality gate
`desk data check` before any research session. Errors block the pipeline. Warnings (gaps, outliers, zero volume) must be inspected and mentioned in the report if they touch the sample.

## Secrets and privacy
- API keys live in `desk/config/.env` or the human's shell only. Never printed, logged, committed, sent to a model, or written to memory.
- No personal data in the desk.
