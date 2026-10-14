# Research memo: BTC N1 technical-signal design — 2026-10-13

Role: price-researcher  
Written without reading other agents' memos: yes  
Status: design only. No market data, signal outcomes, returns, ledger, code, or holdout were accessed. The development cutoff is **2024-07-01**; the holdout remains sealed.

## One preregistration candidate: BTC daily time-series momentum (N1)

**Statement.** In BTC/USDT spot, a positive trailing 20-calendar-day log return predicts a sufficiently positive next-day BTC return to make a long/cash rule profitable after conservative spot trading costs. This is one signal, one lookback, and one holding horizon—not a parameter grid.

**Mechanism.** Trend continuation can arise when slow-moving information and persistent risk demand are incorporated gradually by heterogeneous crypto participants. It is a directional continuation claim, not a claim about chart patterns.

### Fixed, causal rule

Let \(C_t\) be the BTC/USDT daily close at 00:00 UTC on date \(t\), and let \(r_t=\log(C_t/C_{t-1})\). Daily bars are calendar days (365-day annualization).

1. At the completed close \(t\), calculate \(m_t=\log(C_t/C_{t-20})\). Values before 20 completed daily closes are undefined and the target is cash.
2. Set the target decided at \(t\):
   \[
   w_t=\mathbf{1}\{m_t>0\}\in\{0,1\}.
   \]
   A zero signal is cash; no discretionary tie-break or volatility scaling is allowed.
3. Execute \(w_t\) at the next daily-bar execution point, \(t+1\), and hold unchanged until the following execution point, \(t+2\), unless the next completed-close signal changes it. Thus every decision has **one daily holding horizon** and uses only information available no later than \(t\). The backtest must enforce at least this one-bar execution lag and its lag-2 stress test.

The sole strategy return is the BTC exposure selected by this rule, less trading costs. No leverage, shorting, funding, cross-asset ranking, or fitted thresholds belong to N1.

### Directional control and placebo

- **Inverse control (predefined):** \(w_t^{inv}=\mathbf{1}\{m_t<0\}\). It is also long/cash, has identical timing, and is not a separately tuned strategy. It asks whether the sign of the trend observation, rather than merely intermittent BTC exposure, matters.
- **Sign-permuted placebo (predefined):** On the same eligible decision dates, form the observed sequence \(s_t=2w_t-1\); draw a uniform random permutation of its time ordering using NumPy `Generator(PCG64(20261013))`; convert the permuted sequence back to \(w_t^{pl}=(s_t^{perm}+1)/2\). Run exactly 1,000 permutations, applying the same lag, execution and cost model to each. This preserves the number of long and cash decisions while destroying their date association. It is a diagnostic control, not a source of parameter selection.

## Costs, capacity, and test discipline

The initial cost assumption is the desk configuration: 10 bps taker fee plus 5 bps slippage **per side**. Charge
\[
TC_t=0.0015\,|w_t-w_{t-1}|
\]
of contemporaneous portfolio value at each execution; a full cash-to-BTC-to-cash round trip therefore costs 30 bps before any size-dependent impact. Test at 2x and 3x costs, as required by desk policy.

Before deployment, capacity must be bounded using daily BTC/USDT quote ADV measured from the point-in-time source: proposed order notional \(Q\) must satisfy \(Q\leq1\%\,ADV_{20}\), and the capacity report must add square-root impact \(Y\sigma\sqrt{Q/ADV_{20}}\) per side using a documented \(Y\). This is a deployment constraint, not an estimated result. The candidate should not proceed if its expected gross gain per completed round trip is below three times the 30-bp round-trip cost (90 bps) under the selected size model.

## Precommitted falsification

After proper registration, test only the fixed N1 rule on the development sample ending 2024-06-30. Reject the hypothesis if the costed, one-bar-lagged primary rule fails **any** desk development gate: at least 500 observations, annualized Sharpe \(\geq0.8\), maximum drawdown \(\geq-0.35\), DSR \(\geq0.95\), and annualized Sharpe \(\geq0.3\) under both 2x costs and lag-2 stress. Also reject if its costed performance is not better than the median sign-permuted placebo or if the inverse control is at least as strong on the preregistered primary statistic. No revision of lookback, threshold, horizon, or cost assumptions is permitted after this result; any new version is a new counted trial in the same family. The holdout is read once only after development passage.

## Why discretionary constructs are deferred

Fibonacci levels, fair-value gaps, order blocks, and liquidity sweeps have no single stable mapping from OHLC bars to an event, entry, stop, invalidation, and overlapping-event resolution. Choices such as swing-detection window, retracement bands, gap tolerance, block origin, confirmation, and what counts as a sweep can each change both event frequency and exposure. Selecting those definitions after viewing outcomes creates a large hidden multiple-testing family and makes causal timing ambiguous. They should be deferred until each has a versioned, deterministic, causal algorithm and unit-testable edge cases; only then may one be preregistered as a separate family.

## Methodology basis

- `quant-orchestrator`: routes this as alpha research plus validation/execution design.
- `tsay-analysis-financial-time-series`: daily-return timing and serial-dependence framing; no full-sample fitted feature is used.
- `quant-backtest-hygiene`: causal timing, execution lag, cost stress, capacity, DSR and sealed holdout discipline.
- `grinold-kahn-apm`: breakeven horizon and square-root-impact capacity logic.
- `chan-machine-trading`: systematic momentum and crypto execution context.
- `quant-verification`: formulas and units are stated explicitly for implementation and independent checking.
- `aster-research-loop`: one immutable preregistration, counted family trials, then one-shot holdout.
