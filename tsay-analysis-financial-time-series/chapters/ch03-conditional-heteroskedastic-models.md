# Chapter 3: Conditional Heteroskedastic Models

> Tsay, Chapter 3. ARCH, GARCH, GJR, EGARCH, TGARCH, APARCH.

## Core Idea

**Conditional heteroskedasticity** is the property that the variance of `ε_t` depends on past information. The **ARCH(q) model** (Engle 1982): `ε_t = σ_t z_t`, `σ_t² = α_0 + α_1 ε_{t-1}² + ... + α_q ε_{t-q}²`, with `z_t` iid. The **GARCH(p, q) model** (Bollerslev 1986): `σ_t² = α_0 + α_1 ε_{t-1}² + ... + α_q ε_{t-q}² + β_1 σ_{t-1}² + ... + β_p σ_{t-p}²`. The **GJR-GARCH(1,1,1)** captures the **leverage effect** (asymmetric response to negative returns). The **EGARCH(1,1)** uses log-volatility; the **TGARCH(1,1)** uses a threshold; the **APARCH** is the most general.

## Key Concepts

- **ARCH(q)** — autoregressive conditional heteroskedasticity (Engle 1982).
- **GARCH(p, q)** — generalisation with ARMA structure (Bollerslev 1986).
- **GARCH(1,1) persistence** — `α + β`; the half-life of a shock is `log(0.5) / log(α + β)`.
- **GJR-GARCH** — asymmetric; captures leverage (Glosten-Jagannathan-Runkle 1993).
- **EGARCH** — log-volatility (Nelson 1991).
- **TGARCH (threshold GARCH)** — Zakoian 1994.
- **APARCH** — asymmetric power ARCH (Ding, Granger, Engle 1993).
- **Mean model + vol model** — the two-stage estimation.
- **The Ljung-Box test on squared residuals** — diagnostic for remaining ARCH.
- **News impact curve** — the relation between `ε_{t-1}` and `σ_t²`.

## Formulas & Tables

- **ARCH(q)**: `σ_t² = α_0 + Σ α_i ε_{t-i}²`. All `α_i ≥ 0`, `Σ α_i < 1`.
- **GARCH(1,1)**: `σ_t² = α_0 + α_1 ε_{t-1}² + β_1 σ_{t-1}²`. Persistence `α_1 + β_1`. Half-life = `log(0.5) / log(α_1 + β_1)`.
- **GJR-GARCH(1,1)**: `σ_t² = α_0 + α_1 ε_{t-1}² + γ I(ε_{t-1} < 0) ε_{t-1}² + β_1 σ_{t-1}²`. The leverage effect is `γ`.
- **EGARCH(1,1)**: `log(σ_t²) = α_0 + α_1 |z_{t-1}| + γ z_{t-1} + β_1 log(σ_{t-1}²)`, with `z_t = ε_t / σ_t`.

## Key Takeaways

1. GARCH(1,1) is the workhorse; typical persistence is 0.95-0.99.
2. GJR-GARCH captures the leverage effect; the asymmetry is the `γ` term.
3. EGARCH is the log-form alternative; TGARCH is the threshold form.

## Connects To

- ch01 (Stylised facts), ch02 (Linear), ch04 (Nonlinear), `hull-risk-management` ch10 (Volatility).
