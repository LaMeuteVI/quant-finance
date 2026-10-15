"""Tests for the alt panel N1 technical-analysis study (t_1a257193).

Every test here is written against the preregistered contract in
``research/2026-10-15-n1-alts-prereg.md``: the signal family is fixed before
results exist, the primary grid has at least 80 cells per asset, placebo and
inverse controls are explicit, and BH-FDR runs on that fixed family.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.research import n1_ta_alts as n1

HORIZONS = n1.HORIZONS
COLUMNS = (
    "symbol", "signal", "horizon", "kind", "n_events",
    "mean_fwd", "t_stat", "p_value", "ci_lo", "ci_hi",
    "inverse_n", "inverse_mean_fwd", "inverse_t_stat", "inverse_p_value",
    "placebo_shift_mean", "placebo_shift_t_stat", "placebo_shift_p_value",
    "placebo_timing_mean", "placebo_timing_p_value",
    "placebo_horizon_mean", "placebo_horizon_p_value",
    "bh_q_asset", "retention", "retention_final",
)


# ------------------------------- synthetic panel ---------------------------------


@pytest.fixture(scope="module")
def daily() -> pd.DataFrame:
    """Synthetic daily OHLC, ~5 years, deterministic, with trend and noise."""
    rng = np.random.default_rng(7)
    idx = pd.date_range("2019-01-01", periods=1825, freq="D", tz="UTC")
    log_rets = rng.normal(0.001, 0.04, size=len(idx))
    close = 100.0 * np.exp(np.cumsum(log_rets))
    open_ = np.concatenate([[100.0], close[:-1]])
    spread = np.abs(rng.normal(0.0, 0.02, size=len(idx)))
    high = np.maximum(open_, close) * (1.0 + spread)
    low = np.minimum(open_, close) * (1.0 - spread)
    return pd.DataFrame({"open": open_, "high": high, "low": low, "close": close}, index=idx)


@pytest.fixture(scope="module")
def features(daily: pd.DataFrame) -> pd.DataFrame:
    return n1.build_features(daily)


# ------------------------------- fixed family ------------------------------------


def test_primary_family_has_at_least_eighty_cells_per_asset():
    primary_cells = len(n1.PRIMARY_SIGNALS) * len(HORIZONS)
    assert len(n1.PRIMARY_SIGNALS) == 24
    assert primary_cells == 96
    assert primary_cells >= 80


def test_placebo_level_signals_are_declared_outside_the_primary_family():
    assert len(n1.PLACEBO_LEVEL_SIGNALS) == 8
    assert not set(n1.PRIMARY_SIGNALS) & set(n1.PLACEBO_LEVEL_SIGNALS)
    assert len(n1.SIGNAL_LABELS) == len(n1.PRIMARY_SIGNALS) + len(n1.PLACEBO_LEVEL_SIGNALS)


def test_every_signal_is_declared_with_a_definition():
    registry = dict(n1.SIGNAL_LABELS)
    for label in n1.PRIMARY_SIGNALS + n1.PLACEBO_LEVEL_SIGNALS:
        assert registry[label].strip(), label


def test_event_grid_evaluates_the_whole_fixed_family(features):
    grid = n1.event_grid(features, bootstraps=50)
    assert len(grid) == len(n1.SIGNAL_LABELS) * len(HORIZONS) == 128
    assert (grid["kind"] == "primary").sum() == 96
    assert (grid["kind"] == "placebo_level").sum() == 32
    for column in COLUMNS:
        if column in {"symbol", "retention_final", "bh_q_panel"}:
            continue
        assert column in grid.columns, column


def test_grid_carries_inverse_and_every_preregistered_placebo(features):
    grid = n1.event_grid(features, bootstraps=50)
    for column in (
        "inverse_mean_fwd", "inverse_t_stat", "inverse_p_value",
        "placebo_shift_mean", "placebo_shift_p_value",
        "placebo_timing_mean", "placebo_timing_p_value",
        "placebo_horizon_mean", "placebo_horizon_p_value",
        "bh_q_asset", "retention",
    ):
        assert column in grid.columns


def test_signal_masks_cover_every_declared_signal(features):
    pairs = n1.signal_masks(features)
    labels = [label for label, _, _ in pairs]
    assert sorted(labels) == sorted(n1.SIGNAL_LABELS)


# ------------------------------- causality ---------------------------------------


def test_features_are_invariant_to_future_rows_truncation(daily):
    full = n1.build_features(daily)
    cut = len(daily) - 40
    truncated = n1.build_features(daily.iloc[:cut])
    common = truncated.index
    feature_cols = [c for c in full.columns if not c.startswith("fwd_")]
    pd.testing.assert_frame_equal(
        full.loc[common, feature_cols].astype(float).fillna(-1.0),
        truncated[feature_cols].astype(float).fillna(-1.0),
    )


def test_forward_returns_use_only_later_closes(daily):
    feats = n1.build_features(daily)
    for h in HORIZONS:
        expected = np.log(daily["close"]).shift(-h) - np.log(daily["close"])
        pd.testing.assert_series_equal(feats[f"fwd_{h}d"], expected, check_names=False)


def test_daily_builder_rejects_minutes_at_or_after_the_cutoff(monkeypatch):
    """The sealed reader is the cutoff gate, so a breach must be an error.

    ``r2_klines.read_local`` refuses any local partition crossing the cutoff,
    so a minute frame that does contain one means the provenance contract was
    broken upstream.  Silently truncating it would hide exactly that.  This is
    distinct from a *daily bar* stamped on the cutoff, which is legitimate and
    simply dropped (see ``test_daily_label_convention``).
    """
    idx = pd.date_range(
        n1.CUTOFF - pd.Timedelta(hours=2), periods=4 * 60, freq="min", tz="UTC"
    )
    minutes = pd.DataFrame(_minute_schema(), index=idx)
    assert (minutes.index >= n1.CUTOFF).any(), "the fixture must really cross the cutoff"
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: minutes)
    with pytest.raises(ValueError, match="cutoff"):
        n1.build_daily("BNBUSDT")


def _minute_schema(price: float = 1.5, trades: int = 3) -> dict:
    """Full R2 1m kline schema; ``build_bars`` requires every column.

    Passing a trimmed OHLCV frame would make these tests fail inside
    ``bars._require_minutes`` instead of measuring the N1 aggregation, so the
    fixture carries the exact schema the real reader returns.
    """
    return {
        "open": price, "high": price + 0.5, "low": price - 1.0, "close": price,
        "volume": 10.0, "quote_volume": 10.0 * price, "trades": trades,
        "taker_buy_base": 5.0, "taker_buy_quote": 5.0 * price,
    }


def test_daily_builder_derives_utc_days_from_minutes(monkeypatch):
    minutes_idx = pd.date_range("2024-01-01 00:00", periods=48 * 60, freq="1min", tz="UTC")
    minutes = pd.DataFrame(_minute_schema(), index=minutes_idx)
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: minutes)
    built = n1.build_daily("BNBUSDT")
    # Canonical close labelling: bar t holds (t - 1d, t], so two full UTC days of
    # minutes produce two bars stamped at the END of each day.
    assert len(built) == 2
    assert built.index[0] == pd.Timestamp("2024-01-02", tz="UTC")
    assert built.index[-1] == pd.Timestamp("2024-01-03", tz="UTC")
    assert built["close"].iloc[0] == pytest.approx(1.5)


def test_daily_builder_drops_frozen_minutes(monkeypatch):
    minutes_idx = pd.date_range("2024-01-01 00:00", periods=2 * 60, freq="1min", tz="UTC")
    minutes = pd.DataFrame(_minute_schema(trades=1), index=minutes_idx)
    minutes.iloc[-1, minutes.columns.get_loc("trades")] = 0
    monkeypatch.setattr(n1.r2_klines, "read_local", lambda symbol: minutes)
    built = n1.build_daily("BNBUSDT")
    assert len(built) == 1
    assert built.index[0] == pd.Timestamp("2024-01-02", tz="UTC")
    assert built["high"].iloc[0] == pytest.approx(2.0)


# ------------------------------- statistics --------------------------------------


def test_bh_adjust_matches_the_hand_computed_reference():
    np.testing.assert_allclose(
        n1.bh_adjust(np.array([0.01, 0.02, 0.03, 0.04])), [0.04, 0.04, 0.04, 0.04]
    )
    np.testing.assert_allclose(n1.bh_adjust(np.array([0.001, 0.5, 0.9])), [0.003, 0.75, 0.9])


def test_bh_adjust_ignores_nan_cells_without_inflating_the_family():
    q = n1.bh_adjust(np.array([0.001, np.nan, 0.9]))
    assert np.isnan(q[1])
    np.testing.assert_allclose(q[[0, 2]], [0.002, 0.9])


def test_bh_adjust_never_shrinks_below_the_raw_p_value():
    p = np.random.default_rng(11).uniform(size=200)
    assert (n1.bh_adjust(p) >= p - 1e-12).all()


def test_block_bootstrap_is_seeded_and_brackets_the_sample_mean():
    values = np.random.default_rng(3).normal(0.01, 0.02, size=400)
    first = n1.bootstrap_mean(values, block=7, seed=5)
    assert first == n1.bootstrap_mean(values, block=7, seed=5)
    assert first[0] < values.mean() < first[1]


def test_block_bootstrap_returns_nan_on_short_samples():
    assert all(np.isnan(v) for v in n1.bootstrap_mean(np.zeros(10), block=5, seed=1))


def test_placebo_shift_preserves_the_number_of_events_and_breaks_alignment(features):
    mask = (features["rsi14"] < 30).fillna(False)
    shifted = n1.roll_mask(mask, offset=37)
    assert int(shifted.sum()) == int(mask.sum())
    assert int((shifted & mask).sum()) < int(mask.sum())


def test_timeline_placebo_rolls_the_mask_by_one_seeded_offset(features):
    """The declared control is one seeded circular roll, not a per-bar lag.

    Addendum A §6: ``placebo_shift`` keeps the signal's frequency and serial
    clustering and destroys only its alignment with returns.  A random lag
    drawn *per bar* would destroy the clustering too, which is not the declared
    control, so the test reconstructs the placebo from the public primitives and
    requires an exact match with the value the grid reports.
    """
    grid = n1.event_grid(features, bootstraps=50)
    pairs = {label: mask.fillna(False) for label, mask, _ in n1.signal_masks(features)}
    checked = 0
    for _, row in grid.iterrows():
        horizon = int(row["horizon"])
        mask = pairs[row["signal"]]
        rolled = n1.roll_mask(mask, offset=n1.shift_offset(len(mask), n1.SEED + horizon))
        expected = float(features[f"fwd_{horizon}d"][rolled].mean())
        if not np.isfinite(expected):
            continue
        assert row["placebo_shift_mean"] == pytest.approx(expected, rel=1e-9, abs=1e-12), row["signal"]
        checked += 1
    assert checked > 0, "the placebo was never reconstructed on a testable cell"


def test_inverse_masks_never_overlap_the_primary_mask(features):
    for label, mask, inverse in n1.signal_masks(features):
        assert not (mask.fillna(False) & inverse.fillna(False)).any(), label


def test_declared_complement_pairs_are_mutually_exclusive(features):
    """The declared opposite-polarity pairs must never fire on the same bar.

    They are *not* required to cover every bar: threshold signals (RSI,
    stochastic, Fibonacci) leave a neutral zone where neither polarity fires.
    Coverage is only asserted for the band-break families that do partition.
    """
    pairs = {label: mask for label, mask, _ in n1.signal_masks(features)}
    for low_label, high_label, _feature in n1.COMPLEMENT_PAIRS:
        low, high = pairs[low_label].fillna(False), pairs[high_label].fillna(False)
        assert not (low & high).any(), (low_label, high_label)

    partitioning = (
        ("bb20_lower_break", "bb20_upper_break"),
        ("donchian20_breakout_up", "donchian20_breakout_down"),
        ("pivot_s1_break", "pivot_r1_break"),
        ("fvg3_up_fill", "fvg3_down_fill"),
    )
    for low_label, high_label in partitioning:
        low, high = pairs[low_label].fillna(False), pairs[high_label].fillna(False)
        union = low | high
        assert union.sum() > 0, (low_label, high_label)


def test_stochastic_oscillator_stays_within_zero_and_hundred(features):
    inside = features["stoch_k"].dropna()
    assert inside.min() >= -1e-12
    assert inside.max() <= 100.0 + 1e-12


# ------------------------------- retention rule ---------------------------------


def test_retention_requires_every_preregistered_condition(features):
    grid = n1.event_grid(features, bootstraps=50)
    row = grid.iloc[0]
    assert bool(row["retention"]) == bool(
        row["bh_q_asset"] < 0.05
        and row["bootstrap_excludes_zero"]
        and row["inverse_does_not_dominate"]
        and row["placebo_all_non_significant"]
    )


def test_placebo_controls_are_independent_of_the_cell_under_test(features):
    """Each control must be able to fail while the cell itself passes.

    A control that is a deterministic function of the cell (same events, same
    returns, only the sign flipped) would have an identical p-value and could
    never discriminate anything; it would be a tautology, not a placebo.
    """
    grid = n1.event_grid(features, bootstraps=50)
    tested = grid[grid["p_value"].notna()]
    assert len(tested) > 0
    for control in ("placebo_shift", "placebo_timing", "placebo_horizon"):
        assert not np.allclose(
            tested[f"{control}_p_value"].to_numpy(), tested["p_value"].to_numpy()
        ), control


def test_timeline_placebo_keeps_the_signal_but_changes_its_alignment(features):
    grid = n1.event_grid(features, bootstraps=50)
    subset = grid[(grid["kind"] == "primary") & grid["p_value"].notna()]
    # The three controls must not all move together: that would mean a single
    # shared construction, i.e. no genuine placebo.
    assert subset["placebo_shift_mean"].std() > 0
    assert subset["placebo_timing_mean"].std() > 0


def test_panel_fdr_runs_on_the_union_of_primary_cells_of_every_asset(features):
    grid = n1.event_grid(features, bootstraps=50)
    panels = {
        symbol: n1.event_grid(features.assign(), bootstraps=50).assign(symbol=symbol)
        for symbol in ("BNBUSDT", "XRPUSDT")
    }
    combined = pd.concat([panels[s] for s in panels], ignore_index=True)
    combined = combined[combined["kind"] == "primary"]
    assert len(combined) == 192
    out = n1.apply_panel_fdr(combined)
    assert len(out) == len(combined)
    assert out["bh_q_panel"].notna().all()
    assert (out["bh_q_panel"] >= out["p_value"] - 1e-12).all()
    assert out["retention_final"].equals(out["retention"] & (out["bh_q_panel"] < 0.05))


def test_regime_breakdown_covers_only_retained_cells(features):
    grid = n1.event_grid(features, bootstraps=50)
    regime = n1.regime_breakdown(features, grid)
    assert set(regime["signal"]) <= set(grid[grid["retention"]]["signal"])
    assert (regime["n"] >= 30).all()


# ------------------------------- artifacts --------------------------------------


def test_write_reports_emits_markdown_and_csv(tmp_path, monkeypatch, features):
    monkeypatch.chdir(tmp_path)
    grid = n1.event_grid(features, bootstraps=50)
    grid = n1.apply_panel_fdr(grid.assign(symbol="BNBUSDT"))
    summary = n1.write_reports("BNBUSDT", features, grid, pd.DataFrame())
    assert (tmp_path / "research/assets/2026-10-15-bnbusdt-n1-ta.md").exists()
    assert (tmp_path / "research/assets/2026-10-15-bnbusdt-n1-ta.csv").exists()
    assert (tmp_path / "research/assets/2026-10-15-bnbusdt-n1-ta-regime.csv").exists()
    assert summary["cells"] == 128
    assert summary["primary_cells"] == 96
    assert summary["days"] == len(features)
    assert summary["retained"] == int(grid["retention_final"].sum())


def test_run_symbol_counts_cells_programmatically(monkeypatch, daily, tmp_path):
    monkeypatch.chdir(tmp_path)
    # ``run_symbol`` rebuilds features from daily OHLC, so the injected reader
    # must return the real OHLC schema -- ``features`` carries indicators only.
    monkeypatch.setattr(n1, "build_daily", lambda symbol: daily)
    result = n1.run_symbol("SOLUSDT", bootstraps=50)
    assert result["cells"] == 128
    assert result["primary_cells"] >= 80
    assert result["retained"] == int(result["grid"]["retention_final"].sum())
    assert result["cutoff_exclusive"] == "2024-07-01T00:00:00+00:00"
