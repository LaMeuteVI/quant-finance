"""Tests du contrôle qualité minute : données synthétiques, aucun accès réseau.

Chaque règle doit être prouvée par un cas qui la déclenche : un test qui passe
sans jamais faire échouer la règle correspondante ne prouve rien.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from aster.cli import build_parser
from aster.data.minute_quality import profile_frame, profile_symbol, profile_symbols
from aster.data.r2_klines import CUTOFF, PREFIX, RAW_COLUMNS


def _bars(periods: int = 10, start: str = "2024-06-01 00:00", freq: str = "1min"):
    """Index synthétique UTC, pré-cutoff."""
    return pd.date_range(start, periods=periods, freq=freq, tz="UTC")


def _col(value, n: int):
    """Scalaire -> constante ; séquence -> telle quelle, alignée sur l'index.

    Une séquence passée par erreur dans `[value] * n` produirait une colonne
    object et ferait echouer la comparaison, au lieu de tester la regle visee.
    """
    if isinstance(value, (list, tuple, pd.Series, np.ndarray)):
        values = list(value)
        assert len(values) == n, "sequence length must match the index"
        return values
    return [value] * n


def _frame(index, *, trades=7, volume=3.0, open_=100.0, high=101.0, low=99.0, close=100.5):
    n = len(index)
    return pd.DataFrame(
        {
            "open": _col(open_, n), "high": _col(high, n), "low": _col(low, n),
            "close": _col(close, n), "volume": _col(volume, n), "trades": _col(trades, n),
        },
        index=index,
    )


# --- couverture ---------------------------------------------------------------

def test_full_minute_span_has_perfect_coverage():
    q = profile_frame("BTCUSDT", _frame(_bars(60)), partitions=1)
    assert q.rows == 60
    assert q.expected_minutes == 60
    assert q.present_minutes == 60
    assert q.missing_minutes == 0
    assert q.coverage == 1.0
    assert q.errors == []


def test_missing_minute_is_a_hole_not_a_frozen_bar():
    index = _bars(60).delete(30)  # une minute absente
    q = profile_frame("BTCUSDT", _frame(index), partitions=1)
    assert q.missing_minutes == 1
    assert q.coverage == pytest.approx(59 / 60)
    assert q.frozen_bars == 0, "un trou n'est pas une minute gelée"


def test_gap_across_minutes_is_reported_once():
    # Le trou doit etre INTERNE: supprimer la queue ne laisse aucun trou.
    index = _bars(10).delete(list(range(2, 7)))  # 5 minutes absentes au milieu
    q = profile_frame("BTCUSDT", _frame(index), partitions=1)
    assert any("minute gaps" in w for w in q.warnings)
    assert q.missing_minutes == 5


def test_missing_whole_month_is_listed():
    index = _bars(10, start="2024-05-01 00:00").append(_bars(10, start="2024-06-01 00:00"))
    q = profile_frame("BTCUSDT", _frame(index), partitions=1)
    assert q.missing_minutes > 0
    # mai 2024 est présent, juin aussi -> aucun mois entièrement vide
    assert q.missing_months == []


def test_whole_missing_month_detected():
    index = _bars(10, start="2024-04-01 00:00").append(_bars(10, start="2024-06-01 00:00"))
    q = profile_frame("BTCUSDT", _frame(index), partitions=1)
    assert q.missing_months == ["2024-05"]


# --- minutes gelées -----------------------------------------------------------

def test_frozen_minutes_counted_from_zero_trades():
    q = profile_frame("BTCUSDT", _frame(_bars(10), trades=[0] * 3 + [7] * 7), partitions=1)
    assert q.frozen_bars == 3
    assert q.frozen_share == pytest.approx(0.3)
    assert q.frozen_bars <= q.rows


def test_frozen_share_above_threshold_is_an_error_not_a_warning():
    q = profile_frame("DOGEUSDT", _frame(_bars(100), trades=[0] * 10 + [7] * 90), partitions=1)
    from aster.data.minute_quality import _apply_thresholds
    strict = _apply_thresholds(q, max_frozen_share=0.05, min_coverage=0.99)
    assert not strict.usable
    assert any("frozen share" in e for e in strict.errors)


def test_trades_with_zero_volume_is_an_accounting_error():
    index = _bars(10)
    df = _frame(index)
    df.loc[df.index[2], "volume"] = 0.0  # trades=7 mais volume=0
    q = profile_frame("BTCUSDT", df, partitions=1)
    assert q.zero_trade_volume_bars == 1
    assert q.zero_volume_bars == 1


def test_zero_volume_with_zero_trades_is_just_illiquidity():
    index = _bars(10)
    df = _frame(index)
    df.loc[df.index[4], "volume"] = 0.0
    df.loc[df.index[4], "trades"] = 0
    q = profile_frame("BTCUSDT", df, partitions=1)
    assert q.zero_trade_volume_bars == 0
    assert q.zero_volume_bars == 1


# --- intégrité des prix -------------------------------------------------------

def test_high_below_low_is_an_error():
    q = profile_frame("BTCUSDT", _frame(_bars(10), high=98.0, low=99.0), partitions=1)
    assert any("high < low" in e for e in q.errors)
    assert not q.usable


def test_close_outside_bar_range_is_an_error():
    q = profile_frame("BTCUSDT", _frame(_bars(10), close=120.0), partitions=1)
    assert any("closes outside" in e for e in q.errors)


def test_non_positive_price_is_an_error():
    q = profile_frame("BTCUSDT", _frame(_bars(10), low=0.0), partitions=1)
    assert any("non-positive" in e for e in q.errors)


def test_negative_volume_is_an_error():
    df = _frame(_bars(10))
    df.loc[df.index[1], "volume"] = -1.0
    q = profile_frame("BTCUSDT", df, partitions=1)
    assert any("negative volume" in e for e in q.errors)


# --- discipline des timestamps ------------------------------------------------

def test_unsorted_index_is_an_error():
    index = _bars(10)
    df = _frame(index)
    df = df.iloc[::-1]
    q = profile_frame("BTCUSDT", df, partitions=1)
    assert any("not sorted" in e for e in q.errors)


def test_duplicate_timestamps_are_an_error():
    index = _bars(10)
    dup = pd.DatetimeIndex(list(index) + [index[-1]])
    q = profile_frame("BTCUSDT", _frame(dup), partitions=1)
    assert any("duplicated" in e for e in q.errors)


def test_off_minute_grid_is_an_error():
    index = pd.DatetimeIndex(list(_bars(4)) + [_bars(1)[0] + pd.Timedelta(seconds=30)])
    q = profile_frame("BTCUSDT", _frame(index), partitions=1)
    assert any("minute grid" in e for e in q.errors)


def test_post_cutoff_minute_is_an_error_and_never_counted():
    index = _bars(5, start="2024-06-30 23:58").append(_bars(3, start="2024-07-01 00:00"))
    q = profile_frame("BTCUSDT", _frame(index), partitions=1)
    assert any("exploration cutoff" in e for e in q.errors)
    assert not q.usable


def test_naive_index_is_an_error():
    index = pd.date_range("2024-06-01", periods=5, freq="1min")  # sans tz
    q = profile_frame("BTCUSDT", _frame(index), partitions=1)
    assert any("tz-aware" in e for e in q.errors)


def test_empty_frame_is_an_error():
    q = profile_frame("BTCUSDT", _frame(pd.DatetimeIndex([], tz="UTC")), partitions=0)
    assert not q.usable
    assert q.rows == 0


# --- intégration locale (Parquet synthétique, toujours hors réseau) -----------

def _seed(root: Path, symbol: str, month: str, n_rows: int, trades_value: int = 7,
          frozen_first: int = 0) -> Path:
    """Seed one synthetic pre-cutoff partition; ``frozen_first`` leading bars
    carry ``trades = 0`` so a realistic frozen share can be tested."""
    path = root / "data" / "r2" / PREFIX / f"symbol={symbol}" / "year=2024" / f"month={month}" / "part.parquet"
    path.parent.mkdir(parents=True, exist_ok=True)
    ts = pd.date_range(f"2024-{month}-01 00:00:00", periods=n_rows, freq="1min", tz="UTC")
    trades = [0] * frozen_first + [trades_value] * (n_rows - frozen_first)
    table = pa.table({
        "open_time_ms": pa.array((ts.asi8 // 1_000_000).astype("int64")),
        "open_time_utc": pa.array(ts),
        "close_time_ms": pa.array((ts.asi8 // 1_000_000 + 59_999).astype("int64")),
        "open": pa.array([100.0] * n_rows), "high": pa.array([101.0] * n_rows),
        "low": pa.array([99.0] * n_rows), "close": pa.array([100.5] * n_rows),
        "volume": pa.array([3.0] * n_rows), "quote_volume": pa.array([300.0] * n_rows),
        "trades": pa.array(trades), "taker_buy_base": pa.array([2.0] * n_rows),
        "taker_buy_quote": pa.array([200.0] * n_rows),
    })
    assert tuple(table.schema.names) == RAW_COLUMNS
    pq.write_table(table, path)
    import hashlib
    key = path.relative_to(root / "data" / "r2").as_posix()
    manifest = {
        "source": "cloudflare-r2", "bucket": "cryptos", "key": key,
        "size_bytes": path.stat().st_size, "etag": None,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "cutoff_exclusive": CUTOFF.isoformat(),
        "imported_at": "2026-10-13T00:00:00+00:00",
        "timestamp_unit": "datetime", "rows": n_rows,
        "start": ts.min().isoformat(), "end": ts.max().isoformat(),
    }
    path.with_suffix(".parquet.manifest.json").write_text(json.dumps(manifest) + "\n")
    return path


def test_profile_symbol_reads_local_partitions(isolated_desk):
    _seed(isolated_desk, "BTCUSDT", "06", 30)
    q = profile_symbol("BTCUSDT")
    assert q.usable
    assert q.rows == 30
    assert q.partitions == 1
    assert q.coverage == 1.0


def test_profile_symbols_reports_panel_staleness(isolated_desk):
    _seed(isolated_desk, "BTCUSDT", "06", 30)
    # XMR s'arrête en février, les autres vont en juin : le panneau est hétérogène
    xmr = isolated_desk / "data" / "r2" / PREFIX / "symbol=XMRUSDT" / "year=2024" / "month=02" / "part.parquet"
    xmr.parent.mkdir(parents=True, exist_ok=True)
    ts = pd.date_range("2024-02-01 00:00:00", periods=30, freq="1min", tz="UTC")
    table = pa.table({
        "open_time_ms": pa.array((ts.asi8 // 1_000_000).astype("int64")),
        "open_time_utc": pa.array(ts),
        "close_time_ms": pa.array((ts.asi8 // 1_000_000 + 59_999).astype("int64")),
        "open": pa.array([100.0] * 30), "high": pa.array([101.0] * 30),
        "low": pa.array([99.0] * 30), "close": pa.array([100.5] * 30),
        "volume": pa.array([3.0] * 30), "quote_volume": pa.array([300.0] * 30),
        "trades": pa.array([7] * 30), "taker_buy_base": pa.array([2.0] * 30),
        "taker_buy_quote": pa.array([200.0] * 30),
    })
    pq.write_table(table, xmr)
    import hashlib
    key = xmr.relative_to(isolated_desk / "data" / "r2").as_posix()
    manifest = {
        "source": "cloudflare-r2", "bucket": "cryptos", "key": key,
        "size_bytes": xmr.stat().st_size, "etag": None,
        "sha256": hashlib.sha256(xmr.read_bytes()).hexdigest(),
        "cutoff_exclusive": CUTOFF.isoformat(),
        "imported_at": "2026-10-13T00:00:00+00:00",
        "timestamp_unit": "datetime", "rows": 30,
        "start": ts.min().isoformat(), "end": ts.max().isoformat(),
    }
    xmr.with_suffix(".parquet.manifest.json").write_text(json.dumps(manifest) + "\n")

    report = profile_symbols(("BTCUSDT", "XMRUSDT"))
    assert [s["symbol"] for s in report["stale_symbols"]] == ["XMRUSDT"]
    assert report["stale_symbols"][0]["lag_days"] > 100
    assert report["ok"] is False  # un panneau hétérogène n'est pas « ok »
    # mais XMR reste utilisable individuellement
    assert "XMRUSDT" in report["symbols_usable"]


# --- CLI ----------------------------------------------------------------------

def test_cli_quality_r2_dispatch(monkeypatch, isolated_desk):
    _seed(isolated_desk, "BTCUSDT", "06", 30)
    captured = []
    monkeypatch.setattr("aster.cli._print", captured.append)
    args = build_parser().parse_args(["data", "quality-r2", "--symbols", "BTCUSDT"])
    args.fn(args)
    report = captured[0]
    assert report["symbols_usable"] == ["BTCUSDT"]
    assert report["cutoff_exclusive"] == CUTOFF.isoformat()


def test_cli_quality_r2_thresholds_are_explicit(monkeypatch, isolated_desk):
    # 20 % de minutes gelees: rejette au seuil par defaut (0.05), accepte a 0.2.
    _seed(isolated_desk, "DOGEUSDT", "06", 100, frozen_first=20)
    captured = []
    monkeypatch.setattr("aster.cli._print", captured.append)
    args = build_parser().parse_args([
        "data", "quality-r2", "--symbols", "DOGEUSDT",
        "--max-frozen-share", "0.2", "--min-coverage", "0.9",
    ])
    args.fn(args)
    assert captured[0]["symbols_usable"] == ["DOGEUSDT"]  # seuil relâché -> acceptable
    assert captured[0]["thresholds"]["max_frozen_share"] == 0.2
    # Le meme jeu de donnees doit rester rejete sous le seuil par defaut:
    # relacher un seuil est un choix explicite du research, pas un defaut.
    captured.clear()
    strict = build_parser().parse_args(["data", "quality-r2", "--symbols", "DOGEUSDT"])
    strict.fn(strict)
    assert captured[0]["symbols_usable"] == []
    assert any("frozen share" in e for e in captured[0]["per_symbol"][0]["errors"])
