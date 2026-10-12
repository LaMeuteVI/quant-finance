---
name: quant-verification
description: "The discipline of recomputing every formula and every number in a quant skill chapter before publishing. Use after every chapter write, every worked example, every formula extraction. The rule: if a number cannot be verified by a one-line Python script, it does not get into the chapter. Covers the verification toolkit (NumPy, SciPy, pandas, statsmodels), the cross-check protocol (symbolic vs. numerical, hand vs. script), the error taxonomy (OCR garbage, off-by-one, wrong units, wrong sign), and the audit trail (versioned scripts in the skill's tools/ folder)."
---

<!-- argument-hint: [formula name, chapter, or error type] -->

# Quant Verification

**Source**: The institutional verification protocol, derived from book-to-skill chapter writing and the WRITER_BRIEF in this library. | **Domain**: Fondamentaux | **Chapters**: 5 | **Generated**: 2026-10-12

## How to Use This Skill

- **After writing a chapter** with formulas or worked examples, run the verification script.
- **For a specific error type** (e.g. "OCR garbage", "off-by-one", "wrong sign"): use the chapter to identify and fix.
- **For the cross-check protocol**: see ch04.

## The Rule

**If a number cannot be verified by a one-line Python script, it does not get into the chapter.**

## Chapter Index

| # | Title | File |
|---|---|---|
| 1 | The Verification Toolkit | [ch01](./chapters/ch01-the-verification-toolkit.md) |
| 2 | The Cross-Check Protocol | [ch02](./chapters/ch02-the-cross-check-protocol.md) |
| 3 | The Error Taxonomy | [ch03](./chapters/ch03-the-error-taxonomy.md) |
| 4 | The Audit Trail | [ch04](./chapters/ch04-the-audit-trail.md) |
| 5 | Worked Examples of Verification | [ch05](./chapters/ch05-worked-examples-of-verification.md) |

## Related Skills

- **`lopez-de-prado-afml`** (gestion-de-portfeuille) — every chapter has recomputed examples.
- **`grinold-kahn-apm`** (gestion-de-portfeuille) — every chapter has recomputed examples.
- **`hull-risk-management`** (finance-de-marche) — every chapter has recomputed examples.
- **`book-to-skill`** — the parent pipeline.

## Scope & Limits

- **Coverage**: 5 chapters on the verification discipline.
- **What this skill is**: the *protocol* for verifying formulas and numbers. The methodology is in the source skills.
