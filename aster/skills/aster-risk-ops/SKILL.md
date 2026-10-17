---
name: aster-risk-ops
description: Risk operations — risk reports, kill switch and incidents, promotion evidence packs for paper-to-live decisions.
version: 1.0.0
metadata:
  hermes:
    tags: [risk, kill-switch, incident, promotion, live-trading]
    category: quant-desk
    requires_toolsets: [terminal]
---

# Risk operations

## When to Use
A risk alert, a kill-switch event, anything unexplained in the book, or Samuel asks whether a strategy can go live. Binding docs: `desk/policies/risk_policy.md`, `promotion_policy.md`.

## Procedure: incident
1. When in doubt, stop: `uv run desk kill on --reason "<what you saw>"`. Only reducing orders will pass.
2. Gather: `uv run desk risk status`, `uv run desk journal verify`, last 50 journal records, exchange status if relevant.
3. Report to Samuel immediately: what happened, current exposure, what is blocked, your hypothesis of the cause, what you need from him.
4. Write `reports/<date>-incident.md` and ledger lessons. Never clear the kill switch, never edit limits, never touch keys: those are Samuel's.

## Procedure: promotion evidence pack
Only when a hypothesis is `paper_passed` (to `live_pilot`) or has >= 90 days of pilot (to `live`).
1. Build `reports/<date>-promotion-<H>.md` with the 6 sections of `promotion_policy.md`, including the skeptic section and explicit kill criteria.
2. Recommend: go / no-go / go with smaller capital, with numbers. Do not lobby.
3. Tell Samuel the exact command to run himself, in his own terminal (not in Hermes):
   `cd ~/Desktop/Livres/Aster/desk && uv run desk promote <H> --to live_pilot`
   plus the checklist: sub-account funded with the cap only, trade-only API key with withdrawals off and IP whitelist, `risk_limits.yaml` mode/cap reviewed, `ASTER_LIVE_ARMED=1` only in the live cron's environment.

## Pitfalls
- Trying to "fix" a rejected order by resizing to sneak under a limit: the limit is the answer.
- Treating the agent rules as the safety net; the coded gate and the exchange sub-account cap are.

## Verification
Kill status and exposure match the report; journal verify ok.
