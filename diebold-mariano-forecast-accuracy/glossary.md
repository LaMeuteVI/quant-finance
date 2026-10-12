# Glossary — Diebold & Mariano (1995)

- **Asymptotic distribution** — the limiting distribution of a test statistic as N → ∞; `N(0, 1)` for the DM statistic.
- **Bandwidth `H`** — the truncation lag for the HAC estimator; typically `H = ⌊N^(1/3)⌋`.
- **Bartlett kernel** — the standard kernel for the HAC estimator; weights `1 − h/(H+1)`.
- **Cox (1961) test** — the exponential-loss forecast comparison test.
- **DM statistic** — the t-statistic of the differential loss; `N(0, 1)` under H0.
- **Differential loss `d_t`** — the difference in losses between the two forecasts.
- **Diebold-Granger (1983) sign test** — a nonparametric forecast comparison test; loses power due to ties.
- **Familywise error rate** — the probability of at least one false positive across many tests.
- **HAC variance** — the Heteroskedasticity-Autocorrelation Consistent variance estimator; robust to serial correlation.
- **HLN (1997) small-sample correction** — the correction to the DM statistic for small N; essential for N < 100.
- **Loss function `L(e)`** — the cost of the forecast error; the modelling choice.
- **MGN (Morgan-Granger-Newbold 1980) test** — the squared-error forecast comparison test; fails for non-quadratic losses.
- **Newey-West (1987) estimator** — the canonical HAC variance estimator.
- **Reality Check (White 2000)** — the bootstrap-based test for many-model forecast comparison.
- **SPA (Hansen 2005)** — the Superior Predictive Ability test; an improved Reality Check.
- **SPA (Clark-West 2007)** — the nested-forecast version of SPA.
