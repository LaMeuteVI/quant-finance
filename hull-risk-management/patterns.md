# Patterns — Risk Management and Financial Institutions (Hull)

## 1. Parametric VaR (ch12)
- **When**: linear portfolios, short horizons.
- **How**: `VaR_α = z_α × √(h' V h)`.
- **Trade-off**: closed-form; understates tail risk for non-normal returns.

## 2. Historical Simulation VaR (ch13)
- **When**: non-normal returns, enough data.
- **How**: take the empirical quantiles of past P&L.
- **Trade-off**: makes no parametric assumption; 99.9% VaR is impossible from daily data.

## 3. Monte Carlo VaR (ch14)
- **When**: option portfolios, non-linear payoffs.
- **How**: simulate under many scenarios; take the quantiles.
- **Trade-off**: the only "complete" method; model error dominates simulation error.

## 4. Expected Shortfall (ch12)
- **When**: as the modern replacement for VaR.
- **How**: `ES_α = E[Loss | Loss > VaR_α]`.
- **Trade-off**: coherent; harder to backtest than VaR.

## 5. Traffic-Light Backtest (ch12)
- **When**: for IMA-validated VaR models.
- **How**: count exceptions over 250 days; green 0–4, yellow 5–9, red 10+.
- **Trade-off**: institutional standard; the 95% CI for 99% VaR is wide.

## 6. Kupiec POF Test (ch12)
- **When**: formal test of the exception rate.
- **How**: `LR_POF = -2 ln((1-p)^(N-x) p^x) + 2 ln((1-p̂)^(N-x) p̂^x)`; reject if > 3.84.
- **Trade-off**: the formal version of the traffic-light framework.

## 7. Christoffersen Independence Test (ch12)
- **When**: to detect serial dependence in exceptions.
- **How**: HMM with two states; LR statistic.
- **Trade-off**: catches regime-clustered exceptions.

## 8. Square-Root Law of Impact (ch16, cross-ref)
- **When**: sizing an order.
- **How**: `Impact(Q) = σ × √(Q/ADV) × Y`.
- **Trade-off**: the canonical impact model; Y is asset-class-specific.

## 9. Almgren-Chriss Optimal Execution (cross-ref)
- **When**: optimal execution of a large order.
- **How**: `x*(t) = X × sinh(κ(T-t)) / sinh(κT)`.
- **Trade-off**: balances impact (slow) against delay (fast).

## 10. Merton Default Model (ch19)
- **When**: structural model of default.
- **How**: equity is a call on assets; default when assets < liabilities.
- **Trade-off**: closed-form; assumes geometric Brownian motion of assets.

## 11. CVA Decomposition (ch20)
- **When**: pricing counterparty credit risk.
- **How**: `CVA ≈ (1 - R) × Σ (DF_t × EE_t × PD_t)`.
- **Trade-off**: the market value of the counterparty's default risk.

## 12. Component VaR (ch14)
- **When**: decomposing portfolio VaR.
- **How**: `C_VaR_i = h_i × (V h)_i / √(h' V h) × z_α`.
- **Trade-off**: linear decomposition; exact for variance-covariance VaR.

## 13. Stressed VaR (ch14, ch17)
- **When**: as a regulatory requirement.
- **How**: VaR over a 12-month stressed window.
- **Trade-off**: more conservative than 1-year VaR.

## 14. The FRTB Capital Formula (ch17, cross-ref)
- **When**: for trading book capital.
- **How**: `capital = max(SA_capital, IMA_capital)` where `IMA_capital = ES × m`.
- **Trade-off**: the FRTB approach is more granular than the pre-FRTB approach.

## 15. The Independent Validation Process (ch25)
- **When**: every model.
- **How**: second-party review; tests assumptions; tests outputs.
- **Trade-off**: the institutional response to model risk.

## 16. The Pillar 1 / 2 / 3 Framework (ch15, ch16)
- **When**: for capital adequacy.
- **How**: Pillar 1 (minimum capital), Pillar 2 (supervisory review), Pillar 3 (market discipline).
- **Trade-off**: the Basel III three-pillar structure.
