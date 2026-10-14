"""Tests des barres temporelles et d'information (plan de recherche §4.2).

Chaque règle est prouvée par un cas qui la déclenche. Les valeurs de référence
sont recalculées à la main dans le commentaire : ce sont les chiffres publiés
que ces tests figent, pas des nombres sortis de l'implémentation.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.data.bars import (
    TIMEFRAMES,
    build_bars,
    build_information_bars,
    bars_frame_report,
    normalise_clock,
)

_COLUMNS = ["open", "high", "low", "close", "volume", "quote_volume",
            "trades", "taker_buy_base", "taker_buy_quote"]


def _minutes(n: int = 120, start: str = "2024-06-03 00:00", seed: int = 0) -> pd.DataFrame:
    """Minutes synthétiques pré-cutoff, prix et flux croissants."""
    index = pd.date_range(start, periods=n, freq="1min", tz="UTC")
    rng = np.random.default_rng(seed)
    base = 100.0 + np.arange(n) * 0.01
    return pd.DataFrame(
        {
            "open": base,
            "high": base + 0.05,
            "low": base - 0.05,
            "close": base + 0.01,
            "volume": rng.uniform(1.0, 5.0, n),
            "quote_volume": rng.uniform(100.0, 500.0, n),
            "trades": rng.integers(5, 50, n).astype(float),
            "taker_buy_base": rng.uniform(0.4, 0.6, n) * rng.uniform(1.0, 5.0, n),
            "taker_buy_quote": rng.uniform(0.4, 0.6, n) * rng.uniform(100.0, 500.0, n),
        },
        index=index,
    )


# --- réparation d'horloge ----------------------------------------------------

def test_normalise_clock_is_a_no_op_on_a_clean_frame():
    frame = _minutes(10)
    out, repair = normalise_clock(frame)
    assert repair.changed is False
    assert repair.off_grid_before == 0
    assert out is frame, "un frame propre ne doit pas etre copie"
    assert repair.rows_before == repair.rows_after == 10


def test_normalise_clock_snaps_a_constant_source_offset():
    # Defaut Binance observe : dec-2017, decalage constant de +20.799 ms.
    index = pd.date_range("2017-12-04 06:00:20.799000", periods=5, freq="1min", tz="UTC")
    frame = _minutes(5).set_axis(index)
    out, repair = normalise_clock(frame)
    assert repair.changed is True
    assert repair.off_grid_before == 5
    assert repair.off_grid_after == 0
    assert repair.rows_before == repair.rows_after == 5
    assert repair.dropped_duplicates == 0
    # pandas affiche 20.799 ms sous la forme "0 days 00:00:20.799000".
    assert repair.offsets == ("0 days 00:00:20.799000",)
    assert (out.index.floor("min") == out.index).all()
    # Reference : 06:00:20.799 -> 06:00, 06:01:20.799 -> 06:01 ...
    assert out.index[0] == pd.Timestamp("2017-12-04 06:00", tz="UTC")
    assert out.index[-1] == pd.Timestamp("2017-12-04 06:04", tz="UTC")


def test_normalise_clock_floors_rather_than_rounds_into_the_future():
    # 09:59:14.787 appartient au seau 09:59. Un round le pushingait a 10:00 et
    # creerait une observation qui n'existait pas encore.
    index = pd.DatetimeIndex([pd.Timestamp("2024-06-03 09:59:14.787000", tz="UTC")])
    frame = _minutes(1).set_axis(index)
    out, _ = normalise_clock(frame)
    assert out.index[0] == pd.Timestamp("2024-06-03 09:59", tz="UTC")


def test_normalise_clock_keeps_the_last_print_and_reports_the_drop():
    index = pd.DatetimeIndex([
        pd.Timestamp("2024-06-03 00:00:30", tz="UTC"),
        pd.Timestamp("2024-06-03 00:01:00", tz="UTC"),
        pd.Timestamp("2024-06-03 00:01:30", tz="UTC"),
    ])
    frame = _minutes(3).set_axis(index)
    frame.iloc[2, frame.columns.get_loc("close")] = 999.0  # l'impression corrigee
    out, repair = normalise_clock(frame)
    assert repair.dropped_duplicates == 1
    assert repair.rows_after == 2
    stamped = out.loc[pd.Timestamp("2024-06-03 00:01", tz="UTC")]
    assert stamped["close"] == 999.0, "la derniere impression doit gagner"


def test_normalise_clock_rejects_a_naive_index():
    frame = _minutes(3).set_axis(pd.date_range("2024-06-03", periods=3, freq="1min"))
    with pytest.raises(ValueError, match="tz-aware"):
        normalise_clock(frame)


def test_normalise_clock_handles_an_empty_frame():
    empty = pd.DataFrame(columns=_COLUMNS, index=pd.DatetimeIndex([], tz="UTC"))
    out, repair = normalise_clock(empty)
    assert len(out) == 0
    assert repair.rows_before == 0


# --- construction des barres -------------------------------------------------

def test_bars_are_labelled_at_the_close():
    frame = _minutes(120)
    bars = build_bars(frame, "1h")
    # 120 minutes a partir de 00:00 -> deux seaux (00:00,01:00] et (01:00,02:00].
    assert len(bars) == 2
    assert bars.index[0] == pd.Timestamp("2024-06-03 01:00", tz="UTC")
    assert bars.index.name == "bar_close_utc"
    assert bars.attrs["timeframe"] == "1h"


def test_a_close_labelled_bar_contains_only_the_past():
    # Reference : le seau (00:00,01:00] contient les minutes 00:00..00:59.
    # Aucune minute >= 01:00 ne doit y entrer.
    frame = _minutes(180)
    bars = build_bars(frame, "1h")
    first = bars.iloc[0]
    minute_rows = frame.loc[:pd.Timestamp("2024-06-03 00:59", tz="UTC")]
    assert first["volume"] == pytest.approx(minute_rows["volume"].sum())
    assert first["trades"] == minute_rows["trades"].sum()
    assert first["open"] == minute_rows["open"].iloc[0]
    assert first["close"] == minute_rows["close"].iloc[-1]
    assert first["high"] == minute_rows["high"].max()
    assert first["low"] == minute_rows["low"].min()


def test_ohlc_aggregation_is_internally_consistent():
    bars = build_bars(_minutes(240), "15m")
    assert len(bars) == 16
    assert (bars["high"] >= bars["low"]).all()
    assert (bars["high"] >= bars["close"]).all()
    assert (bars["low"] <= bars["close"]).all()
    assert (bars["volume"] > 0).all()


@pytest.mark.parametrize("timeframe", sorted(TIMEFRAMES))
def test_every_declared_timeframe_aggregates_without_leakage(timeframe):
    frame = _minutes(24 * 60 * 3, start="2024-06-01 00:00")
    bars = build_bars(frame, timeframe)
    # Reference : la somme des volumes doit etre exactement celui des minutes.
    assert bars["volume"].sum() == pytest.approx(frame["volume"].sum())
    assert bars["trades"].sum() == pytest.approx(frame["trades"].sum())
    assert len(bars) > 0


def test_aggregate_volume_is_conserved_across_timeframes():
    frame = _minutes(600)
    for timeframe in ("5m", "15m", "1h", "4h"):
        bars = build_bars(frame, timeframe)
        assert bars["volume"].sum() == pytest.approx(frame["volume"].sum()), timeframe


def test_an_empty_interval_is_dropped_not_filled():
    index = pd.DatetimeIndex([
        pd.Timestamp("2024-06-03 00:00", tz="UTC"),
        pd.Timestamp("2024-06-03 00:01", tz="UTC"),
        # trou de 01:00 a 04:00 : trois seaux d'une heure entierement vides
        pd.Timestamp("2024-06-03 04:00", tz="UTC"),
    ])
    frame = _minutes(3).set_axis(index)
    bars = build_bars(frame, "1h")
    # Reference : seaux [00:00,01:00) labelle 01:00, puis [04:00,05:00) labelle
    # 05:00. Les labels 02:00, 03:00 et 04:00 n'ont aucune donnee : ils ne
    # doivent pas devenir un prix plat reporte.
    assert list(bars.index) == [
        pd.Timestamp("2024-06-03 01:00", tz="UTC"),
        pd.Timestamp("2024-06-03 05:00", tz="UTC"),
    ]
    assert bars["close"].notna().all()


def test_frozen_minutes_are_kept_by_default_and_counted():
    frame = _minutes(120)
    frame.iloc[0:6, frame.columns.get_loc("trades")] = 0.0
    bars = build_bars(frame, "1h")
    assert len(bars) == 2, "120 minutes -> deux seaux d'une heure"
    assert bars.iloc[0]["volume"].sum() > 0, "les minutes gelees restent dans l'echantillon"
    assert bars.iloc[0]["frozen_share"] == pytest.approx(6 / 60)
    assert bars.iloc[1]["frozen_share"] == pytest.approx(0.0)


def test_drop_frozen_is_opt_in_and_removes_them():
    frame = _minutes(120)
    frame.iloc[0:6, frame.columns.get_loc("trades")] = 0.0
    bars = build_bars(frame, "1h", drop_frozen=True)
    assert bars.iloc[0]["frozen_share"] == pytest.approx(0.0)
    assert bars.iloc[0]["trades"] == frame["trades"].iloc[6:60].sum()


def test_drop_frozen_on_an_all_frozen_frame_is_an_error_not_an_empty_frame():
    frame = _minutes(10)
    frame["trades"] = 0.0
    with pytest.raises(ValueError, match="empty"):
        build_bars(frame, "1h", drop_frozen=True)


def test_missing_columns_are_named_in_the_error():
    frame = _minutes(10).drop(columns=["taker_buy_base"])
    with pytest.raises(ValueError, match="taker_buy_base"):
        build_bars(frame, "1h")


def test_unsupported_timeframe_is_rejected():
    with pytest.raises(ValueError, match="unsupported timeframe"):
        build_bars(_minutes(10), "3m")


def test_plot_label_is_offered_but_marked_as_open():
    bars = build_bars(_minutes(120), "1h", label="left")
    assert bars.index[0] == pd.Timestamp("2024-06-03 00:00", tz="UTC")
    assert bars.index.name == "bar_open_utc"
    with pytest.raises(ValueError, match="label"):
        build_bars(_minutes(10), "1h", label="middle")


# --- barres d'information ----------------------------------------------------

def test_imbalance_reference_value_on_a_fully_one_sided_bar():
    # Chaque minute : 100 unites tradees, 90 achetees agressivement
    # -> ratio 0.9 -> imbalance +0.8. Sur 60 minutes le seau cumule
    # 60*900 = 54000 $ de taker buy contre 60*1000 = 60000 $ de volume quote,
    # donc signed_dollar = 2*54000 - 60000 = 48000.
    frame = _minutes(60)
    frame["volume"] = 100.0
    frame["taker_buy_base"] = 90.0
    frame["quote_volume"] = 1000.0
    frame["taker_buy_quote"] = 900.0
    bars = build_information_bars(frame, "1h")
    assert bars.iloc[0]["taker_buy_ratio"] == pytest.approx(0.9)
    assert bars.iloc[0]["imbalance"] == pytest.approx(0.8)
    assert bars.iloc[0]["signed_dollar"] == pytest.approx(48_000.0)


def test_imbalance_is_zero_on_a_balanced_bar():
    frame = _minutes(60)
    frame["volume"] = 10.0
    frame["taker_buy_base"] = 5.0
    frame["quote_volume"] = 100.0
    frame["taker_buy_quote"] = 50.0
    bars = build_information_bars(frame, "1h")
    assert bars.iloc[0]["imbalance"] == pytest.approx(0.0)


def test_imbalance_is_bounded_between_minus_one_and_one():
    rng = np.random.default_rng(7)
    frame = _minutes(500)
    frame["volume"] = rng.uniform(0.1, 10.0, len(frame))
    frame["taker_buy_base"] = frame["volume"] * rng.uniform(0.0, 1.0, len(frame))
    bars = build_information_bars(frame, "5m")
    valid = bars["imbalance"].dropna()
    assert valid.between(-1.0, 1.0).all()
    assert valid.abs().max() > 0.5, "un fluxMelange ne doit pas produire un desequilibre plat"


def test_a_zero_volume_bar_has_unknown_imbalance_not_zero():
    frame = _minutes(60)
    frame["volume"] = 0.0
    frame["taker_buy_base"] = 0.0
    bars = build_information_bars(frame, "1h")
    assert bars.iloc[0]["imbalance"] is np.nan or pd.isna(bars.iloc[0]["imbalance"])
    assert pd.isna(bars.iloc[0]["taker_buy_ratio"])


def test_information_bars_preserve_the_temporal_invariants():
    frame = _minutes(300)
    bars = build_information_bars(frame, "15m")
    assert (bars["high"] >= bars["low"]).all()
    assert bars["volume"].sum() == pytest.approx(frame["volume"].sum())
    assert bars["dollar_volume"].sum() == pytest.approx(frame["quote_volume"].sum())
    assert bars.index.name == "bar_close_utc"


def test_imbalance_survives_resampling_as_a_volume_weighted_mean():
    frame = _minutes(60)
    frame["volume"] = 1.0
    frame["taker_buy_base"] = 0.6
    bars = build_information_bars(frame, "1h")
    # Toutes les minutes portent le meme volume : le desequilibre du seau
    # vaut 2 * 0.6 - 1 = 0.2, identique a celui de chaque minute.
    assert bars.iloc[0]["imbalance"] == pytest.approx(0.2)


# --- rapport -----------------------------------------------------------------

def test_bars_frame_report_is_json_ready():
    report = bars_frame_report("BTCUSDT", _minutes(240), "1h")
    assert report["symbol"] == "BTCUSDT"
    assert report["bars"] == 4
    assert report["close_labeled"] is True
    assert report["index"] == "bar_close_utc"
    assert report["start"].endswith("+00:00")
    assert isinstance(report["columns"], list)
    assert -1.0 <= report["mean_imbalance"] <= 1.0


def test_build_bars_does_not_mutate_the_input():
    frame = _minutes(60)
    before = frame.copy()
    build_bars(frame, "1h", drop_frozen=True)
    pd.testing.assert_frame_equal(frame, before)