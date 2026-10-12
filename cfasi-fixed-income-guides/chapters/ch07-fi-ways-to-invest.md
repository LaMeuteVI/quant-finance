# Chapter 7: The Different Ways of Investing in Fixed Income
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 7 (Le diverse modalità di investire nel reddito fisso) | Federico Reggianini, CFA

## Core Idea
There are four routes into bonds: individual securities, passive vehicles (ETPs/ETFs), active funds, and insurance segregated accounts (gestioni separate) valued at amortized cost. The right route depends on portfolio size (diversification), selection capability (credit and macro analysis), and cost. Individual bonds suit institutions with a team; small retail portfolios should usually delegate. Passive bond replication is partial and carries benchmark quirks (debtor-weighting, rising duration). Active funds split into directional, total return and absolute return, and require a quantitative plus qualitative due diligence.

## Frameworks Introduced
- **Size x selection-capability matrix** (route chooser)
  | | Low selection capability | High selection capability |
  |---|---|---|
  | Small portfolio | No diversification, no consistency with objectives (retail single bonds) | Consistency possible, diversification not |
  | Large portfolio | Diversification possible, consistency not | Both possible (institutions, professional investors, eligible counterparties) |
  - Rule: single bonds only if you can both diversify (by maturity, issuer, country, sector) and run credit selection and maintenance in-house.
- **Four-cost comparison (single bond vs ETP)**: trading cost, allocation (alignment to objectives) cost, credit analysis cost, product cost. ETP removes credit analysis and (partly) allocation costs but adds product cost; it is not automatically cheaper.
- **Why Italian retail clung to single bonds** (behavioural): cost misjudgment (only trading cost seen), overconfidence, status-quo bias, endowment effect, regret aversion, home bias. Defaults (Lehman, Italian resolved banks, Veneto banks) hurt investors who lacked diversification.
- **Physical vs synthetic replication**
  | | Physical (sampled) | Synthetic (swap-based, EU since 2001) |
  |---|---|---|
  | Holdings | Sample of benchmark bonds matched on rate and spread risk factors | Swap with a bank paying benchmark return |
  | Transparency | Near total | Lower |
  | Counterparty risk | None | Yes |
  | Cost items | Transaction + management | Swap cost + management |
- **Benchmark validity test** (three criteria): unambiguous (names and weights identifiable), investable (others can trade the constituents), measurable (returns computable at reasonable frequency by several parties).
- **Bond benchmark quirks**:
  - Capitalization bias: bond indices weight the largest issuers and the most indebted countries/companies most, so they overweight the "least virtuous" (opposite of equity indices that reward winners).
  - Duration drift: falling yields lengthen index duration and raise rate sensitivity of passive holders.
  - OTC structure makes full replication costly; sampled replication still contains an active element.
- **Active mandate types**
  | Mandate | Objective | Benchmark | Tracking error |
  |---|---|---|---|
  | Directional active | Beat a market benchmark | Market index (check fit with stated and actual style) | Moderate |
  | Total return | Maximize income plus price gains at index-like volatility | Index, but lower correlation | Higher |
  | Absolute return ("unconstrained") | Positive return regardless of market; cash or inflation plus a spread (e.g. 3-month Euribor +1%) | Cash-plus | Not applicable |
  - Directional: top-down (macro views on rate, credit, currency allocation), bottom-up (credit fundamentals, inefficiencies), or hybrid (top-down allocation, bottom-up selection).
  - Absolute return levers: negative duration, short credit on names or indices, active currency; allocate across several managers because selection is the hardest.
  - Check benchmark coherence by regression of fund returns on the stated benchmark and by tracking error.
- **Active manager due diligence**
  - Quantitative: risk-adjusted returns (Sharpe, information ratio) are a starting point; decompose sources of return, risk taken versus benchmark, dependence on single positions or market phases, behaviour in adverse markets, persistence versus a short lucky window.
  - Qualitative: team, investment philosophy, process (research resources), portfolio construction and risk management, explicit and implicit costs (higher-cost funds underperform lower-cost peers over the long run).
- **Amortized-cost (book value) accounting in segregated accounts**: book value each year = prior book value + (book value x IRR at purchase) − coupon. The path converges to par at maturity regardless of market moves; no mark-to-market volatility unless sale, default or call.

## Key Concepts
- **ETP / ETF** — exchange traded product, usually passive, liquid, transparent, cheap, intraday.
- **Tracking error** — deviation of performance from the benchmark.
- **Sampling / optimized replication** — holding a subset matched on key risk factors.
- **Benchmark (Bloomberg Barclays Global Aggregate)** — about 20,000+ bonds, investment grade only, average yield to worst 1.87%, effective duration 7.04, OAS 34.9 bp (February 2018).
- **Directional / total return / absolute return** — see mandate table.
- **Unconstrained** — absolute-return style freed from benchmark constraints (see ch09).
- **Segregated account (gestione separata, branch I/V insurance products)** — insurer's pool accounted at historical amortized cost.
- **Book value** — carrying value on the pool's books.
- **Overconfidence / home bias / regret aversion** — behavioural drivers of concentrated bond holdings.
- **Eligible counterparty / professional investor** — categories with the capital and capability to hold single bonds.

## Formulas & Reference Tables
- Amortized cost recursion: `BV_t = BV_{t−1} + BV_{t−1} × IRR − Coupon`.
- Index data (Global Aggregate, Feb 2018, from the guide): geography US 36.2%, France 10.2%, UK 10.2%, Germany 8.3%, Italy 6.9%; maturity 1-3 years 25.1%, 3-5 years 20.8%, 5-7 years 13.8%, 7-10 years 15.5%; AAA 36.6%, Baa1-Baa3 25.2% combined, Ba1 0.01%.
- Evidence cited from Morningstar/PIMCO to end-2016: a larger share of active bond funds beat their benchmark across 1-10 year horizons than active equity funds; caveat: partial period, survivorship-adjusted, varies by segment.

## Mental Models
- Use the size/selection matrix before recommending any bond route.
- Use ETFs for core beta when your own selection edge is small; use active only where you can underwrite the edge.
- Use total return mandates when you want income and capital gains at similar volatility; use absolute return as a diversifier, with several managers.
- Use due diligence in two layers: numbers (what happened and why) and people/process (will it repeat).
- Use the amortized-cost lens when comparing a segregated account with a fund holding the same bonds: the difference is price risk disclosure, not economic risk.

## Worked Example
Segregated account bond: 20 years, 3.00% coupon, redeemed at 100, yield at purchase 3.50%.
1. Price (book value at purchase) = `3·[1−1.035^−20]/0.035 + 100/1.035^20 = 92.89`.
2. Year 1 income = `92.89 × 3.5% = 3.25`; book value end of year 1 = `92.89 + 3.25 − 3.00 = 93.15`.
3. Year 2 income = `93.15 × 3.5% = 3.26`; book value = `93.41`; and so on to 100.00 in year 20.
Interpretation: even if the market yield jumps to 6%, the book value follows this path unless the bond is sold, defaults or is called; a fund holding the same bond would show a mark-to-market loss.

## Anti-patterns
- Buying EUR 100,000-minimum corporate bonds in a small retail account for "yield".
- Comparing only trading fees between a bond portfolio and an ETF.
- Assuming a passive bond fund tracks a benchmark with all constituents.
- Picking active managers on one good three-year track record.
- Treating a "benchmark" stated in the prospectus as the real risk reference without testing it.
- Reading smooth segregated-account returns as lower economic risk.

## Practitioner Notes
- Regulation (PRIIPs/MiFID-era rules) made bonds for retail costly for issuers, shifting small investors towards managed products.
- Index duration lengthened as yields fell: an ETF tracking the aggregate in 2018 is more rate-sensitive than the same ETF in 2008.
- Active absolute return funds are hard to select given freedom granted and short track records.

## Key Takeaways
1. Pick the route by portfolio size and selection capability.
2. Single bonds fit institutions; retail diversification is usually inadequate.
3. ETPs add liquidity, transparency, low cost, but no outperformance and partial universe coverage.
4. Bond benchmarks overweight heavy borrowers and drift to longer duration when yields fall.
5. Physical replication is sampled; synthetic replication adds counterparty risk.
6. Active mandates: directional, total return, absolute return, each with different benchmark, tracking error and role.
7. Due diligence: risk-adjusted returns decomposed, plus team, philosophy, process, costs.
8. Amortized-cost accounting hides price volatility, it does not remove it.

## Connects To
- **ch04**: market structure behind benchmark replication and liquidity.
- **ch08**: passive/active portfolio management in detail (tracking error, replication, immunization).
- **ch09**: unconstrained products.
- **ch10**: coupon-paying (income) fund structures.
- **`cfasi-fixed-income-guides` ch12**: unconstrained funds, the same absolute return family.
- **`cfa-fixed-income`**: valuation basics and index construction.
