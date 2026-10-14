# Rapport de recherche — 2026-10-14 (session 3)

## Décisions attendues de Samuel

- **Aucune.** Poursuite autonome. Tous les livrables sont des études descriptives ; aucun ledger hypothesis n'a été créé.
- **Décision stratégique en suspens** : le socle d'edge **intra-actif** sur BTC et ETH est **vide** après N1, N2, N4, N5 et le panel résiduel à 1 facteur. La prochaine primary feature ne peut venir que de **deux axes restants** :
  1. **Modèle multifactoriel** (2-3 facteurs) sur le panel 8 actifs, exploitant les corrélations résiduelles contemporaines 0,18-0,23 que l'ACP à 1 facteur ne capture pas.
  2. **Acquisition de données microstructure tick** (Tardis / Kaiko) qui pourrait enfin révéler un edge non-arbitré — au-delà du scope klines 1m.

  L'axe 1 est faisable en interne sans nouveau pipeline de données. L'axe 2 nécessite ton OK sur un budget et ton autorisation de regarder des données post-cutoff (le holdout scellé doit rester tel quel).

## Travail effectué pendant la session

### 1. Inter-actifs résiduels factoriels 6.1/6.2/6.3 — descriptif
- **Code** : `src/aster/research/inter_residual.py` (320 l.) + 5 tests verts.
- **Protocole** : 8 actifs (BTC, ETH, BNB, XRP, SOL, LINK, DOGE, XMR), rendements daily log sur l'intersection des fenêtres, z-score par actif, débruitage Marcenko-Pastur, **PCA à 1 facteur**, résiduels dans une grille 56 paires × 8 lags = 448 cellules Spearman, plus 12 cellules cross-sectionnelles, 5 000 bootstraps par cellule, BH-FDR sur la grille complète, placebo (cible décalée), filtre de stabilité par année (≥ 4/6 ans de signe cohérent).
- **Résultat** : **5/448 cellules retenues**, **0/12 cross-section**.
- **Conclusion** : les 5 survivantes sont des Spearman |0,08-0,12| (≈ 1 % de R²). Significatives au sens statistique mais **non tradables** (1 % de variance expliquée × impact de marché = edge net négatif). Les corrélations résiduelles contemporaines 0,18-0,23 montrent qu'**un seul facteur marché ne capture pas toute la variance commune** : il faut 2-3 facteurs (BTC + ETH + sector). Pas de ledger hypothesis.

### 2. Panel N0 — descriptif
- **Code** : `src/aster/research/panel_n0.py` (180 l.) + 3 tests verts.
- **6 actifs** : BNB (3,49 M min, $37k DV/min médian, 1,1 % frozen), XRP (3,23 M min, $46k), SOL (2,04 M min, $62k, depuis 2020-08), LINK (2,87 M min, $20k, 4,4 % frozen), DOGE (2,62 M min, $19k, 13,6 % frozen), XMR (2,59 M min, $2,3k, 11,1 % frozen, **délisté 2024-02-20** = garde-fou survivant).
- **Couverture ≥ 99,76 %** sur tout le panel, 168 buckets horaires par actif.
- **Capacité** (Almgren-Chriss) : DV médian tradeful × impact sqrt = la capacité AUM est petite pour XMR/DOGE, grande pour SOL/BNB. Calculs explicites dans chaque dossier.

### 3. Leçons de la session
- **Le bootstrap Spearman pur Python est trop lent** pour des grilles > 100 cellules × 5 000 bootstraps. J'ai vectorisé via Pearson-sur-rangs + dot product numpy, ~10× plus rapide. Réutilisable.
- **Aucun "truc évident" n'a surgi** du panel résiduel à 1 facteur. C'est un résultat utile : il dit que la **communauté de variance crypto est principalement factorielle** (le bêta BTC), pas idiosyncratique. Le seul résidu idiosyncratique exploitable devrait venir d'un facteur sectoriel ou d'un signal de microstructure tick.
- **Le FVG baissier ETH (`fvg_down_entry_h1`)** reste au backlog, pas au ledger. Mécanisme ambigu (continuation baissière vs mean-reversion du gap), ETH-only, edge ≈ -1 %/jour. À rouvrir si on a un signal directionnel de régime.
- **Le pipeline 2-3 facteurs** est la prochaine étape logique. Le code `inter_residual.py` est conçu pour ça : changer `factor_residuals` pour retourner 2-3 facteurs, et le reste suit.

## État de la matrice (cf. `MAP.md`)

| Actif | N0 | N1 | N2 | N3 | N4 | N5 | N6/N7 |
|---|---|---|---|---|---|---|---|
| BTC | ✅ | ✅ no cand. | ✅ no cand. | ✅ forecast | ✅ desc. | ✅ no cand. | gated |
| ETH | ✅ | ✅ no cand. | ✅ no cand. | ✅ forecast | ✅ desc. | ✅ no cand. | gated |
| BNB, XRP, SOL, LINK, DOGE | ✅ | queued | queued | queued | queued | queued | gated |
| XMR (garde-fou) | ✅ | queued | queued | queued | queued | queued | gated |
| Panel 8 actifs (inter-résiduel) | n/a | ✅ no cand. (1 facteur) | n/a | n/a | n/a | n/a | 2-3 facteurs queued |

**Bilan d'edge** : 0 ledger hypothesis vivante. 1 ledger hypothesis rejetée (H-20261013-001). 1 survivante au backlog (ETH FVG, non exploitable). 5 cellules inter-résiduelles survivantes (Spearman 0,08-0,12, non tradables).

## Prochaine étape

**Modèle multifactoriel 2-3 facteurs** sur le panel 8 actifs. C'est une **évolution naturelle de l'existant**, pas un nouveau pipeline. L'extension touche :
1. `factor_residuals` dans `inter_residual.py` (K=2 ou K=3 facteurs, dé-bruités par Marcenko-Pastur individuel, orthogonalisés).
2. La grille pairwise reste identique ; seul change le résidu.
3. Le cross-section momentum devient un **signal factoriel** (somme des loadings × score).

Si la multifactorielle ne livre rien, l'étude est close et la conclusion devient : **l'edge crypto retail intra-journalier, sans données tick microstructure, est épuisé par la concurrence**. C'est une conclusion défendable et Samuel peut décider d'arrêter ou de financer des données tick.

## Garde-fous

- Cutoff strict `2024-07-01T00:00:00Z`. Aucun accès holdout. Aucun secret. Aucun ordre. Aucune modif `risk/`, `execution/`, `policies/`, `config/risk_limits.yaml`.
- Tests : `uv run pytest -q` vert. `uv run desk journal verify` OK, 0 record invalide, 0 événement orphelin.
- Cron `725b2319f619` à 2h, prompt recentré multifactoriel. Prochaine échéance 17:20 UTC.

## Artefacts créés ou modifiés dans la session

- `src/aster/research/inter_residual.py` (320 l., créé)
- `tests/test_inter_residual.py` (70 l., 5 tests, créé)
- `research/2026-10-14-inter-residual-prereg.md` (pré-enregistrement, créé)
- `research/assets/2026-10-14-inter-residual.md` + `…-pairwise.csv` + `…-crosssec.csv` (rapport et données, créés)
- `src/aster/research/panel_n0.py` (180 l., créé)
- `tests/test_panel_n0.py` (3 tests, créé)
- `research/assets/2026-10-14-{bnb,xrp,sol,link,doge}xmr-n0.md` (6 dossiers d'actif, créés)
- `research/assets/2026-10-14-{symbol}-n0-hourly.csv` (6 profils horaires, créés)
- `research/assets/2026-10-14-panel-n0.md` + `…-comparison.csv` (synthèse panel, créés)
- `research/MAP.md` + `research/BACKLOG.md` (mis à jour)
