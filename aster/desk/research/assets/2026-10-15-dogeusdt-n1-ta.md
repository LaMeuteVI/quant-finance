# N1 TA alt panel — DOGEUSDT (2026-10-15)

* Daily bars: **1822** from 2019-07-06 to 2024-06-30 (UTC).
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
| rsi14_oversold | 1d | 76 | 0.01539 | 0.02212 | 0.4473 | 0.2017 | 0.00131 | 0.4276 |
| ma_20_100_fast_below_slow | 14d | 900 | 0.03329 | 0.0448 | 0.4473 | 0.2757 | 0.03012 | 0.04867 |
| rsi14_oversold | 3d | 76 | 0.02260 | 0.04755 | 0.4473 | 0.2827 | 0.00509 | 0.3011 |
| stoch14_cross_up | 3d | 522 | 0.01019 | 0.06505 | 0.4473 | 0.3589 | 0.00408 | 0.1363 |
| rsi14_oversold | 7d | 76 | 0.02864 | 0.06633 | 0.4473 | 0.3618 | 0.01312 | 0.07769 |
| ma_20_100_fast_below_slow | 7d | 900 | 0.01574 | 0.07257 | 0.4473 | 0.3882 | 0.01591 | 0.5268 |
| fib_618_above | 14d | 287 | 0.19262 | 0.07427 | 0.4473 | 0.3897 | -0.00278 | 0.1549 |
| fib_618_above | 7d | 287 | 0.09371 | 0.07629 | 0.4473 | 0.3913 | -0.00126 | 0.5758 |
| fib_618_above | 3d | 287 | 0.04138 | 0.07664 | 0.4473 | 0.3913 | -0.00084 | 0.395 |
| fib_500_above | 14d | 496 | 0.11528 | 0.08036 | 0.4473 | 0.3977 | -0.00467 | 0.05433 |
| ma_5_20_fast_above_slow | 3d | 827 | 0.01303 | 0.08142 | 0.4473 | 0.3988 | 0.00053 | 0.3225 |
| ma_5_20_fast_above_slow | 14d | 827 | 0.05206 | 0.09372 | 0.4473 | 0.4373 | 0.01010 | 0.3681 |

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
