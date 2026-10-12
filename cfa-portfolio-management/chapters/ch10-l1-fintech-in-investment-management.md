# Chapter 10: Fintech in Investment Management
> **Source**: CFA Program Curriculum 2020, Level I, Reading 57 · Portfolio Management | Robert Kissell, PhD, and Barbara J. Mack

## Core Idea
Fintech is technology-driven innovation in how financial services and products are designed and delivered. For investment management it matters in five places: analysis of very large (alternative) datasets, AI/machine-learning analytical tools, algorithmic trading, automated advice (robo-advisers) and distributed-ledger record keeping. The practitioner skill is knowing what each tool is good at, what data it needs, and where it fails (overfitting, black-box opacity, data bias, scalability, regulation).

## Learning Outcomes Covered
- describe "fintech" and its areas relevant to investment management
- describe Big Data (3 Vs, traditional vs alternative sources), AI and machine learning
- distinguish supervised, unsupervised and deep learning; explain overfitting/underfitting
- describe data science methods (capture, curation, storage, search, transfer) and visualization
- describe applications: text analytics/NLP, robo-advisory, risk analysis, algorithmic and high-frequency trading
- describe distributed ledger technology (DLT): consensus, blockchain, permissioned vs permissionless, cryptocurrencies, ICOs, tokenization, post-trade, compliance, and its challenges

## Frameworks Introduced
- **Five areas of fintech relevant to investing**: (1) analysis of large datasets, (2) analytical tools (AI/ML), (3) automated trading, (4) automated advice, (5) financial record keeping (DLT).
  - When to use: to classify any fintech claim or product quickly.
  - How: ask which of the five a tool addresses and what data it consumes. Early fintech was data processing and automation of routine tasks, then rule-based execution, now ML decision-making that "learns" over time.
- **Big Data 3 Vs (Volume, Velocity, Variety)**: volume = millions/billions of data points (MB, GB, TB, PB); velocity = real-time or near-real-time arrival; variety = structured (SQL tables, CSV), semi-structured (HTML) and unstructured (video, text, voice).
  - When to use: to judge whether a dataset needs Big Data tooling rather than a spreadsheet.
  - Failure mode: bigger is not better by itself. Check selection bias, missing data, outliers, sufficiency of volume and fit to the analysis type before modelling.
- **ML workflow: train / validate / test**: split the data into a training set (learn input-output relationships), a validation set (tune the model) and a test set (judge out-of-sample prediction on unseen data); only then apply to new data.
  - When to use: any supervised or unsupervised model that will drive investment decisions.
  - How: clean data first; fit on training; tune on validation; report performance on the untouched test set only.
  - Failure mode: **overfitting** (model treats noise as signal, great in-sample, poor on new data, over-complex) versus **underfitting** (model treats true structure as noise, too simple). Black-box opacity makes either hard to detect without a held-out test set.
- **Taxonomy of machine learning**:
  - **Supervised learning**: labeled inputs and outputs; predicts outcomes for new data (e.g., best signal to forecast returns, predicting next-day market up/down/flat).
  - **Unsupervised learning**: no labels; describes structure (e.g., grouping companies into peer groups by characteristics instead of sector/country).
  - **Deep learning (deep learning nets)**: neural networks with many hidden layers doing multistage non-linear processing; can be supervised or unsupervised; strong at image, pattern and speech recognition.
- **Data science pipeline (five processing methods)**: capture, curation, storage, search, transfer.
  - Capture: how data are collected and transformed; **low-latency** systems (minimal delay) are essential for automated trading, **high-latency** systems suffice when real-time data are not needed.
  - Curation: cleaning, detecting bad data, adjusting for missing data.
  - Storage: archive and access design (structured vs unstructured, latency needs).
  - Search: querying very large datasets.
  - Transfer: moving data from source/storage to the analytical tool (e.g., an exchange price feed).
- **Robo-advisory process**: investor questionnaire (general information, risk capacity, risk tolerance, investment goal/horizon) → algorithmic rules plus historical market data → automated asset allocation, trade execution, portfolio optimization, tax-loss harvesting and rebalancing.
  - Two models: **fully automated digital wealth managers** (no human, typically ETF portfolios, deposits, rebalancing, dividend reinvestment) and **adviser-assisted digital wealth managers** (automation plus a virtual adviser for basic planning and periodic phone reviews, more holistic asset/liability view).
- **DLT network anatomy and blockchain transaction steps**: a DLT network has a digital ledger, a consensus mechanism and a participant network. Blockchain steps: (1) transaction occurs, (2) broadcast to nodes, (3) nodes validate details and parties, (4) verified transactions combine into a block, (5) block linked cryptographically (hash) to the previous block, (6) ledger updated, transaction complete.
  - Why it works: altering history would require controlling the majority of nodes and re-solving the cryptographic puzzles, which is prohibitively expensive, so the record is effectively immutable. Failure mode: security is not absolute (privacy and data-protection breaches are possible), and verification (mining) consumes large amounts of energy.

## Key Concepts
- **Fintech**: technological innovation in the design and delivery of financial services and products; also used loosely for the start-up companies and the sector that develops it.
- **Big Data**: datasets of very large volume, velocity and variety from traditional and alternative sources.
- **Alternative data**: non-traditional data from individuals (social media, reviews, web searches, clicks), business processes (transactions, corporate exhaust) and sensors (satellites, geolocation, IoT).
- **Corporate exhaust**: data generated in the normal course of business (supply chain data, banking records, point-of-sale scans); a leading or real-time indicator versus lagging quarterly reports.
- **Internet of Things (IoT)**: network of devices, buildings, vehicles and appliances with embedded sensors and connectivity that share data.
- **Structured / semi-structured / unstructured data**: tabular and database-ready / partly organized (HTML) / not tabular (video, voice, text) and needing custom processing first.
- **Artificial intelligence (AI)**: computer systems performing tasks that previously required human intelligence; early example the rules-based "expert system" (if-then); neural networks used since the 1980s in credit card fraud detection.
- **Machine learning (ML)**: techniques that extract knowledge from large data without assuming an underlying probability distribution; "find the pattern, apply the pattern."
- **Neural network**: layered model loosely based on how the brain processes information; basis of deep learning.
- **Overfitting / underfitting**: model too tuned to noise / too simplistic to capture structure.
- **Data science**: interdisciplinary field (computer science including ML, statistics, others) extracting information from Big Data.
- **Text analytics**: using programs to derive meaning from large unstructured text or voice datasets (filings, reports, call transcripts, surveys); includes lexical analysis (word frequency) and pattern recognition on keywords.
- **Natural language processing (NLP)**: field at the intersection of computer science, AI and linguistics that interprets human language: translation, speech recognition, text mining, sentiment and topic analysis, and compliance monitoring of communications.
- **Algorithmic trading**: computerized trading on pre-specified rules, e.g., slicing large orders across venues, choosing order type and venue.
- **High-frequency trading (HFT)**: algorithmic trading on tick-level data over ultra-low-latency networks, seeking intraday mispricings.
- **Distributed ledger / blockchain**: shared database where each participant holds a matching copy / a DLT in which blocks of entries are chained by hashes and secured cryptographically.
- **Consensus mechanism**: process by which nodes validate transactions and agree on the ledger state.
- **Permissionless vs permissioned network**: open to anyone, all can see and perform all functions, no central authority (bitcoin) / access levels restricted (add transactions, view only, view selected details).
- **Smart contract**: self-executing program with pre-agreed terms, e.g., automatic execution of contingent derivative claims or instant collateral transfer on default.
- **Tokenization**: representing ownership rights to a physical asset as a token on a ledger, giving a single digital ownership and history record.
- **Initial coin offering (ICO)**: unregulated sale of crypto tokens to investors for fiat or crypto, usually for future products/services, typically without voting rights.

## Formulas & Reference Tables
No formulas in this reading. Reference tables:

**Alternative data sources (Exhibit 2)**
| Source | Examples | Typical structure | Investment use |
|---|---|---|---|
| Individuals | social media, news, reviews, web searches, clicks | unstructured text/photo/video/audio | sentiment, consumer interest |
| Business processes | transactions, credit card data, corporate exhaust | mostly structured | real-time/leading sales and performance signals |
| Sensors | satellites, geolocation, RFID, IoT | often unstructured, largest volume | parking-lot traffic, shipping, crop yields, oil rigs |

**Machine learning types**
| Type | Data | Goal | Investing example |
|---|---|---|---|
| Supervised | labeled inputs and outputs | predict outputs for new data | signal to forecast stock returns; up/down/flat next day |
| Unsupervised | inputs only | describe structure | data-driven peer groups |
| Deep learning | either | multi-layer pattern recognition | image recognition of satellite data, speech |

**Programming languages and databases**
| Tool | Use |
|---|---|
| Python | open source, low entry barrier, basis of many fintech apps |
| R | open source, statistics, ML, optimization, econometrics |
| Java | portable, internet applications |
| C/C++ | speed-optimized code for algorithmic and HFT |
| Excel VBA | macros to automate data tables, queries and reports |
| SQL | structured data in tables, server-based |
| SQLite | structured, embedded in the program (mobile apps), no server |
| NoSQL | unstructured data not fitting rows and columns |

**Visualization tools**: tables/charts for structured data; interactive 3D graphics, heat maps, tree diagrams, network graphs for rich data; **tag cloud** (word size = frequency) and **mind map** (shows relations between concepts) for text.

**Permissionless vs permissioned DLT**
| | Permissionless | Permissioned |
|---|---|---|
| Access | open to any user, all see all transactions | restricted roles (participant, regulator view-only, partial view) |
| Authority | none; consensus validates | controlled by permissions |
| Trust between parties | not required | via access controls |
| Example | bitcoin | closed networks for compliance, sensitive data |

**DLT applications and challenges**
| Application | Benefit |
|---|---|
| Cryptocurrencies / ICOs | near-real-time, intermediary-free payments; cheaper, faster capital raising than an IPO but unregulated and fraud-prone |
| Tokenization | single ownership record for real estate, luxury goods, commodities |
| Post-trade clearing and settlement | near-real-time verification, reconciliation and settlement; less counterparty risk, collateral and fails |
| Compliance | near-real-time regulator view, KYC/AML cost reduction, auditability |

Challenges: no network standardization and legacy-system integration, cost competitiveness, storage scale, immutability (errors fixed only by an offsetting trade), high energy use, differing regulation by jurisdiction.

## Mental Models
- **Use alternative data as an early signal, not as truth**: business-process and sensor data are real-time while company reports are quarterly and lagging, but they carry selection bias and legal/ethical risk. Validate against traditional data.
- **Think of ML as "find the pattern, apply the pattern"**: it needs lots of data, a clean sample and a held-out test set; with little data or a regime change, prefer simpler models.
- **Prefer a three-way split over a single in-sample fit**: only performance on the test set speaks for the model.
- **Match the tool to the data structure**: unstructured data need NLP or image recognition before analysis; structured data fit SQL and classical statistics.
- **Think of robo-advice as scalable suitability for simple, passive portfolios**: it wins on cost and access for the mass market; it struggles when portfolios are complex (alternatives, customization) or in crises when clients want human reassurance.
- **Think of DLT as a shared single source of truth**: its value comes from removing duplicated reconciliation and intermediaries, so it fits post-trade processing, ownership records and compliance better than anything needing reversibility.

## Worked Example
**Splitting data for an ML return-prediction model (illustrative numbers).** A quant has 50,000 daily observations for a signal-to-return model.
1. Split 60/20/20: training 30,000, validation 10,000, test 10,000 (sums to 50,000).
2. Fit candidate models on the training set; choose complexity on validation.
3. Suppose model A (simple) scores an error of 1.20 on training and 1.25 on validation; model B (deep network) scores 0.40 on training and 1.60 on validation.
4. Model B's gap (1.60 − 0.40 = 1.20) versus model A's gap (0.05) signals **overfitting**: it learned noise. Select model A, then report its error on the untouched test set.
5. Interpretation: the in-sample score of B is meaningless for forecasting; only validation and test errors matter.

**Reading a robo-adviser design.** Client enters income, savings rate, horizon (risk capacity) and comfort with a drop (risk tolerance). Following the lower-of-ability-and-willingness logic of the IPS (see ch07), the algorithm should assign the more conservative of the two risk scores, then map it to a passive ETF mix and schedule rebalancing. Research cited in the reading finds robo-advisers do not use the full range of available client information, which is a quality gap to monitor.

## Anti-patterns
- **Trusting an in-sample ML fit**: overfitted models find false relationships and fail on new data.
- **Feeding ML dirty or biased data**: selection bias, missing data and outliers produce confident wrong output; curate first.
- **Using alternative data without legal/ethical review**: web scraping can capture protected personal information obtained without consent; rules vary by jurisdiction and may conflict.
- **Deploying a black box nobody can explain**: opaque ML or robo recommendations cannot be justified to clients or regulators.
- **Sending complex wealthy clients to a pure robo-adviser**: customization needs for alternatives and many asset types persist.
- **Assuming robo-advice is unregulated**: US robo-advisers register as investment advisers under the SEC, UK under the FCA, Australia needs an AFS licence; the same conduct standards apply.
- **Assuming DLT is fully secure, free or reversible**: breaches occur, energy cost is large, and an erroneous trade can only be offset, not deleted.
- **Treating ICOs like IPOs**: no regulatory protection, usually no voting rights, documented fraud losses.

## Exam Focus & Traps
- **3 Vs = volume, velocity, variety.** (Not veracity; that is not in this reading.)
- **Three sources of alternative data**: individuals, business processes, sensors. Sensor data is the largest in volume; business-process data is mostly structured; individual data is mostly unstructured.
- **Supervised = labeled (predict); unsupervised = unlabeled (find structure); deep learning = many-layer neural nets that can be either.** Peer grouping is unsupervised.
- **Overfitting = too complex, learns noise; underfitting = too simple.** The overfitted model fails on a different dataset.
- **ML splits data three ways**: training, validation, test. Validation tunes; test evaluates.
- **ML makes no assumption about the data distribution**, unlike many classical statistical methods.
- **Low-latency matters for automated trading; high-latency is fine for non-real-time analysis.**
- **NLP applications**: translation, speech recognition, text mining, sentiment, topic analysis, compliance monitoring. NLP can tag sentiment shifts ahead of a rating change because analysts rarely change buy/hold/sell.
- **Robo models**: fully automated vs adviser-assisted; most are passive and conservative; they serve the mass market and mass affluent.
- **Algorithmic trading vs HFT**: HFT is a subset using tick data and ultra-low latency for intraday mispricings; algorithmic trading broadly lowers cost, adds anonymity and speed.
- **Consensus has two steps**: transaction validation, then agreement on the ledger update. Mining (a cryptographic puzzle) belongs to open blockchains.
- **Permissionless = no central authority, no single point of failure; permissioned = controlled access.**
- **Immutability cuts both ways**: protects records but means mistakes need an offsetting trade.

## Key Takeaways
1. Classify fintech into five areas: large datasets, AI/ML tools, automated trading, automated advice, DLT record keeping.
2. Big Data is defined by volume, velocity and variety; alternative data comes from individuals, business processes and sensors and often leads traditional lagging data.
3. Data quality comes first: capture, curate, store, search, transfer; then validate with train/validation/test splits.
4. Guard against overfitting and black-box opacity; pair ML with human judgment and explainable checks.
5. NLP lets analysts scale reading of filings, calls, news and central-bank statements to thousands of issuers and detect sentiment shifts early.
6. Robo-advisers deliver low-cost, mostly passive, rebalanced portfolios to the mass market; complex and crisis situations still need humans; regulation applies.
7. Algorithmic trading and HFT cut execution costs and fragmentation friction; low-latency infrastructure is the prerequisite.
8. DLT promises faster settlement, tokenization and cheaper compliance but faces standardization, scalability, energy, immutability and regulatory hurdles.

## Connects To
- **ch04**: portfolio management process and the planning/execution/feedback steps fintech automates.
- **ch07**: IPS and risk-tolerance questionnaires that robo-advisers digitize.
- **ch08**: risk analysis, scenario analysis and model risk that ML and real-time data feed.
- **ch09**: technical analysis rules that algorithms implement and that must be backtested.
- **ch14**: backtesting and simulation, the discipline for validating ML and algorithmic strategies (overfitting, data snooping).
- **ch16**: algorithmic trading, electronic markets, dark pools and trading costs in depth.
- **ch17**: trade strategy and execution algorithms.
- **`cfa-quantitative-methods` ch10**: machine learning in depth (supervised, unsupervised, overfitting, evaluation).
- **`cfa-quantitative-methods` ch11**: big data projects workflow, text analytics and NLP.
- **`cfa-ethics-gips`**: suitability and duties to clients that apply to robo-advisers.
