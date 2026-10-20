# Inter-asset residual factor study — K=3 (descriptive only)

**Status: descriptive only; no ledger hypothesis, no backtest, no holdout.**

- Cutoff exclusive: `2024-07-01T00:00:00+00:00`.
- Symbols: `BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, LINKUSDT, DOGEUSDT, XMRUSDT`.
- Returns: daily log-returns, frozen minutes excluded, days=1,288.
- Denoising: K-factor PCA with Marcenko-Pastur bound at q=T/N (T=1,288, N=8), eigenvalues below the bound averaged to signal mean.
- Sign alignment: F1 ↔ BTCUSDT, F2 ↔ ETHUSDT, F3 ↔ BNBUSDT.
- Lead-lag grid: (-2, -1, 0, 1, 2, 3, 5, 7) days, Spearman, 5,000 circular moving-block bootstraps (block 7), BH-FDR over the whole grid.
- Cross-section: residual momentum over lookbacks {3, 5, 10}, horizons [1, 3, 5, 7], daily top-bottom spread.

## Factor loadings (sign-aligned)

                F1        F2        F3
BTCUSDT   0.391126  0.533470 -0.557747
ETHUSDT   0.408289  0.468110  0.676425
BNBUSDT   0.364680 -0.144774  0.325143
XRPUSDT   0.330618 -0.239936 -0.088021
SOLUSDT   0.327694  0.140440 -0.280809
LINKUSDT  0.385381 -0.592480 -0.016774
DOGEUSDT  0.256860 -0.053545  0.058578
XMRUSDT   0.340796 -0.210074 -0.187976

## Pairwise lead-lag (448 cells)

Retained cells: `6` of `448`.

Top retained by |Spearman|:

  leader follower  lag_days  observations  spearman  p_value  bootstrap_lo  bootstrap_hi  placebo_spearman  placebo_p_value  bh_q_value  bh_survives_q05  bootstrap_excludes_zero  placebo_non_significant  stability  retention    abs_s
 BNBUSDT  XMRUSDT         1          1287  0.107115 0.000118      0.048190      0.164430          0.009671         0.728873    0.001469             True                     True                     True       True       True 0.107115
 BNBUSDT  XMRUSDT        -1          1287  0.085993 0.002017      0.030107      0.142672          0.024654         0.377036    0.019979             True                     True                     True       True       True 0.085993
 XMRUSDT  BNBUSDT         1          1287  0.085993 0.002017      0.029277      0.142032          0.009671         0.728873    0.019979             True                     True                     True       True       True 0.085993
 XMRUSDT  BNBUSDT        -2          1286 -0.085418 0.002171     -0.143951     -0.025849          0.050250         0.071752    0.020262             True                     True                     True       True       True 0.085418
 ETHUSDT DOGEUSDT         5          1283  0.079413 0.004424      0.012063      0.146611          0.019287         0.490049    0.040448             True                     True                     True       True       True 0.079413
LINKUSDT  BNBUSDT        -1          1287 -0.077726 0.005272     -0.131507     -0.023320          0.033623         0.228235    0.046311             True                     True                     True       True       True 0.077726

## Cross-section residual momentum

 horizon  lookback  n_days  mean_spread  std_spread    t_stat  p_value  bootstrap_lo  bootstrap_hi  bh_q_value  bh_survives_q05  bootstrap_excludes_zero
       1         3    1285    -0.028641    1.217970 -0.842948 0.399415     -0.094997      0.033597    0.752206            False                    False
       1         5    1283     0.008146    1.233640  0.236508 0.813077     -0.051709      0.070259    0.813077            False                    False
       1        10    1278    -0.038758    1.128620 -1.227666 0.219799     -0.100922      0.021897    0.527517            False                    False
       3         3    1283     0.017632    1.134855  0.556513 0.577957     -0.038185      0.074340    0.766991            False                    False
       3         5    1281    -0.057140    0.966686 -2.115571 0.034574     -0.112342     -0.002116    0.367651            False                     True
       3        10    1276    -0.045771    1.017338 -1.607111 0.108278     -0.102264      0.009632    0.433111            False                    False
       5         3    1281    -0.008783    0.912245 -0.344602 0.730451     -0.057524      0.040911    0.796855            False                    False
       5         5    1279    -0.019783    0.913527 -0.774486 0.438787     -0.070148      0.029485    0.752206            False                    False
       5        10    1274    -0.040572    0.992172 -1.459559 0.144658     -0.098006      0.012958    0.433975            False                    False
       7         3    1279    -0.013859    0.998811 -0.496222 0.619823     -0.066709      0.038482    0.766991            False                    False
       7         5    1277    -0.013025    0.992459 -0.468987 0.639159     -0.065890      0.038770    0.766991            False                    False
       7        10    1272    -0.050689    0.965124 -1.873165 0.061275     -0.100696     -0.001948    0.367651            False                     True

Retained cross-section cells (BH q<0.05 ∧ bootstrap excludes zero): `0` of `12`.

Artifacts: `research/assets/2026-10-14-inter-residual-k3-pairwise.csv`, `research/assets/2026-10-14-inter-residual-k3-crosssec.csv`, `research/assets/2026-10-14-inter-residual-k3-loadings.csv`.

**Conclusion: see top retained rows above. A cell is candidate for the ledger only if Spearman ≥ 0.20, BH q < 0.001, placebo non-significant, and ≥ 4 years of stable sign. None of the cells here is automatically promoted; promotion requires a separate memo and a pre-registered `desk backtest` trial count.**
