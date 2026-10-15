import src.aster.research.n1_ta_alts as n
import pandas as pd
grids = []
for sym in n.SYMBOLS:
    res = n.run_symbol(sym, bootstraps=500)
    grids.append(res['grid'])
panel = pd.concat(grids, ignore_index=True)
primary = panel[panel['kind'] == 'primary']
print('Primary rows:', len(primary))
print('bh_q_asset < 0.05:', (primary['bh_q_asset'] < 0.05).sum())
print('bootstrap_excludes_zero:', primary['bootstrap_excludes_zero'].sum())
print('inverse_does_not_dominate:', primary['inverse_does_not_dominate'].sum())
print('placebo_all_non_significant:', primary['placebo_all_non_significant'].sum())
print('retention before panel:', primary['retention'].sum())
print(primary[primary['bh_q_asset'] < 0.05][['symbol', 'signal', 'horizon', 'p_value', 'bh_q_asset', 'bootstrap_excludes_zero', 'inverse_does_not_dominate', 'placebo_all_non_significant']])
