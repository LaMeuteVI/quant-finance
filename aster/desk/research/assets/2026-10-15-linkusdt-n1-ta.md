# N1 TA alt panel — LINKUSDT (2026-10-15)

* Daily bars: **1992** from 2019-01-17 to 2024-06-30 (UTC).
* Cutoff (exclusive): `2024-07-01T00:00:00+00:00`; last daily bar `2024-06-30` — no bar at or after the cutoff is used.
* Cells evaluated: **128** = 32 signals x 4 horizons
  (96 primary, 32 placebo-level).
* Tested cells with n >= 30: 128.
* Retained after BH-FDR (asset and panel) + bootstrap + inverse + 3 placebos: **0**.

## Retained cells

None: no cell survived the preregistered retention rule.

## Strongest primary cells by p-value (not retained cells are not evidence)

| signal | horizon | n | mean fwd | p | q(asset) | q(panel) | inverse mean | placebo shift p |
|---|---|---|---|---|---|---|---|---|
| ma_10_30_above | 3d | 817 | 0.01449 | 0.005831 | 0.4806 | 0.3605 | -0.00151 | 0.7312 |
| ma_5_20_above | 3d | 753 | 0.01382 | 0.008178 | 0.4806 | 0.3605 | -0.00027 | 0.4559 |
| ma_10_30_above | 1d | 817 | 0.00512 | 0.01126 | 0.4806 | 0.3605 | -0.00073 | 0.9621 |
| ma_20_100_above | 3d | 1034 | 0.01060 | 0.02134 | 0.5374 | 0.4113 | -0.00093 | 0.3597 |
| ma_5_20_above | 1d | 753 | 0.00466 | 0.02871 | 0.5374 | 0.4113 | -0.00015 | 0.6037 |
| donchian20_breakout_down | 1d | 61 | 0.02281 | 0.02924 | 0.5374 | 0.4113 | 0.00100 | 0.7405 |
| pivot_r1_break | 1d | 277 | 0.00825 | 0.03081 | 0.5374 | 0.4113 | 0.00060 | 0.8634 |
| pivot_r1_break | 3d | 277 | 0.01966 | 0.03428 | 0.5374 | 0.4113 | 0.00270 | 0.4906 |
| ma_20_100_above | 1d | 1034 | 0.00335 | 0.06014 | 0.5374 | 0.5759 | -0.00015 | 0.681 |
| ma_5_20_above | 7d | 753 | 0.02182 | 0.06106 | 0.5374 | 0.5759 | 0.00560 | 0.08694 |
| ma_10_30_above | 7d | 817 | 0.02146 | 0.07798 | 0.5374 | 0.5759 | 0.00496 | 0.1242 |
| stoch14_overbought | 3d | 393 | 0.01240 | 0.08336 | 0.5374 | 0.5759 | 0.00326 | 0.2151 |

## Regime diagnostics (retained cells only, buckets with n >= 30)

No retained cell, no regime table.

## Limits

* Descriptive only. A retained cell is an observation about pre-cutoff history,
  not a tradable edge: no cost model, no execution, no capacity, no holdout.
* No hypothesis was registered and no backtest was run.
* Signals are evaluated on overlapping forward windows, so p-values are
  anti-conservative; the block bootstrap quantifies sampling noise, not
  dependence between cells.
* Multiple horizons of the same signal are highly correlated; BH-FDR assumes
  positive dependence and is therefore conservative here, not anti-conservative.
