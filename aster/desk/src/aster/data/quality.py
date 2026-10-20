"""Data quality checks. A dataset with errors must not feed a backtest."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from aster.data.ccxt_source import TIMEFRAME_MS


@dataclass
class QualityReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def check_ohlcv(df: pd.DataFrame, timeframe: str, outlier_mads: float = 15.0) -> QualityReport:
    r = QualityReport()
    if df.empty:
        r.errors.append("empty dataset")
        return r
    idx = df.index
    if idx.tz is None:
        r.errors.append("index is not tz-aware")
    if idx.has_duplicates:
        r.errors.append(f"{int(idx.duplicated().sum())} duplicated timestamps")
    if not idx.is_monotonic_increasing:
        r.errors.append("index not sorted")
    if (df[["open", "high", "low", "close"]] <= 0).any().any():
        r.errors.append("non-positive prices")
    if (df["high"] < df["low"]).any():
        r.errors.append("high < low on some bars")
    outside = (df["close"] > df["high"] * (1 + 1e-9)) | (df["close"] < df["low"] * (1 - 1e-9))
    if outside.any():
        r.errors.append(f"{int(outside.sum())} closes outside [low, high]")

    step = pd.Timedelta(milliseconds=TIMEFRAME_MS[timeframe])
    gaps = idx.to_series().diff().dropna()
    n_gaps = int((gaps > step).sum())
    if n_gaps:
        r.warnings.append(f"{n_gaps} gaps (largest {gaps.max()})")
    zero_vol = float((df["volume"] <= 0).mean())
    if zero_vol > 0.01:
        r.warnings.append(f"{zero_vol:.1%} bars with zero volume (stale or illiquid)")

    lr = np.log(df["close"]).diff().dropna()
    if len(lr) > 30:
        med = lr.median()
        mad = (lr - med).abs().median() * 1.4826
        if mad > 0:
            n_out = int(((lr - med).abs() > outlier_mads * mad).sum())
            if n_out:
                r.warnings.append(f"{n_out} returns beyond {outlier_mads} MADs: inspect for bad prints")
    return r
