# Chapter 2: The Cross-Check Protocol

> Quant Verification, Chapter 2.

## Core Idea

Every formula in a quant skill is verified by **two independent methods**: (1) a *symbolic* check (the formula is dimensionally correct; the units are consistent; the special cases are correct), and (2) a *numerical* check (the formula is recomputed in Python and compared to the chapter's number). A formula that passes only one of the two is suspect.

## The Protocol

1. **Symbolic check**: dimensions, units, special cases (e.g. `lim x→0`, `lim x→∞`).
2. **Numerical check**: Python script recomputes the chapter's worked example.
3. **Hand check**: a third method (e.g. plotting, alternative derivation, literature cross-reference).
4. **Documentation**: the audit trail records all three checks.

## Key Takeaways

1. Two independent methods are required.
2. The symbolic check is the first line of defence.
3. The numerical check catches what the symbolic check misses.

## Connects To

ch01 (Toolkit), ch03 (Error Taxonomy), ch04 (Audit Trail).
