"""Tests de la grille de couts a deux scenarios (taker / maker).

Chaque test porte un calcul de reference explicite.
"""

from __future__ import annotations

import math

import pandas as pd
import pytest

from aster.data.cost_grid_real import (
    MAKER_FEE_BPS,
    SIZES,
    TAKER_FEE_BPS,
    scenario_grid,
    sqrt_impact_bps,
    trade_cost,
    viable_edge_bps,
)


# --- Impact ------------------------------------------------------------------


def test_sqrt_impact_reference_value():
    # impact = sigma * sqrt(Q/ADV), en bps.  sigma horaire = 1 %, Q = 1 % de
    # l'ADV -> impact = 0,01 * 0,1 = 0,001 = 10 bps.
    assert sqrt_impact_bps(1e6, 1e8, 0.01) == pytest.approx(10.0)


def test_sqrt_impact_scales_with_the_square_root_of_size():
    one = sqrt_impact_bps(1e5, 1e7, 0.01)
    four = sqrt_impact_bps(4e5, 1e7, 0.01)
    assert four == pytest.approx(2.0 * one)


def test_sqrt_impact_is_infinite_when_there_is_no_liquidity():
    # Un seau sans ADV n'a pas de borne : rendre 0 ici ferait passer une idee
    # intraday pour gratuite.
    assert math.isinf(sqrt_impact_bps(1e5, 0.0, 0.01))


def test_sqrt_impact_uses_the_horizon_sigma_not_the_daily_one():
    # Utiliser sigma_journalier sur un trade d'une heure surestime d'un
    # facteur racine(24) = 4,899.
    hourly = sqrt_impact_bps(1e5, 1e7, 0.01)
    daily_wrong = sqrt_impact_bps(1e5, 1e7, 0.01 * math.sqrt(24))
    assert daily_wrong == pytest.approx(math.sqrt(24) * hourly, rel=1e-9)


# --- Scenarios ---------------------------------------------------------------


def test_taker_pays_the_spread_plus_two_fees():
    cost = trade_cost("taker", spread_bps=2.0, impact_bps=5.0)
    assert cost is not None, "le scenario taker est toujours disponible"
    # 2 x 10 bps de frais + 2 bps de spread + 5 bps d'impact.
    assert cost.total_bps == pytest.approx(20.0 + 2.0 + 5.0)
    assert cost.spread_bps == pytest.approx(2.0)


def test_taker_is_the_dominating_scenario_while_the_maker_fee_is_unknown():
    # La config du desk ne definit que le taker.  Tant que le palier maker
    # n'est pas confirme, on ne renvoie RIEN plutot qu'un chiffre invente.
    assert MAKER_FEE_BPS is None
    assert trade_cost("maker", spread_bps=2.0, impact_bps=5.0) is None


def test_maker_does_not_cross_the_spread_once_its_fee_is_known():
    cost = trade_cost("maker", spread_bps=2.0, impact_bps=5.0, maker_fee_bps=7.5)
    assert cost is not None
    # Le maker ne paie que ses frais et l'impact : 2 x 7,5 + 5.
    assert cost.total_bps == pytest.approx(15.0 + 5.0)
    assert cost.spread_bps == pytest.approx(0.0)
    assert "fill" in cost.fill_risk


def test_taker_fill_risk_is_none():
    cost = trade_cost("taker", 2.0, 5.0)
    assert cost is not None
    assert cost.fill_risk.startswith("none")


def test_maker_is_never_cheaper_than_taker_on_this_venue():
    # Sur un spread large comme BNB (3,1 bps), le maker ne paie que 15 bps de
    # frais contre 23 pour le taker : l'ecart vient du spread, pas des frais.
    taker = trade_cost("taker", spread_bps=3.118, impact_bps=0.0)
    maker = trade_cost("maker", spread_bps=3.118, impact_bps=0.0, maker_fee_bps=7.5)
    assert taker is not None and maker is not None
    assert maker.total_bps < taker.total_bps


def test_unknown_scenario_is_refused():
    with pytest.raises(ValueError, match="unknown scenario"):
        trade_cost("sor", 1.0, 1.0)


# --- Grille ------------------------------------------------------------------


def test_scenario_grid_only_contains_taker_while_maker_is_pending():
    hours = pd.Series({h: 1e7 for h in range(24)})
    grid = scenario_grid("BTCUSDT", spread_bps=0.003, hourly_adv=hours, sigma_hour=0.01)
    assert set(grid["scenario"].unique()) == {"taker"}
    # 4 tailles x 24 heures.
    assert len(grid) == len(SIZES) * 24


def test_scenario_grid_impact_falls_with_liquidity():
    hours = pd.Series({h: 1e8 for h in range(24)})
    grid = scenario_grid("BTCUSDT", 0.003, hours, sigma_hour=0.01)
    small = float(grid.loc[grid["notional"] == 1e5, "impact_bps"].median())
    large = float(grid.loc[grid["notional"] == 1e7, "impact_bps"].median())
    assert large == pytest.approx(10.0 * small)  # Q x100 -> impact x10


def test_scenario_grid_participation_is_the_size_over_adv():
    hours = pd.Series({h: 1e8 for h in range(24)})
    grid = scenario_grid("BTCUSDT", 0.003, hours, sigma_hour=0.01)
    row = grid[(grid["notional"] == 1e6) & (grid["utc_hour"] == 0)].iloc[0]
    assert row["participation"] == pytest.approx(0.01)


def test_scenario_grid_records_explicit_spread_sensitivity():
    hours = pd.Series({h: 1e8 for h in range(24)})
    base = scenario_grid("BTCUSDT", 1.0, hours, sigma_hour=0.0, spread_multiplier=1.0)
    conservative = scenario_grid("BTCUSDT", 1.0, hours, sigma_hour=0.0,
                                 spread_multiplier=3.0)
    stress = scenario_grid("BTCUSDT", 1.0, hours, sigma_hour=0.0, spread_multiplier=10.0)
    for grid, multiplier in ((base, 1.0), (conservative, 3.0), (stress, 10.0)):
        assert set(grid["spread_multiplier"]) == {multiplier}
        assert set(grid["spread_bps"]) == {multiplier}
        assert set(grid["proxy_spread_bps"]) == {1.0}
    # With zero impact, x3 is exactly +2 bps versus x1 and x10 +9 bps.
    one = float(base["total_bps"].iloc[0])
    three = float(conservative["total_bps"].iloc[0])
    ten = float(stress["total_bps"].iloc[0])
    assert three - one == pytest.approx(2.0)
    assert ten - one == pytest.approx(9.0)


def test_scenario_grid_refuses_a_non_positive_spread_multiplier():
    hours = pd.Series({h: 1e8 for h in range(24)})
    with pytest.raises(ValueError, match="multiplier"):
        scenario_grid("BTCUSDT", 1.0, hours, sigma_hour=0.01, spread_multiplier=0.0)


# --- Seuil de viabilite ------------------------------------------------------


def test_viable_edge_is_three_times_the_cost():
    assert viable_edge_bps(26.3) == pytest.approx(78.9)


def test_viable_edge_doubles_under_the_x2_stress():
    assert viable_edge_bps(26.3, stress=2.0) == pytest.approx(157.8)