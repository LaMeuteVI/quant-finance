# ETH N4 — regime cartography (descriptive only)

**Status: descriptive only.**

- Cutoff exclusive: `2024-07-01T00:00:00+00:00`.
- Trend regime: sign of the 5d vs 22d log-price mean difference at day t-1.
- Vol regime: 1 if rolling 22d annualised volatility is above the trailing 252d median, else 0.

## Class counts and mean run length

{
  "counts": {
    "trend=-1, vol=0": 698,
    "trend=-1, vol=1": 523,
    "trend=0, vol=0": 21,
    "trend=1, vol=0": 669,
    "trend=1, vol=1": 597
  },
  "persistence": [
    {
      "regime": "trend=-1, vol=0",
      "mean_run": 11.442622950819672,
      "n_days": 698
    },
    {
      "regime": "trend=-1, vol=1",
      "mean_run": 10.057692307692308,
      "n_days": 523
    },
    {
      "regime": "trend=0, vol=0",
      "mean_run": 21.0,
      "n_days": 21
    },
    {
      "regime": "trend=1, vol=0",
      "mean_run": 9.04054054054054,
      "n_days": 669
    },
    {
      "regime": "trend=1, vol=1",
      "mean_run": 8.91044776119403,
      "n_days": 597
    }
  ]
}

## Per-regime feature/horizon correlations

 regime_trend  regime_vol       feature  horizon_days  observations  spearman      p_value
           -1           0     imbalance             1           697  0.126320 8.307160e-04
           -1           0     imbalance             2           696  0.056938 1.334481e-01
           -1           0     imbalance             5           693  0.018687 6.233576e-01
           -1           0 signed_dollar             1           697  0.455729 4.853064e-37
           -1           0 signed_dollar             2           696  0.253974 1.045842e-11
           -1           0 signed_dollar             5           693  0.184490 1.008681e-06
           -1           1     imbalance             1           523  0.173173 6.863692e-05
           -1           1     imbalance             2           523  0.103215 1.822076e-02
           -1           1     imbalance             5           523 -0.023725 5.882613e-01
           -1           1 signed_dollar             1           523  0.533812 7.373113e-40
           -1           1 signed_dollar             2           523  0.394299 6.699888e-21
           -1           1 signed_dollar             5           523  0.235063 5.351087e-08
            1           0     imbalance             1           669  0.194143 4.184695e-07
            1           0     imbalance             2           669  0.129031 8.224008e-04
            1           0     imbalance             5           669  0.045843 2.363557e-01
            1           0 signed_dollar             1           669  0.550762 2.482826e-54
            1           0 signed_dollar             2           669  0.404696 9.405539e-28
            1           0 signed_dollar             5           669  0.250204 5.234388e-11
            1           1     imbalance             1           597  0.225077 2.707078e-08
            1           1     imbalance             2           597  0.137705 7.417420e-04
            1           1     imbalance             5           597  0.079880 5.108379e-02
            1           1 signed_dollar             1           597  0.542986 4.413009e-47
            1           1 signed_dollar             2           597  0.344137 4.857065e-18
            1           1 signed_dollar             5           597  0.227149 2.000541e-08

No regime filter is selected after viewing results.  Any future strategy must come from a fresh pre-registration.

Artifact: `research/assets/2026-10-14-eth-n4-regimes.csv`.
