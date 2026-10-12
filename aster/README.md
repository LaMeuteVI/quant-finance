# Aster — Quant Research & Crypto Trading Desk

Agent Hermes (profil `aster`) spécialisé recherche quantitative et trading crypto, adossé à un desk Python où **tout ce qui touche à l'argent est du code, pas du prompt**.

> Principe directeur : **le LLM cherche, le code trade.** Aster génère des hypothèses, écrit les stratégies, lance les backtests et rédige les rapports. Les ordres ne passent que par une boucle déterministe (`desk trade run`) protégée par un risk gate codé, un kill switch verrouillant, un contrôle de stade dans le ledger et, en live, ta validation humaine.

## Architecture

```
Aster/
├── SOUL.md                 identité, mandat, 7 règles non négociables
├── config.overlay.yaml     fusionné dans la config du profil : cwd = desk, skills externes, fichiers protégés
├── distribution.yaml       manifeste Hermes (profil partageable/versionnable)
├── install.sh              installation / mise à jour idempotente du profil
├── skills/                 procédures propres à Aster (ta bibliothèque Livres/Skills est branchée en direct)
│   ├── aster-desk              cycle quotidien, rôles, briefs de délégation, format des rapports
│   ├── aster-research-loop     idée → pré-enregistrement → backtest → holdout → paper
│   ├── aster-crypto-alpha-map  familles d'edge crypto : mécanisme, données, pièges
│   ├── aster-postmortem        revue hebdo du critique, leçons écrites dans le ledger
│   └── aster-risk-ops          incidents, kill switch, dossier de promotion vers le live
├── hermes_scripts/         scripts cron sans LLM (watchdog risque, rebalancement paper)
└── desk/                   le workspace de l'agent
    ├── AGENTS.md           la carte du desk (chargée automatiquement par Hermes)
    ├── config/             desk.yaml (univers, coûts, gates) · risk_limits.yaml (limites DURES, protégé)
    ├── policies/           research_protocol · backtest_standard · data_policy · risk_policy · execution_policy · promotion_policy
    ├── templates/          hypothèse · mémo · rapport de backtest · post-mortem · fichier stratégie
    ├── src/aster/          data · backtest · validation · ledger · risk · execution · portfolio · research · strategies · cli
    └── tests/              38 tests sur les garde-fous de l'infra (données synthétiques, sans réseau)
```

### Équipe (sous-agents via `delegate_task`)
Aster (PM, seul à enregistrer des hypothèses et à changer les statuts) · Scout (état du marché) · Researchers ×2-3 (prix/volume, funding/dérivés, on-chain), **en parallèle sans se lire** · Skeptic (attaque chaque idée) · Quant dev (code + tests) · Breaker (stress, régimes, PBO) · Critic (post-mortem hebdo).

### Garde-fous appliqués par le code, pas par les instructions
| Garde-fou | Où |
|---|---|
| Pré-enregistrement immuable (hash) de l'hypothèse, de la falsification et de la prédiction chiffrée | `ledger/db.py` |
| Chaque backtest est un essai compté ; le Deflated Sharpe utilise ce compte par famille | `backtest/pipeline.py`, `validation/stats.py` |
| Max 5 versions de stratégie par hypothèse | `ledger/db.py` |
| Holdout scellé (25 % les plus récents), lisible une seule fois | `ledger/db.py`, `validation/cv.py` |
| Détecteur générique de look-ahead (invariance par troncature) sur chaque run | `validation/lookahead.py` |
| Coûts, funding, stress ×2/×3 et lag 2, pires fenêtres | `backtest/engine.py` |
| PSR, DSR, MinTRL, haircut, PBO (CSCV), purged k-fold + embargo, triple barrier, FFD, HRP | `validation/`, `research/`, `portfolio/` |
| Machine à états : impossible d'avancer sans un essai réussi ; live = humain uniquement | `ledger/db.py` |
| Risk gate avant chaque ordre : perte journalière, drawdown, levier, concentration, notionnel, symboles, shorts, prix incohérent ou périmé | `risk/gate.py` |
| Kill switch qui se verrouille sur une perte ; seuls les ordres qui réduisent l'exposition passent ; levée réservée à l'humain | `risk/gate.py`, `desk kill off` |
| Journal append-only chaîné par hash (toute modification est détectée) | `execution/journal.py` |
| Live = `mode: live` + `ASTER_LIVE_ARMED=1` dans ton shell + promotion humaine + clés live | `execution/` |
| Écritures de l'agent sur les limites et politiques soumises à ton approbation | `config.overlay.yaml` |

## Installation

```bash
cd ~/Desktop/Livres/Aster && ./install.sh
```
Le script crée le profil `aster` en clonant ta config Hermes (modèle, clés), installe SOUL et skills, branche `Livres/Skills`, installe le desk (uv) et lance les tests, puis crée 4 crons **en pause** : desk quotidien (7h30), post-mortem (dimanche 18h), watchdog risque (toutes les 15 min, sans LLM), rebalancement paper (2h15, sans LLM). La config d'origine est sauvegardée dans `config.yaml.pre-aster.bak`.

Ensuite : `aster chat`.

## Ce qui reste entre tes mains
- `desk promote H-... --to live_pilot` et `desk kill off` : à lancer **dans ton propre terminal**. Ces commandes refusent de s'exécuter dans une session agent.
- Le passage en live : sous-compte dédié, approvisionné uniquement avec ce que tu acceptes de perdre ; clé API trade-only, retraits désactivés, IP whitelistée. **C'est la seule limite qu'aucun bug ne peut contourner.**
- `risk_limits.yaml`.

## État réel des capacités (v0.1)
Opérationnel : données spot et funding (ccxt), stockage avec provenance, contrôle qualité, backtest pondéré, validation statistique complète, ledger, risk gate, broker paper, broker ccxt testnet/live spot, journal, CLI, crons.
Pas encore fait : perps et shorts en exécution, carnet d'ordres et coûts intraday, univers point-in-time (coins délistés) pour la recherche cross-sectionnelle, options (Deribit), dashboard. Aucune stratégie validée : `tsmom` est un gabarit de démonstration, et il échoue d'ailleurs au gate (drawdown de -55 %).
