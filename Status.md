# Aster desk — status & handoff

> Single source of truth for **what we are doing, where we are, and how to pick up the work** — in any session, with any agent (Aster, Claude Code, Codex, etc.).

**Last updated**: 2026-10-15  
**Owner**: Samuel (decision authority)  
**Agent of record**: Aster (research, code, paper only — no live, no keys, no orders outside `desk trade run --broker paper`)  
**Repo**: `LaMeuteVI/quant-finance` (active branch `feat/aster-agent`)  
**Working tree**: `/root/quant-finance/aster/desk` (canonical)  
**Data cutoff (absolute)**: `2024-07-01T00:00:00Z` for all exploration. Post-cutoff data may be read **once** through a preregistered holdout, never for tuning.

---

## 1. The goal (verbatim from the brief)

> Find one or several crypto strategies whose edge is real, net of costs, statistically defensible, and able to absorb capital. The "gold mine" must:
> 1. Have an identifiable economic mechanism (who pays, and why it keeps paying);
> 2. Survive real costs at the trading timeframe, including stress ×2;
> 3. Pass the dev gate (DSR ≥ 0.95 with the true family trial count), then the **sealed** holdout, then ≥ 28 days of paper trading;
> 4. Hold across multiple regimes, or have a validated regime filter;
> 5. Have a quantified capacity: the max AUM where net Sharpe stays ≥ 1.
>
> Depth is to **understand** the asset and to **generate few but excellent** hypotheses — not to multiply backtests. Killing 9 ideas out of 10 cleanly is part of the work.

**Scope**: research and paper trading only. **No live, no keys, no orders** outside `desk trade run --broker paper`.

## 2. The golden rule (also from the brief)

> Everything post-`2024-07-01` is **forbidden during exploration**: atlas, asset dossiers, correlations, event studies, charts. That data is reserved for holdouts of preregistered hypotheses. Reading it once would contaminate every final test.

A ledger hypothesis reads the holdout **exactly once**. Pre-registration happens before any backtest. Every trial goes through `desk backtest`, which records the trial; the Deflated Sharpe uses that count. No "quick tests" outside the pipeline. Max 5 strategy versions per hypothesis; after that, reject and write the lesson.

## 3. What we have, what we have learned

### 3.1 Pipeline (Phase 0 of the brief)

| Component | Status | Where |
|---|---|---|
| `aster.data.binance_vision` import zip→parquet, ms/µs, dedup, provenance manifest per source file | ✅ done | `src/aster/data/` |
| `desk data import --root <dir>` | ✅ done | `src/aster/cli.py` |
| Time bars 1m, 5m, 15m, 1h, 4h, 1d, causal clock normalisation | ✅ 1m + derived 1d verified; 5/15/1h/4h partial | `src/aster/data/bars.py`, `src/aster/data/r2_klines.py` |
| Information bars: volume, dollar, imbalance, frozen-minutes flag | ✅ `trades==0` column tracked, never forward-filled | `src/aster/data/r2_klines.py` |
| `desk data check` audit | ✅ done | `src/aster/cli.py` |
| Cost grid: max(aggTrades proxy, one tick) × 3 + square-root impact + 10 bps/side fees | ✅ done | `src/aster/data/costs_table.py`, `atlas/cost-grid.csv` |
| Public order-book snapshot for operational spread validation | ✅ isolated, **not** research data | `atlas/current-orderbook-snapshot.csv` |
| Holdout seal (train/dev/holdout split) | ⚠️ **not yet formalised** | backlog item A |
| Multi-exchange cross-check | ⚠️ not implemented | backlog item |

### 3.2 Research matrix (N0→N7 per asset, plus inter-asset)

| Asset | N0 | N1 | N2 | N3 | N4 | N5 | N6 | N7 |
|---|---|---|---|---|---|---|---|---|
| BTC | ✅ | ✅ complete, no candidate | ✅ | ✅ forecast only | ✅ descriptive | ✅ no candidate | gated | gated |
| ETH | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | gated | gated |
| BNB | ✅ | ✅ | queued | queued | queued | queued | queued | queued |
| XRP | ✅ | ✅ | queued | queued | queued | queued | queued | queued |
| SOL | ✅ | ✅ | queued | queued | queued | queued | queued | queued |
| LINK | ✅ | ✅ | queued | queued | queued | queued | queued | queued |
| DOGE | ✅ | ✅ | queued | queued | queued | queued | queued | queued |
| XMR | ✅ (panel) | queued | queued | queued | queued | queued | queued | queued |
| Panel | ✅ | queued | queued | queued | queued | queued | queued | queued |
| AAVE, FET, NEAR, SUI | ✅ R2 present | not yet | not yet | not yet | not yet | not yet | not yet | not yet |

### 3.3 Axes studied — 7 closed, 0 edge tradable

Each axis was registered, coded, tested, run on the pre-2024-07-01 klines-1m panel, and **closed** with a defensible null result.

| # | Axis | Date closed | Verdict | Skill reference | Artifact |
|---|---|---|---|---|---|
| 1 | Intraday term structure (vol morning/evening, autocorr minute-par-minute) | 2026-10-14 | CLOS — 0 edge | tsay ch02, chan ch03 | `notes/2026-10-14-axe-1.md` |
| 2 | Ichimoku Kinko Hyo full (10 chapters Riguet) | 2026-10-14 | CLOS — 0 edge | riguet-ichimoku, chan ch03 | `notes/2026-10-14-axe-2.md` |
| 3 | Mean-reversion OU + half-life + pairs (6 pairs) | 2026-10-14 | CLOS — 0 edge | chan ch03, pairs-trading-partial-cointegration | `notes/2026-10-14-axe-3.md` |
| 4 | Vol risk premium (HAR-RV, RV/BV/JV, VRP per decile) | 2026-10-14 | CLOS — 0 edge | chan ch03, tsay ch03, diebold-mariano | `notes/2026-10-14-axe-4.md` |
| 5 | CFA-style TA enriched (Camarilla/Woodie + Elliott proxy + advanced Fib) | 2026-10-14 | CLOS — 0 edge clear | cfa-pm, riguet, cfa-qm | `notes/2026-10-14-axe-5.md` |
| 6 | ML XGBoost on microstructure features with purged k-fold CV | 2026-10-15 | CLOS — 0 edge tradable | lopez-de-prado ch03/04/07/14, backtest-hygiene ch04/05/09 | `notes/2026-10-15-axe-6.md` |
| 7 | Markov-switching Hamilton 1989 (BTC/ETH/BNB/SOL) | 2026-10-15 | CLOS — 0 edge | tsay ch04 | `notes/2026-10-15-axe-7.md` |
| N1-alt | 5 alts (BNB/XRP/SOL/LINK/DOGE) TA catalogue, 640 cells | 2026-10-15 | complete, no candidate | cfa-pm, riguet, cfa-qm, backtest-hygiene | `notes/2026-10-15-n1-alts.md` |

**Structural conclusion** (7 axes + panel N1): on klines 1m daily, pre-2024-07-01, no standard TA family, no microstructure proxy, no regime model, and no ML pipeline produces an edge that survives BH-FDR, placebos, costs, and stability filters. The 1m kline bar aggregates away the tick microstructure where the residual idiosyncratic information lives.

### 3.4 Ledger (truth)

- **Live hypotheses**: 0
- **Rejected hypotheses**: 1 (`H-20261013-001`, 60-day long/cash TSMOM, failed preregistered drawdown floor, holdout **unread**)

The full pre-registration / trial / verdict protocol is in `policies/research_protocol.md` and the ledger schema lives in `memory/ledger.db`.

### 3.5 Where we are by goal

| Standing goal (from `/goal` style sub-criteria) | Status | Next gated action |
|---|---|---|
| Audit t_1a257193 worktree after the sub-agent's N1-alt run | ✅ done (2026-10-15) | — |
| Audit data: provenance, ms/µs, gaps, frozen minutes, XMR, HYPE, aggTrades | ✅ done (2026-10-15) | — |
| Compare desk to Phase 0 of the brief, propose a minimal plan | ✅ done (2026-10-15) | Samuel picks A–G |
| Fix BACKLOG.md and `.gitignore` | ✅ done (BACKLOG items 16-17 added; `.worktrees/` already ignored) | — |
| Write `Status.md` and agent handoff files | ✅ done (this file) | — |
| **H1**: Holdout split, sealed, written down | ⏳ **pending Samuel's OK** | ledger preregistration template needs to add `holdout_lock` |
| **H2**: At least one crypto strategy with real, net, defensible, scalable edge | ⏳ blocked on (a) tick microstructure data or (b) extending the matrix on a different signal class | requires budget OK for Tardis/Kaiko OR an N2-N5 run per alt that surfaces a candidate |

## 4. Work remaining — Samuel decides

Each is **substantive** and needs explicit approval before code or data work. None has been started.

- **A — Holdout seal.** Pick a cutoff, write the train/dev/holdout boundaries into a committed file, lock the holdout path in `r2_klines.py`. Required before any further backtest.
- **B — Axe 8 microstructure proxy from aggTrades.** Build the aggTrades → trades/min → flow-imbalance pipeline on the 6 assets where 2024-06 data exists (BTC/ETH/BNB/SOL/XRP/DOGE). 1 month window only — useful for pipeline validation, not for a multi-year backtest.
- **C — N2 per alt** (5 alts). Distribution, autocorr, Hurst, jumps.
- **D — N3–N5 per alt.** Vol + regimes + microstructure proxies.
- **E — Section 6 inter-asset.** Dependence structure, lead-lag grid, panel cointegration, canonical residual.
- **F — Atlas.** Lead-lag, regimes, asset dossiers `research/assets/<SYMBOLE>.md` consolidated.
- **G — Web scout** (SSRN/arXiv) and update of `research/veille/`.

## 5. How to pick up the work (any agent, any session)

1. **Read this file** end-to-end before any tool call.
2. **Read `research/MAP.md` and `research/BACKLOG.md`** to know the current matrix state.
3. **Read `policies/`** — these are binding, not suggestions.
4. **Read `AGENTS.md`** in the working tree for the desk layout and command surface.
5. **Verify the holdout seal** before any backtest. If you find post-2024-07-01 data in a research file, **stop and report**; do not look at the data.
6. **Register every hypothesis in the ledger first.** Pre-registration = statement, mechanism, falsification, numerical prediction. No edit after seeing results.
7. **Run every backtest through `desk backtest`.** Outside-the-pipeline runs inflate the DSR.
8. **Datasets**: all data lives in `data/` (gitignored). R2 is the source of truth; never trust a derived parquet without its manifest SHA256.
9. **Tests**: `uv run pytest` must stay green. Do not weaken a gate to make something pass.
10. **Sub-agents**: spawn only Aster sub-agents (Scout, Researcher, Skeptic, Breaker, Critic) via `delegate_task`, never external agents (Forge, Kanban, etc.).
11. **Live**: never. Samuel decides live promotion. `desk kill on` is human-only.

### 5.1 Common commands

| Need | Command |
|---|---|
| Refresh data | `uv run desk data fetch --funding` then `uv run desk data check` |
| What was tried? | `uv run desk ledger list [--status rejected] [--text <kw>]` |
| Register a hypothesis | `uv run desk ledger new --title ... --statement ... --mechanism ... --falsification ... --prediction '<json>' --family ... --market crypto-spot --source <role> --strategy <name>` |
| Backtest (dev) | `uv run desk backtest --hypothesis H-... --strategy <name> --params '{...}' --notes "..."` |
| Advance a stage | `uv run desk ledger status H-... backtest_passed --reason "..."` |
| Holdout (once) | `uv run desk backtest --hypothesis H-... --strategy <name> --sample holdout` |
| Lesson | `uv run desk ledger lesson H-... "..."` |
| Paper trade | `uv run desk trade run --hypothesis H-... --broker paper` |
| Risk / kill | `uv run desk risk status`, `uv run desk kill on --reason "..."` |
| PBO | `uv run desk pbo returns_matrix.csv` |
| Journal integrity | `uv run desk journal verify` |

Human-only, never attempt: `desk promote`, `desk kill off`, editing `risk_limits.yaml`, arming live (`ASTER_LIVE_ARMED`).

## 6. Strategy catalogue (current, all CLOS / no candidate)

There is **no live strategy** to copy-trade. The following were tested and rejected with evidence. They are kept here so future agents (or a future Samuel) do not redo the same work.

| Strategy class | Tested where | Why it failed |
|---|---|---|
| Long/cash TSMOM (60d, BTC) | `H-20261013-001` ledger hypothesis | DD gate: -41.60% vs -35% floor |
| Intraday term-structure vol | Axe 1 | autocorr 1m = -0.025 → 3e-8/trade, dominated by 20 bps fees |
| Ichimoku 10-component system | Axe 2 | Chikou is forward-looking; conversion/base lag too long for crypto |
| OU mean-reversion pairs | Axe 3 | half-life 173 days on BTC/ETH spread; capacity trivial |
| Vol risk premium per decile | Axe 4 | dominated by uptrend drift, not by vol carry |
| Camarilla / Woodie / advanced Fib | Axe 5 | exposures to drift, sample n too small for Fib |
| ML XGBoost purged k-fold | Axe 6 | OOS lift -9.7 pp, DSR p=0.88, beaten by `sign(log_ret_{t-1})` baseline |
| Markov-switching Hamilton 2-regime | Axe 7 | null p ∈ {0.30, 0.45, 0.30, 0.65}, structure inside H0 |
| 8-family TA catalogue (BTC/ETH) | BTC/ETH N1 | 1/224 cells retained, mechanism-ambiguous, ETH-only |
| 8-family TA catalogue (5 alts) | N1-alt | 0/640 cells retained |

## 7. Open questions for Samuel

1. **Tick microstructure data acquisition** (Tardis / Kaiko / Databento). The 1m kline panel cannot expose residual idiosyncratic alpha; the next credible axis is tick data. This requires budget OK **and** a new cutoff seal post-acquisition. Do you want me to (a) draft a data-acquisition memo for one vendor, (b) close the klines research axis and stop until a decision, or (c) continue on a different signal class first?
2. **Holdout seal**: which cutoff do you want locked in? The current cutoff is the exploration cutoff (`2024-07-01`); the dev/holdout split has not been written down yet.
3. **Time horizon**: how many more days/weeks of the current rig do you want before deciding (1)?

## 8. Where things live (file index)

- **Desk policy** (binding): `aster/desk/policies/` — `research_protocol`, `backtest_standard`, `data_policy`, `risk_policy`, `execution_policy`, `promotion_policy`.
- **Desk map and commands**: `aster/desk/AGENTS.md`.
- **Research state**: `aster/desk/research/MAP.md`, `BACKLOG.md`, `EXPLORATION_JOURNAL.md`, `notes/`, `assets/`, `atlas/`, `veille/`.
- **Code**: `aster/desk/src/aster/` (data, backtest, validation, ledger, risk, execution, portfolio, research, strategies, cli).
- **Tests**: `aster/desk/tests/`. Current `uv run pytest`: **333 passed** (2026-10-15, includes axe 7 + N1-alt).
- **Data**: `aster/desk/data/` (gitignored). Source: `data/r2/market/spot/klines_1m/` partitioned by `(symbol, year, month)` with per-partition manifest + SHA256. Cutoff enforced in `read_local()`.
- **This handoff**: `Status.md` (repo root) and `claude.md`, `codex.md`, `hermes.md` (agent-specific workflows).

---

**Bottom line for the next agent**:
1. Don't redo the 7 closed axes. Each has a note with mechanism, prediction, result, lesson.
2. Don't read post-`2024-07-01` data outside a sealed holdout.
3. Don't register a hypothesis without mechanism + falsification + numerical prediction.
4. Don't multiply backtests; depth over breadth.
5. The single most likely next move that could change the verdict is **tick microstructure data**, not another 1m-kline axis. Ask Samuel.
