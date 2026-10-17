"""Q5 — BTC/ETH intraday N2 (descriptive stats).

Computes, for each (symbol, timeframe) pair:

* the first 10 lags of return and absolute-return autocorrelation,
* the Lo-MacKinlay variance ratio at a 2-bar and 4-bar horizon,
* the Hurst exponent (rescaled range, DFA proxy via the variance
  of cumulative sums on a log-spaced block grid).

Frozen minutes are NOT excluded in V1 (Q5 prereg says "no
frozen-minute exclusion yet"). V2 will add the filter.

This is a descriptive memo (not a hypothesis), so it does not count
toward the Deflated Sharpe denominator of any future hypothesis.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.data import store


def _autocorr(x: np.ndarray, lag: int) -> float:
    """Pearson autocorrelation of ``x`` at the given lag (NaN-safe)."""
    if len(x) <= lag + 1:
        return float("nan")
    a = x[:-lag]
    b = x[lag:]
    mask = np.isfinite(a) & np.isfinite(b)
    if mask.sum() < 10:
        return float("nan")
    return float(np.corrcoef(a[mask], b[mask])[0, 1])


def _variance_ratio(x: np.ndarray, q: int) -> float:
    """Lo-MacKinlay homoskedastic variance ratio at horizon ``q``.

    VR(q) = Var(r_q) / (q * Var(r_1)) where r_q is the q-period
    return. Under the random-walk null, VR = 1; > 1 = trending,
    < 1 = mean-reverting.
    """
    x = x[np.isfinite(x)]
    if len(x) < 4 * q:
        return float("nan")
    var_1 = float(np.var(x, ddof=1))
    if var_1 <= 0:
        return float("nan")
    # q-period returns: sum of q consecutive 1-period returns.
    # Trim to a whole number of q-period blocks (n_q * q elements).
    n_q = len(x) // q
    if n_q < 4:
        return float("nan")
    trimmed = x[: n_q * q].reshape(n_q, q)
    r_q = trimmed.sum(axis=1)
    var_q = float(np.var(r_q, ddof=1))
    return var_q / (q * var_1)


def _hurst_rs(x: np.ndarray, max_block: int = 256) -> float:
    """Hurst exponent by rescaled-range on log-spaced block sizes.

    A robust, parameter-light estimator. For each block size n in
    {4, 8, 16, 32, 64, 128, 256} the (R/S) is the range of the
    cumulative-sum series divided by its standard deviation. The
    Hurst exponent is the slope of log(R/S) vs log(n).
    """
    x = x[np.isfinite(x)]
    if len(x) < 4 * max_block:
        return float("nan")
    log_n = []
    log_rs = []
    for n in (4, 8, 16, 32, 64, 128, 256):
        if n > max_block:
            break
        if len(x) < 4 * n:
            break
        n_blocks = len(x) // n
        # Trim to a whole number of blocks.
        trimmed = x[: n_blocks * n].reshape(n_blocks, n)
        rs_values = []
        for block in trimmed:
            mean = block.mean()
            dev = block.std(ddof=1)
            if dev <= 0:
                continue
            cum = np.cumsum(block - mean)
            rng = cum.max() - cum.min()
            rs_values.append(rng / dev)
        if not rs_values:
            continue
        log_n.append(np.log(n))
        log_rs.append(np.log(np.mean(rs_values)))
    if len(log_n) < 3:
        return float("nan")
    slope, _intercept, _r, _p, _se = stats.linregress(log_n, log_rs)
    return float(slope)


def describe(close: pd.Series) -> dict:
    """Return the Q5 V1 descriptive block for one (symbol, timeframe)."""
    r = close.pct_change(fill_method=None).to_numpy()
    r_abs = np.abs(r)
    out = {
        "n_obs": int(np.isfinite(r).sum()),
        "start": str(close.index[0]),
        "end": str(close.index[-1]),
        "ret_autocorr": {f"lag{k}": _autocorr(r, k) for k in (1, 2, 3, 5, 10)},
        "abs_ret_autocorr": {f"lag{k}": _autocorr(r_abs, k) for k in (1, 2, 3, 5, 10)},
        "variance_ratio": {"q2": _variance_ratio(r, 2), "q4": _variance_ratio(r, 4)},
        "hurst_rs": _hurst_rs(r),
    }
    return out


def run(symbols: list[str], timeframes: list[str], exchange: str = "binance") -> dict:
    """Compute the Q5 descriptive block for every (symbol, timeframe)."""
    block: dict = {"by_symbol": {}}
    for sym in symbols:
        block["by_symbol"][sym] = {"by_timeframe": {}}
        for tf in timeframes:
            df = store.read("ohlcv", exchange, sym, tf)
            block["by_symbol"][sym]["by_timeframe"][tf] = describe(df["close"])
    return block


def main() -> None:
    """CLI entry point. Emits the JSON artefact under
    ``research/atlas/q5_intraday_n2.json``.
    """
    # ``paths`` lives in ``aster.cli`` because the CLI is the only
    # place that resolves the desk config; importing it lazily avoids
    # a hard dep on a side-effect-laden module.
    from aster.cli import paths

    cfg = paths.load_config("desk")
    # The store expects ``BTC/USDT`` (it slashes -> dash); keep the
    # desk.yaml universe untouched here.
    universe = cfg.get("universe", ["BTC/USDT", "ETH/USDT"])
    timeframes = ["5m", "15m", "1h", "4h", "1d"]
    block = run(universe, timeframes, exchange=cfg.get("exchange", "binance"))
    out_path = Path("research/atlas/q5_intraday_n2.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(block, indent=2, sort_keys=True))
    print(f"wrote {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
