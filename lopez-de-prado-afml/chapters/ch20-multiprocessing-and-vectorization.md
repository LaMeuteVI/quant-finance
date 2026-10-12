# Chapter 20: Multiprocessing and Vectorization

> López de Prado, AFML, Chapter 20, pp. 303–318.

## Core Idea

**Multiprocessing** and **vectorization** are the engineering techniques that make ML on financial data tractable. **Vectorization** uses NumPy/Pandas to express operations as array operations; the underlying implementation is C/Fortran. **Multiprocessing** parallelises the computation across cores. The institutional concerns: (1) **look-ahead bugs** (using future data in the parallel computation), (2) **race conditions** (the parallel threads interfere), (3) **memory pressure** (large datasets exceed RAM).

## Key Concepts

- **Vectorization** — replacing Python loops with NumPy/Pandas array operations.
- **NumExpr** — a multi-threaded expression evaluator; faster than NumPy for some operations.
- **Multiprocessing** — parallelising across cores; uses `multiprocessing.Pool` or `concurrent.futures`.
- **Dask** — a parallel-computing library for Python; scales NumPy/Pandas to distributed systems.
- **Joblib** — a lightweight multiprocessing library; the standard for parallel `for` loops.
- **Look-ahead bug** — using future data in the parallel computation; the institutional danger.
- **Race condition** — the parallel threads interfere; the result depends on the order of execution.
- **Memory pressure** — large datasets exceed RAM; chunking or Dask is the response.
- **Reproducibility** — setting the random seed for each process; the institutional discipline.

## Key Takeaways

1. Vectorization is the first step; multiprocessing is the second.
2. Look-ahead bugs are the institutional danger in parallel finance code.
3. Dask is the standard for large-scale finance ML.

## Connects To

- ch21 (Brute Force), ch22 (Forecasting), `hull-derivatives` ch26 (Numerical Procedures).
