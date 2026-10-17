# BTC/ETH N3 — pré-enregistrement volatilité et prévision

**Date :** 2026-10-14  
**Statut :** protocole fixé avant lecture des résultats N3 ; étude descriptive de prévision, pas une stratégie et aucun holdout.

## Périmètre et coupure

- Actifs : BTC/USDT et ETH/USDT spot.
- Source : partitions R2 locales Binance Vision 1-minute auditées par `aster.data.r2_klines.read_local`.
- Coupure exploratoire stricte : `2024-07-01T00:00:00Z` exclusive. Aucun octet postérieur n'est lu.
- Échantillon de développement : première date disponible jusqu'au `2022-12-31`; pseudo-OOS : `2023-01-01` jusqu'au dernier jour pré-cutoff. La séparation est fixée avant calcul.
- Les minutes `trades == 0` sont exclues du calcul intraday de RV/BV, jamais forward-fillées. Une journée est conservée seulement si elle contient au moins 720 minutes actives et au moins 1 000 paires consécutives de minutes actives sur la grille d'une minute.

## Mesures réalisées

À partir des closes 1-minute observés et des retours sur minutes consécutives :

- `RV_t = 1e8 * sum(r_i^2)` en unités de bp² ;
- `BV_t = 1e8 * (pi/2) * sum(|r_i| |r_{i-1}|)` ;
- `jump_t = max(RV_t - BV_t, 0)`.

Les jours à observations insuffisantes sont manquants. Les jours calendaires sans données ne sont pas imputés.

## Modèles fixes

Prévision de `log(RV_{t+1})` :

1. naïf : moyenne exponentielle fixe des 30 dernières observations ;
2. HAR-RV : OLS récursive de `log(RV)` sur constante, retard 1 jour, moyenne retardée 5 jours et moyenne retardée 22 jours ;
3. GARCH(1,1)-tourné-volatilité : variance conditionnelle quotidienne sur le retour close-to-close, paramètres estimés récursivement par QMLE gaussien avec bornes fixes ; prévision ramenée en unités RV via `1e6 * sigma²`.

Le modèle HAR est ajusté sur chaque fenêtre d'apprentissage complète ; aucun choix de fenêtre ou de lag après résultat. Le GARCH utilise uniquement les retours connus avant la date de prévision.

## Évaluation pseudo-OOS

- Origine minimale : au moins 756 jours de développement valides.
- Horizons : 1 jour uniquement pour éviter de multiplier les familles ; extension 5/22 jours interdite dans cette version.
- Fonction de perte primaire : squared error sur `log(RV)`.
- Contrôle : absolute error sur `log(RV)`.
- Comparaisons : HAR contre naïf, GARCH contre naïf, HAR contre GARCH.
- DM bilatéral avec variance HAC Newey-West, bande `floor(N^(1/3))`, correction HLN pour horizon 1. Signe positif = premier modèle plus mauvais ; aucun seuil de trading.
- Multiplicité : six comparaisons modèle/perte/actif sont une famille descriptive ; BH-FDR q=5% rapporté, sans sélection de stratégie.

## Règle d'interprétation

Un modèle n'est déclaré supérieur que si son différentiel de perte est stable par année 2023/2024, DM-HLN est significatif après BH-FDR et le gain absolu de perte est rapporté. Une meilleure prévision de volatilité ne constitue pas une preuve d'alpha, ne déclenche aucun `desk backtest` et ne justifie aucune allocation.

## Contrôles et sorties

- Test de coupure et test de causality par troncature inclus dans la suite de tests.
- Unité, formules RV/BV, mesure DM-HLN et estimation GARCH vérifiées par tests de référence.
- Sorties prévues : `research/assets/2026-10-14-btc-eth-n3-vol.csv`, `research/assets/2026-10-14-btc-eth-n3-vol.md`.
- Aucun holdout ; aucune donnée actuelle, funding ou carnet d'ordres.
