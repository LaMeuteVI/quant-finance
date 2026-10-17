# BTC N4/N5 — pré-enregistrement descriptif régimes et flux kline

**Date :** 2026-10-14  
**Statut :** étude descriptive uniquement ; pas de ledger hypothesis, pas de backtest, pas de holdout, pas d’allocation.

## Périmètre

- Actif : BTC/USDT spot.
- Source : `aster.data.r2_klines.read_local("BTCUSDT")` ; partitions R2 auditées.
- Coupure exploratoire : `2024-07-01T00:00:00Z` exclusive.
- Barres : 1d à partir de klines 1m ; flux agressif calculé sur les klines 1m.

## Mesures fixes

### N4 — Régimes
1. Indicateurs de régime sur la fenêtre journalière, calculés avant le jour t :
   - retour composé 5/22/66 jours ;
   - volatilité réalisée `sqrt(RV_t)`, centrée sur la médiane 252 jours ;
   - régime de tendance : `sign(roll5)` ;
   - régime de vol : `sign(roll_vol - med252)` ;
   - régime combiné 2 × 2 = 4 classes.
2. Distribution de chaque classe, autocorrélation, persistance moyenne.

### N5 — Flux kline
1. `imbalance_t = 2 * taker_buy_base_t / volume_t - 1` sur barres 1m actives, agrégé en somme signée en dollars et EWMA 60/240 minutes.
2. `signed_dollar` cumulé sur la journée comme proxy de pression d’ordre.
3. Choc de volume : `z = (quote_volume - EMA252) / std252` sur la quote-volume journalière.
4. Choc de trades : `z_trades` sur `trades` journalier.
5. Roll spread kline par jour : `2 * sqrt(max(-Cov(ΔP_t, ΔP_{t-1}), 0))` sur les rendements 1m actifs d’une journée, en fraction du close moyen.
6. Amihud daily : `mean(|r| / quote_volume) * 1e6` sur les 1m actives de la journée.

### Tests
- Étude causale : features basées sur la barre t, rendements de t+1 / t+2 / t+5.
- Placebos :
  1. signes des rendements décalés mélangés (retain the marginal distribution, kill the lead) ;
  2. journée j shiftée de `+1d` (faux futur immédiat).
- Inverse : `-signed_dollar` doit prédire le signe opposé.
- BH-FDR sur la grille `{horizon × feature × actif}` (BTC ici, 1 actif × 3 horizons × 6 features = 18 cellules, plus leurs inverses et placebos).
- Stabilité annuelle par régime : `1 test/an` sur 2018–2023, signe et magnitude par régime.

## Évaluation

- Pas de PBO sans backtest ; pas de DSR sans ledger hypothesis.
- Taille d’effet : corrélation Spearman par cellule, point estimate et bootstrap à 5 000 blocs.
- Une cellule n’est « notée » que si Spearman est non nul après BH-FDR, son placebo n’est pas non nul et l’inverse est moins fort.

## Règle d’interprétation

N4/N5 produit une **cartographie causale** du flux agressif kline BTC par régime. Aucun résultat descriptif ne devient un signal de trading sans ledger hypothesis séparée avec pré-enregistrement, desk backtest compté, holdout scellé et 28 jours de paper.

## Contrôles et sorties

- Test de coupure et test de causalité par troncature.
- Sorties :
  - `research/assets/2026-10-14-btc-n4-regimes.md`,
  - `research/assets/2026-10-14-btc-n5-flow.md`,
  - `research/assets/2026-10-14-btc-n5-flow.csv`.
- Aucun secret, aucun live, aucune modification de `risk/`, `execution/`, `policies/` ou `config/risk_limits.yaml`.
