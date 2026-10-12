# Chapter 5: Worked Examples of Verification

> Quant Verification, Chapter 5.

## Core Idea

Three concrete examples of the verification protocol in action.

## Example 1: GARCH(1,1) Persistence

*Source*: `hull-risk-management` ch10, `tsay-analysis-financial-time-series` ch03.

*Formula*: persistence = `α + β`. For a typical GARCH(1,1) with `α = 0.05, β = 0.93`, persistence = 0.98.

*Script*:
```python
alpha, beta = 0.05, 0.93
persistence = alpha + beta
half_life = np.log(0.5) / np.log(persistence)
print(f"persistence = {persistence:.4f}, half_life = {half_life:.1f} days")
# -> 0.98, 34.4 days
```

*Cross-check*: with `λ = 0.94` for EWMA, half-life = `log(0.5) / log(0.94) = 11.2` days. The two are different by design.

## Example 2: SVI Total Variance

*Source*: `gatheral-volatility-surface` ch03.

*Formula*: `w(k) = a + b × (ρ(k - m) + sqrt((k - m)² + σ²))`.

*Script*:
```python
a, b, rho, m, sigma = 0.04, 0.5, -0.7, 0.0, 0.4
k = -0.1054  # log(90/100)
w = a + b * (rho * (k - m) + np.sqrt((k - m)**2 + sigma**2))
print(f"w(k={k:.4f}) = {w:.4f}")  # -> 0.2835
```

*Cross-check*: at `k = 0` (ATM), `w(0) = 0.04 + 0.5 × sqrt(0.16) = 0.04 + 0.2 = 0.24` (the ATM total variance). For `T = 0.5`, `σ_BS = sqrt(0.24/0.5) = 0.69` (69%).

## Example 3: DSR for a Backtest

*Source*: `lopez-de-prado-afml` ch14.

*Formula*: `E[max SR | N_t] ≈ sqrt(2 × log N_t) - γ / sqrt(2 × log N_t)`.

*Script*:
```python
N_t = 200
E_max = np.sqrt(2 * np.log(N_t)) - 0.5772 / np.sqrt(2 * np.log(N_t))
print(f"E[max SR | N_t=200] = {E_max:.3f}")  # -> 3.08
```

*Cross-check*: a backtest SR of 2.6 is *below* the null expectation of 3.08; the strategy is *not* impressive.

## Key Takeaways

1. The three examples show the protocol in action.
2. The cross-check (a different method or a different parameter) is essential.
3. The audit trail records the script, the version, and the result.

## Connects To

ch01 (Toolkit), ch02 (Cross-Check Protocol), ch04 (Audit Trail).
