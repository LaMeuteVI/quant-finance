---
name: aster-autopilot
description: Autonomous research mode for long /goal runs, Kanban goal cards and worker crons. Works research/QUEUE.md item by item without stopping to ask, using pre-made decisions in research/DECISIONS.md. Load for any "continue", "keep going", "/goal" or overnight research request.
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [quant, autonomy, goal, orchestration, crypto]
    category: quant-desk
    requires_toolsets: [terminal]
---

# Aster autopilot

## Why this skill exists
Long runs failed for three reasons. (1) The stop list was so broad that any substantial step counted as a "human decision", so every goal ended on a question and the judge parked it. (2) The plan lived in chat messages ("B–G") that a new session, a cron or a compressed context could not see. (3) Turns were spent polling a running worker instead of advancing other work.

This skill fixes all three. **The plan lives in `research/QUEUE.md`, decisions already made live in `research/DECISIONS.md`, and you only stop on a RED item.**

## Sources of truth (read at the start of every session, cron or goal turn 1)
1. `research/QUEUE.md`: ordered work items, each with a status, a definition of done (DoD) and its skills. **This is the standing goal.** A chat message never replaces it; if Samuel gives a new direction in chat, write it into QUEUE.md first (new item or re-order), commit, then work.
2. `research/DECISIONS.md`: decisions already taken, the GREEN/ORANGE/RED autonomy charter, and default answers to the recurring questions.
3. `research/MAP.md`, `research/BACKLOG.md`, `uv run desk ledger list`: the scientific state.
4. `Status.md` (repo root) only for orientation; QUEUE.md wins on any conflict.

## Autonomy charter (summary; full text in DECISIONS.md)
- **GREEN — do it, don't ask.** Choosing the next item, ordering, scope inside an item, writing a preregistration for exploration, code + tests in `src/aster/research/`, `src/aster/data/` (except holdout read paths), running descriptive studies on pre-cutoff data, importing free public data into the sealed store, committing and pushing to `feat/aster-agent`, merging your own research worktrees after the tests pass, spawning `delegate_task` sub-agents, updating MAP/BACKLOG/QUEUE/Status.
- **ORANGE — do it, then report it.** Registering a ledger hypothesis that meets the protocol, running dev backtests through `desk backtest`, rejecting a hypothesis, closing a research class as null *after* the coverage rule below, choosing between two technically valid methods. Log each in DECISIONS.md (one line: date, decision, reason, commit) and keep working.
- **RED — stop and ask.** Spending money; anything live, keys, secrets, withdrawals; `desk promote`, `desk kill off`; editing `risk/`, `execution/`, `policies/`, `config/risk_limits.yaml`; reading a holdout (`--sample holdout` / `read_holdout`); starting paper trading; deleting data or rewriting git history; changing the brief's success criteria.

If a question is not RED, it is not a question: pick the option you would recommend, write it in DECISIONS.md, continue. "Je recommande X, je le fais" replaces "Dis-moi 1, 2 ou 3".

## The turn protocol (each turn of a /goal, each cron run, each Kanban goal card)
1. `cd` to the desk, `git pull --ff-only`, check `research/.autopilot.lock` (see Concurrency).
2. Read QUEUE.md. Take the first item in `IN_PROGRESS`, else the first `READY` whose dependencies are `DONE`.
3. Mark it `IN_PROGRESS` with the date. Load the skills the item names (start with `quant-orchestrator` for routing).
4. Do the work to its DoD. A DoD always includes: preregistration note written *before* the data is touched (for exploration items), artifacts on disk, `uv run pytest -q` green, MAP/BACKLOG updated, commit pushed.
5. Mark it `DONE` with commit hash + artifact paths + a one-line finding. If the work produced new questions, append them as new items (`READY` or `IDEA`) at the right priority; do not ask Samuel about them.
6. End the turn with the handoff block below, then go straight to the next item if budget remains.

An item too large for one turn is split into sub-items in QUEUE.md (`Q12a`, `Q12b`, …) so that each turn closes something.

## Handoff block (last lines of every turn's answer)
The /goal judge only sees the last ~4 KB of your answer. End every turn with exactly this block, so it can tell progress from a stop:

```
QUEUE — fait: Qx (commit abc1234, artefact path) · en cours: Qy · restants READY: N
Prochaine action: <verbe + objet>, je continue.
Décision humaine requise: aucune
```

Only when a RED item is the *only* thing left: `Décision humaine requise: OUI — <the RED item, the options, your recommendation>`. Never end with a question otherwise. Never write "j'attends ton choix" for a GREEN or ORANGE decision.

## Waiting on something
- A sub-agent or a long computation you launched: start it in the background (`terminal(background=true, notify_on_complete=true)`) and **work on another READY item meanwhile**. Do not poll it turn after turn; the /goal judge parks the loop on your background process when nothing else is left.
- A Kanban worker you created: do not babysit it. Mark the dependent QUEUE item `BLOCKED_ON <card id>` and move on. Review its result when it completes.
- Never spend a turn only to report that something is still running.

## Coverage rule before calling a class "null"
A null on one signal class is not a null on the brief. Before writing "on a fait le tour" or proposing to stop, check the brief's coverage list in DECISIONS.md (horizons from 1 minute to 1 week, taker flow, funding, information bars, residual lead-lag at intraday lags, panel, seasonality, jumps, cross-venue check). Every cell not covered is a QUEUE item, not a reason to stop. Closing the whole research programme is a RED decision.

## Concurrency (one writer at a time)
- Before working: if `research/.autopilot.lock` exists and is less than 3 h old, another run owns the desk. Then do read-only review work (check the last DONE item's numbers against its artifacts) or exit cleanly with "verrou actif, aucun travail en double". Otherwise write the lock (`date -u +%FT%TZ > research/.autopilot.lock`; it is gitignored).
- Remove the lock at the end of the run.
- Research worktrees (`.worktrees/<id>`) are merged into `feat/aster-agent` by the run that created them, as soon as their DoD is met. Uncommitted work must never sit across sessions: commit to the worktree branch at minimum.

## Sub-agents
Use `delegate_task` for parallel N-level work (one sub-agent per asset, as the brief's section 10 says). Brief each with: desk path, QUEUE item id and DoD, the preregistration file to follow, output path, "do not read other sub-agents' outputs", "no ledger writes". Then the Skeptic on the merged result. You alone update QUEUE, ledger and verdicts.

## Report to Samuel
- Per turn: the handoff block only.
- Once a day (or when an item produces a candidate): `reports/<date>-research.md` in the brief's section 10 format, and a 5-line Discord summary. No status-only messages; a message with no delta is not sent.

## Pitfalls
- Replacing QUEUE.md with a chat summary, or defining work items only in chat ("B–G").
- Asking Samuel to choose between options you can rank yourself.
- Declaring the research closed after N negative items while the coverage list still has gaps.
- Polling a running worker; status-only cron reports.
- Letting a research worktree stay dirty overnight.

## Verification
`git log` shows one or more commits per DONE item; every DONE line in QUEUE.md has a commit and an artifact path; `uv run pytest -q` green; no `IN_PROGRESS` item older than 24 h without a note.
