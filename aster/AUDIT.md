# Audit du desk Aster (2026-10-16)

Périmètre : branche `feat/aster-agent` @ `8b71b72`. Lu : `desk/src` (10,7 k lignes), `config/desk.yaml`, les policies, `research/` (MAP, BACKLOG, notes), les skills `aster-*`, `hermes.md`, `Status.md`. Je n'ai pas eu accès au VPS, à `data/` ni au ledger.

## Verdict en une phrase
L'infrastructure statistique est sérieuse : DSR, PSR, purged CV, PBO, test de look-ahead, ledger avec hash de préinscription. Mais **la recherche a tourné en rond sur des signaux journaliers à partir des prix de clôture, et `desk backtest` ne sait pas tester autre chose.** Même un bon signal de flux ou de funding ne pourrait pas être backtesté aujourd'hui.

## 1. Bloquants, par ordre d'impact

| # | Constat | Preuve | Impact | Correctif |
|---|---|---|---|---|
| 1 | Le contrat de stratégie ne reçoit que les **prix de clôture** | `strategies/base.py` : `target_weights(prices)` | Impossible de backtester le flux taker, le volume, le funding, le premium, l'OI, donc tout le N5 et la section 6 du brief | QUEUE **P1** |
| 2 | Timeframe **global, en 1d** | `config/desk.yaml: timeframe: 1d`, `pipeline.py` | Pas de stratégie intraday possible | **P2** |
| 3 | Funding facturé sur **toutes** les positions, y compris le spot | `pipeline.py` charge `load_funding` pour l'univers spot, `engine.py` l'applique à `held` | Carry delta-neutre inexprimable, coûts faux pour le spot | **P2** |
| 4 | Le holdout du pipeline est **dans la zone déjà explorée** | `holdout_frac: 0.25` sur des données pré-cutoff via `r2_backtest_store` | Holdout contaminé, comme l'« option A » | **Q1 + P3** |
| 5 | Le post-cutoff n'a jamais été importé, alors qu'il est **gratuit** | `import_r2()` ne liste que les mois avant `CUTOFF` | « Pas de holdout sans acheter de données » est faux | **Q1** |
| 6 | Coûts **forfaitaires** de 10 + 5 bps par côté | `CostModel` | Trop optimiste pour les alts et l'intraday, trop pessimiste pour BTC en maker | **P4** |
| 7 | **Pas de capacité** dans le rapport de backtest | aucune occurrence dans `backtest/` | Le critère 5 du brief (Sharpe net ≥ 1 à l'AUM visé) n'est jamais mesuré | **P4** |

## 2. Recherche : ce qui a été fait, et ce qui ne l'a pas été

Fait proprement : N0 à N5 sur BTC et ETH, N0 et N1 sur 5 alts, et 7 « axes ». Le tout avec BH-FDR, placebos et bootstrap par blocs. Les résultats nuls sont crédibles **pour ce qu'ils testent**.

Pas fait, alors que le brief le demande et que c'est là que se trouvent les meilleurs a priori :
- **Funding, basis, premium, open interest** : jamais téléchargés pour la recherche. C'est la famille d'edge crypto la mieux documentée, avec un mécanisme clair : les longs à levier paient.
- **Tout ce qui est intraday** (1 min à 4 h) : lead-lag BTC → alts aux décalages en minutes, saisonnalité horaire et fixings de funding 00/08/16 UTC, sauts intraday. Les études N1, N2 et inter-actifs sont journalières.
- **Barres d'information à partir des aggTrades** : gratuites sur tout l'historique, alors qu'elles sont traitées comme « 1 mois, juin 2024 ».
- **Veille** : une seule note, contre une réplication systématique des papiers demandée.
- **Dossiers d'actifs** `research/assets/<SYMBOLE>.md` avec niveau N0 → N7 en tête : remplacés par des fichiers datés épars.

Biais de méthode observé : les « axes » 2, 5 et 6 (Ichimoku, Camarilla/Woodie/Elliott, XGBoost) cherchent des stratégies, alors que le brief demande d'abord de comprendre l'actif. Ce sont beaucoup d'essais à faible a priori, ce qui consomme du budget de tests multiples sans faire progresser la compréhension.

## 3. Skills : ce qui manque à Aster

La bibliothèque est riche, mais un tiers est hors sujet pour la crypto : CFA fixed income, ECB yield curve, Tuckman, Ilmanen, FRTB. Il manque :
- un skill **perps et funding** : mécanique du funding Binance (fixings, plafonds, prix mark/index), basis, carry, risques de liquidation et d'ADL ;
- un skill **microstructure crypto** : aggTrades, `is_buyer_maker`, barres d'information, VPIN sur données réelles ;
- une **carte de littérature crypto** avec résultats revendiqués et statut de réplication. `aster-crypto-alpha-map` en donne le squelette, sans références.

La façon la plus efficace d'y remédier est l'item **Q16**. La veille produit ces trois références sous forme de fichiers `research/veille/*.md`. Aster les crée lui-même ; ce sont des données, pas des instructions.

## 4. Ce qui est réaliste « dans quelques jours »

- **Jours 1–2** : Q0, Q1, P1–P4. C'est du code et des tests, mené sans s'arrêter grâce à l'autopilot.
- **Jours 2–4** : Q3 (données perps) et la partie descriptive de Q8, puis préinscription de **F1 (carry funding)**, **F2 (crowding)** et **F3 (trend panel)**, suivie des backtests dev.
- **Ensuite** : chaque candidate qui passe le gate dev (DSR ≥ 0,95, stress ×2, capacité) te revient pour la lecture du holdout (ROUGE), puis 28 jours de paper.

Personne ne peut garantir qu'une de ces trois familles passe : le brief interdit justement de tordre les gates. Mais ce sont les a priori les plus solides disponibles avec ces données, et en quelques jours tu auras des verdicts dev chiffrés et défendables. Une stratégie « validée » au sens du brief prend en revanche au minimum un mois, à cause du paper obligatoire.
