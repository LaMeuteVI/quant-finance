"""Extract key fields from a desk backtest report.json."""
import json
import sys

d = json.load(open(sys.argv[1]))
print("report:", sys.argv[1])
print("hypothesis:", d["hypothesis_id"], "sample:", d["sample"], "passed:", d["passed"])
print("gates:", d.get("gates"))
print("base:", {k: d["base"].get(k) for k in ("n_obs", "sharpe_ann", "max_drawdown", "cagr", "turnover_ann")})
print("dsr:", d.get("statistics", {}).get("dsr"))
print("stress_x2_sharpe_ann:", d.get("stress", {}).get("costs_x2", {}).get("sharpe_ann"))
wf = d.get("walk_forward", {})
print("walk_forward:", {"n_folds": wf.get("n_folds"), "mean_sharpe_ann": wf.get("stability", {}).get("mean_sharpe_ann")})
print("capacity_max_AUM_usd:", d.get("capacity_max_AUM_usd"))
print("gross_price_pnl_ann:", d.get("gross_price_pnl_ann"))
print("funding_pnl_ann:", d.get("funding_pnl_ann"))
print("cost_drag_ann:", d.get("cost_drag_ann"))
print("lookahead:", d.get("statistics", {}).get("lookahead"))
print("signed_flow_quality:", d.get("signed_flow_quality"))
