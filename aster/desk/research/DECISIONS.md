# Decisions log and autonomy charter

> Read with `research/QUEUE.md` at the start of every session (skill `aster-autopilot`).
> Samuel can revoke any line by editing this file. Otherwise every decision here is **already taken**: do not ask about it again.

## 1. Autonomy charter

| Level | Meaning | Covers |
|---|---|---|
| **GREEN** | Do it without asking. | Picking and ordering QUEUE items; scope inside an item; exploration preregistrations; code + tests in `src/aster/research/`, `src/aster/data/` and `tests/`; descriptive studies on pre-cutoff data; importing **free public** data (Binance Vision, the existing R2 bucket) into the local store, including post-cutoff data into the **sealed** store (Q1); `delegate_task` sub-agents; Kanban goal cards for QUEUE items; commits and pushes to `feat/aster-agent`; merging your own research worktrees once tests pass; updating QUEUE/MAP/BACKLOG/Status/atlas/assets. |
| **ORANGE** | Do it, log one line below, keep going. | Registering a ledger hypothesis that follows `policies/research_protocol.md`; dev backtests through `desk backtest`; rejecting a hypothesis with its lesson; closing one signal class as null after the coverage check (section 3); choosing between two valid methods; adding a new QUEUE item above the current top. |
| **RED** | Stop and ask Samuel, with options and a recommendation. | Any spending (paid data, paid APIs, compute); live trading, keys, secrets, withdrawals; `desk promote`, `desk kill off`; editing `risk/`, `execution/`, `policies/`, `config/risk_limits.yaml`; **reading a holdout** (`--sample holdout`, `read_holdout`); starting paper trading for a hypothesis; deleting data or rewriting git history; changing the brief's success criteria; closing the whole research programme. |

Clarification on git and files: "rewriting git history" means `rebase`, `reset --hard` on pushed commits, `push --force`, or amending pushed commits. A normal commit that removes, renames or fixes a tracked file or symlink (for example a wrongly committed `data` symlink) is **GREEN**. So is repairing local links and paths inside the desk. Only deleting actual market data files is RED; when data is missing, re-import it (GREEN).

Two rules from the 2026-10-16 review:
- A run whose weights are all zero or whose statistics are `None` is an **infrastructure failure**. It is never recorded as a rejection; fix the pipeline and re-run in the same family.
- The base cost case uses the real Binance VIP 0 fees (spot taker 10 bps, USDⓈ-M taker 5 bps, per side) plus the grid's spread and impact. ×2 and ×3 are **stress tests**, never the base hurdle. Report the hurdle in bps per round trip, and keep the same number in notes, QUEUE and chat.
- Before saying "no READY item left", list every item whose status is `BLOCKED_ON` and check whether its dependencies are now DONE. If they are, it is READY.

Rule of thumb: if it is not RED, it is not a question. Pick what you would recommend, log it if ORANGE, and continue.

## 2. Decisions already taken (2026-10-16, Samuel)

- **D1 — Items B–G of `Status.md` §4 are all approved.** They are now QUEUE items with a fixed order. No per-item approval is needed.
- **D2 — True holdout.** The final holdout is **all data from 2024-07-01T00:00:00Z onwards**, as the brief says (section 3). It is imported from free public sources into a sealed local store that no exploration code can read (QUEUE Q1). The 2024-04-01 → 2024-06-30 "option A" window becomes a **contaminated dev-validation window**: it keeps its guard but is never presented as the holdout. Reading the true holdout stays RED, once per hypothesis.
- **D3 — No budget decision is pending.** Binance Vision (`data.binance.vision`) is free and public: spot and USDⓈ-M klines, aggTrades, trades, funding rates, premium-index and mark-price klines, and futures metrics, for the full history. Tick-level work (former BACKLOG item 15, "axe 8") therefore starts on that free data. Paid order-book data (Tardis, Kaiko, Databento) stays RED and is only raised if a candidate specifically needs L2 depth.
- **D4 — Negative results are not a stop signal.** "3+ consecutive negative axes" is removed from the stop list. Nulls are logged as lessons and the queue continues. Closing the whole programme is RED and requires the coverage check below to be complete.
- **D5 — Perpetual futures data is in scope for research.** Funding, basis and premium are the best-documented crypto risk premia; they are studied pre-cutoff (Q3, Q8). Document the source in `research/atlas/data-sources.md`. `policies/data_policy.md` is protected: propose a line for Samuel instead of editing it.
- **D6 — Kanban goal cards are allowed** for long, isolated QUEUE items (`--goal`, `--workspace worktree`). This replaces the "never spawn Kanban" line in `hermes.md`. The run that creates a card reviews and merges its result; nobody polls it.
- **D7 — Reporting.** The read-only "Avancement Aster toutes les 90 min" cron is retired: it reported state without advancing anything. One worker cron (see `aster/AUTOPILOT.md`) works the queue. Discord messages are sent only when there is a delta.
- **D8 — Dirty worktrees are integrated, not left for review.** The N1 correction in `.worktrees/` (Kanban `t_5b11e143`) is verified, committed and merged (Q0).

## 3. Coverage check (brief sections 5–7) before closing any class as null

A class is "covered" only if all applicable cells were studied with FDR control and placebos. A gap is a QUEUE item, not a reason to stop.

- Horizons: 1m, 5m, 15m, 1h, 4h, 1d, 1w (not only daily).
- Bars: time bars **and** information bars (volume, dollar, taker-imbalance).
- Flow: taker buy ratio, signed cumulative imbalance, volume and trade-count shocks, Kyle λ, Amihud, Roll, VPIN.
- Seasonality: hour UTC, weekday, funding fixings 00/08/16 UTC, Asia/Europe/US opens, month-end, weekends.
- Jumps and post-jump behaviour; CUSUM, SADF/GSADF bubbles.
- Volatility: GARCH family, HAR-RV, vol compression → expansion, vol-targeting overlays.
- Regimes: every N1–N5 result re-read by regime.
- Perps: funding level, funding change, basis/premium, open interest (where available).
- Inter-asset: lead-lag at 1m → 7d on raw **and** residual returns, VAR/Granger, panel with fixed effects, sector pairs, residual stat-arb, cross-sectional momentum/reversal.
- Literature: replication of the top claims from the veille.
- Second venue check for any surprising result.

## 4. Log (ORANGE decisions, newest last)

| Date | Item | Decision | Reason | Commit |
|---|---|---|---|---|
| 2026-10-16 | — | Charter and D1–D8 adopted | Long /goal runs stopped on non-RED questions and lost the plan held in chat | (this commit) |
