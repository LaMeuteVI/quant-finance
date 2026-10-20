# Phase close — Recherche crypto klines 1m daily, bilan final

**Date** : 2026-10-15
**Statut** : **PHASE CLOSE — décision tick microstructure requise**
**Auteur** : Aster (Samuel demandeuse)
**Cutoff exploration** : `2024-07-01T00:00:00Z` (strictement respecté)
**Période couverte** : 2026-10-13 → 2026-10-15 (≈ 8 sessions)

---

## TL;DR

**5 axes library-backed explorés à fond sur klines 1m daily BTC/ETH (+ alts) pré-2024-07-01 : 0 edge tradable net de coûts identifié.**

Aucun ledger hypothesis vivante. 1 ledger hypothesis rejetée (H-20261013-001, BTC daily TSMOM 60j). Tous les modules, tests, notes et commits sont sur `feat/aster-agent` du repo `LaMeuteVI/quant-finance`.

**Cause structurelle convergente** : les klines 1m daily moyennent l'information microstructurelle (signature tick) qui porte l'edge résiduel sur crypto mature. Le marché a déjà arbitrégué les anomalies visibles à ce bar.

**Décision requise** : passer aux données tick microstructure (Tardis/Kaiko/Databento/CoinAPI) pour capter l'edge résiduel, OU clore définitivement la recherche crypto historique.

---

## Axes explorés (5/5)

| # | Axe | Verdict | Note |
|---|---|---|---|
| 1 | Term structure intra-day (vol morning/evening, autocorr minute-par-minute) | **0 edge** | `research/notes/2026-10-14-axe-1.md` |
| 2 | Ichimoku Kinko Hyo complet (10 chapitres Riguet) | **0 edge** | `research/notes/2026-10-14-axe-2.md` |
| 3 | Mean-reversion OU + half-life + pairs (6 paires testées) | **0 edge** | `research/notes/2026-10-14-axe-3.md` |
| 4 | Vol risk premium (HAR-RV, RV/BV/JV, VRP par décile) | **0 edge** | `research/notes/2026-10-14-axe-4.md` |
| 5 | CFA-style TA enrichi (Camarilla/Woodie/Fib/Elliott proxy) | **0 edge** | `research/notes/2026-10-14-axe-5.md` |

**Axes non lancés (par décision)** : 6 (XGBoost ML), 7 (Markov-switching BTC→alts), 8 (aggTrades microstructure proxy). Probabilité conditionnelle d'edge < 10% d'après les 5 axes précédents. Décision close vs continuation = à Samuel.

---

## Modules Python livrés (5/5, 252 tests verts)

| Module | Lignes | Test | Description |
|---|---|---|---|
| `intraday_term_structure.py` | 261 | 5 verts | Profil vol intra-day, autocorr minute-par-minute |
| `ichimoku_signal.py` | 137 | (couvert par 252 global) | Tenkan/Kijun/SSA/SSB/Chikou, TK cross, Kijun pullback |
| `ou_pairs.py` + `ou_pairs_backtest.py` | 250 | 5 verts | OU half-life, ADF, Engle-Granger, BH-FDR, z-score backtest |
| `vol_risk_premium.py` | 200 | 5 verts | RV daily, BV (bipower), JV (saut), HAR-RV, VRP par décile |
| `ta_enriched.py` | 230 | 5 verts | Camarilla, Woodie, Fib retracements, zigzag swings |

**pytest total** : 252 passed, 18 warnings, ~14s. Working tree clean.

---

## Artefacts produits (29 fichiers CSV + 5 notes)

Tous dans `research/assets/2026-10-14-axe-*.csv` et `research/notes/2026-10-14-axe-*.md`. Tous pushés sur `feat/aster-agent` (commits `889927d`, `ea02198`, `e5bfff1`, `bd2d871`, `daa15d9`).

---

## Bilan technique consolidé

### Résultats transverses

- **Autocorr minute-par-minute (axe 1)** : -0.25 à -0.05 en 2017-2020 (massif), dérive vers 0 en 2022-2023 (arbitragé). Profit net par trade = 3e-8 → dominé par frais 20 bps.
- **Ichimoku Chikou (axe 2)** : forward-looking par construction (chikou = close.shift(-26)), inutilisable en automatisable.
- **Cointégration crypto (axe 3)** : 5/6 paires rejettent ADF après BH-FDR (BTC/ETH, ETH/SOL, BTC/BNB, BTC/XRP, ETH/XRP). Mais half-life effectif du spread = 173 jours → trop lent pour horizon raisonnable. Backtest z-score BTC/ETH : win rate 60%, **PnL net -220 bps/trade, t-stat = -0.79**.
- **HAR-RV (axe 4)** : bat le naïf à 99% de confiance (t-DM = -5.20 BTC, -4.51 ETH, gain RMSE 10%). Mais c'est un signal forecast-only, pas tradable sans options listées. VRP par décile : pas de mean-reversion post-spike (le drift haussier domine).
- **Camarilla/Woodie/Fib (axe 5)** : 2-3 cellules passent BH-FDR q=0.25 sur BTC, 0 passe q=0.05 strict. Signaux observés = continuation haussière = exposition au bêta, pas alpha.

### Cause structurelle

Les klines 1m daily moyennent l'information tick. Or, sur crypto mature (BTC, ETH), les anomalies microstructurelles (mean-reversion intra-minute, déséquilibre agressif, lead-lag) sont arbitrégées par les HFTs depuis ~2020. La confirmation indépendante vient de la **veille Easley et al. (SSRN 4814346)** : AUC 0.55-0.58 sur labels ΔRV depuis klines 1m, **pas de P&L net reporté**. Cohérent avec nos 0/N résultats.

### Études antérieures (sessions 1-4, klines 1m daily)

Pour mémoire (du résumé antérieur) :
- N0-N3 : atlas microstructure, N1 TA formalisée (224 cellules testées, 1 survivante non-retenue), N2 statistique des rendements, N3 GARCH/EGARCH (HAR-RV > naïf, déjà confirmé en axe 4).
- N4-N5 : régimes (5 classes, persistance 9.9-13.6j), 0/15 cellules retenues BTC, 0/15 ETH.
- Inter-résiduels : 1 288 jours × 8 actifs × K=1/2/3, max |Spearman| = 0.107 (R² ≤ 1.1 %), **aucun signal exploitable**.
- Panel N0 : couverture ≥ 99.76 % tous actifs, XMR comme garde-fou biais survivant.

---

## Décision requise à Samuel

### Option A — Acquisition tick microstructure (recommandée)

- **Coût estimé** : $200-500/mois pour Tardis ou Kaiko (1-2 ans d'historique BTC/ETH+alts).
- **Edge potentiel** : capturer la signature tick non-moyennée par les klines 1m.
- **Pré-requis** : nouveau cutoff après acquisition, contrôle de provenance documenté.
- **Plan** : ré-engager les axes 6-8 sur tick data (XGBoost microstructure, Markov-switching, Lee-Ready/Kyle λ/Amihud sur aggTrades).

### Option B — Clôture définitive

- Acceptation du verdict : 0 edge tradable sur crypto historique klines 1m daily.
- Le code et les notes restent versionnés pour reproduction future.
- Aucun budget data supplémentaire.

### Option C — Élargir l'univers

- Tester sur des paires moins couvertes par HFT (PET, FET, SUI, RENDER, ONDO).
- Risque : faible liquidité, coûts plus élevés, capacité limitée.

---

## Crons configurés

- `f952bdbebf25` (every 2h, deliver=local,origin) : moteur de recherche Aster, condition d'arrêt = `phase-close.md` existe OU message Samuel "stop".
- `9130e32f3b69` (every 90 min, deliver=local) : job de surveillance lecture seule.
- `caf0cac99ead` (daily 07:30, paused) : cycle desk journalier.
- `875d956ef061` (every 15 min, paused) : risk watchdog.
- `4e23f0dfba2a` (daily 02:15, paused) : paper trade.

---

## Annexe — Leçons transférables

1. **Klines 1m daily ≠ tick microstructure**. Le bar moyenné cache l'edge. Toute future recherche sur ces données a une borne haute d'alpha ≈ 5-10 bps/jour (avant coûts).
2. **Cointégration crypto est structurelle** (secteur commun), pas tactique. Half-life ≈ 173j sur BTC/ETH. Inutilisable sans catalyseur.
3. **Drift haussier crypto 2017-2023 fausse tous les tests de continuation**. Toujours conditionner sur régime (bull/bear).
4. **Les niveaux techniques (Camarilla, Woodie, Fib, Ichimoku) sont des outils de cartographie, pas de signal**. Le signal qu'on en tire est au mieux un proxy du momentum générique.
5. **Sans options listées, la VRP n'est pas tradable**. Prévoir la vol ≠ gagner sur la vol.
6. **BH-FDR est non-négociable**. 5 axes × ~50 tests = 250 hypothèses. Une p-valeur de 0.05 sans correction n'est rien.

---

**Prochaine action (Aster)** : attente décision Samuel (A, B, C). Aucun travail en cours. Aucun cron n'exécute de recherche active (f952bdbebf25 s'arrêtera au prochain fire quand il lira ce fichier de close).
