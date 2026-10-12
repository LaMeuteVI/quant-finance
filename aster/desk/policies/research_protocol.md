# Research protocol

From idea to decision. Each stage has an owner, an output and an exit criterion. Skipping a stage is a protocol breach and must be reported.

## Stage map
| Stage (ledger status) | Output | Exit criterion |
|---|---|---|
| 0. Idea | memo in `research/` | passes the triage below |
| 1. `preregistered` | ledger entry (immutable hash) | statement, mechanism, falsification, numeric prediction written BEFORE any data is touched for this idea |
| 2. `backtest_passed` | dev trial artifacts | dev gate passed (backtest_standard.md) within 5 versions |
| 3. `holdout_passed` | holdout trial artifact | one-shot holdout gate passed |
| 4. `paper` -> `paper_passed` | journal + `desk paper review --record` | >= 28 days, results consistent with backtest, no kill trip |
| 5. `live_pilot` -> `live` | promotion record (human) | promotion_policy.md |
| any -> `rejected` / `paused` / `retired` | ledger lesson | always write why |

## 0. Triage (before registering)
1. `desk ledger list --text <keywords>` and `--status rejected`: was it tried? If rejected, only re-open with a stated reason why conditions changed (new data, new venue, structural change), registered as a new hypothesis in the same `family`.
2. Name the economic mechanism: who is on the other side and why do they keep losing? (risk premium, behavioural bias, structural flow, liquidity provision, market friction). No mechanism = data mining; reject.
3. Capacity and cost sanity: expected gross edge per trade vs round-trip cost (fees + slippage + funding). If gross edge < 3x cost, reject.
4. Crowding and decay: is this a well-known factor? Expect decayed performance vs published results.

## 1. Pre-registration
Use `templates/hypothesis.md`. Required:
- **Statement**: falsifiable, specific universe, horizon, signal.
- **Mechanism**: one paragraph.
- **Falsification**: the exact result that kills it.
- **Prediction** (JSON, numeric): at least `sharpe_ann_min` and `max_drawdown_floor`. You may tighten desk gates, never loosen them.
- **Family**: groups variants of the same idea; the DSR trial count is per family. Choose it honestly; splitting one idea into many families to dodge the deflation is a breach.

## 2. Dev research loop
- Run only through `desk backtest`. Each run is a counted trial.
- Each new version: one written reason in `--notes`, based on a diagnosed failure mode (where and why it lost), not on "try another parameter".
- Parameter sweeps: register the sweep as one version, run all configs, export the returns matrix and report PBO (`desk pbo`). PBO > 0.3: reject the sweep.
- Max 5 versions per hypothesis (enforced). Then reject and record the lesson.

## 3. Holdout
Only after `backtest_passed`. Read once (enforced). No change of any kind after reading it; failure means rejected.

## 4. Independence of research agents
When several subagents generate ideas (scout, researchers), they work in parallel without reading each other's memos, then a skeptic reviews all of them. This avoids anchoring. See skill `aster-desk`.

## 5. Post-mortem and memory
- Weekly critic review (cron) writes `reports/YYYY-MM-DD-postmortem.md` and one ledger lesson per finding.
- Lessons are short, factual, searchable: what was tried, regime, what failed, why we think it failed.
- Failed ideas are the most valuable records. Never delete them.
