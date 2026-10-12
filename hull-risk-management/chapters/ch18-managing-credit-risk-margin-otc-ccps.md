# Chapter 18: Managing Credit Risk: Margin, OTC Markets, and CCPs
> **Source**: John C. Hull, *Risk Management and Financial Institutions*, 4th ed., Wiley 2012 | Ch. 18, pp. 383–397

## Core Idea
Credit risk on a derivatives book is managed by three levers that all point the same way: **margin, netting, and central clearing**. The post-crisis regulatory response pushed all OTC trades toward exchange-like mechanics — mandatory initial margin, third-party custody, restricted rehypothecation, and CCP clearing — so that the distinction between OTC and exchange-traded markets is disappearing.

## Frameworks Introduced

- **Margin account mechanics**: `margin balance = market value of collateral − amount borrowed` (buying on margin), or `margin balance = posted margin − cumulative P&L` (futures). Two triggers: **initial margin** at trade date, **maintenance margin** thereafter; breaching the maintenance level triggers a margin call.
  - *When to use*: sizing leverage, computing liquidation risk, and estimating the liquidity drain of a derivatives book.
  - *Failure mode*: margin is a *cash* constraint, not a capital constraint. A book can be fully solvent on VaR and still default on a margin call — this is the mechanism behind every 2008-style dealer failure.

- **Margin parameters (book's table)**

| Product | Initial | Maintenance | Restored to |
|---|---|---|---|
| Buying shares on margin (example) | 50% | 25% | maintenance |
| Short sale (example) | 150% | 125% | maintenance |
| Futures via broker (example) | $6,000/contract | $4,500/contract | **initial** |
| Purchased options ≤ 9 months (US) | 75% of option value | 75% | maintenance |
| Written call on stock | `max(100%·option + 20%·S − OTM, 100%·option + 10%·S)` | same | maintenance |
| Written put on stock | `max(100%·option + 20%·S − OTM, 100%·option + 10%·K)` | same | maintenance |

  Fully covered calls (short call against owned stock) carry **no** margin.

- **CCP structure and default waterfall**: the CCP interposes itself, so the two counterparties have no exposure to each other. On member default the CCP closes out and the loss waterfall is:
  1. defaulting member's initial margin,
  2. defaulting member's default fund contribution,
  3. other members' default fund contributions,
  4. CCP skin in the game / equity.

- **Post-crisis bilateral margin rules**: initial margin must cover a **10-day stressed period at 99% confidence**, held by a third-party custodian or segregated. Collateral may be **two-sided or one-sided**; a **threshold** sets the exposure level above which variation margin is called; a **minimum transfer amount** suppresses small exchanges. For CCPs the initial margin is typically set to cover market moves over **five days at 99%**.

- **Price alignment interest**: the CCP pays interest on collateral it holds and charges interest on collateral it has posted, so the economics do not penalise the party posting margin.

- **Rehypothecation**: pre-crisis, ~$4 trillion of collateral demand was met by ~$1 trillion of new collateral — each unit of collateral was used about **4 times**. Post-crisis rules allow **initial margin to be rehypothecated once** under conditions; variation margin may be rehypothecated. Lehman's bankruptcy made CSAs banning or capping rehypothecation standard.

## Key Concepts
1. **Initial vs variation margin** — the buffer against future moves vs the daily settlement of realised moves.
2. **Haircut** — the percentage by which a security's value is reduced when credited to a margin account (T-bills 10%, equities 30% in the book's illustration).
3. **Independent amount** — the bilateral-market name for initial margin.
4. **Threshold** — exposure below which no variation margin is called (e.g. $10m threshold ⇒ no call at $9m, $1m call at $11m).
5. **Minimum transfer amount** — avoids churning collateral on small exposures.
6. **Netting** — all trades between two parties (or a party and a CCP) treated as one transaction for margin and for early termination. Reduces credit risk because a defaulter cannot walk away from out-of-the-money trades. Example: +$10m and −$4m behave as +$6m for IM.
7. **Close-out netting value `V*`** and collateral `C*`; the surviving party's claim is `max(V − C, 0)` and the payment to the defaulting party is `max(C − V, 0)`.
8. **CCP waterfall** — the loss-absorption order above; skin in the game is what makes member admission and margin setting decisions disciplined.
9. **SEF / OTF** — swap execution facility (US) vs organised trading facility (EU); often auto-routed to a CCP.
10. **Convergence** — OTC moving toward exchange-like (centralised, margined, transparent); exchanges adding less standardised products. Whether a trade clears on an exchange or a CCP may cease to matter.
11. **Two-dimensional economics** — a project attractive on capital can be unattractive on liquidity; a 2-D capital/liquidity metric replaces the single RAROC metric (see ch 26).
12. **Too-big-to-fail substitution** — the risk moves from dealers to CCPs. Regulators accept this because CCPs are structurally simpler to regulate than banks, provided they do not expand outside core intermediation.

## Formulas & Reference Tables

Buying-on-margin account: `MB(t) = shares_value(t) − loan`; initial `MB₀ = (1 − 0.50)·1000·120 = 60,000`, loan 60,000.
Margin call trigger: `MB / shares_value < 0.25`.
Margin call amount: `0.25 · shares_value − MB`.

Futures account: `MB_t = MB_{t−1} − 100 × (S_{t−1} − S_t)`; margin call = `initial − MB_t` when `MB_t < maintenance`.

Bilateral claim: `claim_on_defaulting_party = max(V − C, 0)`; `payable_back = max(C − V, 0)`.

## Mental Models
- **Margin is a liquidity test with a solvency flavour.** Use it when judging whether a strategy survives a gap, not when judging expected return.
- **Netting is only as good as the agreement's legal enforceability.** Basel capital recognises it conditionally; credit analysts should too.
- **Central clearing can *reduce* netting** when mandatory clearing splits a book across CCPs and bilateral sets. Figure 18.3 is the canonical proof: average pre-collateral exposure rose from **40 to 110** (or 70 excluding CCP exposure) once only the standard trades were cleared.
- **CCP margin must be met immediately.** There is no grace period — that is why CCP access is a liquidity-rationing event.
- **Every unit of collateral used 4 times pre-crisis.** Any stress scenario that assumes collateral can be recalled simultaneously is fine; any scenario that assumes it can be *reused* simultaneously is not.

## Code Examples
`⚠ reconstructed` — margin call engine and close-out arithmetic.

```python
def margin_call_buying_on_margin(shares, price, loan, init_pct, maint_pct):
    MV = shares * price
    MB = MV - loan
    call = max(0.0, maint_pct * MV - MB)
    return dict(MV=MV, MB=MB, ratio=MB / MV, margin_call=call,
                new_loan=MV - (maint_pct * MV) if call > 0 else loan)

print(margin_call_buying_on_margin(1000, 78, 60_000, 0.50, 0.25))
# MV 78000, MB 18000, ratio 0.2308, call 1500.0, new_loan 58500

def closeout_claim(V, C):
    """V = MtM to the surviving party; C = collateral net held (positive = held)."""
    return dict(claim=max(V - C, 0.0), payable_back=max(C - V, 0.0))

print(closeout_claim(V=10e6, C=6e6))    # claim 4m
print(closeout_claim(V=-3e6, C=-1e6))   # surplus collateral: payable back 2m
```

## Worked Example

**Buying on margin (recomputed, matches the book).** 1,000 shares at $120 = $120,000; initial margin 50% ⇒ $60,000 deposit, $60,000 loan.
Price → $110: MV 110,000, MB 50,000, ratio 45.45% > 25% ⇒ no call.
Price → $78: MV 78,000, cumulative loss 42,000, MB 18,000, ratio **23.08% < 25%** ⇒ call.
Call = `0.25 × 78,000 − 18,000 = 1,500`. After posting, the loan falls to `78,000 − 19,500 = 58,500`.
**Read-across**: the trader was liquidated by a 35% price move, not by a 100% move. That is what maintenance margin does — it is a leverage constraint masquerading as a risk constraint.

**Futures margin call (recomputed).** 100 oz gold at $1,680; IM $6,000, MM $4,500. Day 1: gold → $1,670, loss $1,000, balance $5,000 (> MM, no call). Day 2: gold → $1,660, further loss $1,000, balance $4,000 < $4,500 ⇒ call of **$2,000** to restore to the **initial** level (not the maintenance level — futures differ from margin loans here).

**Figure 18.3 recomputed.** Three dealers, one CCP, two product types (one clearable, one not). Average pre-collateral exposure: bilateral only `(0+100+20)/3 = 40`; with CCP including CCP exposure `(120+120+90)/3 = 110`; excluding CCP exposure `(0+120+90)/3 = 70`. **Mandatory clearing raised gross exposure by 75–175%** because cleared trades can no longer be netted against uncleared ones.

## Anti-patterns
- Treating a derivatives book as funded by capital alone, ignoring the collateral it must post.
- Assuming netting benefits survive a dispute over which trades belong to the netting set.
- Assuming a bilateral CSA with a large threshold and no independent amount is "netting collateralised" — it is unsecured above the threshold.
- Counting rehypothecated collateral as if it were available to meet a simultaneous margin call elsewhere.
- Treating a CCP as risk-free. Hull's own position is that CCP *contracts* can be designed to make failure near-impossible, but only with genuine skin in the game.
- Assuming central clearing always improves netting efficiency. Figure 18.3 says otherwise for partially clearable books.

## Practitioner Notes
- **As of 2026 this chapter's regulatory picture has moved on, and in one direction it has moved *less* than expected.** EMIR/REFIT pushed mandatory clearing across all asset classes in the EU; the EU's `CSA/ISDA Initial Margin requirement` applies to all non-centrally-cleared trades above the threshold. **Post-Brexit, the UK did not implement the EU's mandatory-clearing expansion** — the UK clearing regime remains materially narrower. US Dodd-Frank mandatory clearing applies to designated product types with SEC/CFTC rulemaking. Always state the jurisdiction.
- **CCP resilience is a live research topic after the 2020 "March" volatility events and the 2022 UK gilt/LDI squeeze**, which exposed CCP margin procyclicality and concentration risk that a 2012 chapter cannot contain. Always check a CCP's current default fund, stress losses, and whether the trade you rely on is actually in a CCP.
- **Validation duty for a dealer/asset manager**: run your own collateral stress — size the largest 1-day, 5-day and 10-day margin call on a stressed surface, verify the funding plan covers it, and confirm the margin period of risk in the CSA (10-day IM requirement is on *risk*, not on close-out timing).
- `max(V − C, 0)` close-out arithmetic is the same formula as recovery in ch 20/21 — reuse one implementation.

## Key Takeaways
1. Initial margin + maintenance margin + a margin call is a leverage limit, not a solvency limit.
2. Maintenance margin at 25% liquidates a long equity book after a ~35% move, not a 100% move.
3. Netting is the single largest source of credit relief in a derivatives book — and it is legally conditional.
4. The CCP default waterfall is IM → defaulter's fund → others' funds → CCP equity.
5. Bilateral IM must cover a 10-day stressed 99% period and be segregated; CCP IM is typically 5-day/99%.
6. Central clearing can *increase* gross exposure when a book is only partly clearable (40 → 110 in the book's example).
7. Rehypothecation recycled collateral ~4× pre-crisis; post-crisis IM may be reused only once.
8. Liquidity, not capital, is the binding constraint on post-crisis derivatives profitability.

## Connects To
- **ch 15**: Basel I/Basel II netting (`NRR`) and EAD — the regulatory shadow of this chapter's netting economics.
- **ch 20**: CVA and the wrong-way risk that thresholds, one-sided CSAs and close-out netting create.
- **ch 22**: stress testing the margin call capacity of a book.
- **ch 23**: operational risk — settlement fails, margin disputes, failed CCP access.
- **ch 24**: liquidity risk — the actual constraint identified in this chapter.
- **ch 26**: economic capital and RAROC — the two-dimensional capital/liquidity metric this chapter argues for.
- **ch 27**: enterprise risk management — counterparty exposure limits and wrong-way risk governance.
- **`hull-derivatives`**: CSA mechanics, thresholds, independent amounts, and close-out netting in full.
