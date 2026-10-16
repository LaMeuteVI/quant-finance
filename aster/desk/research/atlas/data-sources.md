Spot 1m R2: Cloudflare R2 bucket `cryptos`, prefix `market/spot/klines_1m`, local at `data/r2/`; 12 symbols, 722 monthly pre-cutoff partitions through 2024-06, audited 2026-10-16 (31,371,418 rows; SHA-256 rechecked; exclusive cutoff `2024-07-01T00:00:00Z`). `desk data audit-r2 --sha256` passes all 12; Q0b remains blocked because `desk data check` checks the absent legacy five-symbol daily store and reports JSON errors despite exit code 0.

Brief §2 names **RENDERUSDT, ONDOUSDT, PUMPUSDT** (spot) and **HYPEUSDT** (perp USDⓈ-M) beyond the 12 imported symbols. Q2 (2026-10-16, prereg `research/notes/2026-10-16-Q2-prereg.md`) probes both free channels (`local-r2-spot`, `data.binance.vision-spot`, `data.binance.vision-um`) via `aster.scripts.probe_universe` (also offline-deterministic, ASTER_OFFLINE=1). Probe on 2026-10-16 returns `exists=no` for all 12 cells (4 symbols × 3 channels). Recorded channel decisions:

- **RENDERUSDT**: no pre-cutoff data anywhere free; route to the post-cutoff sealed store if/when Q1's import is authorised; holdout-only panel member otherwise.
- **ONDOUSDT**: no pre-cutoff data anywhere free; same routing as RENDER.
- **PUMPUSDT**: no pre-cutoff data anywhere free; same routing.
- **HYPEUSDT**: perp-only listing (2025-05); no pre-cutoff spot data; perp channel (funding / premium / mark / OI) is owned by **Q3**, USDⓈ-M via `data.binance.vision/data/futures/um/monthly/`.

The universe stays the 12-symbol panel pre-cutoff and the 12-symbol panel post-cutoff. The 4 brief members without pre-cutoff history are documented as **holdout-only panel members**. They contribute no exploration data and must not enter any desk backtest that consumes the dev sample.

## USDⓈ-M (perpetual futures) data

Q3 (2026-10-16, prereg `research/notes/2026-10-16-Q3-prereg.md`, importer `aster/desk/src/aster/data/funding_rate.py`, CLI `desk data import-funding` and `desk data audit-funding`). Sources probed via `aster.scripts.probe_perp_universe` on 2026-10-16:

- **`fundingRate`** (Binance Vision `data/futures/um/monthly/fundingRate/<SYM>/<SYM>-fundingRate-YYYY-MM.zip`): 12/12 symbols have at least one pre-cutoff month. First-month distribution matches the perp listing dates (BTCUSDT 2020-01, BNBUSDT/XMRUSDT 2020-02, SOLUSDT 2020-09, AAVEUSDT/NEARUSDT 2020-10, SUIUSDT 2023-05, FETUSDT 2023-01). Imported as of 2026-10-16: **538 pre-cutoff Parquet partitions / 12 symbols / 48 879 rows / 2.16 MB** under `data/r2/market/futures/um/funding_rate/`. Each partition carries a sibling `*.manifest.json` recording `{source, key, size_bytes, sha256, rows, start, end, timestamp_unit, cutoff_exclusive}` — no record values. `desk data audit-funding --sha256` is green. The store is the primary input for **F1** (funding carry, BLOCKED_ON reusable items) and **F2** (funding/premium crowding).
- **`premiumIndexKlines`**, **`markPriceKlines`**, **`metrics`** (open interest, long/short ratios): the public archive has no pre-cutoff ZIPs for these datasets on the standard path conventions (probe returned 404 on 2026-10-16 across all paths tried). Historical OI therefore requires a paid source (D3 → RED). Document as a known gap; revisit only if F1/F2 need OI for sizing or risk.
- **`klines 1m` UM** (Binance Vision `data/futures/um/monthly/klines/<SYM>/1m/<SYM>-1m-YYYY-MM.zip`): public archive holds pre-cutoff files for BTCUSDT and ETHUSDT from 2020-01 onwards. Not imported in this iteration (scope kept to `fundingRate` for the carry family); next importable surface for the perp basis leg of F1.

## Spot aggTrades

Q4 (2026-10-16, prereg `research/notes/2026-10-16-Q4-prereg.md`, importer `aster/desk/src/aster/data/aggtrades.py`, bar builders `aster/desk/src/aster/data/information_bars.py`, CLI `desk data import-aggtrades`, `desk data audit-aggtrades [--sha256]`, `desk data build-volume-bars --family {volume,dollar,taker_imbalance}`).

- **Source**: `data.binance.vision/data/spot/monthly/aggTrades/<SYM>/<SYM>-aggTrades-YYYY-MM.zip`, **headerless 8-column CSV** per the official README: `agg_trade_id, price, quantity, first_trade_id, last_trade_id, transact_time (ms epoch), is_buyer_maker, is_best_price_match`. The importer drops `first_trade_id`, `last_trade_id`, `is_best_price_match` and ships a 5-column Parquet (agg_trade_id:int64, price:float64, quantity:float64, transact_time:int64, is_buyer_maker:bool). Manifest metadata-only: `{source, key, size_bytes, sha256, rows, start, end, timestamp_unit, cutoff_exclusive}` — no record values.
- **Cutoff**: strictly pre-2024-07-01 UTC. A monthly archive that crosses the cutoff raises `CutoffViolationError`; the pre-2022-01 months are present on the public archive but were not imported (focus on 2022-01→2024-06 per the brief).
- **Imported as of 2026-10-16**: 4 pre-cutoff Parquet partitions / 1 symbol (BTCUSDT) / 107 730 009 rows / 1.37 GB under `data/r2/market/spot/aggtrades/`. The download and import of the remaining 56 partitions (BTC 2022-05→2024-06 + ETH 2022-01→2024-06) is in flight; final numbers will refresh here as the import run completes. `desk data audit-aggtrades --sha256` green on the imported partitions.
- **Information bars (afml ch02)**: volume bars (fixed BTC notional per bar), dollar bars (fixed USD notional), taker-imbalance bars (closing on extreme running signed imbalance). Smoke test on 1M-row sample of BTCUSDT 2022-01: 863 volume bars, 1 712 dollar bars, 5 taker-imbalance bars; imbalance mean ≈ −0.024, std ≈ 0.009 (efficient-market null). 7 unit tests in `tests/test_information_bars.py` cover the three families (sustained trading, threshold stability, empty input, dollar notional, taker-imbalance extremes, balanced flow, causal close label).

## Atlas conventions

- `research/atlas/` is the only directory that holds pre-cutoff descriptive tables, lead-lag grids, regime labels and cost grids. All values derive from pre-cutoff sources.
- The sealed store `data/sealed/market/spot/klines_1m/` (Q1) and `data/sealed/market/futures/um/funding_rate/` (Q3, not built — only spot sealed shipped) stay empty until a separately authorised import run; exploration paths raise on them.
