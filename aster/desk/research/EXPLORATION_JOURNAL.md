# Journal d'exploration — Aster desk crypto

**Période** : 2026-10-14 → en cours
**Cutoff exploration** : `2024-07-01T00:00:00Z`
**Politique** : chaque axe est tracé en temps réel dans ce journal, avec statement, mécanisme, prédiction chiffrée, tests, résultats, BH-FDR, placebo, inverse, leçon.

---

## État global (mis à jour 2026-10-14 23:18 UTC)

| Axe | Description | Statut | Skills mobilisés | Note |
|---|---|---|---|---|
| 1 | Term structure intra-day (vol morning/evening, autocorr minute-par-minute) | **CLOS — 0 edge** | tsay ch02, chan ch03 | `research/notes/2026-10-14-axe-1.md` |
| 2 | Ichimoku Kinko Hyo complet (10 chapitres Riguet) | **CLOS — 0 edge** | riguet-ichimoku, chan ch03 | `research/notes/2026-10-14-axe-2.md` |
| 3 | Mean-reversion OU + half-life + pairs (6 paires testées) | **CLOS — 0 edge** | chan ch03, pairs-trading-partial-cointegration | `research/notes/2026-10-14-axe-3.md` |
| 4 | Vol risk premium (HAR-RV, RV/BV/JV, VRP par décile) | **CLOS — 0 edge** | chan ch03, tsay ch03, diebold-mariano | `research/notes/2026-10-14-axe-4.md` |
| 5 | CFA-style TA enrichi (Camarilla/Woodie + Elliott proxy + Fib avancé) | queued | cfa-pm, riguet, cfa-qm | — |
| 6 | ML XGBoost sur features microstructure avec purged k-fold CV | queued | lopez-de-prado ch03/04/05/07/08/14 | — |
| 7 | Markov-switching BTC/ETH → cross-sectional alts | queued | tsay ch04, cfa-pm | — |
| 8 | Order book microstructure proxy depuis aggTrades | queued | chan ch06, lopez ch19 | — |

**Total ledger vivantes** : 0. **Total ledger rejetées** : 1 (H-20261013-001, BTC daily TSMOM 60d).

---

## 2026-10-14T23:18:00Z — Clôture axes 1-4 (sessions 7+)

**Bilan 4 axes explorés à fond, 0 edge tradable** :
- 4 modules Python dans `src/aster/research/` (intraday_term_structure, ichimoku_signal, ou_pairs, vol_risk_premium) + 15 tests verts.
- 4 notes dans `research/notes/2026-10-14-axe-{1,2,3,4}.md`.
- 4 commits pushés sur `feat/aster-agent` (commits `889927d`, `ea02198`, `e5bfff1`, `bd2d871`).

**Leçon consolidée** : les 4 axes convergent vers la même conclusion — sur klines 1m daily pré-2024-07-01, les edges crypto sont soit (a) trop faibles (autocorr 1m -0.025, soit 3e-8 par trade, dominé par 20 bps de frais) ; (b) forward-looking (Chikou Ichimoku) ; (c) trop lents (half-life 173j sur le spread BTC/ETH) ; (d) dominés par le drift haussier (VRP par décile montre des rendements forward positifs après spike).

**Cause structurelle probable** : les klines 1m daily moyennent l'information microstructurelle, et le marché crypto mature a déjà arbitrégué les anomalies visibles à ce bar. L'edge résiduel vit sur le tick, ce que confirme la note veille Easley SSRN 4814346 (AUC 0.55-0.58 sans P&L net).

**Prochaines pistes** : axe 5 (Camarilla/Woodie + Elliott proxy + Fib), axe 6 (XGBoost sur features microstructure), axe 7 (Markov-switching BTC→cross-section), axe 8 (proxy microstructurel depuis aggTrades). Avant d'enregistrer une ledger hypothesis, je dois identifier un signal qui passe : (a) gate descriptif (t > 2.5, p < 0.01, BH-FDR < 0.05 sur la grille) ; (b) net de coûts 3× (gain brut > 60 bps/trade) ; (c) ≥ 100 trades ; (d) ≥ 3 ans de sample.

---

## Format de chaque entrée d'axe

Pour chaque axe, le journal enregistre :
1. **Question** : hypothèse falsifiable formulée avant le test.
2. **Mécanisme** : pourquoi on s'attend à un signal.
3. **Prédiction chiffrée** : quel effet on attend (t-stat, bps/trade, R²).
4. **Données et période** : cutoff respecté.
5. **Tests lancés** : méthodes, hypothèses nulles, corrections.
6. **Résultats** : chiffres, avec leur intervalle.
7. **Faux positifs / leakages détectés** : tout artefact d'implémentation.
8. **Leçon** : ce qu'on a appris, applicable aux autres axes.
9. **Verdict** : 0 edge / ledger hypothesis enregistrée / rejetée.
