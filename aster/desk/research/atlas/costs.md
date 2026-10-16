# Couts de transaction intraday — l'atlas du desk

Genere le 2026-10-16 par `src/aster/data/costs_table.py` (modele : `src/aster/data/costs.py`) sur donnees auditees **pre-cutoff**.

- Fenetre d'estimation : 2023-01-01 -> 2024-07-01 (strictement anterieure au cutoff `2024-07-01T00:00:00Z`).

- Source : klines 1m R2 spot, 9,084,979 minutes au total, horloge normalisee.

- Frais : 10 bps par cote (Binance spot taker). Un algo maker doit passer son propre taux.

- Stress : le plan exige de survivre a un cout x2 ; la colonne `x2` est ce scenario.


> **Regle du desk** (§8) : le timeframe minimum d'une idee est celui ou le gain brut moyen par trade depasse **3x** le cout aller-retour de la ligne correspondante.


## 1. Estimation du spread par actif

Trois estimateurs independants. Le desk retient le **maximum**, jamais la moyenne : Corwin-Schultz et Roll sous-estiment systematiquement un spread serre (biais mesure vers le bas, cf. `tests/test_costs.py`), donc leur moyenne flatterait chaque idee intraday.


| Actif | CHL | Corwin-Schultz | Roll | **Retenu** | sigma/j | ADV 1m | minutes gelees |
|---|---:|---:|---:|---:|---:|---:|---:|
| BTC | 1.76 | 1.34 | 1.45 | **1.76** | 0.0251 | 0.76 M$ | 0.01 % |
| ETH | 2.05 | 1.45 | 2.53 | **2.53** | 0.0276 | 0.30 M$ | 0.01 % |
| SOL | 4.72 | 4.21 | 4.92 | **4.92** | 0.0499 | 0.08 M$ | 0.03 % |
| AAVE | 3.96 | 2.45 | 4.52 | **4.52** | 0.0412 | 0.00 M$ | 5.58 % |
| DOGE | 3.45 | 2.74 | 1.85 | **3.45** | 0.0412 | 0.03 M$ | 0.02 % |
| SUI | 4.88 | 3.70 | 0.00 | **4.88** | 0.0526 | 0.02 M$ | 0.35 % |
| XRP | 2.89 | 2.42 | 0.00 | **2.89** | 0.0441 | 0.08 M$ | 0.01 % |
| BNB | 3.15 | 3.11 | 3.03 | **3.15** | 0.0268 | 0.05 M$ | 0.01 % |
| LINK | 3.45 | 2.48 | 0.00 | **3.45** | 0.0397 | 0.02 M$ | 0.22 % |
| NEAR | 4.75 | 3.52 | 3.36 | **4.75** | 0.0537 | 0.01 M$ | 1.57 % |
| XMR | 3.16 | 2.04 | 5.07 | **5.07** | 0.0304 | 0.00 M$ | 6.49 % |
| FET | 5.98 | 4.49 | 9.13 | **9.13** | 0.0680 | 0.01 M$ | 1.43 % |

> **Attention a l'horizon.** Ce tableau mesure le spread sur des barres **1 minute**, le fin du fin. La section 3 mesure sur des barres **1 heure** et trouve 14 a 27 bps, soit ~10x plus. Un spread n'est pas une propriete de l'actif: c'est une propriete de l'actif **a l'echelle ou on regarde**. Citer 1,76 bps pour justifier d'un trade intraday serait une faute. Pour un candidat 1m, la section 3 reste la borne prudente.


## 2. Cout aller-retour par taille (bps, toutes heures melangees)

`frais x2 + spread + impact racine carree`. L'impact utilise le sigma de l'horizon **effectivement trade** : c'est lui, et non le sigma journalier, qui borne le cout d'un trade de 15 minutes.


| Actif | 10 k$ | 100 k$ | 1 M$ | 10 M$ |
|---|---:|---:|---:|---:|
| BTC | 42.8 | 53.1 | 83.6 | 138.9 |
| ETH | 48.8 | 65.6 | 114.3 | 205.6 |
| SOL | 91.0 | 142.7 | 312.3 | 617.0 |
| AAVE | 159.6 | 374.0 | 1,057.1 | 2,293.0 |
| DOGE | 85.8 | 156.9 | 384.6 | 796.9 |
| SUI | 130.2 | 250.6 | 635.3 | 1,331.4 |
| XRP | 72.2 | 121.5 | 277.3 | 559.5 |
| BNB | 59.8 | 93.7 | 204.2 | 405.6 |
| LINK | 100.7 | 194.0 | 490.3 | 1,029.5 |
| NEAR | 139.5 | 293.9 | 780.5 | 1,660.3 |
| XMR | 115.1 | 251.9 | 686.5 | 1,472.3 |
| FET | 178.4 | 385.5 | 1,037.7 | 2,219.2 |

## 3. Cout aller-retour par heure UTC (BTC, 100 k$)

L'intraday se joue ou se meurt sur la dispersion horaire. Une idee dont le cout double entre 02h et 14h UTC n'est pas une idee, c'est un profil.


| Heure UTC | ADV horaire | spread | impact | **total** | x2 stress |
|---:|---:|---:|---:|---:|---:|
00 | 43.0 M$ | 17.43 | 2.47 | **42.4** | 84.7 |
01 | 50.9 M$ | 20.92 | 2.27 | **45.5** | 90.9 |
02 | 48.6 M$ | 18.55 | 2.32 | **43.2** | 86.4 |
03 | 45.3 M$ | 16.49 | 2.40 | **41.3** | 82.6 |
04 | 39.2 M$ | 14.52 | 2.58 | **39.7** | 79.4 |
05 | 38.2 M$ | 15.02 | 2.62 | **40.2** | 80.5 |
06 | 38.9 M$ | 14.01 | 2.59 | **39.2** | 78.4 |
07 | 42.0 M$ | 14.47 | 2.50 | **39.5** | 78.9 |
08 | 54.0 M$ | 15.67 | 2.20 | **40.1** | 80.1 |
09 | 51.5 M$ | 18.04 | 2.25 | **42.5** | 85.1 |
10 | 49.9 M$ | 16.63 | 2.29 | **41.2** | 82.4 |
11 | 50.2 M$ | 16.44 | 2.28 | **41.0** | 82.0 |
12 | 51.8 M$ | 16.98 | 2.25 | **41.5** | 82.9 |
13 | 67.1 M$ | 19.56 | 1.97 | **43.5** | 87.0 |
14 | 78.6 M$ | 23.07 | 1.82 | **46.7** | 93.4 |
15 | 94.8 M$ | 26.66 | 1.66 | **50.0** | 100.0 |
16 | 100.3 M$ | 24.56 | 1.62 | **47.8** | 95.6 |
17 | 82.8 M$ | 26.32 | 1.78 | **49.9** | 99.8 |
18 | 72.5 M$ | 22.23 | 1.90 | **46.0** | 92.0 |
19 | 66.0 M$ | 21.63 | 1.99 | **45.6** | 91.2 |
20 | 62.7 M$ | 23.27 | 2.04 | **47.4** | 94.7 |
21 | 54.2 M$ | 21.07 | 2.20 | **45.5** | 90.9 |
22 | 42.3 M$ | 18.17 | 2.49 | **43.1** | 86.3 |
23 | 40.5 M$ | 17.09 | 2.54 | **42.2** | 84.3 |

**Constat** : sur BTC a 100 k$, le cout aller-retour va de 39.2 bps (06h UTC) a 50.0 bps (15h UTC), soit 1.28x.

La dispersion horaire vient **presque entierement du spread** (14 a 27 bps), pas de l'impact (1,6 a 2,6 bps). Autrement dit: la liquidite de surface de BTC est bonne partout, mais franchir le carnet coute nettement plus cher aux heures Europe/US (14h-21h UTC) qu'a la nuit. C'est un filtre de regime quasi gratuit: un candidat intraday BTC qui refuse de trader avant 12h UTC verrait son cout baisser d'environ 20 % a taille identique.


## 4. Seuil de viabilite : gain brut minimal par trade

Application directe de la regle des 3x du plan.


| Actif | Taille | Cout | **Gain brut min (3x)** | Gain min en stress x2 |
|---|---:|---:|---:|---:|
| BTC | 100 k$ | 42.8 bps | **128.5 bps** | 257.1 bps |
| BTC | 1,000 k$ | 53.1 bps | **159.3 bps** | 318.6 bps |
| ETH | 100 k$ | 48.8 bps | **146.4 bps** | 292.9 bps |
| ETH | 1,000 k$ | 65.6 bps | **196.8 bps** | 393.6 bps |
| SOL | 100 k$ | 91.0 bps | **272.9 bps** | 545.8 bps |
| SOL | 1,000 k$ | 142.7 bps | **428.0 bps** | 856.0 bps |
| AAVE | 100 k$ | 159.6 bps | **478.7 bps** | 957.4 bps |
| AAVE | 1,000 k$ | 374.0 bps | **1,121.9 bps** | 2,243.8 bps |
| DOGE | 100 k$ | 85.8 bps | **257.4 bps** | 514.8 bps |
| DOGE | 1,000 k$ | 156.9 bps | **470.8 bps** | 941.5 bps |
| SUI | 100 k$ | 130.2 bps | **390.6 bps** | 781.3 bps |
| SUI | 1,000 k$ | 250.6 bps | **751.7 bps** | 1,503.5 bps |
| XRP | 100 k$ | 72.2 bps | **216.6 bps** | 433.2 bps |
| XRP | 1,000 k$ | 121.5 bps | **364.6 bps** | 729.2 bps |
| BNB | 100 k$ | 59.8 bps | **179.5 bps** | 359.0 bps |
| BNB | 1,000 k$ | 93.7 bps | **281.1 bps** | 562.3 bps |
| LINK | 100 k$ | 100.7 bps | **302.2 bps** | 604.4 bps |
| LINK | 1,000 k$ | 194.0 bps | **582.1 bps** | 1,164.2 bps |
| NEAR | 100 k$ | 139.5 bps | **418.4 bps** | 836.8 bps |
| NEAR | 1,000 k$ | 293.9 bps | **881.6 bps** | 1,763.3 bps |
| XMR | 100 k$ | 115.1 bps | **345.4 bps** | 690.8 bps |
| XMR | 1,000 k$ | 251.9 bps | **755.6 bps** | 1,511.1 bps |
| FET | 100 k$ | 178.4 bps | **535.1 bps** | 1,070.2 bps |
| FET | 1,000 k$ | 385.5 bps | **1,156.6 bps** | 2,313.3 bps |

## 5. Ce que l'atlas dit deja

1. **A 100 k$, les frais dominent tout le reste.** Les frais taker font 20 bps aller-retour; le spread BTC retenu en fait 1.76 et l'impact une fraction de bps. Toute these d'edge intraday BTC doit survivre a 20 bps avant de compter.

2. **L'echelle des actifs change tout.** DOGE a un spread 3.45 bps, soit 2.0x BTC, mais un ADV 1m de 0.03 M$ contre 0.76 M$ — un facteur 24 en capacite a taille egale. Un edge intraday DOGE est un edge qui ne vit qu'a tres petite taille.

3. **L'exigence de 3x filtre la plupart des ideas intraday a 1m.** Le seuil de viabilite BTC 100 k$ est 65.3 bps (le plancher frais+spread 21.8 bps, avant impact). Un signal qui rapporte 43.5 bps par trade ne serait pas profitable, meme avec un IC significatif. C'est le criterе le plus brutal du plan et il doit passer AVANT tout test statistique.


## 6. Reproduction

```
uv run desk data bars-r2 --symbols BTCUSDT --timeframes 1h,1d
uv run pytest tests/test_costs.py -q
uv run python -m aster.data.costs_table   # regenere ces tableaux
```


Artefacts : `research/atlas/cost-estimates.csv`, `research/atlas/cost-grid.csv`.
