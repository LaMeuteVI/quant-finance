# N1 TA alt panel — BNBUSDT (2026-10-15)

* Daily bars: **2428** from 2017-11-07 to 2024-06-30 (UTC).
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
| ma_20_100_above | 3d | 1307 | 0.01474 | 0.000855 | 0.05822 | 0.04366 | -0.00174 | 0.2788 |
| ma_20_100_above | 7d | 1307 | 0.03137 | 0.0013 | 0.05822 | 0.04366 | -0.00035 | 0.1244 |
| ma_50_200_above | 3d | 927 | 0.01425 | 0.002245 | 0.05822 | 0.04366 | 0.00275 | 0.05276 |
| ma_5_20_above | 3d | 946 | 0.01458 | 0.002918 | 0.05822 | 0.04366 | 0.00239 | 0.4119 |
| ma_10_30_above | 14d | 1014 | 0.06655 | 0.002999 | 0.05822 | 0.04366 | 0.01042 | 0.3232 |
| ma_10_30_above | 7d | 1014 | 0.03287 | 0.003176 | 0.05822 | 0.04366 | 0.00517 | 0.04294 |
| ma_20_100_above | 14d | 1307 | 0.06075 | 0.003677 | 0.05822 | 0.04366 | 0.00242 | 0.1523 |
| ma_10_30_above | 3d | 1014 | 0.01435 | 0.004523 | 0.05822 | 0.04366 | 0.00196 | 0.3056 |
| ma_5_20_above | 1d | 946 | 0.00565 | 0.004524 | 0.05822 | 0.04366 | 0.00037 | 0.172 |
| ma_50_200_above | 1d | 927 | 0.00471 | 0.004731 | 0.05822 | 0.04366 | 0.00102 | 0.1498 |
| ma_5_20_above | 7d | 946 | 0.02868 | 0.005152 | 0.05822 | 0.04366 | 0.00914 | 0.02728 |
| ma_5_20_above | 14d | 946 | 0.06242 | 0.005847 | 0.05822 | 0.04366 | 0.01568 | 0.2199 |

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
