"""Tests for Q15 — ETH fvg_down panel re-test."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from aster.research import q15_fvg_panel as q15


def _make_df(n: int = 2000, start: str = "2022-01-01", freq: str = "1d",
             gap_at: int | None = None, gap_size: float = 0.001,
             fwd_after: float = 0.0, seed: int = 0) -> pd.DataFrame:
    """Construct a synthetic OHLC frame.

    Driftless log random walk with sigma=0.0001 (1 bp per bar). Two-bar
    drift therefore stays well below 5 bps. An injected `gap_at` of 50 bps
    produces a single trigger for the detector.
    """
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, periods=n, freq=freq, tz="UTC")
    log_ret = rng.normal(0.0, 0.0001, n)
    log_ret[0] = 0.0
    log_price = np.cumsum(log_ret)
    close = 100.0 * np.exp(log_price)
    if gap_at is not None and gap_at + 2 < n:
        close[gap_at] = close[gap_at - 2] * 0.995  # 50 bps gap down
    low = close * (1.0 - 0.0001)
    high = close * (1.0 + 0.0001)
    return pd.DataFrame({"close": close, "low": low, "high": high}, index=idx)


def test_detect_gaps_finds_injected():
    df = _make_df(n=2000, gap_at=100)
    triggered = q15._detect_gaps(
        df["close"], df["low"], df["high"], "down", 0.001
    )
    assert int(triggered.sum()) == 1
    assert bool(triggered.iloc[100]) is True


def test_detect_gaps_up_direction():
    df = _make_df(n=2000, freq="1d", seed=1)
    triggered_up = q15._detect_gaps(
        df["close"], df["low"], df["high"], "up", 0.001
    )
    triggered_dn = q15._detect_gaps(
        df["close"], df["low"], df["high"], "down", 0.001
    )
    # Up-gap and down-gap triggers are different events
    assert (triggered_up & triggered_dn).sum() == 0


def test_forward_returns_horizons_present():
    df = _make_df(n=2000, gap_at=100)
    triggered = q15._detect_gaps(
        df["close"], df["low"], df["high"], "down", 0.001
    )
    fwd = q15._forward_returns(df["close"], triggered, [1, 2, 5, 10])
    for h in [1, 2, 5, 10]:
        assert h in fwd
        assert "count" in fwd[h]
        assert "mean" in fwd[h]


def test_bh_fdr_basic():
    # 5 p-values, threshold at 0.05 -> reject the smallest 2
    pvals = [0.001, 0.004, 0.04, 0.5, 0.9]
    rej = q15._bh_fdr(pvals, q=0.05)
    assert rej[0] is True
    assert rej[1] is True
    assert rej[2] is False  # 0.04 not <= 3/5 * 0.05 = 0.03


def test_bh_fdr_no_rejections():
    pvals = [0.5, 0.9, 0.8]
    rej = q15._bh_fdr(pvals, q=0.05)
    assert not any(rej)


def test_bootstrap_ci_returns_quantiles():
    vals = np.random.default_rng(0).normal(0.01, 0.005, 200)
    lo, hi = q15._bootstrap_ci(vals)
    assert lo < hi
    assert abs(lo - 0.01) < 0.01 or abs(hi - 0.01) < 0.01


def test_one_cell_stats_shape():
    df = _make_df(n=2000, gap_at=100)
    cell = q15._one_cell_stats(df, "down", 0.001, [1, 2, 5, 10])
    assert cell["n_events"] == 1
    assert cell["fwd"][1]["count"] == 1


def test_run_produces_full_panel():
    """Skip when spot store is missing."""
    from aster.paths import desk_root
    desk = Path(desk_root()) if False else Path(".").resolve()
    if not (desk / "data/ohlcv/binance/ETH-USDT/1d.parquet").exists():
        pytest.skip("ETH spot store not present (tests run against tmp desk)")
    out = q15.run()
    assert out["n_axes"] == len(q15.SPOT_SLUGS) * len(q15.TIMEFRAMES)
    assert "verdict" in out
    assert out["verdict"]["verdict"] in {"RETAIN", "FALSIFIED", "NEUTRAL"}
