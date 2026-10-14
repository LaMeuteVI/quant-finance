"""Reference tests for panel N0."""
from __future__ import annotations

import pandas as pd

from aster.research.panel_n0 import AssetPayload, hourly_profile, write_combined_report, write_per_asset_report


def test_hourly_profile_aggregates_168_buckets():
    idx = pd.date_range("2024-01-01", periods=24 * 7, freq="h", tz="UTC")
    df = pd.DataFrame({
        "open": 1.0, "high": 1.0, "low": 1.0, "close": 1.0,
        "volume": 10.0, "quote_volume": 100.0, "trades": 5,
        "taker_buy_base": 5.0, "taker_buy_quote": 50.0,
    }, index=idx)
    prof = hourly_profile(df)
    assert len(prof) == 168
    assert prof["median_dollar_volume"].iloc[0] == 100.0


def test_write_per_asset_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    payload = AssetPayload(
        symbol="TESTUSDT", raw_rows=10, coverage=0.999, missing_minutes=10,
        frozen_minutes=0, frozen_share=0.0,
        median_dollar_volume=10.0, median_tradeful_dollar_volume=20.0,
        median_trades=1.0, median_tradeful_trades=2.0,
        median_taker_buy_ratio=0.5, first="2024-01-01T00:00:00+00:00",
        last="2024-01-01T00:09:00+00:00",
    )
    df = pd.DataFrame({"a": [1]}, index=pd.DatetimeIndex(["2024-01-01"], tz="UTC"))
    write_per_asset_report(payload, df)
    written = list(tmp_path.glob("research/assets/*.md"))
    assert any("testusdt" in p.name for p in written)


def test_write_combined_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    payloads = [
        AssetPayload(
            symbol="AAAUSDT", raw_rows=10, coverage=0.999, missing_minutes=0,
            frozen_minutes=0, frozen_share=0.0,
            median_dollar_volume=1.0, median_tradeful_dollar_volume=2.0,
            median_trades=1.0, median_tradeful_trades=1.0,
            median_taker_buy_ratio=0.5, first="2024-01-01T00:00:00+00:00",
            last="2024-01-02T00:00:00+00:00",
        ),
    ]
    write_combined_report(payloads)
    assert (tmp_path / "research/assets/2026-10-14-panel-n0.md").exists()
    assert (tmp_path / "research/assets/2026-10-14-panel-n0-comparison.csv").exists()
