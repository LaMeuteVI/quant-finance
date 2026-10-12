# Chapter 4: Capital Market Expectations, Part 2: Forecasting Asset Class Returns
> **Source**: CFA Program Curriculum 2023, Level III, Reading 4 · Portfolio Management (Asset Allocation) | Christopher D. Piros, PhD, CFA

## Core Idea
Expected returns are built asset class by asset class with three families of formal tools (statistical, discounted cash flow, risk premium), then made mutually consistent through an equilibrium model and a clean covariance matrix. Sample means are too noisy to use directly, so the craft is to anchor on fundamentals (yield, growth, cap rate, risk premium building blocks), add a modest view, and treat currencies, illiquid assets and volatility with explicit corrections (overshooting, de-smoothing, shrinkage, ARCH).

## Learning Outcomes Covered
- discuss approaches (DCF, building blocks, equilibrium) for setting fixed-income return expectations
- discuss emerging market (EM) bond risks (ability vs willingness to pay) and country risk analysis
- discuss approaches for equity return expectations (historical, Grinold-Kroner DCF, risk premium, Singer-Terhaar)
- discuss EM equity risks
- explain how economic and competitive factors drive real estate expectations (cap rates, cycles, liquidity)
- discuss major approaches to forecasting exchange rates (PPP, current account, capital flows, portfolio balance)
- discuss methods of forecasting volatility (sample VCV, factor, shrinkage, de-smoothing, ARCH)
- recommend and justify changes to the weights of a global portfolio from macro trends

## Frameworks Introduced
- **Three formal forecasting toolkits**: statistical (sample statistics, shrinkage, time series), discounted cash flow (price implies required return), risk premium (equilibrium model such as CAPM, factor model, building blocks). Surveys and judgment complement them.
  - When to use: pick the tool by what information the forecast should be conditioned on; use surveys to measure consensus, never as the sole input.
  - How: DCF for assets with identifiable cash flows (bonds, equities, real estate), risk premium for cross-asset consistency, statistics only for VCV or as a prior.
  - Why it works / failure mode: all rely on mean reversion to fundamentals over long horizons; statistical methods inherit sampling error (sample mean is very imprecise even over 118 years).
- **Fixed-income DCF return projection (yield + horizon effects)**: realized return ≈ initial YTM unless the horizon differs from Macaulay duration.
  - When to use: projecting bond or bond portfolio returns for the strategic horizon under a rate view.
  - How: (1) capital gain/loss ≈ −ModDur × ΔY; (2) reinvestment gain ≈ ΔY × time reinvested (timing matters, so split the horizon into subperiods); (3) annual return ≈ YTM + (price effect + reinvestment effect)/horizon.
  - Why it works / failure mode: price and reinvestment effects offset when horizon = Macaulay duration (exact only for a flat curve and an immediate parallel shift). Horizon < duration: capital effect dominates, so rising rates lower return. Horizon > duration: reinvestment dominates, so rising rates raise return.
- **Fixed-income building blocks**: `E(R) = r_f (short default-free) + term premium + credit premium + liquidity premium`.
  - When to use: expected returns for government, corporate, agency and structured bond classes and as inputs to riskier classes.
  - How: observe r_f (T-bill or futures-implied path or Taylor-rule path); term premium ≈ proportional to duration, estimate from ex ante real yield, Cochrane-Piazzesi factor, Kim-Wright, curve slope, long-bond supply; credit premium = spread minus expected default loss (about half of a 1.53% average US spread was loss in a 150-year study); liquidity premium baseline = sovereign minus top agency spread, then adjust for age, size, issuer, complexity and quality.
  - Why it works / failure mode: only r_f is observable; spreads mix premium and expected loss so premiums cannot be read off the curve. Credit premium tends to be richest at the short end (event risk, illiquidity), hence the credit barbell.
- **Grinold-Kroner model**: `E(R_e) ≈ D/P + (%ΔE − %ΔS) + %Δ(P/E)`; equivalently income return (D/P − %ΔS) + nominal earnings growth (%ΔE) + repricing (%ΔP/E).
  - When to use: forecasting equity market returns over finite horizons with explicit buybacks and valuation reversion.
  - How: take D/P and net repurchases from current data; earnings growth = nominal GDP growth (+ small trend wedge); %ΔP/E from mean reversion of a cyclically adjusted multiple (CAPE = price / 10-year average real earnings), converted into an annual rate consistent with the horizon.
  - Why it works / failure mode: GDP growth is far more stable than P/E or earnings/GDP, so anchoring there beats extrapolating returns. Failure mode: extending finite-horizon growth rates to infinity. The only consistent very-long-run values are %ΔE = nominal GDP growth, %ΔS = 0, %ΔP/E = 0.
- **Singer-Terhaar (partially integrated) risk premium model**: `RP_i = φ·RP_i^G + (1−φ)·RP_i^S`, with `RP_i^G = ρ_{i,GM}·σ_i·SR_GM` and `RP_i^S = σ_i·SR_i`.
  - When to use: expected risk premium for any asset class when markets are neither fully integrated nor fully segmented (EM, real estate, commodities).
  - How: (1) get global Sharpe ratio SR_GM, asset σ, correlation with global market; (2) fully integrated premium via CAPM; (3) fully segmented premium treats the asset as its own market (β = ρ = 1); (4) weight by degree of integration φ; (5) add r_f and an illiquidity premium.
  - Why it works / failure mode: nests both CAPM extremes. Typical φ: developed markets 0.75-0.90, EM and real estate 0.50-0.75, liquid-futures commodities toward the high end. Failure mode: assumes perfectly liquid markets, so add liquidity premiums. Pragmatic default: set SR_i = SR_GM.
- **Real estate Gordon/Grinold-style model**: `E(R_re) = cap rate + NOI growth − %ΔCap rate`.
  - When to use: expected return on direct, unlevered, income-producing property.
  - How: cap rate = NOI / value (analog of E/P); long-run NOI growth ≈ GDP growth and no cap-rate change; finite horizon includes expected cap-rate drift (falling cap rate adds return).
  - Failure mode: appraisal-based data is smoothed, so de-smooth before using any volatility or correlation.
- **Exchange-rate forecasting, three complementary lenses**: (1) goods, trade and current account (PPP, competitiveness, sustainability); (2) capital flows (building-block rate differential, overshooting, UIP and carry, hot money); (3) portfolio balance (relative size and composition of currency portfolios).
  - When to use: directional currency view with modest expected appreciation numbers; none stands alone.
  - How: check current-account size and source (<2% of GDP rarely matters; investment-led deficits are sustainable, consumption/fiscal-led deficits are not), then capital flows and whether the currency has already overshot, then long-run PPP as the anchor.
- **Covariance estimation ladder**: sample VCV, then factor-model VCV, then shrinkage of the two (target = factor VCV), then de-smoothing for private assets, then ARCH for time variation.
  - How: see Formulas. Rule of thumb: observations at least 10 times the number of assets for the sample matrix to be reliable.
- **Seven-step quantification process** for macro views (Section 9.2): (1) estimate VCV; (2) Singer-Terhaar equilibrium returns; (3) Grinold-Kroner for equities; (4) building blocks for bonds; (5) directional currency views vs base currency; (6) add currency component to equity and bond returns; (7) combine equilibrium returns with views via Black-Litterman.

## Key Concepts
- **Term premium**: extra expected return for duration risk; positive, roughly proportional to duration, time-varying; cannot be derived directly from the yield curve.
- **Credit premium**: expected return above expected default loss for bearing default risk; embedded in spreads but not equal to them.
- **Liquidity premium**: compensation for illiquidity; baseline = sovereign vs highest-quality agency spread.
- **Downgrade bias**: for AAA/AA bonds, spread is driven by the asymmetry that downgrades are likelier and move spreads more than upgrades.
- **Credit barbell**: concentrate credit risk at short maturities (richest credit premium) and take duration via long governments.
- **Ability to pay vs willingness to pay**: economic vs political/legal split of EM debt risk; sovereign immunity makes willingness hard to enforce.
- **Equity-versus-bills vs equity-versus-bonds premium**: differ by the term premium; geometric versions are additive, arithmetic ones are not.
- **CAPE (cyclically adjusted P/E)**: price over 10-year average inflation-adjusted earnings.
- **Degree of integration (φ)**: weight on the globally integrated CAPM premium in Singer-Terhaar.
- **Appraisal smoothing**: reported private-asset returns are weighted averages of current and past true returns; mean unbiased, volatility and correlations distorted.
- **Overshooting (Dornbusch)**: currency jumps beyond long-run value on better risk-adjusted prospects, then retraces; hence higher-yielding currencies sometimes appreciate and sometimes depreciate.
- **Uncovered interest rate parity (UIP)**: expected FX change = nominal rate differential; empirically fails (carry trades earn about 4.31%/yr vs USD, 1976-2009).
- **Hot money flows**: rapid short-term capital moving on rate differentials; erodes monetary independence and invites crises, especially in EM.
- **Volatility clustering / ARCH**: variance depends on its past level and recent squared shocks.
- **Shrinkage estimator**: weighted average of sample and target estimates; biased but lower mean-squared error (MSE = variance + bias²).

## Formulas & Reference Tables
- Yield-based return (annual, approx.): `R ≈ YTM + [−ModDur·ΔY + reinvestment gain]/H`; Macaulay duration = ModDur × (1 + YTM).
- Building blocks: `E(R_bond) = r_f + Term + Credit + Liquidity`.
- Grinold-Kroner: `E(R_e) ≈ D/P + %ΔE − %ΔS + %Δ(P/E)`. Long run: `D/P + nominal GDP growth`.
- P/E repricing rate for a finite horizon: `g = (P/E_target / P/E_now)^(1/H) − 1` (16→20: 4.56% over 5y, 2.26% over 10y, 0.75% over 30y).
- Singer-Terhaar: `RP_i^G = β_{i,GM}·RP_GM = ρ_{i,GM}·σ_i·(RP_GM/σ_GM)`; `RP_i^S = σ_i·SR_i`; `RP_i = φ·RP_i^G + (1−φ)·RP_i^S`; `E(R_i) = r_f + RP_i (+ liquidity premium)`.
- Real estate: `E(R_re) = Cap rate + NOI growth` (long run); `= Cap rate + NOI growth − %ΔCap rate` (finite horizon; %Δ is relative change, e.g. 5.7%→5.5% is −3.5%).
- Illiquidity premium (Ang et al.): about 0.6% (quarterly liquidity), 0.9% (annual), 2% / 4% / 6% (trade every 2 / 5 / 10 years); 2-4% reasonable for commercial real estate.
- FX building blocks: `E(%ΔS_{d/f}) = (r_d − r_f) + (Term_d − Term_f) + (Credit_d − Credit_f) + (Equity_d − Equity_f) + (Liq_d − Liq_f)` (S in domestic per foreign; positive = domestic depreciation).
- Relative PPP: `E(%ΔS) = π_d − π_f` (expected real exchange rate change = 0).
- K-factor model: `r_i = α_i + Σ_k β_ik F_k + ε_i`; `σ_i² = ΣΣ β_im β_in ρ_mn + ν_i²`; `σ_ij = ΣΣ β_im β_jn ρ_mn`. Parameters: N(N−1)/2 covariances reduce to N·K betas + K(K+1)/2 factor elements (N=100, K=5: 4,950 to 515).
- Shrinkage: `Σ_shrunk = w·Σ_target + (1−w)·Σ_sample` (same w on every element).
- De-smoothing: `R_t = (1−λ)·r_t + λ·R_{t−1}`; `var(r) = [(1+λ)/(1−λ)]·var(R)`; λ = 0.8 gives 9× variance, 3× volatility.
- ARCH(1)-type (as in reading): `σ_t² = γ + α·σ²_{t−1} + β·η²_{t−1}`, α, β, γ ≥ 0, α+β < 1; unconditional variance `γ/(1 − α − β)`.
- EM sovereign warning thresholds (suggestive only): fiscal deficit persistently >4% GDP; debt >70-80% GDP; real growth <4%; current account deficit >4% GDP; foreign debt >50% GDP or >200% of current account receipts; FX reserves <100% of short-term debt (>200% ample).

| Determinant of term premium (Ilmanen) | Direction |
|---|---|
| Level-dependent inflation uncertainty | higher inflation, higher premium |
| Recession hedge ability | demand-driven cycles: low premium; supply-driven: high premium |
| Supply/demand of long bonds | more long supply, higher premium |
| Cyclical | steep near trough, flat/inverted near peak |

| Predictors of future excess bond returns (1962-2009 correlations, 1 yr) | Value |
|---|---|
| Ex ante real yield | 0.48 (0.69 at 5 yr) |
| Cochrane-Piazzesi factor | 0.44 |
| Kim-Wright premium | 0.43 |
| Curve slope (10y−3m) | 0.34 (weak at 5 yr, 0.06) |
| Share of debt >10y | 0.28 (0.66 at 5 yr) |
| Corporate profit/GDP | −0.25 |

IG corporate excess return predictors (1990-2009, 1 yr): option-adjusted spread 0.46, VIX 0.39, curve slope 0.27.

Real estate cap rates, March 2018 (US): hotels 7.2, health care 6.6 (skilled nursing 9.5, medical office 5.7), malls 5.6 (low productivity 8.8, high 5.0), industrial 5.4, office 5.2 (gateway 4.7, secondary 6.6), apartments 4.8.

## Mental Models
- Think of expected return as a **supply side** (Grinold-Kroner: what the economy produces) cross-checked against a **demand side** (risk premiums: what investors require).
- Use **GDP as the anchor** and treat P/E and earnings/GDP as noisy mean-reverting ratios that mostly cancel over time.
- A fixed-term lease is a **corporate bond issued by the tenant secured on the property**; the landlord also holds an equity-like residual. So real estate premium sits between corporate bonds and equities.
- Read real-estate and private-equity volatility as **understated by a smoothing factor**; always de-smooth before optimizing, otherwise the optimizer overweights them.
- Treat currency forecasts as **three phases**: capital rush (appreciation), consolidation, retracement. Do not extrapolate the rate differential.
- **Shrinkage as "two estimates beat one"**: unbiased-but-noisy sample plus biased-but-stable target; the better the prior, the larger the gain.
- Prefer **modest FX views** (small expected appreciation/depreciation) because the evidence is weak; hedge when carry or hedging cost makes the asset unattractive in local terms.

## Worked Example
**Singer-Terhaar (German shares/bonds, r_f = 3.0%, global SR = 0.30, φ = 0.85).**
Shares: σ = 17%, ρ = 0.70, segmented SR = 0.35. Integrated RP = 0.70 × 17 × 0.30 = 3.57%; segmented = 17 × 0.35 = 5.95%; blend = 0.85 × 3.57 + 0.15 × 5.95 = 3.93%; E(R) = 6.93%.
Bonds: σ = 7%, ρ = 0.50, segmented SR = 0.25. Integrated 1.05%, segmented 1.75%, blend 1.16%; E(R) = 4.16%.
Interpretation: shares earn about 2.8 pts over bonds; the segmented component pulls both up because local Sharpe ratios exceed or equal the global one. Raising φ lowers the required return when the segmented premium is higher (integration lowers required returns and is a rationale to overweight markets expected to integrate).

**Grinold-Kroner plus horizon check (Canada).** D/P = 2.25%, net buyback 1% (%ΔS = −1%), earnings growth 6% (GDP 5% + 1 pt), P/E drift +0.25%/yr. E(R) = 2.25 + [6 − (−1)] + 0.25 = 9.5%. Long run (earnings = GDP, no buyback, no repricing) = 2.25 + 5 = 7.25%. Over 10 years the assumptions imply earnings/GDP +10.5%, shares −9.6%, P/E +2.5%: plausible for 10 years, not for perpetuity.

**Bond horizon (YTM 3.25%, ModDur 4.84, yields +200 bp linearly over 2 years).** Capital loss ≈ 4.84 × 2% = 9.68%. Reinvestment boosts: +1.0% (2y), +6.0% more (3 further years), +4.0% (2 more). Annualized: 2y ≈ −1.09%, 5y ≈ 2.71%, 7y ≈ 3.44%. Interpretation: loss dominates short horizons, reinvestment dominates long ones; because the rise is gradual, the breakeven horizon exceeds the 5.0 Macaulay duration.

Other checks: building blocks (3.50 + 0.50 + 0.90 + 0.15) = 5.05% for BBB corporates; real estate (5.7% cap, 2.5% nominal NOI growth, cap falling to 5.5% = −3.5%) = 5.7 + 2.5 + 3.5 ≈ 11.7%; FX (domestic +1% rate, −0.25% term, +0.5% credit) = +1.25% expected domestic depreciation; ARCH (γ = 0.000002, α = 0.9, β = 0.08, σ²_{t−1} = 0.0004, η = 3%) gives σ² = 0.000434, σ = 2.083% vs long-run 1%; covariance shrinkage example: sample σ = 20%/10%, ρ = 0.75; single-factor target (β 1.2 / 0.8, factor var 0.0225, specific 0.0100 / 0.0050); w = 0.4 gives variances 0.04096 and 0.01376 and covariance 0.01764 (ρ = 0.743).

## Anti-patterns
- **Using historical country mean returns to differentiate markets**: all 21 countries' means (5.0%-9.4% real) lie inside each other's confidence intervals; differences are statistical noise.
- **Equating YTM with expected return over any horizon**: only holds when horizon ≈ Macaulay duration and curve is flat.
- **Reading term or credit premium straight off the curve or spread**: spread = premium + expected loss; term premium is not forward minus expected spot.
- **Applying a 10-year P/E repricing rate (2.26%) in a perpetuity**: implies an ever-rising multiple.
- **Feeding smoothed real estate/PE data into the optimizer**: understates risk and overstates diversification.
- **Treating a sample VCV with too few observations as truth**: if assets > observations some portfolios look riskless; need ~10 observations per asset.
- **Extrapolating the interest-rate differential into FX forecasts (UIP)**: carry earns positive returns on average; overshooting reverses direction.
- **Ignoring liquidity in equilibrium models**: they assume perfectly liquid markets; private assets need an explicit premium.

## Exam Focus & Traps
- Direction of FX building-block equation: higher domestic risk-adjusted return implies domestic currency expected to **depreciate** (after the initial jump appreciation).
- Singer-Terhaar: higher φ weights the integrated premium; EM equity example shows net effect needs both components recomputed (4.79% to 4.19%, a 60 bp fall).
- Cap rate formula includes **%Δ cap rate with a minus sign**; falling cap rate adds return. Long-run version omits it.
- De-smoothing: true variance is **greater** than observed; REITs act like stocks short run, like real estate at multi-year horizons (so REITs are a poor 1-year equity diversifier).
- Duration-horizon rule: horizon = Macaulay duration (not modified) for immunity of YTM.
- Credit premium is larger at short maturities; term premium rises with maturity and duration; a steep curve signals both high term and high credit premium.
- EM: carry out the checklist (fiscal deficit, debt/GDP, current account, reserves) and separate ability from willingness; EM equity adds expropriation risk by insiders and the state, weak accounting and governance; country effects dominate industry effects.
- Equity-vs-bonds premium excludes the term premium; equity-vs-bills includes it.
- ARCH: the sign of the shock does not matter (squared); (α+β) controls persistence.
- ⚠ Reading note: in Section 3 the 10-year Treasury/curve indicators come from US 1962-2009 data (Ilmanen); do not generalize correlations as universal constants.

## Key Takeaways
1. Anchor equity forecasts on D/P + net repurchases + nominal GDP growth, and add repricing only when you can justify a multi-year mean reversion.
2. For bonds, start from YTM, then adjust for horizon vs duration, then use building blocks (r_f, term, credit, liquidity) tied to curve slope and spreads.
3. Use Singer-Terhaar with φ around 0.75-0.90 for developed and 0.50-0.75 for EM and real estate, then add an explicit illiquidity premium.
4. Always de-smooth private-asset volatility (λ = 0.8 triples the standard deviation) before any allocation optimization.
5. Estimate the VCV by shrinking the sample matrix toward a factor-based target, and keep observations at least 10 times the number of assets.
6. For currencies, combine PPP (long run), current-account sustainability (source and size) and capital flows (overshooting); express views with modest magnitudes.
7. Late-cycle/trough macro rules: near the trough, raise equities, shorten duration with a barbell and add credit; near the peak do the opposite; shift away from markets with rising current account deficits.
8. Finish with a checklist: trend growth, integration, cycle phase, policy, current account, currencies, and "what is already priced in?".

## Connects To
- **ch03**: framework, macro analysis and pitfalls that feed these asset class forecasts.
- **ch05**: pricing-kernel view of investment markets (real rate, inflation, term, credit, equity premia by cycle phase), the macro layer behind building blocks.
- **ch06**: expected returns, VCV and risk premiums feed strategic asset allocation choices.
- **ch07**: Black-Litterman and optimization consume the equilibrium returns and VCV built here.
- **`ilmanen-yield-curve` ch03-ch04**: term premium, bond risk premium and forecasting bond returns.
- **`cfa-economics` ch04, ch06**: business cycles, trade and capital flows, exchange rates behind FX and trend-growth inputs.
- **`cfa-derivatives` ch07**: currency hedging cost and carry when overshooting makes assets unattractive after hedging.
