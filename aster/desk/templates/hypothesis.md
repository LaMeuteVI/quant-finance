# Hypothesis: <title>

- **Family**: <family slug, shared by variants of the same idea>
- **Market**: crypto-spot | crypto-perp | crypto-options
- **Source**: <role or reference>
- **Regime context**: trending-up | trending-down | chop | high-vol | any

## Statement (falsifiable)
<Universe, signal, horizon, direction. E.g. "Among the top-20 coins by 30d volume, those in the top quintile of 7d funding rate underperform the bottom quintile over the next 7 days.">

## Mechanism
<Who is on the other side and why do they keep paying? Risk premium / behavioural / structural flow / friction.>

## Falsification
<The exact result that kills it.>

## Prediction (JSON, written before any test)
```json
{"sharpe_ann_min": 1.0, "max_drawdown_floor": -0.30}
```

## Prior evidence and ledger check
<`desk ledger list --text ...` results; literature; why it was not tried or why conditions changed.>

## Cost and capacity sanity
<Gross edge per trade vs round-trip cost; turnover; capacity at 10k / 100k / 1M USD.>

## Register
```bash
uv run desk ledger new --title "..." --statement "..." --mechanism "..." --falsification "..." \
  --prediction '{"sharpe_ann_min": 1.0, "max_drawdown_floor": -0.30}' --family ... --market crypto-spot \
  --source ... --strategy <name>
```
