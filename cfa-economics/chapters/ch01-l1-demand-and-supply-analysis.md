# Chapter 1: Topics in Demand and Supply Analysis
> **Source**: CFA Program Curriculum 2020, Level I, Reading 12 · Economics | Richard V. Eastin, Gary L. Arbogast

## Core Idea
Demand sensitivity is measured by unit-free elasticities (own-price, income, cross-price), and these tell you who has pricing power and what happens to revenue when prices move. On the supply side, a firm's cost structure (MC, AVC, ATC, fixed vs variable) determines how much it produces, when it keeps operating at a loss (price above AVC), when it must exit (price below ATC) and which scale is efficient. For an analyst this is the bridge from "market model" to "which companies can earn economic profit".

## Learning Outcomes Covered
- Calculate and interpret price, income and cross-price elasticities; list what drives each.
- Compare substitution and income effects of a price change.
- Distinguish normal from inferior goods (and Giffen/Veblen exceptions).
- Describe diminishing marginal returns.
- Determine and interpret breakeven and shutdown points.
- Describe how economies and diseconomies of scale shape costs (LRAC, minimum efficient scale).

## Frameworks Introduced
- **Demand function and inverse demand function**: `Qxᵈ = f(Px, I, Py)`; solve for P to get `Px = f(Qx)`, which is what the demand curve plots (price on the vertical axis).
  - When to use: any time you are handed an estimated (usually linear) demand equation and must compute elasticities.
  - How: (1) choose the evaluation point (Px, I, Py); (2) compute Q by substitution; (3) elasticity = coefficient × (variable / Q). Hold the other variables constant by folding them into the intercept (gasoline example: 84.5 + 0.25·50 − 2·20 = 57, so Q = 57 − 6.39P and P = 8.92 − 0.156Q).
  - Failure mode: the linear form is only a local approximation; it hits Q = 57 at P = 0 and is not valid for extrapolation. Market demand = sum of individual demands (1,000 identical households multiply every coefficient by 1,000, but elasticities are unchanged because Q scales too).
- **Own-price elasticity of demand**: `Eᵖ = %ΔQᵈ/%ΔP = (ΔQ/ΔP)(P/Q)`.
  - When to use: pricing decisions, revenue forecasts, commodity and consumer-staples analysis.
  - How: read the sign (negative if the law of demand holds) and the magnitude. |E| > 1 elastic, |E| = 1 unit elastic, |E| < 1 inelastic, |E| = 0 perfectly inelastic (vertical demand), |E| = ∞ perfectly elastic (horizontal demand: the demand curve facing a competitive firm).
  - Why it works / failure mode: along a straight-line demand curve ΔQ/ΔP is constant but P/Q varies, so elasticity is elastic above the midpoint, unit elastic at the midpoint and inelastic below it. Slope is not elasticity.
- **Elasticity and total expenditure (= sellers' total revenue)**:
  - Elastic: price and total expenditure move in opposite directions. Inelastic: they move in the same direction. At unit elasticity (the midpoint of a linear curve) total expenditure is at its maximum.
  - Rule for a single-product seller facing inelastic demand: raise price (revenue up, units and cost down, so profit up) until demand becomes elastic.
- **Predictors of own-price elasticity** (more elastic when): many close substitutes; narrower product definition (Baker Bob's loaf is more elastic than "bread"); large share of the budget (housing vs toothpaste); discretionary rather than necessary; longer adjustment time. Exception: durable goods can be more elastic in the short run (a price cut triggers replacement purchases that are only pulled forward).
- **Income elasticity of demand**: `E_I = %ΔQᵈ/%ΔI`. Positive: normal good (demand curve shifts right when income rises). Negative: inferior good (shifts left). Can be zero.
- **Cross-price elasticity of demand**: `E_xy = %ΔQxᵈ/%ΔPy`. Positive: substitutes. Negative: complements. The classification is empirical, not intuitive (coffee on sale in a supermarket may show up as a complement of cabbage).
- **Substitution effect vs income effect** of a price change:

| Good type | Substitution effect (price falls) | Income effect (price falls, real income rises) | Net |
|---|---|---|---|
| Normal | Buy more (relatively cheaper) | Buy more | Reinforce, downward-sloping demand |
| Inferior | Buy more | Buy less | Offset partly; demand still downward-sloping |
| Giffen (extreme inferior, large budget share) | Buy more | Buy less, by more | Quantity falls when price falls: upward-sloping demand |
| Veblen (status good) | n/a: the high price itself adds utility | n/a | Quantity rises with price |

  - Isolating the effects (Monica example): charge a fee that makes the consumer exactly indifferent between the old and new price situation, which removes the income effect; the quantity change that remains is the pure substitution effect. Giving the discount for free then reveals the income effect.
  - The same good can be normal for one income group and inferior for another (fast food).
- **Productivity measures**: total product `TP = Q`; average product `APL = Q/L`; marginal product `MPL = ΔQ/ΔL`. Use APL (not TP) to compare firms: TP only shows scale/market share (Company A: 1,000 widgets per worker hour with the lowest share; Company C: 800 with the highest share).
- **Law of diminishing marginal returns**: with capital fixed, MPL first rises (specialization, increasing marginal returns), then falls as more labor is added to a fixed plant; eventually MPL can turn negative. It is a short-run concept.
- **Cost-productivity links**: `SMC = w/MPL` and `AVC = w/APL` (w = wage per labor hour). Cost falls when input prices fall or productivity rises. Total cost of inputs: `TC = wL + rK` (r = rental rate of capital; own capital carries the opportunity cost of not renting it out).
- **Economic vs accounting profit**: economic profit = TR − total economic cost (explicit + implicit/opportunity costs, including a normal profit = required return on equity capital). Accounting profit = TR − accounting cost. Normal profit is treated as a fixed cost. Economic depreciation is forward-looking (what I give up by using the asset), accounting depreciation is backward-looking (spreading sunk historical cost); sunk costs never enter an optimal decision.
- **Profit-maximization rule**: produce where `MR = MC` and MC is not falling (second-order condition: MC cutting MR from below). Raise Q if MR > MC, cut if MR < MC.
  - `MR = ΔTR/ΔQ = P + Q(ΔP/ΔQ)`. Perfect competition: slope of the firm's demand is 0, so MR = P = AR. Imperfect competition: negative slope, so MR < P (you must cut the price on all units to sell one more).
  - For a price-setter, MR > 0 exactly where demand is elastic, so TR rises then falls with output; the monopolist never operates in the inelastic range.
- **Breakeven and shutdown analysis**:
  - Breakeven: TR = TC, i.e. P (= AR) = ATC. The firm earns normal profit but zero economic profit. In perfect competition the breakeven point is minimum ATC.
  - Shutdown point (competitive firm): P = minimum AVC. Below it the firm loses more by operating than by closing.

| Revenue vs cost | Short-run decision | Long-run decision |
|---|---|---|
| TR ≥ TC (P ≥ ATC) | Operate | Stay |
| TVC ≤ TR < TC (AVC ≤ P < ATC) | Operate (covers variable cost, contributes to fixed cost) | Exit |
| TR < TVC (P < AVC) | Shut down (loss = TFC) | Exit |

  - Note: the curriculum table writes "TR = TVC" for the middle row; at exact equality the firm is indifferent in the short run (loss = TFC either way).
- **Economies and diseconomies of scale**: the long-run total cost curve is the lowest short-run cost curve at each output (an envelope curve); LRAC is the envelope of all SATC curves. LRAC slopes down (economies), is flat (constant returns), then slopes up (diseconomies). Minimum efficient scale = lowest point on LRAC, the long-run equilibrium firm size under perfect competition.
  - Sources of economies: increasing returns to scale, division of labor and management, affordable advanced equipment/technology, waste reduction and by-products, better market information, bulk-purchase discounts (Wal-Mart, electric utilities).
  - Sources of diseconomies: decreasing returns to scale, unmanageable size, duplicated functions and overlapping product lines (GM pre-restructuring), higher input prices from supply constraints.
  - Both can coexist; the net effect on LRAC depends on which dominates.

## Key Concepts
- **Law of demand**: all else equal, a price fall raises quantity demanded; the demand curve slopes down.
- **Own price**: the good's price itself, as opposed to the price of a related good.
- **Normal / inferior good**: positive / negative income elasticity ("inferior" says nothing about quality).
- **Giffen good**: an inferior good with a large budget share and a very negative income effect that overwhelms the substitution effect; positively sloped demand (rice for subsistence-level households).
- **Veblen good**: a luxury/status good whose high price is part of its appeal (conspicuous consumption); not an inferior good.
- **Short run vs long run**: short run = at least one input (typically capital/plant) fixed; long run = all inputs variable and entry/exit possible. The firm operates in the short run but plans in the long run.
- **Quasi-fixed cost**: fixed over a production range but stepping to a new constant level beyond it (some utilities, administrative salaries). Still part of TFC.
- **Variable vs fixed costs**: TVC is zero at Q = 0 and rises with output; TFC is constant, so TC = TFC at Q = 0. Debt service, leases, rental contracts and normal profit are fixed.
- **AFC, AVC, ATC, MC**: AFC = TFC/Q (falls continuously); AVC = TVC/Q; ATC = TC/Q = AFC + AVC; MC = ΔTC/ΔQ. MC cuts both AVC and ATC at their minima. AVC minimum occurs at lower Q than ATC minimum because AFC is still falling.
- **Sunk cost**: already paid and unavoidable; irrelevant for forward-looking decisions.
- **Economic loss**: revenue short of total opportunity cost (distinct from an accounting loss).
- **Average revenue (AR)**: revenue per unit = price.
- **Minimum efficient scale**: output at the bottom of LRAC.

## Formulas & Reference Tables
- Demand: `Qxᵈ = f(Px, I, Py)`; linear form `Q = a − bPx + cI + dPy`.
- Own-price elasticity: `E_P = (ΔQ/ΔPx)(Px/Q) = −b·Px/Q` for linear demand.
- Income elasticity: `E_I = (ΔQ/ΔI)(I/Q) = c·I/Q`.
- Cross-price elasticity: `E_xy = (ΔQ/ΔPy)(Py/Q) = d·Py/Q`.
- Total expenditure/revenue: `TR = P·Q`; `MR = ΔTR/ΔQ = P + Q(ΔP/ΔQ)`; perfect competition `MR = P = AR`.
- Costs: `TC = TFC + TVC`; `TC = wL + rK`; `ATC = AFC + AVC`; `MC = ΔTC/ΔQ`; `SMC = w/MPL`; `AVC = w/APL`.
- Productivity: `APL = Q/L`; `MPL = ΔQ/ΔL`.
- Profit: `π(economic) = TR − TC(economic)`; max where `MR = MC`, MC rising.
- Decision thresholds: breakeven `P = ATC`; short-run shutdown `P < AVC`; long-run exit `P < ATC`.
- Linear demand elasticity zones: elastic above the midpoint (P > Pmax/2), unit elastic at the midpoint, inelastic below.

## Mental Models
- **"Elasticity, not slope"**: compare sensitivities across goods and units with elasticity; use the sign and size relative to 1 to decide whether to raise or cut price.
- **"Revenue climbs toward unit elasticity"**: cut price where demand is elastic, raise price where it is inelastic; a monopolist ends up in the elastic zone.
- **"Close the books on sunk costs"**: in the short run the only question is whether revenue covers avoidable (variable) cost. Fixed costs are paid either way, so never use ATC for the operate/shut decision; use ATC for the stay/exit decision.
- **"MC pulls the average"**: whenever MC is below an average (AVC or ATC) the average falls; above it, it rises. That is why MC crosses each average at its minimum.
- **"Productivity is the stock-picking lens"**: higher APL (or lower LRAC) than rivals means lower cost, wider margin and more value for shareholders; share of output says nothing about efficiency.
- **"Scale needs a landing spot"**: a firm left of minimum efficient scale should grow, one right of it should restructure.

## Worked Example
**Elasticities from a demand function (gasoline, recomputed).** Individual demand `Q = 84.5 − 6.39Px + 0.25I − 2Py` with Px = €1.48/L, I = 50 (€1,000s), Py = 20 (car price, €1,000s).
- Q = 84.5 − 9.457 + 12.5 − 40 = **47.54 L/month**.
- Own-price: −6.39 × 1.48/47.54 = **−0.20** (inelastic). Income: 0.25 × 50/47.54 = **+0.26** (normal good). Cross-price: −2 × 20/47.54 = **−0.84** (complement of cars; weak).
- At Px = €5: Q = 25.05 and E = −6.39 × 5/25.05 = **−1.28** (elastic), so the same linear curve is inelastic at low prices and elastic at high prices.
- Expenditure check at the inelastic point: a 10% price rise (1.48 → 1.628) cuts Q to 46.60 (−2.0%), and spending goes from 70.36 to 75.86 per household (+7.8%): in the inelastic range, price and spending move together.

**Shutdown logic (widget firm).** Q = 100, P = €4, ATC = €7 (AVC 3.75 + AFC 3.25).
- TR = 400; TC = 700; economic loss = 300. TVC = 375, TFC = 325.
- Shut down: loss = 325 (the unavoidable fixed cost). Operate: loss = 300 (revenue covers 375 of variable cost and contributes 25 to fixed cost).
- Decision: operate in the short run (P 4 > AVC 3.75), exit in the long run (P 4 < ATC 7) unless the price recovers. Reading the Ecuador case with the same logic: TR 2.0m, TVC 1.5m, TFC 1.0m, so operating loses 0.5m vs 1.0m for closing (operate); if TR falls to 1.3m, operating loses 1.2m vs 1.0m (shut down).

## Anti-patterns
- **Judging elasticity by the slope of a straight-line demand curve**: slope is constant, elasticity varies from ∞ to 0 along it.
- **Reading "E = −0.2" as "demand falls 0.2"**: it means a 1% price rise cuts quantity by about 0.2%.
- **Using ATC in the short-run shutdown decision**: fixed costs are sunk; compare price with AVC. Using AVC for the long-run exit decision is equally wrong.
- **Equating profit-maximizing output with minimum ATC**: min ATC maximizes profit per unit, not total profit. Total profit peaks at MR = MC (WR International: break-even at 40 and 80 units, profit maximum 30,000 at 60 units, not at the lowest unit cost).
- **Confusing accounting profit with economic profit**: a competitive firm earning zero economic profit still reports positive accounting profit (it earns the normal return).
- **Judging a firm's efficiency by output**: total product shows market share; use APL/MPL, unit cost or LRAC position.
- **Treating P = SMC as sufficient**: there are two such points; only the one with SMC rising is the maximum.
- **Assuming "inferior" means low quality or that Giffen is common**: inferior is an income-response label; Giffen requires very high budget share and no good substitutes.

## Exam Focus & Traps
- **Elastic is |E| > 1**, not E > 1; own-price elasticity is almost always negative, so always take the absolute value before labeling. Total expenditure is maximized at |E| = 1.
- **Which formula when**: slope coefficient × (variable/Q) uses the coefficient of the variable in question, and Q must be recomputed at the stated values. Do not use the price coefficient with the income value.
- **Sign conventions**: cross-price positive = substitutes, negative = complements; income positive = normal, negative = inferior.
- **Substitution vs income effect**: the substitution effect always goes in the "buy more when cheaper" direction. Only the income effect depends on normal/inferior. If the income effect exceeds the substitution effect for an inferior good it is Giffen.
- **Veblen vs Giffen**: Veblen is about status (high price adds value), Giffen about a strongly inferior staple; do not describe Veblen goods as inferior.
- **Shutdown vs exit**: short run compare P (or TR) with AVC (TVC); long run compare with ATC (TC). Loss when shut down = TFC.
- **MC cuts AVC and ATC at their minima**; AVC minimum is at lower output than ATC minimum.
- **LRAC is the envelope of SATC curves**; MES = minimum of LRAC; constant LRAC = constant returns to scale.
- **Diminishing returns vs diseconomies of scale**: the former is short run with a fixed input; the latter is long run with all inputs scaled up.
- **Marginal revenue**: MR = P only in perfect competition; for a downward-sloping demand MR < P.

## Key Takeaways
1. Use elasticities (unit-free) to measure demand sensitivity: |E| > 1 means a price cut raises revenue; |E| < 1 means a price rise raises revenue; revenue peaks at |E| = 1.
2. Elasticity rises with substitutes, budget share, discretionary use and time (durables are the exception); on a linear curve it falls from elastic (top) to inelastic (bottom).
3. Positive cross elasticity = substitutes, negative = complements; positive income elasticity = normal, negative = inferior.
4. The substitution effect always points the "conventional" way; the income effect determines whether the good is normal, inferior or Giffen. Veblen goods break the law of demand through status.
5. Maximize profit at MR = MC with MC rising; MR = P only for price takers.
6. Operate in the short run while P ≥ AVC; stay in the long run only while P ≥ ATC; breakeven (zero economic profit) at P = ATC.
7. Productivity (APL, MPL) and unit costs, not volume, indicate competitive strength; diminishing marginal returns eventually push SMC up.
8. LRAC shape and the firm's position relative to minimum efficient scale tell you whether to grow, restructure, or expect cost-based market share loss.

## Connects To
- **ch 02**: market structures reuse MR = MC, the elasticity-markup link and the long-run zero-profit result.
- **ch 03**: aggregate demand/supply generalize the demand and supply curves to the economy.
- **ch 07**: elasticities of export/import demand underlie the Marshall-Lerner condition for the exchange rate.
- **`cfa-level1-curriculum` ch 01**: the owner's personal revision notes on this reading (formulas and shutdown rules); this chapter adds the substitution/income decomposition, MC/AVC relations, scale analysis and the exam traps.
- **`cfa-level1-curriculum` ch 11**: industry analysis (pricing power, cost position).
- **`cfa-equity-valuation` ch 02**: industry and company analysis builds on cost position, scale and pricing power.
