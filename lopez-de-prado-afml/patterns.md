# Patterns — Advances in Financial Machine Learning (López de Prado)

## 1. The Triple-Barrier Label (ch03)
- **When**: every time you label financial data for supervised learning.
- **How**: define a `t_0, t_1` interval and two horizontal barriers; label `+1` if upper hit first, `−1` if lower, else `0` or realised return.
- **Trade-off**: dynamic barriers (based on realised vol) are essential; static barriers are wrong in volatile regimes.

## 2. The Information-Driven Bar (ch02)
- **When**: every time you sample financial data.
- **How**: use TIB, VIB, or TRB; calibrate the threshold to the expected absolute imbalance.
- **Trade-off**: more work than time bars, but the resulting features are stationary.

## 3. The Sample-Uniqueness Weight (ch03, ch04)
- **When**: every time you fit a model on financial data.
- **How**: compute the concurrent label count `c_t`; the uniqueness is `u_i = (Σ_t c_t × 1_{t,i}) / (c_i × Σ_t c_t)`.
- **Trade-off**: the effective sample size is typically 1/3 to 1/5 of the nominal.

## 4. Purged K-Fold with Embargo (ch07)
- **When**: every time you do CV on financial time series.
- **How**: purge observations whose `t_0, t_1` overlap with the train set; add an embargo of 1% of the sample size.
- **Trade-off**: standard k-fold is wrong; always use purged k-fold.

## 5. Combinatorial Purged CV (CPCV) (ch07, ch12)
- **When**: when you need many backtest paths (for the DSR, PBO).
- **How**: N=6, k=3 gives 20 paths; N=10, k=5 gives 252 paths.
- **Trade-off**: more paths = better estimate of the OOS distribution.

## 6. The Deflated Sharpe Ratio (ch14)
- **When**: every time you report a backtest SR.
- **How**: `DSR` corrects for the number of trials, skew, and kurtosis.
- **Trade-off**: a SR of 2.5 is *expected* under the null with 100 trials.

## 7. The Probability of Backtest Overfitting (ch14)
- **When**: when comparing many strategies.
- **How**: CSCV across N sub-sample splits; PBO is the fraction of splits where the best IS strategy is the worst OOS.
- **Trade-off**: requires N ≥ 16 strategies to be meaningful.

## 8. The Minimum Track Record Length (ch14, ch15)
- **When**: before allocating capital.
- **How**: `MinTRL = 1 + (1 + (γ₄−1)/4 × SR²) × (z_α / SR)²`.
- **Trade-off**: for SR=1 and 95% confidence, MinTRL ≈ 5 years of monthly data.

## 9. The Fractional Differentiation (ch05)
- **When**: when you want stationary, memory-preserving features.
- **How**: `(1−x)^d` with `d ∈ [0, 1]`; the FFD threshold `d*` is the smallest `d` for which the ADF test rejects.
- **Trade-off**: small `d` requires a long window (k* = 100+); large `d` destroys memory.

## 10. The Meta-Labeling Pipeline (ch03, ch10)
- **When**: when the primary model predicts a binary bet.
- **How**: primary model → direction; secondary model → probability of being correct; bet size = `meta_prob × 1/σ̂_t`.
- **Trade-off**: the meta-labeler is for *sizing*, not for *predicting*.

## 11. The Three Sizing Strategies (ch10)
- **When**: every time you size a bet.
- **How**: Strategy 1 (constant), Strategy 2 (inverse-vol), Strategy 3 (mixed).
- **Trade-off**: inverse-vol is the minimum; mean-variance is the optimum.

## 12. The Fractional Kelly (ch10)
- **When**: when sizing a binary bet.
- **How**: `f* = (p × b − q) / b`; the fractional Kelly is `0.5 × f*`.
- **Trade-off**: the full Kelly assumes no estimation error; the fractional is the institutional default.

## 13. The Hierarchical Risk Parity (ch16)
- **When**: as the default asset allocation.
- **How**: cluster the correlation matrix; recursively bisect; allocate inverse-variance.
- **Trade-off**: more robust than mean-variance to estimation error.

## 14. The Three Feature Importances (ch08)
- **When**: every time you select features.
- **How**: MDI (fast, biased), MDA (robust, substitution-affected), SFI (gold standard, expensive).
- **Trade-off**: use MDI as a pre-filter; MDA for the final set; SFI for the top 10–20.

## 15. The Balanced Bootstrap (ch06)
- **When**: with imbalanced classes (the default in finance).
- **How**: draw with probability proportional to 1/class_frequency.
- **Trade-off**: the standard bootstrap over-samples the majority class.

## 16. The Bagging Classifier (ch06)
- **When**: with imbalanced classes.
- **How**: `BalancedBaggingClassifier` from `imblearn`.
- **Trade-off**: the default `RandomForestClassifier` is biased toward the majority class.

## 17. The Live Paper Test (ch11, ch15)
- **When**: before allocating capital.
- **How**: run the strategy in live paper trading for 3–6 months; compare to the OOS.
- **Trade-off**: the only test that captures operational risk.

## 18. The Scale-In Rule (ch11)
- **When**: when allocating capital to a new strategy.
- **How**: 5% of AUM per month; full target in 6 months.
- **Trade-off**: the only protection against a slow leak.

## 19. The Kill Switch (ch11, ch15)
- **When**: every strategy.
- **How**: a clear performance threshold below which the strategy is paused.
- **Trade-off**: the only protection against a tail event.
