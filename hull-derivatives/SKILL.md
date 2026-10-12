---
name: hull-derivatives
description: "Knowledge base from \"Options, Futures, and Other Derivatives\" (11th ed.) by John C. Hull. Use when pricing or hedging forwards, futures, swaps, options (Black-Scholes-Merton, binomial trees, Black's model), computing Greeks, VaR/ES, CVA/XVA, credit derivatives, exotics, or interest rate models (Hull-White, LMM), studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# Options, Futures, and Other Derivatives (11th ed., Global Edition)
**Author**: John C. Hull | **Pages**: ~880 | **Chapters**: 37 | **Generated**: 2026-09-29

## How to Use This Skill

- **Without arguments**: load the core frameworks below for reference.
- **With a topic**: ask about `put-call parity`, `CVA`, `swaption`, `GARCH` or any indexed topic, and I read the relevant chapter.
- **With a chapter**: ask for `ch19` and I load that chapter.
- **Browse**: ask "what chapters do you have?" to see the full index.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering. For formulas, the chapter files hold the exact expressions and a worked numeric example checked against the book.

---

## Core Frameworks & Mental Models

**1. No-arbitrage is the axiom; replication is the method.** Price any derivative by building a portfolio that reproduces its payoff. A riskless portfolio earns r (Ch 5, 13, 15).

**2. Cost of carry (forwards/futures).**
- `F₀ = S₀e^{(r+u−q)T}` for investment assets. Use q = dividend yield, r_f for FX, u = storage.
- Consumption assets: `F₀ ≤ S₀e^{(r+u)T}`. The gap is the convenience yield.
- Value a forward as `(F₀ − K)e^{−rT}`, i.e. assume the forward price is realized, then discount (Ch 5).

**3. Hedging trades price risk for basis risk.**
- Effective hedge price = F₁ + b₂.
- Minimum-variance hedge ratio `h* = ρσ_S/σ_F`. Number of contracts `N* = h*V_A/V_F`. Equity portfolios: `N* = βV_A/V_F`.
- Duration hedge: `N* = P·D_P/(V_F·D_F)` (Ch 3, 6).

**4. Swaps = portfolios of forwards.**
- Value by assuming forward rates or FX rates are realized, then discount at OIS/SOFR.
- The swap rate is the par yield. New swaps are worth zero, which is how the OIS curve is bootstrapped (Ch 7).

**5. Option bounds and parity need no model.**
- `c + Ke^{−rT} = p + S₀`, with PV(dividends) subtracted from S₀ when there are dividends.
- An American call on a non-dividend stock is never exercised early. An American put may be (Ch 11).

**6. Risk-neutral valuation.**
- Price = e^{−rT} × E_Q[payoff], with every asset drifting at r. The real-world μ never enters.
- Tree: `p = (a − d)/(u − d)`, `u = e^{σ√Δt}`. Use a = e^{(r−q)Δt}, e^{(r−r_f)Δt} for FX, or 1 for futures (Ch 13).

**7. Black–Scholes–Merton / Black.**
- `c = S₀e^{−qT}N(d₁) − Ke^{−rT}N(d₂)` with `d₁ = [ln(S₀/K) + (r − q + σ²/2)T]/(σ√T)` and `d₂ = d₁ − σ√T`.
- On futures or forwards (Black): `c = e^{−rT}[F₀N(d₁) − KN(d₂)]`.
- Prefer Black whenever a clean forward exists (Ch 15, 17, 18).

**8. Greeks and dynamic hedging.**
- Δ = N(d₁)e^{−qT}, Γ = N′(d₁)/(Sσ√T), Vega = S√T N′(d₁).
- Delta-neutral books satisfy `Θ + ½σ²S²Γ = rΠ`: long gamma is paid for with theta.
- Neutralize gamma and vega with traded options (two options for both), then fix delta with the underlying. Rebalance delta daily (Ch 19).

**9. The smile is the market's real model.**
- Implied volatility is the same for calls and puts at the same K and T.
- Equity: downward skew (crash fear). FX: U-shaped smile.
- Use the volatility surface as the pricing object, and delta-hedge with the minimum-variance delta (Ch 20).

**10. Numerical method by structure.**
- American with ≤2 factors → tree or finite differences.
- Path-dependent or high-dimensional → Monte Carlo, with variance reduction and the standard error reported.
- American by simulation → Longstaff–Schwartz (Ch 21, 27).

**11. Risk measures.**
- `VaR = z·σ_P·√N`. ES = the mean loss beyond VaR. ES is coherent; regulators use 97.5% ES.
- Option books need delta–gamma or full revaluation.
- EWMA (λ ≈ 0.94) tracks volatility. GARCH(1,1) mean-reverts to `V_L = ω/(1 − α − β)` (Ch 22, 23).

**12. Credit.**
- Hazard rate `λ ≈ s/(1 − R)`. Use risk-neutral probabilities for pricing, real-world for scenarios.
- Merton: equity = a call on the assets, PD = N(−d₂).
- Adjusted value = `f_nd − CVA + DVA`, with `CVA = Σqᵢvᵢ` computed on netting sets.
- CDS spread ≈ λ(1 − R). Default correlation moves value between equity and senior tranches (Ch 9, 24, 25).

**13. Interest rate options.**
- Black is applied to whichever variable is lognormal under the right numeraire: the forward bond price, each forward rate (caplets, T-forward measure), or the forward swap rate (swaptions, annuity measure).
- Payoffs outside their natural numeraire need adjustments: convexity (CMS), timing (in arrears), quanto (cross-currency) (Ch 28–30).

**14. Term-structure models.**
- Vasicek/CIR are equilibrium models and do not fit today's curve.
- Ho–Lee and Hull–White (`dr = [θ(t) − ar]dt + σdz`) fit the curve exactly and are implemented on trinomial trees.
- HJM/LMM model forward rates. In HJM the drift is set by the volatilities. Calibrate to caps and swaptions (Ch 31–33).

**15. Controls beat models.** Most disasters came from hedgers turning into speculators, unenforced limits, blind trust in models and ignored liquidity risk: Barings, SocGen, LTCM, Metallgesellschaft, Orange County (Ch 37).

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-introduction.md) | Introduction | Payoffs, hedgers/speculators/arbitrageurs |
| [ch02](chapters/ch02-futures-markets-and-ccps.md) | Futures Markets and CCPs | Margin, clearing, convergence |
| [ch03](chapters/ch03-hedging-strategies-using-futures.md) | Hedging Strategies Using Futures | Basis risk, h*, beta hedge, stack & roll |
| [ch04](chapters/ch04-interest-rates.md) | Interest Rates | Compounding, bootstrap, FRA, duration |
| [ch05](chapters/ch05-forward-and-futures-prices.md) | Forward and Futures Prices | Cost of carry, convenience yield, IRP |
| [ch06](chapters/ch06-interest-rate-futures.md) | Interest Rate Futures | CTD, SOFR futures, duration hedge |
| [ch07](chapters/ch07-swaps.md) | Swaps | IRS/currency swap valuation, OIS bootstrap |
| [ch08](chapters/ch08-securitization-and-2007-crisis.md) | Securitization and the 2007–8 Crisis | ABS, waterfall, ABS CDO |
| [ch09](chapters/ch09-xvas.md) | XVAs | CVA, DVA, FVA, MVA, KVA |
| [ch10](chapters/ch10-mechanics-of-options-markets.md) | Mechanics of Options Markets | Specs, margin, OCC |
| [ch11](chapters/ch11-properties-of-stock-options.md) | Properties of Stock Options | Bounds, put–call parity, early exercise |
| [ch12](chapters/ch12-trading-strategies-involving-options.md) | Trading Strategies | Spreads, straddles, box, PPN |
| [ch13](chapters/ch13-binomial-trees.md) | Binomial Trees | Replication, risk-neutral p, American |
| [ch14](chapters/ch14-wiener-processes-and-itos-lemma.md) | Wiener Processes and Itô's Lemma | GBM, Itô, lognormality |
| [ch15](chapters/ch15-black-scholes-merton-model.md) | Black–Scholes–Merton | BSM PDE/formulas, implied vol, dividends |
| [ch16](chapters/ch16-employee-stock-options.md) | Employee Stock Options | Expected-life valuation, backdating |
| [ch17](chapters/ch17-options-on-indices-and-currencies.md) | Options on Indices and Currencies | Merton q, Garman–Kohlhagen, insurance |
| [ch18](chapters/ch18-futures-options-and-blacks-model.md) | Futures Options and Black's Model | Black-76, futures trees |
| [ch19](chapters/ch19-the-greek-letters.md) | The Greek Letters | Δ Γ Θ Vega ρ, neutrality, portfolio insurance |
| [ch20](chapters/ch20-volatility-smiles-and-surfaces.md) | Volatility Smiles and Surfaces | Skew, smile, surface, MV delta |
| [ch21](chapters/ch21-basic-numerical-procedures.md) | Basic Numerical Procedures | Trees, Monte Carlo, finite differences |
| [ch22](chapters/ch22-var-and-expected-shortfall.md) | VaR and Expected Shortfall | Historical sim, linear/quadratic, PCA |
| [ch23](chapters/ch23-estimating-volatilities-and-correlations.md) | Estimating Volatilities and Correlations | EWMA, GARCH(1,1), MLE |
| [ch24](chapters/ch24-credit-risk.md) | Credit Risk | Hazard rates, Merton, CVA, copula |
| [ch25](chapters/ch25-credit-derivatives.md) | Credit Derivatives | CDS, indices, CDO tranches |
| [ch26](chapters/ch26-exotic-options.md) | Exotic Options | Barriers, binaries, Asians, variance swaps |
| [ch27](chapters/ch27-more-on-models-and-numerical-procedures.md) | More on Models and Numerics | CEV, jumps, SV, IVF, convertibles, LSM |
| [ch28](chapters/ch28-martingales-and-measures.md) | Martingales and Measures | Market price of risk, numeraires |
| [ch29](chapters/ch29-interest-rate-derivatives-standard-market-models.md) | IR Derivatives: Standard Models | Bond options, caps, swaptions |
| [ch30](chapters/ch30-convexity-timing-and-quanto-adjustments.md) | Convexity, Timing, Quanto | CMS convexity, in-arrears, quanto |
| [ch31](chapters/ch31-equilibrium-models-of-the-short-rate.md) | Equilibrium Short-Rate Models | Vasicek, CIR |
| [ch32](chapters/ch32-no-arbitrage-models-of-the-short-rate.md) | No-Arbitrage Short-Rate Models | Ho–Lee, Hull–White, trinomial trees |
| [ch33](chapters/ch33-modeling-forward-rates.md) | Modeling Forward Rates | HJM, LMM/BGM, agency MBS |
| [ch34](chapters/ch34-swaps-revisited.md) | Swaps Revisited | Compounding, CMS, accrual, cancelable |
| [ch35](chapters/ch35-energy-and-commodity-derivatives.md) | Energy and Commodity Derivatives | Mean reversion, electricity, weather |
| [ch36](chapters/ch36-real-options.md) | Real Options | μ − λσ growth, project options |
| [ch37](chapters/ch37-derivatives-mishaps-and-lessons.md) | Derivatives Mishaps | Risk limits, controls, liquidity |

## Topic Index

- **American options / early exercise** → ch11, ch13, ch21, ch27
- **Asian options** → ch26, ch35
- **Barrier options** → ch26, ch27
- **Basis risk** → ch03
- **Binary options** → ch26
- **Black's model** → ch18, ch28, ch29
- **Black–Scholes–Merton** → ch15, ch17
- **Bootstrap (zero / OIS / hazard)** → ch04, ch07, ch24
- **Caps / floors** → ch29, ch33
- **CDS / credit indices** → ch07, ch25
- **CDO / ABS / tranches** → ch08, ch25
- **Cheapest-to-deliver** → ch06
- **Convenience yield** → ch05, ch35
- **Convertible bonds** → ch27
- **Convexity adjustment** → ch06, ch30
- **Copula (Gaussian)** → ch24, ch25
- **Cost of carry** → ch05
- **CVA / DVA / XVA** → ch09, ch24
- **Duration / convexity** → ch04, ch06, ch31
- **EWMA / GARCH** → ch23
- **Exotic options** → ch26
- **FRA** → ch04, ch07
- **Greeks (delta, gamma, vega, theta, rho)** → ch13, ch19
- **Hedge ratio** → ch03, ch19
- **HJM / LMM** → ch33
- **Ho–Lee / Hull–White** → ch32
- **Implied volatility / smile** → ch15, ch20
- **Itô's lemma / GBM** → ch14
- **Margin / clearing / CCP** → ch02, ch10
- **Market price of risk** → ch28, ch31, ch36
- **Martingale / numeraire** → ch28
- **Merton credit model** → ch11, ch24
- **Monte Carlo** → ch21, ch27
- **Mortgage-backed securities** → ch08, ch33
- **Portfolio insurance** → ch17, ch19
- **Put–call parity** → ch11, ch17, ch18
- **Quanto** → ch05, ch30
- **Real options** → ch36
- **Risk-neutral valuation** → ch13, ch15, ch28
- **Stochastic volatility / jumps** → ch27
- **Swaps (IRS, currency)** → ch07, ch34
- **Swaptions** → ch29
- **Trading strategies (spreads, straddles)** → ch12
- **Trees (binomial / trinomial)** → ch13, ch21, ch32
- **VaR / expected shortfall** → ch22
- **Vasicek / CIR** → ch31
- **Weather / insurance derivatives** → ch35

## Supporting Files

- [glossary.md](glossary.md): all key terms with definitions
- [patterns.md](patterns.md): pricing and hedging techniques as reusable recipes
- [cheatsheet.md](cheatsheet.md): decision rules, formulas and thresholds on one page

---

## Scope & Limits

This skill covers the book's content: synthesized notes, not the book's text. Worked examples reproduce the book's numbers for study. Market conventions (SOFR transition, FRTB) are as of the 11th edition (2021). Check current market data and regulation before relying on it in production. For code-level implementations, combine with project-specific tools. Related skills in this repo: `cfa-level1-curriculum`, `tian-commodity-price-jumps`, `pairs-trading-partial-cointegration`.
