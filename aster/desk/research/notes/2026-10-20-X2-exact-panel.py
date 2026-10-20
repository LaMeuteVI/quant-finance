"""Prove the X2 failure is a data-pipeline artefact, not a strategy result.

Aggregate aggTrades file-by-file (bounded memory) and compare the VWAP
panel against the strided sample the runner used. If the complete panel
shows realistic volatility and the strided one does not, every X2 number
is sampling noise and the hypothesis is UNTESTED, not falsified.
"""
import glob
import numpy as np
import pandas as pd

from aster.research.q21_microstructure import is_buy_aggressor

files = sorted(glob.glob(
    "data/r2/market/spot/aggtrades/symbol=BTCUSDT/year=2022/**/*.parquet",
    recursive=True))
print("partitions:", len(files))
print("sample paths:", files[:2])

# Time-bucketed aggregation across files, one file at a time.
parts = []
for f in files:
    d = pd.read_parquet(f, columns=["transact_time", "price", "quantity",
                                     "is_buyer_maker", "agg_trade_id"])
    d["ts"] = pd.to_datetime(d["transact_time"], unit="ms", utc=True)
    d["agg_buy"] = is_buy_aggressor(d["is_buyer_maker"].values)
    d["dollar"] = d["price"] * d["quantity"]
    d["sqty"] = np.where(d["agg_buy"], d["quantity"], -d["quantity"])
    g = d.set_index("ts").resample("15min")
    parts.append(pd.DataFrame({
        "dollar": g["dollar"].sum(), "qty": g["quantity"].sum(),
        "sqty": g["sqty"].sum(), "n": g["agg_trade_id"].count()}))
    del d

agg = pd.concat(parts).groupby(level=0).sum().sort_index()
bar = pd.DataFrame({
    "vwap": agg["dollar"] / agg["qty"],
    "signed_flow_imbalance": agg["sqty"] / agg["qty"].replace(0, np.nan),
    "n_trades": agg["n"]})
bar = bar.dropna(subset=["vwap"])
bar["ret_1bar"] = bar["vwap"].pct_change()

r = bar["ret_1bar"].replace([np.inf, -np.inf], np.nan).dropna()
print()
print("=== COMPLETE panel (file-by-file, exact VWAP) ===")
print(f"bars: {len(bar)}   trades/bar median: {bar['n_trades'].median():,.0f}")
print(f"ret_1bar bps: std={r.std()*1e4:.3f}")
print(f"annualised vol: {r.std()*np.sqrt(365*96)*100:.1f}%")
print(f"max |ret_1bar|: {r.abs().max()*1e4:.1f} bps")

s = bar["signed_flow_imbalance"].dropna().clip(-1, 1)
print(f"signed_flow mean={s.mean():+.4f} std={s.std():.4f} autocorr1={s.autocorr(1):+.4f}")

q80 = s.rolling(500, min_periods=250).quantile(0.80).shift(1)
above = (s >= q80).fillna(False)
print(f"frac bars above q80: {above.mean():.4f}  "
      f"(prereg assumed 0.20)")

# The quintile spread Q22 reported, recomputed on EXACT bars.
q = s.rank(pct=True, method="first")
rr = bar["ret_1bar"].reindex(q.index)
q4 = rr[q >= 0.8].mean(); q0 = rr[q <= 0.2].mean()
print()
print(f"Q4-Q0 gross per 15m bar: {(q4 - q0) * 1e4:+.2f} bps")
print(f"  (Q22 reported +7.16 bps from the strided sample)")
bar.to_parquet("/tmp/x2_exact_btc_15m.parquet")
print()
print("saved /tmp/x2_exact_btc_15m.parquet")
