# N1 TA alt panel — DOGEUSDT (2026-10-15)

* Daily bars: **1822** from 2019-07-06 to 2024-06-30 (UTC).
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
| ma_5_20_above | 1d | 560 | 0.00828 | 0.02166 | 0.3641 | 0.3661 | -0.00094 | 0.313 |
| rsi14_oversold | 1d | 76 | 0.01539 | 0.02212 | 0.3641 | 0.3661 | 0.00131 | 0.4276 |
| rsi14_oversold | 3d | 76 | 0.02260 | 0.04755 | 0.3641 | 0.3661 | 0.00509 | 0.3011 |
| ma_5_20_above | 3d | 560 | 0.01929 | 0.0516 | 0.3641 | 0.3661 | -0.00017 | 0.3905 |
| stoch14_cross_up | 3d | 522 | 0.01019 | 0.06505 | 0.3641 | 0.3661 | 0.00408 | 0.1363 |
| rsi14_oversold | 7d | 76 | 0.02864 | 0.06633 | 0.3641 | 0.3661 | 0.01312 | 0.07769 |
| fvg3_up_fill | 3d | 18 | -0.03045 | 0.0691 | 0.3641 | 0.3661 | 0.00619 | 0.9886 |
| ma_50_200_above | 3d | 579 | 0.02212 | 0.06959 | 0.3641 | 0.3661 | -0.00178 | 0.4861 |
| fvg3_up_fill | 7d | 18 | -0.03565 | 0.07017 | 0.3641 | 0.3661 | 0.01425 | 0.1711 |
| fib_618_above | 14d | 287 | 0.19262 | 0.07427 | 0.3641 | 0.3661 | -0.00278 | 0.1549 |
| fib_618_above | 7d | 287 | 0.09371 | 0.07629 | 0.3641 | 0.3661 | -0.00126 | 0.5758 |
| fib_618_above | 3d | 287 | 0.04138 | 0.07664 | 0.3641 | 0.3661 | -0.00084 | 0.395 |

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
