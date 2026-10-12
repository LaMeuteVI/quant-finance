# Chapter 3: Monte Carlo Analysis

> **Source**: Diebold & Mariano (1995), Section 3. ⚠ OCR source; reconstructed.

## Core Idea

This section reports the Monte Carlo evidence on the size and power properties of the DM test, the paired t-test, the sign test, and the Morgan-Granger-Newbold (MGN) test. The key finding: the DM test has correct size and reasonable power under all the conditions tested, while the other tests have either wrong size or low power.

## Key Findings

1. **DM test**: correct size (rejects H0 5% of the time when H0 is true at 95% confidence); reasonable power (rejects H0 a high percentage of the time when H0 is false).
2. **MGN test**: correct size only when the loss function is quadratic; incorrect size for non-quadratic losses.
3. **Sign test**: correct size but low power due to ties.
4. **Paired t-test**: correct size when iid; incorrect size in the presence of serial correlation.

## Key Takeaways

1. **The DM test is the institutional default** for two-forecast comparison.
2. **The other tests have specific failure modes** that the DM test addresses.
3. **The Monte Carlo evidence is the empirical justification** for the DM test's adoption.

## Connects To

- **ch01** (DM statistic).
- **ch04** (Empirical Example).
- **ch05** (Conclusions and Future Research).
