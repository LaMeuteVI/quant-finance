# N1 TA alt panel — XRPUSDT (2026-10-15)

* Daily bars: **2249** from 2018-05-05 to 2024-06-30 (UTC).
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
| rsi14_oversold | 1d | 72 | 0.01940 | 0.01702 | 0.9763 | 0.9229 | -0.00093 | 0.3976 |
| fvg3_down_fill | 3d | 20 | -0.02288 | 0.02806 | 0.9763 | 0.9229 | -0.00064 | 0.1794 |
| fvg3_down_fill | 7d | 20 | -0.04049 | 0.03009 | 0.9763 | 0.9229 | -0.00140 | 0.1104 |
| fvg3_down_fill | 1d | 20 | -0.01017 | 0.04642 | 0.9763 | 0.9229 | -0.00019 | 0.4791 |
| rsi14_oversold | 14d | 72 | 0.07176 | 0.05575 | 0.9763 | 0.9229 | -0.00533 | 0.7849 |
| rsi14_oversold | 7d | 72 | 0.03241 | 0.08489 | 0.9763 | 0.9229 | -0.00289 | 0.521 |
| pivot_r1_break | 3d | 265 | 0.01894 | 0.094 | 0.9763 | 0.9229 | -0.00348 | 0.5011 |
| stoch14_overbought | 7d | 236 | 0.03577 | 0.1173 | 0.9763 | 0.9229 | -0.00617 | 0.4164 |
| rsi14_oversold | 3d | 72 | 0.02178 | 0.1175 | 0.9763 | 0.9229 | -0.00159 | 0.8202 |
| pivot_r1_break | 1d | 265 | 0.00692 | 0.1299 | 0.9763 | 0.9229 | -0.00124 | 0.3441 |
| pivot_s1_break | 3d | 207 | -0.01174 | 0.1343 | 0.9763 | 0.9229 | 0.00027 | 0.443 |
| stoch14_overbought | 3d | 236 | 0.01578 | 0.144 | 0.9763 | 0.9229 | -0.00279 | 0.5234 |

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
