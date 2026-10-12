# Chapter 25: Model Risk

> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed. (Wiley, 2012) | Chapter 25, pp. 527–545

## Core Idea

Model risk is the risk that a model is **wrong** — the wrong distribution, the wrong parameters, the wrong structure, or used outside its domain of validity. The chapter enumerates the **reasons models fail** and the **controls** that limit the damage. The 2008 crisis demonstrated that the *most sophisticated* models were the most exposed: the Gaussian copula's collapse showed that a model used by everyone is a model whose failure hurts everyone. Hull 4e devotes the chapter to a single message: **a model is a tool, not a truth; every model is wrong somewhere, and the model risk framework is the discipline of bounding that "somewhere".**

For a quant agent, this chapter is the institutional foundation for the validation discipline (LdP's *AFML* ch11, ch14, ch15 is the modern statistical continuation).

## Frameworks Introduced

- **The "Reasons Models Fail" Taxonomy (Hull 4e, the list)**:
  1. **The model is fundamentally wrong.** The wrong distribution (Gaussian for fat-tailed), the wrong relationship (linear for non-linear), the wrong state-space (Markov-1 when memory is longer).
  2. **The model parameters are wrong.** The mean, volatility, correlation, beta, etc. are mis-calibrated. A correct model with wrong parameters is still a wrong model.
  3. **The model is used outside its domain.** A short-rate model for a 30-year swap; a Black-Scholes for a barrier option; a Gaussian copula for CDO tranche pricing in stress.
  4. **Data errors.** The inputs are wrong (stale prices, missing corporate actions, look-ahead bias).
  5. **Implementation errors.** Coding bugs, unit errors, sign errors, off-by-one in time indices.
  6. **Operational errors.** The model is right but used by the wrong person, in the wrong workflow, with the wrong override.

- **The "Model Risk Management" Controls**:
  1. **Independent validation** — a second pair of eyes, ideally outside the model owner's group, must replicate the model and challenge its assumptions.
  2. **Ongoing monitoring** — the model's performance is tracked over time; the moment the residual error exceeds a threshold, the model is re-validated.
  3. **Limits and overrides** — even a model that is right on average can produce extreme outputs in edge cases; limits cap the damage.
  4. **Model inventory and classification** — every model in the firm is logged with its owner, its purpose, its assumptions, its limitations, and its approval status.
  5. **Stress testing and scenario analysis** — the model is run under *adversarial* scenarios that are not in the historical record.

- **The "Mark-to-Market vs Mark-to-Model" Dilemma**:
  - When a market price is available, use it. When it is not, use a model. The two are not equivalent: a model price carries model risk.
  - *Why it matters*: structured products, illiquid bonds, and exotic derivatives are typically "marked to model"; the model's owner is responsible for the price.

- **The "Replacing the Vendor Model" Decision**:
  - Many banks use vendor models (e.g. Bloomberg, Reuters, Numerix). The bank's model risk function must still validate the vendor model — *the bank cannot outsource model risk*.

- **The "Vintage" Model Problem**:
  - Models age. A 2006-vintage VaR model is not a 2026-vintage model. The parameters and the world have moved; the validation must be redone.

## Key Concepts

1. **Model risk** — the risk that a model is wrong, and the consequences of that wrongness.
2. **Independent validation** — the formal process by which a model is reviewed by someone other than its owner.
3. **Ongoing monitoring** — the formal process of tracking a model's performance over time.
4. **Domain of validity** — the set of inputs and conditions under which a model is supposed to be accurate.
5. **Mark-to-market** — valuing an instrument at the observed market price; carries price risk but not model risk.
6. **Mark-to-model** — valuing an instrument at the model price; carries both price and model risk.
7. **Vendor model** — a model provided by an external vendor; the bank still owns the model risk.
8. **Model inventory** — the firm's register of all production models and their status.
9. **Model risk capital add-on** — the regulatory capital charge for the risk of model failure; FRTB has explicit provisions.
10. **The Basel SR 11-7 framework** — the Fed/OCC model risk management guidance; the binding US standard.

## Formulas & Reference Tables

**No specific formulas in this chapter.** The chapter is about *process* and *control*, not calculation. The relevant quantitative content is in ch12 (backtesting) and ch14 (model-building).

**Key reference: the FRTB model risk capital add-on (BCBS 457 §MAR30–MAR33)**:

A bank using the Internal Models Approach (IMA) must hold a **Default Risk Charge (DRC)** in addition to the ES charge, to cover the risk of default that the ES model misses. The DRC is calculated using a specific formula based on PD and LGD; the bank cannot use the ES model for default risk. This is the explicit regulatory recognition that *no single model is sufficient for all risk types*.

**The Basel III supervisory review process (Pillar 2) and model risk**:

The supervisor reviews the firm's model risk management framework; inadequate framework leads to Pillar 2 capital add-ons. This is the *qualitative* regulatory check on the *quantitative* model output.

**The Hull 4e checklist for model risk management (paraphrased)**:

| Check | Description | Frequency |
|---|---|---|
| Inventory | All production models are registered with owner, version, approval | Continuous |
| Independent validation | A second party challenges the assumptions and tests the outputs | Initial + on material change |
| Ongoing monitoring | The model output is compared to actual outcomes; threshold breaches trigger re-validation | Continuous |
| Stress testing | The model is run under adversarial scenarios | Quarterly |
| Limits | The model's output is constrained by limits that prevent extreme values | Continuous |
| Override audit | All manual overrides are logged and reviewed | Continuous |

## Mental Models

- **Every model is wrong; the question is where and how much.** Model risk management is the discipline of bounding the "where and how much".
- **The most dangerous models are the most widely used ones.** The Gaussian copula's collapse in 2008 is the canonical example; a model used by everyone is a model whose failure hurts everyone.
- **Vendor models are not free of model risk.** The bank owns the risk, not the vendor.
- **The model that "worked" in backtesting is the model most likely to fail in production.** Because the backtest is the selection criterion; the model has been chosen for its backtest fit, not for its truth.

## Worked Example (RECOMPUTED — illustrative)

*Setup.* A bank uses a 1-factor Gaussian copula to price a CDO tranche. The copula was validated in 2006 and approved by the model risk function. The 2008 default correlation spike (the "correlation breakdown") was not in the validation data.

*Step 1 — Model risk identification*.
- The Gaussian copula is *fundamentally wrong* for CDO tranche pricing in stress — the copula's tail dependence is too low, and the implied correlation is forced to fit a calm data window.
- This is reason 3 of the Hull 4e list (the model is used outside its domain of validity).

*Step 2 — The 2008 losses*.
- Mark-to-model prices of senior tranches collapsed from $0.95 to $0.40 in 6 months.
- The model said the tranche was "AAA-equivalent" until the actual losses hit.

*Step 3 — The controls that should have caught it*.
- *Independent validation*: a strong validation function would have noted that the model's tail dependence was 0 and asked "what happens if defaults are correlated?"
- *Ongoing monitoring*: a good monitoring function would have flagged that the model's implied correlation was 5× the historical correlation in late 2007.
- *Stress testing*: a good stress test would have run a "correlation breakdown" scenario.
- *Limits*: a good limit would have capped the notional of the CDO book relative to the firm's capital.

*Step 4 — The lessons*.
- Models must be tested under *adversarial* scenarios, not just historical data.
- A model used by everyone is not a safe model; it is a concentrated risk.
- Vendor models must be validated; the bank cannot outsource model risk.

*Note*: this worked example is illustrative of the framework; the 2008 CDO episode is not in the Hull 4e text. The agent should treat the 2008 episode as the *canonical case study* of model risk failure and reference it when discussing the chapter's principles.

## Anti-patterns

- **Treating a vendor model as "the truth".** The bank owns the model risk, not the vendor.
- **Validating a model once and never re-validating.** Models age; the world changes.
- **Using a backtest fit as the sole validation criterion.** Backtest fit selects for *fitting*, not for *truth*.
- **Ignoring the tail.** The Gaussian copula's tail was the problem, not its central fit.
- **Skipping the override audit.** Overrides are the universal loophole; they must be logged and reviewed.
- **Confusing model risk with model error.** Model error is the *consequence*; model risk is the *exposure* to that consequence.

## Practitioner Notes

- **2026 update.** The FRTB IMA requires **ongoing P&L attribution testing** (PLAT) of the IMA model against the daily risk-theoretical P&L. The PLAT compares the VaR-based hypothetical P&L to the actual P&L; a systematic mismatch is a red-zone flag. This is the modern formalisation of the Hull 4e "ongoing monitoring" check.
- **SR 11-7** (the Fed/OCC 2011 guidance on Model Risk Management) is the binding US regulatory text. It establishes the "three lines of defence" model: (1) the model owner, (2) independent validation, (3) internal audit. The Hull 4e chapter is consistent with SR 11-7 but does not cite it explicitly.
- **The European equivalent** is the EBA Guidelines on Model Risk Management (2024 update). Both frameworks require an inventory, an independent validation function, ongoing monitoring, and a clear escalation path for material model issues.
- **The agent's responsibility.** A quant agent that uses a model is responsible for *understanding its failure modes*. The agent's skill output should always include a "When this model fails" subsection, derived from the source.
- **Model risk ≠ model uncertainty.** Model uncertainty is the *quantitative* characterisation of how wrong the model could be (e.g. the variance of the parameter estimate). Model risk is the *qualitative* process discipline of bounding and monitoring that uncertainty.

## Key Takeaways

1. **Model risk is the risk that a model is wrong, and the consequences.** Every model is wrong somewhere.
2. **The reasons models fail** are: wrong model, wrong parameters, used outside domain, data errors, implementation errors, operational errors.
3. **The controls are**: independent validation, ongoing monitoring, limits and overrides, model inventory, stress testing.
4. **Vendor models are not free of model risk.** The bank owns the risk.
5. **The 2008 Gaussian copula collapse** is the canonical case study; a model used by everyone is a model whose failure hurts everyone.
6. **Model risk is a process discipline, not a calculation.** The output of the model risk function is *judgement*, not numbers.

## Connects To

- **ch12** (VaR and ES): the backtesting framework is one of the model risk controls.
- **ch14** (Model-Building Approach): the model-building approach itself is the source of model risk.
- **ch17** (FRTB): the FRTB IMA is the modern regulatory expression of the Hull 4e model risk framework.
- **`frtb-market-risk-bcbs457` skill**: the binding regulatory text.
- **`lopez-de-prado-afml` ch11 (Dangers of Backtesting), ch14 (Backtest Statistics), ch15 (Strategy Risk)**: the modern statistical continuation of the model risk discipline.
- **`hull-derivatives` ch15 (Volatility Smiles), ch17 (Volatility Surfaces), ch19 (Greek Letters), ch26 (More on Models and Numerical Procedures)**: the model risk in option pricing.
- **`tsay-analysis-financial-time-series` ch3–4 (ARMA, GARCH)**: the model risk in the time-series models.
- **`gatheral-volatility-surface` ch03 (Implied Volatility Surface)**: the model risk in the SVI parameterisation.
