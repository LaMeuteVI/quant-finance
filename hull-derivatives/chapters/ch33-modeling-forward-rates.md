# Chapter 33: Modeling Forward Rates

## Core Idea
HJM and BGM/LMM model the whole forward curve directly, with complete freedom in the choice of volatility structure.
- **HJM**: once volatilities are chosen, no-arbitrage fixes the drift.
- **LMM/BGM**: works with the discrete forward rates that caps are written on, so it calibrates easily to caps and swaptions.

Neither model is Markov in general, so both are typically run by Monte Carlo. Agency MBS (prepayment-driven and path dependent) are a natural application.

## Frameworks Introduced
- **HJM**: `dF(t,T) = m(t,T)dt + s(t,T)dz`.
  - No-arbitrage requires `m(t,T) = s(t,T)∫_t^T s(t,τ)dτ`. The drift is fully determined by the volatilities.
  - Multi-factor: sum over the factors.
  - Ho–Lee (s constant) and Hull–White (s = σe^{−a(T−t)}) are special cases.
  - In general HJM is **non-Markov** (trees don't recombine).
- **LMM / BGM**:
  - The forward rate F_k(t) covers [t_k, t_{k+1}].
  - Under the measure of the zero-coupon bond maturing at t_{k+1}, F_k is a driftless lognormal martingale, which recovers Black's caplet formula.
  - Under the **rolling forward (spot LIBOR) measure**, the drift is `dF_k/F_k = Σ_{i=m(t)}^{k} [δ_iF_iζ_iζ_k/(1 + δ_iF_i)]dt + ζ_k dz`.
- **Calibration**:
  - The caplet volatilities σ_k relate to the instantaneous volatilities: σ_k²t_k = ∫₀^{t_k} ζ_k(t)²dt.
  - A common structure is stationary: ζ_k(t) = Λ_{k−m(t)}.
  - Swaption volatilities are approximated with Rebonato's formula, using the correlations between forwards.
- **Multi-factor LMM**: correlation between forwards, typically via PCA. This is needed for spread options and Bermudans.
- **Ratchet caps, sticky caps, flexi caps**: path-dependent caps that are natural for LMM Monte Carlo.
- **Bermudan swaptions in LMM**: Longstaff–Schwartz regression on the simulated paths.
- **Agency MBS**:
  - Pass-throughs are guaranteed against default (GNMA, FNMA, FHLMC), but prepayment risk remains.
  - Prepayments depend on rates (refinancing incentive), seasoning, burnout and seasonality.
  - **CMOs** split the prepayment risk into tranches.
  - **IO/PO strips**: the IO loses value when rates fall (faster prepayment); the PO gains.
  - Value MBS by Monte Carlo with a prepayment model. **Option-adjusted spread (OAS)** is the spread over the model curve that equates model and market prices.

## Key Concepts
- **Instantaneous forward rate F(t,T)** vs **discrete forward rate F_k(t)**.
- **Spot LIBOR (rolling) measure**: the numeraire is rolled over at each reset.
- **Drift approximation (predictor–corrector)** in LMM Monte Carlo.
- **Negative convexity** of MBS: prices rise less when rates fall, because borrowers refinance.

## Mental Models
- **Choose the volatility, and the drift follows.** In HJM-type models, no-arbitrage leaves no freedom in the drift.
- **LMM speaks the market's language**: its inputs are the caplet volatilities traders quote.
- **An MBS is a bond short a (messy) prepayment option.** Rates down → prepayments up → the duration shortens.

## Anti-patterns
- **Pricing Bermudans with a single-factor LMM**: it underprices the switch option because forward rates are perfectly correlated.
- **Ignoring burnout in prepayment models**: pools that have already refinanced are less sensitive afterward.
- **Using OAS as an arbitrage signal without questioning the prepayment model behind it**.

## Worked Example
**Caplet volatility → instantaneous volatility (Example 33.1).** Equal accrual periods. Black spot caplet volatilities are 24%, 22% and 20%. Use a stationary structure Λ₀, Λ₁, Λ₂.
- Λ₀ = **24%**.
- Λ₀² + Λ₁² = 2 × 0.22², so Λ₁ = **19.80%**.
- Λ₀² + Λ₁² + Λ₂² = 3 × 0.20², so Λ₂ = **15.23%**.

**Humped caplet volatilities (Example 33.2).** The caplet volatilities σ_k for years 1–10 run 15.50, 18.25, 17.91, … 15.54%. The implied instantaneous volatilities Λ_{k−1} run 15.50, **20.64**, 17.21, … 13.40%.
- The hump in Λ is more pronounced than the hump in σ, because σ_k is a root-mean-square average of the Λ values.

## Key Takeaways
1. HJM: the drift is determined by the volatilities. Ho–Lee and Hull–White are special cases.
2. LMM: discrete forwards are lognormal martingales under their own forward measure. Caplets reduce to Black.
3. Calibrate the instantaneous volatility Λ from caplet volatilities, and correlations from swaptions or PCA.
4. Both models are usually run by Monte Carlo; Bermudans use Longstaff–Schwartz.
5. Agency MBS need prepayment models and OAS. IO/PO strips separate the prepayment risk.

## Connects To
- **Ch 28**: forward measures.
- **Ch 29**: Black caplet and swaption formulas.
- **Ch 32**: short-rate models as special cases.
- **Ch 27**: Longstaff–Schwartz.
- **Ch 8**: securitization (non-agency).
