# Chapter 7: The Term Structure and Interest Rate Dynamics
> **Source**: CFA Program Curriculum 2022, Level II, Reading 28 · Fixed Income | Thomas S.Y. Ho, Sang Bin Lee, Stephen E. Wilcox

## Core Idea
Spot rates, forward rates, par yields, swap rates and discount factors are five views of the **same** no-arbitrage information. Once you can move between them, you can see what the market "prices in". Implied forwards are the market-neutral reference path: if they are realized, every bond earns the one-period rate. Every active rate trade (duration, rolldown, curve shape) is a bet that realized spot rates will differ from today's forwards. Shaping risk (level, slope, curvature) is then measured with key rate durations or factor durations, not with effective duration alone.

## Learning Outcomes Covered
- Relate spot rates, forward rates, YTM, expected and realized returns, and curve shape.
- Bootstrap zero (spot) rates from the par curve.
- State what active management assumes about realized spot rates versus forwards, and explain **rolling down the yield curve**.
- Explain the **swap rate curve** and why and how it is used in valuation. Calculate and interpret the **swap spread**.
- Describe short-term spreads that gauge credit and liquidity risk: **TED**, **Libor–OIS**, SOFR.
- Explain the traditional term-structure theories: unbiased (pure) expectations, local expectations, liquidity preference, segmented markets and preferred habitat.
- Measure exposure to yield-curve factors (level, steepness, curvature) and manage it with key rate durations.
- Explain the maturity structure of yield volatilities.
- Build rate views from macro variables: inflation, growth, monetary and fiscal policy, investor demand.

## Frameworks Introduced
- **Forward pricing model** (no-arbitrage): `DF_B = DF_A × F_{A,B−A}`.
  - Buying a B-period zero must cost the same as buying an A-period zero plus a forward commitment to buy a (B−A)-period zero at time A.
  - In rate form this is the **forward rate model**: `(1 + z_B)^B = (1 + z_A)^A × (1 + f_{A,B−A})^{B−A}`.
  - When to use: to extract implied forwards from any spot curve, to price forward contracts, and to test whether your rate view differs from the market's.
  - How to interpret f₇,₁ = 3%: (i) it is the **breakeven reinvestment rate** that leaves you indifferent between an 8-year zero and a 7-year zero rolled for one year; (ii) it is the one-year rate you **lock in** today by extending from 7 to 8 years.
- **Spot rate as a geometric mean of forwards**: `(1 + z_T)^T = (1 + z₁)(1 + f₁,₁)(1 + f₂,₁)…(1 + f_{T−1,1})`.
  - Spots are averages and forwards are marginal rates. So an **upward** spot curve means forwards lie **above** spots, and a **downward** curve means forwards lie **below**.
  - The later the forward start date, the farther the forward curve sits from the spot curve.
  - Forwards cannot extend beyond the longest spot maturity: with a 30-year curve, the 4-year-forward curve only reaches f₄,₂₆.
- **Forward contract price invariance**: if future discount functions equal today's forward discount functions, `DF_T^new = DF_{t+T}/DF_t`, then the forward price is unchanged: `F^new_{A−t,B−A} = F_{A,B−A}`.
  - Consequence: a forward's value changes **only** when realized spot rates deviate from today's forwards.
  - Realized spots **below** forwards → the forward price rises, so buy forwards (or bonds).
  - Realized spots **above** forwards → the forward price falls, so sell.
- **Active management decision rule (Eq. 11)**: `(1 + z_B)^B / (1 + f_{A,B−A})^{B−A} = (1 + z_A)^A`.
  - If the future curve equals today's forward curve, every bond earns the A-period spot rate over the horizon, whatever its maturity.
  - If your expected future spot rates are **below** the quoted forwards, the bond is **undervalued** to you: the market discounts at higher rates than you do. Buy or extend duration.
  - If your expected future spot rates are **above** the forwards, the bond is **overvalued** to you. Sell or shorten.
- **Rolling down (riding) the yield curve**:
  - When to use: the curve slopes upward and you expect it to stay **static** in level and shape over your horizon.
  - How: (1) choose a horizon H; (2) buy a bond with maturity longer than H; (3) at H, sell it at the lower yield of its shorter remaining maturity.
  - Return = coupons + reinvestment ± capital gain from the "roll".
  - Why it works: a static upward curve means each bond is revalued at successively lower yields, so it earns the forward rate that "rolls out" of its pricing. That forward is above the matched-maturity yield.
  - The gain grows with the forward–spot spread and with the bond's maturity (duration).
  - Failure mode: this is a duration bet. If rates rise faster than the forwards imply, it loses.
  - Its leveraged cousin is the **maturity spread carry trade**: borrow short, lend long in the same currency. It was popular after 2008 because of steep curves. Its risk is an unexpected rise in future spot rates, for example an inflation spike.
- **Bootstrapping** (forward substitution from par yields):
  - Treat each par bond as a portfolio of zeros priced at 1.
  - Solve for z₁, then z₂, and so on, from the **shortest to the longest** maturity. With annual coupons, z₁ equals the one-year par rate.
  - Trap: bootstrapping is *forward* substitution, from earliest to latest maturity, not backward.
- **Swap curve as a benchmark**: the swap rate s_T is the par rate of the swap curve. It makes the fixed leg worth 1 (the floating leg's value at inception): `Σ_{t=1..T} s_T/(1 + z_t)^t + 1/(1 + z_T)^T = 1`.
  - When to prefer swaps over government bonds:
    - the government market is illiquid or short, as in many emerging markets;
    - the private sector dwarfs the public sector;
    - the institution hedges its balance sheet with swaps (wholesale banks);
    - you need more maturity points (swaps run to 50 years in USD and EUR);
    - you need cross-country comparability (the market is dealer-led rather than government-controlled).
  - Retail banks with little swap exposure use the government curve instead.
  - Swaps are the benchmark of choice in Europe. In Asia, swap and government markets developed in parallel and both are used.
- **Traditional term-structure theories**: see the table below.
- **Three-factor yield curve model** (Litterman–Scheinkman, 1991):
  - Curve moves decompose into **level**, **steepness (slope)** and **curvature**, extracted from the variance–covariance matrix of rate changes.
  - Level explains most of the variance (more than 75%), steepness less, curvature least.
  - When to use: to hedge or position against **shaping risk**, which effective duration cannot see.
- **Key rate duration (KRD) framework**: `%ΔP ≈ −Σ KeyDur_k × Δz_k`, with `Σ KeyDur_k = effective duration`.
  - KRDs map linearly into factor durations once the factor shapes are defined.

## Key Concepts
- **Discount factor (DF_N)**: the price today of 1 paid at N. `DF_N = 1/(1 + z_N)^N`. The discount function and the spot curve contain the same information.
- **Spot rate (zero rate, z_N)**: the YTM of an option-free, default-free zero. It is the purest T-year rate because it carries no reinvestment assumption.
- **Forward rate f_{A,B−A}**: the rate agreed today for a loan starting at A with tenor B−A. **Forward price** F_{A,B−A} = DF_B/DF_A.
- **Par curve**: the YTMs of coupon government bonds priced at par, usually on-the-runs. It is the input to bootstrapping.
- **YTM**: a cash-flow-weighted average of the spot rates. It equals the realized return only if:
  - the bond is held to maturity;
  - there is no default;
  - all coupons are reinvested at the YTM, which in practice requires a flat, stable curve.
- **Realized return**: the actual holding-period return, driven by actual reinvestment rates and the curve at the horizon.
- **Swap spread**: the swap rate minus the on-the-run government yield of the same maturity. It reflects credit and liquidity and widens in recessions (countercyclical).
- **I-spread (ISPRD, interpolated spread)**: a bond's YTM minus the linearly interpolated swap rate of the same maturity.
- **Z-spread**: a constant spread over the government (or swap) *spot* curve that reprices the bond.
- **TED spread**: 3-month Libor minus the 3-month T-bill yield (T-bill "T" + Eurodollar futures ticker "ED"). A higher TED means more perceived bank credit and liquidity risk.
- **Libor–OIS spread**: Libor minus the OIS rate. OIS floats on the geometric average of an overnight index (fed funds, Eonia). It measures money-market risk and liquidity.
- **SOFR**: the secured overnight financing rate. It is a volume-weighted index of Treasury repo transactions and the successor to USD Libor. Other successors: ESTR replaces Eonia, CORRA replaces CDOR.
- **MRR**: market reference rate, the generic term for the post-Libor floating index.
- **Shaping risk**: price sensitivity to changes in the curve's *shape*, as opposed to its level.
- **Volatility term structure**: the annualized σ of proportional yield changes, by maturity. Short rates are usually the most volatile.
- **Bond (term, duration) risk premium**: the expected excess return of a long default-free bond over a short one or the one-period risk-free rate. It is *ex ante* and must be estimated.
- **Bear flattening, bull steepening, bull flattening**: the naming of curve moves combined with their direction (see Mental Models).
- **Bullet vs barbell**: a bullet concentrates in one maturity. A barbell of similar duration combines short and long maturities, so it has more convexity and profits from flattening.

## Formulas & Reference Tables
- `DF_N = 1/(1 + z_N)^N` and `z_N = (1/DF_N)^{1/N} − 1`
- `DF_B = DF_A × F_{A,B−A}` → `F_{A,B−A} = DF_B/DF_A`, and `DF_{A,B−A} = 1/(1 + f_{A,B−A})^{B−A}`
- Forward rate model: `f_{A,B−A} = [(1 + z_B)^B/(1 + z_A)^A]^{1/(B−A)} − 1`
- Equivalent form (Eq. 6): `1 + f_{A,B−A} = [(1 + z_B)/(1 + z_A)]^{A/(B−A)} × (1 + z_B)`. So f > z_B when z_B > z_A.
- Spot as geometric mean: `z_T = [(1 + z₁)(1 + f₁,₁)…(1 + f_{T−1,1})]^{1/T} − 1`
- Time-t discount function under "forwards realized": `DF_T^new = DF_{t+T}/DF_t`
- Swap rate from spot rates: `s_T = (1 − DF_T)/Σ_{t=1..T} DF_t`, which is the same as `Σ s_T·DF_t + DF_T = 1`
- Swap spread = `s_T − y_T^gov(on-the-run)`. The fixed payer's rate = the government yield + the swap spread.
- Bond return = coupons (and principal) + reinvestment of coupons ± capital gain or loss on sale before maturity.
- Volatility term structure (lognormal convention): `σ(t,T) = σ[Δr(t,T)/r(t,T)] / √Δt`
  - Example: a monthly σ of 10.15% gives 10.15% × √12 = 35.15% a year.
  - **⚠ Correction**: the extracted Eq. 13 is garbled. The correct form annualizes the standard deviation of *proportional* yield changes by dividing by √Δt, with Δt = 1/12 for monthly data.
- Key rate model: `%ΔP ≈ −KeyDur₁Δz₁ − KeyDur₅Δz₅ − KeyDur₁₀Δz₁₀`
- Factor model: `%ΔP ≈ −D_L·Δx_L − D_S·Δx_S − D_C·Δx_C`
  - With level = (1,1,1), steepness = (−1,0,+1) and curvature = (+1,0,+1) on the (1y, 5y, 10y) points:
  - `D_L = KRD₁ + KRD₅ + KRD₁₀`
  - `D_S = −KRD₁ + KRD₁₀`
  - `D_C = KRD₁ + KRD₁₀`

**Traditional term-structure theories**

| Theory | Core claim | Forward rate vs expected future spot | Typical curve implication | Risk attitude |
|---|---|---|---|---|
| Unbiased (pure) expectations | Forwards are unbiased predictors; all maturity strategies have the same expected return over any horizon | f = E[future spot] | Slope reflects expected rate path only | Risk-neutral |
| Local expectations | Expected return on **every** bond over a *short* period = risk-free rate (no-arbitrage); no restriction on long horizons | Unbiased locally only | Consistent with risk; applies to risky bonds too | Risk premiums ≈ 0 only for very short holding periods |
| Liquidity preference | Lenders demand a **liquidity (term) premium** that rises (weakly) with maturity | f = E[spot] + premium (**upward-biased** forecast) | Usually upward sloping; can still invert if steep expected rate cuts or deflation | Risk-averse |
| Segmented markets | Each maturity sector clears on its own supply/demand (ALM constraints: insurers/pensions long, MMFs short) | No link | Any shape; yields independent across sectors | Constrained participants |
| Preferred habitat | Participants prefer a sector but **will move** if the extra expected return is large enough | Expectations + institutional flows | Any shape; closest to reality (e.g., QE/MBS purchases lowered MBS yields) | Will accept risk for enough return |

Evidence the exam expects you to know:
- Short-holding-period returns on long bonds usually **exceed** those on short bonds, which contradicts local expectations.
- Forwards are **upward-biased** predictors of future spots, which is consistent with liquidity premiums.

**Macro drivers of rates and curve shape**

| Driver | Effect |
|---|---|
| Inflation | Explains about ⅔ of short- and intermediate-yield variation |
| Monetary policy | Explains about ⅔ of long-yield variation. Hikes in expansions tend to cause **bear flattening**; cuts in (expected) recessions tend to cause **bull steepening** |
| QE / asset purchases | Lower the bond risk premium in the maturity segments bought. Tapering raises long yields and steepens |
| Fiscal deficits | Higher deficits → more supply → higher yields (late-1990s surplus expectations lowered long Treasury yields) |
| Longer debt maturity structure | Predicts greater excess returns at the long end (a segmentation effect) |
| Domestic demand (pensions, insurers) | Raises prices and lowers the term premium |
| Foreign flows (reserves, FX management) | Inflows lower the term premium; outflows raise it |
| Flight to quality | **Bull flattening**: long yields fall more than short yields |

## Mental Models
- **Forwards are the "zero-alpha path".** Every rate view must be stated *relative to forwards*, not relative to today's spot curve.
  - "Rates will stay unchanged" is itself a view: it means realized spots will be below forwards on an upward curve, which is bullish.
  - "Rates will rise" is only bearish if they rise by *more* than the forwards imply.
- **Think of spot rates as averages and forwards as marginal rates.** When an average rises, the marginal value must be above it. This one idea gives all the spot/forward/par ordering rules. On an upward curve: forward > spot > par (YTM).
- **Use key rate or factor durations whenever the curve can twist.** Effective duration assumes parallel shifts, and level explains most (not all) of the variance. Steepeners, flatteners and barbell-versus-bullet trades are pure shaping-risk bets and should be built duration-neutral.
- **Choose the benchmark by who you are and what you hedge with.** Swap-hedged dealers value off swaps. Government-funded retail balance sheets value off the government curve. In a thin government market, swaps are the only reliable curve.
- **Read the funding spreads as a stress gauge.** Rising TED or Libor–OIS means banks distrust each other (2008, March 2020). Negative long swap spreads since 2008 reflect dealer balance-sheet costs, not a riskless private sector.

## Worked Example
**A. From spots to forwards, YTM and expected return.** Spot rates: z₁ = 9%, z₂ = 10%, z₃ = 11%.
- f₁,₁ = 1.10²/1.09 − 1 = **11.01%**.
- f₂,₁ = 1.11³/1.10² − 1 = **13.03%**.
- f₁,₂ = (1.11³/1.09)^{1/2} − 1 = **12.01%**, which is above z₃ = 11% because the curve slopes upward.
- If next year's curve equals today's forward curve, each zero earns exactly 9% over the year:
  - 1-year zero: 91.74 → 100.
  - 2-year zero: 82.64 → 100/1.1101 = 90.08.
  - 3-year zero: 73.12 → 100/1.1201² = 79.71.
- If instead the curve becomes flat at 10%, the one-year holding returns are 9%, 10% and 13.03%. The long bond wins because its realized spot (10%) is below its forward (12.01%).

**B. Bootstrapping, then back to swap rates** (verified in Python).
- Par rates of 5%, 5.97%, 6.91% and 7.81% bootstrap to z = 5%, 6%, 7%, 8%.
- Going the other way, DF = 0.9524, 0.8900, 0.8163, 0.7350 and `s_T = (1 − DF_T)/ΣDF_t` give swap rates of 5.00%, 5.97%, 6.91%, 7.81%.
- The swap curve *is* a par curve.

**C. YTM is not the expected return.** Spots of 5–9% (years 1–5). Take a 5-year 10% annual bond.
- Price = 105.43 and YTM = 8.62%.
- Implied one-year forwards: 7.01%, 9.03%, 11.06%, 13.09%.
- Reinvest each coupon at these forwards: the terminal value is 162.22.
- Annualized return = (162.22/105.43)^{1/5} − 1 = **9.00%**, which differs from the 8.62% YTM.
- ⚠ The source's expression has a typo (1 + 0.011 in place of 1 + 0.111). Its total of 162.22 is correct.

**D. Rolling down: maturity-matched vs ride.** Par yields: 1y 2%, 3y 4%, 4y 5%, 5y 6%, 6y 7%. Horizon: 2 years. The curve is assumed static.
- Matched: buy the 5-year 6% bond at 100.
  - After 2 years it is a 3-year bond priced at 4%: 6/1.04 + 6/1.04² + 106/1.04³ = **105.55**.
  - Terminal value = 6 × 1.02 + 6 + 105.55 = 117.67, an annualized return of **8.48%**.
- Ride: buy the 6-year 7% bond at 100.
  - After 2 years it is a 4-year bond priced at 5%: **107.09**.
  - Terminal value = 7 × 1.02 + 7 + 107.09 = 121.23, an annualized return of **10.11%**.
- The roll adds about 1.6% a year.
- **⚠ Correction**: the curriculum prices the sale at 3% (3-year) and 4% (4-year), which gives 108.49 and 110.89 and returns of 9.82% and 11.82%. Those yields contradict its own stated curve. The figures above are recomputed with the stated 4% and 5%. The conclusion (the ride beats the matched bond by about 2%) holds either way.

**E. Factor durations.** A portfolio holds $100 each in 1-, 5- and 10-year zeros.
- KRD₁ = 1/3 = 0.3333, KRD₅ = 1.6667, KRD₁₀ = 3.3333. They sum to the effective duration of 5.3333.
- Factor durations: D_L = 5.3333, D_S = −0.3333 + 3.3333 = 3.0, D_C = 0.3333 + 3.3333 = 3.6667.
- Scenario: Δx_L = −50bp, Δx_S = +20bp, Δx_C = +10bp.
- %ΔP = −5.3333(−0.005) − 3.0(0.002) − 3.6667(0.001) = **+1.70%**.

## Anti-patterns
- **Treating the YTM as the expected return on a sloped curve**: the YTM assumes reinvestment at itself. With a sloped curve, volatile rates, default risk or embedded options, the realized return differs.
- **Calling "unchanged rates" a neutral view**: on an upward curve it is a bullish bet against the forwards.
- **Using effective duration to hedge a barbell-versus-bullet or a steepener**: it is blind to slope and curvature. Use KRDs or factor durations.
- **Bootstrapping backward** (long to short) or bootstrapping from non-par, off-the-run, illiquid yields.
- **Reading a negative swap spread as "government riskier than banks"**: since 2008 it has mostly reflected dealer capital and leverage constraints, demand for duration and liquidity.
- **Confusing the liquidity premium of liquidity preference theory with an illiquidity premium**: the former applies to *all* long bonds, including the most liquid on-the-runs.
- **Running a maturity spread carry trade with no stop on inflation risk**: an unexpected jump in spot rates wipes out the carry.

## Exam Focus & Traps
- **Upward spot curve → forward curve above spot curve.** Later start dates move the forward curve farther away from the spot curve: farther above for an upward curve, farther below for a downward curve.
- **Flat curve → all forwards equal the spot rate.**
- **Ordering on an upward curve**: z₁ < y_T < z_T. The YTM sits closest to the spot rate of the largest cash flow (the maturity).
- **Undervalued vs overvalued**: expected spot **below** forward → bond undervalued → buy. The exam flips the wording, so read carefully.
- **Forward price rises only if realized spots are below the forwards.** If spots evolve exactly as the forwards predicted, the forward price does not change.
- **Rolling down**: buy a maturity **longer** than your horizon. It requires an upward-sloping *and* stable curve.
- **Swap spread** = swap rate − government yield (e.g., 2.00% − 1.70% = 30bp). The fixed payer's rate = the Treasury yield + the swap spread. **I-spread** = bond YTM − swap rate. Do not mix them up.
- **Z-spread** is the right spread for pricing a risky bond off a government zero curve. TED and Libor–OIS measure system-wide risk and do not price individual bonds.
- **TED rises** if T-bill yields fall while Libor is unchanged (flight to quality).
- **Theory identification**:
  - "Risk premiums increase with maturity" → liquidity preference.
  - "Investors can be induced out of their maturity" → preferred habitat.
  - Fallen angels forced out of IG-only mandates → segmented markets.
  - "Short-horizon return = risk-free for every bond" → local expectations.
  - Unbiased expectations = risk neutrality.
- **Factor tables**: entries give Δyield per 1σ of the factor. Scale linearly: a 2σ steepness move = 2 × the entry. A *decrease* in a factor flips the sign of that factor's entry.
- **KRD sum = effective duration.** Under a parallel −50bp shift, %ΔP = −(ΣKRD)(−0.005).
- **Curve-move vocabulary**:
  - Bear flattening: short yields rise more (tightening in an expansion).
  - Bull steepening: short yields fall more (easing into a recession).
  - Bull flattening: long yields fall more (flight to quality). A bullet-to-barbell shift profits from it.

## Key Takeaways
1. Use `DF_B = DF_A·F_{A,B−A}`, or `(1+z_B)^B = (1+z_A)^A(1+f)^{B−A}`, to go between spots and forwards. Forwards are marginal rates, spots are averages.
2. If forwards are realized, every bond earns the one-period rate. Every active return comes from realized spots deviating from forwards.
3. Buy (extend) when your expected spots are below the forwards. Ride the curve only if it is upward sloping and you expect it to stay put.
4. The swap curve is a par curve built from MRR-linked swaps. Prefer it where the government market is thin, or where you hedge with swaps.
5. Swap spread = swap rate − government yield (credit and liquidity; countercyclical). TED and Libor–OIS are stress gauges. SOFR is the new secured benchmark.
6. Liquidity premiums make forwards upward-biased forecasts. Preferred habitat best explains QE-type supply effects.
7. Level, slope and curvature explain curve moves, with level dominant. Manage shaping risk with KRDs (which sum to the effective duration) or factor durations.
8. Short rates are the most volatile, mainly because of monetary policy. Long-rate volatility tracks growth and inflation uncertainty.

## Connects To
- **ch03**: L1 spot, par and forward basics, and bootstrapping foundations.
- **ch05**: effective duration, convexity and duration versus horizon, which are needed to read KRDs.
- **ch08**: the arbitrage-free framework turns this spot/forward curve into a calibrated binomial tree.
- **ch09**: effective and key rate durations of bonds with embedded options. Volatility drives option value.
- **ch11**: CDS pricing uses the swap/MRR curve as the discount benchmark.
- **ch14**: yield-curve strategies (bullet vs barbell, rolldown, carry, curve trades) at L3.
- **`tuckman-fixed-income` ch02**: spot, forward and par rates in continuous and discrete form. **ch03**: returns and spreads. **ch05**: key rate and multi-factor hedging. **ch16**: swaps. **ch21**: curve construction.
- **`ilmanen-yield-curve` ch01–ch03**: what forwards imply, the bond risk premium, and rolldown/carry versus the expectations hypothesis.
- **`hull-derivatives` ch04**: interest rates (zero rates, forwards, bootstrapping). **ch07**: swaps (OIS, swap valuation).
- **`cfa-economics` ch05**: the monetary policy transmission behind bear flattening and bull steepening.
