# BTC N4 — regime cartography (descriptive only)

**Status: descriptive only.**

- Cutoff exclusive: `2024-07-01T00:00:00+00:00`.
- Trend regime: sign of the 5d vs 22d log-price mean difference at day t-1.
- Vol regime: 1 if rolling 22d annualised volatility is above the trailing 252d median, else 0.

## Class counts and mean run length

{
  "counts": {
    "trend=-1, vol=0": 611,
    "trend=-1, vol=1": 504,
    "trend=0, vol=0": 21,
    "trend=1, vol=0": 732,
    "trend=1, vol=1": 640
  },
  "persistence": [
    {
      "regime": "trend=-1, vol=0",
      "mean_run": 11.75,
      "n_days": 611
    },
    {
      "regime": "trend=-1, vol=1",
      "mean_run": 9.882352941176471,
      "n_days": 504
    },
    {
      "regime": "trend=0, vol=0",
      "mean_run": 21.0,
      "n_days": 21
    },
    {
      "regime": "trend=1, vol=0",
      "mean_run": 13.555555555555555,
      "n_days": 732
    },
    {
      "regime": "trend=1, vol=1",
      "mean_run": 12.307692307692308,
      "n_days": 640
    }
  ]
}

## Per-regime feature/horizon correlations

 regime_trend  regime_vol       feature  horizon_days  observations  spearman      p_value
           -1           0     imbalance             1           610  0.058647 1.479697e-01
           -1           0     imbalance             2           609 -0.002514 9.506248e-01
           -1           0     imbalance             5           606  0.002858 9.440253e-01
           -1           0 signed_dollar             1           610  0.514113 1.869310e-42
           -1           0 signed_dollar             2           609  0.345160 1.765647e-18
           -1           0 signed_dollar             5           606  0.214523 9.702178e-08
           -1           1     imbalance             1           504  0.074906 9.299361e-02
           -1           1     imbalance             2           504  0.035428 4.274057e-01
           -1           1     imbalance             5           504  0.024391 5.848617e-01
           -1           1 signed_dollar             1           504  0.471860 2.625073e-29
           -1           1 signed_dollar             2           504  0.319710 1.930662e-13
           -1           1 signed_dollar             5           504  0.210788 1.804457e-06
            1           0     imbalance             1           732  0.105394 4.309535e-03
            1           0     imbalance             2           732  0.060785 1.003245e-01
            1           0     imbalance             5           732  0.046124 2.126050e-01
            1           0 signed_dollar             1           732  0.544291 1.096337e-57
            1           0 signed_dollar             2           732  0.397454 4.095393e-29
            1           0 signed_dollar             5           732  0.267757 1.747056e-13
            1           1     imbalance             1           640  0.129567 1.018889e-03
            1           1     imbalance             2           640  0.102767 9.277840e-03
            1           1     imbalance             5           640  0.044622 2.596554e-01
            1           1 signed_dollar             1           640  0.522271 4.503465e-46
            1           1 signed_dollar             2           640  0.365384 1.201184e-21
            1           1 signed_dollar             5           640  0.256159 4.775601e-11

No regime filter is selected after viewing results.  Any future strategy must come from a fresh pre-registration.

Artifact: `research/assets/2026-10-14-btc-n4-regimes.csv`.
