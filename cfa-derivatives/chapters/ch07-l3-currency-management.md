# Chapter 7: Currency Management: An Introduction
> **Source**: CFA Program Curriculum 2023, Level III, Reading 10 · Derivatives & Risk Management (identical to the 2019 edition) | William A. Barker, PhD, CFA

## Core Idea
Foreign assets carry two risks that **multiply**: the local asset return and the move of the foreign currency against your home currency. Currency management first sets a **strategic** position in the IPS, somewhere between fully hedged and currency as an alpha source. It then allows **tactical** deviations driven by market views (fundamentals, technicals, carry, volatility). These are implemented with forwards, FX swaps and options. Every cheaper hedge buys **less downside protection and/or less upside**. There is no free insurance and no single correct hedge ratio.

## Learning Outcomes Covered
- Analyze the effect of currency moves on portfolio return and risk (return and variance decomposition)
- Discuss strategic choices and formulate a currency program from IPS objectives, constraints and market conditions
- Compare active strategies: economic fundamentals, technical analysis, carry trade, volatility trading. Explain how changes in their drivers shift tactical positions.
- Use forwards and FX swaps to set and adjust hedge ratios (rolls, mark-to-market, roll yield)
- Use option structures to reduce hedging cost (OTM puts, risk reversals, put spreads, seagulls, exotics)
- Use cross hedges, macro hedges and minimum-variance hedge ratios for multi-currency portfolios
- Discuss challenges of emerging market (EM) currency exposure (liquidity, tails, NDFs)

## Frameworks Introduced
- **Return decomposition**: `R_DC = (1 + R_FC)(1 + R_FX) − 1`.
  - R_FX is the % change of the foreign currency **against the domestic currency**, measured on a quote with the **domestic currency as the price currency** (DC/FC). Invert market quotes when needed.
  - Portfolio version: `R_DC = Σ ωᵢ(1 + R_FC,i)(1 + R_FX,i) − 1`, with weights in domestic-currency value, Σωᵢ = 1 (shorts allowed).
- **Risk decomposition**: `R_DC ≈ R_FC + R_FX`, so `σ²(R_DC) ≈ σ²(R_FC) + σ²(R_FX) + 2σ(R_FC)σ(R_FX)ρ(R_FC, R_FX)`.
  - Currency exposure usually adds variance. It *reduces* risk only when ρ(R_FC, R_FX) is sufficiently negative.
  - If the foreign asset is riskless (e.g., a T-bill), the formula is **exact**: `σ(R_DC) = (1 + R_FC) × σ(R_FX)`.
- **Two-step portfolio construction**: (1) optimize asset weights on **fully hedged** returns (R_DC = R_FC); (2) decide how far to relax the full hedge, currency by currency. Derivatives "unbundle" price risk and FX risk, so the full joint optimization, which needs every R_FC, R_FX, σ and ρ, can be avoided.
- **Strategic hedging decision**: diversification benefit versus cost.
  - **Diversification**:
    - Time horizon: long-run mean reversion (PPP) argues for less hedging, but "long run" can mean decades.
    - Asset class: bonds are more correlated with FX (both are driven by rates), so hedge them close to 100%. Equities offer more of a case for leaving currency exposure.
    - Safe-haven currencies (USD, JPY, CHF) rise in stress, so keeping some of that exposure hedges risky assets. Non-US investors **under-hedge USD**. US investors **over-hedge** back into USD.
  - **Costs**:
    - Trading costs: bid–offer spreads, option premiums, cash flows from rolling forwards (volatility of the cash account), and back/middle-office infrastructure.
    - **Opportunity cost**: a full hedge gives up favorable moves.
    - **Regret minimization** leads many managers to a **50% hedge ratio**.
    - Treat hedging like insurance with a deductible, so set a tolerance *range*, not a point.
- **Bias toward a fuller hedge when**: the objectives are short term; the beneficial owners are risk averse (and immune to regret); income or liquidity needs are immediate; the portfolio holds foreign **fixed income**; hedging is cheap; markets are volatile; and the owners or oversight committee are skeptical of active FX. Relaxing any of these allows wider bands or FX as an asset class.
- **Spectrum of currency risk management**:

| Approach | Mandate | Neutral position | Manager discretion |
|---|---|---|---|
| **Passive hedging** | Rules-based. Match the benchmark's currency exposure (often a local-currency benchmark, i.e., 100% hedged) and minimize tracking error. | Benchmark hedge ratio | None, apart from periodic rebalancing (e.g., monthly) |
| **Discretionary hedging** | Protect first, add value second. | Benchmark (e.g., 100%) | Limited band, e.g., hedge ratio 95%–105% |
| **Active currency management** | Take FX risk to earn alpha within risk limits. | Benchmark, but staying flat for long is not acceptable | Wide |
| **Currency overlay** | (a) Outsourced passive hedging; (b) external manager with directional latitude on the portfolio's own currencies; (c) **FX as an asset class**, meaning any currency pair, like an FX hedge fund | As mandated | Widest in (c) |

  - Separate **currency beta** (the hedge) from **currency alpha** (the overlay). The overlay should add alpha that is **uncorrelated** with the assets and with other alpha sources. Diversify across overlay managers with **different styles** (or use a fund of funds). Benchmark speculative results against the **100%-hedged neutral**.
- **Economic fundamentals model**: the long-run **real exchange rate** converges to fair value (PPP), which is the anchor. Short/medium-term factors set the path, including overshooting and undershooting.
  - All else equal, the **base currency appreciates** with a rise in: its long-run equilibrium real rate; its real or nominal interest rates; *expected foreign* inflation; the *foreign* risk premium. It also appreciates if it currently sits below its equilibrium value.
- **Technical analysis**: three premises. (1) Price history already contains all fundamentals. (2) Patterns repeat because psychology (greed and fear) repeats. (3) Technicals forecast where price *will* trade, not where it *should* trade.
  - Tools: overbought/oversold readings; **support** (bid clusters) and **resistance** (offer clusters), where price gets sticky and then accelerates once breached as stops trigger; the **200-day moving average**; the 50-day crossing the 200-day as a breakout signal.
  - No reliable FX volume data exist (OTC market), so FX technicals are price-only. They are less useful in trendless markets.
- **Carry trade = trading the forward rate bias = earning positive roll yield**: borrow the low-yield currency, which trades at a forward premium; invest in the high-yield currency, which trades at a forward discount.
  - It exploits the failure of **uncovered interest rate parity (UIP)** over short to medium horizons: high-yielders often *appreciate*, and the forward rate is a **biased** predictor of the future spot rate.
  - Return profile: long calm gains and sudden crash losses, i.e., **negative skew** and fat tails ("picking up nickels in front of a steamroller").
  - Funders are usually safe havens (USD, JPY, CHF). Lower spot volatility of the pair is better. Multi-currency baskets can be optimized.
- **Volatility trading**: delta-hedge options (hedge size = delta × notional, via spot or forwards) to isolate **vega**, then trade implied vol.
  - A long straddle (ATM, net delta 0) or long strangle (OTM, cheaper, pays only beyond the strikes) is long vol.
  - Speculators (e.g., overlay managers) are typically **net short vol** to collect the premium. Hedgers are net long vol and pay time decay.
  - Vol is cyclical: long calm spells, then spikes, often at the same time as carry unwinds.
- **Forward mark-to-market (4 steps)**:
  1. Enter an equal, offsetting forward for the same settlement date.
  2. Price it with the correct side: **selling the base currency → bid; buying the base currency → offer**. All-in = spot + points/10,000 (JPY pairs: /100). Points are *not* annualized.
  3. Settlement cash flow = notional × (new all-in rate − original rate), signed. You gain if the currency you were long appreciated.
  4. Discount at the rate of the **cash-flow currency** for the remaining term (ACT/360).
- **Rolling with FX swaps**: the spot leg settles the maturing forward and the forward leg re-establishes the hedge.
  - **Matched swap**: equal legs; mid-market spot, forward points on the side of the forward trade.
  - **Mismatched swap**: resizes the hedge. It equals a matched swap plus an outright forward for the difference, and the spot rate is priced on the side of the net trade.
  - A **dynamic hedge** (periodic rebalancing) controls drift at a transaction cost. A **static hedge** accumulates unintended exposure as asset values move. Higher risk aversion means more frequent rebalancing.
- **Hedge-or-not decision with roll yield**: expected hedge benefit = expected adverse FX move avoided. Expected cost = roll yield if negative.
  - A **risk-neutral** manager hedges only if the expected depreciation exceeds the cost.
  - A **risk-averse** manager may hedge anyway because the forecast can be wrong.
  - When hedging means selling the low-yielder/buying the high-yielder (an implicit carry position), hedge fully or even over-hedge. Trading against the forward rate bias argues for lower hedge ratios.
- **Option "building blocks" (6 steps)**:
  1. Identify the base currency in the P/B quote.
  2. Decide whether the hedge requires *buying* or *selling* the base currency.
  3. If buying the base currency: core hedge = long call and/or long forward.
  4. If selling the base currency: core hedge = long put and/or short forward.
  5. Cut cost by going OTM, writing options, changing strikes or notionals, or adding exotic features. Each step gives up protection or upside.
  6. Tilt toward your view in proportion to discretion and conviction. Adjust strikes and notionals to approach zero cost.

## Key Concepts
- **P/B quote**: price of 1 unit of base currency B in price currency P (USD/EUR 1.0800 = $1.08 per €).
  - Base-currency hierarchy: EUR > GBP > AUD > NZD > USD (e.g., GBP/EUR, USD/GBP, USD/AUD, JPY/USD, CAD/USD).
  - A **pip** is the 4th decimal (2nd for JPY). The **handle/big figure** is the integer plus the first two decimals.
  - Spot settles **T+2** (CAD/USD T+1).
- **Bid/offer**: the dealer buys the base currency at the bid and sells it at the offer. The client always gets the worse side ("hit the bid" = sell base, "pay the offer" = buy base).
- **Forward points**: (F − S) scaled to the last decimal of spot. Positive points = base currency at a forward **premium** (base rate < price rate, from CIP).
- **FX swap**: simultaneous spot and opposite forward in the same pair. No interim interest, short-dated. Used to **roll hedges**. It is not a currency swap.
- **Hedge ratio**: notional of the hedge / market value of the hedged asset.
- **Roll yield (roll return)**: gain or loss from the forward "rolling down" to spot. Magnitude `|(F − S)/S|`. **Positive** when you *sell* the base currency at a premium or *buy* it at a discount.
- **Forward rate bias**: the forward premium/discount overstates the subsequent spot move and often gets the direction wrong.
- **Risk reversal**: long call + short put (a *long* risk reversal). A collar for a long-base exposure (long put + short call) is a **short risk reversal**.
- **Put spread**: long OTM put + short deeper-OTM put. Protection only between the strikes. A **1×2** version is near zero-cost but adds leverage below the lower strike.
- **Seagull spread**:
  - **Short seagull**: long ATM put (body) + short OTM put and short OTM call (wings). Protects from spot down to the lower strike and allows upside to the call strike.
  - **Long seagull**: short ATM option (body) + long OTM put and long OTM call (wings). For a long-base exposure (write the ATM call): cheap protection below the put strike and unlimited upside above the call strike.
- **Knock-in / knock-out option**: a vanilla option created or extinguished when spot touches a **barrier** (not the strike). It is cheaper than a vanilla option.
- **Digital (binary) option**: pays a fixed amount if in the money (American digital: if touched). It costs more than a vanilla option at the same strike and is a leveraged, lottery-like tool for speculators, not hedgers.
- **Delta-quoted FX options**: ATM = 50-delta. Standard quotes are **25-delta** and **10-delta** (a 10-delta option is further OTM and cheaper). Strikes are backed out of the pricing model.
- **Cross hedge / proxy hedge**: hedging with a correlated but different instrument (e.g., AUD exposure with NZD). A **proxy** hedge hedges back to the home currency. A "cross" hedge (strict sense) shifts exposure from one foreign currency to another (IDR → THB).
- **Macro hedge**: hedge the portfolio's risk *factors or scenarios* (recession, stress) rather than each pair, using currency-basket derivatives, gold or a volatility overlay.
- **Basis risk**: an unstable correlation between the exposure and a cross or macro hedge. In a crisis it can turn a hedge into a doubled bet. Forwards have little basis risk because they converge to spot.
- **Non-deliverable forward (NDF)**: cash-settled in the non-controlled currency (usually USD) for currencies with capital controls (CNY, KRW, RUB, INR, BRL). Its credit exposure is lower than an outright forward's because no principal moves. It is not bound by CIP, because offshore supply and demand drive the price.

## Formulas & Reference Tables
- `R_DC = (1 + R_FC)(1 + R_FX) − 1 = R_FC + R_FX + R_FC·R_FX`
- `R_FX` on a quote DC/FC. From an FC/DC market quote: `R_FX = (S₀/S₁) − 1`.
- `σ²(R_DC) ≈ σ²(R_FC) + σ²(R_FX) + 2σ(R_FC)σ(R_FX)ρ(R_FC,R_FX)`
- Two-asset portfolio: `σ²(ω₁R₁ + ω₂R₂) = ω₁²σ²(R₁) + ω₂²σ²(R₂) + 2ω₁ω₂σ(R₁)σ(R₂)ρ(R₁,R₂)`, with Rᵢ the domestic-currency returns
- CIP: `(F_P/B − S_P/B)/S_P/B = (i_P − i_B)(t/360)/(1 + i_B·t/360)`
- UIP: `%ΔS_H/L ≈ i_H − i_L` (low-yield currency L is the base; a positive value = the high-yielder depreciates)
- All-in forward = spot (bid or offer) + points/10,000 (JPY: /100)
- Forward MTM = `N_B × (F_offset − F_original)/(1 + i_P × days/360)`, signed for the original long base position
- Roll-maturity cash flow for a short-base hedge = `N_B × (F_original − S_T)` in the price currency
- Minimum-variance hedge ratio: `h* = Cov(R_DC, %ΔS)/Var(%ΔS) = ρ(R_DC, %ΔS) × σ(R_DC)/σ(%ΔS)`, i.e., β from the OLS regression `R_DC = α + β·%ΔS + ε`, with %ΔS on the DC/FC quote
- NDF settlement (base = USD) = `N_USD × (S_fixing − F_NDF)/S_fixing` in USD for the long-USD side

| Carry / forward rate bias / roll yield | Buy / invest | Sell / borrow |
|---|---|---|
| Carry trade | High-yield currency | Low-yield currency |
| Trading the forward rate bias | Forward-discount currency | Forward-premium currency |
| Result | Positive roll yield (buy low, sell high) | |

| Hedger's need | Core hedge | Cheaper variants (less protection and/or upside) |
|---|---|---|
| Long foreign currency = base (must sell base) | Short forward / long put | OTM put; short risk reversal (collar); put spread; 1×2 put spread; short seagull; knock-in/out puts |
| Short foreign currency = base, or long FC as price currency (must buy base) | Long forward / long call | OTM call; long risk reversal; call spread; long seagull (write ATM put, buy OTM put and OTM call) |

| Instrument | Why institutions prefer forwards over futures |
|---|---|
| Forwards | Any pair, date or size; no initial or variation margin (though CSAs increasingly require collateral); far larger OTC volume, so more liquid in size |
| Futures | Standardized sizes and dates; not every cross or EM pair; margin and daily MTM tie up liquidity; useful for small sizes (private wealth) |

## Mental Models
- **"Two dice, multiplied."** A foreign asset's home-currency return is local return × currency return. Hedging removes the second die but costs the roll yield, plus the upside you give up.
- **Hedging is insurance with a deductible.** Insure the large adverse moves, self-insure the noise. Tolerance bands, OTM strikes and partial hedge ratios are the deductible.
- **The forward premium is a price tag, not a forecast.** Because of the forward rate bias, selling a currency at a forward premium is paid carry. Selling at a deep discount (a high-yielder or a crisis-hit EM currency) is expensive insurance.
- **"Lower premium = lower insurance."** Every cost-reduction trick (writing options, moving strikes, changing notionals, barriers) removes a slice of protection or upside. Name the residual risk before you accept a zero-cost structure.
- **Correlations are fair-weather friends.** Cross hedges, EM diversification and carry baskets all rely on correlations that jump in "risk-on/risk-off" regimes. Size positions for the crisis correlation.

## Worked Example
**1. Return and risk in home currency.** A euro-based investor holds a Canadian asset. Local prices 101.00 → 99.80 (R_FC = −1.19%). CAD/EUR 1.2925 → 1.3100, so R_FX = (1.2925/1.3100) − 1 = −1.34%.
- R_DC = (0.9881)(0.9866) − 1 = **−2.51%**.
- The Canadian investor holding the euro asset (100.69 → 101.50, R_FC = +0.80%; R_FX = 1.3100/1.2925 − 1 = +1.35%) earns **+2.17%**.
- With σ(R_FC) = 3%, σ(R_FX) = 2%, ρ = 0.5: σ(R_DC) = √(0.0009 + 0.0004 + 0.0006) = **4.36%**.

**2. Multi-currency risk and a natural cross hedge.** A US investor holds 1-year AU and NZ T-bills: R_FC 4% and 6%; expected R_FX +5% each; σ(R_FX) 8% and 10%; ρ(USD/AUD, USD/NZD) = 0.85.
- Individual returns: 1.04 × 1.05 − 1 = 9.2% and 1.06 × 1.05 − 1 = 11.3%. Risks (exact, riskless assets): 1.04 × 8% = 8.32% and 1.06 × 10% = 10.6%.
- Equal weights: R_DC = 10.25%; σ = √(0.25·0.0832² + 0.25·0.106² + 2·0.25·0.0832·0.106·0.85) = **9.1%**.
- Long NZ / short AU (+1/−1): R_DC = 2.1%; σ = √(0.0832² + 0.106² − 2·0.0832·0.106·0.85) = **5.6%**. With ρ = 0.95 it falls to **3.7%**. Long/short positions in correlated currencies hedge each other, and the residual is basis risk.

**3. Forward MTM before maturity.** Long GBP 5m, 6-month forward at AUD/GBP 1.9000. Three months later: spot 1.9200/1.9205, 3-month points 40/45, 90-day AUD rate 4%.
- Offset by *selling* GBP (the base currency), so use the bid: 1.9200 + 0.0040 = 1.9240.
- Cash flow at settlement = 5m × (1.9240 − 1.9000) = AUD 120,000 (gain, because GBP rose). MTM = 120,000/(1 + 0.04 × 90/360) = **AUD 118,812**.

**4. Rolling a hedge with a mark-to-market cash flow.** A US fund holds EUR 10.0m of assets and hedges 100% by selling EUR 1-month forward.
- Inception: spot USD/EUR 1.0800/1.0802, points +18/+20. Sell EUR at the bid: all-in F = **1.0818** (EUR at a premium, so positive roll yield for the seller).
- One month later: assets EUR 10.4m; spot 1.1000/1.1002; points +17/+19. The net EUR sale increases, so both legs are priced on the bid.
  - **Spot leg**: buy EUR 10.0m at 1.1000 to settle the maturing forward. **Cash flow today** = 10.0m × (1.0818 − 1.1000) = **−USD 182,000** (the hedge loses because the EUR rose).
  - **Forward leg**: sell **EUR 10.4m** (resized: a mismatched swap) at 1.1000 + 0.0017 = **1.1017**.
- Check: the USD value of the original EUR 10m rose by 10m × (1.1001 − 1.0801) = +200,000 (mid rates). The hedge lost 182,000. The difference of **+18,000** is the positive roll yield (0.0018 × 10m).
- The **cash** outflow must be funded now, even though the offsetting gain is unrealized in the asset. That is the liquidity cost of forward hedging.

**5. Minimum-variance hedge.** A UK investor holds a USD 10m S&P 500 fund. σ(%ΔS_GBP/USD) = 2.7%, σ(R_DC) = 4.4%, ρ = 0.2.
- h* = 0.2 × 4.4/2.7 = **0.33**, so short about USD 3.3m forward. The market quote is USD/GBP, so selling USD means **buying GBP**: a *long* USD/GBP forward.
- In the curriculum's Swiss-equity case, β = 1.35 gives a hedge ratio of **135%**. Min-variance ratios can exceed 100% when R_FC and R_FX are positively correlated.

**6. Hedge decision with roll yield** (HKD-based, long GBP and long ZAR).
- HKD/GBP: spot 12.4610, forward 12.6550 (+1.56%), forecast 12.3000 (−1.29%). Selling GBP at a premium earns roll yield *and* avoids the expected loss, so **hedge**.
- HKD/ZAR: spot 0.9510, forward 0.9275 (−2.47% cost), forecast 0.9300 (−2.21%). The expected cost exceeds the expected loss, so a risk-neutral manager does **not hedge**. A risk-averse manager weighs the certain 2.5% cost against the risk that the ZAR falls further.

## Anti-patterns
- **Computing R_FX on the market quote without checking which currency is the price currency**: this gives a wrong sign or magnitude when your home currency is the base.
- **Adding R_FC and R_FX for large moves**: the approximation ignores the cross-term (10% and 5% give 15.5%, not 15%).
- **Running a static hedge on a volatile asset**: the hedge ratio drifts and leaves pure unintended currency risk.
- **Treating a zero-cost structure as free**: 1×2 put spreads and short seagulls reopen or double exposure beyond the short strike.
- **Using exotics for institutional hedging**: they are hard to value, hard to get hedge-accounting treatment for, and carry high dealer margins. They suit sophisticated overlay or speculative accounts.
- **Using VaR or Sharpe ratios on carry and EM books**: normal-distribution metrics understate negative-skew, fat-tail risk. The Sharpe ratio looks great until the unwind.
- **Relying on a cross or macro hedge without re-estimating β/ρ**: basis risk can turn the hedge into a doubled position in stress.
- **Assuming a currency peg or capital controls mean low risk**: pegs break abruptly. NDF gains built over calm periods can reverse overnight.

## Exam Focus & Traps
- **Bid or offer?** Selling the base currency → bid (spot and points). Buying it → offer. For a JPY/HKD hedge that *sells JPY*, you are **buying HKD, the base**, so use the **offer** points.
- **Forward MTM**: discount at the **cash-flow currency's** rate. The offsetting forward must be for the **same settlement date** (remaining term), not a new full tenor.
- **Rebalancing a hedge**: if the foreign asset *fell* in value, reduce the short forward by **buying the difference forward**, not spot.
- **Roll yield sign**: selling base at a premium, or buying base at a discount, gives **positive** roll yield. Negative roll yield = trading **against** the forward rate bias = a negative carry trade.
- **Carry trade choice**: pick the widest yield spread **and** the lowest implied volatility (e.g., fund CHF at −0.10%, invest PLN at 4.75% with 8.4% vol, rather than MXN at 15.6% vol).
- **Fundamentals**: a *rise in foreign expected inflation* or in the *foreign risk premium* makes the **base** currency appreciate. Monetary tightening in India → INR appreciates → **INR/USD falls** (USD is the base).
- **Technicals**: a 200-day MA *above* spot that has not been crossed is **resistance** above, not support.
- **Cheapest way to go long vol**: buy a 25-delta (or 10-delta) **strangle**. Writing a 40-delta strangle is short vol.
- **Liquidity shock after a hedge rebalance**: "do nothing" is correct, because being fully hedged already minimizes currency risk.
- **Min-variance hedge** = ρ × σ(R_DC)/σ(R_FX). Do not invert the ratio. For a direct forward hedge it is ≈100%, so the regression is superfluous. It matters for cross, macro and joint (R_FC and R_FX) hedges. The Campbell (2010) evidence: ≈100% for bonds, wide dispersion for equities by currency pair.
- **Overlay mandates**: a fund that must avoid all FX risk and lacks expertise uses an overlay for **passive hedging**. A fund that already hedges in-house uses an overlay to **separate alpha from hedging**. Several overlay managers add value only if their **styles differ** (low correlation).
- **EM crisis mechanics**: a central-bank rate hike to defend the currency **deepens the forward discount**, so the hedge (selling the currency forward) becomes more expensive exactly when needed. Crosses such as CLP/THB trade through USD, so you pay two spreads with time-zone liquidity gaps.
- **⚠ Correction (curriculum practice problem, "Delgado" roll)**: the solution multiplies USD amounts by a *USD/EUR* rate to get euros, and it nets a spot-leg flow against the new forward leg that settles a month later. With USD/EUR = USD per EUR, **divide**: EUR = USD/(USD/EUR). The cash flow realized at the roll is the maturing forward versus spot on the old notional. Sold USD 2.5m forward at 0.8914 + 0.0030 = 0.8944 (EUR 2,795,170) and bought USD 2.5m back spot at 0.8875 (EUR 2,816,901), giving ≈ **−EUR 21,731**. The new USD 2.65m forward at 0.8901 has no cash flow today.

## Key Takeaways
1. Measure R_FX on the DC/FC quote. Multiply the return components. Currency risk adds to asset risk unless correlation is negative.
2. Build the portfolio on hedged returns first, then decide the currency exposure. The IPS fixes the neutral hedge ratio, the band, the rebalancing frequency, the benchmark and the permitted tools.
3. Hedge foreign bonds close to 100%. Foreign equities, safe-haven exposure, long horizons and cheap carry justify partial hedging. Regret minimization explains the popularity of 50%.
4. The four active styles (fundamentals, technicals, carry, volatility) rest on different beliefs. Carry is short a crash (negative skew). Vol selling earns a premium until the spike.
5. Forwards and FX swaps are the workhorses. Price the correct side of the market, mark to market by offsetting and discounting, and resize hedges with mismatched swaps. Budget for roll-yield and cash-flow costs.
6. Options add convexity at a premium. Collars, put spreads, seagulls and exotics cut the premium by giving back protection or upside.
7. For multi-currency and EM exposures, use cross, macro and min-variance hedges and NDFs, and actively monitor basis risk, liquidity, tail risk and government intervention.

## Connects To
- **ch06**: currency swaps, cross-currency basis swaps and currency futures for modifying FX exposure.
- **ch05**: option strategies (collars, spreads, straddles/strangles) underpinning FX option hedges.
- **ch03**: forward pricing and valuation (CIP, MTM of forwards).
- **`cfa-economics` ch07–ch08**: exchange rate quotes, cross rates, forward points, and the parity conditions (CIP, UIP, PPP, forward rate bias) behind carry and fundamental models.
- **`hull-derivatives` ch03**: minimum-variance hedge ratio, basis risk and rolling hedges. **ch07**: swaps.
- **`cfa-fixed-income` ch14**: hedged vs. unhedged foreign bond returns and currency decisions in yield-curve strategies.
- **`passarelli-option-greeks` ch12–ch13, ch15**: delta-neutral trading and straddles/strangles, the mechanics of FX volatility trading.
- **`cfa-asset-allocation-cme` ch06–ch08**: strategic asset allocation, and currency exposure as an allocation decision.
