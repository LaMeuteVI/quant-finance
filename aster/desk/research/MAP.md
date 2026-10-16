# Research matrix

Global exploration cutoff: `2024-07-01T00:00:00Z`. Outside a one-shot holdout run, no post-cutoff market data may be inspected. The public 2026 order-book snapshot in `research/atlas/current-orderbook-snapshot.csv` is an authorised operational cost check, explicitly not research or holdout data.

| Asset | N0 | N1 | N2 | N3 | N4 | N5 | N6 | N7 | Next gated action |
|---|---|---|---|---|---|---|---|---|---|
| BTC | **complete** — `assets/2026-10-13-btc-n0.md` | **complete, no candidate** — `assets/2026-10-14-btc-n1-ta.md` | **complete, no candidate** — `assets/2026-10-14-btc-n2.md` | **complete, forecast only** — `assets/2026-10-14-btc-eth-n3-vol.md` | **complete, descriptive** — `assets/2026-10-14-btc-n4-regimes.md` | **complete, descriptive tick-flow V1** — `research/memos/2026-10-16-Q6-N5.md`, `research/atlas/q6_intraday_flow.json` | gated — no primary feature | gated | Q6 V1 on 10,481 BTCUSDT 50-BTC volume bars (10% sample of four 2022 partitions): flow lag-1 autocorr +0.172 and extreme-flow next-bar returns ±0.014%; descriptive only, not yet a ledger hypothesis. Q7 lead-lag grid adds no cost-surviving feature. Q8 finds persistent positive funding, but no net strategy input. |
| ETH | **complete** — `assets/2026-10-14-eth-n0.md` | **complete, no candidate** — `assets/2026-10-14-eth-n1-ta.md` | **complete, no candidate** — `assets/2026-10-14-eth-n2.md` | **complete, forecast only** — `assets/2026-10-14-btc-eth-n3-vol.md` | **complete, descriptive** — `assets/2026-10-14-eth-n4-regimes.md` | **complete, no candidate** — `assets/2026-10-14-eth-n5-flow.md` | gated — no primary feature | gated | Same as BTC: structural uptrend dominates every *_above signal; only `fvg_down_entry_h1` retains the joint filter (mean fwd_1d -1.05%, BH q=0.026), but mechanism is unclear (continuation vs exhaustion) and the cell is ETH-only, not BTC. The cell goes to the **backlog**, not the ledger. No ledger hypothesis registered. Next: panel N1. |
| BNB | **complete** — `assets/2026-10-14-bnbusdt-n0.md` | **complete, no candidate (corrected rerun)** — `assets/2026-10-15-bnbusdt-n1-ta.md` | **complete, descriptive** — `research/memos/2026-10-16-Q9-N5.md`, `research/atlas/q9_intraday_n2.json` | **complete, forecast only** — `research/memos/2026-10-16-Q10-N5.md`, `research/atlas/q10_volatility.json` | **complete, no candidate** — `research/memos/2026-10-16-Q11-N4.md`, `research/atlas/q11_regimes.json` | **complete, no candidate** — `research/memos/2026-10-16-Q12-N5.md`, `research/atlas/q12_intraday_flow.json` | queued | queued | Q10 HAR-RV forecast gains are not alpha; no candidate. |
| XRP | **complete** — `assets/2026-10-14-xrpusdt-n0.md` | **complete, no candidate (corrected rerun)** — `assets/2026-10-15-xrpusdt-n1-ta.md` | **complete, descriptive** — `research/memos/2026-10-16-Q9-N5.md`, `research/atlas/q9_intraday_n2.json` | **complete, forecast only** — `research/memos/2026-10-16-Q10-N5.md`, `research/atlas/q10_volatility.json` | queued | queued | queued | queued | Q10 HAR-RV forecast gains are not alpha; no candidate. |
| SOL | **complete** — `assets/2026-10-14-solusdt-n0.md` | **complete, no candidate (corrected rerun)** — `assets/2026-10-15-solusdt-n1-ta.md` | **complete, descriptive** — `research/memos/2026-10-16-Q9-N5.md`, `research/atlas/q9_intraday_n2.json` | **complete, forecast only** — `research/memos/2026-10-16-Q10-N5.md`, `research/atlas/q10_volatility.json` | queued | queued | queued | queued | Q10 HAR-RV forecast gains are not alpha; no candidate. |
| LINK | **complete** — `assets/2026-10-14-linkusdt-n0.md` | **complete, no candidate (corrected rerun)** — `assets/2026-10-15-linkusdt-n1-ta.md` | **complete, descriptive** — `research/memos/2026-10-16-Q9-N5.md`, `research/atlas/q9_intraday_n2.json` | **complete, forecast only** — `research/memos/2026-10-16-Q10-N5.md`, `research/atlas/q10_volatility.json` | queued | queued | queued | queued | Q10 HAR-RV forecast gains are not alpha; no candidate. |
| DOGE | **complete** — `assets/2026-10-14-dogeusdt-n0.md` | **complete, no candidate (corrected rerun)** — `assets/2026-10-15-dogeusdt-n1-ta.md` | **complete, descriptive** — `research/memos/2026-10-16-Q9-N5.md`, `research/atlas/q9_intraday_n2.json` | **complete, forecast only** — `research/memos/2026-10-16-Q10-N5.md`, `research/atlas/q10_volatility.json` | queued | queued | queued | queued | Q10 HAR-RV forecast gains are not alpha; no candidate. |
| Panel incl. XMR | **complete** — `assets/2026-10-14-panel-n0.md` | queued | queued | queued | queued | queued | queued | queued | XMR delisted 2024-02-20 (preserved as survivorship-bias guardrail). Panel N1–N2 only after a primary feature is identified from inter-residual or intra-asset studies. |

## Infrastructure status

- [x] Pre-cutoff R2 spot 1m local reader/audit, fixed cutoff enforcement and provenance checks.
- [x] Quality profile: gaps and `number_of_trades == 0` frozen minutes remain explicit, never forward-filled.
- [x] Causal time bars and source-clock normalisation.
- [x] Conservative taker cost reference: `max(aggTrades proxy, one tick) × 3`, square-root impact, 10 bps/side fees, sensitivities ×1/×3/×10. See `atlas/costs.md`.
- [x] Current public order-book operational check, isolated from exploration data.
- [x] BTC and ETH N2 fixed-horizon descriptive toolkit: block bootstrap, inverse/placebo, BH-FDR.
- [x] Inter-asset lead-lag / residual-return / FDR toolkit.
- [x] GARCH/HAR-RV and forecast-comparison toolkit.
- [x] Panel N0 dossiers (BNB, XRP, SOL, LINK, DOGE, XMR).
- [x] Inter-asset residual factor study (PCA + Marcenko-Pastur denoising + lead-lag residual + cross-sectional residual momentum) over 8 assets.
- [x] Multi-factor extension K=2, K=3 with per-eigenvalue MP denoising and reference-asset sign alignment.

## Evidence discipline

One hypothesis and one dev trial exist in the ledger: `H-20261013-001`, rejected after failing its preregistered drawdown gate; its holdout remains unread. BTC, ETH, BTC–ETH inter-asset, and the 8-asset inter-residual study (1-factor and K=2, K=3) are all descriptive artifacts only. N3 found forecast value in HAR-RV but no trading edge. Before any new `desk backtest`: ledger preregistration with mechanism, falsification and numerical prediction; then all trials through the pipeline, DSR using the true family trial count, and a single sealed holdout read.

Next gated action: the klines-1m phase on the pre-cutoff 8-asset panel is **exhausted** (see BACKLOG item 12). The only credible next axis is tick microstructure data (BACKLOG item 15), which requires Samuel's budget OK and a new cutoff seal. N6/N7 cannot run without a primary feature, and no primary feature has been found on the klines-1m panel.
