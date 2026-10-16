Spot 1m R2: Cloudflare R2 bucket `cryptos`, prefix `market/spot/klines_1m`, local at `data/r2/`; 12 symbols, 722 monthly pre-cutoff partitions through 2024-06, audited 2026-10-16 (31,371,418 rows; SHA-256 rechecked; exclusive cutoff `2024-07-01T00:00:00Z`). `desk data audit-r2 --sha256` passes all 12; Q0b remains blocked because `desk data check` checks the absent legacy five-symbol daily store and reports JSON errors despite exit code 0.

Brief §2 names **RENDERUSDT, ONDOUSDT, PUMPUSDT** (spot) and **HYPEUSDT** (perp USDⓈ-M) beyond the 12 imported symbols. Q2 (2026-10-16, prereg `research/notes/2026-10-16-Q2-prereg.md`) probes both free channels (`local-r2-spot`, `data.binance.vision-spot`, `data.binance.vision-um`) via `aster.scripts.probe_universe` (also offline-deterministic, ASTER_OFFLINE=1). Probe on 2026-10-16 returns `exists=no` for all 12 cells (4 symbols × 3 channels). Recorded channel decisions:

- **RENDERUSDT**: no pre-cutoff data anywhere free; route to the post-cutoff sealed store if/when Q1's import is authorised; holdout-only panel member otherwise.
- **ONDOUSDT**: no pre-cutoff data anywhere free; same routing as RENDER.
- **PUMPUSDT**: no pre-cutoff data anywhere free; same routing.
- **HYPEUSDT**: perp-only listing (2025-05); no pre-cutoff spot data; perp channel (funding / premium / mark / OI) is owned by **Q3**, USDⓈ-M via `data.binance.vision/data/futures/um/monthly/`.

The universe stays the 12-symbol panel pre-cutoff and the 12-symbol panel post-cutoff. The 4 brief members without pre-cutoff history are documented as **holdout-only panel members**. They contribute no exploration data and must not enter any desk backtest that consumes the dev sample.
