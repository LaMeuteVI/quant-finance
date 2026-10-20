"""Q21 — Free tick-data microstructure V2 (D3, GREEN).

Pure Python module. No I/O at import. Functions take a pandas DataFrame of
aggTrades (columns: agg_trade_id, price, quantity, transact_time, is_buyer_maker)
and return a bar-level DataFrame of microstructure observables.

All observables are causal (row t uses data <= t). No look-ahead.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


# -------- Tick-rule and signed volume --------


def tick_rule_sign(is_buyer_maker: np.ndarray) -> np.ndarray:
    """Standard tick-rule: trade is buy if price went up since the previous trade,
    sell if it went down. For the first trade in a series, default to +1 (buy).
    Note: `is_buyer_maker` is the *opposite* of aggressor side — a buyer-initiated
    trade has `is_buyer_maker=False`. We work in terms of aggressor side
    `is_buy = ~is_buyer_maker` for intuition.
    """
    price = np.asarray(is_buyer_maker, dtype=float)
    sign = np.empty_like(price, dtype=np.int8)
    sign[0] = 1  # default for first trade
    delta = np.diff(price, prepend=price[0])
    sign[1:] = np.where(delta[1:] > 0, 1, np.where(delta[1:] < 0, -1, 0)).astype(np.int8)
    return sign


def is_buy_aggressor(is_buyer_maker: np.ndarray) -> np.ndarray:
    """Aggressor buy = NOT buyer-maker (i.e. taker lifted the offer)."""
    return ~np.asarray(is_buyer_maker, dtype=bool)


# -------- Bar aggregation --------


@dataclass
class BarResult:
    bar: pd.DataFrame  # indexed by bar-start timestamp (UTC)
    n_trades_total: int
    n_bars: int


def aggregate_bars(
    df: pd.DataFrame,
    *,
    bar_freq: str = "1min",
    max_rows: int = 0,
) -> BarResult:
    """Aggregate aggTrades into time bars at the given frequency.

    Returns a DataFrame indexed by bar-start UTC with columns:
        vwap, n_trades, buy_vol, sell_vol, total_vol, signed_vol, signed_flow,
        high, low, ret_1bar (causal, computed per bar from bar vwap).
    If `max_rows > 0` and the input exceeds it, takes a deterministic
    `df.iloc[::len(df) // max_rows][:max_rows]` sample (the Q6 lesson).
    """
    work = df
    if max_rows and len(work) > max_rows:
        stride = max(1, len(work) // max_rows)
        work = work.iloc[::stride].copy()
    work = work.copy()
    work["ts"] = pd.to_datetime(work["transact_time"], unit="ms", utc=True)
    work["aggressor_buy"] = is_buy_aggressor(work["is_buyer_maker"].values)
    work["signed_qty"] = np.where(work["aggressor_buy"], work["quantity"], -work["quantity"])
    work["dollar"] = work["price"] * work["quantity"]
    work["signed_dollar"] = work["signed_qty"] * work["price"]

    grouped = work.set_index("ts").resample(bar_freq)
    bar = pd.DataFrame({
        "vwap": grouped["dollar"].sum() / grouped["quantity"].sum(),
        "n_trades": grouped["agg_trade_id"].count(),
        "buy_vol": grouped.apply(lambda g: g.loc[g["aggressor_buy"], "quantity"].sum()),
        "sell_vol": grouped.apply(lambda g: g.loc[~g["aggressor_buy"], "quantity"].sum()),
        "total_vol": grouped["quantity"].sum(),
        "signed_vol": grouped["signed_qty"].sum(),
        "signed_dollar": grouped["signed_dollar"].sum(),
        "high": grouped["price"].max(),
        "low": grouped["price"].min(),
    })
    bar = bar.dropna(subset=["vwap"])
    bar["ret_1bar"] = bar["vwap"].pct_change()
    bar["signed_flow_imbalance"] = bar["signed_vol"] / bar["total_vol"].replace(0, np.nan)
    return BarResult(bar=bar, n_trades_total=len(work), n_bars=len(bar))


# -------- Observables on bars --------


def kyle_lambda(bar: pd.DataFrame, *, min_n: int = 30) -> dict:
    """Bar-level Kyle λ from the standard OLS:

        ret_1bar_t = λ · signed_flow_t + ε_t

    λ > 0 means price moves in the direction of the flow (impact).
    """
    work = bar[["ret_1bar", "signed_flow_imbalance"]].dropna()
    if len(work) < min_n:
        return {"lambda": None, "t_stat": None, "n": int(len(work)), "valid": False}
    x = work["signed_flow_imbalance"].values
    y = work["ret_1bar"].values
    x_mean, y_mean = x.mean(), y.mean()
    x_dm, y_dm = x - x_mean, y - y_mean
    denom = float((x_dm * x_dm).sum())
    if denom == 0:
        return {"lambda": None, "t_stat": None, "n": int(len(work)), "valid": False}
    lam = float((x_dm * y_dm).sum() / denom)
    resid = y - lam * x
    sigma2 = float((resid * resid).sum()) / max(1, len(x) - 2)
    se = math.sqrt(sigma2 / denom) if denom > 0 else float("nan")
    t = lam / se if se > 0 else float("nan")
    return {"lambda": lam, "t_stat": t, "n": int(len(work)), "valid": True}


def amihud(bar: pd.DataFrame, *, min_n: int = 30) -> dict:
    """Bar-level Amihud: illiquidity = |return| / dollar volume.

    Reports mean and the Spearman correlation between |Amihud| and the
    *next* bar's absolute return (causal: |Amihud_t| vs |ret_{t+1}|).
    """
    work = bar[["ret_1bar", "signed_dollar"]].dropna()
    if len(work) < min_n:
        return {"mean": None, "spearman_abs_to_next_abs": None, "n": int(len(work)), "valid": False}
    illiq = work["ret_1bar"].abs() / work["signed_dollar"].abs().replace(0, np.nan)
    work = work.assign(illiq=illiq).dropna()
    if len(work) < min_n:
        return {"mean": None, "spearman_abs_to_next_abs": None, "n": int(len(work)), "valid": False}
    next_abs = work["ret_1bar"].abs().shift(-1)
    rho = pd.Series(work["illiq"].values).corr(pd.Series(next_abs.values), method="spearman")
    return {"mean": float(work["illiq"].mean()), "spearman_abs_to_next_abs": float(rho) if rho == rho else None, "n": int(len(work)), "valid": True}


def roll_spread(bar: pd.DataFrame, *, min_n: int = 50) -> dict:
    """Roll (1984) effective spread estimator:

        spread = 2 · √(−Cov(ΔP_t, ΔP_{t−1}))

    Uses bar vwap returns. Returns the implied half-spread.
    """
    work = bar[["vwap"]].dropna()
    if len(work) < min_n:
        return {"roll_spread_bps": None, "n": int(len(work)), "valid": False}
    dp = work["vwap"].pct_change().dropna()
    cov = dp.cov(dp.shift(1))
    if cov is None or cov >= 0:
        return {"roll_spread_bps": None, "cov": float(cov) if cov is not None else None, "n": int(len(dp)), "valid": False}
    half = 2.0 * math.sqrt(-float(cov))
    return {"roll_spread_bps": float(half * 1e4), "cov": float(cov), "n": int(len(dp)), "valid": True}


def vpin(bar: pd.DataFrame, *, n_buckets: int = 50, min_bars: int = 100) -> dict:
    """Volume-synchronised probability of informed trading (Easley et al.).

    Simplified: bucket by cumulative volume, then |buy − sell| / total per
    bucket, mean over the rolling window.
    """
    work = bar[["buy_vol", "sell_vol", "total_vol"]].dropna()
    if len(work) < min_bars:
        return {"vpin": None, "n_buckets": 0, "valid": False}
    bucket_size = work["total_vol"].sum() / n_buckets
    if bucket_size <= 0:
        return {"vpin": None, "n_buckets": 0, "valid": False}
    buy_cum, sell_cum, abs_diff, bucket_count = 0.0, 0.0, 0.0, 0
    diffs = []
    for _, row in work.iterrows():
        buy_cum += row["buy_vol"]
        sell_cum += row["sell_vol"]
        if (buy_cum + sell_cum) >= bucket_size:
            diffs.append(abs(buy_cum - sell_cum) / (buy_cum + sell_cum))
            buy_cum, sell_cum = 0.0, 0.0
            bucket_count += 1
    if not diffs:
        return {"vpin": None, "n_buckets": bucket_count, "valid": False}
    return {"vpin": float(np.mean(diffs)), "n_buckets": bucket_count, "valid": True}


# -------- Cross-asset signed-flow lead-lag --------


def cross_asset_flow_lag(
    bar_a: pd.DataFrame, bar_b: pd.DataFrame, *, max_lag: int = 5
) -> dict:
    """Spearman correlation of `signed_flow_imbalance` between two bar series,
    at lag = k bars (k from -max_lag to +max_lag).

    lag=k > 0 means bar_a leads bar_b by k bars.
    Returns per-lag rho with sample size.
    """
    a = bar_a[["signed_flow_imbalance"]].dropna()
    b = bar_b[["signed_flow_imbalance"]].dropna()
    j = a.join(b, how="inner", lsuffix="_a", rsuffix="_b")
    if len(j) < 50:
        return {"lags": {}, "valid": False}
    out = {}
    for k in range(-max_lag, max_lag + 1):
        if k > 0:
            rho = j["signed_flow_imbalance_a"].iloc[:-k].corr(
                j["signed_flow_imbalance_b"].iloc[k:], method="spearman"
            )
        elif k < 0:
            rho = j["signed_flow_imbalance_a"].iloc[-k:].corr(
                j["signed_flow_imbalance_b"].iloc[:k], method="spearman"
            )
        else:
            rho = j["signed_flow_imbalance_a"].corr(
                j["signed_flow_imbalance_b"], method="spearman"
            )
        out[str(k)] = {
            "rho": float(rho) if rho == rho else None,
            "n": int(len(j) - abs(k)),
        }
    return {"lags": out, "valid": True, "n_intersection": int(len(j))}


# -------- Cost hurdle --------


def net_3x_cost(per_bar_bps: float, cost_bps_side: float = 10.0) -> float:
    """Conservative 3× taker cost: 3 × (2 × side cost) = 6 × side cost in bps.
    Plus 0 bps impact (already baked into per_bar_bps, which is the *gross*
    bar P&L bps). Returns the per-bar net in bps.
    """
    return per_bar_bps - 6.0 * cost_bps_side


def predictive_signed_flow(bar: pd.DataFrame, *, min_n: int = 100) -> dict:
    """H-20261016-005: signed_flow_imbalance → next-bar return.

    Reports the Spearman correlation between bar-t's signed flow imbalance and
    bar-(t+1)'s return. The bar-t → bar-(t+1) link is causal (uses data ≤ t
    for the predictor, return is realised at t+1).
    """
    work = bar[["ret_1bar", "signed_flow_imbalance"]].dropna()
    if len(work) < min_n:
        return {"spearman": None, "n": int(len(work)), "valid": False}
    pred = work["signed_flow_imbalance"].iloc[:-1]
    tgt = work["ret_1bar"].iloc[1:]
    rho = pred.corr(tgt, method="spearman")
    return {"spearman": float(rho) if rho == rho else None, "n": int(len(pred)), "valid": True}


def quintile_return(bar: pd.DataFrame, *, n_quintiles: int = 5, min_n: int = 200) -> dict:
    """Sort bars by `signed_flow_imbalance` into quintiles, report mean next-bar
    return by quintile (in bps). Causal (predictor at t, return at t+1).
    """
    work = bar[["ret_1bar", "signed_flow_imbalance"]].dropna()
    if len(work) < min_n:
        return {"quintiles": None, "valid": False}
    work = work.assign(
        quintile=pd.qcut(work["signed_flow_imbalance"], n_quintiles, labels=False, duplicates="drop")
    )
    work = work.assign(next_ret=work["ret_1bar"].shift(-1)).dropna()
    means = work.groupby("quintile")["next_ret"].mean() * 1e4  # bps
    out = {f"Q{int(k)}": float(v) for k, v in means.items()}
    out["Q_max_minus_Q_min"] = float(means.max() - means.min())
    out["n"] = int(len(work))
    return {"quintiles": out, "valid": True}


# -------- Run entry point --------


def _read_btc_partitions(root: Path, *, max_rows: int = 0, seed: int = 20241016) -> pd.DataFrame:
    """Read partition parquets under `root`, deterministically subsample.

    `root` is the aggTrades root (`data/r2/market/spot/aggtrades`) or a
    per-symbol subdir; the glob uses the leaf `part-*` so both work.
    If `max_rows > 0`, take a stride-based sample during read to avoid loading
    100M+ rows just to downsample.
    """
    import pyarrow.parquet as pq

    parts = sorted(root.glob("**/part-*.parquet"))
    if not parts:
        return pd.DataFrame()
    # First pass: get total row count cheaply.
    total = 0
    for p in parts:
        total += pq.ParquetFile(p).metadata.num_rows
    if not max_rows or total <= max_rows:
        frames = [pd.read_parquet(p) for p in parts]
        return pd.concat(frames, ignore_index=True)
    # Stride sample at read time, capped at max_rows.
    stride = max(1, total // max_rows)
    frames = []
    kept = 0
    for p in parts:
        n = pq.ParquetFile(p).metadata.num_rows
        # Take every `stride`-th row from this partition.
        local_stride = max(1, stride)
        idx = np.arange(0, n, local_stride)
        f = pd.read_parquet(p).iloc[idx]
        frames.append(f)
        kept += len(f)
        if kept >= max_rows:
            break
    df = pd.concat(frames, ignore_index=True)
    if len(df) > max_rows:
        df = df.sample(n=max_rows, random_state=seed).reset_index(drop=True)
    return df


def run(symbols: list[str] | None = None, *, bar_freq: str = "1min") -> dict:
    """Entry point: load aggTrades from the on-disk R2 store, run observables.

    Returns a dict suitable for JSON serialisation.
    """
    root = Path("/root/quant-finance/aster/desk/data/r2/market/spot/aggtrades")
    if not root.exists():
        return {"status": "no_data_on_disk", "protocol": "Q21 V2", "bar_freq": bar_freq}

    # Default: BTCUSDT 2022 Q1 + 4 months (already on disk).
    by_symbol = {}
    for sym_dir in sorted(root.glob("symbol=*")):
        sym = sym_dir.name.split("=")[1]
        if symbols and sym not in symbols:
            continue
        parts = sorted(sym_dir.glob("year=*/*/part-*.parquet"))
        by_symbol[sym] = {
            "n_partitions": len(parts),
            "partitions": [str(p.relative_to(root)) for p in parts],
        }

    out: dict = {
        "protocol": "Q21 V2 (D3 GREEN)",
        "bar_freq": bar_freq,
        "by_symbol_disk": by_symbol,
        "results": {},
    }
    for sym in by_symbol:
        df = _read_btc_partitions(root / f"symbol={sym}", max_rows=2_000_000)
        if df.empty:
            out["results"][sym] = {"status": "empty"}
            continue
        br = aggregate_bars(df, bar_freq=bar_freq, max_rows=0)
        bar = br.bar
        out["results"][sym] = {
            "n_trades": br.n_trades_total,
            "n_bars": br.n_bars,
            "kyle_lambda": kyle_lambda(bar),
            "amihud": amihud(bar),
            "roll_spread": roll_spread(bar),
            "vpin": vpin(bar),
            "predictive_signed_flow": predictive_signed_flow(bar),
            "quintile_return": quintile_return(bar),
        }
    # Cross-asset (BTC ↔ ETH if both present)
    if "BTCUSDT" in out["results"] and "ETHUSDT" in out["results"]:
        df_btc = _read_btc_partitions(root / "symbol=BTCUSDT", max_rows=2_000_000)
        df_eth = _read_btc_partitions(root / "symbol=ETHUSDT", max_rows=2_000_000)
        bar_btc = aggregate_bars(df_btc, bar_freq=bar_freq, max_rows=0).bar
        bar_eth = aggregate_bars(df_eth, bar_freq=bar_freq, max_rows=0).bar
        out["cross_asset_btc_eth"] = cross_asset_flow_lag(bar_btc, bar_eth, max_lag=5)
    return out


def _json_safe(o):
    if isinstance(o, dict):
        return {k: _json_safe(v) for k, v in o.items() if not k.startswith("_")}
    if isinstance(o, list):
        return [_json_safe(x) for x in o]
    if isinstance(o, float) and (o != o or o in (float("inf"), float("-inf"))):
        return None
    if isinstance(o, (np.floating,)):
        f = float(o)
        return None if (f != f or f in (float("inf"), float("-inf"))) else f
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def main() -> None:
    res = run(["BTCUSDT", "ETHUSDT"], bar_freq="1min")
    safe = _json_safe(res)
    out_path = Path("research/atlas/q21_microstructure.json")
    out_path.write_text(json.dumps(safe, indent=2, default=str), encoding="utf-8")
    print(f"wrote {out_path}: {len(safe.get('results', {}))} symbols processed")


if __name__ == "__main__":
    main()
