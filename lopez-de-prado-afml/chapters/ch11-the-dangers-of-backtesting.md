# Chapter 11: The Dangers of Backtesting

> **Source**: Marcos López de Prado, *Advances in Financial Machine Learning*, Wiley 2018 | Chapter 11, pp. 151–160

## Core Idea

A backtest is a *single sample* from a stochastic process. Most published backtests overfit their data — not because the researcher is dishonest, but because the backtest optimisation is itself a multiple-testing problem that the researcher is usually not aware of. The chapter enumerates the **seven pathologies** that make backtests unreliable, the **standard tests** that catch them, and the **discipline** that limits their damage.

This chapter is the warning label on every backtest the agent produces.

## The Seven Pathologies of Backtesting

1. **Multiple testing / selection bias**: of N_t backtested strategies, the one with the best in-sample Sharpe is reported; the expected max Sharpe under the null is `√(2 log N_t)`. A backtest SR of 2.5 from 100 trials is *expected* under the null.
   - *Test*: the **Deflated Sharpe Ratio (DSR)** (ch14). The DSR corrects the SR for the number of trials.

2. **Backtest overfitting**: even with a single strategy, the in-sample optimisation overfits the data; the out-of-sample performance is *lower* than the in-sample. The probability of overfitting can be computed.
   - *Test*: the **Probability of Backtest Overfitting (PBO)** (ch14), via Combinatorially Symmetric Cross-Validation (CSCV, related to CPCV in ch07).

3. **Data leakage (look-ahead bias)**: the strategy uses information that was not available at the time of the trade. Common sources: the labels were constructed using future data; the features were standardised using the full sample; the backtest split the data without purging.
   - *Test*: **purged k-fold CV with embargo** (ch07). A "leakage test" that re-runs the backtest with the labels shifted by one day is a quick sanity check.

4. **Non-stationarity**: the strategy is fit on data that has a different distribution from the data on which it will be deployed. Common sources: regime change (2008 crisis, COVID 2020), structural break (a corporate action, a market-microstructure change).
   - *Test*: the **CUSUM test** for structural breaks (ch17). The agent should test for breaks in the strategy's P&L, not just in the underlying market.

5. **Survivorship bias**: the strategy is fit on data that includes only assets that survived to the end of the period. The delisted assets (bankruptcies, M&A) are missing from the backtest.
   - *Test*: include the delisted assets in the backtest. The CRSP/Compustat universe is the standard US database; for other markets, use the equivalent (e.g. Bloomberg historical constituent lists).

6. **Strategy crowding**: the strategy's alpha is not really alpha; it is the *aggregate* alpha of many other funds running similar strategies. The alpha is "in the price" of the strategy's trades; the strategy captures only the front-runner's edge.
   - *Test*: compare the strategy's returns to a peer-group index (e.g. the eVestment hedge-fund database, the HFR index family). If the strategy's alpha is dominated by the peer index, the strategy is crowded.

7. **False discovery**: a strategy passes the backtest because the *researcher* chose it, not because it is real. The Bayesian false discovery probability is non-trivial when the prior probability of a true strategy is low.
   - *Test*: the **Bayesian false discovery rate** (FDR) of the strategy's OOS performance; the Harvey–Liu haircut (t > 3.0 for individual signals).

## Frameworks Introduced

- **The "out-of-sample" trap**: a strategy that passes the OOS test may still fail in live trading, because the OOS test is a *single sample* from a stochastic process. The OOS test is necessary but not sufficient.
- **The "live paper" test**: a strategy must pass the *live paper trading* test (6–12 months of real-time paper trading) before any allocation of capital. The live paper test is the only test that captures the operational risks of the strategy.
- **The "scale-in" rule**: never allocate full capital at once; scale in over 3–6 months. The scale-in rule gives the strategy a chance to fail *before* losing material capital.
- **The "kill switch"**: every strategy must have a clear kill switch (a performance threshold below which the strategy is paused). The kill switch is the only protection against a slow leak.

## Key Concepts

1. **Look-ahead bias** — the use of information not available at the time of the trade.
2. **Survivorship bias** — the omission of delisted assets from the backtest.
3. **Multiple testing / selection bias** — the bias from choosing the best of N_t strategies.
4. **Backtest overfitting** — the optimisation of the strategy to the in-sample data.
5. **Non-stationarity** — the change in the data distribution over time.
6. **Strategy crowding** — the reduction in alpha as more funds run the same strategy.
7. **False discovery** — the bias from the researcher's choice of strategy.
8. **Out-of-sample (OOS) test** — the backtest on data not used in the optimisation.
9. **Live paper trading** — the real-time paper trading of the strategy.
10. **Scale-in** — the gradual allocation of capital to the strategy.
11. **Kill switch** — the performance threshold below which the strategy is paused.

## Formulas & Reference Tables

**Expected max SR under the null (multiple testing)**

`E[max SR | N_t] ≈ √(2 log N_t) − (γ / √(2 log N_t)) + (log log N_t + log(4π) − 2γ) / (2 (2 log N_t)^(3/2))`

For N_t = 100, this gives E[max SR] ≈ 2.51.

**The Harvey–Liu haircut (RFS 2016)**

The standard t-statistic threshold for financial anomalies should be 3.0 (not 2.0). A strategy with a t-stat of 2.5 is *not* statistically significant when corrected for multiple testing.

**The Bayesian False Discovery Probability**

`FDR = P(H0 | observed result) = P(observed | H0) × P(H0) / P(observed)`

If the prior probability of a true strategy is low (e.g. 1 in 1000), even a "significant" t-stat may have a high FDR.

**The Bayesian Sharpe Ratio (BSR)**

`BSR = P(SR > 0 | data) = Φ((SR̂ × √T − SR₀) / √(1 + SR̂² × √T))`

where `SR₀` is the prior mean Sharpe (often 0 or 0.5).

## Mental Models

- **A backtest is a single sample; treat it as such.** The DSR is the multiple-testing correction; the PBO is the overfitting test; the OOS test is the only honest test.
- **The seven pathologies are not independent.** A backtest can suffer from all of them simultaneously; the agent should test for all.
- **The live paper test is the only test that captures operational risk.** No amount of statistical testing captures the *operational* failure of a strategy (e.g. the strategy's orders are not getting filled, the data feed is delayed, the corporate action calendar is wrong).
- **The scale-in rule is the only protection against a slow leak.** No strategy is "obviously" wrong on day 1; the leak is gradual.

## Worked Example (RECOMPUTED — illustrative)

*Setup.* A researcher runs 200 backtests, picks the one with the best Sharpe, and reports it as the "new strategy". The reported Sharpe is 2.6 over 3 years of monthly data.

*Step 1 — Multiple testing*.
- `E[max SR | N_t = 200] ≈ √(2 × log 200) − 0.5772 / √(2 × log 200) = √(10.6) − 0.177 = 3.26 − 0.18 = 3.08`.
- So the expected max SR under the null is **3.08**. The researcher's 2.6 is *below* the null — there is no evidence of skill.

*Step 2 — DSR (Bailey & López de Prado 2014)*.
- `DSR` adjusts the SR for N_t = 200; the DSR for SR = 2.6 is *negative*. The strategy fails the DSR.

*Step 3 — Look-ahead bias check*.
- Re-run the backtest with the labels shifted by one day. If the new Sharpe is similar, the original had no look-ahead. If the new Sharpe is much higher, the original had look-ahead.

*Step 4 — OOS test (single split)*.
- Split the data: 2 years IS, 1 year OOS. Run the strategy on the IS data, then evaluate on the OOS data. The OOS Sharpe is typically 30–50% of the IS Sharpe. If the OOS Sharpe is < 1.0, the strategy is not worth trading.

*Step 5 — The "live paper" step*.
- After the OOS test, run the strategy in live paper trading for 3–6 months. If the live paper performance is consistent with the OOS, allocate capital gradually (5% of AUM per month) up to the target allocation.

*Sanity check (Python).*
```python
import math
N_t = 200
log_N = math.log(N_t)
E_max = math.sqrt(2*log_N) - 0.5772/math.sqrt(2*log_N)
print(f"E[max SR | N_t=200] = {E_max:.3f}")  # ~3.08
print(f"Researcher's SR (2.6) is BELOW the null expectation -> no evidence of skill")
```

## Anti-patterns

- **Running many backtests and reporting only the best.** Always compute the DSR; if DSR < 0.95, the strategy is not significant.
- **Skipping the OOS test.** A "trust the backtest" attitude is the fastest way to lose money.
- **Skipping the live paper test.** Operational failures are the most common cause of strategy death.
- **Allocating full capital immediately.** The scale-in rule is the only protection against a slow leak.
- **Forgetting the kill switch.** Every strategy must have a clear kill threshold.

## Practitioner Notes

- **2026 update.** The seven pathologies are now standard in institutional research; the **DSR/PBO/SPA** trio is the institutional standard. The companion papers (Bailey–López de Prado 2014 DSR; Bailey–Borwein–López de Prado–Zhu 2014 Pseudo-Math; 2016 PBO; Harvey–Liu 2015 multiple testing) are the canonical references.
- **Live paper trading** is more common in modern practice; the *paper trading* environment is now a standard offering of every prime brokerage (Interactive Brokers, Bloomberg EMSX, etc.).
- **The scale-in rule** is institutional default; the regulatory push (Basel III model risk management) is for the *gradual* deployment of any new model.
- **Strategy crowding** is a real phenomenon; the eVestment database and the HFR indices are the standard references for peer-group comparisons.

## Key Takeaways

1. **The seven pathologies are not optional.** Every backtest must be tested for all of them.
2. **The DSR is the multiple-testing correction.** A SR of 2.5 from 100 trials is expected under the null.
3. **The PBO is the overfitting test.** It is computed via CSCV.
4. **The OOS test is necessary but not sufficient.** The live paper test is the only test that captures operational risk.
5. **Scale-in is the only protection against a slow leak.** No strategy is "obviously" wrong on day 1.

## Connects To

- **ch07** (Cross-Validation in Finance): purged k-fold and CPCV are the backtest-of-the-backtest tools.
- **ch14** (Backtest Statistics): the DSR and PBO are the institutional statistics.
- **ch15** (Understanding Strategy Risk): the deeper look at strategy risk.
- **`hull-risk-management` ch12 (VaR and ES), ch25 (Model Risk)**: the institutional risk-management framing.
- **`hull-risk-management` ch14 (Model-Building Approach)**: the backtest of a VaR model.
- **`diebold-mariano-forecast-accuracy` skill**: the forecast-comparison test that complements the strategy-comparison test.
