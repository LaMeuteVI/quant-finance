# Aster desk research programme — SUSPENDED 2026-10-19 by Samuel, REOPENED 2026-10-19

**Status**: suspended (Samuel explicit « Je rouvre le programme »). Closure revoked; the F-track was not sufficiently diagnosed before closure (F3 is a near-miss on costs, F1v2 didn't test the carry hypothesis), so additional work is required before any closure decision.

**Branch**: `feat/aster-agent`.
**Commit suspend**: `005c76a` (closure commit).
**Commit reopen**: see `git log origin/feat/aster-agent` (this session).

## Final state

- **Items QUEUE** : 26 DONE, 1 BLOCKED (Q18 — financial ML, primary feature never qualified), 0 READY/IDEA/IN_PROGRESS/REJECTED-in-flight.
- **Tests** : 591 passed, 1 skipped, 46 warnings (`uv run pytest -q`).
- **Track F** : 3 strategies registered, 3 falsified.
- **Coverage check** (DECISIONS.md §3) : 12/13 axes covered on free pre-cutoff Binance Vision data, 1 cell falsified by 4h cross-check (Q5-V4 month-end), 1 cell RED (D3 paid data).
- **No holdout read**, **no live**, **no paper**, **no order**, **no key**, **no spend**.

## Track F summary

| Strategy | Sharpe_ann | DSR | Max DD | Verdict | Ledger entry | Hash |
|---|---:|---:|---:|---|---|---|
| F1v2 (funding_carry_dn) | 0.18 | — | — | REJECTED (gates) | H-20261018-003 | c8b1e88 |
| F2 (crowding_premium) | -0.62 | 0.05 | -0.74 | REJECTED (gates) | H-20261018-005 | 2d71a19 |
| F3 (vol_target_trend_ensemble) | 0.70 | 0.91 | -0.337 | REJECTED (gates) | H-20261019-001 | 18cd2a2 |

Family trial counts :
- F1 family `funding-carry`: 2 trials (H-20261016-002 v1, H-20261018-003 v2). 3 trials remaining (max 5).
- F2 family `crowding-premium`: 1 trial (H-20261018-005). 4 trials remaining.
- F3 family `btc-daily-tsmom`: 2 trials (H-20261013-001 v1, H-20261019-001 v2). 3 trials remaining.

## Coverage check (DECISIONS.md §3)

| Cell | Status | Source | Verdict |
|---|---|---|---|
| Horizons 1m-1w | COUVERTE | Q5-V1, Q9, Q21, Q22 | — |
| Bars (time + information) | COUVERTE | Q4 | — |
| Flow (taker ratio, signed cumul, Kyle λ, Amihud, Roll, VPIN) | COUVERTE | Q6, Q12, Q21, Q22 | — |
| Seasonality (hour, weekday, funding fixings) | COUVERTE funding | Q5-V2 | funding autocorr mean 0.785, RETAIN |
| Seasonality (month-end / turn-of-month) | VIDE cross-check | Q5-V4 | 1d RETAIN bar, 4h falsifies (cross-sectional co-movement artefact) |
| Jumps + post-jump + CUSUM + SADF | Jumps+CUSUM VIDES, SADF REPLETI | Q5-V3 | BTC SADF +8.51, ETH +4.71 |
| Volatility (GARCH/EGARCH/HAR-RV) | COUVERTE | Q10 | — |
| Regimes | COUVERTE | Q11 | — |
| Perps (funding/basis/OI) | COUVERTE | Q3, Q3b, Q8 | carry >= 30 bps/yr (Q8 floor) |
| Inter-asset | COUVERTE | Q7, Q13, Q14 | — |
| Literature | COUVERTE | Q16 | — |
| Second venue check | RED | — | D3 paid data |
| F-track N7 synthesis | 0 live candidate | Q19 | allocation = 0 on all 3 |

## Remaining items (carry over after closure)

- **Q18 — N6 financial ML** is `BLOCKED_ON a primary feature from Q5–Q14`. No primary feature has qualified. The block persists as documentation only.

## Reset criteria (if the programme were to restart)

If Samuel ever instructs a restart of the programme, the following are the explicit required actions:

1. Add a new QUEUE item « Q24 — programme restart » at the top.
2. The new family cannot be in an already-falsified family without Samuel's explicit sign-off (D1 closes that loop except for spec-approved Red-Lit re-tests).
3. Cost-hurdle carries over (D5: VIP 0 spot 10 bps/side, perp 5 bps/side plus grid; ×2/×3 for stress only).
4. D3 paid-data axes stay RED until Samuel sets a budget.
5. The holdout (2024-07-01Z onwards) remains unread.

## Cron status

- All Aster-Profile crons are paused since 2026-10-13/16 (aster-daily-desk, aster-weekly-postmortem, aster-risk-watchdog, aster-paper-trade, aster-research-cron `f952bdbebf25`, aster-autopilot).
- No cron fires are scheduled to advance research while the programme is closed.

## Files of record

- `research/QUEUE.md` — final queue snapshot.
- `research/BACKLOG.md` — entry `Falsified-on-coverage (2026-10-19, autopilot stop)`.
- `research/memos/2026-10-19-Q5-V2-N19.md` — seasonality funding RETAIN, spot falsified.
- `research/memos/2026-10-19-Q5-V3-N20.md` — SADF explosif RETAIN.
- `research/memos/2026-10-19-Q15-N21.md` — FVG panel FALSIFIED.
- `research/memos/2026-10-19-Q5-V4-N22.md` — month-end RETAIN at 1d, 4h falsifies.
- `research/memos/2026-10-19-F3-N17.md` — F3 REJECTED.
- `research/memos/2026-10-19-Q19-N18.md` — N7 synthesis 0 candidate.
- `reports/2026-10-19-research.md` — daily report.
- `research/atlas/q5_v2_seasonality.json`, `q5_v3_jumps.json`, `q15_fvg_panel.json`, `q5_v4_monthend.json`, `q19_synthesis.json`.
- `research/notes/2026-10-19-Q5-V2-prereg.md`, `2026-10-19-Q5-V3-prereg.md`, `2026-10-19-Q15-prereg.md`, `2026-10-19-Q5-V4-prereg.md`.
