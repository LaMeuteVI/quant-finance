---
name: cfa-derivatives
description: "CFA Program derivatives curriculum across three levels: Level I (2020 R48-R49), Level II (2022 R33-R34), Level III (2023 R8-R10): markets and instruments, no-arbitrage pricing, forward commitment and contingent claim valuation, option strategies, swaps/futures overlays, currency management. Use when pricing or valuing forwards, futures, FRAs, swaps, options, or when asked about put-call parity, binomial model, Black-Scholes-Merton, Black model, Greeks and delta hedging, carry arbitrage, covered call, protective put, collar, straddle, calendar spread, bond futures BPV hedge, cheapest-to-deliver, variance swap, VIX, FX hedging, roll yield, seagull, minimum-variance hedge ratio, or when preparing a CFA derivatives quiz."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# CFA Derivatives (Levels I, II, III)
**Source**: CFA Program Curriculum Derivatives: L1 2020 R48-R49, L2 2022 R33-R34, L3 2023 R8-R10 | **Domain**: Finance de marché | **Chapters**: 7 | **Generated**: 2026-09-29

## How to Use This Skill
- **Without arguments** — load the core frameworks below
- **With a topic** — ask about `<topic>`; I read the relevant chapter before answering
- **With a chapter** — ask for `ch05`
- **Browse** — "what chapters do you have?"
- **Exam mode** — ask for a quiz on a chapter; I build it from its Worked Example and Exam Focus sections.

When a topic is not covered in Core Frameworks below, I read the relevant chapter file before answering.

---

## Core Frameworks & Mental Models

**Pricing logic**
- **No-arbitrage replication** (ch01, ch02, ch04): build a riskless hedge, force it to earn r, read the price. Never discount at r + λ; risk aversion drops out. Arbitrage = zero risk AND zero capital, a relative ruler, not a forecast.
- **Carry model** (ch02, ch03): `F₀ = FV(S₀ + CC − CB) = (S₀ − γ + θ)(1+r)^T`. Benefits lower F₀, costs raise it. Too high: sell forward, borrow, buy spot (carry); too low: reverse carry.
- **Price vs value** (ch02, ch03): price is a fixed term, value starts at 0. `V_t = PV(F_t − F₀) = S_t − PV(carry) − F₀/(1+r)^(T−t)`; at expiry `S_T − F₀`. Futures value resets to zero at each settlement.
- **Swaps = strips of off-market forwards / pairs of bonds** (ch02, ch03): `s = (1 − DF_n)/ΣDF`; value of a payer `N(s_t − s₀)ΣDF_remaining`. Currency swap: tie notionals by S₀, value both legs with current curves and spot. Equity swap: equity leg resets to notional like a floater.
- **FRA** (ch03): `FRA₀ = {[1 + L_Y t_Y]/[1 + L_X t_X] − 1}/t_m`; long pays fixed, profits when rates rise; settlement discounted by 1 + D·t_m.
- **Bond futures** (ch03, ch06): `F₀ = FV(B₀ + AI₀) − AI_T − FV(coupons)`, quoted `Q₀ = F₀/CF`; CTD maximizes invoice minus dirty cost (long duration/low coupon when yields > 6%).

**Option valuation**
- **Put-call parity** (ch02, ch05): `S + p = c + PV(X)`; with forward `PV(F) + p = c + PV(X)`. Any three build the fourth; protective put = fiduciary call.
- **Binomial** (ch02, ch04): `π = (1+r−d)/(u−d)`, `h = Δoption/ΔS`, roll back node by node; American = max(continuation, exercise). Calls on non-payers are never exercised early; deep ITM puts may be.
- **BSM and Black** (ch04): call = `S e^(−γT)N(d1) − X e^(−rT)N(d2)` (leveraged stock). Black for futures/FRA/swap rates: caplets discount to payment date, swaptions use AP·PVA, T is option expiry.
- **Greeks and delta hedging** (ch04, ch05): `N_H = −Δ_P/Δ_H`; gamma and vega first with options, delta last with stock; theta is the rent on gamma; implied vol is the quoting unit and the smile/skew shows BSM fails.

**Strategies**
- **State direction AND volatility view** (ch05): matrix of IV decrease/unchanged/increase against bearish/neutral/bullish (write calls / straddle / puts; collar / calendar / risk reversal; buy puts / straddle / calls).
- **Strategy payoffs** (ch05): covered call BE `S₀ − c₀`; protective put max loss `S₀ − X + p₀`; zero-cost collar c₀ = p₀; long straddle BE `X ± (c₀ + p₀)`; calendars are long vega, short gamma. Equal delta does not mean equal risk.
- **Exposure-matching equation** (ch06): `Exposure_P + N × Exposure_unit = Exposure_T`. Swap: `N_S = (MDUR_T − MDUR_P)/MDUR_S × MV_P`; bond futures `BPVHR = (BPV_T − BPV_P)/BPV_CTD × CF`; equity `N_f = (β_T − β_S)/β_f × S/F`.
- **Volatility instruments** (ch06): variance swap settlement `N_vega(σ² − K²)/(2K)` is convex; VIX futures roll in contango; fed funds probability from `100 − price`.

**Currency**
- **Return/risk decomposition** (ch07): `R_DC = (1+R_FC)(1+R_FX) − 1`; R_FX on DC/FC quote; FX adds variance unless ρ is negative.
- **Hedging policy** (ch07): optimize on hedged returns, then relax; foreign bonds ~100% hedged, equities partial, 50% for regret. Passive / discretionary / active / overlay spectrum.
- **Forwards, rolls, options** (ch07): selling base uses bid; MTM by offsetting same-date forward, discount at cash-flow currency; mismatched FX swap resizes. Roll yield positive when selling base at premium. Cheaper option hedges (OTM, collar, put spread, seagull, barrier) each give up protection or upside.
- **Active styles** (ch07): fundamentals (PPP anchor), technicals, carry (negative skew), volatility; minimum-variance hedge `h* = ρσ(R_DC)/σ(ΔS)`.

---

## Chapter Index
| # | Title | Level · Reading | Key Frameworks |
|---|---|---|---|
| [ch01](chapters/ch01-l1-derivative-markets-and-instruments.md) | Derivative Markets and Instruments | L1 · R48 | Forward commitments vs contingent claims, margin mechanics, arbitrage |
| [ch02](chapters/ch02-l1-basics-of-derivative-pricing-and-valuation.md) | Basics of Derivative Pricing and Valuation | L1 · R49 | Replication, forward price/value, parity, one-period binomial |
| [ch03](chapters/ch03-l2-pricing-valuation-forward-commitments.md) | Pricing and Valuation of Forward Commitments | L2 · R33 | Carry arbitrage, FRA, bond futures, interest/currency/equity swaps |
| [ch04](chapters/ch04-l2-valuation-of-contingent-claims.md) | Valuation of Contingent Claims | L2 · R34 | Binomial trees, BSM, Black, caplets/swaptions, Greeks |
| [ch05](chapters/ch05-l3-options-strategies.md) | Options Strategies | L3 · R8 | Covered call, protective put, spreads, straddle, collar, calendar, skew |
| [ch06](chapters/ch06-l3-swaps-forwards-futures-strategies.md) | Swaps, Forwards, and Futures Strategies | L3 · R9 | Duration/beta overlays, BPVHR, variance swaps, VIX |
| [ch07](chapters/ch07-l3-currency-management.md) | Currency Management: An Introduction | L3 · R10 | Return decomposition, hedge policy, FX swaps, option structures, carry |

## Topic Index
- **Accrued interest / clean-dirty** → ch03
- **American vs European options, early exercise** → ch02, ch04
- **Arbitrage, law of one price** → ch01, ch02, ch04
- **Basis (futures, bond), basis risk** → ch03, ch06, ch07
- **Beta adjustment, cash equitization** → ch06
- **Binomial model, risk-neutral probability** → ch02, ch04
- **Black model, caplets, floorlets** → ch04
- **Black-Scholes-Merton** → ch04
- **Bull / bear spreads** → ch05
- **Calendar spread** → ch05
- **Carry arbitrage, cost of carry** → ch02, ch03
- **Carry trade, forward rate bias, UIP** → ch07
- **Cheapest-to-deliver, conversion factor** → ch03, ch06
- **Collar, zero-cost collar** → ch05, ch07
- **Contingent claims vs forward commitments** → ch01
- **Covered call, protective put** → ch05
- **Credit derivatives (CDS, CLN, TRS)** → ch01
- **Cross-currency basis swap, covered interest parity** → ch06, ch07
- **Currency overlay, passive/active hedging** → ch07
- **Currency swap** → ch02, ch03, ch06
- **Delta hedging, gamma risk** → ch04, ch05
- **Dividends, escrow method** → ch03, ch04
- **Equity swap, total return swap** → ch03, ch06
- **Exchange-traded vs OTC** → ch01
- **Fed funds futures probability** → ch06
- **Forward points, FX forward MTM, roll** → ch07
- **FRA** → ch02, ch03, ch06
- **Futures vs forwards price difference** → ch02, ch03
- **Greeks (delta, gamma, vega, theta, rho)** → ch04, ch05
- **Hedge ratio (binomial, BPV, minimum-variance)** → ch02, ch04, ch06, ch07
- **Implied volatility, smile, skew, term structure** → ch04, ch05
- **Interest rate swap** → ch02, ch03, ch06
- **Margin (initial, maintenance, MTM)** → ch01
- **Minimum-variance hedge** → ch07
- **Option bounds, moneyness, time value** → ch02, ch04
- **Option factors (S, X, r, T, σ)** → ch02
- **Put-call parity, synthetics** → ch02, ch05
- **Return and risk decomposition (FX)** → ch07
- **Risk reversal, seagull, put spread, exotics** → ch05, ch07
- **Roll yield** → ch07
- **Straddle, strangle** → ch05, ch07
- **Swap rate, swap valuation** → ch02, ch03
- **Swaptions, payer/receiver** → ch04
- **Variance swap, VIX futures** → ch05, ch06
- **Volatility trading (FX)** → ch07

## Supporting Files
- [glossary.md](glossary.md) — key terms with definitions
- [patterns.md](patterns.md) — techniques, recipes and procedures
- [cheatsheet.md](cheatsheet.md) — decision rules, thresholds, exam traps

---

## Related Skills
- `hull-derivatives` — deeper theory: continuous-time models, exotics, day-count detail, Greeks hedging in practice
- `passarelli-option-greeks` — trader's view of Greeks, spreads, volatility trading
- `tuckman-fixed-income` — bond futures, CTD, swaps and curve construction in depth
- `cfa-fixed-income` — ABS, CDS, embedded options, duration strategies using these instruments
- `cfa-economics` — FX quotes, parity conditions (CIP, UIP, PPP) behind ch07
- `cfa-asset-allocation-cme` — rebalancing and allocation policy that overlays implement
- `cfa-level1-curriculum` — personal L1 revision notes on the same reading

## Scope & Limits
Covers the CFA derivatives readings only: L1 (2020 curriculum), L2 (2022, errata applied) and L3 (2023). Check current learning outcome statements, as later curricula revise readings. Source corrections found in the readings are flagged in chapters as Correction or Errata. Exotic and credit derivative modeling, commodity derivatives and structured products are only touched here; see the related skills.
