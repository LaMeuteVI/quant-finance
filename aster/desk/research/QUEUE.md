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

- **Q0b — Restore the local data store.** `BLOCKED_ON legacy data-check contract: only 5 daily symbols, while Q0b requires green on 12 R2 symbols`
  After `git pull`, `aster/desk/data` must be a real directory or a symlink to the real store, never a link to itself. `ls -la aster/desk/data`; if it is still a link to itself, `rm aster/desk/data` (removes only the link). Find the store: `find / -xdev -name '*.manifest.json' -path '*r2*' 2>/dev/null | head` and `ls /root/marketdata-binance-phase1`. Then link it (`ln -s <store root> aster/desk/data`) or re-run `uv run desk data import` (GREEN). DoD: `uv run desk data check` green on the 12 symbols, `uv run pytest -q` green, a one-line note in `research/atlas/data-sources.md` saying where the store lives.

- **Q1 — True sealed holdout (D2).** `READY` · skills: `quant-backtest-hygiene`, `lopez-de-prado-afml` ch11–12
  Import post-cutoff months (2024-07 → latest available) for every symbol into `data/sealed/`, from the existing R2 bucket if it holds them, else from `data.binance.vision`. The import computes only sha256, row count, first/last timestamp and timestamp unit; no returns, no statistics, no plots. `read_local()` and every research module must be unable to read `data/sealed/` (test it). `read_holdout()` reads the sealed store, single-shot per (hypothesis, symbol), persisted in the ledger rather than in memory. Update `research/notes/2026-10-15-holdout-audit.md` and the `r2_klines.py` docstring: option A becomes the contaminated dev-validation window.
  DoD: tests proving (a) exploration paths raise on sealed data, (b) single-shot is persisted across processes; manifest committed; no data value printed in logs.

- **Q2 — Missing universe members.** `READY` · depends on Q1
  The brief lists RENDER, ONDO, PUMP and HYPE (perp) besides the 12 imported symbols. Import whatever exists pre-cutoff into the research store and the rest into the sealed store. Assets with no pre-cutoff history are holdout-only panel members: record this in `research/atlas/data-sources.md`.

- **Q3 — Perpetual futures data, pre-cutoff (D5).** `READY`
  From `data.binance.vision` USDⓈ-M: `fundingRate`, 1m klines, `premiumIndexKlines`, `markPriceKlines`, `metrics` (open interest, long/short ratios, available from about 2020–2021) for BTC, ETH and every alt with a perp. Same provenance and cutoff discipline as spot. Extend `desk data check`.
  DoD: `research/atlas/data-sources.md` (source, coverage, known gaps); data check green; tests on the parser.

- **Q4 — Bars and aggTrades.** `READY`
  Finish the 5m/15m/1h/4h bars marked partial in `Status.md`. Import spot aggTrades for BTC and ETH for 2022-01 → 2024-06 (free, Binance Vision; size-check the disk first) and build volume, dollar and taker-imbalance bars from them (afml ch02). This replaces the "1 month only" limitation of the former axe 8.

## Block P: make `desk backtest` able to test what the research finds (critical path)
Audit 2026-10-16 (`aster/AUDIT.md`): the pipeline can only backtest daily, close-price-only strategies on a flat cost. None of the brief's flow, funding, basis or intraday ideas can be expressed. These items come before any new hypothesis.

- **P1 — Multi-input strategy contract.** `READY` · skills: `quant-backtest-hygiene`, `lopez-de-prado-afml` ch11–14
  `Strategy.target_weights(data)` receives a `MarketData` object (close, open, high, low, volume, quote_volume, taker_buy, trades, funding, premium, open interest), each causal and aligned to bar close. Close-only strategies keep working through an adapter. The truncation look-ahead test runs on every field. Changing `src/aster/strategies/base.py` and `backtest/pipeline.py` is GREEN (not risk/ or execution/); keep every existing test green and add tests per field.
- **P2 — Per-hypothesis timeframe and instrument.** `READY` · depends on P1
  Timeframe and instruments (spot vs USDⓈ-M perp, per leg) come from the preregistration, not from `config/desk.yaml`. Bars 1h/4h/15m/5m built from the R2 minute store via `r2_backtest_store`. Funding is charged on perp legs only (today it is charged on every held weight). Delta-neutral pairs (spot long + perp short) must be expressible.
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

## Done
(move items here with date, commit and artefact)
