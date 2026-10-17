import src.aster.research.n1_ta_alts as n
import pandas as pd
grids = []
for sym in n.SYMBOLS:
    res = n.run_symbol(sym, bootstraps=500)
    grids.append(res['grid'])
panel = pd.concat(grids, ignore_index=True)
primary = panel[panel['kind'] == 'primary']
sig = primary[primary['bh_q_asset'] < 0.05]
for _, row in sig.iterrows():
    print(row['symbol'], row['signal'], row['horizon'], 'p:', row['p_value'], 'q_asset:', row['bh_q_asset'], 'boot_ex:', row['bootstrap_excludes_zero'], 'inv_ok:', row['inverse_does_not_dominate'], 'plac_ok:', row['placebo_all_non_significant'])
    print('   placebo shift p:', row['placebo_shift_p_value'], 'timing p:', row['placebo_timing_p_value'], 'horizon p:', row['placebo_horizon_p_value'])
