# Chapter 18: Entropy Features

> López de Prado, AFML, Chapter 18, pp. 263–279.

## Core Idea

**Entropy features** capture the *information content* of the price/volume process. The **Shannon entropy** `H(X) = -Σ p(x) log p(x)` measures the average information; the **Kullback-Leibler divergence** `KL(p || q) = Σ p(x) log(p(x)/q(x))` measures the distance between two distributions. For **financial time series**, the **binarised entropy** (encoding the sign of the return), the **plug-in (bin-counting) entropy**, and the **Lempel-Ziv complexity** are the most useful.

## Key Concepts

- **Shannon entropy** — `H(X) = -Σ p(x) log p(x)`.
- **KL divergence** — `KL(p || q) = Σ p(x) log(p(x)/q(x))`; asymmetric, non-negative.
- **Jensen-Shannon divergence** — symmetric version; `JS(p, q) = 0.5 × KL(p || m) + 0.5 × KL(q || m)` with `m = 0.5 × (p + q)`.
- **Binarised entropy** — encoding the sign of the return; useful for short-term signals.
- **Plug-in entropy** — bin-counting estimator; sensitive to bin size.
- **Lempel-Ziv complexity** — the number of distinct patterns in the sequence; captures structural complexity.
- **Permutation entropy** — the entropy of the ordinal patterns; captures non-linear dependence.
- **Sample entropy** — the conditional probability that two similar segments remain similar; captures regularity.

## Formulas & Tables

- **Shannon entropy**: `H(X) = -Σ p(x) log p(x)`.
- **KL divergence**: `KL(p || q) = Σ p(x) log(p(x)/q(x))`.
- **Lempel-Ziv complexity**: the number of distinct substrings in the sequence.
- **Permutation entropy**: `H(π) = -Σ p(π) log p(π)`, with `π` the ordinal pattern.

## Key Takeaways

1. Entropy features capture the *information content* of the process.
2. The binarised entropy is the most useful for short-term signals.
3. The Lempel-Ziv complexity captures structural complexity.

## Connects To

- ch02 (Financial Data Structures), ch19 (Microstructural Features), `hull-derivatives` ch26 (Numerical Procedures).
