# Chapter 22: High-Performance Computational Intelligence and Forecasting

> López de Prado, AFML, Chapter 22, pp. 335–348.

## Core Idea

The closing chapter sketches the future of high-performance computing for finance: **distributed computing** (Dask, Spark), **GPU computing** (RAPIDS, cuDF), **neural-network architectures** (Transformer, Mamba, SSM), and the **forecasting frameworks** that combine them. The institutional message: the *problem* is the data and the model, not the compute; more compute without better discipline produces *more* overfitting, not less.

## Key Concepts

- **Distributed computing** — Dask, Spark; the standard for large-scale finance ML.
- **GPU computing** — RAPIDS (cuDF, cuML); 10-100x speedup for some operations.
- **Transformer (Vaswani 2017)** — the attention-based architecture; the workhorse for time series with long memory.
- **Mamba / SSM (State Space Models)** — the linear-time alternative to Transformer; the workhorse for very long sequences.
- **Foundation models for time series** — Chronos, TimeGPT; pre-trained on large datasets, fine-tuned on small.
- **The data discipline** — the institutional message: the problem is the data, not the compute.
- **The reproducibility crisis** — the institutional message: every result must be reproducible.

## Key Takeaways

1. The future is distributed + GPU + Transformer/SSM.
2. More compute without better discipline produces more overfitting.
3. Reproducibility is the institutional discipline.

## Connects To

- ch20 (Multiprocessing), ch21 (Quantum), ch14 (Backtest Statistics).
