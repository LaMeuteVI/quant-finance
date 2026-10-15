import src.aster.research.n1_ta_alts as n
import json

def main():
    summary = {}
    for symbol in n.SYMBOLS:
        res = n.run_symbol(symbol, bootstraps=5000)
        summary[symbol] = {k: v for k, v in res.items() if k not in ('grid', 'features', 'regime')}
    print(json.dumps(summary, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
