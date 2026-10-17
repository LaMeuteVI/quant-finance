"""Publish the conservative intraday cost reference.

This is a research guardrail, not an execution simulator.  The spread input is
an aggTrades transaction-price proxy.  The reference applies the desk rule:
``max(proxy, one tick) * 3`` and reports x1/x3/x10 sensitivity.  A historical
quote feed is deliberately a backlog item, not a blocker.
"""
from __future__ import annotations

import math
from datetime import date

import pandas as pd

from aster.data.bars import build_bars, normalise_clock
from aster.data.cost_grid_real import MAKER_FEE_BPS, SIZES, TAKER_FEE_BPS, scenario_grid
from aster.data.r2_klines import read_local
from aster.data.spread_calibration import TICK_SIZES

CUTOFF = pd.Timestamp("2024-07-01", tz="UTC")
WINDOW_START = pd.Timestamp("2024-06-01", tz="UTC")
SENSITIVITIES = (1.0, 3.0, 10.0)


def hourly_inputs(symbol: str) -> tuple[pd.Series, float]:
    """Median hourly notional ADV and horizon-matched hourly sigma, pre-cutoff."""
    repaired = normalise_clock(read_local(symbol))
    frame = repaired[0] if isinstance(repaired, tuple) else repaired
    frame = frame[(frame.index >= WINDOW_START) & (frame.index < CUTOFF)]
    hourly = build_bars(frame, "1h")
    daily = build_bars(frame, "1d")
    sigma_h = float(daily["close"].pct_change().std()) / math.sqrt(24.0)
    adv = hourly["quote_volume"].groupby(hourly.index.hour).median()
    return adv, sigma_h


def bps_one_tick(symbol: str, price: float) -> float:
    return TICK_SIZES[symbol] / price * 1e4


def f(value: float, decimals: int = 3) -> str:
    return f"{value:,.{decimals}f}"


def main() -> int:
    measured = pd.read_csv("research/atlas/effective-spread.csv").set_index("symbol")
    lines = [
        "# Coûts intraday — référence conservatrice\n",
        f"Généré le {date.today().isoformat()} ; données de marché exploratoires arrêtées au {CUTOFF.isoformat()}.\n",
        "## Décision d'utilisation\n",
        "Le coût de référence **taker** est : `2 × frais + impact racine carrée + spread`. "
        "Le spread de référence est `max(proxy aggTrades, un tick) × 3`. Les sensibilités ×1, ×3 et ×10 sont publiées. "
        "Cette précision est proportionnée à la décision : sur les majors, 20 bps de frais aller-retour dominent quelques ticks.\n",
        f"- Frais taker configurés : **{TAKER_FEE_BPS:.1f} bps par côté**.\n",
        "- Frais maker : **non renseignés** dans la mission/configuration ; aucune valeur n'est supposée. "
        "Le scénario maker est donc explicitement **en attente**, avec risque de non-exécution à calibrer par candidate.\n",
        "- Les proxies aggTrades utilisent `is_buyer_maker` comme côté agressif primaire ; le tick rule est un contrôle. "
        "Ils ne sont **pas** des effective spreads Lee–Ready canoniques, faute de midpoint quote historique.\n",
        "- Corwin–Schultz, Abdi–Ranaldo et Roll high-low ne figurent pas dans cette grille : sur les barres crypto ils sont contaminés par la volatilité.\n",
        "\n## Proxy aggTrades et contrôle tick rule — juin 2024\n",
        "| Actif | Proxy venue (bps) | Tick-rule contrôle (bps) | 1 tick (bps) | Base avant sensibilité (bps) |",
        "|---|---:|---:|---:|---:|",
    ]
    bases: dict[str, float] = {}
    for symbol, row in measured.iterrows():
        proxy = float(row["median_bps"])
        tick = bps_one_tick(symbol, float(row["reference_price"]))
        base = max(proxy, tick)
        bases[symbol] = base
        control = float(row["tick_rule_median_bps"])
        lines.append(f"| {symbol.replace('USDT','')} | {f(proxy)} | {f(control)} | {f(tick)} | **{f(base)}** |")

    lines += [
        "\n## Coût taker médian par taille\n",
        "Chaque cellule inclut les frais et l'impact. Les trois nombres sont les sensibilités spread **×1 / ×3 (référence) / ×10**.\n",
        "| Actif | 10 k$ | 100 k$ | 1 M$ | 10 M$ |",
        "|---|---:|---:|---:|---:|",
    ]
    grids: dict[tuple[str, float], pd.DataFrame] = {}
    for symbol in measured.index:
        adv, sigma_h = hourly_inputs(symbol)
        cells: list[str] = []
        for size in SIZES:
            values = []
            for multiplier in SENSITIVITIES:
                grid = scenario_grid(symbol, bases[symbol], adv, sigma_h,
                                     spread_multiplier=multiplier)
                grids[(symbol, multiplier)] = grid
                value = float(grid.loc[grid["notional"] == size, "total_bps"].median())
                values.append(f(value, 1))
            cells.append(" / ".join(values))
        lines.append(f"| {symbol.replace('USDT','')} | " + " | ".join(cells) + " |")

    lines += [
        "\n## BTC : coût par heure UTC, 100 k$ taker\n",
        "Sensibilité ×1 / ×3 / ×10. La variation horaire vient de l'ADV et donc de l'impact ; le proxy de spread est maintenu constant par construction.\n",
        "| Heure UTC | ADV médian (M$) | Impact (bps) | Total ×1 / ×3 / ×10 (bps) |",
        "|---:|---:|---:|---:|",
    ]
    btc_grids = {m: grids[("BTCUSDT", m)].query("notional == 100000.0").set_index("utc_hour")
                 for m in SENSITIVITIES}
    for hour in range(24):
        row = btc_grids[3.0].loc[hour]
        totals = " / ".join(f(float(btc_grids[m].loc[hour, "total_bps"]), 2) for m in SENSITIVITIES)
        lines.append(f"| {hour:02d} | {f(float(row['adv_usd']) / 1e6, 1)} | {f(float(row['impact_bps']), 2)} | {totals} |")

    lines += [
        "\n## Scénario maker\n",
        "**Non chiffré.** Le palier maker a été laissé vide dans l'instruction utilisateur (`maker __ bps`) et n'existe pas dans `config/desk.yaml`. "
        "Même après réception du taux, un coût maker sera une borne basse : chaque candidate devra démontrer son taux de remplissage, ses annulations et sa sélection adverse.\n",
        "\n## Limites et backlog\n",
        "1. Snapshot public ccxt de top-of-book : validation opérationnelle actuelle seulement, autorisée comme exception à la coupure et sans prétention historique.\n",
        "2. Quotes historiques : Tardis.dev ou équivalent pour quoted/effective spread canonique si une candidate se trouve à moins de ~2× son coût.\n",
        "3. BNB reste plus large que les autres dans le proxy de juin 2024 ; son tick est vérifié sur la grille observée, et la règle ×3 reste conservatrice.\n",
        "4. Ne pas raffiner davantage les coûts avant une candidate proche du seuil.\n",
        "\n## Reproduction\n",
        "```bash\nuv run python -m aster.data.spread_calibration\nuv run python -m aster.data.costs_publish\nuv run pytest tests/test_effective_spread.py tests/test_cost_grid_real.py -q\n```\n",
    ]
    with open("research/atlas/costs.md", "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    print("wrote research/atlas/costs.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
