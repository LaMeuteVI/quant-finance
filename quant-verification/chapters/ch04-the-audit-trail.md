# Chapter 4: The Audit Trail

> Quant Verification, Chapter 4.

## Core Idea

Every chapter write produces a **versioned script** in the skill's `tools/` folder. The script is the *audit trail*: it documents the verification, the assumptions, the libraries, and the version of the chapter. If a chapter is updated, the script is updated. The agent never re-derives a formula; the script does.

## The Audit Trail Format

```
# verify_chXX.py
# Chapter XX of <skill>
# Generated: 2026-10-12
# Author: <agent>
# 
# This script verifies the formulas and worked examples in chapter XX.
# Run: python3 verify_chXX.py

import numpy as np
import scipy.stats as stats
# ... the verification code ...
```

## Key Takeaways

1. Every chapter has a `tools/verify_chXX.py` script.
2. The script is the *source of truth* for the formulas.
3. The script is versioned with the chapter.

## Connects To

ch02 (Cross-Check Protocol), ch05 (Worked Examples).
