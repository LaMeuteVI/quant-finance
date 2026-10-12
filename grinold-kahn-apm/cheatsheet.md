# Cheatsheet — Active Portfolio Management (Grinold & Kahn)

> The judgment layer. Decision rules, thresholds, trade-off matrices.

## When to do X, do Y, because Z

- **When you have a new signal**, run the **rule of thumb** `α = s × IC × σ(θ)`. **Because** it is the universal conversion from signal to forecast; it scales alpha by evidence (IC) and by room to move (σ_θ).
- **When you evaluate a research project**, compute the **Breakeven IC** `√(cost / B)`. **Because** most signals cannot meet the BEIR; only the most promising are worth the cost.
- **When you construct a portfolio**, start from the **unconstrained optimum** `h* = (1/λ) V^(-1) α`, then add **constraints** (long-only, sector neutrality, turnover limit). **Because** the unconstrained optimum is rarely implementable; the constrained optimum is the projection.
- **When you are uncertain about the alpha**, use the **certainty-equivalent** `h*_CE = (1/λ) (V + P)^(-1) α`. **Because** the unconstrained version overweights the most uncertain assets.
- **When you backtest a strategy**, compute the **DSR**. **Because** a backtest SR of 2.5 is *expected* under the null with 100 trials.
- **When you see a high-IR year**, apply the **mean-reversion correction** `IR_next ≈ IR_this × ρ̂`. **Because** the persistence of alpha is empirically weak.
- **When you design a long/short strategy**, account for **borrow cost**. **Because** borrow cost on the short side is the binding constraint; a 3% borrow cost wipes out a 1.4% gross alpha.
- **When you report performance**, use the **Brinson–Beebower–Fachler** decomposition with **Carino smoothing**. **Because** the BBF is the institutional standard; the Carino smoothing makes the components add to the total.
- **When you size a trade**, scale by `1/√cost`. **Because** doubling the cost reduces the optimal size by 30%.

## Decision tree — what kind of strategy is this?

```
Is the signal a fundamental? (P/E, P/B, P/CF, ROE, etc.)
  ├─ Yes → Use the rule of thumb with quarterly rebalancing
  │         Cost: ~5–15 bps per trade, breakeven horizon ~1 quarter
  │         Typical IC: 0.03–0.08; typical IR: 0.3–0.6
  └─ No → Is it a price-based signal? (momentum, mean-reversion)
            ├─ Yes → Use a short-horizon rebalancing (weekly or daily)
            │         Cost: ~2–10 bps per trade, breakeven horizon ~1 week
            │         Typical IC: 0.02–0.05; typical IR: 0.2–0.5
            └─ No → Is it an alternative data signal? (news, satellite, social)
                      ├─ Yes → Use a high-frequency rebalancing
                      │         Cost: ~10–50 bps per trade, breakeven horizon ~1 day
                      │         Typical IC: 0.01–0.05; typical IR: 0.1–0.4
                      │         Capacity is the binding constraint
                      └─ No → Generic signal; default to the rule of thumb
```

## Thresholds & defaults

| Quantity | Default | Range | Source |
|---|---|---|---|
| Risk aversion `λ` | 2.0 (mean-variance 50/50) | 1.0 (risk-seeking) to 10.0 (risk-averse) | ch14 |
| Information horizon | Monthly | Daily to annual | ch13 |
| Information Coefficient | 0.04 (typical) | 0.01 (weak) to 0.10 (strong) | ch10 |
| Breadth | 100–2500 | 10 (low) to 5000 (high) | ch06 |
| Target TE (active equity) | 4% | 1% (low) to 10% (high) | ch14 |
| Breakeven turnover (low-cost) | 100% per year | 10% to 500% | ch16 |
| Capacity (active equity) | $1B per strategy | $50M to $20B | ch16 |
| Borrow cost (typical short) | 1–3% per year | 0.5% to 50% (hard-to-borrow) | ch15 |
| t-stat for significance | 3.0 | 2.0 (low) to 4.0 (strict) | ch20 (Harvey–Liu 2015) |
| DSR threshold | 0.95 | 0.90 (low) to 0.99 (strict) | ch20 |
| Information ratio target | 0.5 | 0.3 (low) to 1.0 (high) | ch06 |

## Tells & smells

- **The strategy has no documented consensus.** → It is probably contaminated with consensus error; the alpha is not real.
- **The in-sample R² is high but the OOS R² is low.** → Look-ahead bias; the strategy used future data.
- **The strategy is profitable in the backtest at $1M but unprofitable at $1B.** → Capacity constraint; the cost is the binding factor.
- **The strategy's borrow cost is > 3% on the short side.** → The short side is value-destructive; consider long-only.
- **The strategy has a 1-year track record of high IR.** → Not enough data; require 3–5 years.
- **The strategy's performance is dominated by the 2008 or 2020 crisis.** → The strategy may be a "crisis beta" rather than a true alpha.
- **The strategy's high-IR years are followed by low-IR years.** → The IR is not persistent; treat it as noise.
- **The strategy's alpha disappears when the universe is expanded.** → The strategy was overfit to a small universe.

## Citation table (2026 institutional standards)

| Item | Threshold | Source |
|---|---|---|
| Multiple testing t-stat | ≥ 3.0 | Harvey, Liu & Zhu (RFS 2015) |
| DSR threshold | ≥ 0.95 | Bailey & López de Prado (JPM 2014) |
| PBO threshold | ≤ 0.10 | Bailey, Borwein, López de Prado & Zhu (JCFE 2016) |
| Post-publication decay | ~26% OOS, ~58% after costs | McLean & Pontiff (2016) |
| Factor persistence | value, momentum, quality: yes; size: weak; others: no | Fama–French 2010; AQR 2018 |
| 130/30 IR boost | 1.26× (theoretical) | Grinold & Kahn ch15 |
| Optimal cost scaling | 1/√cost | Grinold & Kahn ch16 |
| Square-root impact | σ × √(Q/ADV) × Y | Almgren & Chriss 2001; ch16 |
| Traffic-light zone (99% VaR, 250 days) | green 0–4, yellow 5–9, red 10+ | Hull ch12 (cross-ref) |
| Backtest minimum track record | 4+ years of monthly data | LdP ch14 (cross-ref) |

## Connects To

- See `chapters/ch17-performance-analysis.md` for the BBF + Carino smoothing procedure.
- See `chapters/ch14-portfolio-construction.md` for the unconstrained and certainty-equivalent construction.
- See `chapters/ch16-transactions-costs-turnover-and-trading.md` for the cost models.
- See `chapters/ch06-the-fundamental-law-of-active-management.md` for the IR formula.
