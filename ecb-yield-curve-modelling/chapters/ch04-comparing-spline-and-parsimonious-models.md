# Chapter 4: Comparing Spline-Based and Parsimonious Models
> **Source**: ECB Statistics Paper No 27 (2018), §3.3 and end of §3 (national practices), §5.4 (model selection) | Nymand-Andersen

## Core Idea
Neither family dominates. Splines fit more closely but oscillate at the long end, are sensitive to settings and are hard to explain; parsimonious models give smooth, stable, interpretable curves but may be too stiff at the short end. The literature (Waggoner, Anderson et al., Anderson-Sleath, Bliss) and the ECB's own tests converge on one rule: pick the model by the purpose of the curve, and test it in and out of sample.

## Frameworks Introduced
- **Smoothness versus fit trade-off**: every method sits on a line between "too flexible" (fits outliers, oscillates) and "too parsimonious" (misses genuine bends).
  - When to use: before choosing a model, state the final use (policy indicator, pricing, relative value).
  - How: policy/communication curve leans to smoothness; detection of rich/cheap bonds leans to flexibility.
  - Failure mode: one-number judgement (in-sample RMSE) that rewards over-fitting.
- **Literature scorecard** (who found what):
  - Waggoner (1997): FNZ beats McCulloch above 1 year; McCulloch beats FNZ below 1 year; Waggoner's variable penalty beats McCulloch everywhere and FNZ at short maturities, though McCulloch and penalty methods give very similar results.
  - Anderson et al. (1996), UK: four methods give similar spot curves but very different **forward** curves; N&S and Svensson forwards gravitate to a flat long end; McCulloch forwards fluctuate and ascend steeply; Mastronikola flattens but with more curvature.
  - Anderson-Sleath (1999): Svensson beats N&S out of sample; Waggoner VRP beats FNZ (FNZ lacks short-end flexibility like N&S); main VRP-Svensson differences are robustness and long-end constraints (Svensson converges to a constant; VRP is only forced to be very smooth). A single changed long-end data point can change Svensson dramatically, even at the short end.
  - Bliss (1996): FNZ performs badly in and out of sample (short maturities, measurement-error sensitive); smoothed Fama-Bliss, Svensson and McCulloch perform comparably.
- **Model selection design (ECB)**: test both families with the same data and tests; involve several central banks; accept that the same model implemented by different banks differs (curve type, objective, constraints, starting values, algorithm).

## Key Concepts
- **Flexibility**: capacity to track short-end curvature and genuine bends.
- **Smoothness**: absence of abrupt breaks; slope changes come from the market, not the model.
- **Robustness**: stability to small data changes or outliers.
- **Transparency**: ease of communicating and interpreting parameters.
- **Over-fitting**: fitting noise; splines can match in-sample data with arbitrary precision.
- **Over-parameterisation**: several parameter sets, nearly the same curve (parsimonious models too).
- **Long-end constraint**: Svensson/N&S forward converges to a constant; splines are merely smooth there.
- **Segmented market assumption**: justification for a step penalty with steps at 1 and 10 years.
- **Hybrid model**: Banque de France N&S/Svensson switch.
- **Knot spacing rule**: roughly equal bonds between knots (Bank of Greece: a knot about every sixth bond), not every 3-4 bonds.
- **National practices**: N&S and Svensson dominate inside the euro area (Bundesbank, Banco de España, Banca d'Italia, Banque de France); Waggoner-type splines at BoE, NY Fed, BoJ, BoC.

## Formulas & Reference Tables
| Criterion | Spline-based (Waggoner, VRP) | Parsimonious (N&S, Svensson) |
|---|---|---|
| Parameters | Knots + 2 (many) | 4 or 6 |
| Interpretation | Little economic meaning | Level, slope, hump, asymptote |
| Short-end flexibility | High (variable penalty) | Limited (N&S), better (Svensson) |
| Long-end behaviour | Smooth but can be erratic/volatile | Converges to a flat constant |
| Sensitivity to settings | Algorithm, smoothing parameters, penalty, knots | Starting values, algorithm |
| Sensitivity to one data point | Lower ("minimum support") for Waggoner | Higher at long end (Svensson changes short end) |
| Transparency for public release | Low | High |
| Best use | Comparisons across economic areas, spotting abnormal bonds | Published policy curves |

Models tested (Table 5): N&S and Svensson (Bundesbank, BdF, Greece); Waggoner step-wise penalty, steps at 1 and 10 years (Greece, BoE); Waggoner with continuous VRP (BoE). Waggoner run with **yield** minimisation; VRP with **price weighted by duration** minimisation.

## Mental Models
- **Curve differences hide in the forwards**: spot curves look alike across methods; compare forward curves to see method risk.
- **Spline = tailor-made suit, parsimonious = off the rack**: better local fit versus portability and interpretability.
- **Out-of-sample is the referee**: in-sample always favours more parameters.
- **Bond sample quality can outweigh model choice**: differences between models were small once the sample was clean (ch07).

## Worked Example
Choosing a model for a daily published policy curve (reasoning recast from §3.3 and §5.4):
1. Purpose = market-expectation indicator, public release, long history → smoothness, transparency, stability rank first.
2. Candidate set: Svensson (6 parameters), VRP (3 smoothing parameters plus knots).
3. Evidence: both fit within about 3-7 bp; splines slightly lower errors to 10 years, but long-end (10-30 years) hit rates fall to 4-5% and spreads become volatile for VRP.
4. Decision: Svensson; keep VRP/Waggoner for cross-area comparison. Outcome as in ch08.

## Anti-patterns
- **Choosing by in-sample fit alone**: spline wins trivially.
- **Ignoring implementation differences** when comparing banks' results: starting values, objective and algorithm differ.
- **Placing knots by a rule built for small national samples**.
- **Assuming a spline's extra flexibility at 20-30 years is information**: data are sparse there.

## Practitioner Notes
- Anderson-Sleath note: parametric curves are less suited to spotting anomalies in single maturities or bonds; spline curves are better there.
- Brousseau (2002): a one-factor Duffie-Kan model with five parameters fits observed curves to within a few basis points; theoretical mean curves are less concave than observed ones (multi-factor affine models address this).
- The paper does not explicitly model rates near the zero lower bound; it flags that as further research.

## Key Takeaways
1. No universal winner; purpose decides.
2. Splines: best fit, hardest to explain, most settings.
3. Parsimonious: smooth, interpretable, limited flexibility.
4. Forwards, not spots, show methodological differences.
5. Use both in-sample and out-of-sample tests (ch06).
6. Long-end behaviour separates the families.
7. Document assumptions (segmentation, penalty steps, knots).

## Connects To
- **ch02**, **ch03**: the two model families.
- **ch06**: test design; **ch07**: evidence; **ch08**: resulting choice.
- **`tuckman-fixed-income` ch21**: fitted versus exact curve construction.
- **`ilmanen-yield-curve`**: curve-fitting model risk and PCA factors.
