# Chapter 3: The Error Taxonomy

> Quant Verification, Chapter 3.

## Core Idea

Errors in quant chapters fall into 6 categories: (1) **OCR garbage** (the extraction garbled a character; e.g. `t^2` became `L^2`), (2) **off-by-one** (the index is shifted; e.g. `t-1` should be `t`), (3) **wrong units** (annualised vs. daily; bps vs. percent), (4) **wrong sign** (the + should be -), (5) **wrong convention** (the Black-Scholes sign convention vs. the Hull sign convention), (6) **stale reference** (the formula has been updated in the literature; the chapter is outdated).

## The 6 Categories

| # | Category | Example | Detection |
|---|---|---|---|
| 1 | OCR garbage | `t^2` → `L^2` | Re-extract; compare to source |
| 2 | Off-by-one | `t-1` → `t` | Run the script; check the index |
| 3 | Wrong units | Annual vs. daily | Check the units in the formula |
| 4 | Wrong sign | + vs. - | Check the convention |
| 5 | Wrong convention | Black-Scholes vs. Hull | Cross-check the source |
| 6 | Stale reference | 1999 APM vs. 2026 LdP | Check the date |

## Key Takeaways

1. The 6 categories cover most errors.
2. The detection method varies by category.
3. The audit trail records the detection.

## Connects To

ch02 (Cross-Check Protocol), ch04 (Audit Trail).
