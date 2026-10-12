# Chapter 9: Valuation and Analysis of Bonds with Embedded Options
> **Source**: CFA Program Curriculum 2022, Level II, Reading 30 · Fixed Income | Leslie Abreo, Ioannis Georgiou, CFA, Andrew Kalotay, PhD (binomial trees revised by Donald J. Smith). L2 errata for Reading 30 applied.

## Core Idea
A bond with an embedded option is the sum of its parts: **straight bond ± option**. The option value depends on interest-rate volatility, so you value it on a calibrated **binomial interest rate tree** (build the tree, test for exercise at every node, backward-induct). That one procedure prices calls, puts, caps, floors and convertibles, and it also produces the OAS, effective duration and effective convexity, which are the risk measures that matter for these bonds. Yield-based measures (modified duration, YTM) are invalid here because the cash flows change when rates change.

## Learning Outcomes Covered
- Describe embedded options (call, put, extension, convertible, estate put, sinking fund provisions).
- Relate callable/putable value to straight bond value and option value.
- Value callable/putable bonds on a tree; explain the effect of volatility, yield curve level and shape.
- Calculate and use the option-adjusted spread (OAS); explain how volatility changes it.
- Calculate and interpret effective duration and effective convexity; compare callable, putable, straight bonds.
- Use one-sided durations and key rate durations.
- Value capped and floored floaters.
- Convertibles: features, conversion value, minimum value, market conversion price/premium, risk-return profile, arbitrage-free valuation.

## Frameworks Introduced
- **Building-block valuation** (arbitrage-free value = sum of parts):
  - `Callable = Straight − Issuer call` (investor is long the bond, short the call).
  - `Putable = Straight + Investor put` (investor is long both).
  - `Capped floater = Straight − Cap`; `Floored floater = Straight + Floor`.
  - `Callable convertible = Straight + Call on stock − Issuer call` (add `+ Investor put` if putable).
  - When to use: to find the option value, value the straight bond and the optioned bond separately and take the difference.
- **Three-step tree valuation of an optioned bond**:
  1. Generate a calibrated binomial tree from the benchmark par curve and a volatility σ (see ch08).
  2. At each node decide exercise: the **issuer calls** if the node value (ex-coupon, before the call) is above the call price; the **investor puts** if it is below the put price. Reset the node value to the exercise price.
  3. Backward induction: `V_t = [ ½(V_{t+1,H} + C) + ½(V_{t+1,L} + C) ] / (1 + i_t)`, using the reset values.
  - Exercise is tested on the ex-coupon value; the coupon paid on the exercise date is added in the step to the node before. Exercise nodes are only those on call/put dates (Bermudan: only scheduled dates).
  - Assumption: holders are risk-neutral and exercise optimally. Real holders may exercise early even when the option is worth more alive.
- **Zero-volatility valuation** (no tree): discount with one-period **forward rates** rather than spots, because you need values at future dates to test exercise. Gives the option's intrinsic value only. Below, option value at 0% vol is 0.407 for the call, 0.283 for the put; both rise with volatility.
- **OAS (option-adjusted spread)**: the constant spread added to **every** one-period forward rate on the tree so that the model value equals the market price.
  - How: guess a spread, revalue with exercise decisions, iterate (price too high means spread too low).
  - Z-spread = OAS at zero volatility (option-free bond: Z-spread = OAS). OAS = Z-spread minus option cost.
  - Use: compare OAS to bonds of similar credit and structure. Lower OAS than peers = rich (avoid); higher = cheap; similar = fair.
  - Failure mode: OAS depends on the volatility assumption. A callable looks cheap at low σ and fairly priced at high σ.
- **Effective duration procedure with a market price** (must be done on a tree):
  1. Solve OAS from the price PV₀ at the chosen σ.
  2. Shift the benchmark par curve down by Δ, rebuild the tree, revalue at the **same OAS** → PV₋.
  3. Shift up by Δ, rebuild, revalue at the same OAS → PV₊.
  4. Apply the formulas below. Credit spread is held constant, only the benchmark moves.
- **One-sided durations**: same formula with only the up or the down shift. Use when the option is near the money, because prices are asymmetric.
- **Key rate durations (partial durations)**: shift one benchmark maturity at a time (2y, 3y, 5y, 10y, 30y…) and apply the effective duration formula. Use them to measure **shaping risk** (steepening/flattening). Key rates of an optioned bond depend on time to exercise as well as maturity.
- **Convertible bond framework**: minimum value = max(conversion value, straight value) (a moving floor); premium metrics; classify as busted / hybrid / equity-like by share price versus conversion price.

## Key Concepts
- **Straight bond**: the underlying option-free bond of the same issuer, maturity, coupon and currency.
- **Call protection period**: initial period when the issuer cannot call; may be months to years.
- **European / Bermudan / American call**: exercisable on one date / on scheduled dates after protection / at any time after the first call date. Putable bonds are European or rarely Bermudan, never American.
- **Make-whole call**: call price set at a narrow spread to a sovereign benchmark, so refunding is uneconomic and investors are more than compensated.
- **Extendible bond**: holder can keep the bond past maturity, possibly at a different coupon. Economically equal to a putable bond: a 3-year putable in Year 2 = a 2-year extendible by one year (same cash flows in every state).
- **Estate put (survivor's option)**: put at par exercisable by heirs; value depends on holder's life expectancy.
- **Sinking fund bond**: amortizing structure with issuer options: call, **acceleration** (e.g. "triple up": sink 3× the mandatory amount at par) and **delivery option** (deliver bonds bought below par instead of cash). Call plus delivery option is an issuer **long straddle**: benefits from rates falling (call, acceleration) and rising (delivery).
- **Effective (option-adjusted) duration**: price sensitivity to a parallel shift of the benchmark curve with credit spread constant.
- **Effective convexity**: sensitivity of effective duration to rates; negative for a callable near the money, always positive for a putable.
- **Conversion price**: par ÷ conversion ratio. **Conversion ratio**: shares received per bond (17.5 per $1,000 gives $57.14).
- **Conversion value (parity value)**: share price × conversion ratio.
- **Market conversion price**: convertible price ÷ conversion ratio, i.e. what you effectively pay per share via the bond.
- **Forced conversion**: issuer calls the bond when the share price is above the conversion price so holders convert (or lose value), removing the coupon and the redemption risk.
- **Busted convertible**: share price far below the conversion price, so the bond trades on straight value (bond-like risk).
- **Hard put / soft put**: issuer must pay cash / issuer chooses payment form (cash, stock, subordinated notes).
- **CoCo / CoCoCo**: contingent convertible (converts or writes down on a regulatory capital breach, higher coupon, deeply subordinated) / a CoCo that is also investor-convertible.

## Formulas & Reference Tables
Parity relations:
- `Callable = Straight − Call`  ⇒  `Call = Straight − Callable`  (Eq. 1)
- `Putable = Straight + Put`  ⇒  `Put = Putable − Straight`  (Eq. 2)
- `Capped floater = Straight − Cap` (Eq. 5); `Floored floater = Straight + Floor` (Eq. 6). An uncapped, unfloored reference-rate floater set in arrears with no spread is worth par, so `Cap = 100 − capped value`, `Floor = floored value − 100`.

Effective duration and convexity (Δ = parallel shift in decimal; PV₋ shifted down, PV₊ shifted up, PV₀ current **full** price):
- `EffDur = (PV₋ − PV₊) / (2 × Δ × PV₀)`  (Eq. 3)
- `EffCon = (PV₋ + PV₊ − 2·PV₀) / (Δ² × PV₀)`  (Eq. 4). Some vendors report this divided by 100.
- One-sided up-duration `= (PV₀ − PV₊)/(Δ × PV₀)`; one-sided down-duration `= (PV₋ − PV₀)/(Δ × PV₀)`. Effective duration is their average.

Convertible metrics:
- `Conversion value = share price × conversion ratio`
- `Minimum value = max(conversion value, straight value)`
- `Market conversion price = convertible price / conversion ratio`
- `Market conversion premium per share = market conversion price − share price`
- `Market conversion premium ratio = premium per share / share price`
- `Premium over straight value = convertible price / straight value − 1` (a flawed downside measure since the floor moves)
- `Conversion premium (at issue) = conversion price / share price at issue − 1` (57.14/40.10 − 1 = 42.5%)
- After a stock split of n:1: conversion price ÷ n, conversion ratio × n.

Effect table (all else equal):

| Driver | Callable | Putable | Option value |
|---|---|---|---|
| Volatility ↑ | Value ↓ | Value ↑ | Call ↑, put ↑ |
| Volatility ↑ | OAS ↓ (at fixed price) | OAS ↑ (put worth more, so a wider spread is needed to hit the same price; mirror image) | |
| Rates ↓ (level) | Rises less than straight (capped) | Rises like straight, put fades | Call ↑, put ↓ |
| Rates ↑ (level) | Behaves like straight | Falls less than straight (floored) | Call ↓, put ↑ |
| Curve flatter/inverted | Call value ↑ | Put value ↓ | More low-rate nodes, more calls |
| Curve steeper | Call value ↓ | Put value ↑ | Forward rates high on the tree |

Duration ranking:

| Instrument | Effective duration |
|---|---|
| Cash | 0 |
| Zero-coupon bond | ≈ maturity |
| Fixed-rate bond | < maturity |
| Callable / putable | ≤ straight bond's duration |
| Floater (MRR flat) | ≈ time to next reset |
| Deep-in-the-money optioned bond | ≈ straight bond maturing on first exercise date |

Convexity: straight bond low positive; **callable turns negative near the money**; putable always positive. Putable has more upside than callable when rates fall, less downside when rates rise.

## Mental Models
- **Short the call / long the put**: a callable investor sells upside to the issuer. Price appreciation is capped at about the call price (negative convexity); a putable investor owns a floor.
- **Volatility is the option's fuel**: option value rises with σ; the callable falls in value, the putable rises, OAS of a callable shrinks. Never compare OAS across different σ.
- **Where does the option bite?**: callable duration shrinks when rates fall (call in the money); putable duration shrinks when rates rise. Deep in the money, the bond behaves like a straight bond maturing at the exercise date. Far out of the money it behaves like the maturity-date straight bond.
- **Key rates move with the exercise date**: a 30-year callable in 10 years with a high coupon has most exposure at the 10-year key rate; a low coupon puts exposure at 30 years. For putables it is the mirror image.
- **Convertible = bond + call on the stock**: busted (bond-like: watch rates and spreads), hybrid (near the conversion price), equity-like (tracks parity, ignores rates and spreads).
- **Upward-sloping curve = fewer calls**: high forward rates in the tree mean the issuer rarely refinances; a par-issued callable on a normal curve is out of the money at zero volatility.

## Worked Example
All numbers recomputed in Python (backward induction plus calibration). Bond: 3-year 4.25% annual, callable or putable at par at Years 1 and 2. Par curve 2.5%, 3.0%, 3.5%; σ = 10%.

1. **Spot and forward curve**: spots 2.500%, 3.008%, 3.524%. Forwards 2.500%, 3.518%, 4.564%. Straight value = 102.114 (spot discounting = tree value: sanity check).
2. **Calibrated tree** (Time 2 / Time 1 / Time 0): Time 0 2.500%. Time 1: 3.1681% (L) and 3.8695% (H), with H/L = e^{0.2}. Time 2: 3.7041%, 4.5242%, 5.5258%.
3. **Zero volatility**: forward-rate discounting gives a value at Year 2 of 99.700 (no call), at Year 1 of 100.417 → called at 100, today 101.707. `Call = 102.114 − 101.707 = 0.407`. Putable: Year 2 put at 100 → 100.707 at Year 1, today 102.397, `Put = 0.283`.
4. **Callable at 10% vol**: Year 2 node values 98.791 / 99.738 / 100.526 → reset to 100.000 at the low node. Year 1: H = (4.25 + ½·98.791 + ½·99.738)/1.038695 = 99.658; L = (4.25 + ½·99.738 + ½·100)/1.031681 = 100.922 → reset to 100. Today = (4.25 + ½·99.658 + ½·100)/1.025 = **101.540**. `Call = 102.114 − 101.540 = 0.574`.
5. **Putable at 10% vol**: puts at Year 2 in the top two states (98.791 and 99.738 → 100). Value today **102.522**, `Put = 0.408`.
6. **Volatility check**: callable 101.707 (σ≈0), 101.540 (10%), 101.357 (15%), 101.177 (20%). Putable 102.398 (≈0), 102.522, 102.612, 102.696. Callable falls, putable rises, exactly as predicted.
7. **OAS**: if the callable trades at 101.000, a constant spread of **28.55 bp** on every tree rate reprices it. At 30 bp value is 100.973; at 28 bp 101.010. Same price at σ = 5%, 15%, 20% gives OAS of about 38.2, 18.9, 9.4 bp. Assuming a higher σ makes the bond look less cheap.
8. **Effective duration** (price 101.000, OAS 28.55 bp, Δ = 30 bp): PV₋ = 101.599, PV₊ = 100.407. `EffDur = (101.599 − 100.407)/(2 × 0.003 × 101.000) = 1.97`. The straight bond's duration on the same tree is about 2.80: the call shortens it.
9. **Effective convexity**: at price 100.785 (OAS ≈ 40 bp), PV₋ = 101.381, PV₊ = 100.146, so `EffCon = (101.381 + 100.146 − 201.570)/(0.003² × 100.785) ≈ −47.4` (negative, near the money). At price 101.000 the same calculation gives a small positive value (≈ +7), so the sign is sensitive to the price and to rounding: use unrounded PVs.
10. **Capped/floored floaters** (same tree, coupon = reference rate set in arrears): 4.5% cap → 99.761, `Cap = 0.239`. 3.5% floor → 101.133, `Floor = 1.133`. A 5.6% cap is above the top node (5.5258%), so it is worthless (value 100.000); a 3.0% floor adds 0.488 (100.488); a 2.5% floor adds nothing (the lowest rate at Time 1 is 3.17%, but Time 0 rate is exactly 2.5%).
11. **Convertible (Twitter 0.25% due 2024)**: conversion ratio 17.5 → conversion price $57.14; share price $35.14 → conversion value $614.95. 5-year straight value at 2.5% flat, semiannual = $894.86, so minimum value = $894.86. Convertible price $952.25 → market conversion price = $54.41 per share ($54.40 in the reading), premium per share ≈ $19.27 (reading: $19.26), premium ratio ≈ 54.8%, premium over straight value 6.41%. The stock is well below the conversion price and the convertible is near its bond floor: bond-like ("busted" side). If yields on comparable straight bonds were 12%, straight value would be $567.59, below conversion value $614.95 → an arbitrage of $47.36 (buy, convert, sell shares).

## Anti-patterns
- **Using modified duration or YTM for optioned bonds**: cash flows change with rates. Use effective duration on a tree, computed at constant OAS.
- **Comparing OAS across different volatility assumptions**: OAS shrinks as σ rises, so cheapness is an artifact of σ. Compare at the same σ.
- **Averaging up/down durations when the option is near the money**: effective duration hides the asymmetry. Report one-sided durations.
- **Valuing a callable to maturity or to the first call date only**: it is only right if the option is deep in or out of the money. Otherwise use the tree.
- **Using the premium over straight value as true downside**: the straight floor moves with rates and credit spreads.
- **Ignoring dilution/coupon give-up when calling convertibles "win-win"**: issuer shareholders bear dilution; investors accept a lower coupon; forced conversion is an issuer tool.
- **Shifting rates on the tree instead of the par curve**: rebuild and recalibrate the tree after each curve shift.

## Exam Focus & Traps
- **Sign conventions**: callable = straight − call; putable = straight + put; capped = straight − cap; floored = straight + floor. The option value is always a difference of two bond prices.
- **Which bond changes with volatility**: straight bond value never changes with σ; callable falls, putable rises, both option values rise.
- **Reset values**: use the exercise price at nodes where exercise happens (call: if value > call price; put: if value < put price), and use the **reset** value in the next backward step. Do not add the coupon before testing exercise.
- **Callable price rise is capped near the call price**: a callable's effective duration can never exceed the straight bond's; a high-coupon or low-rate callable is a proxy for the first-call-date bond.
- **One-sided durations**: callable near the money has up-duration > down-duration; putable has down-duration > up-duration.
- **Convexity**: callable negative near the money; putable always positive; straight positive but small.
- **Key rate durations**: an option-free par bond depends only on its own maturity key rate; zeros and low coupons can show **negative** key rate durations at shorter maturities. Optioned bond key rates depend on time to exercise.
- **Puttable = extendible** with a different underlying straight bond.
- **Cap and floor mechanics**: a cap is an issuer option; a floor is an investor option; set in arrears means the reset rate is also the payment rate at the next date. Cap above the highest tree rate = worthless.
- **Convertible profile**: share price far below conversion price → bond-like, driven by rates and credit; far above → stock-like, ignore spread and rate moves; near → hybrid. Arbitrage: price below max(conversion, straight) → buy the convertible (convert and sell shares, or hold a bond that is cheap).
- **⚠ Correction (errata, Reading 30, section 10.2.3)**: the market conversion premium per share is **market conversion price minus share price**, i.e. $54.40 − $35.14 = $19.26 (not $57.14 − $54.40 = $2.74). The errata's printed ratio "54.18%" is a transposition: $19.26 / $35.14 = **54.81%** (54.85% with the unrounded $54.414 conversion price). The old 7.80% figure is wrong.
- **⚠ Reading text**: Exhibit 4 title and the phrasing "conversion value" vs "parity value" are interchangeable; some texts call the exhibit's convertible minimum a floor, which is not fixed.
- **Convexity scaling**: raw effective convexity (e.g. −47.4) is sometimes reported divided by 100; check the convention.

## Key Takeaways
1. Value optioned bonds as straight bond ± option; the tree gives the option value as a price difference.
2. Higher volatility lowers a callable's value, raises a putable's, and reduces a callable's OAS at a fixed price.
3. OAS is a relative-value measure: compare it with similar credit and structure at the same σ; low OAS = rich, high = cheap.
4. Effective duration needs a repricing at constant OAS with a rebuilt tree. Callable and putable durations never exceed the straight bond's.
5. Near the money, look at one-sided durations and effective convexity: callable is negatively convex, putable is positively convex.
6. Key rate durations show where on the curve the bond is exposed and shift toward the exercise date as the option moves into the money.
7. Capped floater = straight − cap; floored floater = straight + floor; check whether the cap/floor is ever binding on the tree.
8. Convertible minimum value = max(conversion value, straight value); classify it as busted, hybrid or equity-like by share price versus conversion price, and use market conversion premium to see what you pay for the option.

## Connects To
- **ch08**: builds and calibrates the binomial tree, backward induction and arbitrage-free framework used here.
- **ch07**: spot, par and forward curves; key rate and shaping risk.
- **ch05**: effective duration, convexity and callable bond behaviour at Level I.
- **ch01**: contingency provisions (call, put, convertible) and embedded option terminology.
- **ch10 / ch11**: credit analysis and CDS give the credit-spread inputs (Z-spread, OAS vs credit).
- **ch04**: MBS prepayment option is valued the same way but needs Monte Carlo (path dependence).
- **`tuckman-fixed-income`**: OAS and effective duration of callables in depth.
- **`hull-derivatives`**: option valuation and lattice methods.
