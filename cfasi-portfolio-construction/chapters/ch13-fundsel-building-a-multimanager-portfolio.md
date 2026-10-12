# Chapter 13: Building a Multimanager Portfolio: A Possible Solution (Costruire un portafoglio multimanager)
> **Source**: CFA Society Italy x Advisor Private, "ETF & Fund Selection" guide (Advisor Private no. 16, 2019), Chapter 5 | Denis Manzi, CFA, CIPM; builds on Waring, Whitney, Pirone and Castille (2000), Waring and Siegel (2003), Scott D. Stewart (2013)

## Core Idea
A multimanager structure of passive and active funds can be built like any portfolio of traditional securities: as a mean-variance optimization, but over **managers** and in **active-risk space**. Take the strategic asset allocation as given, treat each manager as a security whose expected return is its pure alpha, and find the manager mix with the lowest active risk for each level of alpha. The index fund sits at the origin (zero alpha, zero active risk). The investor then picks a point on the efficient frontier according to appetite for active risk.

## Frameworks Introduced
- **Decomposition of manager performance (Waring et al.)**:
  - **Active return** = manager return minus declared benchmark. Often wrongly called alpha. Caused by different market or multi-factor exposure from the benchmark. Passive funds: approximately zero.
  - **Pure active return (alpha)** = return beyond what could be obtained by buying index funds that replicate the manager's persistent style. Computed by regression to find the manager's **natural benchmark** (best-fit index).
  - **Total active risk** = standard deviation of (manager minus declared benchmark).
  - **Misfit risk** = standard deviation of (natural benchmark minus declared benchmark): the risk of a style mismatch; one manager's misfit can be offset by another (value tilt vs growth tilt).
  - **Pure active risk** = standard deviation of (manager minus natural benchmark) = risk of the alpha itself. Not rewarded on average even before fees (zero-sum game).
  - Examples: manager +5%, S&P 500 +4% gives active return 1%; with best-fit index S&P 500 Value +5%, pure active return = 0.
- **Pure Information Ratio (Waring-Siegel)**: for one manager `PIR = pure active return / pure active risk`; for N managers `PIR = sum(pure active returns) / sqrt(sum(pure active risks^2) + net misfit risk^2)` (the source says "sum of risks", with zero alpha correlation; the usual statistically consistent version combines risks in quadrature). Compare managers and manager portfolios without distortion from style exposures. Prefer higher PIR. Active selection must deliver positive pure alpha at acceptable pure active risk.
- **Multimanager optimization procedure**:
  1. Fix the SAA at asset-class level (assumes done); this chapter only covers the implementation with external managers. Complexity of the class raises manager-selection difficulty (private equity vs US large-cap equity).
  2. Treat each manager like a stock or bond; optimize allocations among managers by Markowitz in the (active risk, alpha) space: for each level of expected alpha, minimize active risk. Origin = index funds.
  3. Inputs: (1) each manager's expected pure alpha and pure active risk; (2) expected correlation between managers' alphas (can be assumed zero); (3) betas to risk factors of each manager's natural benchmark; (4) expected return, risk and correlation of those factors. If no misfit risk is assumed, (3) and (4) drop out.
  4. Choose the point on the frontier by active-risk aversion: strong aversion means mostly index and enhanced index funds; higher tolerance means more weight in active managers.
  - Observations: the alpha estimate is decisive; if you cannot estimate it, you should not hold an active manager. Anyone holding an active fund has implicitly forecast its alpha (reverse optimization can reveal it). Do not rely only on past performance, especially if past alpha was not statistically significant. Alpha correlations across managers can be assumed zero.
  - Tools: Excel Solver suffices; retains the limits of mean-variance (inputs, instability).
- **Illustration (Waring-Siegel Figure)**: as active-risk appetite rises, weights shift: no risk: index 100%; moderate: index 44, risk-controlled 33, Active 1 10, Active 2 10, Active 3 3; higher risk: index 0, risk-controlled 39, Active 1 26, Active 2 26, Active 3 9.
- **Worked case in the source**: three vehicles for US equity with zero alpha correlation: ETF (alpha 0, active risk 0), enhanced index fund (alpha 2, active risk 1), active fund (alpha 4, active risk 1.5). Portfolio 50% ETF / 25% enhanced / 25% active: alpha = 0.5x0 + 0.25x2 + 0.25x4 = 1.5; active risk = sqrt((0.25x1)^2 + (0.25x1.5)^2) = 0.45 (the source leaves the risk calculation implicit). Figure 2 of the source labels frontier points ETF 100%, ETF 28%/enhanced 72%, and active 100%.
- **Fee interplay**: link to FAR in ch10: fees must be set against pure active risk, and portfolios of many managers pay fees on offsetting active bets.

## Key Concepts
- **Declared vs natural benchmark**: stated index vs best-fit style index from regression.
- **Active return / pure active return**: vs declared benchmark / vs natural benchmark.
- **Total / misfit / pure active risk**: three risk layers.
- **Pure information ratio**: pure alpha per unit of pure active risk.
- **Enhanced (risk-controlled) index fund**: low-tracking-error semi-active fund.
- **Efficient frontier of managers**: min active risk per expected alpha.
- **Reverse optimization**: infer the alpha implied by current holdings.
- **Active-risk budget**: total tracking error accepted by the investor.
- **Manager risk**: risk of selecting a manager that fails.

## Formulas & Reference Tables
- `Active return = R_manager - R_declared benchmark`.
- `Pure active return = R_manager - R_natural benchmark` (natural benchmark = style regression fit).
- `Total active risk = std(R_manager - R_declared)`; `Misfit risk = std(R_natural - R_declared)`; `Pure active risk = std(R_manager - R_natural)`.
- `PIR (single) = pure alpha / pure active risk`.
- Portfolio of managers (zero alpha correlations): `alpha_p = sum(w_i alpha_i)`; `active risk_p = sqrt(sum(w_i^2 sigma_i^2))` (pure risks, no misfit).
- Source example values: total active risk of manager returns (3%, 6%, 4%) vs benchmark (4%, 3%, 3%): differences -1, +3, +1, standard deviation 2 (sample, verified). Misfit risk with natural benchmark (4%, 5%, 3%) vs declared (3%, 6%, 4%): differences -1, +1, +1, standard deviation 1.15 (verified). Pure information ratios: manager A passive (0, 0, n/a), B (-1, 2, -0.5), C (3, 2, 1.5).
- **⚠ Note**: in the source's three-vehicle example the frontier is not made of ETF/enhanced pairs only. Recomputation with zero correlations gives, for alpha 1.44, a minimum active risk of 0.43 using about 51% ETF, 26% enhanced, 23% active, compared with 0.72 for the 28/72 ETF/enhanced mix, because the active fund has the highest alpha per unit of risk (4/1.5 = 2.67 vs 2.0). The optimum stays on a straight line through the origin (alpha / active risk = 3.33) until the ETF weight is exhausted: min active risk is 0.15, 0.30, 0.43, 0.60 for alphas 0.5, 1.0, 1.44, 2.0; at alpha 3.0 (50% enhanced / 50% active) it is 0.90.

| Target alpha | Min active risk | Mix ETF / enhanced / active |
|---|---|---|
| 0.5 | 0.15 | 83 / 9 / 8 |
| 1.0 | 0.30 | 66 / 18 / 16 |
| 1.44 | 0.43 | 51 / 26 / 23 |
| 2.0 | 0.60 | 32 / 36 / 32 |
| 3.0 | 0.90 | 0 / 50 / 50 |

## Mental Models
- Use pure alpha, not raw active return, to evaluate managers: strip out style exposures you could buy cheaply.
- Use the frontier in (active risk, alpha) space to translate risk aversion into weights.
- Use index funds as the zero-risk anchor of every multimanager portfolio.
- Use misfit risk deliberately: offsetting value and growth managers diversify style, not alpha.
- Use reverse optimization to see which alphas your current holdings assume.
- If you cannot defend an alpha forecast, hold the index.

## Worked Example
Pure information ratio and mix. Inputs: manager B pure alpha -1, pure active risk 2; manager C alpha +3, risk 2; index A (0, 0). Steps: PIR B = -1/2 = -0.5; PIR C = 3/2 = 1.5. Two-manager portfolio 50% C / 50% index: alpha 1.5, pure active risk 0.5 x 2 = 1.0, PIR 1.5. Adding 25% B reduces alpha: 0.25 x (-1) + 0.5 x 3 = 1.25 with active risk sqrt((0.5x2)^2 + (0.25x2)^2) = 1.12, PIR 1.12. Interpretation: adding a negative-alpha manager lowers the portfolio PIR; only positive-PIR managers belong, with weights set by risk budget.

## Anti-patterns
- Calling active return alpha without regression on the natural benchmark.
- Equal-weighting managers regardless of alpha/risk.
- Hiring many managers with offsetting active bets (diversifying away the alpha while paying all fees).
- Using historical returns as expected alphas without testing significance.
- Ignoring that mean-variance optimization amplifies input errors.
- Starting from managers rather than from the SAA classes.

## Practitioner Notes
- Document the alpha forecast for each manager and update it only on evidence (see ch14).
- Use constraints (min/max weights, max tracking error per sleeve) to stabilize the optimizer.
- Check overlaps (hidden factor exposures) across managers via the natural benchmark betas.
- Keep an index-fund sleeve in each class as the risk-free-in-active-terms option.
- Fees: put net-of-fee alpha into the optimizer.

## Key Takeaways
- Build a multimanager portfolio as an optimization over managers, in active-risk and alpha space.
- Separate active return, pure alpha, total, misfit and pure active risk.
- Pure information ratio ranks managers and portfolios without style distortions.
- The alpha forecast is the key input; if you cannot form one, use passive.
- Risk aversion to active risk sets the mix between index/enhanced and active managers.
- With uncorrelated alphas, the best mixes weigh managers by alpha/risk: recompute rather than eyeballing frontier labels.

## Connects To
- **ch09-ch10**: why managers, FAR and overdiversification.
- **ch11**: selection framework.
- **ch12**: passive manager choice (the zero-alpha anchor).
- **ch14**: how Pramerica builds portfolios of selected funds (Z-score, plateau optimization).
- **ch02-ch03**: Black-Litterman, risk budgeting, mean-variance.
- **`cfa-asset-allocation-cme` ch07**: optimizer inputs and asset allocation principles.
- **`cfa-portfolio-management` ch15, ch19**: active management analysis, information ratio, manager selection.
