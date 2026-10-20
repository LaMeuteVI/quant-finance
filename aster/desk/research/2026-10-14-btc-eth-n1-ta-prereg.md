# BTC/ETH N1 — pré-enregistrement descriptif des signaux techniques communs

**Date :** 2026-10-14
**Statut :** étude descriptive uniquement ; pas de ledger hypothesis, pas de backtest, pas de holdout, pas d’alpha claim.
**Cutoff exclusif :** `2024-07-01T00:00:00Z`.

## 1. But

Tester causalement, sur BTC et ETH, les signaux techniques que tout le monde regarde — formalisés de manière unique et pré-enregistrée — et mesurer **deux choses** :

1. Est-ce que le signal prédit le rendement forward ? Event study contre placebo.
2. Est-ce que l’**inverse** prédit mieux ? Puisque les stops s’accumulent sur les niveaux vus par la foule (lopez-de-prado-afml ch11, chan-machine-trading ch07).

Un signal nu qui ne bat pas son placebo **et** dont l’inverse n’est pas dominé par le signal direct est déclaré **bruit** dans le rapport — conclusion utile, leçon ajoutée au dossier d’actif.

## 2. Données et période

- Source unique : `aster.data.r2_klines` (Binance Vision spot 1m).
- Univers : `BTCUSDT`, `ETHUSDT`.
- Fenêtre d’estimation : `[2017-08-17, 2024-06-30]` pour BTC, `[2017-11-09, 2024-06-30]` pour ETH.
- Minutes figées (`trades == 0`) : exclues des rendements et de toutes les features dérivées du close ; incluses dans la grille temporelle des niveaux (un support vu à 11 000 USD existe que la minute ait traded ou non).

## 3. Signaux testés (catalogue N1)

1. **Croisement de moyennes mobiles** : `sma(20,100)` (long) et `sma(5,20)` (court), événement `crossover(±1)`.
2. **RSI(14) zones** : `rsi < 30` (oversold), `rsi > 70` (overbought), sur daily.
3. **Bollinger Bands(20,2σ)** : `close < lower`, `close > upper`.
4. **Donchian breakout 20 j** : `close > high_20`, `close < low_20`.
5. **Pivots weekly** : support/résistance calculés sur `(H+L+C)/3` hebdomadaire classique, distance au pivot en σ locale.
6. **Fibonacci retracements** : niveaux 0,382 / 0,5 / 0,618 sur le swing haut/bas des 252 j, **plus placebos 0,55 / 0,60 / 0,65 / 0,70** (même type de structure, pas de justification technique — c’est le falsifier).
7. **Fair Value Gap (FVG, 3-bar)** : gap non comblé up/down en daily ; événement `entry`.
8. **Order block (OB) daily** : dernière bougie opposée avant un swing FVG, marquée par son midpoint.

Cibles : `fwd_returns ∈ {1d, 3d, 7d, 14d}` (log-returns).

## 4. Tests appliqués à chaque (signal, horizon)

Pour chaque cellule de la grille :

1. **Point estimate** : `t-stat` de la moyenne des `fwd_returns` conditionnels à l’événement, vs 0.
2. **Placebo event-time** : même test sur cible décalée de 1 jour (kill le timing).
3. **Inverse** : tester `-signal_event` (par exemple `close > upper` remplacé par `close < lower`, ou `rsi < 30` remplacé par `rsi > 70`) ; vérifier que l’inverse n’a pas le même signe et la même magnitude.
4. **Bootstrap par blocs circulaires** : `5 000` resamples, longueur de bloc `max(5, h)`, IC 95 % de la moyenne conditionnelle.
5. **BH-FDR** sur la grille entière (toutes cellules × tous actifs).
6. **Stabilité par régime** : signer le résultat par `regime_trend ∈ {-1, 0, 1}` et `regime_vol ∈ {0, 1}` (libellés du N4 descriptif).

Rétention conjointe : **BH q < 0,05** ∩ **bootstrap exclut 0** ∩ **placebo non-significatif** ∩ **l’inverse ne domine pas**.

## 5. Garde-fous

- Aucun chiffre du rapport ne vient d’un artefact `post > 2024-06-30`.
- Aucun appel à `r2_backtest_store` ou à la pipeline `desk backtest`. Étude purement descriptive.
- Aucun secret, aucun ordre. Le module ne touche pas à `risk/`, `execution/`, `policies/`, `config/risk_limits.yaml`.
- Les placebos sont déclarés comme tels dans le CSV final, pas confondus avec les vrais niveaux.

## 6. Artefacts

- `src/aster/research/n1_ta.py` (module partagé BTC/ETH).
- `tests/test_n1_ta.py` (tests de référence : rsi, bollinger, fvg).
- `research/assets/2026-10-14-btc-n1-ta.{md,csv}`
- `research/assets/2026-10-14-eth-n1-ta.{md,csv}`

## 7. Hypothèses à ne PAS enregistrer depuis ce fichier

- « RSI < 30 produit un reversal 1d » → ne pas pré-enregistrer, parce que c’est la définition même du signal testé, pas une découverte.
- « Bollinger upper est un signal de retournement » → idem.
- « Donchian 20j breakout est un signal de continuation » → idem.

Une conclusion descriptive **peut** mener à un ledger hypothesis **uniquement** si la cellule survit au filtre conjoint **et** que le mécanisme est identifié **et** que l’estimation coûts/capacité passe (cf. message.txt §1, §9).
