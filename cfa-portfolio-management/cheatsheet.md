# Cheatsheet — CFA Portfolio Management

## Decision rules
| When | Do | Because |
|---|---|---|
| Rating a manager who does not control client flows | Use TWR | MWR punishes or rewards client timing (ch05) |
| Portfolio is the client's whole wealth | Sharpe or M² | Total risk matters (ch06) |
| Portfolio is a sleeve of a diversified whole | Treynor or Jensen α | Only beta risk is priced (ch06) |
| Ability and willingness to take risk conflict | Take the lower, document | Overstating capacity forces selling (ch07) |
| Pricing one stock | Use β, not σ | Idiosyncratic risk is unpriced (ch06) |
| Choosing a manager | Highest IR, then set σ_A* = TC·(IR/SR_B)·σ_B | IR is skill, risk is a dial (ch15) |
| VaR for options or fat tails | Historical or Monte Carlo | Normal VaR misses non-linearity (ch13) |
| Backtest looks great | Check PIT data, lags, costs, t > 3, other markets | Survivorship, look-ahead, snooping (ch14) |
| ETF held days | Pay for liquidity | Spread and premium dominate (ch11) |
| ETF held years | Pay for low fee and tracking difference | Fee compounds (ch11) |
| Urgent alpha trade | Arrival price algorithm, price limit | Alpha decays (ch17) |
| Rebalance or two-sided list | VWAP or TWAP | No view, low urgency (ch17) |
| Redemption at NAV or index change | Trade at the close | Fund is valued at the close (ch17) |
| Large order, leakage fear | Liquidity seeking or dark aggregator | Hide size, accept partial fills (ch17) |
| Zero VWAP cost on a big order | Check arrival-price IS | You were the VWAP (ch16) |
| Hot manager year | Do not hire on performance alone | Mean reversion makes Type I errors (ch19) |

## Decision tree: which attribution
1. Holdings unavailable (hedge fund)? Returns-based. 2. Active, high turnover? Transactions-based. 3. Low turnover, passive? Holdings-based. 4. Decision process top-down? Brinson-Fachler (country, sector, security). 5. Factor or quant? Factor attribution. 6. Bottom-up stock picker? Position contribution to tracking risk, never sector effects.

## Trade-off matrices
| Index weighting | Tilt | Turnover |
|---|---|---|
| Price | high-priced stocks | low |
| Equal | small, contrarian | highest |
| Cap/float | large, momentum | low |
| Fundamental | value, contrarian | medium |

| VaR method | Best for | Weakness |
|---|---|---|
| Parametric | linear, normal | fat tails |
| Historical | representative lookback, options | past only |
| Monte Carlo | complex, fat-tailed | model risk |

| Cost measure | Includes unfilled? | Bias |
|---|---|---|
| Effective spread | no | understates large orders |
| VWAP | no | zero when dominant |
| Implementation shortfall | yes | horizon-sensitive |

## Thresholds and defaults
- Correlation: < 0.5 useful, > 0.9 almost useless (ch05). Normal ±1/2/3σ = 68/95/99% (ch05, 08).
- VaR z: 1.65 (5%), 2.33 (1%), 1.00 (16%); annual σ/√250 for daily (ch13).
- Tracking error: passive ≤ 0.10%, enhanced ~2%, active 2-6%, aggressive 6-10%+ (ch12).
- IC < 0.20, TC 0.2-0.9, realized IR within ±0.30 (ch15).
- ETF creation unit 50,000 shares; securities lending collateral 102%/105% (ch11).
- Pattern break filters: 3-5% (neckline), 5-10% (trendline); RSI 70/30, stochastic 80/20 (ch09).
- Backtest t-stat > 3.0; K(K−1)/2 correlations (ch14).
- Participation: POV/VWAP ≤ 5-10% of volume; arrival price ≤ ~15% (ch17).
- Recovery gain after loss L: L/(1−L) (50% needs 100%) (ch18).
- IPS review about every 3 years or on major change (ch04).

## Tells and smells
- A "stock picker" whose active return is nearly all one factor tilt (ch12, 18).
- Manager claiming IR near 3.9 from 6,000 "independent" bets (ch15).
- Too-smooth returns, un-explainable strategy, small auditor (ch19).
- Sharpe used on option sellers or trend followers (ch18).
- Auditor or administrator changes at a fund (ch19).
- Quant backtest with zero reporting lag (ch14).
- Annualized 1-week return (ch05).
- All-buy basket treated as risk-neutral (ch17).

## Exam traps
| Trap | Correct |
|---|---|
| Margin return denominator | Equity plus purchase commission, not position (ch01) |
| Long put exposure | Short the underlying (ch01) |
| Total vs price return index | Beginning weights; TR ≥ PR (ch02) |
| Nested forms | Semi-strong implies weak (ch03) |
| Which evidence contradicts which form | Technical/momentum: weak; value, drift: semi-strong; insiders: strong (ch03) |
| DC vs DB risk | DC employee, DB sponsor (ch04) |
| Real after-tax return | Tax first, then inflation (ch05) |
| U formula units | Decimals; A > 0 averse (ch05) |
| ρ = −1 | Zero risk only at w₁ = σ₂/(σ₁+σ₂) (ch05) |
| CML vs SML | CML efficient portfolios on σ; SML all assets on β (ch06) |
| Total risk addition | Variances add, not σ (ch06, 12) |
| Absolute vs relative objective | "Within X of index" is relative (ch07) |
| VaR meaning | Minimum loss at probability p (ch08, 13) |
| Scaling daily VaR | Rescale μ and σ; never ×√T of VaR (ch13) |
| TRIN | Above 1 bearish (ch09) |
| ETF premium | AP creates, sells ETF; discount: AP redeems (ch11) |
| Fundamental model intercept | Not expected return (macro intercept is) (ch12) |
| Survivorship bias | Type of look-ahead; PIT does not fix snooping (ch14) |
| Binary-call IC | 2p − 1 (55% right = 0.10) (ch15) |
| IR vs cash | IR falls when cash added; SR does not (ch15) |
| Effective spread | 2 × cost per share (ch16) |
| IS denominator | S × Pd, not executed shares (ch17) |
| Market-adjusted cost | Uses stock beta (ch17) |
| BF allocation | (wᵢ − Wᵢ)(Bᵢ − B); selection uses Wᵢ (ch18) |
| Sortino downside deviation | Divide by all N periods (ch18) |
| Appraisal ratio | α/σₑ, not variance (ch18) |
| Capture ratio | Read UC and DC separately (ch19) |
| Performance fees and σ | Lower measured σ (ch19) |
