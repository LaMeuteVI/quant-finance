# Rapport de recherche — 2026-10-14 (session 2)

## Décisions attendues de Samuel

- **Aucune** action requise. Session purement descriptive.
- **Décision stratégique à valider** : BTC/ETH N1→N5 ont produit **0 ledger hypothesis** sur BTC et **1 candidat backlog** sur ETH (`fvg_down_entry_h1`). Aucun edge technique tradable net de frais et de placebo. Trois voies de suite :
  1. **Inter-actifs 6.1/6.2/6.3** (résiduels factoriels, lead-lag sur résiduels, panel) sur les 12 symboles survivants + XMR.
  2. **Passer le panel** directement (XMR, BNB, XRP, SOL, LINK, DOGE) sans BTC/ETH comme cœurs — l’hypothèse cross-sectionnelle peut exister sans signal single-name.
  3. **Cadrer XMR** comme garde-fou survivant dès maintenant (asset delisted 2024-02-01) avant que les autres livrent.
- Je recommande la voie (1) : inter-actifs a déjà la tuyauterie (`inter_asset_n2.py`), les résiduels existent, et un lead-lag résiduel ou un facteur cross-section est exactement le type d’edge qui échappe aux primary features single-name.

## Avancées du jour

### BTC/ETH N1 — analyse technique que tout le monde voit (descriptif, pré-cutoff strict)

- Catalogue implémenté : MA crossovers 20/100 et 5/20, RSI(14) zones, Bollinger 20/2σ, Donchian 20, pivots weekly, Fibonacci 0,382/0,5/0,618 + 4 placebos 0,55/0,6/0,65/0,7, FVG 3-bar daily.
- Cibles : log-returns forward à 1/3/7/14 jours. **112 cellules par actif** × BTC + ETH.
- Tests : moyenne conditionnelle + t-test, **5 000 bootstraps** à blocs circulaires, **placebo = horizon suivant** (révise la première version qui décalait l’event-time — capturait de l’autocorrélation mécanique), inverse, BH-FDR.
- **BTC : 0 cellule retenue** sur 112. Tous les signaux `*_above` (close > fib, RSI > 70, etc.) ont des t-stats très significatifs à 3/7/14 jours, mais **le placebo à l’horizon suivant est aussi significatif** : l’edge apparent est l’uptrend structurel, pas un signal tradable.
- **ETH : 1 cellule retenue** : `fvg_down_entry_h1` (entrée dans un gap baissier 3-bar daily, horizon 1 jour). Moyenne fwd_1d = **−1,05 %** (t=−2,67, BH q=0,026), bootstrap [−1,80 %, −0,38 %] exclut 0, placebo à 3 j non significatif (p=0,097), inverse (fvg_up_entry) ne domine pas. **Mécanisme ambigu** (continuation baissière vs mean-reversion du gap) et **ETH-only**. Va au **backlog**, pas au ledger.
- Artifacts : `research/assets/2026-10-14-btc-n1-ta.{md,csv}`, idem ETH. Tests `tests/test_n1_ta.py` verts (RSI, Bollinger, Donchian, SMA cross, Fib).
- Bilan d’étape : **BTC et ETH n’ont livré aucun primary feature tradable sur N1, N2, N4, N5.** N3 a livré du forecast, pas de l’alpha. N6/N7 restent gated.

### Bug trouvé et corrigé pendant la session

- Première version du placebo dans `n1_ta.py` décalait l’event-time (mask.shift(1)) puis testait sur la cible originale. Avec des forward returns à 1 j, cible décalée d’1 j = cible à 2 j, qui partage ~24 h avec la cible originale → corrélation mécanique énorme → « placebo » presque aussi fort que signal → filtre trivial. 26 cellules BTC « retenues » à tort. Corrigé : placebo = next-longer horizon (cible 3j testée contre signal à 1j, etc.). Nouveau résultat : 0/112 BTC, 1/112 ETH. **Avant de dire « ce signal marche », le placebo doit vraiment mesurer autre chose.**

## Verdict du jour

- **0 ledger hypothesis** sur BTC et ETH (1–5).
- **0 backtest** de stratégie.
- **0 ouverture du holdout.**
- **1 candidat backlog** : `fvg_down_entry_h1` ETH (mécanisme ambigu, ETH-only, BH q=0,026 dans grille de 112).

## Risques et anomalies

- **Faux positifs en série** : le filtre placebo « event-time shift » est un piège classique en event study. Tout event study futur dans ce desk doit utiliser un placebo qui **ne partage pas la masse de probabilité avec la cible originale**. J’ai documenté ça dans le code (`event_grid`).
- **Uptrend structurel** : la grille N1 montre que **presque tous les signaux techniques de momentum** ont une t-stat > 3 sur 3/7/14 j mais aucun ne surpasse l’uptrend. C’est cohérent avec l’uptrend BTC/ETH 2017–2024 mais c’est aussi **la raison pour laquelle la plupart des backtests crypto « simples » survivants sont des artefacts de tendance**. Une stratégie de momentum ne peut être enregistrée qu’après conditionnement explicite au régime (filtre N4) et test de breakdown par régime.
- **Pas de capacité chiffrée** pour le candidat FVG : 203 observations sur 7 ans = ~30 trades/an, taille d’ordre non chiffrée, edge brut vs coût non vérifié. Avant ledger : il faut un calcul de coût aller-retour intraday ETH + une estimation de capacité.

## Demain / prochaine étape

- **Inter-actifs 6.1/6.2/6.3** : matrice de corrélation par horizon, débruitée Marcenko-Pastur, puis lead-lag sur résiduels factoriels BTC. Si un lead-lag résiduel émerge, c’est une primary feature cross-asset. Si non, panneau panel.
- En parallèle : N0 rapide sur XMR, BNB, XRP, SOL, LINK, DOGE pour avoir l’atlas complet.
- Aucun ledger hypothesis tant qu’une primary feature n’est pas confirmée.

## Fichiers vivants

- `research/MAP.md` — BTC/ETH N1 à jour, ligne ETH N1 ajoutée.
- `research/BACKLOG.md` — sections 7–12 réécrites, candidat FVG ETH en backlog.
- `research/2026-10-14-btc-eth-n1-ta-prereg.md` — pré-enregistrement descriptif.
- `src/aster/research/n1_ta.py` — module partagé BTC/ETH (496 l.).
- `tests/test_n1_ta.py` — tests verts.
- `research/assets/2026-10-14-btc-n1-ta.{md,csv}` — grille BTC 112 cellules, 0 retenue.
- `research/assets/2026-10-14-eth-n1-ta.{md,csv}` — grille ETH 112 cellules, 1 retenue.

## Suite immédiate

- `uv run pytest -q` : **vert**.
- `uv run desk journal verify` : **vert**, 0 record invalide.
- Pas de modification de `risk/`, `execution/`, `policies/`, `config/risk_limits.yaml`.
- Pas d’armement live (`ASTER_LIVE_ARMED` non touché).
