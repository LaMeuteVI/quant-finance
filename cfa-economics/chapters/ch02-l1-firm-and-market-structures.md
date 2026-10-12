# Chapter 2: The Firm and Market Structures
> **Source**: CFA Program Curriculum 2020, Level I, Reading 13 · Economics | Richard Fritz, Michele Gambera

## Core Idea
Market structure (number of sellers, product differentiation, barriers to entry, pricing power, non-price competition) determines whether a firm's economic profit survives in the long run. Every structure obeys the same rule, produce where `MR = MC`; structures differ in how `MR` relates to `P`, whether the firm has a supply curve, and whether entry competes profits away. For the analyst the real questions are "how high and durable are the barriers?" and "how does the firm's demand elasticity compare with its marginal cost?", not which textbook box the firm falls into.

## Learning Outcomes Covered
- Describe perfect competition, monopolistic competition, oligopoly and pure monopoly
- Relate price, marginal revenue, marginal cost, economic profit and demand elasticity in each structure
- Describe the firm's supply function in each structure (only perfect competition has one)
- Determine optimal price and output in each structure; long-run equilibrium factors
- Describe pricing strategy by structure (kinked demand, Cournot, Nash, Stackelberg, dominant-firm leadership, cartels, price discrimination)
- Use and criticize concentration measures (N-firm ratio, HHI); identify a firm's structure

## Frameworks Introduced
- **Five-factor classification (Exhibit 1)**: number/size of sellers, product differentiation, pricing power, barriers to entry/exit, degree of non-price competition.
  - When to use: first screen for any firm's long-run profit sustainability.
  - How: score each factor; then add (a) regulation, (b) threat of potential entrants (see Porter), (c) high exit costs (non-redeployable assets) which also deter entry.
  - Failure mode: counting sellers while ignoring contestability. A sole supplier facing easy entry prices like a competitive firm.

| Feature | Perfect competition | Monopolistic competition | Oligopoly | Monopoly |
|---|---|---|---|---|
| Sellers | Many | Many | Few | One |
| Product | Identical | Differentiated | Identical or differentiated | Unique, no close substitute |
| Barriers to entry | Very low | Low | High | Very high |
| Pricing power | None | Some | Some to considerable | Considerable |
| Non-price competition | None | Advertising, differentiation | Advertising, differentiation | Advertising |
| Firm demand | Horizontal (elasticity infinite) | Downward, fairly elastic | Depends on rivals (kinked etc.) | The market demand |
| `MR` vs `P` | `MR = P` | `MR < P` | `MR < P` | `MR < P` |
| Supply curve | Yes (the MC curve above AVC) | None | None | None |
| Long-run economic profit | Zero | Zero | Possible, decays with entry | Possible if barriers persist |
| Long-run output | At minimum ATC (`P = MC = min ATC`) | Q < min-ATC output (excess capacity), `P = ATC` | Varies | Q below competitive, `P > MC` |

- **Profit-maximization rule**: `MR = MC` (and, for staying open, `P` at least covers average variable cost in the short run; `P` at least `ATC` in the long run). Price then comes off the demand curve at that quantity, not off the cost curve.
- **Marginal revenue / elasticity link**: `MR = P(1 − 1/ε)` with `ε = |own-price elasticity|`. Profit-max for any firm with pricing power therefore sits where `ε > 1` (MR must be positive to equal a positive MC). `TR` is maximized where `MR = 0` (`ε = 1`).
  - Pricing-power rule: `P = MC / (1 − 1/ε)`; the Lerner markup `(P − MC)/P = 1/ε`.
- **Linear demand shortcut**: if `P = α − βQ`, then `TR = αQ − βQ²` and `MR = α − 2βQ`. MR has the same intercept and twice the slope.
- **Perfect competition**: firm is a price taker, `P = AR = MR`; short-run economic profit if `P > ATC` at the `MR = MC` output; entry shifts industry supply right until `P = min ATC`. Long-run firm supply = LRMC above min LRAC. Schumpeter's cycle (innovation, swarming of imitators, zero profit until the next innovation) reconciles competition with constant innovation.
- **Monopolistic competition**: `MR = MC` for quantity, demand curve for price. Short-run profit pulls in entrants whose products steal demand, shifting each incumbent's demand left until it is tangent to LRAC (`P = ATC`, profit zero) at a point left of minimum ATC. Costs include differentiation spend (advertising). Variety is the social benefit that offsets the excess capacity.
- **Oligopoly demand models**:
  - **Kinked demand**: rivals match cuts, ignore increases. Demand is elastic above the prevailing price and less elastic below, MR has a vertical gap at the kink, so a range of MC shifts leaves price and output unchanged (sticky prices). Weakness: does not explain how the prevailing price was set.
  - **Cournot (simultaneous quantities)**: each firm takes rivals' output as given; equilibrium has symmetric quantities between competitive and monopoly outcomes. With `P = a − bQ`, constant `MC = c`, `N` equal firms: `q = (a − c)/[b(N + 1)]`, `Q = N(a − c)/[b(N + 1)]`; as `N` rises price tends to MC (basis for antitrust thinking about concentration).
  - **Nash equilibrium**: no firm can raise profit by changing strategy unilaterally, given rivals' strategies. Not generally the joint-profit-maximizing outcome (prisoner's-dilemma structure); Cournot is a Nash equilibrium in quantities.
  - **Stackelberg (sequential)**: leader commits to quantity first, follower reacts; leader earns more than in Cournot (first-mover advantage), follower less.
  - **Dominant-firm price leadership**: dominant firm (typically a 40%+ share, usually lowest cost) sets `MR_L = MC_L`, followers take the price and supply the rest; followers do not undercut because a lower-cost leader can win a price war. Leader's share rises at low prices, falls over time as profits attract entry (US Steel 66% in 1901, 42% by 1925).
- **Cartel / collusion success factors (six)**: few sellers or a dominant one; homogeneous products; similar cost structures; frequent, small, regular orders (little scope to cheat); credible severe retaliation; little external competition (OPEC's high price made US shale and tar sands viable).
- **Monopoly**: sources of power are patents/copyright, control of critical resources, government authorization/natural monopoly (economies of scale), brand loyalty, network effects. Output at `MR = MC`, price from demand, so `P > MC` and output below the competitive level (deadweight loss). Monopolists have weak incentive to improve quality or innovate absent a threat of entry.
- **Regulating a natural monopoly (Exhibit 19)**: (1) marginal-cost pricing `P = LRMC` is efficient but, with falling LRAC, leaves `P < LRAC`, so a subsidy is needed (Amtrak-type); (2) average-cost pricing `P = LRAC` gives the owners a normal return (zero economic profit) and output between monopoly and competitive; (3) nationalization; (4) franchise bidding. Regulator's hard job: measure true cost and a fair risk-related return.
- **Price discrimination**: 1st degree (each unit at reservation price, whole consumer surplus captured; output equals competitive); 2nd degree (menu by quantity or quality: volume discounts, bundles, restrictions); 3rd degree (by customer group: student vs professional license, same-day-return airfares); two-part tariff (per-unit price at MC plus fixed fee equal to consumer surplus).
- **Concentration measures**: N-firm concentration ratio = sum of top-N shares; `HHI = Σ sᵢ²` (shares as decimals; regulators often use percent, scale 0 to 10,000). Equal shares give `HHI = 1/M`.
  - Limits of both: ignore barriers/potential entry and demand elasticity; the N-firm ratio barely moves when two top firms merge; neither measures profitability. Ideal (but data-hungry) approach is econometric estimation of demand and supply elasticity with attention to endogeneity (price and quantity are jointly determined, so one needs a two-equation model); time series suffer structural change, cross-sections suffer specification choices.
- **Porter's five forces (cross-link)**: threat of entry, supplier power, buyer power, substitutes, rivalry. Four map onto the Exhibit 1 columns; supplier power is the extra practical force. "Economic moat" = barriers plus switching costs that sustain returns above the cost of capital.

## Key Concepts
- **Economic profit vs accounting profit**: economic profit = TR minus all costs including opportunity cost of owner capital and labor; zero economic profit means the normal return is earned.
- **Normal profit**: the opportunity-cost return on capital embedded in economic cost.
- **Price taker**: a firm whose own output cannot move market price; faces horizontal demand.
- **Marginal revenue**: change in total revenue from one more unit; equals price only when the firm cannot move price.
- **Marginal cost / ATC relationship**: MC cuts ATC at ATC's minimum; MC above ATC pulls average up.
- **Law of diminishing returns**: sets the U shape of MC and ATC.
- **Price elasticity of demand**: `ε = −%ΔQ / %ΔP`; elastic above 1, unitary at 1, inelastic below 1. Rises with number of close substitutes, budget share and time horizon.
- **Income elasticity**: `%ΔQ / %ΔY`; above 1 luxury, below 0 inferior. **Cross-price elasticity** positive for substitutes, negative for complements; high cross elasticity with other products signals weak market power (the DuPont cellophane case).
- **Consumer surplus**: area under the demand curve above price paid; the demand curve is a marginal-value curve.
- **Deadweight loss**: surplus lost because the monopolist restricts output below the competitive level.
- **Natural monopoly**: declining long-run average cost over the relevant market size, so one firm is cheapest.
- **Network effects**: value rises with adoption (exchanges attract liquidity), a barrier to entry in markets and software.
- **Barrier to exit**: non-redeployable assets (smelters); deters entry as much as capital cost.
- **Cartel**: open, formal collusion; implicit collusion works through price signals.

## Formulas & Reference Tables
- Linear demand: `QD = a − bP` → `P = a/b − Q/b`; `TR = (a/b)Q − Q²/b`; `MR = a/b − (2/b)Q`
- `MR = P(1 − 1/ε)`; monopoly pricing `P = MC/(1 − 1/ε)`
- Profit: `π = TR − TC`; economic profit per unit = `P − ATC`
- Perfect competition long-run: `P = MR = MC = min ATC`
- Cournot duopoly, `P = a − Q`, MC = c: `q₁ = q₂ = (a − c)/3`; monopoly `Q = (a − c)/2`; competitive `Q = a − c`
- Stackelberg duopoly (same demand): leader `(a − c)/2`, follower `(a − c)/4`
- Consumer surplus (linear): `½ × quantity × (demand intercept − price)`
- Two-part tariff fee = consumer surplus at price = MC
- `CRₙ = Σ top-n shares`; `HHI = Σ sᵢ²`
- Elasticity effect on revenue: `ε>1: ↑P → ↓TR`; `ε<1: ↑P → ↑TR`

| Structure ranking (typical) | Quantity | Price |
|---|---|---|
| Perfect competition | highest | lowest |
| Cournot oligopoly | between | between |
| Monopoly | lowest | highest (unless scale economies lower its MC) |

## Mental Models
- **MR = MC, then read price off demand**: never read price off the MC curve (except for the price taker).
- **Markup tracks 1/elasticity**: the less substitutable the product, the higher `P − MC`. A static elastic estimate is the quickest pricing-power test.
- **Profit lives behind barriers**: sustained excess returns require patents, scale, switching costs or network effects; otherwise entry erodes them and the speed of erosion is the useful forecast.
- **Cartels cheat**: apply the six-factor checklist; the more members, the more differentiated the product and the more dissimilar the costs, the sooner it breaks.
- **Count the contestability, not just the firms**: concentration ratio and HHI are regulatory screens, not valuation inputs.

## Worked Example
**1. Monopoly with linear demand and cost.** `P = 800 − 2Q`, `TC = 20,000 + 50Q + 3Q²`.
- `MR = 800 − 4Q`, `MC = 50 + 6Q`; `MR = MC` gives `Q = 75`; `P = 800 − 150 = 650`.
- Profit = 650 × 75 − (20,000 + 3,750 + 16,875) = 48,750 − 40,625 = **8,125**. At this point MR = MC = 500.
- Elasticity at the optimum: `ε = P/(P − MR) = 650/150 = 4.33`, in the elastic range as required. Check by the markup rule: `P(1 − 1/4.33) = 500`.

**2. Duopoly with `P = 450 − Q`, `MC = 30` (recomputed).**

| Outcome | Q | P | Profit |
|---|---|---|---|
| Perfect competition | 420 | 30 | 0 |
| Cournot (each 140) | 280 | 170 | 19,600 per firm (39,200 total) |
| Stackelberg | 315 (leader 210, follower 105) | 135 | 22,050 leader, 11,025 follower |
| Monopoly / perfect cartel | 210 | 240 | 44,100 total |

Interpretation: Cournot sits between competition and monopoly. A cartel earns 44,100 joint profit, 22,050 each, above Cournot's 19,600, so each member is tempted to cheat on the quota. Moving first (Stackelberg) lifts the leader's profit above its Cournot level (22,050 vs 19,600) at the follower's expense. With `N` equal firms, price falls 240, 170, 135, 100, 68.2 for N = 1, 2, 3, 5, 10.

**3. Merger arithmetic (shares 35, 25, 20, 10 and four at 2.5).** CR3 = 80%, after merging the top two CR3 = 60 + 20 + 10 = 90%, CR4 = 92.5%. Full-market HHI rises from 0.2375 to 0.4125 (the curriculum quotes the three-firm HHI: 0.225 to 0.410). A merger creating a 60% firm barely moves CR3 relative to the new firm's real power; HHI captures it better.

**4. Two-part tariff.** `QD = 20 − 4P`, MC = 2: Q = 12, consumer surplus = 0.5 × 12 × 3 = 18, so charge 2 per visit plus a fee of 18.

## Anti-patterns
- Assuming concentrated means profitable: ignoring the threat of entry (sugar wholesaler example) and regulation.
- Reading a "supply curve" for oligopolists or monopolists; there is none, quantity depends on demand and rivals.
- Treating the Nash equilibrium as the best outcome for the firms; it generally leaves joint profit on the table.
- Using HHI or CR_N as proof of market power without elasticity and barrier analysis.
- Calling all monopolies inefficient: natural monopolies with scale economies, regulation or contestable entry can beat perfect competition.
- Mixing HHI scales (decimals vs 0 to 10,000) when comparing to regulatory thresholds.

## Exam Focus & Traps
- `MR = MC` is the rule in all four structures; only perfect competition has `MR = P`.
- Monopoly price from elasticity: MC 40, ε 1.5 gives `P = 40/(1 − 1/1.5) = 120` (not average cost 70).
- Perfect-competition entry price from `MC = ATC` (e.g., `ATC = 256/Q + 2 + 4Q`, `MC = 2 + 8Q`: Q = 8, price 66; any price above 66 attracts entry).
- Dominant firm facing an undercutter: leader's share tends to rise as marginal competitors exit; over the long run it falls.
- Collusion is less likely when shares are similar, products differ, costs differ, many sellers.
- HHI disadvantage on the exam: it ignores barriers to entry (low barriers restrict incumbents' power); N-firm ratio ignores mergers among the top firms.
- Nash matrix questions: find each player's dominant or best response; the equilibrium is where both are best responding.
- **⚠ Correction (minor)**: the source's soybean-meal marginal-revenue figures (183.16 and 227.97) round slightly off; `465 × (1 − 1/1.65) = 183.18` and `578.75 × (1 − 1/1.65) = 227.99`.
- **Note on the Nash exhibit (OCR-garbled)**: payoffs (ArcCo, BatCo) are low/low (50, 70), ArcCo low/BatCo high (80, 0), ArcCo high/BatCo low (300, 350), high/high (500, 300). Only high/low is Nash (BatCo's dominant strategy is low; ArcCo's best response is then high); joint profit is maximal at high/high (800), which needs a side payment of at least 51 to hold.

## Key Takeaways
1. Structure is set by seller count, differentiation, barriers, pricing power and non-price competition; long-run profit depends mainly on barriers and contestability.
2. Everyone maximizes at `MR = MC`; price comes from demand; `MR = P(1 − 1/ε)` links markup to elasticity.
3. Perfect and monopolistic competition earn zero long-run economic profit; monopolistic competition ends with excess capacity, perfect competition at minimum ATC.
4. Oligopoly outcomes depend on the strategic model: kinked demand (sticky prices), Cournot (between competition and monopoly), Nash (non-cooperative), Stackelberg (first-mover gain), cartels (unstable).
5. Monopoly restricts output; regulation by average-cost pricing gives a normal return, marginal-cost pricing needs a subsidy.
6. Price discrimination and two-part tariffs transfer consumer surplus to the seller.
7. CR_N and HHI are screens that ignore entry and elasticity; econometric elasticity estimates are better but data-hungry.
8. Dominant-firm shares and cartel prices erode as profits draw entry.

## Connects To
- **ch 01**: elasticity, cost curves, consumer surplus, and shutdown logic reused here.
- **ch 03**: aggregate supply and sticky prices tie to market power and price rigidity.
- **ch 06**: monopolistic competition and scale economies explain intra-industry trade.
- **`cfa-equity-valuation` (industry and company analysis)**: Porter's five forces, moat and pricing power drive competitive-position forecasts.
