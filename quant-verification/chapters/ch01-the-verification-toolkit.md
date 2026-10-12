# Chapter 1: The Verification Toolkit

> Quant Verification, Chapter 1.

## Core Idea

The verification toolkit is the standard Python libraries: **NumPy** (array operations), **SciPy** (special functions, distributions, optimisation), **pandas** (data wrangling), **statsmodels** (time-series), **scikit-learn** (ML), **mlfinlab** (the LdP framework). For each formula, the agent writes a one-line script and runs it before publishing the chapter.

## The Toolkit

- **NumPy** — `np.mean, np.std, np.var, np.cumsum, np.diff, np.sqrt, np.exp, np.log`.
- **SciPy.stats** — `norm.ppf, norm.pdf, t.ppf, chi2.ppf, jarque_bera, shapiro, kstest, adfuller, kpss`.
- **pandas** — `pd.read_csv, pd.DataFrame.rolling, .ewm, .corr, .cov, .pct_change, .shift, .diff`.
- **statsmodels** — `statsmodels.tsa.arima.model.ARIMA, .VAR, .GARCH, statsmodels.regression.linear_model.OLS`.
- **scikit-learn** — `LinearRegression, RandomForestRegressor, GradientBoostingRegressor, StandardScaler, train_test_split`.
- **mlfinlab** (Hudson & Thames) — `BetSizing, FeatureImportance, CrossValidation, BacktestStatistics, StructFin`.

## Worked Example

*Setup.* Verify the SVI total variance formula from `gatheral-volatility-surface` ch03.

*Step 1 — Write the script*:
```python
import numpy as np
a, b, rho, m, sigma = 0.04, 0.5, -0.7, 0.0, 0.4
k = np.log(0.9)  # log-moneyness for K=90, F=100
w = a + b * (rho * (k - m) + np.sqrt((k - m)**2 + sigma**2))
print(f"SVI w(k) = {w:.4f}")  # -> 0.2835
```

*Step 2 — Run*. The script produces 0.2835, matching the chapter's worked example.

## Key Takeaways

1. The toolkit is standard Python: NumPy, SciPy, pandas, statsmodels.
2. Every formula gets a one-line script.
3. The script output is the published number.

## Connects To

ch02 (Cross-Check Protocol), ch03 (Error Taxonomy).
