"""Verify the final X2 desk report against the completion contract."""
from __future__ import annotations

import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
d = json.loads(path.read_text())
required_top = [
    "hypothesis_id", "sample", "gates", "checks", "base", "stress",
    "statistics", "gross_price_pnl_ann", "funding_pnl_ann",
    "capacity_max_AUM_usd", "walk_forward", "signed_flow_quality",
]
missing = [k for k in required_top if k not in d]
assert not missing, missing
assert d["sample"] == "dev"
assert d["hypothesis_id"] == "H-20261020-024"
for key in ("min_obs", "sharpe_ann_min", "max_drawdown_floor", "dsr_min", "stress_sharpe_ann_min"):
    assert key in d["gates"], key
for key in ("sharpe_ann", "max_drawdown"):
    assert key in d["base"], key
assert "dsr" in d["statistics"]
assert "costs_x2" in d["stress"]
assert "sharpe_ann" in d["stress"]["costs_x2"]
assert d["walk_forward"]["n_folds"] >= 4
assert "stability" in d["walk_forward"]
q = d["signed_flow_quality"]
assert q["cutoff_exclusive"] == "2024-07-01T00:00:00+00:00"
assert q["all_values_in_range"] is True
assert q["active_rows"] == 11520
assert d["passed"] is False
assert d["checks"]["lookahead_clean"] is True
print("CONTRACT PASS")
print("report:", path)
print("sharpe_ann:", d["base"]["sharpe_ann"])
print("dsr:", d["statistics"]["dsr"])
print("stress_x2_sharpe_ann:", d["stress"]["costs_x2"]["sharpe_ann"])
print("walk_forward_folds:", d["walk_forward"]["n_folds"])
print("walk_forward_mean:", d["walk_forward"]["stability"]["mean_sharpe_ann"])
print("capacity_usd:", d["capacity_max_AUM_usd"])
print("funding_pnl_ann:", d["funding_pnl_ann"])
print("gross_price_pnl_ann:", d["gross_price_pnl_ann"])
print("active_flow_rows:", q["active_rows"])
