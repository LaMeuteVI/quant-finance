# N1 TA alt panel — XRPUSDT (2026-10-15)

* Daily bars: **2249** from 2018-05-05 to 2024-06-30 (UTC).
* Cutoff (exclusive): `2024-07-01T00:00:00+00:00`; last daily bar `2024-06-30` — no bar at or after the cutoff is used.
* Cells evaluated: **128** = 32 signals x 4 horizons
  (96 primary, 32 placebo-level).
* Tested cells with n >= 30: 120 (the fixed 128-cell family is retained; below-floor cells are reported as NaN).
* Retained after BH-FDR (asset and panel) + bootstrap + inverse + 3 placebos: **0**.

## Retained cells

None: no cell survived the preregistered retention rule.

## Strongest primary cells by p-value (not retained cells are not evidence)

| signal | horizon | n | mean fwd | p | q(asset) | q(panel) | inverse mean | placebo shift p |
|---|---|---|---|---|---|---|---|---|
| ma_20_100_fast_below_slow | 14d | 1153 | 0.04743 | 0.005028 | 0.3506 | 0.167 | -0.04800 | 0.8238 |
| ma_20_100_fast_below_slow | 7d | 1153 | 0.02368 | 0.005478 | 0.3506 | 0.167 | -0.02390 | 0.9937 |
| ma_20_100_fast_above_slow | 14d | 997 | -0.04800 | 0.01438 | 0.4097 | 0.1948 | 0.04743 | 0.5696 |
| ma_20_100_fast_below_slow | 3d | 1153 | 0.00890 | 0.01478 | 0.4097 | 0.1948 | -0.00878 | 0.5709 |
| rsi14_oversold | 1d | 72 | 0.01940 | 0.01702 | 0.4097 | 0.2007 | -0.00093 | 0.3976 |
| ma_20_100_fast_above_slow | 7d | 997 | -0.02390 | 0.01921 | 0.4097 | 0.2017 | 0.02368 | 0.5521 |
| ma_20_100_fast_below_slow | 1d | 1153 | 0.00290 | 0.04432 | 0.81 | 0.2757 | -0.00289 | 0.3831 |
| rsi14_oversold | 14d | 72 | 0.07176 | 0.05575 | 0.81 | 0.3183 | -0.00533 | 0.7849 |
| ma_20_100_fast_above_slow | 3d | 997 | -0.00878 | 0.05695 | 0.81 | 0.3183 | 0.00890 | 0.9361 |
| rsi14_oversold | 7d | 72 | 0.03241 | 0.08489 | 1 | 0.4075 | -0.00289 | 0.521 |
| pivot_r1_break | 3d | 265 | 0.01894 | 0.094 | 1 | 0.4373 | -0.00348 | 0.5011 |
| ma_20_100_fast_above_slow | 1d | 997 | -0.00289 | 0.1106 | 1 | 0.4576 | 0.00290 | 0.5099 |

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
