# Cheatsheet — Advances in Financial Machine Learning (López de Prado)

## When to do X, do Y, because Z

- **When you label financial data**, use the **triple-barrier method** with **dynamic barriers**. **Because** raw future returns are too noisy.
- **When you sample financial data**, use **information-driven bars (TIB/VIB/TRB)**. **Because** time bars are not stationary.
- **When you do CV on time series**, use **purged k-fold with embargo**. **Because** standard k-fold leaks information.
- **When you report a backtest SR**, compute the **Deflated Sharpe Ratio**. **Because** a SR of 2.5 is expected under the null with 100 trials.
- **When you compare many strategies**, compute the **Probability of Backtest Overfitting**. **Because** the best IS strategy may be the worst OOS.
- **When you size a bet**, use **inverse-vol scaling + meta-label**. **Because** equal-weight is not the optimum; the meta-label scales by confidence.
- **When you select features**, use **MDA** (MDI for pre-filter, SFI for the top 10–20). **Because** MDI is biased, MDA is robust, SFI is the gold standard.
- **When you allocate assets**, use **HRP** as the default. **Because** mean-variance is dominated by estimation error.
- **When you detect a regime change**, use the **CUSUM, SupF, or Bai–Perron** test. **Because** every backtest should test for breaks.
- **When you go live**, run the **live paper test** for 3–6 months, then **scale in** 5% per month. **Because** the only protection against a slow leak is gradual allocation.

## Decision tree — what kind of ML problem is this?

```
Is the prediction a price level, a return, or a label?
  ├─ Price level → Use the FFD (d* from ADF test)
  ├─ Return → Use triple-barrier labels
  └─ Label → Use triple-barrier labels with dynamic barriers

Is the model linear or non-linear?
  ├─ Linear → Use the rule of thumb (s × IC × σ(θ)) + FFD features
  └─ Non-linear → Use a tree-based model (Random Forest / XGBoost)

Is the strategy single-asset or portfolio?
  ├─ Single-asset → Use inverse-vol sizing + meta-label
  └─ Portfolio → Use HRP as the default; mean-variance only with shrinkage
```

## Thresholds & defaults

| Quantity | Default | Range | Source |
|---|---|---|---|
| Triple-barrier window | 5 days | 1 to 20 days | ch03 |
| Triple-barrier multiplier (m) | 1.0 | 0.5 to 2.0 | ch03 |
| FFD threshold `d*` | 0.3 | 0.2 to 0.5 | ch05 |
| FFD window `k*` | 100 | 50 to 1000 | ch05 |
| CPCV N | 6 | 4 to 10 | ch07 |
| CPCV k | N/2 | N/4 to 3N/4 | ch07 |
| Embargo | 1% of sample | 0.5% to 5% | ch07 |
| DSR threshold | 0.95 | 0.90 to 0.99 | ch14 |
| PBO threshold | 0.10 | 0.05 to 0.25 | ch14 |
| t-stat threshold | 3.0 | 2.5 to 4.0 | ch14 (Harvey-Liu 2015) |
| MinTRL (SR=1, 95%) | 5 years | 1 to 20 years | ch14, ch15 |
| Live paper test | 6 months | 3 to 12 months | ch11, ch15 |
| Scale-in | 5% per month | 2% to 10% per month | ch11 |
| Kelly multiplier | 0.5 | 0.25 to 1.0 | ch10 |

## Tells & smells

- **The in-sample SR is high but the OOS SR is low** → look-ahead bias; the strategy used future data.
- **The OOS SR is positive but the live paper SR is negative** → operational issue; the strategy is right but the execution is wrong.
- **The strategy is profitable in the backtest at $1M but unprofitable at $1B** → capacity constraint; the cost is the binding factor.
- **The strategy's alpha disappears in stress periods** → the strategy is a "calm beta"; not a true alpha.
- **The DSR is negative** → the SR is not impressive given the number of trials; the strategy is a fluke.
- **The PBO is > 50%** → the strategy is more likely to be the worst OOS than the best; abandon it.
- **The MinTRL exceeds the OOS history** → the strategy is not yet significant; collect more data.

## Citation table (2026 institutional standards)

| Item | Threshold | Source |
|---|---|---|
| Multiple testing t-stat | ≥ 3.0 | Harvey, Liu & Zhu (RFS 2015) |
| DSR threshold | ≥ 0.95 | Bailey & López de Prado (JPM 2014) |
| PBO threshold | ≤ 0.10 | Bailey, Borwein, López de Prado & Zhu (JCFE 2016) |
| MinTRL (SR=1, 95%) | ~5 years monthly | López de Prado ch14 |
| Post-publication decay | ~26% OOS, ~58% after costs | McLean & Pontiff (2016) |
| Fractional Kelly | 0.5× | López de Prado ch10 |
| Triple-barrier multiplier | 1.0× realised vol | López de Prado ch03 |
| FFD threshold | 0.3 | López de Prado ch05 |
| Lee-Ready (1991) | buy/sell classifier | Lee & Ready (JFE 1991) |
| BVC (2012) | HFT buy/sell | Easley, López de Prado, O'Hara |
