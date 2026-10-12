# Chapter 10: Machine Learning
> **Source**: CFA Program Curriculum 2022, Level II, Reading 4 · Quantitative Methods | DeRose, Dixon, Le Lannou

## Core Idea
Machine learning (ML) finds patterns in large, high-dimensional, non-linear data with few distributional assumptions, but its flexibility makes overfitting the central risk. Every algorithm choice reduces to three questions: is there a labeled target (supervised vs unsupervised), is the target continuous or categorical (regression vs classification), and is the data non-linear or high-dimensional. Judge any model by out-of-sample error, never by training fit.

## Learning Outcomes Covered
- describe supervised, unsupervised and deep learning
- describe overfitting and the methods that address it (regularization, cross-validation, data partitioning)
- describe penalized regression/LASSO, SVM, KNN, CART, ensemble learning and random forest, and the problems each suits
- describe PCA, k-means and hierarchical clustering, and the problems each suits
- describe neural networks, deep learning nets and reinforcement learning; choose an algorithm with the decision flowchart

## Frameworks Introduced
- **Supervised vs unsupervised vs deep/reinforcement learning**: supervised = labeled data (target Y, features X) used to train a prediction rule; unsupervised = no target, find structure; deep learning/RL = neural-network-based methods for complex tasks.
  - When to use: supervised when you know what to predict (default, rating, return); unsupervised for exploration (peer groups, dimension cut); RL when an agent learns from rewards over time.
  - How: classification if Y is categorical or ordinal, regression if Y is continuous (regardless of the algorithm's name).
- **Three-way data partition**: training sample (fit), validation sample (tune hyperparameters, compare structures), test sample (final out-of-sample check). Training + validation = in-sample; test = out-of-sample.
- **Bias-variance decomposition**: out-of-sample error = bias error + variance error + base error.
  - Bias: model too simple, underfits (high in-sample error). Variance: model too sensitive to the training set, overfits (low in-sample, high out-of-sample error). Base: irreducible noise.
  - Failure modes: high bias shows a learning curve where training and validation accuracy converge below the desired level (more data will not help); high variance shows a persistent gap (more data or less complexity helps).
- **Complexity reduction (regularization)**: add a penalty or structural limit (penalized regression, tree depth, pruning, minimum node size).
- **k-fold cross-validation**: shuffle the non-test data into k equal folds (k typically 5 or 10); train on k−1, validate on 1; repeat k times; average validation error as the estimate of out-of-sample error. Each point is validated once and trains k−1 times.
  - Limitation: not valid for time series (shuffling breaks order); use walk-forward (time-series) cross-validation instead.
- **LASSO (penalized regression)**: minimize `Σ(Yᵢ − Ŷᵢ)² + λΣ|b_k|`, λ > 0. A feature stays only if it cuts squared error by more than the penalty it adds, so LASSO does automatic feature selection. λ = 0 is OLS. The penalty is only used when fitting; evaluation uses plain squared residuals on test data.
- **Algorithm-selection flowchart** (see Formulas & Reference Tables).

## Key Concepts
- **Features / target / labeled data**: X variables, Y variable, and a dataset with matched X and Y.
- **Overfitting**: model memorizes noise in the training data (perfect hindsight, no foresight); contributors are noise in the data and model complexity.
- **Underfitting**: model too simple to capture structure; high bias.
- **Generalization**: model retains predictive power on new data.
- **Learning curve**: validation and training accuracy against training-set size; diagnoses bias vs variance.
- **Fitting curve**: in-sample and out-of-sample error against complexity; the optimal complexity sits just before out-of-sample error starts to rise.
- **Hyperparameter**: a setting chosen before learning (λ, k in KNN/k-means, tree depth, number of trees, SVM cost, network size, learning rate); tuned on the validation set.
- **Regularization**: any method that shrinks complexity/variance (LASSO, pruning, depth limits).
- **SVM**: linear classifier finding the hyperplane that maximizes the margin; the support vectors (nearest points) alone define it; soft-margin penalizes misclassified training points; non-linear kernels risk overfitting.
- **KNN**: classifies a point by majority vote of its k nearest neighbors; non-parametric; sensitive to the distance metric, irrelevant features and k.
- **CART**: binary tree of root, decision and terminal nodes, each split = one feature and a cutoff; classification leaf = majority class, regression leaf = mean of labels.
- **Ensemble learning**: combining many models; voting classifiers (heterogeneous) or bagging (homogeneous, bootstrap samples drawn with replacement).
- **Random forest**: many CART trees trained on bootstrap samples with a random subset of m < n features per split; reduces variance but is a black box.
- **PCA**: transforms correlated features into uncorrelated composite variables (eigenvectors ordered by eigenvalue = share of variance); scree plot guides how many to keep (often 85-95% of variance).
- **K-means**: assigns observations to k centroids and iterates until no reassignment; k fixed in advance.
- **Hierarchical clustering**: agglomerative (bottom-up, local, good for small clusters, fast) or divisive (top-down, global structure, good for large clusters); read via a dendrogram.
- **Neural network / DNN**: layers of nodes (summation + non-linear activation); input, hidden, output layers; DNN has at least 2 hidden layers; trained by forward and backward propagation.
- **Reinforcement learning**: agent maximizes cumulative reward by trial and error in an environment, with no labeled data.

## Formulas & Reference Tables
```
LASSO objective:     min  Σᵢ(Yᵢ − Ŷᵢ)² + λ Σₖ|bₖ|        (λ is a hyperparameter)
Error decomposition: Eₒᵤₜ = bias error + variance error + base error
PCA scree rule:      keep fewest components explaining the target variance (≈85-95%)
k-fold CV estimate:  Êₒᵤₜ = (1/k) Σⱼ E_val,j
Neural net node:     output = f(Σᵢ wᵢxᵢ);  f = sigmoid (0 to 1) or ReLU max(0,x)
Weight update:       new weight = old weight − learning rate × ∂(total error)/∂(old weight)
Avg-linkage dist:    d(A,B) = mean of pairwise distances between members of A and B
```

**Algorithm guide**

| Algorithm | Type | Use case | Strengths | Weaknesses |
|---|---|---|---|---|
| Penalized regression / LASSO | Supervised, regression | Prediction with many (correlated) features; sparse model | Parsimonious, feature selection, stable | Linear; λ must be tuned |
| SVM | Supervised, classification | Binary classification on small/medium, high-dimensional, complex data (bankruptcy, text sentiment) | Robust to outliers and correlated features | Non-linear kernels overfit; margin choice |
| KNN | Supervised, classification | Credit rating of an unrated bond, custom index, similarity problems | Simple, non-parametric, multi-class | Distance metric, k choice, irrelevant features, needs few features |
| CART | Supervised, classification or regression | Non-linear, interacting features; explainable rules (fraud, selection) | Interpretable tree, no distribution assumptions | Overfits unless pruned/limited |
| Random forest | Supervised, ensemble | Factor models, IPO success, rare-event classification | Lower variance, handles non-linearity, robust to noise | Black box |
| PCA | Unsupervised, dimension reduction | Many correlated features, visualization, covariance matrix | Fewer uncorrelated inputs, reduces overfitting | Components hard to interpret |
| K-means | Unsupervised, clustering | Peer groups, large data, diversification | Fast, scales to huge data | k fixed in advance; depends on initial centroids |
| Hierarchical clustering | Unsupervised, clustering | Unknown number of groups; compare granularities | No k required, dendrogram | Heavier computation |
| Neural network / DNN | Supervised or unsupervised | Highly non-linear, large data (option pricing, speech, text) | Flexible, captures interactions | Black box, data and compute hungry, overfits |
| Reinforcement learning | Reward-driven | Trading agent, games, control | No labels needed | Slow, success in markets unproven |

**Decision flowchart** (reading's Exhibit 37)
1. Complexity reduction needed (many highly correlated features)? Yes: PCA.
2. Else numerical prediction (continuous Y)? Linear data: penalized regression/LASSO; non-linear: CART, random forest, neural nets.
3. Else classification with labeled data: linear/simple: KNN or SVM; non-linear: CART, random forest, neural nets.
4. Unlabeled data (clustering): linear data and known number of categories: k-means; unknown number: hierarchical; non-linear: neural nets.

## Mental Models
- **Suit tailoring**: underfit = baggy suit, overfit = custom suit that fits one person, robust fit = a suit that fits everyone of similar size.
- **Complexity is a dial**: linear models tend toward bias, non-linear toward variance; look for the point where out-of-sample error bottoms out.
- **Wisdom of crowds**: average many noisy, diverse models (bagging, random forest) to cut variance; diversity matters more than count.
- **Interpretability tax**: trees and LASSO explain themselves; random forests, SVMs with kernels, and DNNs do not. Pick the simplest model that meets the accuracy need.
- **Domain expert's role**: source inputs, interpret outputs and translate to action; the algorithm will not fix bad features or label leakage.

## Worked Example
**LASSO trade-off.** With λ = 0.5, a feature with coefficient 0.10 adds 0.5 × 0.10 = 0.05 to the penalty; if dropping it raises the squared-residual sum by only 0.02, LASSO shrinks it to 0 because 0.02 < 0.05. A feature with coefficient 2.0 adds a penalty of 1.0 and survives only if it lowers squared error by more than 1.0.

**Average-linkage agglomerative clustering (8 S&P stocks, source distance matrix).**
- Closest pair: JPM-GS at 0.215, merged first.
- UBS to cluster {GS, JPM}: (0.243 + 0.281)/2 = 0.262, so UBS joins at height 0.262.
- AAPL-GOOG merge at 0.307; GM-F merge at 0.334.
- Banks + AAPL/GOOG merge at (0.364+0.380+0.375+0.332+0.338+0.345)/6 = 0.3557 ≈ 0.356.
- Cutting for 3 clusters: {banks, AAPL, GOOG}, {F, GM}, {FB}. For low-correlation picks, buy FB, one of F/GM, one bank. Verified with python (0.262, 0.3557).

**CART leaf probability.** An ETF with P/S 2.29, P/E 7.20, P/B 1.41 reaches the leaf with value [13, 4, 4] (winners, average, losers); P(winner) = 13/21 = 61.9%. Caution: the leaf has only 21 of 1,067 funds and the tree is depth-limited to 5.

## Anti-patterns
- **Judging a model by in-sample fit**: low training error with high test error is overfitting.
- **Tuning hyperparameters on the test set**: leaks information; use a validation set or cross-validation and keep the test set untouched.
- **k-fold CV on time series**: shuffles the time order; use walk-forward validation (train on the past, test on the next period).
- **Unconstrained trees / huge networks**: fit the noise; add depth limits, pruning, LASSO.
- **Unscaled features in distance- or gradient-based models** (KNN, k-means, SVM, neural nets): standardize first.
- **Accuracy on imbalanced classes**: a model predicting "no fraud" always scores 99.8%; use F1/precision/recall (see ch11).
- **Treating a clustering result as truth**: results depend on distance measure, k and initial centroids; check face validity and rerun with different seeds.
- **Reading causality into feature importance**: importance shows association with the label, not cause.

## Exam Focus & Traps
- Regression vs classification is decided by the target type, not the algorithm name (logistic regression is a classifier).
- Penalty term grows with the number of included features (not decreases); penalty applies in training only.
- Bias = underfit (high in-sample error); variance = overfit (low in-sample, high out-of-sample error). High-bias learning curves converge below the target; more data does not fix them.
- SVM maximizes the margin; support vectors determine the boundary; adding points far from the margin changes nothing. KNN needs k set in advance and k too small = noisy, too large = diluted.
- Random forest = bagging + random feature subsets, majority vote; trade-off is interpretability.
- K-means needs k; hierarchical does not. Agglomerative = bottom-up (local), divisive = top-down (global).
- PCA is unsupervised and its components are uncorrelated; eigenvalue = variance explained.
- Neural nets are not "exact models of the brain"; DNN = at least 2 hidden layers; hyperparameters include layers, nodes, learning rate, activation.
- Reading's classic statement: dimension reduction retains as much variation as possible while shrinking the feature set.

## Key Takeaways
1. Pick the algorithm by (labeled?, continuous or categorical?, linear or non-linear?, many correlated features?).
2. Always evaluate on held-out data; partition into training, validation and test samples.
3. Fight overfitting with complexity penalties (LASSO, depth limits, pruning) and cross-validation.
4. Use bias-variance diagnostics: learning curves tell you whether to add data or simplify.
5. Ensembles (bagging, random forest) usually beat a single tree and are the default for tabular non-linear problems; accept the loss of interpretability.
6. Use PCA to compress correlated features before modeling, and clustering to build data-driven peer groups and diversify across clusters.
7. Neural networks and DNNs are for large, complex, non-linear data; they need many observations, tuning, and are hard to explain.
8. For time series and finance, use walk-forward validation and judge strategy value by out-of-sample information ratio, not in-sample MSE.

## Connects To
- **ch09**: time-series validation (out-of-sample RMSE, instability) vs ML cross-validation; walk-forward is the shared principle.
- **ch11**: the project workflow (data prep, feature engineering, model training, evaluation with precision, recall, F1) that wraps these algorithms.
- **ch07**, **ch08**: regression assumptions that ML relaxes; LASSO as the penalized extension.
- **`cfa-portfolio-management` ch12**: factor models where ML (random forest, DNN) is applied.
- **`cfa-portfolio-management` ch14**: backtesting and overfitting discipline (out-of-sample testing).
