# Faire tourner Aster en continu

Guide pour Samuel : pourquoi Aster s'arrêtait, et comment le relancer en mode autonome.

## 1. Diagnostic : pourquoi il s'arrête et perd le fil

| Symptôme dans Discord | Cause réelle | Correctif |
|---|---|---|
| « J'attends ton choix A/B/C/D », « Dis-moi 1, 2 ou 3 », puis `Goal parked (judge)` | `hermes.md` §5 et `Status.md` §4 lui demandent de s'arrêter à chaque « chantier substantiel », au holdout, après « 3+ axes négatifs » et pour tout budget. Toute étape devient une décision humaine. Le juge de `/goal` voit une question en fin de réponse, conclut `blocked`, et le goal se gare. | Charte VERT/ORANGE/ROUGE dans `desk/research/DECISIONS.md` : seule la liste ROUGE (argent, live, clés, lecture du holdout, paper, policies/risk) déclenche une question. |
| `/goal continue B C D E F G` → « À quoi correspondent B–G ? » | La liste B–G n'existait que dans un message Discord. Un nouveau goal, une session cron ou un contexte compressé ne la voit pas. `hermes.md` dit même que le goal vit « dans la commande /goal, pas dans un fichier ». | Le plan vit dans `desk/research/QUEUE.md`. Le goal se résume à « exécute QUEUE.md ». |
| `Iteration budget exhausted (60/60)` | `agent.max_turns` vaut 60 dans ton profil (la valeur par défaut d'Hermes est 500). | Le passer à 300 (section 3). |
| 8 tours de suite « le run #35 est toujours actif » | Il surveillait un worker Kanban au lieu d'avancer sur autre chose. Chaque tour de goal était brûlé en polling. | Règle « pas de polling » : il lance en arrière-plan, travaille l'item suivant, et Hermes gare le goal tout seul sur le process. |
| Cron toutes les 90 min qui répète « aucun delta, Kanban inaccessible » | Le cron était en lecture seule. Il rapportait l'état sans jamais rien faire avancer, et n'avait pas le toolset Kanban. | À supprimer. Le remplacer par un cron **worker** qui exécute la file (section 4). |
| Correction N1 non commitée depuis hier | Aucune « définition de fini » n'imposait commit et merge. | Item Q0 + règle « jamais de worktree sale entre deux sessions ». |

### Problèmes de fond sur la recherche
Il ne s'agit pas seulement de l'outillage :

1. **Le vrai holdout est gratuit.** `import_r2()` ne télécharge que les mois **avant** 2024-07-01, d'où la conclusion « pas de holdout propre sans acheter des données ». Or Binance Vision (et sans doute ton bucket R2) contient 2024-07 → 2026-10 gratuitement. Le holdout « option A » (avril–juin 2024) est contaminé : les 7 axes l'ont lu. Correctif : Q1 importe le post-cutoff dans un store scellé, sans le lire.
2. **« Acheter Tardis/Kaiko » n'est pas nécessaire pour commencer.** aggTrades et trades Binance sont gratuits sur tout l'historique, pas seulement juin 2024. Les données de funding, premium, mark price et open interest des perps le sont aussi.
3. **« On a fait le tour » est faux.** N1, N2 et l'inter-actifs ont surtout été faits à l'horizon **journalier** (1/3/7/14 j). Le brief demande de 1 minute à 1 semaine : lead-lag à 1–30 min, saisonnalité des fixings de funding, flux taker sur barres d'information, sauts intraday. Et le funding/basis, la prime la mieux documentée en crypto, n'a jamais été étudié. C'est le Bloc 1 de QUEUE.md, en priorité.

## 2. Ce qui a été ajouté au repo

- `skills/aster-autopilot/SKILL.md` : le mode autonome. Protocole par tour, bloc de passation lisible par le juge, pas de polling, verrou anti-doublon, règle de couverture avant de déclarer un « null ».
- `desk/research/QUEUE.md` : la file de travail (Q0 → Q20). Les anciens A–G y sont mappés.
- `desk/research/DECISIONS.md` : la charte d'autonomie et les décisions D1–D8, déjà prises pour qu'il ne les redemande pas. **Relis-la avant de merger** : en mergeant, tu l'adoptes. Change ce qui ne te convient pas.

## 3. Mise en place sur le VPS (5 minutes, pas besoin de me donner SSH)

```bash
cd /root/quant-finance && git fetch origin && git checkout feat/aster-agent
git merge origin/claude/upbeat-lovelace-1uluji      # ou merge de la PR sur GitHub
cd aster && ./install.sh                             # copie le nouveau skill dans le profil
```

Dans `~/.hermes/profiles/aster/config.yaml` :

```yaml
agent:
  max_turns: 300        # tu es à 60 : c'est le "Iteration budget exhausted (60/60)"
goals:
  max_turns: 60         # 60 tours de goal avant pause, au lieu de 20
```

Puis redémarre la gateway (`hermes gateway restart`, ou ton service systemd).

À éditer toi-même : ce sont des fichiers d'instructions protégés, je n'y ai pas touché.
- `hermes.md` §5 « When to stop and ask Samuel » : remplacer la liste par « Voir research/DECISIONS.md, niveau ROUGE uniquement ». Supprimer « 3+ consecutive negative axes », « Holdout seal definition » et la ligne Tardis.
- `hermes.md` §0 « Standing goal : maintained as a Hermes in-session /goal command, not as a markdown file » : remplacer par « Standing goal : research/QUEUE.md ».
- `hermes.md` §4 « Spawn Forge / Kanban » : à retirer si tu valides D6.
- `Status.md` §4 « Samuel decides » : remplacer par un renvoi vers QUEUE.md.

Ménage des crons :
```bash
hermes -p aster cron list
hermes -p aster cron remove 9130e32f3b69     # "Avancement Aster — toutes les 90 min"
```

## 4. Lancer le travail

### Option A, recommandée : un goal avec contrat, dans **un seul** canal Discord
Colle ceci tel quel :

```
/goal Exécuter desk/research/QUEUE.md avec le skill aster-autopilot, item par item, jusqu'à ce qu'aucun item ne soit READY
verify: chaque item passé DONE dans QUEUE.md cite un commit poussé et un artefact ; uv run pytest -q est vert
constraints: cutoff 2024-07-01 pour l'exploration ; aucun holdout lu ; pas de live, clé, ordre ni paper ; pas de modification de risk/, execution/, policies/, config/risk_limits.yaml
boundaries: aster/desk uniquement, branche feat/aster-agent
stop when: la seule action restante est de niveau ROUGE dans desk/research/DECISIONS.md
```

- Toujours dans le même canal ou thread : la session et le goal y sont rattachés. Pour reprendre après une pause : `/goal resume`, jamais un nouveau `/goal` avec une liste en texte.
- Pour ajouter une consigne sans casser la boucle : `/subgoal <texte>`. Mieux encore, ajoute un item dans QUEUE.md.
- Optionnel, porte qualité déterministe (admin gateway requis) : `/goal gate add cd /root/quant-finance/aster/desk && uv run pytest -q`.

### Option B : la nuit, un cron worker au lieu d'un cron de statut
```bash
hermes -p aster cron create --name aster-autopilot --deliver local "every 2h" \
  --workdir /root/quant-finance/aster/desk --skill aster-autopilot --skill quant-orchestrator \
  --skill quant-backtest-hygiene --skill lopez-de-prado-afml \
  "Charge le skill aster-autopilot. Lis research/QUEUE.md et research/DECISIONS.md. Exécute jusqu'à 3 items READY dans l'ordre, chacun jusqu'à sa DoD (commit poussé). Respecte le verrou research/.autopilot.lock. Ne pose aucune question sauf pour un item ROUGE. Termine par le bloc de passation."
```
Le verrou empêche le cron et un `/goal` actif de travailler en même temps sur le desk.

### Option C : un item long = une carte Kanban goal-mode
```bash
hermes kanban create "Q8 funding/basis/carry" --assignee aster --goal --goal-max-turns 40 \
  --workspace worktree --skill aster-autopilot --skill chan-machine-trading \
  --body "Exécuter l'item Q8 de research/QUEUE.md jusqu'à sa DoD. Charte : research/DECISIONS.md."
```

## 5. Ce que tu dois encore trancher (ROUGE, et rien d'autre)
- Lecture d'un holdout pour une hypothèse, quand une candidate passe le dev gate.
- Passage en paper.
- Achat de données L2 payantes, seulement si une candidate en a besoin.

Tout le reste, il le fait et le note dans DECISIONS.md.
