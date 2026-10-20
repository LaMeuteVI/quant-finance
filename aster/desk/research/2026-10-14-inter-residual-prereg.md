# Inter-actifs 6.1/6.2 — pré-enregistrement résiduels factoriels

**Date :** 2026-10-14
**Statut :** étude descriptive uniquement ; pas de ledger hypothesis, pas de backtest, pas de holdout.
**Cutoff exclusif :** `2024-07-01T00:00:00Z`.

## 1. But

BTC et ETH N1/N2/N4/N5 n'ont livré aucune primary feature tradable. Avant de conclure que le desk n'a rien à exploiter, on tente le niveau inter-actifs (message.txt §6.1, §6.2, §6.3) : est-ce qu'un signal résiduel (après extraction du facteur marché BTC) existe et est exploitable, et existe-t-il en cross-section sur le panel ?

## 2. Univers et période

- Source : `aster.data.r2_klines` (Binance Vision spot 1m).
- Symboles : `BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `XRPUSDT`, `SOLUSDT`, `LINKUSDT`, `DOGEUSDT`, `XMRUSDT` (8 actifs survivants/délistés avec historique long, dont XMR comme garde-fou).
- Fenêtre : union des fenêtres disponibles, intersectée avec `[2018-01-01, 2024-06-30]`.
- Minutes figées (`trades == 0`) : exclues.
- Actifs à historique court (SUI, RENDER, ONDO, PUMP, HYPE) : **exclus** de cette étude pour préserver la robustesse.

## 3. Méthode (6.1 structure de dépendance + 6.2 lead-lag résiduel)

1. Construire les rendements journaliers log à partir des minutes actives.
2. Aligner les séries sur l'intersection des jours disponibles.
3. Standardiser par actif (z-score, moyenne/std daily) pour neutraliser l'effet de niveau.
4. **Matrice de corrélation** (Pearson) sur rendements standardisés, à 1j, 3j, 7j.
5. **Débruitage Marcenko-Pastur** : pour chaque matrice, calculer la valeur propre max théorique du MP sous N=8, T=jours, ratio q=T/N. Les valeurs propres au-delà sont du signal. Projection des séries dans l'espace signal-only.
6. **ACP / factor model** : 1er facteur = « marché », 2e et 3e facteurs = rotated components. Pour chaque actif, calculer le **résidu** = retour journalier standardisé moins la projection sur le 1er facteur.
7. **Lead-lag résiduel** : grille (lead, lag) ∈ {−2, −1, 0, 1, 2, 3, 5, 7} jours, sur les résiduels entre chaque paire d'actifs. Spearman, bootstrap 5 000 blocs, BH-FDR sur toute la grille (8 actifs → 56 paires × 15 décalages = 840 cellules par horizon ; c'est beaucoup, mais c'est ce qu'il faut pour pouvoir conclure).
8. **Test placebo** : cible décalée d'un jour.
9. **Test inverse** : pour chaque cellule (i→j, lag=k), tester aussi (j→i, lag=-k).
10. **Filtre de rétention** : BH q < 0,05 ∧ bootstrap exclut 0 ∧ placebo non-significatif ∧ inverse ne domine pas ∧ ≥ 3 ans d'observations par an (pas une arnaque 2020-only).
11. **Stabilité par année** (2018, 2019, 2020, 2021, 2022, 2023) : la cellule survit si le signe et la magnitude sont stables sur ≥ 4/6 années.

## 4. Cross-section 6.3

- Sur les résiduels, calculer chaque jour un **ranking cross-sectionnel** des actifs par rendement résiduel.
- Tester si un signal « momentum cross-sectionnel 5j sur résiduels » ou « reversal cross-sectionnel 1j sur résiduels » est prédictif du rendement forward du top/bottom quantile.
- BH-FDR sur le panel de 8 actifs × 4 horizons (1/3/5/7j).

## 5. Garde-fous

- Cutoff strict.
- Aucun secret, aucun ordre, aucun appel à `desk backtest` ou `r2_backtest_store`.
- Aucune modification de `risk/`, `execution/`, `policies/`, `config/risk_limits.yaml`.
- Si une cellule survit, elle est **candidat au backlog** avec mécanisme, coûts et capacité à documenter — pas un ledger hypothesis automatique.

## 6. Artefacts

- `src/aster/research/inter_residual.py` (module partagé).
- `tests/test_inter_residual.py` (tests de référence : MP eigenvalue max, Spearman bootstrap, BH).
- `research/assets/2026-10-14-inter-residual.md` (rapport).
- `research/assets/2026-10-14-inter-residual-pairwise.csv`.
- `research/assets/2026-10-14-inter-residual-crosssec.csv`.
