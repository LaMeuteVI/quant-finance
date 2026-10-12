# Chapter 24: Credit Risk

## Core Idea
Default probabilities come from three sources:
- **Historical data** gives real-world probabilities.
- **Bond spreads** give risk-neutral probabilities.
- **Equity prices** (Merton) can give either.

Use risk-neutral probabilities for valuation (CVA, pricing). Use real-world probabilities for scenario analysis and credit VaR. Default correlation drives portfolio tail losses; the standard model is the Gaussian copula.

## Frameworks Introduced
- **Hazard rate (default intensity) λ(t)**:
  - Survival probability to t: `V(t) = e^{−λ̄(t)·t}`, where λ̄(t) is the average hazard rate to t.
  - Unconditional default probability in (t₁, t₂) = V(t₁) − V(t₂).
- **Credit spread approximation**: `λ̄ ≈ s(T)/(1 − R)`, where s is the spread over the risk-free rate and R is the recovery rate.
- **Bootstrapping hazard rates from bond prices**: match each bond's price to its expected default loss, one maturity at a time.
- **Real-world vs risk-neutral**: risk-neutral probabilities are much higher. The gap reflects the risk premium for default correlation and systematic risk, plus bond illiquidity.
- **Merton's model**: equity is a call on the firm's assets V, with strike equal to the debt D.
  - `E₀ = V₀N(d₁) − De^{−rT}N(d₂)` and `σ_E·E₀ = N(d₁)·σ_V·V₀`.
  - Solve these two equations for V₀ and σ_V. The default probability is `N(−d₂)`.
  - It ranks firms well. Calibrate it to actual default data (the KMV approach).
- **CVA computation**: `CVA = Σ qᵢ(1 − R)·EEᵢ·DFᵢ`.
  - EEᵢ is the expected exposure, from Monte Carlo simulation of the netting set.
  - The simulation includes collateral and the margin period of risk.
- **Credit risk mitigation**: netting, collateral (CSA), downgrade triggers, CCPs.
- **Default correlation**:
  - **Gaussian copula** of time to default: `xᵢ = aᵢF + √(1 − aᵢ²)Zᵢ`.
  - **Vasicek** worst-case default rate: `WCDR(T, X) = N[(N⁻¹(PD) + √ρ·N⁻¹(X))/√(1 − ρ)]`.
  - Regulatory capital (IRB): `capital = EAD × LGD × (WCDR − PD)`.
- **CreditMetrics**: a copula model of rating transitions. Credit VaR comes from simulated rating migrations.

## Key Concepts
- **Ratings**: AAA to BBB is investment grade; BB and below is junk. Agencies: Moody's, S&P, Fitch.
- **Cumulative default probability tables**:
  - Investment grade: default probabilities often *increase* with the horizon.
  - Junk: conditional default probabilities *decrease* with the horizon.
- **Recovery rate R**: the bond price just after default, as a percentage of face value. It is **negatively correlated** with default rates.
- **EAD and LGD**: exposure at default and loss given default (LGD = 1 − R).
- **Downgrade trigger**: collateral must be posted on a downgrade. In 2008 AIG needed massive collateral it could not raise.
- **Wrong-way risk**: exposure rises when the counterparty's default probability rises.

## Mental Models
- **Which measure to use**: valuation → risk-neutral; risk management and scenarios → real-world.
- **Spread ≈ λ(1 − R)** is an annual loss rate. A small change in the assumed recovery changes the implied λ a lot.
- **Equity volatility signals credit risk**: highly volatile equity plus high leverage means a high Merton default probability.
- **Correlation fattens the tail**: with the same average default probability, a higher ρ gives a much higher 99.9% loss.

## Anti-patterns
- **Using risk-neutral default probabilities for capital or scenario planning**: this overstates expected losses.
- **Relying on collateral downgrade triggers as a safety net**: they fire exactly when the counterparty can no longer pay (AIG).
- **Treating recovery as a constant 40%**: recoveries fall in recessions, when defaults cluster.

## Worked Example
**Hazard rates from spreads (Example 24.1).** Spreads of 150, 180 and 195bp for 1, 2 and 3 years. R = 40%.
- Average hazard rates: 1.5%/0.6 = 2.5%, then 3.0% and 3.25%.
- Year-2 hazard rate: 2 × 3.0 − 2.5 = **3.5%**.
- Year-3 hazard rate: 3 × 3.25 − 2 × 3.0 = **3.75%**.

**Merton model (Example 24.3).** E₀ = $3m, σ_E = 80%, D = $10m due in 1 year, r = 5%.
- Solving gives V₀ = 12.40 and σ_V = 21.23%.
- d₂ = 1.1408, so the **default probability = N(−d₂) = 12.7%**.
- Market value of the debt = 12.40 − 3 = 9.40. The PV of the promised payment is 9.51.
- The expected loss is therefore ≈ **1.2%**.

## Key Takeaways
1. λ̄ ≈ s/(1 − R) links spreads to default intensity.
2. Risk-neutral default probabilities exceed real-world ones. Use each for its own purpose.
3. In Merton, equity is a call on the assets and the default probability is N(−d₂). The model is good for ranking.
4. CVA = Σ qᵢ(1 − R)EEᵢDFᵢ, computed on netting sets with collateral.
5. Default correlation (Gaussian copula, Vasicek WCDR) drives credit VaR and capital.

## Connects To
- **Ch 9**: XVAs.
- **Ch 25**: CDS, CDOs and copula tranche pricing.
- **Ch 11**: equity as a call (capital structure).
- **Ch 22**: credit VaR vs market VaR.
