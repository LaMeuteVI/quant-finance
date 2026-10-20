import numpy as np, pandas as pd
from aster.backtest.cost_model import GridCostModel
from aster.backtest.engine import run_backtest
from aster.research.x2_signed_flow import _slug
from aster.strategies.intraday_signed_flow import IntradaySignedFlow

bar = pd.read_parquet("/tmp/x2_exact_btc_15m.parquet")
slug = _slug("BTCUSDT")
flow = bar[["signed_flow_imbalance"]].rename(columns={"signed_flow_imbalance": slug})
px = bar[["vwap"]].rename(columns={"vwap": slug})
grid = GridCostModel.from_csv("research/atlas/cost-grid.csv")
ann = 365 * 96

print(f"{'hold':>5}{'turnover':>11}{'cost/RT_bps':>12}{'cost_frac/yr':>14}{'gross_frac/yr':>14}{'net_frac/yr':>13}{'survive?':>10}")
for hold in (1, 3, 6, 12, 24, 48):
    w = IntradaySignedFlow(timeframe="15min", hold_bars=hold).target_weights(px, signed_flow=flow)
    res = run_backtest(px, w, costs=grid, AUM=250_000.0, perp_legs=[], lag=1)
    to = res.turnover.fillna(0).mean() * ann
    cost = res.costs.fillna(0).mean() * ann
    gross = res.gross_returns.dropna().mean() * ann
    net = res.returns.dropna().mean() * ann
    print(f"{hold:5d}{to:11,.0f}{'':>12}{cost:14.2f}{gross:14.2f}{net:13.2f}"
          f"{'NO' if cost > gross else 'yes':>10}")
print()
print("Rule: a book survives only if annual cost drag < annual gross edge.")
print("At C1b spot (22.68 bps RT), a rule needing Q4-Q0 = 30.40 bps/bar")
print("can afford at most 30.40/22.68 = %.2f round-trips per YEAR," % (30.40/22.68))
print("i.e. one trade every %.0f bars. The prereg's hold_bars=3 gives" % (35040/(30.40/22.68)))
print("%.0f round-trips per year - about %.0fx too many." % (35040/3, (35040/3)/(30.40/22.68)))
