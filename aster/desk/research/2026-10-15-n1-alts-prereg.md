# Preregistration — N1 panel alts (TA descriptive), 2026-10-15

Author: Forge (worker t_1a257193). Written **before** any result of this study was
computed, on the isolated branch `wt/aster-n1-alts`.

## Scope

Level **N1 only** (descriptive formalised technical analysis) on five secondary
panel assets: `BNBUSDT`, `XRPUSDT`, `SOLUSDT`, `LINKUSDT`, `DOGEUSDT`.

* Source: local R2 Binance **spot klines 1m**, aggregated to UTC daily bars.
  **Labelling convention is the canonical one**, `build_bars(..., label="close")`,
  i.e. the bucket indexed `t` covers `[t - 1d, t)` and its timestamp is the
  *close* of that day; the bar is only knowable at `t`. It matches the
  primitive that produced `data/ohlcv`, so panel and store share one labelling
  rule. It does **not** hold "the bar dated `t` holds exactly the UTC day `t`":
  the first draft of this prereg said `label="left", closed="left"` and that
  statement was wrong. See **Addendum B** at the end of this file — the
  correction was made before any result was computed and the original wording is
  quoted there rather than erased.
* Frozen minutes (`trades == 0`) and zero/negative-close minutes are dropped
  before aggregation, as in the BTC/ETH N1 study.
* **Exploration cutoff exclusive `2024-07-01T00:00:00Z`.** No bar, feature or
  statistic is computed on data at or after the cutoff; `r2_klines.read_local`
  refuses any local partition that crosses it, and the daily builder asserts
  `max(index) < CUTOFF`.
* Not in scope: N2, N3..N7, axes 7/8, section 6 (inter-asset), holdout,
  backtest, ledger. This study registers no hypothesis.

## Fixed signal family (declared a priori, before any p-value exists)

Horizians: forward **log-returns at h ∈ {1, 3, 7, 14} days**, measured from the
close of the event bar `t`.

Primary signals (24 → **96 primary cells per asset** = 24 × 4 horizons):

| Family | Signals | Definition |
|---|---|---|
| MA crossover | 4 | sign(MA(fast) − MA(slow)) for (20,100) and (5,20) |
| RSI(14) | 2 | `rsi14 < 30` (oversold), `rsi14 > 70` (overbought) |
| Bollinger(20, 2σ) | 2 | close below lower band / above upper band |
| Donchian(20) | 2 | close above prior 20d high / below prior 20d low |
| Stochastic %K(14) | 4 | `%K < 20`, `%K > 80`, sign(%K − %D(3)) = ±1 |
| Weekly pivots | 2 | close below S1, close above R1 |
| Fibonacci | 6 | close below / above 0.382, 0.5, 0.618 (252d swing, min 60) |
| Daily FVG (3-bar) | 2 | up-FVG entry, down-FVG entry |

Placebo-level signals (8 → 32 cells per asset), same machinery, **not** primary:
close below / above Fibonacci 0.55, 0.60, 0.65, 0.70 — same construction as the
real levels, so they measure how much of the Fibonacci effect is level-choice.

Total fixed grid: **32 signals × 4 horizons = 128 cells per asset**, of which
96 are primary. This grid size is a constant of the module and is asserted at
runtime: no cell may be dropped, added or re-selected after the fact.

Why the family is fixed now: any addition after seeing a p-value would
invalidate BH-FDR. Stochastic %K is added **because it is a standard member of
the common-TA catalogue**, not because of any observed result. Ichimoku is
excluded on purpose: axis 2 already closed it on this panel
(`research/notes/2026-10-14-axe-2.md`), and re-testing a closed axis inside a
second FDR family is not legitimate.

## Addendum A — inference correction (written before any result was computed)

The independent review of the draft rejected the inference method as
anti-conservative. Forward returns over `h` days **overlap**, so consecutive
events share `h-1` days of return and an IID t-test on the filtered event
series understates the standard error. The per-cell statistics are therefore
replaced as follows. No result existed when this was written.

1. **HAC t-test on the event-conditional score.** `one_sample_test` regresses
   the daily score `y_t = mask_t * fwd_h_t` (zero on non-event bars) on a
   constant and uses a Newey–West covariance with **bandwidth `max(h, 1)`**,
   i.e. at least `h-1`, which is the overlap length that must be covered.
   `mean_fwd` is the event mean; `t_stat`/`p_value` come from the HAC fit.
   The HAC estimator is verified in the test suite to be at least as
   conservative as the IID t-test on a positively autocorrelated series.
2. **Circular block bootstrap on the full calendar grid.** The interval is
   estimated by a circular moving-block bootstrap in which the **event mask and
   the return are resampled jointly** on the whole daily grid (block length
   `max(5, h)`, 5 000 draws, seed `20261015`). The filtered event series is
   never resampled on its own; the mask/return pairing is what breaks.
3. **FVG bounds corrected.** A 3-bar bullish gap opened by bar `t-1` is
   `[high_{t-2}, low_{t-1}]`; a bearish gap is `[low_{t-2}, high_{t-1}]`. The
   draft used `high/low` shifted by 2 for both bounds, which inverted the
   bullish interval and made a fill impossible. Detection, bounds and causal
   fill are now covered by a synthetic 3-bar gap fixture.
4. **RSI saturation.** `avg_loss == 0` → `RSI = 100`, `avg_gain == 0` →
   `RSI = 0` (a strictly monotone series saturates; it is never left at 50).
5. **Band features redefined so that the polarity pair is the exact complement.**
   `bb20_band` was `(close > lower) | (close < upper)`, which is the *union* of
   the two break signals, not their complement, and was never used by any
   signal. It is replaced by `bb20_inside_band = (close >= lower) & (close <= upper)`,
   and the equivalent inside/outside features for Donchian and weekly pivots.
   The preregistered signals themselves are unchanged.
6. **Placebos redefined to be falsifiable.** The draft drew a *random lag per
   bar*, which destroys serial clustering and is not the declared control. The
   three placebos are now exactly as declared above:
   * `placebo_shift_*`: the event mask circularly rolled by **one** seeded
     random offset (same frequency and serial clustering, alignment with
     returns destroyed) and tested against the **real** forward return;
   * `placebo_timing_*`: the same events measured on `fwd_h` shifted one day
     later (`log c_{t+h+1} - log c_{t+1}`);
   * `placebo_horizon_*`: the same events on the next strictly longer horizon,
     with `h = 14` falling back to `h = 7` as declared.

## Per-cell statistics (identical for primary and placebo-level cells)

1. `mean_fwd`, `t_stat`, `p_value`: HAC t-test (Newey–West, bandwidth
   `max(h, 1)`) of the event-conditional score against 0; NaN when `n < 30`.
2. `ci_lo`/`ci_hi`: circular **moving-block bootstrap** of the joint
   (mask, return) pair on the full daily grid, block length `max(5, h)`,
   5 000 draws, seed `20261015`.
3. **Inverse** cell: the exact complementary mask (same signal, opposite
   polarity) — `inverse_mean_fwd`, `inverse_t_stat`, `inverse_p_value`. This is
   the "does the opposite predict better" question (rejection / stop-hunt /
   false-breakout reading).
4. **Placebos**, all explicit, none optional:
   * `placebo_shift_*`: the same mask circularly rolled by a random
     offset (seeded), preserving the signal's frequency and serial structure
     while destroying alignment with returns;
   * `placebo_timing_*`: the same events measured on the forward return shifted
     one day later;
   * `placebo_horizon_*`: the same events on the next-longer horizon (h=14
     falls back to h=7, the weakest available control).

## Multiplicity

* BH-FDR is applied to the **fixed family of 128 cells of that asset**
  (`bh_q_asset`), and independently to the **union of the 96 primary cells of
  the five assets** (`bh_q_panel`, 480 tests). Both are computed on the same
  declared family — no subset, no re-selection, no post hoc choice of the
  family.
* A cell is **retained** only if all of:
  `bh_q_asset < 0.05` ∧ `bh_q_panel < 0.05` ∧ bootstrap CI excludes 0 ∧
  inverse does not dominate (`|inverse_mean| ≤ |mean_fwd|`) ∧ all three
  placebos non-significant (`p ≥ 0.05`).

## Interpretation rules fixed in advance

* A surviving cell is a **descriptive observation**, never a strategy. It does
  not authorise a ledger hypothesis, a backtest or a holdout read.
* Effect size is reported in the cell (mean forward log-return per event), not
  as a p-value alone.
* Assets are read independently; no cross-asset pooling of effect sizes.
* Regime breakdown (trend × volatility) is computed only for retained cells and
  reported as diagnostics, with a 30-observation floor per bucket.
* Non-causality is a hard stop: features must satisfy the truncation test
  (features computed on a truncated series equal those computed on the full
  series), asserted in the test suite.

## Reporting

Per asset: `research/assets/2026-10-15-<sym>-n1-ta.{md,csv}` plus
`…-regime.csv`. Study note with method, exact cell/test counts, placebos,
verdict and limits: `research/notes/2026-10-15-n1-alts.md`. `research/MAP.md`
and `research/BACKLOG.md` updated with the outcome.

## Addendum B — daily labelling and sampling, written 2026-10-15 before any result

This addendum is written **before any N1 result was computed**. No N1-ta panel
CSV, statistic, per-asset artifact or study note (`research/notes/2026-10-15-n1-alts.md`)
exists at the time of writing; the only files this study has added to the tree
are this prereg and the study code. Other 2026-10-15 artifacts in the tree
(`2026-10-15-ml-panel-diagnostics.*`, the `2026-10-15-axe-6.md` / `-phase-close.md`
notes) belong to other studies and are not inputs to N1-ta. The prior independent
review (`show t_1a257193`) blocked the panel on this exact point, so it is
recorded here rather than left implicit.

### What the first draft claimed, quoted verbatim

> * Source: local R2 Binance **spot klines 1m**, aggregated to UTC daily bars
>   (`label="left", closed="left"`), matching the implementation in
>   `src/aster/research/n1_ta_alts.py::build_daily`: the bar dated `t` holds
>   exactly the UTC day `t`. (Corrected from `closed="right"` in the first
>   draft, which would have shifted every daily bar by one day.)

That claim was **false**, and it was false in a way that would have made every
label look one day early. `label="left", closed="left"` gives the bucket `[t, t+1d)`
indexed by its *open* — a bar whose close and features are not knowable until
`t+1d`. Using it for forward returns would date a close to the morning of its
own day, i.e. a look-ahead of up to one full day.

### What is actually implemented

`aggregate_daily` delegates to the canonical production primitive
`aster.data.bars.build_bars(..., label="close")`, so the bucket indexed `t`
covers `[t - 1d, t)` and `t` is the **close** of that day. This is the same
primitive and the same rule as `r2_backtest_store.daily_from_minutes`, i.e.
the pipeline store and this panel share one labelling convention. The interval
included at the boundary is proven on a synthetic fixture in
`tests/test_daily_label_convention.py`: the bucket holds the previous day's
00:00 minute and excludes `t`'s own 00:00 minute.

### Sampling order, which is itself part of the protocol

1. `normalise_clock` first (as `daily_from_minutes` does), because repairing
   after the filter would key the filter on unrepaired timestamps.
2. Then the BTC/ETH N1 filter `(trades > 0) & (close > 0)`.
3. Only then does the frame reach `build_bars`, and the same admissible rows
   produce the per-bar `minutes` count, so count and content cannot disagree.

Because of step 2 the panel is **not** byte-identical to the materialised
`data/ohlcv` daily bars (that store is built from unfiltered minutes). What is
shared is the labelling convention and the minute source. No claim of byte
identity is made anywhere.

### Frozen-minute decision, explicit

`build_bars` keeps `trades == 0` minutes by default. The review flagged that
the prereg asserted frozen minutes were dropped while the code passed
`drop_frozen=False`. **Decision: drop them**, via the explicit N1 protocol
filter above — this matches the BTC/ETH N1 study rather than departing from
it. The effect is recorded here pre-result rather than justified after the
fact.
