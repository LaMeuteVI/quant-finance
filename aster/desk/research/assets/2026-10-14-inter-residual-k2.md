# Inter-asset residual factor study — K=2 (descriptive only)

**Status: descriptive only; no ledger hypothesis, no backtest, no holdout.**

- Cutoff exclusive: `2024-07-01T00:00:00+00:00`.
- Symbols: `BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, LINKUSDT, DOGEUSDT, XMRUSDT`.
- Returns: daily log-returns, frozen minutes excluded, days=1,288.
- Denoising: K-factor PCA with Marcenko-Pastur bound at q=T/N (T=1,288, N=8), eigenvalues below the bound averaged to signal mean.
- Sign alignment: F1 ↔ BTCUSDT, F2 ↔ ETHUSDT, F3 ↔ BNBUSDT.
- Lead-lag grid: (-2, -1, 0, 1, 2, 3, 5, 7) days, Spearman, 5,000 circular moving-block bootstraps (block 7), BH-FDR over the whole grid.
- Cross-section: residual momentum over lookbacks {3, 5, 10}, horizons [1, 3, 5, 7], daily top-bottom spread.

## Factor loadings (sign-aligned)

                F1        F2
BTCUSDT   0.391126  0.546173
ETHUSDT   0.408289  0.270025
BNBUSDT   0.364680 -0.196813
XRPUSDT   0.330618 -0.045843
SOLUSDT   0.327694  0.235094
LINKUSDT  0.385381 -0.725311
DOGEUSDT  0.256860 -0.041443
XMRUSDT   0.340796 -0.069877

## Pairwise lead-lag (448 cells)

Retained cells: `3` of `448`.

Top retained by |Spearman|:

  leader follower  lag_days  observations  spearman  p_value  bootstrap_lo  bootstrap_hi  placebo_spearman  placebo_p_value  bh_q_value  bh_survives_q05  bootstrap_excludes_zero  placebo_non_significant  stability  retention    abs_s
LINKUSDT  SOLUSDT         5          1283 -0.085040 0.002299     -0.146924     -0.026538         -0.009778         0.726420    0.023954             True                     True                     True       True       True 0.085040
 BTCUSDT  XMRUSDT        -1          1287  0.080615 0.003804      0.026037      0.133282         -0.005661         0.839272    0.036263             True                     True                     True       True       True 0.080615
 XMRUSDT  BTCUSDT         1          1287  0.080615 0.003804      0.026362      0.135656         -0.028239         0.311404    0.036263             True                     True                     True       True       True 0.080615

## Cross-section residual momentum

 horizon  lookback  n_days  mean_spread  std_spread    t_stat  p_value  bootstrap_lo  bootstrap_hi  bh_q_value  bh_survives_q05  bootstrap_excludes_zero
       1         3    1285    -0.031349    1.090654 -1.030360 0.303035     -0.090645      0.024250    0.785800            False                    False
       1         5    1283    -0.007079    1.086411 -0.233397 0.815490     -0.059523      0.044509    0.860822            False                    False
       1        10    1278    -0.038045    1.156119 -1.176403 0.239653     -0.101906      0.023644    0.785800            False                    False
       3         3    1283     0.005324    0.981123  0.194376 0.845913     -0.043750      0.053623    0.860822            False                    False
       3         5    1281    -0.025584    0.937360 -0.976872 0.328817     -0.080726      0.029616    0.785800            False                    False
       3        10    1276    -0.027707    1.005521 -0.984278 0.325166     -0.081994      0.025825    0.785800            False                    False
       5         3    1281     0.004345    0.886900  0.175363 0.860822     -0.045895      0.053457    0.860822            False                    False
       5         5    1279    -0.016336    0.916353 -0.637572 0.523867     -0.063882      0.031949    0.785800            False                    False
       5        10    1274    -0.020399    0.993381 -0.732967 0.463714     -0.078001      0.032171    0.785800            False                    False
       7         3    1279    -0.010263    0.965923 -0.380002 0.704007     -0.060919      0.039269    0.860822            False                    False
       7         5    1277    -0.020514    1.002668 -0.731125 0.464837     -0.073532      0.032278    0.785800            False                    False
       7        10    1272    -0.049455    0.961205 -1.835018 0.066737     -0.103915      0.001346    0.785800            False                    False

Retained cross-section cells (BH q<0.05 ∧ bootstrap excludes zero): `0` of `12`.

Artifacts: `research/assets/2026-10-14-inter-residual-k2-pairwise.csv`, `research/assets/2026-10-14-inter-residual-k2-crosssec.csv`, `research/assets/2026-10-14-inter-residual-k2-loadings.csv`.

**Conclusion: see top retained rows above. A cell is candidate for the ledger only if Spearman ≥ 0.20, BH q < 0.001, placebo non-significant, and ≥ 4 years of stable sign. None of the cells here is automatically promoted; promotion requires a separate memo and a pre-registered `desk backtest` trial count.**
