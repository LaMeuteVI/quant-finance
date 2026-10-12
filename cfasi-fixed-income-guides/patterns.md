# Patterns — Fixed Income Guide Recipes

## Bond Risk Mapping
**When to use**: before judging any bond's yield.
**How**: 1. Decompose the contract (ch01). 2. Tag the risks: rate, curve, credit (default, spread, downgrade), call, reinvestment, liquidity, currency, volatility, event, inflation (ch02). 3. Match the features to risks (long maturity, low coupon, call, put, floater cap and reset).
**Trade-offs**: qualitative; follow with duration and spread numbers. (ch 01, 02)

## Choose the Yield Measure
**When to use**: comparing or quoting yield.
**How**: straight bond: YTM; callable or putable: yield to worst; linker: real yield and breakeven; floater: discount margin; screening only: current yield. Convert to holding-period return if selling early.
**Trade-offs**: YTM assumes hold to maturity and reinvestment at YTM. (ch 06)

## Bootstrap Spot Rates and Forwards
**When to use**: arbitrage-free pricing, forward views.
**How**: 1. Use the 1-year zero. 2. Solve `P2 = C2/(1+z1) + (N2+C2)/(1+z2)²` for z2; repeat for z3. 3. Forward `(1+1f2) = (1+S2)²/(1+S1)`; general: `(1+S_n)^n = (1+S_{n−1})^{n−1}(1+(n−1)f_n)`. 4. Price each cash flow at its own spot.
**Trade-offs**: needs liquid same-issuer bonds; for flat curves equals YTM pricing. (ch 05, 06)

## Spread Ladder (Nominal → Z → OAS)
**When to use**: relative value of credits.
**How**: nominal spread for a quick check; Z-spread for straight bonds (constant spread over the spot curve); OAS if the bond has options; `option cost = Z − OAS`; ASW for floating-rate comparison; CDS basis `CDS − Z`.
**Trade-offs**: OAS depends on the volatility model (higher vol lowers a callable's OAS). (ch 05, 13)

## Duration-Convexity Scenario
**When to use**: price response to a yield shift.
**How**: `ΔP/P ≈ −MD Δy + ½ C Δy²`; for KRD, `−Σ KRD_k Δy_k`; for options use effective duration from repricing. Add spread duration × Δspread for credit.
**Trade-offs**: callable bonds have negative convexity near the call; parallel-only duration hides curve risk. (ch 06, 08, 13)

## Immunize a Dated Liability
**When to use**: known amount at a known date.
**How**: 1. Compute the liability PV and duration. 2. Cash flow match if possible; otherwise match Macaulay duration with dispersed cash flows. 3. Rebalance as duration drifts; fix with futures overlay. 4. If a surplus exists, use contingent immunization with a floor.
**Trade-offs**: credit risk remains; parallel shifts assumed. (ch 08)

## Sampled Index Replication
**When to use**: passive bond mandates.
**How**: match effective duration, KRDs, sector and quality mix, coupon and maturity buckets; cap issuer weight; rebalance for index events; measure tracking error.
**Trade-offs**: partial coverage means active risk; OTC liquidity limits trades. (ch 07, 08)

## Top-Down / Bottom-Up Active Process
**When to use**: benchmark-relative mandates.
**How**: bottom-up: universe by homogeneous credit bucket → relative value → spread curve per issuer → build to duration and spread duration. Top-down: macro view → sector, curve and quality tilts.
**Trade-offs**: bottom-up fails when credit risks differ greatly inside a bucket. (ch 08)

## Fund Due Diligence (Quant + Qual)
**When to use**: selecting and monitoring active or unconstrained funds.
**How**: 1. Build a peer group by guidelines and realized volatility. 2. Quant: risk-adjusted returns, drawdowns, regression on HY/EM/equity/rates, correlation matrices on two windows. 3. Stress windows (2011, 2013, 2015, early 2016, Feb 2018). 4. Qual: team, process, limits, derivatives and leverage, duration decomposition, liquidity crisis plan, style drift. 5. AUM, fees, base currency, investor target, capacity.
**Trade-offs**: heavy on analyst time; correlations rise in stress. (ch 07, 09, 10)

## Decode Fund Duration
**When to use**: unconstrained or flexible bond funds.
**How**: ask for duration by country and curve segment; hedge instruments (10Y futures) and basis risk; spread duration; behaviour of floaters, ABS/MBS; what the number is if negative (inverse sensitivity); why the manager holds it.
**Trade-offs**: manager-provided data; verify with risk reports. (ch 09)

## Payout Source Check
**When to use**: distributing or Income funds.
**How**: compare distribution yield with portfolio income yield; read class-level rules (fixed % NAV, variable, fixed cents); check tax, frequency, reinvestment plan; regress performance on HY/EM/equity.
**Trade-offs**: if payout exceeds income, NAV erodes. (ch 10)

## EM Country Screen
**When to use**: adding EM exposure.
**How**: classify (primary, secondary, frontier); score seven risk families; compare local vs hard currency; check FX reserves, current account, debt/GDP, central bank credibility; avoid single-theme (commodity) concentration.
**Trade-offs**: non-normal returns; models need judgment. (ch 11, 16)

## HY Spread Check and Spread Duration Band
**When to use**: sizing HY risk.
**How**: expected loss = PD × (1 − RR); excess spread = spread − expected loss; compare spread to history: above +1/+2 sd raise spread duration, below −1/−2 sd cut it; test callable bonds at original maturity.
**Trade-offs**: mean reversion is not guaranteed in a regime shift. (ch 13)

## Convertible Delta-Hedge (Gamma Trade)
**When to use**: monetizing volatility on convertibles.
**How**: short `delta × conversion ratio` shares per lot; re-hedge as delta moves (sell more on rallies, buy back on dips); monitor credit, borrow, dividends.
**Trade-offs**: low realized volatility earns little; busted names carry credit risk. (ch 14)

## AT1 / Tier 2 Call Evaluation
**When to use**: pricing subordinated bank and hybrid paper.
**How**: compute reset coupon = swap + reset spread; compare with issuer's replacement cost; set call vs extension probability; add coupon risk (MDA distance, distributable reserves) and trigger distance.
**Trade-offs**: regulator approval can override economics. (ch 03, 15)

## EM Local Fair Value (Building Blocks)
**When to use**: valuing EM local curves.
**How**: MM fair by definition; MM2Y from expected policy path; 2Y10Y = f(risk factor), risk factor = 10Y spread to benchmark − 5Y CDS − inflation differential; expect mean reversion in 1-12 months; add FX via carry and parity checks.
**Trade-offs**: unstable regimes degrade statistical models. (ch 16)

## Private Debt Underwriting Process
**When to use**: evaluating a private debt deal or fund.
**How**: origination → screening → credit analysis (site visits, business plan stress tests) → rating and negotiation (covenants, guarantees, ratchets) → subscription → monitoring (covenant tests, reporting).
**Trade-offs**: 6-8 weeks per deal; illiquid; resource-intensive. (ch 17)
