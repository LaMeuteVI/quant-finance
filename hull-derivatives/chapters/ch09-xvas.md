# Chapter 9: XVAs

## Core Idea
The "no-default" value of a derivatives portfolio must be adjusted for counterparty default (CVA), own default (DVA), funding (FVA), initial-margin funding (MVA) and capital (KVA). All are computed at the **netting-set** level, not trade by trade.

## Frameworks Introduced
- **CVA** = `Σ qᵢ·vᵢ`.
  - qᵢ = the counterparty's default probability in interval i.
  - vᵢ = the PV of the expected loss if default occurs at the interval midpoint. That is (1 − R) × expected positive exposure, discounted.
- **DVA** = `Σ q*ᵢ·v*ᵢ`: the same formula with the bank's own default probability and the counterparty's expected loss.
- **Portfolio value** = `f_nd − CVA + DVA`.
- **Netting**: all trades under one ISDA master agreement are treated as a single derivative on default. The incremental CVA of a new trade can be negative (it reduces exposure).
- **Collateral**:
  - Variation margin (VM) with threshold/MTA reduces exposure. It does not eliminate it: there is the **margin period of risk**, typically 10–20 days.
  - Initial margin (IM) covers the gap risk.
- **FVA**: the cost/benefit of funding uncollateralized derivatives at the bank's funding rate vs the risk-free rate. Split into FCA (cost) and FBA (benefit, which overlaps with DVA).
- **MVA**: the cost of funding initial margin (CCPs, and the mandatory IM on non-cleared trades).
- **KVA**: the cost of the regulatory capital that the trade consumes over its life.

## Key Concepts
- **No-default value (f_nd)**: the value from standard pricing models, assuming neither side defaults.
- **Exposure**: `max(V, 0)` to the bank at default (after collateral).
- **Wrong-way risk**: exposure is positively correlated with the counterparty's default probability (e.g., selling CDS protection to a bank on a correlated name).
- **Right-way risk**: the opposite, where exposure falls when default probability rises.
- **Early termination / settlement amount**: the close-out value plus half the bid-ask spread for replacement.
- **Monte Carlo exposure simulation**: simulate the market variables, revalue the netting set at each time step, apply collateral rules and average the positive exposure.

## Mental Models
- Think of **CVA as a short option**: the bank is short a default-contingent call on its netting-set value.
- **DVA is counter-intuitive**: the bank's portfolio value rises as its own credit deteriorates. It is controversial in accounting and excluded from regulatory capital.
- **Funding does not change value (finance theory)**, yet banks do charge FVA, MVA and KVA based on average funding costs.
- Price new trades by **incremental XVA** on the netting set, not standalone.

## Anti-patterns
- **Computing CVA trade by trade**: this ignores netting and collateral and overstates the charge.
- **Ignoring wrong-way risk**: exposure and default are not independent in stress.
- **Double counting FBA and DVA**.

## Worked Example
X and Y negotiate an uncollateralized swap. The no-default fixed rate is 2.2%.
- X, accounting only for Y's default risk, will pay only 2.1%.
- Y, accounting only for X's default risk, wants 2.35%.
- With no DVA the parties are 25bp apart and no deal happens.
- When each side also includes DVA (its own default), both value the cash flows symmetrically and converge near 2.2%. DVA restores the zero-sum nature of the contract.

## Key Takeaways
1. Value = f_nd − CVA + DVA. Adjust further for FVA, MVA and KVA.
2. CVA = Σ q_i·v_i. It depends on default probabilities, recovery and expected exposure profiles.
3. Compute XVAs at the netting-set level, including collateral and margin period of risk.
4. Initial margin and capital create real funding costs (MVA, KVA), even though theory says funding should not matter.
5. Watch for wrong-way risk: it is the dominant model error in stress.

## Connects To
- **Ch 2**: CSAs, collateral, CCP margins.
- **Ch 24**: detailed CVA computation, default probability estimation.
- **Ch 25**: CDS used to hedge CVA.
- **Ch 22**: exposure simulation and risk measures.
