# Chapter 21: Brute Force and Quantum Computers

> López de Prado, AFML, Chapter 21, pp. 319–333.

## Core Idea

**Brute force** is the exhaustive search over the model space; the institutional danger is **search overfitting** (ch11). The chapter argues that **brute force is not free** — it requires exponential time, and the OOS performance of the brute-force best model is *typically* no better than a well-designed heuristic. **Quantum computing** is a future technology that may change the trade-off; the **VQE (Variational Quantum Eigensolver)** and **QAOA (Quantum Approximate Optimisation Algorithm)** are the relevant algorithms, but no commercially relevant quantum computer for finance exists in 2026.

## Key Concepts

- **Brute force search** — exhaustive search over the model space.
- **Search overfitting** — the brute-force best model is overfit; the OOS performance is poor.
- **Heuristic search** — gradient descent, random search, Bayesian optimisation; the practical alternative.
- **Quantum supremacy** — the threshold at which a quantum computer outperforms a classical one for a specific task.
- **VQE (Variational Quantum Eigensolver)** — a quantum algorithm for finding the ground state of a Hamiltonian; the basis for quantum chemistry.
- **QAOA (Quantum Approximate Optimisation Algorithm)** — a quantum algorithm for combinatorial optimisation; the basis for future portfolio optimisation.
- **NISQ (Noisy Intermediate-Scale Quantum)** — the current era of quantum computing; small, noisy.
- **Quantum annealing** — the D-Wave approach; commercial but limited.

## Key Takeaways

1. Brute force search is prone to overfitting; the OOS performance is poor.
2. Heuristic search (Bayesian optimisation) is the practical alternative.
3. Quantum computing is a future technology; no commercial relevance for finance in 2026.

## Connects To

- ch11 (Dangers of Backtesting), ch09 (Hyper-Parameter Tuning).
