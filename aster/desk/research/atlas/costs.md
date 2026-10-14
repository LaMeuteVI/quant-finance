# Coûts intraday — référence conservatrice

Généré le 2026-10-13 ; données de marché exploratoires arrêtées au 2024-07-01T00:00:00+00:00.

## Décision d'utilisation

Le coût de référence **taker** est : `2 × frais + impact racine carrée + spread`. Le spread de référence est `max(proxy aggTrades, un tick) × 3`. Les sensibilités ×1, ×3 et ×10 sont publiées. Cette précision est proportionnée à la décision : sur les majors, 20 bps de frais aller-retour dominent quelques ticks.

- Frais taker configurés : **10.0 bps par côté**.

- Frais maker : **non renseignés** dans la mission/configuration ; aucune valeur n'est supposée. Le scénario maker est donc explicitement **en attente**, avec risque de non-exécution à calibrer par candidate.

- Les proxies aggTrades utilisent `is_buyer_maker` comme côté agressif primaire ; le tick rule est un contrôle. Ils ne sont **pas** des effective spreads Lee–Ready canoniques, faute de midpoint quote historique.

- Corwin–Schultz, Abdi–Ranaldo et Roll high-low ne figurent pas dans cette grille : sur les barres crypto ils sont contaminés par la volatilité.


## Proxy aggTrades et contrôle tick rule — juin 2024

| Actif | Proxy venue (bps) | Tick-rule contrôle (bps) | 1 tick (bps) | Base avant sensibilité (bps) |
|---|---:|---:|---:|---:|
| BTC | 0.469 | 0.479 | 0.002 | **0.469** |
| ETH | 0.628 | 0.690 | 0.028 | **0.628** |
| BNB | 3.038 | 3.165 | 0.165 | **3.038** |
| SOL | 1.220 | 1.460 | 0.693 | **1.220** |
| XRP | 3.261 | 3.864 | 2.044 | **3.261** |
| DOGE | 1.419 | 1.978 | 0.743 | **1.419** |

## Coût taker médian par taille

Chaque cellule inclut les frais et l'impact. Les trois nombres sont les sensibilités spread **×1 / ×3 (référence) / ×10**.

| Actif | 10 k$ | 100 k$ | 1 M$ | 10 M$ |
|---|---:|---:|---:|---:|
| BTC | 21.0 / 21.9 / 25.2 | 22.1 / 23.0 / 26.3 | 25.6 / 26.5 / 29.8 | 36.7 / 37.6 / 40.9 |
| ETH | 21.4 / 22.6 / 27.0 | 22.9 / 24.2 / 28.6 | 27.9 / 29.2 / 33.6 | 43.6 / 44.9 / 49.3 |
| BNB | 25.7 / 31.8 / 53.0 | 31.4 / 37.5 / 58.8 | 49.6 / 55.7 / 76.9 | 107.0 / 113.1 / 134.4 |
| SOL | 23.4 / 25.8 / 34.4 | 28.1 / 30.5 / 39.1 | 43.0 / 45.4 / 53.9 | 90.0 / 92.4 / 101.0 |
| XRP | 25.1 / 31.6 / 54.4 | 29.1 / 35.6 / 58.4 | 41.7 / 48.2 / 71.0 | 81.4 / 88.0 / 110.8 |
| DOGE | 25.2 / 28.0 / 37.9 | 33.3 / 36.1 / 46.1 | 59.0 / 61.8 / 71.8 | 140.2 / 143.1 / 153.0 |

## BTC : coût par heure UTC, 100 k$ taker

Sensibilité ×1 / ×3 / ×10. La variation horaire vient de l'ADV et donc de l'impact ; le proxy de spread est maintenu constant par construction.

| Heure UTC | ADV médian (M$) | Impact (bps) | Total ×1 / ×3 / ×10 (bps) |
|---:|---:|---:|---:|
| 00 | 27.4 | 2.14 | 22.61 / 23.55 / 26.83 |
| 01 | 39.6 | 1.78 | 22.25 / 23.19 / 26.47 |
| 02 | 41.1 | 1.75 | 22.22 / 23.16 / 26.44 |
| 03 | 43.4 | 1.70 | 22.17 / 23.11 / 26.39 |
| 04 | 33.8 | 1.93 | 22.40 / 23.34 / 26.62 |
| 05 | 33.4 | 1.94 | 22.41 / 23.35 / 26.63 |
| 06 | 33.5 | 1.94 | 22.41 / 23.35 / 26.63 |
| 07 | 43.6 | 1.70 | 22.17 / 23.11 / 26.39 |
| 08 | 58.0 | 1.47 | 21.94 / 22.88 / 26.16 |
| 09 | 41.4 | 1.74 | 22.21 / 23.15 / 26.43 |
| 10 | 51.3 | 1.57 | 22.03 / 22.97 / 26.26 |
| 11 | 47.4 | 1.63 | 22.10 / 23.04 / 26.32 |
| 12 | 52.3 | 1.55 | 22.02 / 22.96 / 26.24 |
| 13 | 67.5 | 1.37 | 21.83 / 22.77 / 26.06 |
| 14 | 97.8 | 1.13 | 21.60 / 22.54 / 25.82 |
| 15 | 92.7 | 1.17 | 21.63 / 22.57 / 25.85 |
| 16 | 90.5 | 1.18 | 21.65 / 22.59 / 25.87 |
| 17 | 80.5 | 1.25 | 21.72 / 22.66 / 25.94 |
| 18 | 63.2 | 1.41 | 21.88 / 22.82 / 26.10 |
| 19 | 51.7 | 1.56 | 22.03 / 22.97 / 26.25 |
| 20 | 62.7 | 1.42 | 21.89 / 22.82 / 26.11 |
| 21 | 48.3 | 1.61 | 22.08 / 23.02 / 26.30 |
| 22 | 27.3 | 2.15 | 22.62 / 23.55 / 26.84 |
| 23 | 26.6 | 2.17 | 22.64 / 23.58 / 26.86 |

## Scénario maker

**Non chiffré.** Le palier maker a été laissé vide dans l'instruction utilisateur (`maker __ bps`) et n'existe pas dans `config/desk.yaml`. Même après réception du taux, un coût maker sera une borne basse : chaque candidate devra démontrer son taux de remplissage, ses annulations et sa sélection adverse.


## Limites et backlog

1. Snapshot public ccxt de top-of-book : validation opérationnelle actuelle seulement, autorisée comme exception à la coupure et sans prétention historique.

2. Quotes historiques : Tardis.dev ou équivalent pour quoted/effective spread canonique si une candidate se trouve à moins de ~2× son coût.

3. BNB reste plus large que les autres dans le proxy de juin 2024 ; son tick est vérifié sur la grille observée, et la règle ×3 reste conservatrice.

4. Ne pas raffiner davantage les coûts avant une candidate proche du seuil.


## Reproduction

```bash
uv run python -m aster.data.spread_calibration
uv run python -m aster.data.costs_publish
uv run pytest tests/test_effective_spread.py tests/test_cost_grid_real.py -q
```
