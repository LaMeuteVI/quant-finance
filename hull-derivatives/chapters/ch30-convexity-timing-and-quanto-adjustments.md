# Chapter 30: Convexity, Timing, and Quanto Adjustments

## Core Idea
The two-step shortcut is: (1) set the expected value of each variable equal to its forward value, (2) discount at today's rate for the payment date. It is only correct when the payoff is measured in the numeraire that makes that variable a martingale. There are three standard fixes:
- **Convexity adjustment**: the payoff depends on a *yield or swap rate*, not a price.
- **Timing adjustment**: the variable is observed at T but paid at T*.
- **Quanto adjustment**: the variable is observed in one currency but paid in another.

## Frameworks Introduced
- **Convexity adjustment (bond yield or swap rate observed at T)**:
  - `E_T(y_T) = y₀ − ½·y₀²σ_y²T·G″(y₀)/G′(y₀)`.
  - G(y) is the bond price as a function of its yield, and G′ < 0, so the expected yield is **above** the forward yield.
  - For swap rates, treat the swap rate as the yield of a par bond with coupon = the forward swap rate.
- **Timing adjustment (observe at T, pay at T*)**:
  - `E_{T*}(V_T) = E_T(V_T)·exp[−ρ_VR·σ_V·σ_R·R₀·(T* − T)·T/(1 + R₀/m)]`.
  - R is the forward rate for (T, T*), and ρ is its correlation with V.
  - For V = the interest rate itself, this simplifies to `F·[1 − ...]`: a LIBOR/SOFR-in-arrears style adjustment.
- **Quanto adjustment (observe V in currency Y, pay in X)**:
  - `E_X(V_T) = E_Y(V_T)·e^{ρ_VW·σ_V·σ_W·T}`.
  - W is the forward exchange rate: units of Y per unit of X.
- **General principle (Ch 28)**: switching numeraire shifts the drift by ρσ_v(σ_new − σ_old). Every adjustment is an instance of this.
- **Siegel's paradox**: if X/Y follows GBM, then Y/X also does, but E[Y/X] ≠ 1/E[X/Y]. Forward FX rates cannot be unbiased predictors in both currencies (Jensen's inequality).

## Key Concepts
- **Constant maturity swap (CMS)**: pays a swap rate observed at T. It requires a convexity adjustment.
- **Rates in arrears**: the rate is observed and paid at the same time, rather than paid one period later. It requires a timing adjustment.
- **Quanto (cross-currency) derivative**: e.g., a Nikkei future paid in USD (CME Nikkei 225 contract).
- **Diff swap**: the floating rate of one currency is applied to a principal in another currency. It is quanto-adjusted.

## Mental Models
- Ask: **"In which numeraire is the payoff naturally expressed?"** If the variable is not a martingale under the measure of the payment date and currency, the variable needs adjusting.
- **Convexity always pushes the expected yield up**, because bond prices are convex in yields.
- **The quanto sign follows the correlation**: if the asset rises when currency Y weakens against X, the adjustment is negative.

## Anti-patterns
- **Valuing CMS swaps as if the forward swap rate were the expected rate**: this misprices long-dated CMS by basis points.
- **Ignoring the quanto effect on cross-currency index products**.
- **Using a futures rate as a forward rate** without the separate futures/forward convexity adjustment of Ch 6.

## Worked Example
**CMS convexity (Example 30.1).**
- Payoff: in 3 years, receive 100 × the 3-year swap rate at that time.
- Inputs: swap rates flat at 6% (annual), swap-rate volatility 22%, 3-year zero rate 5%.
- With G(y) for a 6% bond: G′(0.06) = −2.6730 and G″(0.06) = 9.8910.
- E(y) = 0.06 + ½ × 0.06² × 0.22² × 3 × 9.8910/2.6730 = **6.097%**.
- Value = 100 × 0.06097/1.05³ = **$5.27** (it would be $5.18 without the adjustment).

**Quanto Nikkei (Example 30.3).**
- Inputs: Nikkei = ¥15,000, yen rate 2%, dollar rate 5%, dividend yield 1%.
- The yen forward price is 15,000e^{0.01} = 15,150.75.
- With σ_V = 20%, σ_W = 12% and ρ = 0.3, the expected value for a USD payoff = 15,150.75e^{0.3 × 0.2 × 0.12} = **15,260.23**.

## Key Takeaways
1. "Expected = forward" holds only under the measure of the payment date and currency.
2. Yields and swap rates paid at T need a positive convexity adjustment ∝ y²σ²T·G″/G′.
3. Payment at T* ≠ T needs a timing adjustment, driven by the correlation with the T→T* rate.
4. Cross-currency payoffs need a quanto factor e^{ρσ_Vσ_W T}.
5. All three are numeraire-change drift corrections.

## Connects To
- **Ch 6**: futures/forward convexity.
- **Ch 28**: the change-of-numeraire formula.
- **Ch 29**: the vanilla standard models where no adjustment is needed.
- **Ch 34**: CMS, compounding swaps, diff swaps.
- **Ch 5**: the CME Nikkei futures anomaly.
