---
name: ecb-yield-curve-modelling
description: "Knowledge base from Per Nymand-Andersen, 'Yield curve modelling and a conceptual framework for estimating yield curves: evidence from the European Central Bank's yield curves' (ECB Statistics Paper No 27, 2018). Use when estimating or choosing a government yield curve model, fitting Nelson-Siegel or Svensson curves, spline models (McCulloch, Fisher-Nychka-Zervos, Waggoner, variable roughness penalty), cleaning a bond sample, testing curves in and out of sample, or explaining why the ECB uses Svensson. Topics: spot, forward, par curve, level slope curvature, smoothness vs flexibility, WMAE, RMSE, hit rate, robustness, knot points, outlier removal, break-even inflation."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Yield Curve Modelling and the ECB Yield Curves
**Source**: Per Nymand-Andersen, ECB Statistics Paper Series No 27 (February 2018) | **Domain**: Finance de marché | **Chapters**: 8 | **Generated**: 2026-09-29

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `Svensson`, `hit rate` or `outlier removal`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch03`
- **Browse** — "what chapters do you have?"

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**1. The curve is an estimate, never an observation.** Euro area bonds beyond 12 months are coupon bonds, so spot, forward and par curves are inferred through a functional form or spline fitted to prices (ch01).

**2. Fit versus smooth is a dial set by the use.** Policy or communication curve: smoother and more transparent. Relative value or anomaly spotting: more flexible. Never judge on in-sample error alone (ch04, ch06).

**3. Nelson-Siegel (4 parameters).** `f(t) = β₀ + β₁e^(−t/τ) + β₂(t/τ)e^(−t/τ)`. β₀ = long asymptote (>0), β₀+β₁ = short rate (>0), β₂ = hump, τ = hump position. Spot: `s(T) = β₀ + β₁g + β₂(g − e^(−T/τ))`, `g = (1−e^(−T/τ))/(T/τ)` (ch03).

**4. Svensson (6 parameters)** adds `β₃(t/τ₂)e^(−t/τ₂)` for a second hump. Better fit and the ECB's model, but over-parameterised: different parameter sets give almost identical curves; use yesterday's parameters as starting values (ch03, ch08).

**5. Spline family.** McCulloch fits the discount function (unstable forwards); FNZ fits the forward function with a constant roughness penalty (poor short end); Waggoner uses a step penalty at 1 and 10 years (0.1 / 100 / 100,000); Anderson-Sleath VRP uses a continuous penalty `λ(m) = 10^[log₁₀L − (log₁₀L − log₁₀S)e^(−m/μ)]` with L=100,000, S=0.1, μ=1 (ch02).

**6. Data quality beats model choice.** Twelve recommendations: credit-homogeneous central-government bonds, no options or indexation, turnover at least EUR 1m a day, bid-ask at most 3 bp, mid-quote near 17:00 CET, 3 months to 30 years, 2σ outlier removal twice per maturity bracket, stable composition (ch05).

**7. Testing protocol.** Hold out 1 bond in 10 ranked by maturity; test over five regimes; three criteria: flexibility and goodness of fit, robustness, smoothness (ch06).

**8. Error statistics.** RMSE `√(Σ(y−ŷ)²/N)`, MAE `Σ|y−ŷ|/N`, WMAE with 1/√duration weights, hit rate within a band; state the band (1.5, 3, 5 bp) (ch06).

**9. Evidence.** All four models fit within a few bp (WMAE 2-5 bp). Svensson slightly beats N&S; splines fit marginally closer but are erratic at 10-30 years (VRP worst); the calm 2003-2005 sample limits generality (ch07).

**10. Why the ECB picked Svensson.** Fit differences insignificant, so transparency, communicability and a stable long end decided. Splines stay for cross-area comparison. Settings: yield minimisation, β₀ positive, previous-day starts, spot/forward/par, 12:00 CET release (ch08).

**11. Reading the curve.** Forwards are expected short rates plus a premium, not forecasts; steepening often precedes acceleration, flattening or inversion a slowdown; nominal minus inflation-linked gives break-even inflation (ch01).

**12. Visual inspection is mandatory.** Hit rates and RMSE missed erratic spline behaviour at long maturities; compare forwards, not spots, to see method risk (ch04, ch07).

---

## Chapter Index
| # | Title | Part of paper | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-yield-curve-methods-for-central-banking.md) | Yield Curve Methods for Central Banking | Summary, §1-§3 intro | Curve uses, four term-structure theories, level/slope/curvature |
| [ch02](chapters/ch02-spline-based-models.md) | Spline-Based Models | §3.1, App. 2-3 | McCulloch, FNZ, Waggoner, VRP, B-spline, penalty |
| [ch03](chapters/ch03-parsimonious-functional-forms.md) | Parsimonious Functional Forms | §3.2, Table 6 | Nelson-Siegel, Svensson, hybrid, spot/forward formulas |
| [ch04](chapters/ch04-comparing-spline-and-parsimonious-models.md) | Comparing Spline and Parsimonious Models | §3.3, §5.4 | Smoothness-fit trade-off, literature scorecard |
| [ch05](chapters/ch05-bond-sample-selection-and-data-cleaning.md) | Bond Sample Selection and Data Cleaning | §4, Table 9 | 12 data recommendations, 2σ outlier filter |
| [ch06](chapters/ch06-testing-framework-and-evaluation-criteria.md) | Testing Framework and Evaluation Criteria | §5, App. 1 | In/out-of-sample, WMAE, RMSE, hit rate, robustness, smoothness |
| [ch07](chapters/ch07-empirical-results-euro-area-government-bonds.md) | Empirical Results on Euro Area Bonds | §6 | Four-model scorecard, spread diagnostics |
| [ch08](chapters/ch08-model-selection-and-ecb-implementation.md) | Model Selection, ECB Implementation, Conclusions | Conclusions, App. 6 | Svensson choice, Table F.1 settings |

## Topic Index
- **Anderson-Sleath penalty** → ch02
- **Asymptote β₀** → ch03
- **B-spline / De Boor** → ch02
- **Bank of England / national practices** → ch04, ch08
- **Banque de France hybrid** → ch03, ch07
- **Bid-ask spread filter** → ch05
- **Break-even inflation** → ch01
- **Coupon bond / zero-coupon scarcity** → ch01
- **Credit risk / AAA sample** → ch05, ch08
- **Data supplier criteria** → ch05
- **Day-count and settlement** → ch05, ch08
- **Discount function** → ch02
- **ECB methodology (Table F.1)** → ch08
- **Error statistics (RMSE, MAE, WMAE)** → ch06
- **ESA 2010 sectors** → ch05
- **Fisher-Nychka-Zervos** → ch02, ch04
- **Flexibility vs smoothness** → ch01, ch04, ch06
- **Forward rate** → ch01, ch03
- **Hit rate** → ch06, ch07
- **Hybrid model** → ch03, ch07
- **In-sample / out-of-sample** → ch06
- **Knot points** → ch02, ch06
- **Level, slope, curvature** → ch01, ch03
- **Liquidity (turnover, spread)** → ch05
- **Literature review (Bliss, Waggoner)** → ch04
- **McCulloch** → ch02
- **Mid-quote price** → ch05
- **Nelson-Siegel** → ch03
- **Optimisation and starting values** → ch03, ch08
- **Outlier removal** → ch05
- **Over-parameterisation** → ch03, ch07
- **Par yield curve** → ch01, ch03
- **Parsimonious models** → ch03, ch04
- **Robustness test** → ch06, ch07
- **Roughness penalty** → ch02
- **Sample size and time periods** → ch05, ch06
- **Smoothness test** → ch06, ch07
- **Spline models** → ch02, ch04
- **Spot rate** → ch01, ch03
- **Svensson** → ch03, ch07, ch08
- **Term-structure theories** → ch01
- **Test periods (regimes)** → ch06
- **Variable roughness penalty (VRP)** → ch02, ch07
- **Waggoner** → ch02, ch04
- **WMAE** → ch06, ch07
- **Yield minimisation** → ch03, ch08
- **Zero lower bound** → ch04, ch08

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, tells

---

## Related Skills
- `tuckman-fixed-income` — ch21 curve construction, ch02 spot/forward/par relationships
- `ilmanen-yield-curve` — what forward curves mean: expectations, term premia, curve trades
- `cfa-fixed-income` — ch07 term structure and interest rate dynamics (spot, forward, par, level/slope/curvature)
- `hull-derivatives` — ch4 interest rates, zero rates, forward rates

## Scope & Limits
Covers one ECB paper: euro area government bond curves, 2003-2005 data, four models. Tables 7-8 and the charts are images, so numeric ranges come from the text. It does not cover no-arbitrage dynamic models in depth, corporate or swap curves, or behaviour at the zero lower bound (flagged as research). Two source inconsistencies are flagged in ch02 (penalty formula) and ch06 (hit-rate band).
