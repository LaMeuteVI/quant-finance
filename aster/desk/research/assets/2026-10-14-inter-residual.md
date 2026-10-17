# Inter-asset residual factor study (descriptive only)

**Status: descriptive only; no ledger hypothesis, no backtest, no holdout.**

- Cutoff exclusive: `2024-07-01T00:00:00+00:00`.
- Symbols: `BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, LINKUSDT, DOGEUSDT, XMRUSDT`.
- Returns: daily log-returns, frozen minutes excluded, days=1,288.
- Denoising: Marcenko-Pastur max eigenvalue bound at q=T/N with T=1,288, N=8.
- Lead-lag grid: (-2, -1, 0, 1, 2, 3, 5, 7) days, Spearman, 5,000 circular moving-block bootstraps (block 7), BH-FDR over the whole grid.
- Cross-section: residual momentum over lookbacks {3, 5, 10}, horizons [1, 3, 5, 7], daily top-bottom spread.

## Factor loadings (1st factor, sign-aligned to BTC positive)

               MKT
BTCUSDT   0.391126
ETHUSDT   0.408289
BNBUSDT   0.364680
XRPUSDT   0.330618
SOLUSDT   0.327694
LINKUSDT  0.385381
DOGEUSDT  0.256860
XMRUSDT   0.340796

## Pairwise lead-lag (448 cells)

Retained cells: `5` of `448`.

## Cross-section residual momentum

 horizon  lookback  n_days  mean_spread  std_spread    t_stat  p_value  bootstrap_lo  bootstrap_hi  bh_q_value  bh_survives_q05  bootstrap_excludes_zero
       1         3    1285    -0.045209    1.156443  0.009364 0.737348           NaN           NaN    0.997622            False                    False
       1         5    1283    -0.026005    1.138620 -0.006721 0.809937           NaN           NaN    0.997622            False                    False
       1        10    1278    -0.040891    1.186718  0.006680 0.811442           NaN           NaN    0.997622            False                    False
       3         3    1283    -0.024430    1.027798  0.011692 0.675658           NaN           NaN    0.997622            False                    False
       3         5    1281    -0.050053    0.969614  0.004428 0.874199           NaN           NaN    0.997622            False                    False
       3        10    1276    -0.019055    1.081166  0.000084 0.997622           NaN           NaN    0.997622            False                    False
       5         3    1281     0.003558    0.910302 -0.038096 0.172995           NaN           NaN    0.997622            False                    False
       5         5    1279     0.004077    0.946649 -0.030129 0.281614           NaN           NaN    0.997622            False                    False
       5        10    1274    -0.025184    1.031806  0.014044 0.616517           NaN           NaN    0.997622            False                    False
       7         3    1279    -0.020699    0.954788  0.002229 0.936513           NaN           NaN    0.997622            False                    False
       7         5    1277    -0.034899    1.051198  0.023333 0.404787           NaN           NaN    0.997622            False                    False
       7        10    1272    -0.055057    0.995858 -0.027339 0.329920           NaN           NaN    0.997622            False                    False

Retained cross-section cells (BH q<0.05 ∧ bootstrap excludes zero): `0` of `12`.

Artifacts: `research/assets/2026-10-14-inter-residual-pairwise.csv`, `research/assets/2026-10-14-inter-residual-crosssec.csv`.

**Conclusion: surviving cells are at Spearman 0.08-0.12 (1% R²), statistically significant but not tradable. The contemporaneous residual correlations (|0.18-0.23|) reveal that a single market factor does not exhaust the common variance; 2-3 factors are likely needed. No ledger hypothesis is registered.**
