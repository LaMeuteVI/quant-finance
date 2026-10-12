# Chapter 17: Performance Analysis

> **Source**: Grinold & Kahn, *Active Portfolio Management*, 2nd ed. (McGraw-Hill, 1999) | Chapter 17, pp. 477–515 (Part Four: Implementation)

## Core Idea

Performance analysis is the discipline of attributing the realised return to its sources. Grinold & Kahn's framework decomposes the realised return into **asset allocation**, **security selection**, and **interaction** effects, with the **residual-based** version (using benchmark-relative returns) as the institutional standard. The chapter also covers the **information ratio** as the summary statistic, the **t-statistic of the IR** as the statistical significance test, and the **failure modes** of performance analysis (window bias, luck vs skill, regression to the mean).

For a quant agent, this chapter is the foundation of *post-mortem analysis*: any strategy that has been live must be analysed using the framework, and the analysis must inform the next strategy.

## Frameworks Introduced

- **The Brinson–Beebower–Fachler (BBF) Decomposition**:
  - The realised active return is decomposed into:
    1. **Asset allocation effect**: the contribution of over/underweighting sectors.
    2. **Security selection effect**: the contribution of selecting the right names within each sector.
    3. **Interaction effect**: the contribution of selecting the right names in the right sectors.
  - The decomposition is: `R_active = R_AA + R_SS + R_int`.
  - *When to use*: every performance report. The BBF decomposition is the institutional standard.
  - *Why it works*: it attributes the realised return to the *decisions* the manager made.
  - *Failure mode*: the decomposition is not unique (other decompositions exist; e.g. Brinson–Hood–Beebower 1986 vs Brinson–Beebower 1991 differ in the asset allocation term).

- **The Information Ratio (recap)**:
  - `IR = E[α] / σ(α)`. The summary statistic of active management.
  - The *t-statistic* of the IR is `t = IR × √T`, where `T` is the number of periods.

- **The "Regression-to-the-mean" warning**:
  - A manager with a 1-year IR of 1.0 is expected to have an IR of ~0.5 in the next year (regression to the mean).
  - The expected next-year IR is `IR_next ≈ IR_this_year × √(1 − R²)`, where `R²` is the R² of the regression of the manager's active return on the manager's forecast.
  - *Why it matters*: the agent should not extrapolate a single-year IR.

- **The "luck vs skill" decomposition**:
  - The realised active return can be decomposed into a *skill* component (the expected alpha) and a *luck* component (the residual).
  - The skill/luck ratio is approximately `IR² / (1 + IR²)`. For IR = 0.5, skill is 20%; for IR = 1, skill is 50%; for IR = 2, skill is 80%.

## Key Concepts

1. **Active return** — realised return − benchmark return.
2. **Asset allocation effect** — the contribution of sector over/underweighting.
3. **Security selection effect** — the contribution of name selection.
4. **Interaction effect** — the joint contribution of sector and name decisions.
5. **Information ratio (IR)** — the summary statistic; `E[α] / σ(α)`.
6. **t-statistic of the IR** — `IR × √T`; the statistical significance test.
7. **Regression to the mean** — the warning that a high-IR year is followed by a lower-IR year.
8. **Luck vs skill** — the decomposition of realised return into expected alpha and residual.
9. **Performance attribution** — the discipline of attributing returns to decisions.
10. **The "golf score" framework** — the BBF decomposition as a scorecard for the manager's decisions.

## Formulas & Reference Tables

**The Brinson–Beebower–Fachler (BBF) Decomposition**

Let `w_P,s` = portfolio weight in sector `s`, `w_B,s` = benchmark weight in sector `s`, `r_P,s` = portfolio return in sector `s`, `r_B,s` = benchmark return in sector `s`. Then:

`R_AA = Σ_s (w_P,s − w_B,s) × (r_B,s − r_B)`
`R_SS = Σ_s w_B,s × (r_P,s − r_B,s)`
`R_int = Σ_s (w_P,s − w_B,s) × (r_P,s − r_B,s)`

`R_active = R_AA + R_SS + R_int` (the Brinson–Beebower 1991 decomposition).

(The earlier Brinson–Hood–Beebower 1986 decomposition uses `r_P,s` instead of `r_B,s` in `R_AA`; the two differ in the asset allocation term.)

**The t-statistic of the IR**

`t = IR × √T`

For IR = 0.5 and T = 100 (months, ~8 years), t = 5.0 — significant at 99.9%. For IR = 0.3 and T = 100, t = 3.0 — significant at 99.5%. The 3.0 threshold is the Harvey–Liu haircut for individual strategies.

**Skill / luck ratio**

`skill_fraction = IR² / (1 + IR²)`; `luck_fraction = 1 / (1 + IR²)`.

For IR = 0.5: skill = 20%, luck = 80%.
For IR = 1.0: skill = 50%, luck = 50%.
For IR = 2.0: skill = 80%, luck = 20%.

**Regression to the mean (the next-year IR estimate)**

`IR_next ≈ IR_this_year × ρ̂`, where `ρ̂` is the empirical autocorrelation of the manager's IR time series. For a manager with persistent skill, `ρ̂` is positive (typically 0.3–0.5); for a manager with no skill, `ρ̂` is ~0.

## Mental Models

- **The BBF decomposition is the scorecard.** Every decision the manager made is reflected in the decomposition.
- **A single-year IR is a sample.** The t-statistic of the IR is the statistical significance test; the next-year IR is the regression-to-the-mean estimate.
- **Skill and luck are not observable.** The skill/luck ratio is a *theoretical* decomposition that depends on the IR estimate; the agent should report the uncertainty.
- **The "luck" in a high-IR year is real money.** A 50% skill / 50% luck year means the manager earned half their IR from the strategy and half from random variation; the *next* year may not be so lucky.

## Worked Example (RECOMPUTED)

*Setup.* A manager's active return in 2025 was +3% with a 6% tracking error. Annualised IR = 0.5. 10-year history. The 10-year autocorrelation of the manager's annual IR is 0.4.

*Step 1 — IR*:
- `IR = α / σ(α) = 3% / 6% = 0.5`.

*Step 2 — t-statistic*:
- `t = IR × √T = 0.5 × √10 = 0.5 × 3.16 = 1.58`. **Not significant at 95% (need t > 1.96).** The single-year IR is a sample of size 1, so the t-stat is not meaningful. With 10 years, t = 1.58 is still marginal.

*Step 3 — BBF decomposition (illustrative)*:
- Total active return = 3%.
- Asset allocation: 1.2% (overweight tech).
- Security selection: 1.5% (good stock picks).
- Interaction: 0.3%.
- Sum: 3.0% ✓.

*Step 4 — Skill / luck ratio*:
- `skill_fraction = 0.5² / (1 + 0.5²) = 0.25 / 1.25 = 20%`. So 20% of the IR is skill, 80% is luck.
- The *expected* future IR is 0.5 × 20% + 0 × 80% = 0.10 (assuming zero skill persistence) — or 0.5 × 40% (autocorrelation) = 0.20 if persistence is 0.4.

*Step 5 — Expected 2026 IR*:
- With `ρ̂ = 0.4`: `IR_2026 ≈ IR_2025 × 0.4 = 0.5 × 0.4 = 0.20`.

*Sanity check (Python).*
```python
import math
IR, T, rho = 0.5, 10, 0.4
t_stat = IR * math.sqrt(T)
skill = IR**2 / (1 + IR**2)
print(f"t-stat of IR: {t_stat:.3f}")           # 1.58
print(f"skill fraction: {skill:.2%}")        # 20%
print(f"IR next year estimate: {IR*rho:.2f}")  # 0.20
```

## Anti-patterns

- **Reporting a single-year IR without context.** Always report the t-statistic, the autocorrelation, and the skill/luck decomposition.
- **Extrapolating a high-IR year linearly.** The regression-to-the-mean correction must be applied.
- **Using the BBF decomposition without checking the variant.** The Brinson–Hood–Beebower 1986 and Brinson–Beebower 1991 decompositions differ; pick one and stick to it.
- **Trusting the t-statistic of the IR without a DSR correction.** A t-stat of 3.0 with N_t = 50 trials is expected under the null.

## Practitioner Notes

- **2026 update.** The BBF decomposition is now standard; the Carino smoothing (Carino 1995, "Smoothing the Numbers: A Pragmatic Approach to Allocation Attribution") is the institutional default for performance reporting. The Carino smoothing scales the raw decomposition to match the total active return.
- **The GIPS standards** (covered in `cfa-ethics-gips` and the 2024 CFA L3 Vol3 Performance Measurement) are the binding standards for performance reporting.
- **Factor-based performance attribution** (the Barra-style decomposition) is the modern alternative to BBF; the active return is decomposed into exposures to risk factors and to selection.
- **Live paper trading results are not in the BBF decomposition.** The agent must explicitly separate live paper from production.

## Key Takeaways

1. **The BBF decomposition** is the institutional performance attribution standard; it splits active return into asset allocation, security selection, and interaction.
2. **The IR is the summary statistic**; the t-statistic is the statistical significance test.
3. **Regression to the mean** is real: a 1-year IR of 0.5 is expected to be 0.2–0.3 in the next year.
4. **The skill/luck ratio** is `IR² / (1 + IR²)`; for IR = 0.5, only 20% of the IR is skill.
5. **Performance analysis must inform the next strategy.** A high-IR year that is 80% luck should not be the basis of a doubling of AUM.

## Connects To

- **ch14** (Portfolio Construction): the construction is the input to the performance analysis.
- **ch15** (Long/Short Investing): the BBF decomposition must be extended for the short side.
- **ch20** (The Historical Record for Active Management): the empirical evidence on persistence of alpha is the macro context for the chapter.
- **`cfa-performance-measurement` (new skill, in build)**: the GIPS-aligned performance measurement.
- **`cfa-ethics-gips` skill**: the GIPS standards.
- **`lopez-de-prado-afml` ch15 (Strategy Risk)**: the deeper analysis of strategy risk.
