# Chapter 4: Understanding Business Cycles (Economics)

## Core Idea
Business cycles are recurrent but not periodic swings (trough → expansion → peak → contraction) that affect most sectors at the same time. Schools of thought disagree on the causes and on the right policy response. Leading, coincident and lagging indicators, together with unemployment and inflation measures, help locate the economy within the cycle.

## Frameworks Introduced
- **Four phases** and their typical behavior:

| Phase | Output | Employment | Inflation | Capex / inventories |
|---|---|---|---|---|
| Trough / early expansion | Starts rising | Layoffs slow; overtime and temp workers first | Moderate, falling | Light equipment first; inventory rebuilding |
| Late expansion | Strong growth | Unemployment falls sharply | Accelerates | Heavy equipment and plants |
| Peak | Growth slows | Hiring slows | High | Unplanned inventory build-up |
| Contraction | Falls | Hours cut, then layoffs | Falls with a lag | Capex cut abruptly |

- **Sector behavior over the cycle**:
  - **Capital spending** is the most volatile component.
  - **Inventories**: a rising inventory/sales ratio signals weakening demand.
  - **Consumers**: durables > non-durables > services in cyclicality. Disposable income growth is the best predictor of spending.
  - **Housing**: sensitive to mortgage rates and the price-to-income ratio.
  - **External trade**: exports depend on foreign growth and the currency.
- **Schools of thought**:
  - **Classical / neoclassical**: flexible prices clear markets, and money is neutral (Say's law). There is no real theory of the cycle.
  - **Keynesian**: sticky wages and prices, and weak "animal spirits" in demand. Government should boost AD ("in the long run we are all dead").
  - **Monetarist (Friedman)**: steady money growth. Policy lags make activism harmful. The long-run Phillips curve is vertical at the natural rate.
  - **Austrian**: credit-fueled malinvestment, then bust. Individual subjective choices matter.
  - **New classical / Real Business Cycle (RBC)**: cycles are rational responses to *real* shocks (technology). Money plays no role.
  - **New Keynesian / DSGE**: micro-founded models with frictions.
  - **Minsky**: stability breeds complacency, then leverage, then a "Minsky moment" panic.
- **Unemployment**:
  - Unemployment rate = unemployed/labor force. Participation rate = labor force/working-age population.
  - Types: **frictional** (job search), **structural** (skills mismatch), **cyclical** (weak demand).
  - Hidden: **discouraged workers** are outside the labor force. **Underemployed** workers count as employed.
  - The unemployment rate is a **lagging indicator**. Hours worked and temporary hiring react earlier.
- **Okun's law**: every 1 percentage point of unemployment above the natural rate ≈ a 2% output gap.
- **Inflation**:
  - Deflation: falling price level. Disinflation: slowing but positive inflation. Hyperinflation: extremely fast rises.
  - **Cost-push**: wages, commodities, labor shortages. Watch for unemployment below **NAIRU**.
  - **Demand-pull**: output near potential, high capacity utilization.
- **Price indexes**:
  - **Laspeyres** (base-period basket): `ΣP_nQ_0 / ΣP_0Q_0`. It suffers from substitution, quality and new-product biases, all of which push measured inflation up.
  - **Paasche** (current basket): `ΣP_nQ_n / ΣP_0Q_n`.
  - **Fisher** = √(Laspeyres × Paasche).
  - Hedonic adjustments correct for quality changes.
  - Measures: **CPI** (CPI-U), **PCE**, **PPI/WPI**, **HICP** (ECB), GDP deflator. **Headline** inflation includes everything; **core** excludes food and energy.
- **Indicators**:
  - **Leading**: capital goods orders, building permits, stock prices, M2, the yield spread, PMI, consumer expectations. The Conference Board LEI has 10 components. Other composites: OECD CLI, ECRI.
  - **Coincident**: industrial production, payroll employment, real income, sales.
  - **Lagging**: unemployment duration, unit labor costs, the prime rate, inventory/sales.

## Key Concepts
- **Recession vs depression**: a depression is an exceptionally severe contraction.
- **Natural rate of unemployment (NRU/NAIRU)**: the unemployment level consistent with stable inflation.
- **Phillips curve**: short-run inflation–unemployment trade-off. It is vertical in the long run.
- **TIPS**: bonds whose principal is indexed to CPI-U.

## Mental Models
- **Businesses adjust hours before headcount and inventories before capex.** Read the cycle from those margins first.
- **Use leading indicators to forecast and lagging indicators to confirm.** Unemployment confirms; it does not predict.
- **Policy view depends on the school**: Keynesians stimulate AD, monetarists keep money growth steady, Austrians let the bust clear malinvestment.

## Anti-patterns
- ⚠ **Correction vs the notes**: a *rising* (not falling) inventory-to-sales ratio near the peak signals a weakening economy.
- **Reading a falling unemployment rate as strength** when participation is dropping (discouraged workers).
- **Using headline CPI alone to set policy**: food and energy are volatile. Central banks watch core inflation.

## Worked Example
**Laspeyres vs Paasche.** Two goods:
- Year 0: bread $2 × 100 units, fuel $3 × 50 units.
- Year 1: bread $2.2 × 110 units, fuel $4 × 40 units (consumers substitute away from fuel).
- Laspeyres = (2.2 × 100 + 4 × 50)/(2 × 100 + 3 × 50) = 420/350 = **1.200**.
- Paasche = (2.2 × 110 + 4 × 40)/(2 × 110 + 3 × 40) = 402/340 = **1.182**.
- Fisher = √(1.200 × 1.182) = **1.191**.
- Laspeyres overstates inflation because it ignores the substitution away from fuel.

## Key Takeaways
1. Cycles are recurrent, not periodic. Capex and inventories are the swing components.
2. Unemployment is lagging. Hours, temporary hiring and orders lead.
3. Laspeyres has an upward bias (substitution, quality, new goods). Fisher is the geometric mean of Laspeyres and Paasche.
4. Cost-push inflation (wages, commodities) vs demand-pull (output near potential).
5. Know each school's diagnosis and prescription (Keynesian, monetarist, Austrian, RBC, Minsky).

## Connects To
- **Ch 3**: AD/AS gaps.
- **Ch 5**: the policy response to the cycle.
- **Ch 11**: cyclical vs defensive industries.
- **Ch 14**: TIPS and inflation-linked bonds.
