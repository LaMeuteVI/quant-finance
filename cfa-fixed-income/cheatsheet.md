# Cheatsheet — CFA Fixed Income

## Decision rules
| When | Do | Because |
|---|---|---|
| Bond has an embedded option, MBS, floater or liability | Effective duration/convexity on a calibrated tree at constant OAS | Cash flows move with rates; YTM-based duration is invalid (ch 05, 09) |
| Comparing bonds across structures | Use OAS at the same σ | Z-spread ignores option cost; OAS shrinks as σ rises (ch 09, 15) |
| Callable at low rates | Expect negative convexity, capped upside | Investor is short the call (ch 05, 09) |
| Curve can twist | Key rate or factor durations, duration-neutral legs | Effective duration sees only parallel shifts (ch 07, 14) |
| Horizon > MacDur | Fear lower rates (reinvestment) | Gap = MacDur − horizon < 0 (ch 05) |
| Horizon < MacDur | Fear higher rates (price) | Gap > 0 (ch 05) |
| Upward static curve, view = unchanged | Ride/roll down, buy longer than horizon | Unchanged curve is bullish versus forwards (ch 07) |
| Forecast yield < implied forward | Extend/buy that bond | It beats the one-period rate (ch 07, 14) |
| Single liability | MacDur = horizon, minimize convexity | Zero replication (ch 13) |
| Multiple liabilities | BPV_A = BPV_L, convexity_A > convexity_L | Money duration, not % (ch 13) |
| Government market thin or you hedge with swaps | Value off the swap curve | More tenors, dealer-hedged (ch 07) |
| Hedge with futures | Know the CTD; N = ΔBPV/(BPV_CTD/CF) | Wrong CTD shifts the hedge by hundreds of contracts (ch 13, 14) |
| Reduce duration | Pay-fixed swaps or short futures, not cash short | Borrow cost and availability (ch 14) |
| Illiquid bond mark | Matrix pricing from equal-credit comps | Stale last trade (ch 03, 12) |
| Credit risk ranking | Rank by PD × LGD, not rating | Ratings mostly capture PD (ch 06, 10) |
| High yield | Weight liquidity, recovery, structure, covenants | Price tracks recovery near default (ch 06, 15) |
| Credit risk by spread move | DTS, not spread duration alone | Spreads move proportionally (ch 15) |
| Convexity purchase | Only if expecting large moves or higher vol | It costs yield; break-even about ±25bp (ch 14) |
| Slowdown view in credit | Buy HY protection, sell IG protection | Wider HY beta (ch 11, 15) |
| Negative basis | Buy bond + protection | Earn differential on convergence (ch 11) |
| Pension hedge | Rates ≤ swap rate: receive-fixed; moderately higher: collar; much higher: receiver swaption | Payoff shape versus rate view (ch 13) |
| Large pension duration hedge | Prefer swaps to futures | Futures need daily variation margin (ch 13) |

## Decision tree: which duration
1. Option-free, small yield move: modified duration (+ convexity if large).
2. Currency P&L or hedge ratio: PVBP/money duration.
3. Immunizing horizon: Macaulay.
4. Rate-contingent cash flows: effective.
5. Slope/curvature exposure: key rate.

## Trade-off matrix
| Structure | Convexity | Wins if | Loses if |
|---|---|---|---|
| Barbell | Highest | Flattening, more curvature, vol up, big moves | Steepening, low vol |
| Ladder | Middle | Stability, liquidity | Large moves |
| Bullet | Lowest | Steepening, less curvature, vol down | Flattening, big moves |
| Sequential short tranche | — | Extension protection | Contraction |
| PAC | — | Both sides within collar | Collar busted, support exhausted |
| Support tranche | — | Paid for prepayment risk | Everything |
| Cash settlement CDS | — | Holder of bond priced above CTD | Bond priced below CTD |

## Thresholds and defaults
| Item | Value |
|---|---|
| Investment grade | Baa3/BBB− or better |
| CDS standard coupons | 1% IG, 5% HY; DC supermajority 12 of 15 |
| CDS recovery baseline | 40% senior unsecured |
| Spread rule of thumb | s ≈ h × (1 − RR) |
| PSA | 6% CPR at month 30; x PSA scales |
| Curve variance (US Treasuries) | level ≈82%, slope ≈12%, curvature ≈4% |
| VaR z | 1.65 (95%), 2.33 (99%) |
| Altman Z | >3.0 sound, 1.8–3.0 grey, <1.8 distressed |
| Sovereign debt/GDP | <30% good, >100% poor; interest/revenue <5% good, >15% poor |
| Liquidity (bid-offer) | ~5bp very liquid, 10–12bp reasonable, >50bp illiquid |
| Enhanced indexing | +20–30bp alpha, ≤50bp tracking error |
| Futures tick | 1/32 = $31.25 on $100k |
| Tree spacing | e^{2σ} adjacent, e^{2tσ} top/bottom |
| Net debt | Cash may be trapped; prefer debt paydown |
| Recovery by seniority | Loans 80%, senior secured 62%, senior unsecured 48%, subordinated 28% (Moody's L1 data) |

## Tells and smells
- Same rating, lower price: rating lags or higher expected loss.
- "Buy back as much stock as it likes": no restricted-payments covenant.
- Stock below book, big goodwill: weak collateral.
- Credit curve inverted: near-term stress, not long-bond risk.
- Negative swap spread since 2008: dealer balance-sheet cost, not government risk.
- Quoted price differs from spot-curve value: YTM discounting on a sloped curve is not arbitrage-free; the gap is the arbitrage.
- Option-free bond price changes when σ changes: tree not calibrated.
- Support tranche shrinking: PAC protection fading.
- Credit card ABS in lockout: no prepayment risk; early amortization trigger is the exception.
- Implied PD far above history: risk-neutral premium, liquidity, tax, not a forecast.
- Sticky basis: repo funding, embedded options, off-par prices.

## Exam traps
| Trap | Correct answer |
|---|---|
| Spot vs forward notation "2y5y" | 5-year rate starting in 2 years |
| Periodicity conversion | Lower frequency needs higher APR |
| Discount rate vs add-on | DR understates; convert via price to BEY |
| FRN reset | Coupon uses prior-date reference rate; QM > DM = premium |
| Duration gap sign | MacDur − horizon; positive fears higher rates |
| Put effect on duration | Lowers it; putables always positively convex |
| Callable/putable when yields rise | putable falls least < callable < option-free |
| Convexity annualization | ÷ m², duration ÷ m |
| Tree calibration | Does not find mispriced benchmarks; σ affects only options |
| Monte Carlo paths | More = precision, not truth |
| Model type | Ho–Lee and KWF arbitrage-free; CIR (√r vol) and Vasicek equilibrium |
| Option-free value of tree vs σ | Unchanged |
| Convertible premium per share | Market conversion price − share price |
| Index CDS "buy" (CFA) | Long credit; single-name buy protection = short credit |
| CDS upfront | (spread − coupon) × duration; spread > coupon buyer pays |
| Restructuring | Not a credit event in North American standard contract |
| Basis sign | CDS − bond spread; negative = bond wider |
| CDS recovery vs R31 | CDS RR on principal; bond CVA RR on exposure incl. coupon |
| Secured vs unsecured | Second lien beats senior unsecured; pari passu ignores maturity |
| Notching | Larger at lower ratings; IG ≤ one notch |
| Hazard POD | POD_t = h × POS_{t−1}, not h |
| Migration | Use end-of-horizon duration, current rating row |
| Nf sign | (BPV_L − BPV_A)/BPV_fut; negative = sell |
| Receive-fixed swap | Positive duration |
| Parallel shift in immunization | Sufficient, not necessary; twists hurt |
| Wholesale funds | Central bank, interbank, large negotiable CDs; not repo |
| Single-price auction | All winners get the stop-out yield |
| Repo naming | Dealer view: repo = borrows cash; special collateral = lower repo rate |
| Haircut | Higher for longer term, weaker collateral |
| Prepayment | Longest sequential tranche: highest extension, lowest contraction risk |
| PSA first month | 165 PSA CPR = 1.32%, peak 9.9% |
| Butterfly | Reason from yield moves, not labels |
| Rolldown | Needs static curve, not rolling to forwards |
