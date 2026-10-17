# Cryptos — desk de recherche quantitatif crypto

Tout le travail de recherche crypto du desk vit dans ce repo.
Ce dossier `cryptos/` est un point d'entrée ; le contenu réel est à la racine du repo.

## TL;DR pour reprendre

```bash
git clone https://github.com/LaMeuteVI/quant-finance.git
cd quant-finance
uv sync
uv run pytest -q                       # doit être vert
uv run desk --help                     # commandes du desk
uv run desk journal verify             # intégrité du journal
uv run desk ledger list                # ledger des hypothèses
```

## Carte du repo

| Dossier | Contenu |
|---|---|
| `AGENTS.md` | Règles de travail du desk (à lire en premier) |
| `policies/` | Politiques de recherche, backtest, risque, exécution, promotion (binding) |
| `config/` | Configuration du desk (universe, coûts, gates) |
| `src/aster/` | Code source : data, backtest, validation, ledger, risk, execution, portfolio, research, strategies, cli |
| `tests/` | Tests unitaires (doit toujours être vert) |
| `research/` | Mémos de recherche et atlas |
| `research/assets/` | Dossiers d'actifs N0→N7 et études descriptives (BTC, ETH, BNB, XRP, SOL, LINK, DOGE, XMR) |
| `reports/` | Rapports journaliers / hebdomadaires / post-mortems |
| `backtests/` | Artefacts de backtests (un dossier par trial, écrit par `desk backtest`) |
| `memory/ledger.db` | Source de vérité des hypothèses, essais et leçons (versionné) |
| `state/` | Daybook paper, état du kill switch |
| `templates/` | Templates hypothesis, research memo, backtest report, post-mortem, strategy file |
| `data/` | Données brutes (gitignored — 2.6 Go) ; voir `data/` (les manifests sont versionnés) |
| `cryptos/` | Ce README — point d'entrée |

## État actuel de la recherche (2026-10-14)

Voir `reports/2026-10-14-research-session3.md` (le plus récent) et `research/MAP.md` (matrice actifs × niveaux).

**Bilan** : 4 sessions de travail. 0 ledger hypothesis vivante. 1 rejetée
(`H-20261013-001`, daily TSMOM 60j BTC). Tous les axes klines-1m daily
explorés (BTC, ETH N1-N5, inter-résiduels 1-2-3 facteurs) ont échoué à
produire un edge tradable après correction multi-tests stricte, contrôle
placebo, et filtre de stabilité. Cause structurelle probable : les klines
1m moyennisent la microstructure tick où vit l'information résiduelle.

## Garde-fous stricts (rappel)

- **Cutoff** : `2024-07-01T00:00:00Z`. Aucune donnée post-cutoff n'est consultée pendant l'exploration.
- **Périmètre** : recherche et paper trading uniquement. Aucun ordre live.
- **Aucun secret** dans le repo (`.env`, API keys, etc.). `.gitignore` les exclut.
- **Holdout scellé** : lu une seule fois via `desk backtest --sample holdout`. Jamais en exploration.
- **Données brutes** non versionnées (trop lourdes, regenerables). Seuls les manifests de provenance sont commités.

## Workflow pour reprendre avec Claude Code

1. Clone + `uv sync`.
2. Lis `AGENTS.md` et `policies/research_protocol.md`.
3. Lis `reports/2026-10-14-research-session3.md` pour le contexte.
4. Lis `research/MAP.md` (matrice) et `research/BACKLOG.md` (idées en attente).
5. `uv run desk ledger list` pour l'état des hypothèses.
6. Choisis la prochaine phase dans le MAP, pré-enregistre via `desk ledger new` si tu veux lancer une nouvelle hypothèse, sinon poursuis l'exploration descriptive sur les axes non couverts.

Tout le code est testé, le journal est vérifié à chaque fin de session, et chaque chiffre dans un rapport pointe vers un artefact (`*.csv`, `*.md`, `*.db`).
