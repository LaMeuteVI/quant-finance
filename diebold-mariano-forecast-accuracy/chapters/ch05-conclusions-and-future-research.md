# Chapter 5: Conclusions and Future Research

> **Source**: Diebold & Mariano (1995), Section 5, with **⚠ Practitioner update** for 2026. ⚠ OCR source; reconstructed.

## Core Idea

The 1995 paper concluded that the DM test is a robust tool for forecast comparison, with the caveat that it is a *two-model* test. The future research directions (handled in subsequent literature) are (1) the small-sample correction (HLN 1997), (2) the nested-forecast correction (Clark-West 2001), (3) the many-model extension (White Reality Check 2000, Hansen SPA 2005), and (4) the multiple-testing correction (Harvey-Liu 2015, Bailey-López de Prado DSR).

## ⚠ Practitioner Update (2026)

The 1995 paper is the *foundational* paper for forecast comparison, but a 2026 quant agent must know the *extensions*:

1. **Harvey, Leybourne & Newbold (1997)** — the small-sample correction. The uncorrected DM statistic is badly size-distorted in small N. Always use the HLN correction for N < 100.
2. **Clark & West (2001)** — the nested-forecast correction. When forecast 2 nests forecast 1 (e.g. forecast 1 is a restricted version of forecast 2), the standard DM test reverses sign in small samples. The Clark-West adjustment subtracts the sample variance of the forecast-error-difference increment.
3. **White (2000) "A Reality Check for Data Snooping"** — the test for comparing *many* models. White's Reality Check uses the *maximum* t-statistic across models; it controls the familywise error rate.
4. **Hansen (2005) "A Test for Superior Predictive Ability" (SPA)** — the improved Reality Check; the bootstrap-based test for whether the *best* of many models is significantly better than a benchmark.
5. **Clark & West (2007)** — the nested-forecast version of SPA. Use this when comparing a model against a set of nested alternatives.
6. **Harvey, Liu & Zhu (2015) "…and the Cross-Section of Expected Returns"** — the multiple-testing correction for the cross-section of anomalies. The 3.0 t-stat threshold.
7. **Bailey & López de Prado (2014) "The Deflated Sharpe Ratio"** — the SR-corrected-for-multiple-testing version of the DM test.
8. **Diebold & Mariano (2002)** — the multivariate DM test for comparing forecasts of vector time series.

### The 2026 Institutional Decision Tree for Forecast Comparison

```
How many forecasts are you comparing?
  ├─ 2 forecasts → Use the DM test (with HLN correction)
  ├─ 2 nested forecasts → Use the Clark-West (2001) test
  └─ Many forecasts → Use Hansen SPA (2005) or White Reality Check (2000)
      └─ Comparing to a benchmark → SPA
      └─ Comparing to the best alternative → Reality Check

Are you using the test on the cross-section of anomalies?
  └─ Yes → Apply the Harvey-Liu 2015 haircut (3.0 t-stat)

Are you using the test on a backtest SR?
  └─ Yes → Apply the DSR (Bailey-López de Prado 2014)
```

## Key Takeaways

1. **The DM test is the foundation**; the 2026 extensions are necessary for most practical use cases.
2. **The HLN small-sample correction is essential** for N < 100.
3. **The Clark-West correction is essential** for nested forecasts.
4. **Hansen SPA / White Reality Check are the correct tests** for many-model comparison.
5. **The DSR is the correct test** for backtest SRs.

## Connects To

- **ch01** (DM statistic).
- **ch04** (empirical example).
- **`lopez-de-prado-afml` ch14 (Backtest Statistics)**: the DSR, PBO, MinTRL.
- **`hull-risk-management` ch12 (VaR and ES)**: the backtest of a VaR model uses the same discipline.
