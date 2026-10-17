"""Tests du spread effectif (tick rule / Lee-Ready).

Référence `quant-verification` : la classification et la formule du spread sont
confrontées à des séries construites dont la réponse est calculable à la main.

La série de référence ci-dessous est un marché à un seul prix avec un bounce
exact de 5 ticks (chaque achat à P+5, chaque vente à P-5) :

    P      = 100
    half   = 5
    vente  -> 95
    achat  -> 105

Le spread aller-retour attendu est 2 x 10 = 20 unités, soit 20 / 100 = 20 %
= 2000 bps.  C'est volontairement énorme et sans ambiguïté : si le code calcule
autre chose, il est faux.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from aster.data.effective_spread import (
    block_spreads,
    classify_trades,
    effective_spread,
    hourly_spread_from_trades,
    read_agg_trades,
    summarise_spread,
)

# --- 1. Classification -------------------------------------------------------


def test_tick_up_is_buy_and_tick_down_is_sell():
    prices = pd.Series([100.0, 101.0, 100.5])
    side = classify_trades(prices)
    # Le premier trade n'a pas de prix precedent : il n'est pas classe.
    assert side.iloc[0] == 0
    # 100 -> 101 est une hausse : acheteur.
    assert side.iloc[1] == 1
    # 101 -> 100.5 est une baisse : vendeur.
    assert side.iloc[2] == -1


def test_quote_rule_keeps_the_last_sign_through_a_flat_stretch():
    # Le cas que le tick rule seul rate : une serie plate apres une hausse.
    prices = pd.Series([100.0, 101.0, 101.0, 101.0, 100.0])
    side = classify_trades(prices)
    assert side.tolist() == [0, 1, 1, 1, -1]


def test_flat_tape_is_not_a_reversal():
    # Une pause n'inverse pas le sens : c'est le point de la quote rule.
    prices = pd.Series([100.0, 99.0, 99.0, 99.0])
    side = classify_trades(prices)
    assert side.tolist() == [0, -1, -1, -1]


def test_first_trade_is_unclassified_not_a_buy():
    prices = pd.Series([100.0, 100.0, 101.0])
    assert classify_trades(prices).iloc[0] == 0


# --- 2. Formule du spread effectif ------------------------------------------


def _bounce_tape(n: int = 400, *, half_spread: float = 5.0, price: float = 100.0,
                 seed: int = 0) -> pd.Series:
    """A single-price market bouncing exactly +/- half_spread, alternating."""
    rng = np.random.default_rng(seed)
    side = np.where(rng.random(n) > 0.5, 1.0, -1.0)
    values = price + side * half_spread
    return pd.Series(values)


def test_effective_spread_recovers_the_exact_bounce():
    tape = _bounce_tape(half_spread=5.0)
    report = effective_spread(tape, symbol="TEST")
    # Achats a 105, ventes a 95 -> 2 x (105 - 95) / 100 = 20 % = 2000 bps.
    assert report.mean_buy_price == pytest.approx(105.0)
    assert report.mean_sell_price == pytest.approx(95.0)
    assert report.spread_bps == pytest.approx(2000.0)
    assert report.n_trades == 400


def test_effective_spread_scales_linearly_with_the_bounce():
    for half in (0.5, 1.0, 5.0):
        report = effective_spread(_bounce_tape(half_spread=half), symbol="TEST")
        # 2 x (P+half - (P-half)) / P = 4 x half / P, en bps.
        assert report.spread_bps == pytest.approx(4.0 * half / 100.0 * 1e4)


def test_effective_spread_refuses_a_one_sided_window():
    # Un marche qui ne fait que des achats n'a pas de spread identifiable.
    # Renvoyer 0 ferait passer une idee intraday pour gratuite : c'est le pire
    # mode de defaillance possible, donc on leve.
    buys_only = pd.Series([100.0 + i for i in range(50)])
    with pytest.raises(ValueError, match="not identifiable"):
        effective_spread(buys_only, symbol="TEST")


def test_effective_spread_refuses_an_incoherent_side_classification():
    # Un spread effectif negatif ne peut pas survenir sur un tape reel : le
    # tick rule et le prix sont produits par le meme processus.  Il survient
    # quand la classification est INCOHERENTE avec les prix, exactement le bug
    # que le garde-fou doit attraper avant qu'un cout negatif ne fuite dans
    # la grille.  On le declenche donc par un `side` explicite et faux.
    prices = pd.Series([100.0, 101.0, 100.0, 101.0] * 60)   # tape neutre
    incoherent = pd.Series([1, -1] * 120)                     # "buy" sur les prix bas
    with pytest.raises(ValueError, match="negative effective spread"):
        effective_spread(prices, side=incoherent, symbol="TEST")


def test_effective_spread_refuses_a_non_positive_mid():
    # Un tape qui vit sous zero (ou autour de zero) n'est pas un marche et la
    # normalisation bps n'a aucun sens.  On construit un tape a deux cotes qui
    # reste negatif : 30 trades sous zero, alternes.
    prices = pd.Series([-100.0, -101.0] * 30)
    with pytest.raises(ValueError, match="non-positive mid price"):
        effective_spread(prices, symbol="TEST")


def test_effective_spread_needs_a_minimum_sample():
    with pytest.raises(ValueError, match="at least two trades"):
        effective_spread(pd.Series([100.0]))


def test_block_spreads_prefers_venue_aggressor_side_when_available():
    # Prix constants : le tick rule ne peut rien classifier.  Le flag de venue,
    # lui, identifie deux cotes au meme prix : spread nul, mais estimateur
    # identifiable et causal.
    index = pd.date_range("2024-06-01", periods=40, freq="s", tz="UTC")
    prices = pd.Series(100.0, index=index)
    sides = pd.Series([1, -1] * 20, index=index)
    blocks = block_spreads(prices, index, side=sides, block="1min", symbol="TEST")
    assert float(blocks.iloc[0]) == pytest.approx(0.0)


def test_block_spreads_refuses_misaligned_venue_side():
    index = pd.date_range("2024-06-01", periods=40, freq="s", tz="UTC")
    with pytest.raises(ValueError, match="price and side"):
        block_spreads(pd.Series(100.0, index=index), index, side=pd.Series([1, -1]))


def test_venue_side_and_tick_rule_are_separate_estimators():
    # C'est intentionnel : le flag venue est la source primaire et le tick rule
    # est un controle. Cette serie contient une classification de venue opposee
    # a la direction des ticks, donc les deux estimations doivent diverger.
    index = pd.date_range("2024-06-01", periods=60, freq="s", tz="UTC")
    prices = pd.Series(100.0 + np.arange(60) * 0.01, index=index)
    side = pd.Series([-1, 1] * 30, index=index)
    venue = block_spreads(prices, index, side=side, block="1min", symbol="TEST")
    with pytest.raises(ValueError, match="two-sided flow"):
        block_spreads(prices, index, block="1min", symbol="TEST")
    assert len(venue) == 1


def test_block_spreads_takes_cost_magnitude_for_venue_side():
    # Un bloc de vente peut deriver vers le bas et donner buy_mean < sell_mean.
    # Un cout ne peut pas etre negatif : le proxy prend la magnitude.
    index = pd.date_range("2024-06-01", periods=40, freq="s", tz="UTC")
    prices = pd.Series([101.0] * 20 + [99.0] * 20, index=index)
    sides = pd.Series([1] * 20 + [-1] * 20, index=index)
    blocks = block_spreads(prices, index, side=sides, block="1min", symbol="TEST")
    assert float(blocks.iloc[0]) == pytest.approx(400.0)


# --- 3. Lecture des archives Binance -----------------------------------------


def test_read_agg_trades_parses_a_headerless_zip(tmp_path):
    # Format reel Binance Vision : sans en-tete, prix en colonne 2 (index 1),
    # timestamp en millisecondes colonne 6 (index 5).
    import zipfile

    path = tmp_path / "agg.zip"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(
            "BTCUSDT-aggTrades-2024-06-01.csv",
            "1,100.50,0.01,1,1,1717200000000,True,120.0,1\n"
            "2,100.60,0.02,1,1,1717200001000,False,120.0,1\n",
        )
    frame = read_agg_trades(str(path))
    assert list(frame.columns) == ["price", "ts", "aggressor_side"]
    assert frame["price"].tolist() == [100.50, 100.60]
    # Binance `is_buyer_maker=True` means buyer was passive => sell aggressor.
    assert frame["aggressor_side"].tolist() == [-1, 1]
    assert str(frame["ts"].dt.tz) == "UTC"
    assert frame["ts"].iloc[0] == pd.Timestamp("2024-06-01 00:00:00", tz="UTC")


# --- 5. L'estimateur de production : block_spreads ---------------------------


def _tick_walk(n, seed, tick=0.0001, mid=0.4965):
    """A price that moves one tick at a time, up and down.

    The DGP must have MOMENTUM for the tick rule to work.  An i.i.d. draw on
    two ticks carries no trend, so the classifier falls back on the quote rule
    for half the tape and the measured spread doubles to ~4 ticks: measured
    8.06 bps against 3.89 bps for the walk, on identical noise.  A random walk
    of ticks is the honest benchmark and it matches the real tape: 1.93 ticks
    here against 1.88 ticks measured on XRPUSDT June 2024.
    """
    rng = np.random.default_rng(seed)
    index = pd.date_range("2024-06-01", periods=n, freq="s", tz="UTC")
    steps = rng.choice([-1.0, 1.0], n)
    return pd.Series(mid + tick * np.cumsum(steps), index=index), index


def test_block_spreads_recovers_a_two_tick_market():
    # Référence XRPUSDT juin 2024 : tick 0.0001, prix ~0.4965, donc 1 tick =
    # 2.014 bps.  Une marche par ticks doit ressortir ~2 ticks.
    tape, index = _tick_walk(600, seed=21)
    blocks = block_spreads(tape, index, block="1min", symbol="TEST")
    assert len(blocks) > 0
    measured = float(blocks.median())
    ticks = measured / (0.0001 / 0.4965 * 1e4)
    assert ticks == pytest.approx(2.0, rel=0.35), (
        f"mesure {ticks:.2f} ticks, la reference tape vaut 1.88")


def test_block_spreads_is_flat_across_a_drifting_market():
    # Le test qui distingue le vrai estimateur du naive.  Le tape derive de
    # -5 % en 15 minutes tout en marchant par ticks.  L'estimateur par blocs
    # doit rester proche du tick ; la comparaison naive buy-mean contre
    # sell-mean absorbe la derive et sort a plusieurs centaines de bps
    # (127 bps mesures sur le vrai XRP le 2024-06-04, contre 3,79 vrais).
    tick, mid = 0.0001, 0.4965
    rng = np.random.default_rng(22)
    n = 900
    index = pd.date_range("2024-06-04 04:00", periods=n, freq="s", tz="UTC")
    steps = rng.choice([-1.0, 1.0], n)
    drift = np.linspace(0.0, -0.05, n)
    tape = pd.Series(mid * (1.0 + drift) + tick * np.cumsum(steps), index=index)
    blocks = block_spreads(tape, index, block="1min", symbol="TEST")
    measured = float(blocks.median())
    ticks = measured / (0.0001 / 0.4965 * 1e4)
    assert ticks == pytest.approx(2.0, rel=0.5), (
        f"l'estimateur par blocs n'a pas retire la derive: {ticks:.2f} ticks")
    # ... and the naive version is dramatically worse on the very same tape.
    naive = effective_spread(tape, symbol="TEST").spread_bps
    assert abs(naive) > 3.0 * abs(measured), (
        "le test suppose que la version naive est bien moins fiable ; "
        "si elle ne l'est plus, l'estimateur par blocs n'a plus d'interet")


def test_block_spreads_drops_blocks_without_two_sided_flow():
    # Un bloc qui ne fait que des achats n'a pas de spread identifiable.
    index = pd.date_range("2024-06-01", periods=120, freq="s", tz="UTC")
    tape = pd.Series(100.0 + np.arange(120) * 0.01, index=index)  # montee pure
    with pytest.raises(ValueError, match="two-sided flow"):
        block_spreads(tape, index, block="1min", symbol="TEST")


def test_block_spreads_rejects_misaligned_inputs():
    with pytest.raises(ValueError, match="must align"):
        block_spreads(pd.Series([1.0, 2.0]), pd.Series([pd.Timestamp("2024-01-01")]))


def test_summarise_spread_reports_ticks():
    blocks = pd.Series([4.0, 4.1, 3.9, 4.2], index=pd.date_range("2024-06-01", periods=4,
                                                                  freq="min", tz="UTC"))
    stats = summarise_spread(blocks, reference_price=0.4965, tick_size=0.0001)
    assert stats["n_blocks"] == 4
    # médiane de [4.0, 4.1, 3.9, 4.2] = 4.05 (moyenne des deux centraux).
    assert stats["median_bps"] == pytest.approx(4.05)
    # 1 tick = 0.0001/0.4965*1e4 = 2.014 bps, donc 4.05 bps ~ 2.01 ticks.
    assert stats["ticks_median"] == pytest.approx(2.01, rel=0.02)


def test_hourly_spread_covers_every_hour_with_two_sided_flow():
    index = pd.date_range("2024-06-01", periods=24 * 4, freq="1h", tz="UTC")
    rng = np.random.default_rng(5)
    # 4 h de data -> 1 trade par heure, largement sous le minimum de 20 trades
    # et le seuil de 10 achats + 10 ventes par heure.  On construit 60 trades
    # par heure pour que chaque seau soit identifiable.
    trades_per_hour = 60
    stamps = index.repeat(trades_per_hour)
    # Bounce de 0.5 unite sur 100 -> 4 x 0.5 / 100 = 2 % = 200 bps.
    prices = pd.Series(100.0 + rng.choice([-0.5, 0.5], len(stamps)), index=stamps)
    report = hourly_spread_from_trades(prices, stamps, symbol="TEST")
    assert len(report) == 24
    assert (report > 0).all()
    assert report.median() == pytest.approx(200.0, rel=0.35)


def test_hourly_spread_drops_hours_without_two_sided_flow():
    index = pd.date_range("2024-06-01", periods=24, freq="1h", tz="UTC")
    prices = pd.Series(100.0, index=index)  #aucun tick : rien a classifier
    with pytest.raises(ValueError, match="two-sided flow"):
        hourly_spread_from_trades(prices, index, symbol="TEST")


def test_hourly_spread_rejects_misaligned_inputs():
    with pytest.raises(ValueError, match="must align"):
        hourly_spread_from_trades(pd.Series([1.0, 2.0]), pd.Series([pd.Timestamp("2024-01-01")]))