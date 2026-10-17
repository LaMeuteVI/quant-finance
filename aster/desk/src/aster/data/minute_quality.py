"""Pre-cutoff minute-bar quality profile for the local R2 spot kline store.

Complements :func:`aster.data.r2_klines.audit_local`.  The audit proves a partition
is intact (schema, provenance, cutoff, hash).  This module measures what the audit
cannot: whether the *market* data is usable for bar construction.

It answers four questions per symbol, without ever reading post-cutoff values:

1. coverage: how many calendar minutes exist between the first and last observed
   bar, how many are actually present, and which months are missing entirely;
2. frozen bars: minutes the exchange reported with zero trades, i.e. a stale
   print, which must never be treated as an observation;
3. price integrity: non-positive prices, ``high < low``, closes outside the bar
   range, negative volume, and minute timestamp discipline;
4. panel staleness: a symbol whose history stops long before the cutoff would
   silently distort a cross-sectional universe, so the lag is measured against
   the most recent bar observed in the panel.

Every threshold is an explicit argument.  The function never relaxes a gate on
its own and never mutates data.  It does not fill gaps and it does not drop
frozen bars: cleaning is a separate, tested, deliberate step.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace

import pandas as pd
import pyarrow.parquet as pq

from aster.data.r2_klines import CUTOFF, SYMBOLS, _local_partitions, audit_local

# Only the columns the profile needs: a 31M-row pass stays cheap.
_PROFILE_COLUMNS = ("open_time_utc", "open", "high", "low", "close", "volume", "trades")
_MINUTE = pd.Timedelta(minutes=1)
# A symbol trading less recently than this is flagged as a panel-level anomaly.
_DEFAULT_MAX_STALENESS_DAYS = 7.0


@dataclass(frozen=True)
class SymbolQuality:
    """Per-symbol verdict.  Frozen so a report cannot mutate it afterwards."""

    symbol: str
    partitions: int
    rows: int
    first: str
    last: str
    expected_minutes: int
    present_minutes: int
    missing_minutes: int
    coverage: float
    frozen_bars: int
    frozen_share: float
    zero_volume_bars: int
    zero_trade_volume_bars: int
    missing_months: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def usable(self) -> bool:
        return not self.errors

    def as_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "usable": self.usable,
            "partitions": self.partitions,
            "rows": self.rows,
            "first": self.first,
            "last": self.last,
            "expected_minutes": self.expected_minutes,
            "present_minutes": self.present_minutes,
            "missing_minutes": self.missing_minutes,
            "coverage": self.coverage,
            "frozen_bars": self.frozen_bars,
            "frozen_share": self.frozen_share,
            "zero_volume_bars": self.zero_volume_bars,
            "zero_trade_volume_bars": self.zero_trade_volume_bars,
            "missing_months": self.missing_months,
            "errors": self.errors,
            "warnings": self.warnings,
        }


def _missing_months(index: pd.DatetimeIndex, first: pd.Timestamp, last: pd.Timestamp) -> list[str]:
    """Calendar months between first and last with no bar at all."""
    observed = {(ts.year, ts.month) for ts in index}
    missing: list[str] = []
    cursor = pd.Timestamp(year=first.year, month=first.month, day=1, tz="UTC")
    stop = pd.Timestamp(year=last.year, month=last.month, day=1, tz="UTC")
    while cursor <= stop:
        if (cursor.year, cursor.month) not in observed:
            missing.append(f"{cursor.year:04d}-{cursor.month:02d}")
        cursor += pd.offsets.MonthBegin(1)
    return missing


def profile_frame(symbol: str, frame: pd.DataFrame, partitions: int) -> SymbolQuality:
    """Profile one symbol's bars.  Pure: takes a UTC-indexed frame, returns a verdict."""
    index = pd.DatetimeIndex(frame.index)
    rows = len(index)
    if rows == 0:
        return SymbolQuality(
            symbol=symbol, partitions=partitions, rows=0, first="", last="",
            expected_minutes=0, present_minutes=0, missing_minutes=0, coverage=0.0,
            frozen_bars=0, frozen_share=0.0, zero_volume_bars=0, zero_trade_volume_bars=0,
            errors=[f"{symbol}: no local minutes"],
        )

    errors: list[str] = []
    warnings: list[str] = []
    first, last = index.min(), index.max()

    # --- timestamp discipline -------------------------------------------------
    # A naive or non-UTC index cannot be compared against CUTOFF safely, so the
    # timezone verdict is reached first and the remaining checks are skipped
    # rather than raising.  A profile must always return a verdict, never throw.
    tz_error = None
    if index.tz is None:
        tz_error = f"{symbol}: index is not tz-aware"
    elif str(index.tz) != "UTC":
        tz_error = f"{symbol}: index timezone is {index.tz}, expected UTC"
    if tz_error:
        errors.append(tz_error)

    if not index.is_monotonic_increasing:
        errors.append(f"{symbol}: index not sorted")
    duplicates = int(index.duplicated().sum())
    if duplicates:
        errors.append(f"{symbol}: {duplicates} duplicated timestamps")
    off_grid = int((index.floor("min") != index).sum())
    if off_grid:
        errors.append(f"{symbol}: {off_grid} timestamps off the minute grid")
    if tz_error is None and (index >= CUTOFF).any():
        errors.append(f"{symbol}: contains minutes at or after the exploration cutoff")

    # --- coverage -------------------------------------------------------------
    # Every calendar minute between the first and last observation.  A missing
    # minute is a hole, not a frozen bar, and must never be silently filled.
    # NaT timestamps poison the arithmetic, so they are excluded explicitly.
    if index.hasnans:
        errors.append(f"{symbol}: {int(index.isna().sum())} NaT timestamps")
    clean = index[~index.isna()]
    first = clean.min() if len(clean) else first
    last = clean.max() if len(clean) else last
    present = int(clean.nunique())
    expected = int((last - first) / _MINUTE) + 1 if tz_error is None and len(clean) > 1 else present
    coverage = present / expected if expected else 0.0

    # --- frozen and stale bars ------------------------------------------------
    trades, volume = frame["trades"], frame["volume"]
    frozen = int((trades == 0).sum())
    frozen_share = frozen / rows
    zero_volume = int((volume == 0).sum())
    # Trades > 0 with volume == 0 is an accounting inconsistency, not illiquidity.
    # Reported separately so it cannot hide inside a generic warning.
    zero_trade_volume = int(((trades > 0) & (volume == 0)).sum())

    # --- price integrity ------------------------------------------------------
    prices = frame[["open", "high", "low", "close"]]
    non_positive = int((prices <= 0).any(axis=1).sum())
    if non_positive:
        errors.append(f"{symbol}: {non_positive} bars with a non-positive price")
    inverted = int((frame["high"] < frame["low"]).sum())
    if inverted:
        errors.append(f"{symbol}: {inverted} bars with high < low")
    outside = int(((frame["close"] > frame["high"]) | (frame["close"] < frame["low"])).sum())
    if outside:
        errors.append(f"{symbol}: {outside} closes outside [low, high]")
    negative_volume = int((volume < 0).sum())
    if negative_volume:
        errors.append(f"{symbol}: {negative_volume} bars with negative volume")

    # --- gaps -----------------------------------------------------------------
    steps = index.to_series().diff().dropna()
    gaps = int((steps > _MINUTE).sum())
    if gaps:
        warnings.append(f"{symbol}: {gaps} minute gaps (largest {steps.max()})")
    if frozen_share > 0.01:
        warnings.append(f"{symbol}: {frozen_share:.2%} of minutes have zero trades")

    return SymbolQuality(
        symbol=symbol,
        partitions=partitions,
        rows=rows,
        first=first.isoformat(),
        last=last.isoformat(),
        expected_minutes=expected,
        present_minutes=present,
        missing_minutes=max(expected - present, 0),
        coverage=coverage,
        frozen_bars=frozen,
        frozen_share=frozen_share,
        zero_volume_bars=zero_volume,
        zero_trade_volume_bars=zero_trade_volume,
        missing_months=_missing_months(index, first, last),
        errors=errors,
        warnings=warnings,
    )


def _apply_thresholds(quality: SymbolQuality, max_frozen_share: float,
                      min_coverage: float) -> SymbolQuality:
    errors = list(quality.errors)
    if quality.frozen_share > max_frozen_share:
        errors.append(f"{quality.symbol}: frozen share {quality.frozen_share:.2%} exceeds the "
                      f"{max_frozen_share:.2%} usability limit")
    if quality.coverage < min_coverage:
        errors.append(f"{quality.symbol}: coverage {quality.coverage:.4%} is below the "
                      f"{min_coverage:.2%} usability floor")
    if quality.zero_trade_volume_bars:
        errors.append(f"{quality.symbol}: {quality.zero_trade_volume_bars} minutes report "
                      f"trades > 0 with volume == 0 (accounting inconsistency)")
    return replace(quality, errors=errors)


def profile_symbol(symbol: str, max_frozen_share: float = 0.05,
                   min_coverage: float = 0.99) -> SymbolQuality:
    """Profile one approved local symbol.

    The audit is re-run first on purpose: a profile must never be produced from a
    store whose provenance has not been verified in this process.
    """
    audit_local((symbol,))
    partitions = _local_partitions((symbol,))
    frames = [pq.ParquetFile(path).read(columns=list(_PROFILE_COLUMNS)).to_pandas()
              for path, _ in partitions]
    frame = pd.concat(frames, ignore_index=True)
    frame.index = pd.DatetimeIndex(pd.to_datetime(frame.pop("open_time_utc"), utc=True),
                                   name="open_time_utc")
    return _apply_thresholds(profile_frame(symbol, frame, len(partitions)),
                             max_frozen_share, min_coverage)


def profile_symbols(symbols: tuple[str, ...] = SYMBOLS,
                    max_frozen_share: float = 0.05,
                    min_coverage: float = 0.99,
                    max_staleness_days: float = _DEFAULT_MAX_STALENESS_DAYS) -> dict:
    """Profile a set of approved symbols and return a JSON-ready report."""
    reports = [profile_symbol(symbol, max_frozen_share=max_frozen_share,
                              min_coverage=min_coverage) for symbol in symbols]
    usable = [r for r in reports if r.usable]
    rows_total = sum(r.rows for r in reports)
    frozen_total = sum(r.frozen_bars for r in reports)

    # Panel staleness: measured against the most recent bar in the panel, so a
    # symbol that stopped trading (or was never updated) cannot hide behind the
    # others. This is reported, never auto-excluded.
    panel_last = max((pd.Timestamp(r.last) for r in reports if r.rows), default=None)
    stale: list[dict] = []
    if panel_last is not None:
        for r in reports:
            if not r.rows:
                continue
            lag_days = (panel_last - pd.Timestamp(r.last)) / pd.Timedelta(days=1)
            if lag_days > max_staleness_days:
                stale.append({"symbol": r.symbol, "last": r.last,
                              "lag_days": round(float(lag_days), 3)})

    return {
        "ok": bool(reports) and len(usable) == len(reports) and not stale,
        "cutoff_exclusive": CUTOFF.isoformat(),
        "thresholds": {
            "max_frozen_share": max_frozen_share,
            "min_coverage": min_coverage,
            "max_staleness_days": max_staleness_days,
        },
        "panel_last_bar": panel_last.isoformat() if panel_last is not None else None,
        "symbols_requested": list(symbols),
        "symbols_usable": [r.symbol for r in usable],
        "symbols_unusable": [r.symbol for r in reports if not r.usable],
        "stale_symbols": stale,
        "totals": {
            "symbols": len(reports),
            "rows": rows_total,
            "frozen_bars": frozen_total,
            "frozen_share": (frozen_total / rows_total) if rows_total else 0.0,
        },
        "per_symbol": [r.as_dict() for r in reports],
    }
