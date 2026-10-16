# N1 TA alt panel — LINKUSDT (2026-10-15)

* Daily bars: **1992** from 2019-01-17 to 2024-06-30 (UTC).
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
| donchian20_breakout_down | 1d | 61 | 0.02281 | 0.02924 | 0.5777 | 0.2264 | 0.00100 | 0.7405 |
| pivot_r1_break | 1d | 277 | 0.00825 | 0.03081 | 0.5777 | 0.2275 | 0.00060 | 0.8634 |
| pivot_r1_break | 3d | 277 | 0.01966 | 0.03428 | 0.5777 | 0.2385 | 0.00270 | 0.4906 |
| ma_5_20_fast_above_slow | 1d | 1044 | 0.00362 | 0.03898 | 0.5777 | 0.2529 | -0.00027 | 0.2524 |
| stoch14_overbought | 3d | 393 | 0.01240 | 0.08336 | 0.5777 | 0.4042 | 0.00326 | 0.2151 |
| fib_382_above | 14d | 1228 | 0.03504 | 0.09721 | 0.5777 | 0.4378 | 0.00618 | 0.3076 |
| bb20_lower_break | 7d | 67 | 0.02995 | 0.09759 | 0.5777 | 0.4378 | 0.01112 | 0.4677 |
| ma_5_20_fast_above_slow | 3d | 1044 | 0.00770 | 0.1059 | 0.5777 | 0.4538 | 0.00277 | 0.3454 |
| fib_382_above | 7d | 1228 | 0.01728 | 0.107 | 0.5777 | 0.4538 | 0.00288 | 0.05235 |
| bb20_lower_break | 1d | 67 | 0.01442 | 0.1195 | 0.5777 | 0.4665 | 0.00122 | 0.3932 |
| fib_382_above | 3d | 1228 | 0.00699 | 0.1236 | 0.5777 | 0.4709 | 0.00196 | 0.6028 |
| rsi14_overbought | 3d | 136 | 0.02472 | 0.1437 | 0.5777 | 0.5046 | 0.00362 | 0.103 |

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
