import numpy as np, pandas as pd
from pathlib import Path
from aster.research.q21_microstructure import _read_btc_partitions, aggregate_bars
root = Path("/root/quant-finance/aster/desk/data/r2/market/spot/aggtrades")
raw = _read_btc_partitions(root, max_rows=4_000_000)
bar = aggregate_bars(raw, bar_freq="15min")
b = bar.bar
ret = b["ret_1bar"].replace([np.inf, -np.inf], np.nan).dropna()
n = b["n_trades"]
print(f"bars={len(b)}  trades/bar: mean={n.mean():.1f} median={n.median():.0f} min={n.min():.0f} max={n.max():.0f}")
print(f"bars with <5 trades: {(n<5).sum()} ({(n<5).mean()*100:.1f}%)")
print(f"ret_1bar bps: std={ret.std()*1e4:.3f}  annvol={ret.std()*np.sqrt(365*96)*100:.1f}%  max|ret|={ret.abs().max()*1e4:.1f}bps")
print(f"cumulative sum of ret_1bar: {b['ret_1bar'].fillna(0).sum()*100:.1f}%")
print()
print("Reference: BTC 15m real annvol in 2022 ~ 40-60%. A correct bar panel")
print("gives annvol in that range. Anything far above it is sampling noise.")
print()
print("trades/bar percentiles:")
print(n.describe())
