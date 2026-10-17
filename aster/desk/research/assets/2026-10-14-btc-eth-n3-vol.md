# BTC/ETH N3 — realized volatility forecasts

**Status: descriptive pseudo-OOS forecast study only; no strategy, no holdout, no allocation.**

- Cutoff exclusive: `2024-07-01T00:00:00+00:00`; training boundary: `2022-12-31T23:59:59+00:00`.
- Validity gate: active minutes >= `720`, one-minute active pairs >= `1000`; minimum model history `756` observations.
- RV/BV are calculated from consecutive active 1-minute closes; frozen minutes and missing minutes are not imputed.
- Models: 30-observation naive, recursive HAR-RV, recursive GARCH(1,1) volatility benchmark.
- Evaluation: log-RV squared and absolute loss; DM-HLN with HAC bandwidth floor(N^(1/3)); BH-FDR across the fixed 12 model/loss/asset comparisons.

## Dataset audit

  symbol  minute_rows  daily_rows  valid_days
BTC/USDT      3605599        2510        2470
ETH/USDT      3605598        2510        2463

## Forecast comparison

  symbol     loss model_1 model_2  observations  mean_loss_diff_model1_minus_model2     dm_hln      p_value  year_2023_mean_diff  year_2024_mean_diff   bh_q_value  bh_q05
BTC/USDT  squared     har   naive           546                           -0.193462  -3.431225 6.008623e-04            -0.193062            -0.194262 6.008623e-04    True
BTC/USDT  squared   garch   naive           546                            0.564798   4.673049 2.967603e-06             0.745930             0.202533 3.956804e-06    True
BTC/USDT  squared     har   garch           546                           -0.758260  -7.069075 1.559698e-12            -0.938992            -0.396795 6.238794e-12    True
BTC/USDT absolute     har   naive           546                           -0.107172  -4.521911 6.128378e-06            -0.099301            -0.122915 7.354054e-06    True
BTC/USDT absolute   garch   naive           546                            0.257040   5.592422 2.239232e-08             0.333842             0.103437 4.478464e-08    True
BTC/USDT absolute     har   garch           546                           -0.364213 -10.137185 3.778291e-24            -0.433143            -0.226352 4.533950e-23    True
ETH/USDT  squared     har   naive           546                           -0.146487  -4.151791 3.298839e-05            -0.133426            -0.172607 3.598733e-05    True
ETH/USDT  squared   garch   naive           546                            0.544923   5.071232 3.952478e-07             0.684754             0.265262 5.928717e-07    True
ETH/USDT  squared     har   garch           546                           -0.691410  -6.275760 3.479304e-10            -0.818180            -0.437869 1.043791e-09    True
ETH/USDT absolute     har   naive           546                           -0.106431  -5.561496 2.674716e-08            -0.093818            -0.131655 4.585228e-08    True
ETH/USDT absolute   garch   naive           546                            0.258248   5.957179 2.566295e-09             0.314393             0.145959 6.159109e-09    True
ETH/USDT absolute     har   garch           546                           -0.364679  -8.872252 7.168156e-19            -0.408211            -0.277614 4.300893e-18    True

A lower loss for a volatility forecast is not alpha. No strategy hypothesis is registered from this report; any future volatility-targeting idea requires its own mechanism, costs, capacity, counted desk backtest, sealed holdout and paper-trading evidence.

Forecast artifact: `research/assets/2026-10-14-btc-eth-n3-vol.csv`; summary: `research/assets/2026-10-14-btc-eth-n3-vol-summary.csv`.
