# Chapter 1: Portfolio Performance Evaluation

> CFA L3 2024, V3 LM1. The institutional performance evaluation framework.

## Core Idea

**Performance evaluation** is the discipline of attributing the realised return to its sources. The **time-weighted return (TWR)** is the standard for manager performance; the **money-weighted return (MWR, IRR)** is the standard for fund performance. The **Brinson-Fachler (1991) decomposition** is the institutional attribution standard; the **Carino smoothing** is the institutional adjustment. The **factor attribution** (Fama-French 5-factor, Carhart 4-factor) is the modern alternative.

## Key Concepts

- **Time-Weighted Return (TWR)** — the geometric mean of the sub-period returns; eliminates the effect of cash flows.
- **Money-Weighted Return (MWR, IRR)** — the IRR of the cash-flow stream; incorporates the effect of cash flows.
- **Modified Dietz** — the approximate MWR; weights the return by the capital deployed.
- **Performance Attribution** — the decomposition of the active return.
- **Brinson-Fachler (1991)** — `R_active = R_AA + R_SS + R_int`.
- **Carino Smoothing** — the scaling factor that makes the BBF components sum to the total.
- **Factor Attribution** — the decomposition into exposures to risk factors.

## Formulas & Tables

- **TWR**: `TWR = Π (1 + r_i) - 1`, with `r_i` the sub-period return.
- **MWR (IRR)**: solve `Σ CF_t / (1 + IRR)^t = 0` for `IRR`.
- **Modified Dietz**: `R = (V_1 - V_0 - Σ CF_t) / (V_0 + Σ w_t × CF_t)`, with `w_t = (T - t) / T`.
- **Brinson-Fachler**: as in `grinold-kahn-apm` ch17.
- **Carino smoothing factor**: `k = R_active / Σ (w_i × R_i)`, with `w_i` the original weights and `R_i` the original components.
- **Factor attribution**: `R_i - R_f = α_i + β_M × (Mkt-RF) + β_S × SMB + β_V × HML + ... + ε_i`.

## Key Takeaways

1. TWR is for manager performance; MWR is for fund performance.
2. BBF is the institutional attribution; Carino smoothing is the institutional adjustment.
3. Factor attribution is the modern alternative.

## Connects To

- `grinold-kahn-apm` ch17, `lopez-de-prado-afml` ch14, `lopez-de-prado-ml-asset-managers` ch07.
