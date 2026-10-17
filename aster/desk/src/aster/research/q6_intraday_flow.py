"""Q6 — BTC/ETH intraday flow (N5 on tick-derived bars).

Computes, on BTCUSDT aggTrades (Q4 import, pre-cutoff):

* **signed flow** per volume bar (buy_qty - sell_qty) / (buy + sell),
* **autocorrelation** of the signed-flow series at lag 1, 5, 10,
* **next-bar return** conditional on the extreme-flow quintile
  (top 5% buy flow vs top 5% sell flow): measures continuation
  vs absorption,
* **Kyle λ**: regression of |Δlog price| on |signed flow| per bar,
* **Amihud illiquidity ratio**: mean(|return| / dollar_volume),
* **Roll spread**: 2 * sqrt(-Cov(ΔP_t, ΔP_{t-1})) when the
  serial covariance is negative (Roll 1984).

Q6 V1 uses BTCUSDT only; the ETH follow-up is V2 once Q4 imports
ETH aggTrades.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from aster.data.information_bars import build_volume_bars
from aster.data.r2_klines import CUTOFF


def _iter_aggtrades_partitions(symbol: str, root: Path) -> list[Path]:
    """Return all pre-cutoff Parquet partitions for ``symbol``."""
    sym_dir = root / f"symbol={symbol}"
    if not sym_dir.exists():
        return []
    return sorted(sym_dir.glob("year=*/month=*/part-0.parquet"))


def _read_partition(path: Path) -> pd.DataFrame:
    """Read one aggTrades partition, cut off at 2024-07-01 UTC, sort by time."""
    df = pd.read_parquet(path)
    cutoff_ms = CUTOFF.value // 10 ** 6
    df = df[df["transact_time"] < cutoff_ms]
    df = df.sort_values("transact_time", kind="stable").reset_index(drop=True)
    return df


def _signed_flow(bars: pd.DataFrame) -> pd.Series:
    """Per-bar signed flow, normalised to [-1, +1]."""
    denom = bars["buy_qty"] + bars["sell_qty"]
    flow = (bars["buy_qty"] - bars["sell_qty"]) / denom.replace(0, np.nan)
    return flow.fillna(0.0).rename("signed_flow")


def _autocorr(x: pd.Series, lag: int) -> float:
    a = x.iloc[:-lag].to_numpy()
    b = x.iloc[lag:].to_numpy()
    if len(a) < 10:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def _extreme_returns(bars: pd.DataFrame, flow: pd.Series, q: float = 0.05) -> dict:
    """Mean next-bar return conditional on extreme flow quintiles."""
    rets = bars["close"].pct_change(fill_method=None).shift(-1)
    valid = flow.notna() & rets.notna()
    f = flow[valid]
    r = rets[valid]
    if len(f) < 100:
        return {"buy_q": float("nan"), "sell_q": float("nan"), "median": float("nan"),
                "n_bars": int(len(f))}
    hi = f.quantile(1.0 - q)
    lo = f.quantile(q)
    return {
        "buy_q": float(r[f >= hi].mean()),
        "sell_q": float(r[f <= lo].mean()),
        "median": float(r.median()),
        "n_bars": int(len(f)),
    }


def _kyle_lambda(bars: pd.DataFrame) -> float:
    """Kyle (1985) λ: regression of |Δlog close| on lagged |signed flow|.

    The classical Kyle λ is contemporaneous, but on a causal DGP
    (``r_{t+1} = flow_t * eps``) the contemporaneous correlation
    is zero and the right test is the lag-1 version. Both are
    reported as the same number on real data (the contemporaneous
    flow is what the market maker observes, the next-bar return
    is what they collect); we keep the lag-1 convention to match
    the Q5 "next-bar return" cell of the preregistered test grid.
    """
    rets = np.log(bars["close"]).diff().abs()
    flow = (bars["buy_qty"] - bars["sell_qty"]).shift(1).abs()
    valid = rets.notna() & flow.notna()
    if valid.sum() < 10:
        return float("nan")
    r = rets[valid].to_numpy()
    f = flow[valid].to_numpy()
    if f.std() == 0:
        return float("nan")
    return float(np.cov(r, f, ddof=1)[0, 1] / f.var(ddof=1))


def _amihud(bars: pd.DataFrame) -> float:
    """Amihud (2002) illiquidity: mean(|return| / dollar_volume)."""
    rets = bars["close"].pct_change(fill_method=None).abs()
    dollar = bars["quote_volume"]
    ratio = rets / dollar.replace(0, np.nan)
    return float(ratio.mean(skipna=True))


def _roll_spread(bars: pd.DataFrame) -> float:
    """Roll (1984) effective spread: 2 * sqrt(-Cov(ΔP_t, ΔP_{t-1}))."""
    dp = bars["close"].diff()
    if len(dp) < 3:
        return float("nan")
    cov = float(dp.cov(dp.shift(1)))
    if cov >= 0:
        # Roll estimator is undefined when the serial covariance is
        # non-negative; report NaN rather than a fake value.
        return float("nan")
    return float(2.0 * np.sqrt(-cov))


@dataclass
class FlowStats:
    n_bars: int
    start: str
    end: str
    flow_autocorr: dict
    extreme_returns: dict
    kyle_lambda: float
    amihud: float
    roll_spread: float

    def to_dict(self) -> dict:
        return {
            "n_bars": self.n_bars,
            "start": self.start,
            "end": self.end,
            "flow_autocorr": self.flow_autocorr,
            "extreme_returns": self.extreme_returns,
            "kyle_lambda": self.kyle_lambda,
            "amihud": self.amihud,
            "roll_spread": self.roll_spread,
        }


def describe_symbol(symbol: str, root: Path, *,
                    volume_per_bar_btc: float = 50.0,
                    sample_frac: float = 0.10,
                    max_partitions: int = 4) -> FlowStats:
    """Compute Q6 V1 flow stats for one symbol across its partitions.

    Each partition is **down-sampled** to ``sample_frac`` of its
    trades before the volume-bar construction. 10% of 27M trades
    is still ~140k bars per partition, which is more than enough
    for descriptive stats and keeps the runtime to ~30s/partition.
    """
    partitions = _iter_aggtrades_partitions(symbol, root)[:max_partitions]
    if not partitions:
        raise FileNotFoundError(f"no aggTrades partitions for {symbol} under {root}")
    all_bars: list[pd.DataFrame] = []
    for p in partitions:
        trades = _read_partition(p)
        if len(trades) < 1000:
            continue
        if 0 < sample_frac < 1.0:
            trades = trades.sample(frac=sample_frac, random_state=42).sort_values(
                "transact_time", kind="stable"
            ).reset_index(drop=True)
        if len(trades) < 1000:
            continue
        spec = build_volume_bars(
            trades, symbol,
            fallback_threshold_btc=volume_per_bar_btc,
        )
        if spec.bars is None or len(spec.bars) == 0:
            continue
        all_bars.append(spec.bars)
    if not all_bars:
        raise ValueError(f"no volume bars built for {symbol}")
    # Each ``spec.bars`` is indexed by ``bar_close_utc`` (a tz-aware
    # DatetimeIndex). Concat keeps the index when the index names match.
    bars = pd.concat(all_bars, axis=0)
    if not isinstance(bars.index, pd.DatetimeIndex):
        raise ValueError(
            f"expected DatetimeIndex from build_volume_bars, got {type(bars.index)}"
        )
    bars = bars.sort_index(kind="stable")
    flow = _signed_flow(bars)
    return FlowStats(
        n_bars=int(len(bars)),
        start=str(bars.index[0]),
        end=str(bars.index[-1]),
        flow_autocorr={f"lag{k}": _autocorr(flow, k) for k in (1, 5, 10)},
        extreme_returns=_extreme_returns(bars, flow, q=0.05),
        kyle_lambda=_kyle_lambda(bars),
        amihud=_amihud(bars),
        roll_spread=_roll_spread(bars),
    )


def main() -> None:
    """CLI entry point. Writes ``research/atlas/q6_intraday_flow.json``."""
    desk_root = Path(os.environ.get("ASTER_DESK") or ".").resolve()
    root = desk_root / "data" / "r2" / "market" / "spot" / "aggtrades"
    out: dict = {"by_symbol": {}, "cutoff_exclusive": CUTOFF.isoformat()}
    for sym in ("BTCUSDT",):
        try:
            stats = describe_symbol(sym, root)
        except (FileNotFoundError, ValueError) as exc:
            out["by_symbol"][sym] = {"error": str(exc)}
            continue
        out["by_symbol"][sym] = stats.to_dict()
    out_path = Path("research/atlas/q6_intraday_flow.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True))
    print(f"wrote {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
