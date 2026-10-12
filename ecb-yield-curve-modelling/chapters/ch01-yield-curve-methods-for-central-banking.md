# Chapter 1: Yield Curve Methods for Central Banking Purposes
> **Source**: Nymand-Andersen, ECB Statistics Paper No 27 (Feb 2018), Abstract, §1 Non-technical summary, §2 Introduction, §3 (opening) | Per Nymand-Andersen

## Core Idea
A central bank needs one representative, near-risk-free term structure (spot, forward, par) extracted from noisy coupon-bond prices, because the curve is read as market expectations of policy rates, growth and inflation. Since zero-coupon bonds are scarce beyond 12 months, the curve must be estimated by imposing a functional form or a spline, and the choice of method is a trade-off between flexibility (capturing genuine bends) and smoothness (not fitting noise). The paper's twin message: estimate on a cleaned, high-quality bond sample first, then choose a model by explicit statistical tests.

## Frameworks Introduced
- **Why a central bank estimates a yield curve**: to read the path of expected short rates, the growth outlook and trend inflation at short, medium and long horizons.
  - When to use: monetary-policy analysis, financial-stability and market-operations work, derivation of real rates and break-even inflation.
  - How: estimate a nominal AAA-related government curve; subtract it from a comparable inflation-linked curve to get break-even inflation; use the slope as an activity indicator (steepening often anticipates acceleration, flattening or inversion a slowdown).
  - Failure mode: Bund (AAA) yields are only a proxy for risk-free; euro area sovereign spreads contain credit risk, so the sample must be credit-homogeneous.
- **Four term-structure theories** (how to read slope):
  - **Liquidity preference**: risk-averse investors demand a term premium, so the curve slopes up all else equal.
  - **Pure expectations hypothesis**: forwards equal expected future spot rates, no premia; the average expected short rate over the horizon equals the long rate. Empirically it overstates future short rates, because a fluctuating risk premium remains.
  - **Segmented markets**: supply and demand in each maturity sector set its yield, sectors only loosely connected.
  - **Preferred habitat**: a segmented-markets cousin; investors move out of their maturity habitat only if compensated enough.
  - Practitioner stance: the expectations hypothesis is "a reasonable starting point"; premia are small and stable at short horizons in normal markets.
- **Two families of estimation methods** (Anderson et al. 1996):
  1. Models with assumptions on state-variable dynamics plus equilibrium or no-arbitrage pricing.
  2. Statistical "smoothing" techniques fitted to observed prices (spline-based and parsimonious parametric). This paper only tests family 2.
- **Shock decomposition**: level (parallel move), slope (short and long end move disproportionately), curvature (mainly the medium-term rates; curve becomes more hump-shaped).

## Key Concepts
- **Yield curve**: term structure of interest rates of default-free zero-coupon bonds, plotted against residual maturity.
- **Yield-to-maturity (YTM)**: the single discount rate that equates the PV of all cash flows to the price; for a zero-coupon bond it equals its spot rate.
- **Spot (zero-coupon) rate** s(t,m): discount rate for a single cash flow at maturity m.
- **Instantaneous forward rate** f(t): the marginal rate for a very short loan starting t years ahead; the object the parametric models specify directly.
- **Par yield curve**: coupon rate at which a bond prices at par, derived from the spot curve.
- **Residual maturity**: time left to redemption (the x-axis throughout the paper).
- **Smoothing**: removing noise from observed prices; trade-off against fit.
- **Flexibility**: ability of the estimated curve to follow genuine bends, especially at the short end.
- **Parsimonious model**: few parameters, but able to produce monotonic, humped and S-shaped curves (Nelson-Siegel 1987).
- **Spline**: piecewise polynomial joined smoothly at knot points (see ch02).
- **Break-even inflation**: nominal curve minus comparable inflation-linked (real) curve.
- **ESCB**: European System of Central Banks; its Task Force on Financial Market Statistics supplied the empirical work.
- **Credit-risk-free proxy**: AAA-rated central-government bonds, in practice the Bund curve.

## Formulas & Reference Tables
- Price of a coupon bond with known spot rates (source notation):
  `P_t = Σ_{m=1..M} C / (1 + s_{t,m})^m + N / (1 + s_{t,M})^M`
  C = coupon, N = redemption value, s_{t,m} = spot rate at maturity m, M = final maturity.
- **YTM**: y solves `P_t = Σ C/(1+y)^m + N/(1+y)^M`.
- Why functional form: with n bonds and a full spot vector unknown (more unknowns than prices), an imposed form f(m; parameters) turns it into an iterative fit of few parameters.

| Theory | Driver of slope | Implication for reading the curve |
|---|---|---|
| Liquidity preference | Term premium | Upward slope even with flat expected rates |
| Pure expectations | Expected future short rates only | Slope maps to expected rate path |
| Segmented markets | Sector supply and demand | Curve can have local distortions |
| Preferred habitat | Demand plus compensation to leave habitat | Premia vary with supply of duration |

| Curve shape | Typical reading |
|---|---|
| Normal (upward) | Term premium, expected growth and rate rises |
| Flat | Transition |
| Inverted | Often precedes slowdown |

## Mental Models
- **Curve as expectations plus premium**: read forwards as "expected short rate + risk premium"; do not treat them as pure forecasts (expectations hypothesis overstates future short rates).
- **Fit versus smooth is a dial, not a choice of right answer**: the final use of the curve sets the optimal setting (policy indicator: smoother; relative-value trading: more flexible).
- **Garbage in, curve out**: changes in the estimated curve should reflect changes in yields, not changes in the composition of the bond sample.
- **Zero-coupon scarcity forces modelling**: euro area bonds beyond 12 months are almost all coupon bonds, so spot rates are inferred, never observed.

## Worked Example
Break-even inflation from two curves (illustrative, my numbers): 10-year nominal spot 4.12%, 10-year real (inflation-linked) spot 1.90%.
Break-even ≈ 4.12% − 1.90% = 2.22% (Fisher, before inflation-risk premium and liquidity effects).
Interpretation: the market prices roughly 2.2% average annual inflation over ten years, plus unobserved premia; only a consistent method on both curves makes the difference meaningful.

## Anti-patterns
- **Reading a forward rate as a forecast**: ignores time-varying risk premia.
- **Estimating a curve from a sample whose composition changes day to day**: moves in the curve then come from the data, not from yields.
- **Choosing the model before the use case**: the paper stresses that final use drives the smoothness-fit trade-off.
- **Treating Bund yields as credit-free for all purposes**: sovereign spreads contain credit risk.

## Practitioner Notes
- The ECB curve is used for policy signalling, transparency (daily public release), and as input to financial stability, integration and market-operations analysis.
- National central banks began producing curves in the early 1990s (one from 1972); Nelson-Siegel and Svensson dominate inside the euro area, spline models (Waggoner variants) at the BoE, NY Fed, BoJ, BoC.
- Post-crisis demands: national curves next to the euro area curve and behaviour near zero rates (outside scope; cites Krippner 2015).
- The paper's data: two years of daily euro area government bond prices (1 April 2003 to 31 March 2005, 502 trading days).

## Key Takeaways
1. A yield curve is an estimate, not an observation: coupon bonds must be unbundled using a functional form or spline.
2. Use the curve for level, slope and curvature, and for implied forwards as market expectations, with a premium caveat.
3. The curve should be near risk-free, credit-homogeneous and stable in composition.
4. Two model families are compared: spline-based (flexible, many parameters) and parsimonious (few parameters, interpretable).
5. The smoothness versus flexibility trade-off is dictated by the intended use.
6. Data quality comes before model choice (ch05).
7. Nominal curve plus inflation-linked curve gives real rates and break-evens.

## Connects To
- **ch02**: spline-based methods; **ch03**: Nelson-Siegel and Svensson.
- **ch05**: bond sample selection; **ch08**: why the ECB chose Svensson.
- **`tuckman-fixed-income` ch21**: curve construction (spot, forward, par relationships and fitting).
- **`cfa-fixed-income` ch07**: term structure theories, spot, forward, par.
- **`hull-derivatives` ch4**: interest rates, zero rates and forward rates.
- **`ilmanen-yield-curve`**: expectations, term premium and curve-shape drivers.
