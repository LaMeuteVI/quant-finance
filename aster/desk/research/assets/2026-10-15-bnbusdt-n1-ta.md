# N1 TA alt panel — BNBUSDT (2026-10-15)

* Daily bars: **2428** from 2017-11-07 to 2024-06-30 (UTC).
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
| ma_5_20_fast_above_slow | 3d | 1331 | 0.01508 | 0.0005052 | 0.05402 | 0.1519 | -0.00272 | 0.1859 |
| ma_5_20_fast_above_slow | 7d | 1331 | 0.03200 | 0.001019 | 0.05402 | 0.1519 | -0.00246 | 0.2416 |
| ma_5_20_fast_above_slow | 1d | 1331 | 0.00510 | 0.001266 | 0.05402 | 0.1519 | -0.00099 | 0.06039 |
| ma_5_20_fast_above_slow | 14d | 1331 | 0.05985 | 0.004341 | 0.129 | 0.167 | -0.00129 | 0.125 |
| donchian20_breakout_up | 3d | 176 | 0.03161 | 0.006124 | 0.129 | 0.167 | 0.00523 | 0.0299 |
| donchian20_breakout_up | 7d | 176 | 0.05287 | 0.009052 | 0.129 | 0.191 | 0.01394 | 0.415 |
| donchian20_breakout_up | 14d | 176 | 0.13025 | 0.00915 | 0.129 | 0.191 | 0.02643 | 0.7043 |
| pivot_r1_break | 14d | 389 | 0.08798 | 0.009999 | 0.129 | 0.1922 | 0.02363 | 0.3103 |
| stoch14_overbought | 14d | 569 | 0.07869 | 0.01098 | 0.129 | 0.1948 | 0.02022 | 0.328 |
| rsi14_overbought | 7d | 244 | 0.07946 | 0.01122 | 0.129 | 0.1948 | 0.00975 | 0.96 |
| stoch14_overbought | 7d | 569 | 0.03641 | 0.0115 | 0.129 | 0.1948 | 0.01074 | 0.1202 |
| stoch14_overbought | 1d | 569 | 0.00676 | 0.01214 | 0.129 | 0.1948 | 0.00110 | 0.1061 |

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
