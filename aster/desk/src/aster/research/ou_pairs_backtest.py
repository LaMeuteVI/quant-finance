"""Axe 3b — Backtest pairs BTC/ETH (descriptive only, pas de ledger hypothesis).

Stratégie :
- Fenêtre d'estimation 252j pour calculer alpha, beta, sigma du spread log(BTC)-alpha-beta*log(ETH).
- Z-score = (spread - mu_252) / sigma_252.
- Long spread si z < -2 (BTC sous-évalué vs ETH), short spread si z > +2.
- Sortie si |z| < 0.5 ou après 30 jours max.
- Coût : 20 bps aller-retour par leg × 2 legs = 40 bps par round-trip.

But : mesurer la rentabilité nette d'une stratégie simple sur la période
pré-2024-07-01, sans claim de robustesse. C'est un smoke-test, pas un backtest
fiable (pas de slippage, pas de market impact, pas de slippage sur gaps).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from aster.research.ou_pairs import daily_close

ASSET_DIR = Path("research/assets")
ENTRY_Z = 2.0
EXIT_Z = 0.5
MAX_HOLD_DAYS = 30
COST_BPS_PER_LEG = 20.0  # aller-retour 2 legs = 40 bps


def rolling_pairs_backtest(
    a: pd.Series, b: pd.Series, window: int = 252
) -> pd.DataFrame:
    """Backtest rolling cointegration pairs trading."""
    log_a = np.log(a)
    log_b = np.log(b)
    n = len(log_a)
    trades = []
    position = 0  # 1 = long spread (long a, short b), -1 = short spread, 0 = flat
    entry_date = None
    entry_a = entry_b = entry_z = 0.0
    for i in range(window, n):
        # estimate on trailing window
        la = log_a.iloc[i - window:i].values
        lb = log_b.iloc[i - window:i].values
        beta, alpha, r, p, se = stats.linregress(lb, la)
        spread = la - alpha - beta * lb
        mu = spread.mean()
        sigma = spread.std()
        if sigma == 0:
            continue
        # current spread
        spread_now = log_a.iloc[i] - alpha - beta * log_b.iloc[i]
        z = (spread_now - mu) / sigma

        if position == 0:
            if z < -ENTRY_Z:
                position = 1
                entry_date = log_a.index[i]
                entry_a = a.iloc[i]
                entry_b = b.iloc[i]
                entry_z = z
            elif z > ENTRY_Z:
                position = -1
                entry_date = log_a.index[i]
                entry_a = a.iloc[i]
                entry_b = b.iloc[i]
                entry_z = z
        else:
            # check exit
            days_held = (log_a.index[i] - entry_date).days
            exit_now = abs(z) < EXIT_Z or days_held >= MAX_HOLD_DAYS
            if exit_now:
                # P&L = position * (log_a - log_a_entry) - position * beta * (log_b - log_b_entry)
                ret_a = np.log(a.iloc[i] / entry_a)
                ret_b = np.log(b.iloc[i] / entry_b)
                pnl_log = position * (ret_a - beta * ret_b)
                # cost
                cost_log = -2 * COST_BPS_PER_LEG / 10000.0  # 2 legs, each rt = 20 bps
                pnl_net = pnl_log + cost_log
                trades.append(
                    {
                        "entry_date": entry_date,
                        "exit_date": log_a.index[i],
                        "side": "long" if position == 1 else "short",
                        "beta": beta,
                        "entry_z": entry_z,
                        "exit_z": z,
                        "days_held": days_held,
                        "pnl_gross_bps": pnl_log * 10000.0,
                        "pnl_net_bps": pnl_net * 10000.0,
                    }
                )
                position = 0
    return pd.DataFrame(trades)


def main() -> None:
    btc = daily_close("BTCUSDT")
    eth = daily_close("ETHUSDT")
    common = btc.index.intersection(eth.index)
    a = btc.reindex(common).dropna()
    b = eth.reindex(common).dropna()
    trades = rolling_pairs_backtest(a, b, window=252)
    print(f"=== BTC/ETH pairs (z-entry={ENTRY_Z}, z-exit={EXIT_Z}, max-hold={MAX_HOLD_DAYS}j) ===")
    print(f"Trades: {len(trades)}")
    if len(trades) > 0:
        print(
            f"Mean gross bps = {trades['pnl_gross_bps'].mean():.2f}, "
            f"mean net bps = {trades['pnl_net_bps'].mean():.2f}"
        )
        print(f"Std net bps = {trades['pnl_net_bps'].std():.2f}")
        print(f"Win rate = {(trades['pnl_net_bps'] > 0).mean():.1%}")
        print(f"Sum net bps = {trades['pnl_net_bps'].sum():.0f}")
        # T-stat sur PnL net
        t = trades["pnl_net_bps"].mean() / (
            trades["pnl_net_bps"].std() / np.sqrt(len(trades))
        )
        print(f"T-stat net = {t:.2f}")
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    trades.to_csv(ASSET_DIR / "2026-10-14-axe-3-btc-eth-pairs-trades.csv", index=False)
    print(f"Saved {len(trades)} trades to {ASSET_DIR}/2026-10-14-axe-3-btc-eth-pairs-trades.csv")


if __name__ == "__main__":
    main()
