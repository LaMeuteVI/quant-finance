# Patterns — CFA Level I Calculation Recipes

## Point Elasticity from a Demand Function
**When to use**: a linear demand equation with several drivers.
**How**: E_x = (∂Q/∂x) × (x/Q), evaluated at the given point. Plug every driver in first to get Q.
**Trade-offs**: the value is only valid locally; elasticity changes along a linear curve (Ch 1).

## Profit Maximization and Shutdown Test
**When to use**: firm output and price decisions.
**How**: set MR = MC. Shut down in the short run if P < AVC. Exit in the long run if P < ATC. For a monopoly, P = MC/(1 − 1/|E|).
**Trade-offs**: MR = P only in perfect competition (Ch 1–2).

## Sectoral-Balance Check
**When to use**: assessing twin deficits or current-account sustainability.
**How**: (S − I) = (G − T) + (X − M). Solve for the unknown balance.
**Trade-offs**: an accounting identity, not causality (Ch 3, 6).

## Forward FX Rate from Interest Parity
**When to use**: pricing FX forwards or checking for covered interest arbitrage.
**How**: F = S × (1 + i_price × d/360)/(1 + i_base × d/360). Forward points = (F − S) × 10⁴.
**Trade-offs**: watch the base/price currency convention and day counts (Ch 7).

## Margin-Call Price
**When to use**: leveraged long stock positions.
**How**: P_call = P₀ × (1 − IM)/(1 − MM). Levered return = (ΔP × shares − interest + dividends)/equity.
**Trade-offs**: ignores the call money rate unless you add it (Ch 8).

## Index Return by Weighting
**When to use**: comparing price-, equal- and cap-weighted indexes.
**How**: price-weighted: ΣP₁/ΣP₀ − 1. Equal: average of returns. Cap: ΣMV₁/ΣMV₀ − 1.
**Trade-offs**: splits change the divisor of price-weighted indexes (Ch 9).

## Gordon / Multistage DDM
**When to use**: equity valuation of dividend payers.
**How**: V = D₁/(r − g), with r from CAPM and g = b × ROE. Multistage: PV(explicit dividends) + PV(Gordon terminal value at the start of the stable phase).
**Trade-offs**: very sensitive to r − g; requires r > g (Ch 13).

## Bond Price and YTM
**When to use**: fixed-rate bond valuation.
**How**: PV = Σ C/(1 + r)ᵗ + F/(1 + r)ᴺ. YTM = the IRR (solve numerically). Between coupon dates, full price = PV × (1 + r)^{t/T} and flat = full − AI.
**Trade-offs**: YTM assumes reinvestment at the YTM (Ch 16).

## Implied Forward Rate
**When to use**: break-even reinvestment rates.
**How**: f = [(1 + z_B)^B/(1 + z_A)^A]^{1/(B−A)} − 1.
**Trade-offs**: needs spot (zero) rates, not coupon yields (Ch 16).

## Money-Market Pricing
**When to use**: T-bills, CP, CDs, repo.
**How**: discount basis: PV = FV(1 − d/Y × DR). Add-on basis: PV = FV/(1 + d/Y × AOR). Convert to a 365-day add-on yield (bond-equivalent yield) to compare.
**Trade-offs**: 360 vs 365 day conventions differ (Ch 16).

## Duration–Convexity Price Estimate
**When to use**: price sensitivity of a bond or portfolio.
**How**: ApproxModDur = (P₋ − P₊)/(2Δy·P₀). ApproxCon = (P₋ + P₊ − 2P₀)/(Δy²·P₀). %ΔP ≈ −ModDur·Δy + ½·Con·Δy².
**Trade-offs**: use effective measures (benchmark-curve shifts) for bonds with options (Ch 18).

## Immunization by Duration Matching
**When to use**: locking in a return over a horizon.
**How**: set Macaulay duration = horizon and rebalance as time passes.
**Trade-offs**: assumes parallel shifts (Ch 18).

## Prepayment Conversion
**When to use**: MBS cash-flow projection.
**How**: CPR = 1 − (1 − SMM)¹². 100 PSA ramps 0.2%/month to 6% CPR at month 30.
**Trade-offs**: prepayment models drive MBS value (Ch 17).

## Credit Screen
**When to use**: quick issuer credit assessment.
**How**:
- Compute debt/EBITDA, FFO/debt, EBITDA/interest and liquidity versus maturities.
- Compare with peers and with rating medians.
- Then EL = PD × (1 − R).
**Trade-offs**: ratios are backward-looking. Add industry and covenant analysis (Ch 19).
