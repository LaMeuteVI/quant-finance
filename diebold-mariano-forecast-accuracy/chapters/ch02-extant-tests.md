# Chapter 2: Extant Tests

> **Source**: Diebold & Mariano (1995), Section 2. ⚠ OCR source; reconstructed.

## Core Idea

The 1995 DM paper was written because the *existing* tests of forecast comparison were inadequate. This section reviews the pre-1995 tests and explains *why* they fail: the Diebold-Granger-Newbold (1974) test assumes iid Gaussian loss differences; the standard t-test requires serial independence; the nonparametric sign test ignores ties; the Morgan-Granger-Newbold test requires the loss function to be quadratic. The DM test's contribution is to be robust to all of these failure modes.

## Frameworks Introduced

- **The Pre-1995 Test Landscape**:
  - The **paired t-test** (most common): requires iid Gaussian loss differences.
  - The **Diebold-Granger (1983) sign test**: nonparametric, but loses power due to ties.
  - The **Morgan-Granger-Newbold (1980) test**: requires the loss function to be quadratic.
  - The **Cox (1961) test**: requires the loss function to be exponential.
  - The **Granger-Newbold (1986) test**: requires the loss to be squared and the errors to be Gaussian.

- **The Three Failure Modes of the Pre-1995 Tests**:
  1. **Serial correlation in the loss differences**: the test statistic is biased; the size is wrong.
  2. **Contemporaneous correlation between the forecasts**: the loss differences are correlated; the variance is underestimated.
  3. **Asymmetric or non-quadratic loss**: the test statistic is misspecified; the conclusion is wrong.

- **The DM Test's Solution**:
  - The DM test uses a HAC variance estimator (Newey-West 1987) to handle serial correlation.
  - The DM test uses a *general* loss function (not restricted to squared or absolute).
  - The DM test does not require the errors to be Gaussian; the asymptotic distribution is `N(0, 1)` for any loss function.

## Key Concepts

1. **Loss difference `d_t`** — the difference in losses between the two forecasts.
2. **The loss function `L(e)`** — the cost of the forecast error; the modelling choice.
3. **Serial correlation** — the autocorrelation in the loss differences; the first failure mode.
4. **Contemporaneous correlation** — the correlation between the two forecasts' errors at the same time; the second failure mode.
5. **HAC variance** — the Newey-West variance estimator; robust to serial correlation.
6. **Asymmetric loss** — a loss function that penalises positive and negative errors differently; the third failure mode.

## Worked Example (RECOMPUTED)

*Setup.* A paired t-test of two forecasts. The loss differences have serial correlation 0.3 and the sample size is 100.

*Step 1 — The biased t-statistic*:
- The iid t-statistic is `t = d̄ / (s_d / √N) = -2.5` (significant at 95%).

*Step 2 — The HAC-corrected t-statistic*:
- The HAC variance is *larger* than the iid variance: `V_HAC = V_iid × (1 + 2 × Σ ρ_h) ≈ V_iid × (1 + 2 × 0.3) = 1.6 × V_iid`.
- The HAC t-statistic is `t_HAC = -2.5 / √1.6 = -1.98` (still significant at 95% but barely).

*Step 3 — The DM statistic*:
- `DM = d̄ / √(V_HAC / N) = -1.98` (same as HAC t-statistic in this case).

## Anti-patterns

- **Using the paired t-test in the presence of serial correlation.** Use the DM test.
- **Using the sign test when there are many ties.** Use the DM test.
- **Using the squared-error test with asymmetric loss.** Use the DM test.

## Key Takeaways

1. **The pre-1995 tests fail** under serial correlation, contemporaneous correlation, or asymmetric loss.
2. **The DM test is robust** to all three failure modes.
3. **The HAC variance** is the key innovation.

## Connects To

- **ch01** (Testing Equality of Forecast Accuracy): the DM test.
- **ch03** (Monte Carlo Analysis): the size and power properties.
- **ch04** (Empirical Example): the exchange-rate forecast.
