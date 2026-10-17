# BTC N1/N2 statistics roadmap — smallest staged sequence

**Scope:** research infrastructure only for Binance spot `BTCUSDT`; fixed exploration cutoff `2024-07-01T00:00:00Z`. This roadmap proposes descriptive statistics and falsification tooling. It creates no hypothesis, strategy, trade, ledger trial, or backtest.

## Audit conclusion

### What is already usable

- **Immutable pre-cutoff source boundary and provenance:** `aster.data.r2_klines` restricts reads to approved local R2 partitions, audits schema/manifests, and refuses rows at or after the cutoff. `read_local()` returns a UTC-indexed minute frame.
- **Quality diagnostics:** `minute_quality.py` separates coverage gaps, frozen minutes, timestamp defects, price errors, and panel staleness; the CLI emits machine-readable reports.
- **Causal aggregation primitives:** `bars.py` provides 5m, 15m, 1h, 4h and 1d OHLCV/information bars with close labels, no synthetic empty intervals, and explicit frozen-minute handling. The tested `normalise_clock()` repair reports every changed offset/duplicate rather than silently modifying data.
- **Useful later-stage controls:** truncation-invariance, sealed holdout timing, purged CV, PSR/DSR/MinTRL, and CSCV/PBO already exist. They belong to registered-strategy/backtest work, not to descriptive N1.

### Current blocker and gaps

1. **BTC is not yet N0-cleared.** `research/atlas/quality-r2-2026-10-13.json` reports BTC `ok: false`, despite 99.7631% coverage and 0.6657% frozen minutes, because 21,602 timestamps are off the exact minute grid. `research/assets/2026-10-13-btc-n0-spec.md` correctly blocks N0 aggregation pending diagnosis. The clock-repair routine may be the remedy, but it has not yet been approved as a source-specific, persisted/reproducible repair with a post-repair quality disposition.
2. **The R2 quality gate and bar command are not connected.** `data quality-r2` rejects BTC pre-normalisation, while `data bars-r2` can normalise and summarize it. No command records a before/after audit, the affected timestamp ranges, repair metadata, or a post-repair quality verdict. N1 must not treat a bar-shape summary as a data-quality acceptance.
3. **No descriptive-return toolkit or artifact contract exists.** There is no pure function/CLI/test suite for log-return construction, horizon alignment, overlap flags, missing-interval exclusion, return moments/quantiles, autocorrelation, or UTC/session/regime tabulation. `backtest.metrics.summary()` is portfolio-performance reporting, not a reusable return-distribution/inference module.
4. **No signal-experiment registry or placebo/FDR layer exists.** `research/labeling.py` provides causal labels and `validation/stats.py` provides DSR, but there is no formal signal specification, test-family inventory, placebo generator, p/q-value calculation, robust dependence treatment, or immutable result manifest. Current DSR deflates only ledger-recorded strategy trials; it cannot count unregistered exploratory technical variants/horizons.
5. **Existing PBO is necessary later but not sufficient here.** `pbo_cscv()` accepts a matrix of strategy return series and is appropriate for a declared configuration sweep. It does not correct many signal/return association tests, preserve intraday dependence in a placebo, or establish a false-discovery budget.

## Stage order and stop rules

| Stage | Smallest deliverable | Exit criterion | Stop rule |
|---|---|---|---|
| Gate 0 | BTC timestamp-repair disposition | Before/after quality artifacts and an explicit acceptance/rejection of the repair | Any unexplained off-grid rows, duplicate collision, changed OHLC/volume beyond timestamp normalization, or failed post-repair audit blocks N0/N1/N2. |
| N0 closeout | Existing BTC N0 dossier outputs | All outputs required by `research/assets/2026-10-13-btc-n0-spec.md`, including gap/frozen taxonomy | No returns, forward outcomes, or technical indicators added. |
| N1 | BTC descriptive returns/horizon report and machine-readable tables | Tests prove time alignment, no gap bridging, and reproducibility from the accepted minute input | No signal ranking, threshold selection, trading weights, costs, or performance/backtest statistics. |
| N2a | Technical-signal specification and placebo-control framework | A test manifest is written before evaluating the first signal result; synthetic tests prove causal alignment and placebo invariants | No result may be called a discovery before multiplicity-adjusted inference. |
| N2b | Family-level inference/FDR report | All planned tests, raw p-values, adjusted q-values, and null/placebo diagnostics are retained | Any surviving result is only a research lead; it still requires triage and pre-registration before `desk backtest`. |

## Gate 0: minimal data disposition before N1

Do not change source data. Implement a **read-time, explicit repair recipe** only after confirming that the observed BTC offset is the documented source-clock defect and not mixed timestamp units or malformed rows.

Required evidence:

1. Run the existing raw audit and quality profile, retain stdout unchanged, and identify every offset value and contiguous affected range.
2. Apply `normalise_clock()` in memory; emit its `ClockRepair` object, including rows before/after, all offsets, duplicate drops, and NaT drops.
3. Re-run the full quality profile on the normalized UTC-minute index and compare raw versus repaired OHLCV row counts and aggregate volume/trades. Timestamp normalization must not alter a source value; any duplicate-resolution loss must be enumerated and reviewed.
4. Write a single provenance record linking the raw manifests, repair version/code revision, repair report, post-repair quality report, and output hashes. The N0 dossier should cite this record and state whether the repair is accepted.

This is intentionally not a silent relaxation of the current quality gate. If accepted, downstream N1/N2 readers must invoke the same named repair recipe and carry its identifier in every artifact.

## N1: descriptive return and horizon behavior

### Minimal implementation surface

Add one pure research module (for example `aster.research.returns`) and one read-only reporting command. The module should accept an already accepted, close-labelled bar frame and return tables; it must not import backtest, strategy, ledger, execution, or cost code. Add deterministic synthetic-data tests beside `tests/test_research.py` or in a dedicated test file.

The report command should accept only:

- `BTCUSDT` initially;
- a fixed set of bar horizons: **5m, 15m, 1h, 4h, 1d**;
- the accepted repair identifier and cutoff; and
- explicitly declared descriptive grouping dimensions (UTC hour, UTC weekday, UTC calendar month, and the policy-defined market eras).

It should write a human-readable dossier plus CSV/JSON tables under a date-stamped research artifact directory. The JSON manifest must include source-manifest hashes, code revision, exact command, cutoff, repair identifier, bar settings, exclusions, pandas/numpy versions, and hashes of every generated table.

### Definitions fixed before calculation

For close-labelled bars with close price \(C_t\), define the one-bar log return

\[
r_t = \log(C_t/C_{t-1}).
\]

For horizon \(h\) consecutive valid bars, define

\[
r_{t\rightarrow t+h}=\log(C_{t+h}/C_t).
\]

A return is valid only where both endpoint prices are finite/positive **and every expected source bar between endpoints is present**. Do not forward-fill prices, convert an absent interval to a zero return, or splice across a detected gap. Report invalid-return counts by horizon and by month. The bar's close label is known only at its closing timestamp; N1 contains descriptions only and makes no decision at that timestamp.

Keep two clearly labelled samples:

- **all valid bars**, and
- **clean contiguous bars** after exclusion of intervals touching a source gap or any explicitly disallowed quality state.

Frozen minutes are not automatically a missing price. Preserve the N0 distinction: report return results with the frozen-minute share of each aggregate interval available as a conditioning/quality column; do not silently delete frozen observations.

### Required N1 output

For each fixed horizon and sample definition:

1. Counts: candidate endpoints, valid observations, excluded endpoints by reason, first/last timestamp, and overlap indicator.
2. Distribution: arithmetic mean and median of log returns, standard deviation, MAD, p01/p05/p25/p75/p95/p99, min/max, skew, non-excess kurtosis, and fractions positive/negative/zero.
3. Dependence: ACF of returns and squared returns at predeclared lags 1, 2, 5, 10, 20; report, do not over-interpret, a Ljung–Box diagnostic at the same fixed maximum lag.
4. Horizon scaling: compare realized standard deviation with \(\sqrt{h}\) scaling from the one-bar standard deviation; label it a descriptive ratio, not a diffusion-model acceptance test.
5. Stable descriptive cuts: UTC hour, weekday, calendar month, and the policy-defined bull/bear/crash/chop eras. Display observation counts alongside every statistic and label overlapping-horizon rows as dependent.
6. Quality linkage: the distribution of `frozen_share`, source-gap exclusions, and bar counts by horizon. Every table must identify whether clock repair was applied.

No p-value, best horizon, directional claim, threshold, or parameter selection is needed in N1. The result is a baseline that makes later signal claims auditable.

### N1 minimum tests

- exact manual return values and sign convention;
- 5m/15m/1h endpoint alignment using close-labelled bars;
- a one-minute/source-bar hole invalidates every spanning return rather than creating a flat price;
- no forward fill, no `bfill`, no centered window, and no post-cutoff row can enter;
- truncating input leaves every already-computable descriptive row unchanged;
- overlapping versus non-overlapping horizon flags/counts are correct;
- UTC-aware index, monotonicity, duplicate, non-positive-close, and timezone failures raise rather than coerce.

## N2a: technical-signal formalization and placebo controls

N2 begins only after N1 artifacts are frozen. It evaluates **association**, not a trade simulation. Restrict the first pass to one BTC technical-signal family and a small, declared grid; do not turn an indicator library into an unbounded search engine.

### Pre-result signal specification

Before computation, create a versioned JSON/YAML test manifest containing:

- data artifact/repair ID and fixed cutoff;
- signal family name and economic/behavioral rationale;
- exact formula, inputs, lookback(s), threshold(s), transform, missing-data rule, and warm-up handling;
- decision timestamp: signal \(S_t\) uses only values known by close \(t\); target is a predeclared future return \(r_{t\rightarrow t+h}\), with \(h\) fixed in the manifest;
- test universe: all signal × horizon × regime × conditioning combinations, including tests expected to fail;
- primary endpoint (one per family), secondary endpoints, alpha/FDR method, dependence method, and placebo set;
- an immutable `experiment_id`, author/date, and a manifest hash written before result tables.

A technical indicator is not formalized by a chart name. Its output must be a causal numeric series with unit tests demonstrating that appending future prices cannot revise a prior signal value. Full-sample normalization, in-sample threshold fitting, parameter choice after observing outcomes, centered windows, and `shift(-k)` are disallowed by policy.

### Minimal association statistics

For each declared test, retain the entire aligned observation table or a hash-addressed parquet artifact containing `signal_time`, signal value/bin, target-end time, forward return, quality flags, and regime tag. Report:

- sample count and effective non-overlapping/block count;
- unconditional and signal-conditioned future-return means/medians and their difference;
- rank association (Spearman) and a simple signed/binned contrast only if its bins were declared beforehand;
- effect estimate with confidence interval and raw two-sided p-value;
- exact lag/horizon, number of overlapping labels, and any excluded rows.

Because forward horizons overlap and crypto returns are heteroskedastic/serially dependent, ordinary IID t-tests are not an acceptance criterion. Use a conservative dependence-aware primary inference method: a moving-block bootstrap or stationary bootstrap with a block length declared before inspection and at least as long as the target horizon; report the resampling seed and full null distribution. A HAC/Newey–West estimate can be a secondary sensitivity check with a predeclared lag at least \(h-1\), not a substitute for the placebo.

### Placebo controls (all required)

Each placebo is evaluated on the **same complete registered test list** and produces an empirical null distribution for the primary statistic.

1. **Circular block shift of the signal:** shift the complete causal signal series relative to the unchanged return path by predeclared offsets larger than the largest lookback plus horizon; use a set of offsets spanning distinct calendar phases. This preserves the signal's autocorrelation and distribution while breaking its claimed alignment with future returns. Exclude wrapped observations rather than silently joining across the sample boundary.
2. **Time-of-day/weekday-matched block permutation:** permute contiguous signal blocks within predeclared UTC hour-of-week strata. This tests whether an apparent signal is merely activity seasonality while retaining marginal clock effects and local dependence.
3. **Sign/direction placebo:** where the signal has a stated direction, evaluate the inverted signal under the same construction. It is a diagnostic, not an independent discovery; a symmetric result undermines a directional mechanism.
4. **Lag placebo:** apply the identical rule after a predeclared stale delay longer than the alleged information horizon. A result that is as strong after this delay indicates persistence, clock confounding, or a specification error rather than actionable timing.
5. **Synthetic null regression test:** unit tests on simulated dependent but no-predictive-edge data must show broadly calibrated placebo/adjusted inference. This verifies code behavior, not a market claim.

Do not use a lead-price “placebo” to validate a signal: it intentionally uses unavailable future information and belongs only in a negative leakage test expected to fail causal checks.

## N2b: multiple-testing and FDR requirements

### Test accounting

The experiment manifest is the source of truth for statistical trial count. Count every signal variant, horizon, threshold, transform, regime split, conditioning rule, and re-run that could influence selection—even if its result is omitted from a memo. A later alteration creates a new `experiment_id`; it cannot overwrite the prior manifest or shrink the family after results are known.

Maintain two ledgers with different purposes:

- **research test registry:** all N2 association/placebo tests and their multiplicity family; and
- **strategy trial ledger:** existing immutable hypothesis/backtest trials, which continue to supply family-level DSR, PBO for sweeps, and version limits after a hypothesis is registered.

Neither substitutes for the other.

### Family and correction rule

Use a hierarchical, dependency-robust rule:

1. Define one **primary family** as every primary signal/outcome association planned for the BTC technical family, including all examined horizons and declared regime/condition interactions. Set two-sided FDR target **q = 0.05**.
2. Apply **Benjamini–Yekutieli (BY)** to raw p-values in that family as the mandatory reported control because technical variants and overlapping return horizons are dependent in an unknown way. Report raw p-values, BY q-values, family size, and the rejection threshold for every test.
3. Only if the family has at least one BY-surviving primary result may secondary diagnostics within that selected signal branch be described. Secondary analyses remain labelled exploratory and receive their own BY correction; they do not establish a new discovery.
4. Placebo tests are not silently excluded. For each primary test, report an empirical placebo p-value (with the finite-resample correction \((1+\#\{|T_{null}|\ge |T_{obs}|\})/(1+B)\)) alongside the analytic/dependence-aware p-value. A primary result needs both BY q ≤ 0.05 and a predeclared satisfactory placebo diagnostic to be called a research lead.
5. If a bounded, clearly positive-dependence subset is later justified, BH q-values may be shown as a labelled sensitivity analysis, never replacing mandatory BY without written justification before results are read.

A result with a raw p-value below 0.05 but BY q-value above 0.05 is a non-discovery. It may remain in the registry as a negative result; it must not be tuned into a strategy.

### Required N2 report tables

- immutable manifest and test count by family;
- all tests, not only survivors: formula/version, horizon, sample count, effect, CI, raw p, empirical-placebo p, BY q, and status;
- placebo-null diagnostics: number of resamples/shifts, seeds/offsets, distribution quantiles, observed statistic position, and failed-invariant counts;
- sensitivity table: clean-contiguous versus all-valid samples, non-overlapping targets, and fixed policy regimes—each declared as a separate corrected family when used for inference;
- a limitations section: effective sample/bet count, overlap, data repairs/gaps, stationarity/regime risk, and why association is not execution evidence.

## Hand-off boundary after N2

A surviving N2 result is only eligible for **triage**, not implementation. It must still pass the research protocol's mechanism and 3× conservative-cost sanity check, ledger duplicate/rejection search, and immutable pre-registration. Only then can a strategy be written and `desk backtest` begin. At that later point the current pipeline's look-ahead test, sealed 25% holdout, DSR family accounting, stress costs/lags, PBO for sweeps, and paper gate remain mandatory.

## Recommended implementation sequence

1. Resolve Gate 0 and close the existing N0 dossier; do not broaden beyond BTC.
2. Add/test the pure N1 return builder and report writer with the fixed five horizons and artifact manifest.
3. Freeze one N2 technical-family manifest and implement only its causal signal interface, aligned association table, and synthetic tests.
4. Add the five required placebo controls and a reusable BY/empirical-p-value reporting function; test their invariants before touching BTC outcomes.
5. Run the registered N2 association report only after steps 1–4 are accepted. Any subsequent strategy work follows the existing pre-registration and backtest process.

This order is deliberately small: it adds one audited data disposition, one descriptive-return layer, and one bounded inference/control layer before any strategy or backtest code.
