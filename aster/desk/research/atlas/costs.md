# Couts de transaction — atlas (v2, 2026-10-20)

Regeneration conforme a la regle du desk (BACKLOG): **high-low / Corwin-Schultz interdit comme estimateur de spread pour les actifs majeurs liquides**. Sources:

- Spread majors liquides (BTC, ETH, BNB, SOL, XRP) : **aggTrades effective spread** (median bps, `is_buyer_maker` side rule, source `binance_is_buyer_maker` dans `research/atlas/effective-spread.csv`), plancher = max(1 tick, spread carnet `research/atlas/current-orderbook-snapshot.csv`).

- Spread thin alts (LINK, SUI, NEAR, FET, XMR, AAVE, DOGE) : formule `max(Corwin-Schultz, CHL)` du desk (work ferme anterieur), source marquee `thin_alt_cs_chl_max` dans la colonne `spread_source`. High-low = diagnostique de stress, pas un input.

- Frais spot taker : 10 bps/side (Binance VIP 0). Frais USDⓈ-M taker : 5 bps/side (reference).

- Impact : racine carree (`sigma_horizon * sqrt(participation)`), meme formule que la version v1, conservee.

- Stresses x2/x3 inchanges (multiplicateur sur la ligne de cout).

- Coupe : strictement pre-2024-07-01 (fenetre d'estimation 2023-01-01 -> 2024-07-01, voir section 1 de v1).

- **Aucune strategie n'a ete re-tournee avec cette grille au moment de l'ecriture de ce fichier.** Le SHA-256 ci-dessous fige la grille AVANT toute relecture.


## Artefacts et hash


- `research/atlas/cost-grid.csv` (nouveau)  : SHA-256 `818e1688ebe850e15164c81be2d8b12d5adde0510454622ef55a8215da096e04`

- `research/atlas/cost-grid.csv.bak.v1-cs` (ancien, gele) : SHA-256 `4e98d0990b0ab1d792041f5dc5c15a2eeb5ad45fddc217bdefc2b60aa7633a31`


## Reproduction


```
uv run python research/notes/2026-10-20-C1-grid-rebuild.py
```

Les `effective-spread.csv` et `effective-spread-hourly.csv` sont regenres par `uv run desk data build-effective-spread` ; le carnet via `uv run desk data orderbook-snapshot`.
