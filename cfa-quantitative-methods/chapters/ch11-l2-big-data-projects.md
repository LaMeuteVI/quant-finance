# Chapter 11: Big Data Projects
> **Source**: CFA Program Curriculum 2022, Level II, Reading 5 · Quantitative Methods | Mallikarjun, Abbasi

## Core Idea
A big data project is an iterative pipeline: conceptualize, collect, prepare and wrangle, explore, train. For unstructured text the same pipeline applies, but the first four steps change (text problem formulation, curation, text preparation, text exploration) so that raw text becomes a structured document term matrix (DTM) a model can read. Most project time goes into data preparation, and a model is only as good as its inputs. Judge it with a held-out confusion matrix (precision, recall, F1, accuracy), ROC/AUC for classifiers and RMSE for continuous targets, then tune hyperparameters on the validation set.

## Learning Outcomes Covered
- identify and explain the steps in a data analysis project (structured vs text)
- describe the objectives, steps and examples of preparing and wrangling data (cleansing, preprocessing)
- describe the objectives, methods and examples of data exploration (EDA, feature selection, feature engineering)
- describe the objectives, steps and techniques of model training (method selection, performance evaluation, tuning)
- describe preparing, wrangling and exploring text data for financial forecasting, and extracting, selecting and engineering text features
- evaluate the fit of an ML algorithm (confusion matrix, precision, recall, F1, accuracy, ROC/AUC, RMSE)

## Frameworks Introduced
- **Model-building steps, structured data**: (1) conceptualization (output, users, business embedding), (2) data collection (internal/external, database, API, vendor), (3) data preparation and wrangling, (4) data exploration, (5) model training. Iterative: results feed re-conceptualization.
- **Text ML steps** (differ in steps 1-4): (1) text problem formulation, (2) data (text) curation (web scraping/spidering, labeling targets), (3) text preparation and wrangling, (4) text exploration (word clouds, text feature selection and engineering), then (5) model training as usual. Output is structured (e.g., sentiment score) and can feed a larger model.
- **Data preparation = cleansing then preprocessing**
  - Cleansing fixes six error types: incompleteness (missing), invalidity (outside valid range), inaccuracy (not true value), inconsistency (conflicts with other fields), non-uniformity (formats/units differ), duplication.
  - Preprocessing (wrangling): extraction, aggregation, filtration, selection, conversion, outlier handling, scaling.
- **Text cleansing** (regex-based): remove html tags, punctuation (keep useful ones as annotations like /percentSign/, /dollarSign/, /endSentence/), numbers (replace with /number/ unless values matter, e.g., information extraction), extra white spaces. Order matters (removing punctuation turns "1.2 million" into "12 million").
- **Text preprocessing**: tokenize; normalize (lowercase, remove stop words, stem or lemmatize); build bag-of-words (BOW); build the DTM (rows = documents, columns = tokens, cells = counts or TF/TF-IDF); n-grams to keep word order.
- **Data exploration = EDA + feature selection + feature engineering.**
- **Model training = method selection, performance evaluation, tuning**; split data 60/20/20 (train / validation (CV) / test); fix class imbalance by under- or over-sampling.

## Key Concepts
- **3Vs + veracity**: volume, variety, velocity; the fourth V, veracity, is credibility and reliability of sources (10-15% of social media content may be fake).
- **Structured vs unstructured data**: structured fits a data table; unstructured (about 80% of all data) must be transformed first.
- **Data cleansing vs wrangling**: cleansing removes errors; wrangling transforms (extract, aggregate, filter, select, convert) and scales.
- **Outlier detection**: standard deviation (beyond 3 SD, for normally distributed data); IQR rule (beyond Q3 + 1.5 IQR or below Q1 − 1.5 IQR; 3.0 IQR flags extreme values).
- **Outlier treatment**: trimming/truncation (remove, e.g., 5% trimmed = drop top and bottom 5%); winsorization (replace by the max/min of non-outlier values).
- **Normalization vs standardization**: normalization rescales to [0,1] (needs no distribution assumption, sensitive to outliers); standardization centers to mean 0, SD 1 (less outlier sensitive, assumes roughly normal data). Remove outliers before scaling; scale for SVM and neural nets.
- **Stop words, stemming, lemmatization**: stemming is rule-based (Porter: "analyzing" to "analyz"), lemmatization returns the dictionary root ("analyze") and is more costly. Both reduce data sparseness.
- **Data sparseness**: many rare, low-frequency tokens; harms training and invites overfitting.
- **BOW vs DTM vs n-grams**: BOW ignores order; DTM is the matrix of BOW counts; bigrams/trigrams keep sequences such as "stock_market" or "no_market".
- **EDA tools**: histograms, box plots, scatterplots, heat maps, word clouds; descriptive statistics; PCA for high dimension.
- **Feature selection**: choose a subset of existing features (parsimonious model). Structured: chi-square, correlation, information gain (univariate scores). Text: term frequency (TF) and document frequency (DF) pruning, chi-square, mutual information (MI; 0 if token's distribution is the same across classes, toward 1 if token appears mainly in one class).
- **Dimensionality reduction vs feature selection**: reduction (PCA) creates new uncorrelated composite features; selection keeps or drops original features.
- **Feature engineering**: create or transform features. Structured: ratios, logs, bracket dummies (income_above_100k), one-hot encoding, date-time parts. Text: number-length tokens (/number4/), n-grams, named entity recognition (NER) tags, parts-of-speech (POS) tags.
- **Noisy tokens** are both the most frequent (stop words; underfit pressure) and the most sparse (rare terms; overfit pressure).
- **Parameters vs hyperparameters**: parameters are learned from data (regression coefficients, NN weights, support vectors); hyperparameters are set by the modeler (λ, k, tree depth, number of trees, hidden layers, p-threshold).
- **Class imbalance**: a naive model predicting the majority class gets high accuracy but misses the rare event (e.g., defaults); fix with undersampling the majority or oversampling the minority (also synthetic samples).
- **Grid search**: train and cross-validate over combinations of hyperparameter values; pick the combination where training and CV errors are both low and close.
- **Fitting curve**: error vs hyperparameter (complexity). Small λ: low train error, high CV error (variance, overfit). Large λ: both high (bias, underfit). Optimal: both low and similar.
- **Ceiling analysis**: evaluate each component of a multi-stage pipeline to find which sub-model most limits overall accuracy.
- **Sentiment polarity** (robo-readers): positive/negative/neutral view toward a target.

## Formulas & Reference Tables
```
Normalization:        X_norm = (X − X_min) / (X_max − X_min)             range [0, 1]
Standardization:      Z = (X − μ) / σ                                    mean 0, SD 1
IQR outlier bounds:   Q1 − 1.5·IQR  and  Q3 + 1.5·IQR   (3.0·IQR = extreme)

Confusion matrix:               Actual 1     Actual 0
                  Predicted 1     TP           FP (Type I)
                  Predicted 0     FN (Type II) TN

Precision (P)   = TP / (TP + FP)            cost of false positives high
Recall (R)      = TP / (TP + FN)            = sensitivity = true positive rate; cost of false negatives high
Accuracy        = (TP + TN) / (TP + FP + TN + FN)
F1              = 2·P·R / (P + R)           harmonic mean of P and R
False pos. rate = FP / (FP + TN)            ROC x-axis; ROC y-axis = TPR = recall
RMSE            = sqrt( Σ(Predicted_i − Actual_i)² / n )   continuous targets
AUC: 1.0 = perfect, 0.5 = random guess

Text:  TF (collection) = count of token in corpus / total tokens in corpus
       TF (sentence)   = count in sentence / words in sentence
       DF              = sentences containing token / total sentences
       IDF             = ln(1 / DF)                                     (natural log in the reading)
       TF-IDF          = TF(sentence) × IDF
```

**Which tool when**

| Task | Tool |
|---|---|
| Binary classifier, FP costly (flag a good product as bad, buy a false signal) | Maximize precision |
| Binary classifier, FN costly (miss a default, miss fraud) | Maximize recall |
| Balanced overall score, or classes unequal | F1 (accuracy only if classes balanced) |
| Compare classifiers across all thresholds | ROC curve and AUC |
| Continuous prediction | RMSE |
| Numeric text feature weight | TF-IDF (high = frequent in few documents) |

**Method selection guide (reading)**: supervised numeric data: CART, regression; text: GLM, SVM; images: neural nets/deep learning; speech: deep learning; wide data (10,000-100,000 features, few instances): SVM; long data (many instances): neural nets. Unsupervised: dimensionality reduction, clustering, anomaly detection.

## Mental Models
- **Garbage in, garbage out**: cleansing and wrangling dominate project time and drive model quality more than the algorithm.
- **Text to table**: every text pipeline is a conveyor belt that ends in a spreadsheet (DTM); once there, classic ML applies.
- **Precision vs recall as a threshold dial**: raising the p-threshold cuts false positives and raises precision but loses true positives (recall falls); lowering it does the reverse. Choose the cutoff by the cost of each error.
- **Information edge erosion**: bought, pre-cleaned vendor data may have the alpha cleaned out; internal data and custom feature engineering keep the edge.
- **Two noise ends**: both the commonest tokens (no information) and the rarest tokens (spurious fit) are junk; keep the middle.
- **Fit-by-three-samples**: train to learn, validation to tune, test once to certify.

## Worked Example
**Confusion matrix on the reading's balanced sample (Exhibit 24).** 20 observations, 10 per class: TP = 6, FN = 4, FP = 2, TN = 8.
- Precision = 6/8 = 0.75; recall = 6/10 = 0.60; accuracy = 14/20 = 0.70.
- F1 = 2 × 0.75 × 0.60 / (0.75 + 0.60) = 0.90/1.35 = 0.667. F1 sits nearer the smaller of P and R, which is why it is stricter than an arithmetic mean (0.675 here, tiny gap; larger when P and R diverge).
- Verified with python.

**Threshold tuning on the sentiment project (CV set).** Logistic regression (LASSO) on Financial Phrase Bank sentences, p-threshold varied:

| Threshold | TP | FP | FN | TN | Precision | Recall | F1 | Accuracy |
|---|---|---|---|---|---|---|---|---|
| 0.45 | 281 | 41 | 4 | 110 | 0.87 | 0.99 | 0.93 | 0.90 |
| 0.50 | 284 | 38 | 7 | 106 | 0.88 | 0.98 | 0.93 | 0.90 |
| 0.60 (chosen) | 284 | 30 | 7 | 114 | 0.90 | 0.98 | 0.94 | 0.91 |
| 0.75 | 281 | 28 | 17 | 110 | 0.91 | 0.94 | 0.93 | 0.90 |

Moving the threshold from 0.45 to 0.75 trades recall (0.99 to 0.94) for precision (0.87 to 0.91); 0.60 maximizes F1 and accuracy because the project values FP and FN equally. Verified with python (e.g., 0.60: P = 284/314 = 0.9045, F1 = 0.9388, accuracy = 398/435 = 0.9149).

**Overfit diagnosis by AUC.** Unregularized logistic regression: AUC 96.5% train vs 86.2% CV (a gap = overfit). After LASSO: 95.7% train vs 94.8% CV (similar = good fit). A model with every token including stop words and no regularization: 99.1% train vs 89.4% CV, still overfit. High AUC on both sets rules out underfitting.

**TF-IDF arithmetic (reading's corpus, 2,180 sentences).** The token "the": collection TF = 2,397/44,151 = 0.0543; DF = 1,453/2,180 = 0.6665; IDF = ln(1/0.6665) = 0.4057; in sentence 701 sentence-level TF = 6/39 = 0.1538, TF-IDF = 0.1538 × 0.4057 = 0.0624 (python). A common word gets a low IDF, so TF-IDF is low.

**Structured-data wrangling (Exhibits 4-5).** Salary 50,200 + other income 5,000 aggregate into Total Income 55,200; Date of Birth extracted into Age; Name dropped (ID suffices); non-US row filtered; CAD values converted to USD. Aggregation also turned a salary outlier (ID 6) into a non-outlier.

## Anti-patterns
- **Skipping data cleansing**: invalid, duplicate or non-uniform rows (negative income, mixed currencies) silently corrupt training.
- **Leaking across splits**: building the BOW or DTM vocabulary from the full corpus, or tuning on the test set. Build the final BOW from the training corpus only and apply identical preprocessing to CV, test and new data.
- **Reporting accuracy on imbalanced classes**: use precision, recall and F1; rebalance by under- or oversampling the training data.
- **Scaling before removing outliers**: normalization is outlier-sensitive; clean outliers first.
- **Removing every stop word blindly**: words such as "not", "more", "very", "few" carry sentiment in financial text; use frequency analysis to define custom stop words (the reading removed 14 tokens above the 99.5th percentile TF and 714 below the 30th percentile).
- **Dropping numbers when values matter**: fine for sentiment, wrong for information extraction (e.g., pulling monetary values from filings).
- **Confusing feature selection with preprocessing or dimensionality reduction**: selection scores and drops existing features; preprocessing is cleanup; PCA builds new composites.
- **Applying standardization to non-normal data**: standardization assumes roughly normal data; use normalization when the distribution is unknown.
- **Ignoring domain experts**: EDA and feature work without domain knowledge finds spurious relationships.

## Exam Focus & Traps
- Know the six cleansing errors by example: missing = incompleteness, impossible value (negative income, birth year 1900) = invalidity, "Don't Know" for a yes/no field = inaccuracy, female title with male gender = inconsistency, mixed date/currency formats = non-uniformity, repeated row = duplication.
- Extraction (new variable such as Age or loan-to-income ratio) vs aggregation (combine several, e.g., Total Income) vs selection (drop a column) vs filtration (drop rows). A ratio of two existing features is feature engineering/extraction, not selection.
- ⚠ Source typo: the reading's IQR bound text reads "-1.5 x IQR + 2nd Quartile" for the lower bound. The correct rule is Q1 − 1.5 × IQR (first quartile). No Reading 5 correction appears in the 2022 Level II errata file.
- Trimming removes outliers; winsorization replaces them with the nearest non-outlier value.
- Stemming (rule-based, can yield non-words) vs lemmatization (true root, more expensive); stemming is more common in English.
- Column of a DTM = a token; cell = count of that token in that document; row = a document.
- Tokenization belongs to preprocessing, not cleansing; the output of text preparation is a DTM.
- Precision uses FP in the denominator (Type I); recall uses FN (Type II). Recall = sensitivity = TPR. FPR = FP/(FP + TN).
- F1 is preferred to accuracy when classes are unequal; accuracy is acceptable for balanced classes.
- AUC 0.5 = random; closer to 1 = better; a more convex ROC curve is better.
- High train error = underfit (bias); CV error much higher than train error = overfit (variance). Small dataset or few features cause underfitting; many features cause overfitting; feature engineering helps underfitting.
- Hyperparameters are set by the modeler (λ, k, depth, number of trees, p-threshold); parameters (coefficients, weights, support vectors) are learned.
- Default split is 60/20/20; unsupervised learning needs no split. Stop words are normally removed for ML but may be kept for context-sensitive applications.
- High-frequency noise tokens cause underfitting pressure, sparse tokens cause overfitting.
- High MI means a token is concentrated in one class; MI = 0 means identical distribution across classes.

## Key Takeaways
1. Follow the five-step pipeline (conceptualize, collect, prepare, explore, train) and expect to iterate; text projects replace steps 1-4 with text-specific versions.
2. Data preparation is where most time goes: cleanse the six error types, then wrangle (extract, aggregate, filter, select, convert, treat outliers, scale).
3. Convert text into a DTM: clean, tokenize, normalize (lowercase, stop words, stem/lemmatize), build BOW (with n-grams if order matters), fill cells with counts or TF-IDF.
4. Select features by pruning noisy tokens (very high and very low frequency) and by chi-square or mutual information; engineer features (n-grams, NER, POS, number tokens, one-hot encoding).
5. Split data 60/20/20, rebalance imbalanced training classes, and keep the test set untouched.
6. Evaluate classifiers with confusion-matrix metrics: precision when FP is costly, recall when FN is costly, F1 as the balance; ROC/AUC for threshold-free comparison; RMSE for continuous targets.
7. Diagnose fit by comparing training and CV error; fix overfit with regularization, fewer features, more data; fix underfit with more features and engineered features.
8. Tune hyperparameters (including the classification p-threshold) on the validation set with grid search and fitting curves; use ceiling analysis for multi-stage pipelines.

## Connects To
- **ch10**: the algorithms (LASSO, SVM, CART, neural nets) that this chapter's pipeline feeds; bias-variance and cross-validation theory.
- **ch07**, **ch08**: logistic regression and LASSO are regression extensions; multicollinearity and heteroskedasticity checks reappear in feature selection.
- **ch09**: for time-series data, shuffling splits is invalid; use walk-forward validation and out-of-sample RMSE.
- **ch02**: descriptive statistics, quartiles and outliers used in EDA and cleansing.
- **`cfa-portfolio-management`**: using ML signals in systematic strategies; out-of-sample and backtest discipline.
