---
name: ilmanen-yield-curve
description: "Antti Ilmanen, Understanding the Yield Curve (Salomon Brothers series, Parts 1-6, 1995): forward rate analysis, rate expectations vs risk premium vs convexity bias, long-run bond risk premium, forecasting bond returns, barbell-bullet trades, expected-return framework for curve trades. Use when analyzing the Treasury curve, forward rates, break-even yield changes, rolling yield, rolldown, pure expectations hypothesis, term premium, persistence factor, inverse wealth, duration timing, convexity value, barbell vs bullet, flatteners and steepeners, scenario analysis."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Understanding the Yield Curve (Salomon Brothers series, Parts 1–6)
**Source**: Antti Ilmanen, Salomon Brothers U.S. Fixed-Income Research, 1995 | **Domain**: Finance de marché | **Chapters**: 6 | **Generated**: 2026-09-30

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch04`
- **Browse** — "what chapters do you have?"

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Reading the curve**
- **Three influences on curve shape** (ch01, ch06): `f(n−1,n) = s₁ + Dur·E(Δs) + BRP + CB`. Expectations, risk premium, convexity bias (negative). It is an identity, so each split needs a proxy: surveys for expectations, long-run returns for premia, implied or historical volatility for convexity.
- **Shape reading** (ch06): expected parallel moves set slope, reshaping expectations set curvature, premia set average slope and front-end concavity, convexity sags the long end.
- **Forwards are break-evens first, expectations last** (ch01, ch02): model-free. Short duration only if you expect a rise larger than `f₁,ₙ − sₙ₋₁`. Forward-implied ≠ market-expected.
- **Risk premium hypothesis beats PEH** (ch02): persistence factor ~0.8 below 1y and 1.4–2.3 beyond. Use today's curve as the base case; rolling-yield advantages tend to be kept.

**Break-evens and carry**
- **Break-even = carry cushion + rolldown** (ch02): `Δfₙ₋₁ = (sₙ − s₁)/Dur_h + (sₙ − sₙ₋₁)` approximately.
- **Rolling yield** (ch01): `fₙ₋₁,ₙ ≈ sₙ + (n−1)(sₙ − sₙ₋₁)` is a zero's return on an unchanged curve; the one-year forward curve is an expected-return map.
- **Forward curve as magnifying glass** (ch01): high local forwards flag cheap sectors; trade level- and slope-neutral butterflies.
- **Forward-spot premium** (ch02): `FSP = (n−1)·Δfₙ₋₁`; linear spot curve gives FSP = 2 × term spread.

**Strategic duration and premia**
- **Concave premium** (ch03): US 1970–94 premium ~200bp from 1m to 2y and ~0 beyond; Sharpe falls with maturity. Keep short-horizon benchmarks ≤ ~2y; long bonds for long liabilities or tactical views.
- **Neutral sample rule** (ch03): never quote a premium without the sample's yield trend; `GM ≈ AM − σ²/2`.
- **Extend within cash** (ch03): 3m bills beat 1m bills 99% of years; take credit at the short end.

**Tactical timing**
- **Four-predictor model** (ch04): term spread, real yield, inverse wealth, momentum; R² ~10%, hit rate 61%. Inverse wealth separates a premium-steep curve from an expectations-steep one.
- **Scale with forecast size** (ch04): scaled strategy Sharpe 0.68 vs always-bond 0.06; judge over 3–5 years, out-of-sample only.

**Convexity and trades**
- **Convexity-adjusted expected return** (ch05): rolling yield + `½·Cx·σ²`, with `Cx ≈ Dur²/100` for zeros; watch bp vs relative volatility.
- **Barbell-bullet break-evens** (ch05): compute flattening and parallel-shift break-evens. It is usually a curve trade with a convexity kicker (10s–30s: 11bp vs 138bp).
- **Five-term expected return** (ch06): yield + rolldown + convexity + view + local rich/cheap. Prefer trades whose edge is in the static terms.
- **Scenario analysis with probabilities** (ch06): back out implied mean view, volatility and correlations; one scenario means zero volatility.

---

## Chapter Index
| # | Title | Part (book) | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-overview-of-forward-rate-analysis.md) | Overview of Forward Rate Analysis | Part 1 | Three influences, forwards as break-evens, cheap-sector butterflies |
| [ch02](chapters/ch02-market-rate-expectations-and-forward-rates.md) | Market's Rate Expectations and Forward Rates | Part 2 | PEH vs risk premium hypothesis, persistence factor, break-even spread change |
| [ch03](chapters/ch03-duration-extension-and-bond-risk-premium.md) | Duration Extension and Bond Risk Premium | Part 3 (OCR) | Six BRP theories, neutral sample, strategic duration |
| [ch04](chapters/ch04-forecasting-us-bond-returns.md) | Forecasting U.S. Bond Returns | Part 4 | Four-predictor model, scaled and 1/0 strategies |
| [ch05](chapters/ch05-convexity-bias-and-the-yield-curve.md) | Convexity Bias and the Yield Curve | Part 5 | Convexity-adjusted return, barbell-bullet break-evens |
| [ch06](chapters/ch06-framework-for-analyzing-yield-curve-trades.md) | Framework for Analyzing Yield Curve Trades | Part 6 (OCR) | Forward decomposition, five-term return, scenarios |

## Topic Index
- **Arithmetic vs geometric mean** → ch03, ch05
- **Barbell-bullet trades** → ch01, ch02, ch05, ch06
- **Bond risk premium** → ch01, ch03, ch04, ch06
- **Bootstrapping** → ch01
- **Break-even yield change** → ch01, ch02
- **Career risk** → ch03, ch04
- **Cash management / money-market curve** → ch03
- **Cheap sectors via forwards** → ch01
- **Convexity bias** → ch01, ch05, ch06
- **Convexity value** → ch05, ch06
- **Curvature measurement** → ch02, ch05
- **Data snooping** → ch04
- **Duration timing** → ch03, ch04
- **Dynamic strategies (scaled, 1/0)** → ch04
- **Expanding-window forecast** → ch04
- **Flatteners and steepeners** → ch02, ch05
- **Forward rates** → ch01, ch02, ch06
- **Forward-spot premium** → ch02, ch06
- **Geometric premium by maturity** → ch03
- **Hit rates** → ch03, ch04
- **Implied volatility of barbell-bullet** → ch05
- **International bond premia** → ch03
- **Inverse wealth** → ch04
- **Liquidity premium / preferred habitat** → ch01, ch03
- **Local expectations hypothesis** → ch01, ch02, ch06
- **Local rich/cheap, repo** → ch06
- **Momentum** → ch04
- **Par, spot, forward ordering** → ch01
- **Persistence factor** → ch02, ch04
- **Pure expectations hypothesis** → ch01, ch02
- **Real yield** → ch04
- **Risk premium hypothesis** → ch02
- **Rolldown** → ch01, ch02, ch06
- **Rolling yield** → ch01, ch02, ch05
- **Scenario analysis** → ch06
- **Sharpe ratio by maturity** → ch03, ch04
- **Survey expectations** → ch02, ch06
- **Term spread** → ch01, ch04
- **Unbiased expectations hypothesis** → ch01, ch02, ch06
- **Volatility (bp vs relative), term structure** → ch03, ch05
- **Yield to maturity limits** → ch01

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules and thresholds

---

## Related Skills
- `tuckman-fixed-income` — forward/spot algebra (ch02), carry and roll-down (ch03), short-rate models and curve shape (ch08)
- `cfa-fixed-income` — term structure theories (ch07), yield curve strategies (ch14)
- `ecb-yield-curve-modelling` — fitting Nelson–Siegel and Svensson curves
- `cfa-asset-allocation-cme` — term premium in capital market expectations (ch04)
- `hull-derivatives` — no-arbitrage forwards, volatility and straddle analogy
- `cfa-level1-curriculum` — duration and convexity basics (ch18)

## Scope & Limits
- Covers the 1995 Salomon Brothers series on U.S. Treasuries; data end 1994–95 (1970–94 premia, 1965–95 forecasting). Conclusions are sample-dependent; re-test on current data.
- Parts 3 and 6 were read from OCR; some figures are charts and were described from text, and a few numbers were corrected (flagged ⚠ in chapters).
- Does not cover callable/MBS convexity, unhedged FX, or modern post-2008 regimes.
