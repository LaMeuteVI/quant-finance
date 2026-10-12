# Chapter 4: Optimal Clustering

> López de Prado, MLAM, Chapter 4.

## Core Idea

**Optimal clustering** of financial assets: the **Gap statistic** (Tibshirani, Walther, Hastie 2001) compares the within-cluster dispersion to a null reference; the **silhouette score** measures how well each point fits in its cluster; the **ONC (Optimal Number of Clusters)** algorithm combines multiple cluster-validity indices. For **hierarchical clustering**, the **cophenetic correlation** measures the dendrogram's fidelity to the original distances.

## Key Concepts

- **Gap statistic** — `Gap(k) = E[log W_k] - log W_k`; compare to the null.
- **Silhouette score** — `s(i) = (b(i) - a(i)) / max(a(i), b(i))`; `a(i)` is the average distance to the same cluster, `b(i)` is the minimum average distance to another cluster.
- **ONC algorithm** — combines multiple cluster-validity indices; robust to noise.
- **Cophenetic correlation** — the correlation between the distance matrix and the cophenetic distances.
- **Ward's method** — the hierarchical clustering method that minimises within-cluster variance.
- **Single-linkage** — the hierarchical clustering method that connects the closest pairs.
- **Average-linkage** — the hierarchical clustering method that uses the average distance.
- **K-means** — the partition-based clustering method.

## Key Takeaways

1. The Gap statistic and the silhouette score are the standard cluster-validity indices.
2. The cophenetic correlation measures the dendrogram's fidelity.
3. The ONC algorithm combines multiple indices.

## Connects To

- ch03 (Distance metrics), ch07 (Portfolio Construction), `lopez-de-prado-afml` ch16 (HRP).
