# Cost grid — desk rule, C1b (2026-10-20)

## Regle

1. **Spread des majors liquides** : `aggTrades` effective spread (`is_buyer_maker`, median en bps), plancher `max(1 tick, order-book snapshot)`. Les estimateurs high-low (Corwin-Schultz, CHL) sont **interdits** comme source de spread sur BTC / ETH / BNB / SOL / XRP — BACKLOG, "Closed cost work". DOGE a aussi des aggTrades. Les thin alts (LINK, SUI, NEAR, FET, XMR, AAVE) conservent `max(CHL, CS)`.
2. **Frais par instrument (C1b)** : spot taker **10 bps/cote**, USDⓈ-M perp taker **5 bps/cote** (VIP 0, sans remise). Le fee chargee suit la **jambe**, pas un taux plat.
3. **Impact** : racine carree sur la participation a l'ADV, inchange depuis la grille v1.
4. **Stress** : bareme x2 et x3 applique au cout total (frais + spread + impact).
5. **Taille** : 4 points de notional (100k / 1M / 10M / 50M) x 24 heures UTC = 1152 lignes pour 12 symbols.

## Arbitrage de venue (C1b)

La grille porte quatre colonnes supplementaires :
`fee_bps_per_side_spot`, `fee_bps_per_side_perp`, `round_trip_bps_spot`, `round_trip_bps_perp`,
calculees par `round_trip_bps_venue = 2*fee_venue + spread_bps + impact_bps` — la convention v1 du desk (le spread est symetrique, donc paye une seule fois par aller-retour) ; **seul le terme de frais change** par rapport a la grille plate, ce que verifie `test_spot_schedule_matches_the_pre_c1b_flat_column`. BTC 100k heure 0 : spot **22.95 bps**, perp **12.95 bps**, ecart exactement **10.00 bps**.

`aster.backtest.cost_model.infer_venue(column, perp_legs)` classifie chaque colonne du moteur, dans cet ordre :
1. `perp_legs` de la preregistration — si la colonne y est listee, c'est une jambe perp, sans discussion ;
2. sinon la convention de nommage du desk : perp = `<slug>:USDT` (ex. `BTC-USDT:USDT`), spot = `<slug>` nu (ex. `BTC-USDT`) ; les tickers Binance R2 (`BTCUSDT`) sont aussi perp ;
3. **defaut spot** — conservateur, car le fee spot est 2x le perp : une erreur de classification ne peut que sur-facturer, jamais sous-facturer.

Arbitre : `GridCostModel.per_trade_cost_bps(..., perp_legs=...)`, appele par `engine.run` avec le `perp_set` normalise. `ConstantCostModel` ignore l'argument (bareme plat historique).

Test : `tests/test_c1b_instrument_fees.py` — 16 tests, dont la DoD explicite « perp-only = 2x5 + spread + impact » vs « spot-only = 2x10 + spread + impact », et un ecart exactement de 10.00 bps entre les deux baremes sur les 1152 lignes.

## Coupe

Pre-2024-07-01 (fenetre d'estimation 2023-01-01 -> 2024-07-01).

## Artefacts et hash

| Fichier | Role | SHA-256 |
|---|---|---|
| `research/atlas/cost-grid.csv` | **actif (C1b)** | `c5a244bbad1e870330613ea6610479ae3aedca00aa55918db8f24da4322e63c7` |
| (v2, meme chemin a l'epoque) | rejete — pas de frais par instrument, ne plus utiliser | `818e1688ebe850e15164c81be2d8b12d5adde0510454622ef55a8215da096e04` |
| `research/atlas/cost-grid.csv.bak.v1-cs` | ancien gele — Corwin-Schultz sur les majors | `4e98d0990b0ab1d792041f5dc5c15a2eeb5ad45fddc217bdefc2b60aa7633a31` |

## Reproduction

```
uv run python research/notes/2026-10-20-C1-grid-rebuild.py
uv run pytest tests/test_c1_grid_invariant.py tests/test_c1b_instrument_fees.py
```
