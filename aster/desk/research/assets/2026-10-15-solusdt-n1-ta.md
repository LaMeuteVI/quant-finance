# N1 TA alt panel — SOLUSDT (2026-10-15)

* Daily bars: **1419** from 2020-08-12 to 2024-06-30 (UTC).
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
| pivot_r1_break | 3d | 193 | 0.04272 | 0.001174 | 0.03261 | 0.04175 | 0.00234 | 0.02108 |
| ma_10_30_above | 3d | 543 | 0.02563 | 0.001316 | 0.03261 | 0.04175 | -0.00327 | 0.1501 |
| ma_10_30_above | 7d | 543 | 0.05876 | 0.002192 | 0.03261 | 0.04175 | -0.00691 | 0.04523 |
| rsi14_overbought | 3d | 180 | 0.05093 | 0.002396 | 0.03261 | 0.04175 | 0.00153 | 0.1752 |
| fib_500_above | 3d | 687 | 0.02008 | 0.0024 | 0.03261 | 0.04175 | -0.00365 | 0.9897 |
| ma_50_200_above | 3d | 496 | 0.02208 | 0.003448 | 0.03261 | 0.04175 | 0.00012 | 0.5962 |
| fib_618_above | 7d | 604 | 0.05129 | 0.003561 | 0.03261 | 0.04175 | -0.00593 | 0.08391 |
| fib_500_above | 7d | 687 | 0.04687 | 0.003821 | 0.03261 | 0.04175 | -0.00816 | 0.1477 |
| fib_618_above | 3d | 604 | 0.02043 | 0.004541 | 0.03411 | 0.04175 | -0.00149 | 0.8189 |
| ma_50_200_above | 7d | 496 | 0.05162 | 0.005372 | 0.03411 | 0.04175 | 0.00033 | 0.8908 |
| rsi14_overbought | 7d | 180 | 0.10144 | 0.006098 | 0.03411 | 0.04175 | 0.00620 | 0.04668 |
| fib_382_above | 3d | 793 | 0.01653 | 0.006167 | 0.03411 | 0.04175 | -0.00319 | 0.8658 |

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
