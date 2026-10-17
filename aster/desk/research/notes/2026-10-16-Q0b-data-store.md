# Q0b — Restauration du store R2

Date : 2026-10-16

## Résultat vérifié

- `uv run desk data import-r2` : exit 0. 722 partitions mensuelles de 12 symboles importées dans `data/r2/`, uniquement sous le cutoff exclusif `2024-07-01T00:00:00Z`.
- `uv run desk data audit-r2 --sha256` : exit 0, `ok: true`, 722 partitions, 31 371 418 lignes, 1 923 359 791 octets, 12 symboles, SHA-256 recalculés et conformes aux manifestes.
- Aucun fichier de données de marché n’a été supprimé ni ajouté au commit. Les fichiers sous `data/` restent locaux/ignorés.
- `uv run pytest -q` : exit 0; suite verte. Avertissements `NearConstantInputWarning` existants dans les tests N2, non bloquants.

## Critère Q0b non satisfait

`uv run desk data check` retourne exit 0 mais son JSON contient des erreurs pour les 5 symboles configurés : les fichiers quotidiens legacy `data/ohlcv/binance/*/1d.parquet` sont absents. Cette commande ne prend pas de liste de 12 symboles et ne vérifie pas le store R2. Le contrôle R2 équivalent est vert sur les 12 via `desk data audit-r2 --sha256`, mais le critère littéral de `research/QUEUE.md` (« data check green on the 12 symbols ») n’est pas rempli. Q0b reste donc bloqué; son critère n’a pas été réécrit.

Aucune analyse de rendements ou statistique n’a été menée sur les données post-cutoff; aucune donnée de holdout n’a été importée ou lue dans cette étape.
