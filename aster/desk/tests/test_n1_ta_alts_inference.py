"""RED-first tests for the review corrections of t_1a257193.

Each test here targets one defect raised by the independent review and is
written **before** the corresponding fix:

1. inference: overlapping forward returns must not be tested with an IID
   t-test, and the interval must not resample the filtered event series;
2. RSI saturation at ``avg_loss == 0`` / ``avg_gain == 0``;
3. fair-value-gap bounds and causal fill, on a known 3-bar gap;
4. band features that were tautological ORs of the two polarities;
5. placebos that preserve serial clustering and can actually fail.

Reference: ``research/2026-10-15-n1-alts-prereg.md``, Addendum A.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research import n1_ta_alts as n1


# --------------------------------------------------------------------------- #
# 1. Inference: HAC on the event-conditional score, joint calendar bootstrap
# --------------------------------------------------------------------------- #


def test_placebo_horizon_uses_next_longer_horizon_with_14d_fallback_to_7d():
    """The horizon placebo mapping is fixed and must not wrap to 1 day."""
    assert {h: n1._placebo_horizon(h) for h in n1.HORIZONS} == {
        1: 3, 3: 7, 7: 14, 14: 7,
    }


def _ma_fixture() -> pd.DataFrame:
    """Constant closes with independent, signed SMA spreads for both pairs."""
    idx = pd.date_range("2024-01-01", periods=6, freq="D", tz="UTC")
    frame = pd.DataFrame(index=idx)
    frame["close"] = 100.0
    for column in (
        "sma_5", "sma_10", "sma_20", "sma_30", "sma_50", "sma_100", "sma_200",
        "rsi14", "bb20_lower", "bb20_upper", "donchian_high",
        "donchian_low", "stoch_k", "stoch_d", "pivot_r1", "pivot_s1",
        "fvg3_up", "fvg3_down",
        *(f"fib_{ratio:03d}" for ratio in (382, 500, 618, 550, 600, 650, 700)),
    ):
        frame[column] = 0.0
    # The close is deliberately constant.  A and B are independent state inputs:
    # SMA20-SMA100 = [+1, 0, -1, NaN, +1, -1]
    # SMA5-SMA20   = [-1, +1, 0, +1, NaN, -1]
    frame["sma_20"] = 100.0
    frame["sma_100"] = 100.0 - np.array([1, 0, -1, np.nan, 1, -1], dtype=float)
    frame["sma_5"] = 100.0 + np.array([-1, 1, 0, 1, np.nan, -1], dtype=float)
    frame["sma_10"] = frame["sma_30"] = frame["sma_50"] = frame["sma_200"] = 100.0
    return frame


def test_ma_signals_are_preregistered_daily_sma_states_not_close_or_crossovers():
    """All defined SMA rows are states; equality is neutral and NaNs stay undefined."""
    features = _ma_fixture()
    pairs = {label: mask for label, mask, _ in n1.signal_masks(features)}
    expected = {
        "ma_20_100_fast_above_slow": pd.Series([True, False, False, pd.NA, True, False], index=features.index, dtype="boolean"),
        "ma_20_100_fast_below_slow": pd.Series([False, False, True, pd.NA, False, True], index=features.index, dtype="boolean"),
        "ma_5_20_fast_above_slow": pd.Series([False, True, False, True, pd.NA, False], index=features.index, dtype="boolean"),
        "ma_5_20_fast_below_slow": pd.Series([True, False, False, False, pd.NA, True], index=features.index, dtype="boolean"),
    }
    for label, state in expected.items():
        pd.testing.assert_series_equal(pairs[label], state, check_names=False)


def test_ma_signal_registry_has_only_the_four_preregistered_fast_slow_states():
    assert tuple(label for label in n1.SIGNAL_LABELS if label.startswith("ma_")) == (
        "ma_20_100_fast_above_slow", "ma_20_100_fast_below_slow",
        "ma_5_20_fast_above_slow", "ma_5_20_fast_below_slow",
    )


def test_hac_t_test_is_at_least_as_conservative_as_the_iid_t_test():
    """Overlapping/positively autocorrelated scores: HAC must widen the error.

    An IID t-test on the filtered event series is anti-conservative when the
    score is positively autocorrelated.  Newey-West with a bandwidth covering
    the autocorrelation must therefore give |t| no larger than the IID version.
    """
    rng = np.random.default_rng(101)
    n = 1200
    # AR(1) score with rho = 0.6: the regime an overlapping h-day return creates.
    shocks = rng.normal(size=n)
    score = np.zeros(n)
    for i in range(1, n):
        score[i] = 0.6 * score[i - 1] + shocks[i]
    score -= score.mean()

    hac = n1.hac_mean_test(score, bandwidth=6)
    iid_mean, iid_t, _iid_p = n1.one_sample_test(score)

    assert hac[0] == pytest.approx(iid_mean, rel=1e-9)
    assert abs(hac[1]) <= abs(iid_t) + 1e-9
    assert hac[2] >= _iid_p - 1e-9


def test_hac_t_test_matches_the_hand_computed_newey_west_variance():
    """The hand-rolled HAC must match an explicit Newey-West computation.

    Computed here from the definition (no extra dependency):
        S = g0 + 2 * sum_{l=1..L} w_l * g_l,  w_l = 1 - l/(L+1),
        g_l = (1/T) * sum_t (y_t - ybar)(y_{t-l} - ybar),
        se(ybar) = sqrt(S / T),  t = ybar / se.
    """
    rng = np.random.default_rng(202)
    n = 600
    score = rng.normal(0.01, 0.05, size=n)
    score[10:60] += 0.2  # a cluster of events

    bandwidth = 7
    got_mean, got_t, _got_p = n1.hac_mean_test(score, bandwidth=bandwidth)

    centered = score - score.mean()
    variance = float(np.dot(centered, centered) / n)
    for lag in range(1, bandwidth + 1):
        weight = 1.0 - lag / (bandwidth + 1.0)
        gamma = float(np.dot(centered[lag:], centered[:-lag]) / n)
        variance += 2.0 * weight * gamma
    se = float(np.sqrt(variance / n))
    assert got_mean == pytest.approx(float(score.mean()), rel=1e-12)
    assert got_t == pytest.approx(float(score.mean()) / se, rel=1e-6)


def test_hac_t_test_uses_bartlett_weights_on_a_fixed_vector():
    """Explicit Bartlett weights and variance for a fixed vector.

    No general ordering is claimed: a Newey-West t-stat is not monotone in the
    bandwidth for an arbitrary sample.  The Bartlett weight at lag ``l`` is
    ``1 - l / (bandwidth + 1)``, so bandwidth 1 keeps lag 1 with weight 1/2 and
    bandwidth 2 gives lag 1 a weight of 2/3 (the earlier draft inverted this
    ratio and expected 1/3).

    The vector is longer than ``MIN_EVENTS`` because the estimator declares
    NaN below it -- a fixed vector of 8 bars would have returned NaN and the
    test would have asserted nothing.
    """
    values = np.array([0.02, -0.01, 0.03, 0.05, -0.02, 0.04, 0.01, -0.03] * 5)
    assert len(values) >= n1.MIN_EVENTS
    centered = values - values.mean()

    def expected_t(bandwidth: int) -> float:
        variance = float(np.dot(centered, centered) / len(values))
        for lag in range(1, bandwidth + 1):
            weight = 1.0 - lag / (bandwidth + 1.0)
            gamma = float(np.dot(centered[lag:], centered[:-lag]) / len(values))
            variance += 2.0 * weight * gamma
        se = float(np.sqrt(variance / len(values)))
        return float(values.mean()) / se

    assert n1.bartlett_weight(0, 3) == pytest.approx(1.0)
    assert n1.bartlett_weight(1, 1) == pytest.approx(0.5)
    assert n1.bartlett_weight(1, 2) == pytest.approx(2.0 / 3.0)
    assert n1.bartlett_weight(2, 2) == pytest.approx(1.0 / 3.0)
    assert n1.bartlett_weight(4, 3) == 0.0   # beyond the band the weight is zero
    for bandwidth in (1, 2, 3):
        _mean, got_t, _p = n1.hac_mean_test(values, bandwidth=bandwidth)
        assert got_t == pytest.approx(expected_t(bandwidth), rel=1e-9)


def test_hac_t_test_returns_nan_when_there_are_too_few_events():
    score = np.array([0.1, 0.2, -0.05, 0.3])
    assert all(np.isnan(v) for v in n1.hac_mean_test(score, bandwidth=3))


def test_cell_statistics_are_undefined_below_the_preregistered_event_floor():
    """A 29-event cell stays in the fixed family but receives no inference."""
    mask = np.zeros(60, dtype=bool)
    mask[: n1.MIN_EVENTS - 1] = True
    returns = np.linspace(-0.03, 0.03, len(mask))

    stats = n1._score_stats(mask, returns, horizon=1, seed=n1.SEED, draws=50)

    assert all(np.isnan(value) for value in stats)


def test_hac_bandwidth_is_at_least_the_overlap_length():
    """The preregistered bandwidth is ``max(h, 1)``, i.e. >= h-1 lag."""
    for horizon in n1.HORIZONS:
        assert n1.hac_bandwidth(horizon) >= max(horizon - 1, 1)


def test_calendar_bootstrap_resamples_the_mask_and_the_return_jointly():
    """The pairing must break, not only the event series.

    Bootstrapping the filtered events would keep every (mask, return) pair and
    could not widen the interval at all under a clustered signal.
    """
    rng = np.random.default_rng(5)
    n = 900
    returns = rng.normal(0.0, 0.02, size=n)
    # Clustered events: 10 consecutive days, then 40 quiet days.
    mask = np.zeros(n, dtype=bool)
    for start in range(0, n - 60, 50):
        mask[start:start + 10] = True
    returns[mask] += 0.05

    joint = n1.calendar_block_bootstrap(
        mask, returns, block=10, seed=3, draws=800
    )
    filtered_only = n1.bootstrap_mean(
        returns[mask], block=10, seed=3, draws=800
    )

    joint_width = joint[1] - joint[0]
    filtered_width = filtered_only[1] - filtered_only[0]
    assert joint_width > filtered_width, (joint, filtered_only)
    assert joint[0] <= returns[mask].mean() <= joint[1]


def test_calendar_bootstrap_is_seeded_and_returns_nan_when_too_short():
    """Seeded on a testable draw, NaN on a series too short to resample.

    ``nan == nan`` is False, so the reproducibility of the NaN branch is
    asserted with ``np.isnan`` and not by comparing the tuples.
    """
    rng = np.random.default_rng(5)
    mask = np.zeros(400, dtype=bool)
    mask[::4] = True                      # 100 events >= MIN_EVENTS
    returns = rng.normal(size=400)
    first = n1.calendar_block_bootstrap(mask, returns, block=10, seed=8, draws=200)
    again = n1.calendar_block_bootstrap(mask, returns, block=10, seed=8, draws=200)
    assert first == again
    assert all(np.isfinite(v) for v in first), "the testable branch must be exercised"

    too_short = n1.calendar_block_bootstrap(
        np.zeros(10, dtype=bool), np.zeros(10), block=5, seed=1, draws=50
    )
    assert all(np.isnan(v) for v in too_short)


# --------------------------------------------------------------------------- #
# 2. RSI saturation
# --------------------------------------------------------------------------- #


def test_rsi_saturates_at_one_hundred_when_there_is_no_loss():
    idx = pd.date_range("2024-01-01", periods=40, freq="D", tz="UTC")
    close = pd.Series(np.arange(1.0, 41.0), index=idx)
    out = n1._rsi(close, 14).dropna()
    assert len(out) > 0, "the fixture must actually produce RSI values"
    assert (out == 100.0).all()
    assert not out.isna().any()


def test_rsi_saturates_at_zero_when_there_is_no_gain():
    idx = pd.date_range("2024-01-01", periods=40, freq="D", tz="UTC")
    close = pd.Series(np.arange(41.0, 1.0, -1.0), index=idx)
    out = n1._rsi(close, 14).dropna()
    assert len(out) > 0, "the fixture must actually produce RSI values"
    assert (out == 0.0).all()


def test_rsi_never_leaves_the_zero_hundred_range():
    rng = np.random.default_rng(17)
    idx = pd.date_range("2024-01-01", periods=800, freq="D", tz="UTC")
    close = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0, 0.03, 800))), index=idx)
    out = n1._rsi(close, 14).dropna()
    assert out.between(0.0, 100.0).all()


# --------------------------------------------------------------------------- #
# 3. Fair value gaps: known 3-bar gap, correct bounds, causal fill
# --------------------------------------------------------------------------- #


def _bars(high, low, close) -> pd.DataFrame:
    idx = pd.date_range("2024-01-01", periods=len(high), freq="D", tz="UTC")
    close = np.asarray(close, dtype=float)
    return pd.DataFrame(
        {"open": close, "high": np.asarray(high, dtype=float),
         "low": np.asarray(low, dtype=float), "close": close},
        index=idx,
    )


# A 3-bar gap *formed at bar f* uses bars f-2 and f:
#   bullish: low[f]  > high[f-2], gap = (high[f-2], low[f])
#   bearish: high[f] < low[f-2],  gap = (low[f-2], high[f])
# The signal fires on a bar t >= f + 3 whose close trades back inside the gap.
_BULLISH = _bars(
    high=[100.0, 101.0, 102.0, 110.0, 111.0, 112.0, 110.0],
    low=[99.0, 100.0, 101.0, 108.0, 107.0, 106.0, 105.0],
    close=[99.5, 100.5, 101.5, 109.0, 110.0, 111.0, 106.5],
)   # gap formed at f=3 -> (101.0, 108.0); bar 6 closes 106.5, inside.
_BEARISH = _bars(
    high=[100.0, 101.0, 102.0, 95.0, 94.0, 96.0, 99.0],
    low=[99.0, 100.0, 101.0, 92.0, 90.0, 91.0, 94.0],
    close=[99.5, 100.5, 101.5, 93.5, 92.0, 95.0, 97.5],
)   # gap formed at f=3 -> (95.0, 100.0); bar 6 closes 97.5, inside.


def test_bullish_gap_is_detected_with_high_on_the_older_bar_and_low_on_the_opening_bar():
    feats = n1.build_features(_BULLISH)
    assert bool(feats["fvg3_up"].iloc[6]), feats[["fvg3_up", "fvg3_down"]].iloc[6]
    assert not bool(feats["fvg3_down"].iloc[6])
    low_bound, high_bound = n1.fvg3_bounds(_BULLISH, 6)
    assert low_bound == pytest.approx(101.0)   # high[f-2] = high of bar 1
    assert high_bound == pytest.approx(108.0)  # low[f]   = low of bar 3
    assert low_bound < high_bound


def test_bearish_gap_is_detected_with_low_on_the_older_bar_and_high_on_the_opening_bar():
    feats = n1.build_features(_BEARISH)
    assert bool(feats["fvg3_down"].iloc[6]), feats[["fvg3_up", "fvg3_down"]].iloc[6]
    assert not bool(feats["fvg3_up"].iloc[6])
    low_bound, high_bound = n1.fvg3_bounds(_BEARISH, 6, direction="down")
    assert low_bound == pytest.approx(100.0)   # low[f-2] = low of bar 1
    assert high_bound == pytest.approx(95.0)   # high[f]  = high of bar 3
    assert low_bound > high_bound  # the empty interval lies below price


def test_gap_bounds_are_never_derived_from_the_same_bar():
    """The draft took both bounds from ``shift(2)``, inverting the interval."""
    for fixture, direction in ((_BULLISH, "up"), (_BEARISH, "down")):
        low_bound, high_bound = n1.fvg3_bounds(fixture, 6, direction=direction)
        assert low_bound != high_bound, fixture
        assert not np.isnan(low_bound) and not np.isnan(high_bound)


def test_gap_fill_needs_the_close_inside_the_gap():
    bullish = _BULLISH.copy()
    bullish.iloc[6, bullish.columns.get_loc("close")] = 95.0
    assert not bool(n1.build_features(bullish)["fvg3_up"].iloc[6])

    bearish = _BEARISH.copy()
    bearish.iloc[6, bearish.columns.get_loc("close")] = 80.0
    assert not bool(n1.build_features(bearish)["fvg3_down"].iloc[6])


def test_gap_fill_is_causal_and_never_fires_before_the_gap_exists():
    """Bars before the gap is formed cannot report a fill of that gap."""
    feats = n1.build_features(_BULLISH)
    assert not feats["fvg3_up"].iloc[:5].any()
    # Truncating the panel must not change any earlier row.
    truncated = n1.build_features(_BULLISH.iloc[:7])
    pd.testing.assert_series_equal(
        feats["fvg3_up"].iloc[:7], truncated["fvg3_up"], check_names=False
    )


def test_gap_formed_but_not_yet_filled_is_not_an_event():
    """A gap still wide open on the event bar must not be counted as filled."""
    open_gap = _bars(
        high=[100.0, 101.0, 102.0, 110.0, 111.0, 112.0, 113.0],
        low=[99.0, 100.0, 101.0, 108.0, 109.0, 110.0, 111.0],
        close=[99.5, 100.5, 101.5, 109.0, 110.0, 111.0, 112.0],
    )
    assert not bool(n1.build_features(open_gap)["fvg3_up"].iloc[6])


# --------------------------------------------------------------------------- #
# 4. Band features must be a real rule, not the union of the two polarities
# --------------------------------------------------------------------------- #


def _flat_panel(n: int = 400) -> pd.DataFrame:
    idx = pd.date_range("2023-01-01", periods=n, freq="D", tz="UTC")
    rng = np.random.default_rng(31)
    close = pd.Series(100.0 * np.exp(np.cumsum(rng.normal(0.001, 0.02, n))), index=idx)
    return pd.DataFrame(
        {"open": close.shift(1).bfill(), "high": close * 1.01,
         "low": close * 0.99, "close": close},
        index=idx,
    )


def test_bb20_band_is_the_complement_of_the_two_breaks_not_their_union():
    """On every bar where the bands are defined, inside == ~(lower | upper).

    Warm-up bars have undefined bands; they are excluded on both sides rather
    than silently counted as "outside", which would hide a real mismatch.
    """
    feats = n1.build_features(_flat_panel())
    pairs = {label: mask for label, mask, _ in n1.signal_masks(feats)}
    defined = feats["bb20_lower"].notna() & feats["bb20_upper"].notna()
    inside = feats["bb20_inside_band"].loc[defined].astype(bool)
    lower = pairs["bb20_lower_break"].loc[defined].fillna(False).astype(bool)
    upper = pairs["bb20_upper_break"].loc[defined].fillna(False).astype(bool)
    assert len(inside) > 200
    pd.testing.assert_series_equal(inside, ~(lower | upper), check_names=False)


def test_donchian_and_pivot_bands_are_inside_flags():
    """The tautological union columns are gone; only inside flags remain."""
    feats = n1.build_features(_flat_panel())
    for tautological in ("bb20_band", "donchian20", "pivot_band"):
        assert tautological not in feats.columns, tautological
    for inside in ("bb20_inside_band", "donchian20_inside", "pivot_inside_band"):
        assert inside in feats.columns, inside
        # An inside flag must be False on a real fraction of bars, otherwise it
        # carries no information at all.
        assert 0.0 < float(feats[inside].fillna(False).mean()) < 1.0, inside


# --------------------------------------------------------------------------- #
# 5. Placebos: falsifiable, clustering-preserving
# --------------------------------------------------------------------------- #


def test_shift_placebo_keeps_the_event_count_and_the_run_structure():
    """A rolled mask keeps both the number of events and their clustering."""
    idx = pd.date_range("2024-01-01", periods=400, freq="D", tz="UTC")
    mask = pd.Series(False, index=idx)
    mask[100:110] = True
    mask[300:305] = True
    rolled = n1.roll_mask(mask, offset=173)
    assert int(rolled.sum()) == int(mask.sum())
    # Run lengths are preserved exactly: circular roll moves, it does not shuffle.
    assert _max_run(rolled) == _max_run(mask)
    assert _max_run(rolled.fillna(False)) == _max_run(mask)


def _max_run(mask: pd.Series) -> int:
    values = mask.fillna(False).to_numpy()
    best = run = 0
    for value in values:
        run = run + 1 if value else 0
        best = max(best, run)
    return best


def test_shift_placebo_offset_is_seeded_uniform_on_the_forward_support():
    """One draw on ``[1, n-1]``, reproducible, never the degenerate 0.

    A single-sample "two seeds give two offsets" assertion is a coin flip: with
    ``n=11`` there are only ten eligible offsets, so a collision is a 10% flake.
    The property that actually matters is checked instead -- the offset is
    strictly forward, it is a function of the seed alone, and distinct seeds
    cover more than one offset over a long panel.
    """
    n = 500
    for seed in (n1.SEED, n1.SEED + 1, 7):
        offset = n1.shift_offset(n, seed)
        assert 1 <= offset <= n - 1, "0 would leave the placebo perfectly aligned"
        assert offset == n1.shift_offset(n, seed), "the draw must be reproducible"
    assert len({n1.shift_offset(n, seed) for seed in range(200)}) > 1

    # A panel too short to shift has no offset rather than a degenerate one.
    assert n1.shift_offset(1, n1.SEED) == 0


def test_timing_placebo_is_the_return_one_day_later():
    """``fwd_h`` shifted one day later == c_{t+h+1} - c_{t+1}."""
    idx = pd.date_range("2024-01-01", periods=50, freq="D", tz="UTC")
    log_close = pd.Series(np.log(np.arange(50.0) + 100.0), index=idx)
    horizon = 3
    late = n1.timing_placebo_return(log_close, horizon)
    expected = log_close.shift(-(horizon + 1)) - log_close.shift(-horizon)
    pd.testing.assert_series_equal(late, expected, check_names=False)


def test_placebo_p_values_are_computed_with_the_same_hac_inference():
    """A control that used a weaker test than the cell would be unfair.

    The controls must be scored with the same HAC machinery, otherwise "the
    placebo is non-significant" could simply be an artefact of a loose test.
    """
    grid = n1.event_grid(n1.build_features(_flat_panel()), bootstraps=50)
    tested = grid[grid["p_value"].notna()]
    assert len(tested) > 0
    for control in ("placebo_shift", "placebo_timing", "placebo_horizon"):
        assert tested[f"{control}_p_value"].notna().any(), control


def test_event_grid_uses_hac_and_calendar_bootstrap_not_the_iid_path(monkeypatch):
    """Integration: the grid must route every statistic through the new code.

    An IID ``one_sample_test`` and a filtered-series ``bootstrap_mean`` would
    silently give the old, anti-conservative answers; the counters below make
    that a test failure rather than a comment.
    """
    calls = {"hac": 0, "calendar": 0, "iid": 0, "filtered_bootstrap": 0}
    real_hac = n1.hac_mean_test
    real_calendar = n1.calendar_block_bootstrap

    def counting_hac(values, bandwidth, **kwargs):
        calls["hac"] += 1
        return real_hac(values, bandwidth=bandwidth, **kwargs)

    def counting_calendar(mask, returns, **kwargs):
        calls["calendar"] += 1
        return real_calendar(mask, returns, **kwargs)

    def forbidden_iid(*args, **kwargs):
        calls["iid"] += 1
        raise AssertionError("event_grid must not use the IID t-test")

    def forbidden_bootstrap(*args, **kwargs):
        calls["filtered_bootstrap"] += 1
        raise AssertionError("event_grid must not bootstrap the filtered series")

    monkeypatch.setattr(n1, "hac_mean_test", counting_hac)
    monkeypatch.setattr(n1, "calendar_block_bootstrap", counting_calendar)
    monkeypatch.setattr(n1, "one_sample_test", forbidden_iid)
    monkeypatch.setattr(n1, "bootstrap_mean", forbidden_bootstrap)

    grid = n1.event_grid(n1.build_features(_flat_panel()), bootstraps=50)

    assert len(grid) == 128
    assert calls["iid"] == 0 and calls["filtered_bootstrap"] == 0
    # Each eligible cell and eligible control uses HAC; below-floor cells are
    # retained in the declared family but deliberately have no inference.
    eligible = grid["n_events"] >= n1.MIN_EVENTS
    assert calls["hac"] >= int(eligible.sum()) * 5
    # The bootstrap interval is a property of an eligible cell under test only:
    # the inverse and the three placebos report means and p-values, never a CI.
    assert calls["calendar"] == int(eligible.sum())
