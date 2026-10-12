# Chapter 1: Introduction

## Core Idea
A derivative's value depends on an underlying variable; the same three instruments (forwards/futures, options, swaps) serve three very different users: hedgers (cut risk), speculators (buy leverage) and arbitrageurs (lock in mispricing). The rest of the book builds one no-arbitrage framework to value all of them.

## Frameworks Introduced
- **Exchange-traded vs OTC markets**: standardized contracts with a clearing house vs bilateral, customized contracts.
  - When to use: pick exchange-traded for liquidity and minimal credit risk. Pick OTC for tailored size, dates and underlyings.
  - Post-2008: standardized OTC derivatives must go through central counterparties (CCPs). Non-cleared trades carry mandatory margin.
- **Payoff diagrams (long/short × call/put/forward)**:
  - Long forward: `S_T − K`. Short forward: `K − S_T`.
  - Long call: `max(S_T − K, 0)`. Long put: `max(K − S_T, 0)`. The short positions are the negatives.
  - How: always draw payoff at maturity versus `S_T` before reasoning about value.
- **Three trader types**:
  - Hedgers use forwards to fix a price. They use options to buy insurance while keeping upside.
  - Speculators use futures/options for leverage.
  - Arbitrageurs exploit price gaps across markets. Their activity is what keeps prices consistent.

## Key Concepts
- **Derivative**: an instrument whose value depends on (derives from) other, more basic variables.
- **Forward contract**: an OTC agreement to buy/sell an asset at time T for price K. Settled at the end of its life.
- **Futures contract**: an exchange-traded, standardized forward. It is marked to market daily.
- **Call / Put**: the right (not the obligation) to buy / sell at strike K by or on the expiration date.
- **American vs European**: exercisable at any time vs only at maturity.
- **Long / Short position**: buyer / seller. The option writer receives the premium and bears the obligation.
- **Arbitrage**: a riskless profit from simultaneous trades in two or more markets.
- **Systemic risk**: one institution's default cascades through a network of OTC exposures (Lehman).

## Mental Models
- Think of a **forward as a free obligation** and an **option as paid insurance**. A hedge with forwards removes both downside and upside. A hedge with options keeps the upside for a premium.
- Use **leverage math**: a futures/option position gives a large exposure for a small cash outlay. The same leverage magnifies losses.
- Arbitrage opportunities are small and short-lived. **Assume no arbitrage** as the default pricing axiom.

## Anti-patterns
- **Using derivatives outside the mandate**: a hedger who drifts into speculation (SocGen, Kerviel, 2008 — €4.9bn loss). Always enforce risk limits and monitor them.
- **Confusing the option price with its payoff**: profit = payoff − premium (ignoring the time value of money).

## Worked Example
A speculator with $2,000 expects a stock at $20 to rise. A 2-month call with strike $22.50 costs $1.
- **Buy stock**: 100 shares. If S rises to $27 → profit $700 (+35%). If S falls to $15 → loss $500.
- **Buy options**: 2,000 calls. If S rises to $27 → payoff (27 − 22.5) × 2,000 = $9,000, profit $7,000 (+350%). If S ends below $22.50 → lose the full $2,000.
- The lesson: options turn the same view into a far more leveraged, asymmetric bet.

## Key Takeaways
1. Every derivative can be reduced to a payoff at maturity. Draw it first.
2. Forwards/futures lock in a price. Options provide a floor/cap and cost a premium.
3. OTC markets are now largely centrally cleared or collateralized. Credit risk is managed, not gone.
4. Arbitrage keeps derivative prices consistent with spot prices. No-arbitrage is the core valuation axiom.
5. Derivatives are versatile enough to be dangerous. Operational controls matter as much as models.

## Connects To
- **Ch 2**: futures mechanics (margin, clearing).
- **Ch 5**: no-arbitrage pricing of forwards.
- **Ch 10–12**: options markets, bounds and strategies.
- **Ch 37**: the mishaps (SocGen, Barings…) as lessons in controls.
