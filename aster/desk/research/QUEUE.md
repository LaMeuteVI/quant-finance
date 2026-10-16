# Research queue: the standing goal

> Single source of truth for **what to do next**. It replaces any list of items held in chat ("A–G", "B–G"...).
> Worked top to bottom by the `aster-autopilot` skill. Decisions and the autonomy charter: `research/DECISIONS.md`.
> Statuses: `READY` · `IN_PROGRESS (date)` · `BLOCKED_ON <id or reason>` · `DONE (date, commit, artefact)` · `IDEA` (not yet scheduled) · `RED` (needs Samuel).
> Every exploration item: preregistration note first, pre-cutoff data only, FDR over the whole grid, placebo, effect size with interval, net-of-cost reading against `research/atlas/costs.md`, `uv run pytest -q` green, MAP/BACKLOG updated, commit pushed.

## Former labels
A = holdout seal (done as option A, superseded by Q1) · B = Q6 · C = Q9 · D = Q10–Q12 · E = Q13–Q14 · F = Q17 · G = Q16.

## Block 0: hygiene and infrastructure

- **Q0 — Integrate the N1 correction worktree.** `DONE (2026-10-16, 9e40c01; follow-up: the commit also tracked a self-referential `aster/desk/data` symlink, untracked again in the next commit, see Q0b)`
  The Kanban card `t_5b11e143` (prereg-conformant SMA states, placebo 14d→7d, panel BH) left uncommitted changes in `.worktrees/`. Review the diff, run the targeted tests and the full suite, commit on `wt/aster-n1-alts`, merge into `feat/aster-agent`, push. Make sure `data/` inside the worktree is a symlink or gitignored, never committed. Remove the stale `.worktrees/t_1a257193` entry if it is empty.
  DoD: `git status` clean in the main tree and the worktree; merged commit hash in the N1-alts note; 0/640 result re-stated from the corrected artefacts.

- **Q0b — Restore the local data store.** `DONE (2026-10-16, 2925bf1, research/notes/2026-10-16-Q0b-data-store.md)`
  722 pre-cutoff partitions, 12 symbols, `desk data audit-r2 --sha256` green. The original DoD wrongly named `desk data check`, which only checks the legacy 5-symbol daily ccxt store (`data/ohlcv`), absent by design. Feeding `desk backtest` from R2 (`r2_backtest_store`) and making `desk data check` cover the R2 store are part of P2.

- **Q1 — True sealed holdout (D2).** `DONE (2026-10-16, dd056b6, research/notes/2026-10-15-holdout-audit.md, aster/desk/tests/test_r2_klines.py + test_store.py)`
  Code: `reject_sealed_path()` blocks every exploration reader including `data.store.read()`; `read_holdout(symbol, *, hypothesis_id, ledger)` requires a ledger and atomically persists a `(hypothesis_id, symbol)` consumption record via `Ledger.consume_sealed_holdout()`; `transfer_sealed()` writes only metadata manifests (no record values) and refuses pre-cutoff partitions before any remote I/O. Tests: exploration paths raise on sealed data, `read_holdout` raises across a fresh process for a previously consumed pair, transfer rejects pre-cutoff objects without remote I/O. 349 pytest green; warnings unchanged. Convention `[2024-04-01, 2024-07-01)` retired and demoted to contaminated pre-cutoff dev-validation window. **Sealed store is intentionally empty** — population requires a separately authorised import run before any hypothesis can pass its dev gate into holdout.

- **Q2 — Missing universe members.** `DONE (2026-10-16, 72eb80a, research/notes/2026-10-16-Q2-prereg.md, research/atlas/data-sources.md, aster/desk/src/aster/scripts/probe_universe.py)`
  Probe of RENDER, ONDO, PUMP, HYPE across `local-r2-spot`, `data.binance.vision-spot`, `data.binance.vision-um` returns `exists=no` for all 12 cells (4 symbols × 3 channels). None of the four brief members has pre-cutoff data on any free public channel we currently rely on. Decision: route RENDER/ONDO/PUMP to the post-cutoff sealed store when Q1's import is run; otherwise treat them as holdout-only panel members. HYPE perp channel stays under Q3. 353 pytest green (4 new probe tests).

- **Q3 — Perpetual futures data, pre-cutoff (D5).** `DONE (2026-10-16, 924434f, research/notes/2026-10-16-Q3-prereg.md, research/atlas/data-sources.md, aster/desk/src/aster/data/funding_rate.py, aster/desk/src/aster/scripts/probe_perp_universe.py)`
  Probe of `data.binance.vision` USDⓈ-M monthly ZIPs: `fundingRate` is present for **all 12 panel symbols** pre-cutoff (first-month per symbol matches perp listing dates). `premiumIndexKlines`, `markPriceKlines` and `metrics` return 404 on the public archive paths tried → documented as known gaps, revisit only if F1/F2 need OI for sizing/risk (paid source = RED per D3). Importer `aster.data.funding_rate.import_archive` plus CLI `desk data import-funding` / `desk data audit-funding` added; each Parquet partition ships a metadata-only manifest with SHA-256 and row/time-bound/cutoff checks. Imported 538 pre-cutoff partitions / 12 symbols / 48 879 rows / 2.16 MB under `data/r2/market/futures/um/funding_rate/`; `audit-funding --sha256` green. F1 and F2 unblock on the dev side once P1–P4 land; this store is their primary input. 361 pytest green (8 new tests).

- **Q4 — Bars and aggTrades.** `DONE (2026-10-16, 437d08d, research/notes/2026-10-16-Q4-prereg.md, research/atlas/data-sources.md, aster/desk/src/aster/data/aggtrades.py, aster/desk/src/aster/data/information_bars.py, aster/desk/src/aster/cli.py)`
  Importer `aster.data.aggtrades.import_archive` reads Binance Vision headerless 8-column CSV, drops 3 debugging columns and ships a 5-column Parquet (agg_trade_id:int64, price:float64, quantity:float64, transact_time:int64, is_buyer_maker:bool) with a metadata-only manifest (sha256, size_bytes, rows, start/end, cutoff_exclusive). Cutoff strictly pre-2024-07-01 UTC; any post-cutoff row raises `CutoffViolationError`. CLI: `desk data import-aggtrades --root <zips>`, `desk data audit-aggtrades [--sha256]`, `desk data build-volume-bars --family {volume,dollar,taker_imbalance}`. Bar builders implement afml ch02 §2.3 (volume / dollar / taker-imbalance) with per-day rolling 30-day median thresholds; aggregation vectorised via a single `groupby` (was O(N×B), now O(N)). 7 unit tests on the builders (sustained trading, threshold stability, empty input, dollar notional, imbalance extremes, balanced flow, causal close label) + 7 on the importer/audit. Imported 4 pre-cutoff Parquet partitions / BTCUSDT / 107 730 009 rows / 1.37 GB under `data/r2/market/spot/aggtrades/`; `audit-aggtrades --sha256` green. Smoke test on 1M-row sample: 863 volume bars, 1 712 dollar bars, 5 taker-imbalance bars; imbalance mean ≈ −0.024, std ≈ 0.009. The remaining 56 partitions (BTC 2022-05→2024-06 + ETH 2022-01→2024-06) are downloading in the background; the Q4 commit is the code + tests + first 4 partitions, not a frozen snapshot of disk state. 375+14 = 389 pytest green.

## Block P: make `desk backtest` able to test what the research finds (critical path)
Audit 2026-10-16 (`aster/AUDIT.md`): the pipeline can only backtest daily, close-price-only strategies on a flat cost. None of the brief's flow, funding, basis or intraday ideas can be expressed. These items come before any new hypothesis.

- **P1 — Multi-input strategy contract.** `IN_PROGRESS (2026-10-16)` · skills: `quant-backtest-hygiene`, `lopez-de-prado-afml` ch11–14
  `Strategy.target_weights(data)` receives a `MarketData` object (close, open, high, low, volume, quote_volume, taker_buy, trades, funding, premium, open interest), each causal and aligned to bar close. Close-only strategies keep working through an adapter. The truncation look-ahead test runs on every field. Changing `src/aster/strategies/base.py` and `backtest/pipeline.py` is GREEN (not risk/ or execution/); keep every existing test green and add tests per field.
- **P2 — Per-hypothesis timeframe and instrument.** `READY` · depends on P1
  Timeframe and instruments (spot vs USDⓈ-M perp, per leg) come from the preregistration, not from `config/desk.yaml`. Bars 1h/4h/15m/5m built from the R2 minute store via `r2_backtest_store`; `desk data check` extended to the R2 and sealed stores (today it only checks the absent legacy `data/ohlcv` daily store). Funding is charged on perp legs only (today it is charged on every held weight). Delta-neutral pairs (spot long + perp short) must be expressible.
- **P3 — True holdout in the pipeline.** `READY` · depends on Q1
  Today `holdout_frac: 0.25` puts the holdout inside the pre-cutoff window, which exploration has already read. New rule: dev = data before 2024-07-01, holdout = sealed store from 2024-07-01, read through `consume_holdout`. Test that a dev run cannot load a single sealed row.
- **P4 — Realistic costs and capacity (brief section 9).** `READY`
  Replace the flat 10 + 5 bps with the per-asset, per-hour cost grid from `research/atlas/cost-grid.csv` plus square-root impact on ADV. Report net Sharpe at 100k / 1M / 10M / 50M USD and capacity (max AUM with net Sharpe ≥ 1) in every `report.json`. Keep the ×2 and ×3 stress tests.
- **P5 — Walk-forward and PBO by default.** `READY`
  Every dev run also reports a walk-forward (expanding, embargoed) and, when params are swept, a CSCV/PBO, using `validation/cv.py` and `validation/pbo.py`.

## Fast track: three priors strong enough to preregister as soon as P1–P4 are done
These come from the literature and the brief's mechanism list, not from our data. This makes them cheap in trial count and quick to bring to a dev verdict. Each one: memo → Skeptic → ledger preregistration (ORANGE) → at most 5 versions → verdict. Holdout and paper stay RED.

- **F1 — Funding carry, delta-neutral.** `BLOCKED_ON P1–P4, Q3`
  Long spot / short perp (and the reverse when funding is negative) on BTC, ETH and liquid alts, entered when expected funding net of fees and basis drift is above costs. Mechanism: leveraged longs pay for the hedge. Main risks: funding regime flips, basis blow-outs in crashes, venue risk. Capacity potentially large on BTC/ETH.
- **F2 — Funding and premium as a crowding signal.** `BLOCKED_ON P1–P2, Q3, Q8 descriptive`
  Directional perp position against extreme funding or premium z-scores, conditioned on open-interest change. Mechanism: crowded leveraged positioning is forced out (liquidations).
- **F3 — Vol-targeted trend ensemble on the panel.** `BLOCKED_ON P1, P4`
  Blend of 20–120 day trend signals, long/short perps, volatility targeting, 8–10 assets, XMR kept as a survivorship guard. Same idea as the rejected `H-20261013-001`, so the trials count **in the existing family `btc-daily-tsmom`**: no new family to reset the DSR. It differs in diversification, shorting and sizing, so the preregistration must say why it should pass where the BTC long/cash version failed its drawdown floor.

## Block 1: the unexplored intraday and perp space (highest priority after Block P)
Previous N1–N5 work was mostly at daily horizons. The brief's intraday cells are open.

- **Q5 — BTC/ETH intraday N2.** `READY` · depends on Q4 · skills: `tsay-analysis-financial-time-series` ch02/ch05, `cfa-quantitative-methods` ch09, `lopez-de-prado-afml` ch17–18
  Horizons 1m → 1d: return and absolute-return autocorrelation, Lo–MacKinlay variance ratio, Hurst/DFA per horizon (momentum or mean-reverting, at which scale?), seasonality (hour UTC, weekday, funding fixings 00/08/16, session opens, month-end, weekends), intraday jump detection and post-jump continuation vs reversal, CUSUM/SADF. Frozen minutes excluded explicitly.

- **Q6 — BTC/ETH intraday flow (N5 on tick-derived bars; former B / axe 8).** `READY` · depends on Q4
  Taker imbalance, signed cumulative flow, Kyle λ, Amihud, Roll, VPIN on volume bars. Question: does aggressive flow predict the next 1m–4h return (continuation) or get absorbed (reversal), conditional on liquidity, volatility and hour? Absorption horizon. Compare with the kline proxy to measure what the proxy loses.

- **Q7 — Intraday lead-lag grid (section 6.2).** `READY` · depends on Q4
  BTC→alts, ETH→alts, alt→alt, both directions, lags 1, 2, 5, 15, 30 min, 1, 4, 12 h, on raw **and** factor-residual returns; BTC flow vs BTC return as predictor; VAR/Granger; block-bootstrap CI, BH-FDR on the full grid, stability per year, frozen-minute exclusion, edge in bps vs round-trip cost per hour UTC.

- **Q8 — Funding, basis and carry.** `READY` · depends on Q3 · skills: `chan-machine-trading`, `hull-derivatives`, `grinold-kahn-apm`
  Funding persistence and predictability; funding fixings seasonality; extreme funding / premium as a crowding signal for the next spot and perp returns; open-interest shocks; cash-and-carry and cross-sectional funding carry net of fees, borrowing and basis risk; capacity. Mechanism: leveraged demand pays for the hedge. Highest prior among the brief's mechanisms.

## Block 2: alt depth and inter-asset (former C, D, E)
One `delegate_task` sub-agent per asset, in parallel, never reading each other; Skeptic after.

- **Q9 — N2 per alt (BNB, XRP, SOL, LINK, DOGE, XMR; then AAVE, FET, NEAR, SUI in panel).** `READY` · former C · reuse the Q5 code
- **Q10 — N3 per alt** (GARCH/EGARCH/GJR, inverse leverage effect, HAR-RV, Diebold–Mariano vs naïve, compression → expansion). `READY` · former D
- **Q11 — N4 per alt** (threshold/Markov/HMM, BTC-correlation regimes, re-read of N1–N3 by regime). `READY` · former D
- **Q12 — N5 per alt** (flow on klines, then on aggTrades where Q4 is extended). `READY` · former D
- **Q13 — Dependence structure (6.1).** `READY` · former E · skills: `lopez-de-prado-ml-asset-managers` ch02–04, `tsay` ch08–09, `hull-risk-management` ch11
  Denoised/detoned correlation by horizon and regime, clustering, DCC, tail dependence in crashes.
- **Q14 — Panel and relative value (6.3).** `READY` · former E · skills: `pairs-trading-partial-cointegration`
  Fixed-effects panel tests of every surviving signal; sector pairs (L1 SOL/NEAR/SUI, AI FET/RENDER, payments XRP/DOGE, DeFi AAVE/LINK); intraday residual mean reversion; cross-sectional momentum/reversal on residuals at 1h–1w. State the narrow cross-section and survivorship bound in the report.

## Block 3: literature, atlas, synthesis
- **Q15 — ETH `fvg_down_entry_h1` follow-up.** `IDEA` · from BACKLOG item 8; re-test on the panel before anything else.
- **Q16 — Veille (former G, section 7).** `READY`
  SSRN, arXiv q-fin, AQR/Man/Robeco/Two Sigma, Kaiko/Coin Metrics/Glassnode on crypto return predictability, funding, microstructure, intraday seasonality. Per source: reference, claim, period, assumed costs, ladder level. Top 3 claims become replication sub-items in this queue.
- **Q17 — Atlas and asset dossiers (former F).** `READY` after each block
  One `research/assets/<SYMBOL>.md` per asset with the level reached (N0 → N7) at the top, linking the dated artefacts; `research/atlas/` lead-lag, regimes, costs, data-sources. MAP updated.
- **Q18 — N6 financial ML.** `BLOCKED_ON a primary feature from Q5–Q14`
  Meta-labeling on primary signals, triple barrier, purged CV with embargo, MDA/SFI by feature clusters, trial count reported.
- **Q19 — N7 synthesis and preregistration.** `BLOCKED_ON Q5–Q14`
  Per asset: signal map (horizon, IC with CI, corrected t, IC decay, bps vs cost, regime dependence, capacity, correlation to other signals). Register the 1–3 most mature hypotheses (ORANGE), dev backtests (ORANGE), Skeptic and Breaker, capacity at 100k/1M/10M/50M. **Holdout read and paper are RED.**
- **Q20 — Weekly "État de la recherche".** `READY`, every Sunday: matrix, candidates, what died and why, effort reallocation.
