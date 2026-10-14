# Journal d'exploration — Aster desk crypto

**Période** : 2026-10-14 → en cours
**Cutoff exploration** : `2024-07-01T00:00:00Z`
**Politique** : chaque axe est tracé en temps réel dans ce journal, avec ses hypothèses, ses tests, ses résultats et ses conclusions. Le journal est versionné et commité sur GitHub au fur et à mesure.
**Statut de la recherche** : 0 ledger hypothesis vivante. 1 ledger hypothesis rejetée (H-20261013-001).

## Axes engagés

| # | Axe | Statut | Skills mobilisés | Artefact principal |
|---|---|---|---|---|
| 1 | Term structure intra-day (vol morning/evening, autocorr minute-par-minute) | **CLOS — 0 edge** | tsay ch02, chan ch03 | `research/notes/2026-10-14-axe-1.md` |
| 2 | Ichimoku Kinko Hyo complet | in_progress | riguet-ichimoku, chan ch03 | (à venir) |
| 3 | Mean-reversion OU + half-life + pairs | queued | chan ch03, pairs-trading-partial-cointegration | (à venir) |
| 4 | Volatility risk premium (HAR-RV + GJR-GARCH + EGARCH + SVI) | queued | tsay ch03/ch05, gatheral ch03 | (à venir) |
| 5 | TA enrichi CFA (Camarilla/Woodie pivots + Elliott proxy + Fib avancé) | queued | cfa-pm, riguet, cfa-qm | (à venir) |
| 6 | ML alpha (XGBoost + purged k-fold + DSR/PBO/MinTRL) | queued | lopez-de-prado-afml ch03/04/05/07/08/14 | (à venir) |
| 7 | Régime BTC Markov-switching → cross-section alts | queued | tsay ch04, cfa-pm | (à venir) |
| 8 | Order book microstructure proxy (Lee-Ready, Kyle, Amihud, signed flow) | queued | chan ch06, lopez ch19 | (à venir) |

## Convention de journalisation par axe

Pour chaque axe, ce journal est mis à jour avec :

1. **Date / heure UTC de début**
2. **Question de recherche précise** (statement court)
3. **Mécanisme économique attendu** (qui paie, pourquoi ça persiste)
4. **Données et période**
5. **Tests lancés** (liste exhaustive)
6. **Résultats intermédiaires** (au fur et à mesure)
7. **Faux positifs détectés et leçons**
8. **Conclusion** (ledger hypothesis registered / 0 edge / axe clos)
9. **Lien vers l'artefact** (CSV/md/code)

## Notes par axe (timeline)

### 2026-10-14T15:22:00Z — Début axe 1 (term structure intra-day)

**Question** : existe-t-il un profil de vol intra-journalier (1m) qui prédit les rendements forward à 5/15/60 minutes, en contrôlant pour le placebo et l'inverse ?

**Mécanisme attendu** :
- U-shape de vol intra-day (vol élevée à l'ouverture/fermeture, faible au milieu de la session US/EU). La crypto n'a pas d'ouverture/fermeture, mais les **sessions régionales** (Asie 00-08 UTC, EU 08-16 UTC, US 13-22 UTC) peuvent créer un profil similaire.
- Si la vol asiatique prédit la vol EU/US, on a un **lead-lag microstructurel temporel**.
- Si la décorrélation minute-par-minute aux heures de faible vol (régime calme) est plus forte, on a un **signal mean-reversion**.

**Données** : klines 1m BTCUSDT et ETHUSDT, fenêtre `[start_asset, 2024-06-30]`.

### 2026-10-14T15:28:00Z — Fin axe 1 (CLOS, 0 edge tradable)

**Résultats** :
- Autocorr minute-par-minute 1m : -0.025 (BTC) et -0.021 (ETH) en médiane, 60-62% des buckets négatifs.
- **Stabilité catastrophique** : autocorr 1m passe de -0.25 en 2017 à **+0.008 en 2023** sur BTC. Le signal a été **arbitragé** par les HFTs.
- **Multi-bar (5m, 15m) : autocorr persiste** à -0.04 à -0.07 en 2024. Signal résiduel non-arbitragé.
- **Profit net théorique** : BTC 5m 2024 = -5760 bps/jour net de coûts. **1000× trop faible** pour battre 20 bps aller-retour.
- Cross-bucket (asia→eu, etc.) : ~0.001, aucun lead temporel.
- Profil horaire de vol : trop petit pour exploitation.

**Conclusion** : 0 edge tradable. Axe clos. Aucun ledger hypothesis. Aucun backtest.

**Leçon transférable** : l'arbitrage microstructurel opère à 1m mais pas encore à 5-15m. C'est un **timing d'arbitrage** : un signal peut être mort à un bar et vivant à un autre. À réutiliser sur tous les autres axes (chercher le bar où le signal est maximal avant de le traduire en stratégie).

**Artefact** : `research/notes/2026-10-14-axe-1.md`.

### 2026-10-14T15:30:00Z — Début axe 2 (Ichimoku Kinko Hyo complet)

**Question** : les 5 lignes Ichimoku (Tenkan, Kijun, Senkou A, Senkou B, Chikou), combinées avec le filtre Kumo (nuage) et le pullback Kijun, produisent-elles un signal tradable sur klines 1m BTC/ETH ?

**Mécanisme attendu** (Riguet, formation totale Ichimoku) :
- Tenkan-sen (9-period high/low mid) au-dessus de Kijun-sen (26-period) = tendance haussière.
- Prix au-dessus du Kumo (Senkou A > Senkou B) = tendance confirmée.
- Chikou span au-dessus du prix de 26 périodes en arrière = confirmation.
- Kijun pullback : entrée long quand le prix retrace à la Kijun en tendance haussière.
- Kumo twist (Senkou A croise Senkou B) = signal de retournement majeur.

**Pourquoi sur crypto 1m** : Ichimoku a été conçu pour des bougies journalières sur actions japonaises. Sur 1m, les faux signaux sont nombreux. **Mais** le filtre Riguet (Chikou + Kijun + Kumo simultanément) peut fonctionner si on l'aligne sur la **tendance 4h ou daily** et qu'on trade les pullbacks en 15-30m.

**Hypothèse à tester** : signal "TK cross + Kumo alignment + Chikou confirmation" en daily, traduit en entrée 15m pullback. Si la combinaison 3-lignes + 1-filtre passe placebo + inverse + DSR ≥ 0.95, ledger hypothesis candidate.

**Données** : klines 1m BTCUSDT, ETHUSDT, agrégées en daily pour le signal, 15m pour l'entrée.

**Statut** : exploration démarre. Code à écrire dans `src/aster/research/ichimoku_signal.py`. Premier test : backtest descriptif des 3-règles (TK cross, Kumo twist, Kijun pullback) en daily sur BTC 2017-2024.

---
