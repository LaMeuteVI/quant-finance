# Chapter 8: Introduction to Active and Passive Fixed Income Portfolio Management
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 8 (Introduzione sulla gestione di portafogli a reddito fisso attivi e passivi) | Federico Reggianini, CFA

## Core Idea
A bond portfolio manager always manages to a reference: a liability (asset-liability management) or a benchmark. "Passive" does not mean buy-and-hold; immunization and index replication both need frequent rebalancing. When the target is a dated liability, use portfolio immunization (cash flow matching, duration matching, derivatives overlay, contingent immunization). When the target is an index, replicate its risk factors (duration, key rates, sector, quality, issuer) to minimize tracking error. Active managers deviate from the benchmark bottom-up (relative value inside homogeneous credit buckets) or top-down (macro views on sectors, curve, quality).

## Frameworks Introduced
- **Liability taxonomy (ALM)**
  | Type | Amount | Timing | Example |
  |---|---|---|---|
  | 1 | Known | Known | Fixed-coupon bullet bond |
  | 2 | Known | Unknown | Callable/putable bonds |
  | 3 | Unknown | Known | Floating-rate bond (coupon dates known) |
  | 4 | Unknown | Unknown | Catastrophe insurance claims |
  - Immunization is built for type 1 liabilities (also multiple dated liabilities).
- **Portfolio immunization principle**: structure the portfolio so that the price effect at the horizon and the reinvestment income from coupons and principal offset, neutralizing both interest-rate and reinvestment risk. Four techniques:
  1. **Cash flow matching**: buy zeros (or bonds) whose cash flows replicate the liability. Obstacles: no zeros of exact maturity; coupon bonds bring reinvestment risk; every bond carries credit risk.
  2. **Duration matching**: build a portfolio whose Macaulay duration equals the liability's duration (for a single bullet liability, its time to payment), with cash flows dispersed around the liability date. The most used method because exact cash flow matches are rare.
  3. **Derivatives overlay**: use government bond futures to adjust duration of an already immunized portfolio after yield-curve moves, cheaper and more liquid than switching bonds; credit risk of the bonds remains.
  4. **Contingent immunization**: manage actively while the portfolio value exceeds the present value of the liability by a surplus; when the surplus shrinks to a floor, switch to full immunization. The surplus can be invested in any asset provided it can be liquidated quickly.
- **Duration matching conditions** (classical): (1) asset Macaulay duration = liability duration; (2) PV of assets at least PV of liabilities; (3) asset cash flow dispersion at least as large as the liability's (so gains on reinvestment cover price changes). Rebalance as time passes and rates move, since duration drifts.
- **Index replication ladder**: full replication (buy everything, essentially infeasible in bonds), then risk-factor replication, then stratified sampling.
  - Why full replication fails in bonds: far more securities than equity indices (MSCI World about 1,642 stocks vs Global Aggregate over 20,000 bonds), more issuers, OTC liquidity, frequent index updates (monthly) from issues, calls, puts, defaults.
- **Risk-factor replication checklist**: (1) effective duration; (2) key rate durations (parallel, steepening, twist); (3) sector and credit quality allocation like the benchmark; (4) allocation by sector, coupon, maturity (to manage calls and MBS refinancing); (5) issuer exposure caps (an overweight issuer inflates tracking error on default or M&A).
- **Bottom-up active process** (four steps): (1) universe selection by homogeneous credit categories (sector, rating, region); (2) relative value analysis to isolate bonds cheap versus peers, weighing extra yield against extra spread, default and liquidity risk; (3) spread curve analysis per issuer (plot Z-spread against spread duration, overweight bonds above their issuer curve after checking why); (4) portfolio construction by duration, spread duration and weights per category.
- **Top-down active process**: macro drivers (growth, profits, default rates, risk appetite, rates, currencies) drive sector/issuer allocation; categories can be broader than in bottom-up.
- **Active manager toolbox**: lower trading cost (bid-offer), security selection, over/underweight on curve areas versus benchmark, over/underweight sectors or quality buckets.

## Key Concepts
- **Asset-liability management (ALM)** — setting investments by the obligations to be met.
- **Cash flow matching** — dedicating bonds to liability dates.
- **Macaulay duration** — present-value-weighted average time to cash flows, named after Frederick Macaulay.
- **Surplus** — portfolio value minus PV of liabilities.
- **Tracking error** — standard deviation of the difference between portfolio and benchmark returns.
- **Effective duration** — price sensitivity from repricing at yields down and up: `(P− − P+) / (2 × P × Δi)`.
- **Key rate duration (KRD)** — sensitivity to a change at one point of the curve; the KRDs sum to effective duration.
- **Parallel shift, steepening, twist (curvature)** — curve movements; classical duration covers only the first.
- **Spread duration** — sensitivity to changes in spread.
- **Full replication / sampling** — hold all constituents / a subset.
- **Relative value** — comparing bonds within a homogeneous credit class.

## Formulas & Reference Tables
- `Tracking error = sqrt( Σ[(R_pi − R_bi) − (R_p − R_b)]² / (n − 1) )`, where `R_pi, R_bi` are portfolio and benchmark returns in period i, `R_p, R_b` their averages.
- `Effective duration = (P_− − P_+) / (2 × P_0 × Δi)`, with `P_−`, `P_+` prices after yields fall/rise by `Δi`.
- Portfolio duration = value-weighted average of component durations; for zeros, duration = maturity.
- Scenario P&L from KRDs: `ΔP/P ≈ −Σ KRD_k × Δy_k`.
- Duration-matching condition: `D_assets = D_liabilities`.
- Table of the guide's key-rate example (three zeros at 1, 5, 10 years, prices 95, 90, 80, total 265): KRD(1y) = 0.36, KRD(5y) = 1.70, KRD(10y) = 3.02, total 5.08. The guide truncates to 0.35 / 1.69 / 3.01 / 5.07.

## Mental Models
- Use immunization when you owe a known sum on a known date: match duration, check dispersion, rebalance.
- Use contingent immunization when the funding surplus is large and a controlled risk budget is acceptable.
- Use a futures overlay to repair duration drift cheaply, remembering it does not remove credit risk.
- Use KRDs rather than a single duration whenever curve shape (steepener, twist) matters; parallel-only duration can mis-state loss by over 50% (guide example).
- Use bottom-up inside tight credit buckets and top-down across them; the quality of relative value analysis falls when risk differences are large.
- Use issuer limits in index tracking: one default or M&A event can dominate tracking error.

## Worked Example
Immunize a EUR 100m liability due in 10 years (guide's duration-matching case).
1. Portfolio of three bonds (maturities 2037, 2042, 2050 from a 2030 start), cost EUR 79,213,190.15.
2. Portfolio IRR (from combined cash flows) is 2.358%; time-weighted average of discounted cash flows gives Macaulay duration `10.00` years, equal to the liability horizon.
3. Value at year 10, reinvesting all cash flows at the scenario rate: rates unchanged (2.358%) EUR 100.006m; fall to 1.5%: EUR 100.094m; rise to 4%: EUR 100.311m. I recomputed all three.
4. PV of liability at the portfolio IRR is EUR 79.21m, so surplus is about EUR 5,000.
Interpretation: the shortfall risk disappears under parallel moves; the tiny positive excess in each scenario is the convexity and dispersion benefit.
**⚠ Correction**: the guide's table of individual Macaulay durations (5.07, 6.41, 9.27 years) is not consistent with the bonds; recomputed from the stated coupons, yields and maturities they are about 6.95, 10.75 and 13.30 years. The portfolio-level duration of 10.00 derived from the combined cash flows is correct, and the stated allocations (53%, 27%, 20%) apply to par amounts, not market value, so the weighted average of the bond durations by value does not equal 10 exactly.

KRD scenario example (zeros at 1, 5, 10 years): parallel +100 bp gives `−5.07%`; steepening (0, +100, +200 bp at 1, 5, 10 years) gives about `−7.72%` (guide: 7.73%); curvature (+100, 0, +100) gives `−3.37%`.

## Anti-patterns
- Calling a duration-matched portfolio "buy and hold".
- Matching duration with a single bullet when the liability's cash flows are dispersed, or with assets much more dispersed than liabilities.
- Assuming the aggregate index is fully replicable; liquidity and index changes make sampling mandatory.
- Overweighting one issuer to mimic spread without capping its tracking error contribution.
- Ignoring that derivatives overlays leave credit risk intact.
- Relative value across credit buckets of very different risk (e.g. the entire "banks" bucket).

## Practitioner Notes
- Index rebalancing events (new issues, calls, puts, defaults) force constant adjustments; bond indices update monthly compared with annually or semi-annually for many equity indices.
- Passive bond management still contains active decisions when full replication is impossible.
- Contingent immunization requires liquid assets for the surplus; illiquid holdings can block the switch to immunization.

## Key Takeaways
1. Know the benchmark or liability before judging a bond manager.
2. Four immunization tools: cash flow matching, duration matching, derivatives overlay, contingent immunization.
3. Duration matching equals liability duration with enough dispersion and periodic rebalancing.
4. Bond index replication targets risk factors, not individual securities.
5. KRDs expose curve risk that single duration hides.
6. Tracking error is the passive manager's risk metric.
7. Active management: bottom-up relative value inside homogeneous credit buckets, top-down macro tilts across sectors and curve.
8. Liquidity of the surplus assets is a hard constraint in contingent immunization.

## Connects To
- **ch06**: Macaulay and modified duration, convexity.
- **ch07**: route choice between passive and active funds.
- **ch09**: unconstrained products that remove the benchmark constraint.
- **`cfa-fixed-income` ch05, `cfa-portfolio-management`**: liability-driven investing and immunization in the CFA curriculum.
- **`tuckman-fixed-income`**: key rate durations and hedging.
