# Holdout seal — audit, options, decision required

**Date**: 2026-10-15  
**Author**: Aster  
**Goal**: Item A of the post-review backlog (cf. `Status.md` § 4)  
**Status**: **DECISION REQUIRED from Samuel before any code is written**

## 1. The brief

> "Coupure stricte : aucune donnée postérieure au 2024-07-01 en exploration; seules les hypothèses autorisées peuvent utiliser ces données en holdout. Un holdout ne se consulte qu'une fois."

> "Demande mon accord avant holdout, paper trading, action irréversible, arbitrage de priorité ou chantier substantiel."

A "holdout" here means: a contiguous, sealed, never-touched time window that a preregistered hypothesis may read **exactly once** to confirm or kill the dev result. It must be a true out-of-sample test, not a re-use of the exploration sample.

## 2. What we have on disk

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

## 4. The options

### Option A — Convention holdout on the last 3 months of the in-store window

- **Window**: `2024-04-01 → 2024-06-30` (3 months, 12 symbols).
- **Status**: read by 8 studies already; we declare it "holdout" by convention and **forbid any future exploratory code from reading it** until a hypothesis is registered.
- **Pros**: zero cost, immediate. We can register this convention in code (`HOLDOUT_START = pd.Timestamp("2024-04-01", tz="UTC")`) and have a guard that raises if exploration code touches it.
- **Cons**: **the dev sample is contaminated**. The dev hypotheses that would read this holdout have been informed by descriptive statistics on the same dates (vol regimes, mean returns, correlation structure). The contamination is **statistical**, not just procedural: a 0.65 Sharpe at dev that survives on 0.62 at holdout may be the same number within noise, or it may be a leak. We would need to be very explicit about this in any report that uses the result.
- **Risk for live**: a contaminated holdout under-prices live decay. We would still need a fresh 28-day paper before any live decision.

### Option B — Acquire post-2024-07-01 data and seal a true holdout

- **Window**: any contiguous range, e.g. 2024-07-01 → 2024-12-31 (6 months) or 2025-01-01 → 2025-06-30 (6 months).
- **Status**: truly untouched in our local store.
- **Pros**: a real holdout. The whole point of the brief.
- **Cons**:
  - **Cost**: Tardis / Kaiko / Databento / CoinAPI monthly subscription. Budget decision for Samuel.
  - **New cutoff seal**: we would re-define `EXPLORATION_CUTOFF` and `HOLDOUT_START` to a new value. This is a config change with risk if any other code still depends on the old 2024-07-01 cutoff (it does — the `read_local` raises on `>= 2024-07-01`).
  - **Latency**: download, manifest re-build, audit re-run, tests re-run. Days to weeks.
  - **Re-calibration**: any prior family trial count for the Deflated Sharpe Ratio may need a re-think (the dev/holdout boundary is part of the family definition).
- This is **item 15 of the existing BACKLOG**. It has been waiting for a budget OK.

### Option C — No holdout; only walk-forward + purged k-fold + DSR

- **What it means**: rely on time-series CV and DSR/PBO without a sealed holdout.
- **Cons**: explicitly violates the brief ("Un holdout ne se consulte qu'une fois" implies one exists).

### Option D — Hybrid: keep Option A as a *convention* until Option B lands

- We ship Option A today (convention holdout, contamination noted), in parallel we plan Option B (data acquisition).
- The convention holdout can be **replaced** by the real one when the data arrives. Any hypothesis read on the convention holdout must be re-read on the real one. That re-read is **not** an additional holdout read — it is a correction of the original.

## 5. Recommendation

**Option D**, with a clear-eyed note that Option A is a *convention*, not a *true* holdout. This is the only way to make forward progress without waiting for a budget decision, and it preserves the option of a real holdout later.

**But** — per the brief — Samuel's explicit agreement is required before this is written into the code. This is exactly the "holdout / irreversible / substantial change" gate.

## 6. What I would do if Samuel approves Option D

- Add `HOLDOUT_START = pd.Timestamp("2024-04-01", tz="UTC")` in `r2_klines.py` next to `CUTOFF`.
- Add a `read_holdout(symbol)` API that returns only `index >= HOLDOUT_START` and `index < CUTOFF`, with a global "holdout has been read" flag (single-shot).
- Add a `holdout_consumed` check in `read_local` so exploration code raises if it accidentally reads into the holdout window.
- Add tests:
  - `read_local` raises on `index >= HOLDOUT_START` for any non-holdout caller.
  - `read_holdout` succeeds once, raises on second call.
  - The holdout window is exactly `2024-04-01 → 2024-06-30` for all 12 spot symbols.
- Add `research/notes/2026-10-15-holdout-seal.md` documenting the contamination caveat.
- Update `BACKLOG.md` to mark item A done (with the caveat).
- Update `Status.md` § 3 "where we are by goal".

Nothing in `risk/`, `execution/`, `config/risk_limits.yaml`, or `policies/` would be touched.

## 7. What I will NOT do without explicit OK

- Define a `HOLDOUT_START` value in code.
- Touch the `CUTOFF = 2024-07-01` value.
- Add a `read_holdout` API.
- Add the contamination-warning note as if it were the final word.

## 8. What I need from Samuel

A short message: **A, B, C, or D** (A, B, C = the option as described; D = the hybrid with explicit contamination acknowledgement). If D, I proceed with the § 6 plan. If anything else, I want to know before writing code.

---

**Evidence sources** (all in this repo):
- Data audit: `research/notes/2026-10-15-audit-data.md` (would be created on § 6).
- MAP: `research/MAP.md`.
- BACKLOG: `research/BACKLOG.md`.
- EXPLORATION_JOURNAL: `research/EXPLORATION_JOURNAL.md`.
- Code: `src/aster/data/r2_klines.py:27` (`CUTOFF`), `src/aster/data/r2_klines.py:270` (`read_local` raises on post-cutoff).
- Tests: `tests/test_r2_klines.py` (current test suite, 333 passing).
