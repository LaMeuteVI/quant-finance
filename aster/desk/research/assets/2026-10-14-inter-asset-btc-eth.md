# BTC–ETH inter-asset descriptive study

**Status: descriptive only; no strategy validation or holdout read.**

- Development boundary: `2022-10-11T00:00:00+00:00`; cutoff: `2024-07-01T00:00:00+00:00`.
- Horizons: `[1, 3, 7, 14, 30, 60]`; lags: `[0, 1, 3, 7]`; bootstrap: `10000`, seed `20261014`.
- A lead-lag row compares a trailing leader return ending at t-k with the target forward return from t to t+h.
- BH-FDR is applied over the fixed 54-test grid. Overlapping returns mean the p-values are diagnostic, not independent evidence.

## Contemporaneous and lead–lag results

           kind  horizon_days  lag_days  direction  observations  correlation  spearman       p_value  bootstrap_lo  bootstrap_hi  bootstrap_excludes_zero    bh_q_value
contemporaneous             1         0 BTC_to_ETH          1880     0.789942  0.775244  0.000000e+00      0.736258      0.835883                     True  0.000000e+00
       lead_lag             1         0 BTC_to_ETH          1879    -0.069581       NaN  2.546144e-03           NaN           NaN                    False  5.092289e-03
       lead_lag             1         0 ETH_to_BTC          1879    -0.093217       NaN  5.191781e-05           NaN           NaN                    False  1.401781e-04
       lead_lag             1         1 BTC_to_ETH          1878     0.059115       NaN  1.039705e-02           NaN           NaN                    False  1.697611e-02
       lead_lag             1         1 ETH_to_BTC          1878     0.061186       NaN  7.995703e-03           NaN           NaN                    False  1.349275e-02
       lead_lag             1         3 BTC_to_ETH          1876     0.015836       NaN  4.930422e-01           NaN           NaN                    False  5.433526e-01
       lead_lag             1         3 ETH_to_BTC          1876     0.029138       NaN  2.071345e-01           NaN           NaN                    False  2.485615e-01
       lead_lag             1         7 BTC_to_ETH          1872    -0.006269       NaN  7.863458e-01           NaN           NaN                    False  8.011825e-01
       lead_lag             1         7 ETH_to_BTC          1872    -0.042493       NaN  6.604377e-02           NaN           NaN                    False  8.915910e-02
contemporaneous             3         0 BTC_to_ETH          1878     0.754404  0.771489  0.000000e+00      0.692627      0.806313                     True  0.000000e+00
       lead_lag             3         0 BTC_to_ETH          1875     0.062483       NaN  6.801257e-03           NaN           NaN                    False  1.224226e-02
       lead_lag             3         0 ETH_to_BTC          1875     0.018745       NaN  4.172319e-01           NaN           NaN                    False  4.793728e-01
       lead_lag             3         1 BTC_to_ETH          1874     0.086946       NaN  1.642438e-04           NaN           NaN                    False  4.223412e-04
       lead_lag             3         1 ETH_to_BTC          1874     0.052228       NaN  2.376124e-02           NaN           NaN                    False  3.467857e-02
       lead_lag             3         3 BTC_to_ETH          1872     0.053826       NaN  1.985858e-02           NaN           NaN                    False  2.978786e-02
       lead_lag             3         3 ETH_to_BTC          1872     0.002803       NaN  9.035420e-01           NaN           NaN                    False  9.035420e-01
       lead_lag             3         7 BTC_to_ETH          1868     0.026378       NaN  2.544926e-01           NaN           NaN                    False  2.987522e-01
       lead_lag             3         7 ETH_to_BTC          1868    -0.014723       NaN  5.248128e-01           NaN           NaN                    False  5.556842e-01
contemporaneous             7         0 BTC_to_ETH          1874     0.767723  0.772218  0.000000e+00      0.704940      0.821203                     True  0.000000e+00
       lead_lag             7         0 BTC_to_ETH          1867     0.080257       NaN  5.183311e-04           NaN           NaN                    False  1.272267e-03
       lead_lag             7         0 ETH_to_BTC          1867    -0.036134       NaN  1.185807e-01           NaN           NaN                    False  1.524608e-01
       lead_lag             7         1 BTC_to_ETH          1866     0.070873       NaN  2.188987e-03           NaN           NaN                    False  4.546357e-03
       lead_lag             7         1 ETH_to_BTC          1866    -0.041338       NaN  7.422005e-02           NaN           NaN                    False  9.775324e-02
       lead_lag             7         3 BTC_to_ETH          1864     0.050391       NaN  2.959310e-02           NaN           NaN                    False  4.097506e-02
       lead_lag             7         3 ETH_to_BTC          1864    -0.033017       NaN  1.541843e-01           NaN           NaN                    False  1.936267e-01
       lead_lag             7         7 BTC_to_ETH          1860     0.068296       NaN  3.209658e-03           NaN           NaN                    False  6.190055e-03
       lead_lag             7         7 ETH_to_BTC          1860     0.015440       NaN  5.057520e-01           NaN           NaN                    False  5.462121e-01
contemporaneous            14         0 BTC_to_ETH          1867     0.753348  0.765992  0.000000e+00      0.682452      0.818306                     True  0.000000e+00
       lead_lag            14         0 BTC_to_ETH          1853     0.124057       NaN  8.445574e-08           NaN           NaN                    False  2.682712e-07
       lead_lag            14         0 ETH_to_BTC          1853    -0.016538       NaN  4.767824e-01           NaN           NaN                    False  5.363802e-01
       lead_lag            14         1 BTC_to_ETH          1852     0.130611       NaN  1.688412e-08           NaN           NaN                    False  6.078284e-08
       lead_lag            14         1 ETH_to_BTC          1852    -0.014051       NaN  5.456448e-01           NaN           NaN                    False  5.666312e-01
       lead_lag            14         3 BTC_to_ETH          1850     0.129495       NaN  2.276403e-08           NaN           NaN                    False  7.682861e-08
       lead_lag            14         3 ETH_to_BTC          1850    -0.031110       NaN  1.810525e-01           NaN           NaN                    False  2.222008e-01
       lead_lag            14         7 BTC_to_ETH          1846     0.113223       NaN  1.076942e-06           NaN           NaN                    False  3.230827e-06
       lead_lag            14         7 ETH_to_BTC          1846    -0.059401       NaN  1.068866e-02           NaN           NaN                    False  1.697611e-02
contemporaneous            30         0 BTC_to_ETH          1851     0.740368  0.750350 2.796412e-321      0.621147      0.833225                     True 2.516770e-320
       lead_lag            30         0 BTC_to_ETH          1821     0.221088       NaN  1.342736e-21           NaN           NaN                    False  9.063471e-21
       lead_lag            30         0 ETH_to_BTC          1821    -0.078033       NaN  8.600862e-04           NaN           NaN                    False  2.019333e-03
       lead_lag            30         1 BTC_to_ETH          1820     0.219668       NaN  2.519759e-21           NaN           NaN                    False  1.360670e-20
       lead_lag            30         1 ETH_to_BTC          1820    -0.071829       NaN  2.168082e-03           NaN           NaN                    False  4.546357e-03
       lead_lag            30         3 BTC_to_ETH          1818     0.213984       NaN  2.845499e-20           NaN           NaN                    False  1.396881e-19
       lead_lag            30         3 ETH_to_BTC          1818    -0.066713       NaN  4.431231e-03           NaN           NaN                    False  8.251258e-03
       lead_lag            30         7 BTC_to_ETH          1814     0.204764       NaN  1.266951e-18           NaN           NaN                    False  5.701278e-18
       lead_lag            30         7 ETH_to_BTC          1814    -0.051600       NaN  2.797436e-02           NaN           NaN                    False  3.975303e-02
contemporaneous            60         0 BTC_to_ETH          1821     0.753682  0.759335  0.000000e+00      0.628262      0.857183                     True  0.000000e+00
       lead_lag            60         0 BTC_to_ETH          1761     0.232394       NaN  5.037820e-23           NaN           NaN                    False  3.886318e-22
       lead_lag            60         0 ETH_to_BTC          1761     0.057919       NaN  1.506329e-02           NaN           NaN                    False  2.324051e-02
       lead_lag            60         1 BTC_to_ETH          1760     0.224338       NaN  1.626695e-21           NaN           NaN                    False  9.760171e-21
       lead_lag            60         1 ETH_to_BTC          1760     0.063421       NaN  7.780854e-03           NaN           NaN                    False  1.349275e-02
       lead_lag            60         3 BTC_to_ETH          1758     0.206944       NaN  1.855605e-18           NaN           NaN                    False  7.707899e-18
       lead_lag            60         3 ETH_to_BTC          1758     0.074284       NaN  1.828734e-03           NaN           NaN                    False  4.114652e-03
       lead_lag            60         7 BTC_to_ETH          1754     0.177665       NaN  6.621591e-14           NaN           NaN                    False  2.554042e-13
       lead_lag            60         7 ETH_to_BTC          1754     0.101475       NaN  2.064134e-05           NaN           NaN                    False  5.866485e-05

## Annual one-day stability

 year  observations  correlation       p_value
 2017           135     0.474322  6.193245e-09
 2018           364     0.822734  7.916564e-91
 2019           364     0.821124  3.473988e-90
 2020           365     0.873809 1.037682e-115
 2021           364     0.778899  2.389081e-75
 2022           283     0.884971  2.841672e-95

## Residual diagnostics

 horizon_days  direction  lag_days  observations  residual_leader_correlation      p_value    slope
            1 BTC_to_ETH         0          1879                    -0.042319 6.665378e-02 1.005421
            1 BTC_to_ETH         1          1878                     0.031591 1.711752e-01 1.005421
            1 BTC_to_ETH         3          1876                     0.013047 5.722404e-01 1.005421
            1 BTC_to_ETH         7          1872                     0.014698 5.250679e-01 1.005421
            1 ETH_to_BTC         0          1879                    -0.062156 7.036224e-03 0.620643
            1 ETH_to_BTC         1          1878                     0.011245 6.262464e-01 0.620643
            1 ETH_to_BTC         3          1876                     0.022989 3.196408e-01 0.620643
            1 ETH_to_BTC         7          1872                    -0.034158 1.395840e-01 0.620643
            3 BTC_to_ETH         0          1875                     0.052694 2.250137e-02 0.956723
            3 BTC_to_ETH         1          1874                     0.068527 2.997269e-03 0.956723
            3 BTC_to_ETH         3          1872                     0.056989 1.366062e-02 0.956723
            3 BTC_to_ETH         7          1868                    -0.013650 5.554670e-01 0.956723
            3 ETH_to_BTC         0          1875                    -0.022427 3.317484e-01 0.594869
            3 ETH_to_BTC         1          1874                    -0.001309 9.548291e-01 0.594869
            3 ETH_to_BTC         3          1872                    -0.053065 2.167392e-02 0.594869
            3 ETH_to_BTC         7          1868                    -0.045705 4.825754e-02 0.594869
            7 BTC_to_ETH         0          1867                     0.067471 3.537398e-03 0.980635
            7 BTC_to_ETH         1          1866                     0.053555 2.069252e-02 0.980635
            7 BTC_to_ETH         3          1864                     0.020976 3.654155e-01 0.980635
            7 BTC_to_ETH         7          1860                     0.043005 6.369360e-02 0.980635
            7 ETH_to_BTC         0          1867                    -0.114107 7.681951e-07 0.601038
            7 ETH_to_BTC         1          1866                    -0.106785 3.783248e-06 0.601038
            7 ETH_to_BTC         3          1864                    -0.089980 1.002098e-04 0.601038
            7 ETH_to_BTC         7          1860                    -0.040333 8.203524e-02 0.601038
           14 BTC_to_ETH         0          1853                     0.092073 7.212507e-05 0.961925
           14 BTC_to_ETH         1          1852                     0.101155 1.291955e-05 0.961925
           14 BTC_to_ETH         3          1850                     0.110277 1.989268e-06 0.961925
           14 BTC_to_ETH         7          1846                     0.116761 4.893297e-07 0.961925
           14 ETH_to_BTC         0          1853                    -0.128082 3.155925e-08 0.589997
           14 ETH_to_BTC         1          1852                    -0.130289 1.831720e-08 0.589997
           14 ETH_to_BTC         3          1850                    -0.146536 2.409300e-10 0.589997
           14 ETH_to_BTC         7          1846                    -0.161873 2.626534e-12 0.589997
           30 BTC_to_ETH         0          1821                     0.186909 8.873824e-16 0.948189
           30 BTC_to_ETH         1          1820                     0.182910 3.712017e-15 0.948189
           30 BTC_to_ETH         3          1818                     0.175612 4.654331e-14 0.948189
           30 BTC_to_ETH         7          1814                     0.161611 4.390587e-12 0.948189
           30 ETH_to_BTC         0          1821                    -0.146114 3.740375e-10 0.578096
           30 ETH_to_BTC         1          1820                    -0.131367 1.856651e-08 0.578096
           30 ETH_to_BTC         3          1818                    -0.107579 4.282770e-06 0.578096
           30 ETH_to_BTC         7          1814                    -0.064830 5.741488e-03 0.578096
           60 BTC_to_ETH         0          1761                     0.230254 1.275739e-22 0.920616
           60 BTC_to_ETH         1          1760                     0.224289 1.660734e-21 0.920616
           60 BTC_to_ETH         3          1758                     0.208980 8.448834e-19 0.920616
           60 BTC_to_ETH         7          1754                     0.180428 2.664797e-14 0.920616
           60 ETH_to_BTC         0          1761                     0.059055 1.318961e-02 0.617018
           60 ETH_to_BTC         1          1760                     0.067325 4.718729e-03 0.617018
           60 ETH_to_BTC         3          1758                     0.084457 3.926295e-04 0.617018
           60 ETH_to_BTC         7          1754                     0.116616 9.721812e-07 0.617018

Joint bootstrap/FDR survivors: `6`. Only contemporaneous rows have bootstrap intervals by design.

No strategy is registered from these diagnostics. A candidate would require economic mechanism, residual stability, cost/capacity analysis and a new ledger preregistration.
