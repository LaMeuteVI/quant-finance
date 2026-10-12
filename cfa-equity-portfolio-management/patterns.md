# Patterns — Equity Portfolio Management Recipes

## Choose a Benchmark for a Passive Mandate
**When to use**: setting or auditing a passive/indexed equity allocation.
**How**:
1. Test it is rules-based, transparent, investable (float, liquidity, replicable).
2. Pick segment, cap range and style from the IPS; note factor exposures.
3. Choose weighting (float-cap default; equal, fundamental, min-variance, multi-factor are factor bets).
4. Compute `HHI = Σw²`, effective N = 1/HHI; check reconstitution/rebalance rules, buffering/packeting.
**Trade-offs**: cap weight is cheap with high capacity but concentrated (NASDAQ 100 ≈ 25 effective stocks); alternatives cost more and crowd (ch 02).

## Select the Index-Tracking Construction Method
**When to use**: building a passive portfolio stock by stock.
**How**: liquid, small or homogeneous index and big mandate → full replication. Many constituents or small AUM → stratified sampling (sector/country strata, proportional weights). Need minimum TE with an N-stock cap → optimization (add total-volatility constraint, rerun often). Cap-spanning index → blended: replicate the liquid ~1,000, sample the tail.
**Trade-offs**: TE vs trading cost is U-shaped in holdings; optimization uses past covariances (ch 02).

## Control Tracking Error
**When to use**: running an index fund.
**How**: (1) trade at market-on-close; (2) net inflows against redemptions; (3) equitize cash and accrued dividends with futures or ETFs; (4) keep beta 1.0 and factor exposures near index; (5) minimise fees, commissions, market impact; (6) explain residual with attribution.
**Trade-offs**: futures bring roll, margin and basis risk (ch 02).

## Equity Index Futures Overlay Sizing
**When to use**: equitize cash, rebalance to policy, or adjust beta tactically.
**How**: contracts = (exposure to hedge or add) / (multiplier × futures price), round. Margin call trigger = initial − maintenance margin, converted to index points by dividing by multiplier. P&L = multiplier × Δ price.
**Trade-offs**: leverage amplifies margin calls (a 0.98% index fall cut margin 20.9% in the ASX example); derivatives expire, so use cash for permanent exposure (ch 02).

## Equity Swap Settlement
**When to use**: synthetic index exposure for any index, with tax deferral.
**How**: receive N × index return; pay N × (Libor + spread) × days/360; net the two each period.
**Trade-offs**: counterparty, liquidity, interest-rate and tax-policy risk (ch 02).

## Sector Return Attribution (Passive Check)
**When to use**: explaining tracking error and sources of return.
**How**: contribution = weight × sector return for portfolio (C) and benchmark (E); difference F = C − E by sector; tie the total to the portfolio-minus-benchmark gap.
**Trade-offs**: ex post only; groupings (sector, country, factor) must fit the mandate (ch 02).

## Securities Lending Programme
**When to use**: offset costs of a long-term holder (index funds are preferred lenders).
**How**: set lender authorization with an agent; borrower posts 102-105% collateral; invest cash collateral only in low-risk money-market paper; rebate to borrower; recall shares before key votes.
**Trade-offs**: collateral reinvestment, borrower credit, liquidity and operational risk; fee splits with agent; lost votes (ch 01, 02).

## Fundamental Active Process (Seven Steps)
**When to use**: running or auditing a discretionary equity strategy.
**How**: (1) universe and thesis; (2) prescreen; (3) industry/competitive and financial analysis; (4) forecast cash flows/earnings; (5) valuation to target prices; (6) construct portfolio with sector stance; (7) rebalance with sell discipline, target-price updates and stop-loss.
**Trade-offs**: depth and conviction vs behavioral biases, value and growth traps (ch 03).

## Quantitative Process and Factor Test
**When to use**: building a factor/quant strategy.
**How**: thesis → clean point-in-time data (include delisted names, original data) → quantile or IC back-test → combine factors (watch correlation) → out-of-sample test → risk model, cost model, optimizer → regular rebalancing.
**Trade-offs**: ICs: Pearson (outlier sensitive) vs Spearman; quantile test ignores middle deciles; costs destroy fast-decaying signals; crowding risk (ch 03).

## Factor Timing Research (Normalized-Yield Regression)
**When to use**: testing style rotation on a macro variable.
**How**: detrend the variable (`yield_t − 12-month average`); regress factor return on it contemporaneously and with a one-month lead; use the lagged version for prediction; require out-of-sample validity and an economic rationale.
**Trade-offs**: spurious relationships; weak for some factors, strong for size and beta (ch 03).

## Pairs Trade (Spread Rule)
**When to use**: mean-reverting stat arb on two similar stocks.
**How**: spread = ln(P_A/P_B); rolling mean and σ; enter long laggard/short leader beyond ±2σ; exit at the mean; stop-loss.
**Trade-offs**: structural breaks (CNR/CP third trade); needs an economic link, not only correlation (ch 03).

## Merger Arbitrage
**When to use**: announced deals.
**How**: cash deal long target; stock deal long target, short acquirer at exchange ratio; estimate failure probability and duration; annualize the spread; size by return and risk.
**Trade-offs**: sharp target drop if the deal fails (ch 03).

## Activist Campaign Screen
**When to use**: choosing targets.
**How**: look for slow growth, weak momentum, weak governance, underused assets; engage (letters, board seats, proposals, proxy contest, settlement); expect defenses (poison pill, staggered board, multi-class).
**Trade-offs**: wrong target if already efficient or if better suited to distressed restructuring (ch 03).

## Decompose Active Return and Risk
**When to use**: manager diagnosis and fee justification.
**How**: regress excess returns on Market, Size, Value, Momentum (+ BAB, Quality); `R_A = Σ(β_p − β_b)F + α + ε`; compute % of variance explained (R²) and % active risk by factor; read residual as skill, luck or missing factor.
**Trade-offs**: few observations cannot separate skill from luck (ch 04).

## Active Share / Active Risk Classification
**When to use**: spotting closet indexers and styles.
**How**: AS = ½ Σ|Δw|; compare with TE. AS ~0.25 and TE <2% = closet; AS ~0.7 and TE ~3% = diversified multi-factor; AS >0.9 and TE 8-12% = stock picker; high TE with sector deviations = sector rotator.
**Trade-offs**: AS depends on benchmark choice; ignores correlations (ch 04).

## Fundamental Law Sizing
**When to use**: checking if a return target is realistic or what breadth is needed.
**How**: `E(R_A) = IC × √BR × σ × TC`; solve for BR = (target/(IC σ TC))² or required IC.
**Trade-offs**: decisions are not independent; TC < 1 with constraints (ch 04).

## Risk Contribution Table
**When to use**: risk budgeting across positions, sectors, factors.
**How**: `CV_i = x_i Σ_j x_j C_ij`; % = CV_i/V_p. Relative version uses active weights and relative-return covariances. Factor share of variance = (b'Σ_F b)/σ_p² (e.g., 91% Market in the low-risk example).
**Trade-offs**: relative risk reverses intuition: cash lowers absolute but raises active risk (ch 04).

## Capacity and Position Limit Check
**When to use**: setting limits as AUM grows.
**How**: position cap = min(% of assets, ADV% × ADV); ADV ≈ daily turnover × cap; index-based caps (min(10× index weight, index weight + 1%)); compute AUM where the smallest permitted stock binds.
**Trade-offs**: more names, larger caps, lower turnover as AUM grows (ch 04).

## Leverage Ceiling
**When to use**: deciding how far to lever a strategy.
**How**: `R_g ≈ L·R_a − (Lσ)²/2 − funding`; optimum L ≈ (R_a − funding)/σ²; check crisis volatility.
**Trade-offs**: 10% / 20% asset: 2x and 3x both give 12%, funding cost pushes the peak lower (ch 04).

## Design a 130/30 Mandate
**When to use**: relaxing long-only constraints on a score-based process.
**How**: keep the objective (max factor score); net exposure = 100%, gross ≤ 160%; allow negative weights; cap short size below long size (e.g., 1% vs 3%) given noisier short signals; keep sector constraints; set up prime broker and collateral.
**Trade-offs**: borrow cost and recall, unlimited short loss, higher fees, losses if both long and short views fail (ch 04).
