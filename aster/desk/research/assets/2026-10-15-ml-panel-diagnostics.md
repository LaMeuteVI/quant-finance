# ML panel diagnostics on klines 1m daily — falsification-first

**Status: descriptive only; no ledger hypothesis, no backtest, no holdout read.**

- Cutoff: `2024-07-01T00:00:00+00:00`; dev end: `2022-10-11T00:00:00+00:00`.
- Symbols: `['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'SOL/USDT']`.
- Panel size: n_panel=`3543`, n_is=`2835`, n_oos=`708`.
- Features (8): `log_return_1d, hl_range_norm_atr, co_asymmetry_norm_atr, realized_var_1d, sign_persist_1d, rv_ratio_5d_1d, vol_of_vol_5d, zscore_20d`.
- Label: 5-day ATR(14) triple-barrier, drop vertical touches, binary +1 / -1.
- Purged k-fold (k=5) with embargo `6` days; tail 20% held out as a fixed OOS slice.
- Model: sparse logistic regression (L2) with λ ∈ [0.01, 0.1, 1.0, 10.0, 100.0]; L-BFGS-B, max 200 iters.
- DSR (Bailey & López de Prado 2014, normal approximation); trials = len(λ) + 1.

## Results

- Best λ (purged CV): **0.1** with CV hit-rate **0.5732**.
- OOS hit-rate (logreg, fixed tail): **0.4350**.
- Majority class baseline (OOS): **0.5791**.
- Sign-of-prior-return baseline (OOS, n=`3541`): **0.5323**.
- Random classifier (OOS): **0.5042**.
- OOS lift over majority: **-0.1441**.
- OOS lift over sign baseline: **-0.0973**.
- DSR p-value (vs SR=0, n trials=`6`): **0.8837**.

## Triage rule (pre-registered in this note, before any number above was read)

1. OOS hit-rate > max(majority class, sign baseline) by at least 3 absolute percentage points, AND
2. DSR p-value < 0.05 against SR=0 (n trials = len(λ) + 1), AND
3. CV best hit-rate > sign baseline CV hit-rate by at least 1 absolute percentage point.

- Rule 1: logreg `0.4350` vs max(maj, sign) `0.5791` → **diff -0.1441** (need ≥ +0.03).
- Rule 2: DSR p-value `0.8837` (need < 0.05).
- Rule 3: see CV table in `2026-10-15-ml-panel-diagnostics-folds.csv`.

## Verdict

If any rule fails → **0 edge tradable** and the klines-1m ML axis is closed; the only credible next axis is tick microstructure data (BACKLOG item 15), which requires Samuel's budget OK and a fresh cutoff seal.

If all rules pass → a primary feature is identified; escalate to ledger preregistration and a counted `desk backtest` (NOT in this note).
