# Holdout seal — audit, options, decision required

**Date**: 2026-10-15  
**Author**: Aster  
**Goal**: Item A of the post-review backlog (cf. `Status.md` § 4)  
**Status**: **DECISION REQUIRED from Samuel before any code is written**

## 1. The brief

The original convention window is contaminated: prior research had already used
it. Q1 replaces it with a true sealed holdout whose strict boundary is
`2024-07-01T00:00:00Z`.

- Exploration reads remain exclusively in `data/r2/` and reject any timestamp
  at or after the boundary.
- Post-cutoff imports live only in `data/sealed/market/spot/klines_1m/`.
- Each sealed manifest records only `source`, `key`, SHA-256, byte size, row
  count, first/last timestamp, and timestamp unit. It intentionally contains
  no market record values, calculated returns, statistics, or import timestamp.
- `read_holdout()` requires an explicit ledger and persists a one-shot
  `(hypothesis_id, symbol)` consumption record atomically in SQLite. A fresh
  process cannot consume the same pair again.

No actual sealed data was opened, analysed, printed, or plotted while making
this change; the tests create synthetic Parquet fixtures only.

## 2. Prior audit and the retired convention

Audit of `data/r2/market/spot/klines_1m/` (2026-10-15):

- 722 manifests, 31,371,418 rows, 12 spot symbols, 83 monthly partitions.
- Earliest: 2017-08-18 (BTC, ETH). Latest: 2024-06-30 23:59:00 UTC.
- `cutoff_exclusive = 2024-07-01T00:00:00+00:00` in 100 % of manifests.
- Source: `cloudflare-r2`; fetched 2026-10-13.

AggTrades (6 symbols) covers 2024-06 only. OHLCV 1d derived for 5 symbols.

`src/aster/data/r2_klines.py:27` defines a single `CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")` and `read_local()` raises if any row is `>= CUTOFF`. There is **no train / dev / holdout split** in the code today — the file is one monolithic exploration store.

## 3. What we have read so far (exploration footprint)

7 axes closed since 2026-10-14 (cf. `EXPLORATION_JOURNAL.md`, `BACKLOG.md` items 1-17, `MAP.md`):

1. Intraday term structure
2. Ichimoku full system
3. OU mean-reversion + pairs
4. Vol risk premium
5. CFA-style TA enriched (Camarilla/Woodie/Fib)
6. ML XGBoost purged k-fold
7. Markov-switching Hamilton 1989 (BTC/ETH/BNB/SOL)
8. Panel N1 alts (BNB/XRP/SOL/LINK/DOGE) — 640 cells

These 8 studies (axes 1-7 + N1-alt panel) have used the **entire 2017-08 → 2024-06 window** for descriptive statistics, BH-FDR, placebos, lead-lag grids, regime labels, residual factor mining, etc. Every asset and every timestamp inside the cutoff has been touched by some form of analysis.

**There is no untouched window inside the local data store.**

## 4. Resolution and implementation evidence

The `2024-04-01 → 2024-06-30` convention is contaminated validation data, not a
holdout. It remains pre-cutoff and may be read by exploration. Q1 adopts the
post-cutoff boundary and isolation model without running an import.

Focused tests use synthetic Parquet only and verify:

1. an exploration-oriented path guard rejects `data/sealed/`;
2. a pre-cutoff partition is refused by the sealed importer before remote I/O;
3. a sealed import writes only the approved metadata manifest schema and the
   metadata validates against the synthetic Parquet file;
4. `read_holdout()` requires the ledger gate and returns post-cutoff data only;
5. after a first sealed read, a separate Python process is refused for the same
   `(hypothesis_id, symbol)` pair.

The importer was not invoked against R2, Binance Vision, credentials, or any
market-data file by Q1. Population of the sealed store requires a later,
separately authorised import run.

## 5. Historical record (superseded)

The following decision language is retained solely as an audit record of the
superseded convention design.

### Former option A

`2024-04-01 → 2024-06-30` was a three-month convention window, but it had
already been used by prior research and therefore could not provide independent
evidence.

### Former option B

Acquire post-2024-07-01 data and seal it as the true holdout. Q1 implements the
storage and access controls for this option; it does not acquire or inspect data.

---

**Evidence sources** (all in this repo):
- Data audit: `research/notes/2026-10-15-audit-data.md` (would be created on § 6).
- MAP: `research/MAP.md`.
- BACKLOG: `research/BACKLOG.md`.
- EXPLORATION_JOURNAL: `research/EXPLORATION_JOURNAL.md`.
- Code: `src/aster/data/r2_klines.py:27` (`CUTOFF`), `src/aster/data/r2_klines.py:270` (`read_local` raises on post-cutoff).
- Tests: `tests/test_r2_klines.py` (current test suite, 333 passing).
