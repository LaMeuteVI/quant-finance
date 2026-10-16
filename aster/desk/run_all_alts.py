import src.aster.research.n1_ta_alts as n
import json


def main():
    runs = n.run_panel(bootstraps=5000)
    summary = {
        symbol: {key: value for key, value in result.items()
                 if key not in ("grid", "features", "regime")}
        for symbol, result in runs.items()
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
