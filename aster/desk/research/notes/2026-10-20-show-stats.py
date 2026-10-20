"""Print the report statistics and verify required blocks exist."""
import json
import sys

d = json.load(open(sys.argv[1]))
print(json.dumps({"statistics": d.get("statistics"), "walk_forward": d.get("walk_forward"), "capacity_max_AUM_usd": d.get("capacity_max_AUM_usd")}, indent=2, default=str))
