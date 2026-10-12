# Chapter 3: Market Efficiency
> **Source**: CFA Program Curriculum 2020, Level I, Reading 38 · Portfolio Management (Equity/Markets)

## Core Idea
An informationally efficient market is one in which asset prices reflect new information quickly and rationally. If it holds, consistent risk-adjusted excess returns (net of all costs) are not available, and a cheap passive strategy beats costly active management. The practical question is not "efficient or not" but how much, with respect to which information set (past prices, public information, private information), after which costs, and for which market. Anomalies, behavioral biases and the Grossman-Stiglitz cost argument all sit inside that framework.

## Learning Outcomes Covered
- describe market efficiency and related concepts, including their importance to investment practitioners
- contrast market value and intrinsic value
- explain factors that affect a market's efficiency
- contrast weak-form, semi-strong-form and strong-form market efficiency
- explain the implications of each form for fundamental analysis, technical analysis and portfolio management
- describe market anomalies
- describe behavioral finance and its potential relevance to understanding market anomalies

## Frameworks Introduced
- **Fama's three forms of efficiency (nested information sets)**:
  - Weak: prices reflect all past market data (prices, volume). Technical analysis cannot earn abnormal returns.
  - Semi-strong: prices reflect all public information (includes weak). Fundamental analysis on public data cannot earn abnormal returns.
  - Strong: prices reflect public and private information (includes semi-strong). Even insiders cannot earn abnormal returns.
  - Evidence: developed markets are broadly weak and semi-strong efficient; not strong-form (insider trading earns abnormal profits, which is why it is illegal).
- **Market value vs intrinsic value decision rule**: intrinsic value estimated by discounted cash flow; if estimate > market price, the asset looks undervalued (buy); if < price, overvalued (sell or short). In an efficient market the two coincide on average, so active investing is not justified.
- **Factors affecting efficiency (contribute vs impede)**:
  - Number of market participants and analyst coverage: more is better.
  - Information availability and financial disclosure (Regulation FD, insider-trading rules, market abuse regulation): more is better.
  - Limits to trading (arbitrage obstacles, short-sale restrictions, high trading costs, opaque prices): impede.
  - Transaction costs and information-acquisition costs set the bounds within which a market can be "efficient" while still showing price discrepancies.
- **Event study process**: (1) identify the study period, (2) identify the stocks with the event, (3) estimate expected return for the announcement date (CAPM, market model, index return), (4) excess return = actual − expected, (5) test whether excess returns differ from zero.
  - Interpretation: excess return confined to the announcement date is consistent with semi-strong efficiency; drift after the announcement signals a trading opportunity.
- **Anomaly triage (before exploiting any anomaly)**: Is it persistent out of sample? Does it survive risk adjustment (for example the Fama-French three-factor model)? Does it survive transaction costs? Is there an economic rationale, or is it data mining?
- **Anomaly taxonomy by research method**: time-series (calendar effects, momentum, overreaction), cross-sectional (size, value), other (closed-end fund discount, earnings surprise, IPO underpricing, return predictability).
- **Behavioral finance lens**: loss aversion, herding, overconfidence, information cascades, representativeness, mental accounting, conservatism, narrow framing as candidate explanations of anomalies.

## Key Concepts
- **Informationally efficient market**: prices reflect new information quickly and rationally; prices respond only to the unexpected (surprise) element of releases.
- **Speed of adjustment**: at least as long as the shortest time needed to trade on it; studies in FX and developed equity use windows of a minute or less (NYSE evidence of 5 to 60 minutes).
- **Market efficiency is a continuum**: varies over time, across geographies and across market types (OTC and dealer markets such as bonds, MBS and swaps tend to be less efficient than exchange-listed equities).
- **Market value**: price at which an asset can currently be bought or sold; the supply-demand intersection.
- **Intrinsic (fundamental) value**: value an investor with full understanding of the asset's characteristics would assign; estimated, never observed.
- **Abnormal return**: actual return minus expected return given risk; zero on average in an efficient market.
- **Random walk vs efficiency**: not the same; efficiency does not require returns to follow a random walk.
- **Arbitrage**: set of transactions producing riskless profit; arbitrageurs push prices together.
- **Short selling**: allows exploitation of overvaluation; restrictions impede efficiency and price discovery (although regulators worry it exaggerates declines).
- **Bounds of arbitrage**: price gaps smaller than lowest-cost trader's transaction costs persist without being exploitable; narrow in liquid markets (T-bills), wide in illiquid ones.
- **Grossman-Stiglitz**: prices must pay a return to information acquisition; in equilibrium returns net of research costs are fair returns. Classic view: costs wasted; modern view: market is inefficient only if active investing earns superior returns net of costs.
- **Fundamental analysis role**: even in a semi-strong efficient market it is necessary because analysts' work is how information gets into prices; abnormal profit only with a comparative advantage.
- **Technical analysis role**: exploiting patterns arbitrages them away, helping maintain weak-form efficiency; consistent abnormal profit unlikely in developed markets, some evidence in developing ones (Hungary, Bangladesh, Turkey).
- **Portfolio manager role under efficiency**: not necessarily to beat the market, but to build a portfolio consistent with objectives, diversification, asset allocation, risk preferences and tax situation.
- **Data mining (data snooping)**: searching the data until a profitable pattern appears; the pattern is then likely a chance result.
- **Calendar anomalies**: January effect (small caps, first five trading days; tax-loss selling and window dressing explain only part; not persistent after risk adjustment), turn-of-the-month, day-of-the-week (negative Monday), weekend, holiday effects.
- **Overreaction (DeBondt-Thaler)**: three- to five-year losers outperform and winners underperform subsequently.
- **Momentum**: short-term winners keep winning; contradicts weak form, but may be rational (shocks to expected cash-flow growth).
- **Size effect**: small caps outperform on a risk-adjusted basis, not confirmed out of sample; Fama-French (2008) find it only in microcaps.
- **Value effect**: low P/E, low M/B, high dividend yield stocks outperform growth over long horizons; contradicts semi-strong efficiency if it persists, but disappears under the Fama-French three-factor model (size and book-to-market are risk factors).
- **Closed-end fund discount**: average 4% to 10% below NAV; not exploitable after the cost of buying and liquidating the fund, and discounts revert.
- **Earnings surprise (post-announcement drift)**: positive surprises are followed by superior returns, negative by poor; partly an artifact of unmodeled transaction costs and risk.
- **IPO underpricing**: first-day gains (over 100% in 1995-2000 for many), but poor long-run performance for buyers after the first day, so semi-strong efficiency holds for those later buyers.
- **Return predictability from prior information** (interest rates, inflation, volatility, dividend yield): a link to economic fundamentals is not inefficiency, and the relation is unstable over time.
- **Loss aversion**: losses weigh more than equal gains; could explain overreaction, but under-reaction is just as prevalent.
- **Herding**: trading on the same side, ignoring own information; may cause under- or over-reaction.
- **Overconfidence**: overestimating one's ability to process information; mispricing mostly in growth stocks, usually temporary.
- **Information cascade**: sequential imitation of early movers; fragile if wrong, stronger when information quality is poor.
- **Representativeness, mental accounting, conservatism, narrow framing**: further biases listed in the reading.

## Formulas & Reference Tables
- `Abnormal return = actual return − expected return` (expected from CAPM, market model or index)
- `Excess return in an event study = R_actual,event date − E(R)`
- Rational test of mispricing: `IV − MV > 0` implies undervalued; `IV − MV < 0` overvalued; `IV − MV = 0` fairly valued (efficient market on average).
- Intrinsic value (DCF) `IV = Σ CFₜ/(1 + r)ᵗ`; underestimating risk raises IV via a too-low r and fakes an "inefficiency".
- Net-of-cost test for a strategy: `abnormal return = risk-adjusted gross return − transaction costs − information-acquisition costs`.

| Form | Information reflected | Contradicted by | Implication |
|---|---|---|---|
| Weak | past prices and volume | technical rules that earn risk-adjusted abnormal returns net of costs; strong serial correlation; momentum | technical analysis futile |
| Semi-strong | all public information | event studies with post-announcement drift; value effect; earnings surprise | fundamental analysis on public data futile (absent edge) |
| Strong | public + private | insiders earning abnormal returns | even insiders cannot profit |

| Anomaly | Type | Contradicts | Why often not exploitable |
|---|---|---|---|
| January / small-firm in January | time series | weak (calendar) | tax-loss selling, risk, not persistent |
| Day-of-week, weekend, holiday, turn-of-month | time series | weak | transaction costs, no economic rationale |
| Momentum | time series | weak | may be rational; costs |
| Overreaction (3-5 year reversal) | time series | weak / semi-strong | statistical problems, under-reaction also exists |
| Size | cross-sectional | semi-strong | disappeared out of sample; microcaps only |
| Value (P/E, M/B, yield) | cross-sectional | semi-strong | explained by Fama-French factors |
| Closed-end fund discount | other | semi-strong | liquidation costs; discount reverts |
| Earnings surprise | other | semi-strong | costs and risk not controlled |
| IPO underpricing | other | semi-strong (initial) | only allocated buyers gain; methodology (small, equal-weighted samples) |

| Factor | Effect on efficiency |
|---|---|
| More participants / analysts | increases |
| Opening to foreign investors | increases |
| Disclosure rules (Reg FD), insider-trading law | increases |
| Short-selling bans | impede |
| High trading costs, opaque prices | impede |

## Mental Models
- **Efficiency is a statement about excess returns net of risk and costs, not about prices being "right" in every instance.** Prices can be wrong at times; the test is whether anyone can profit consistently.
- **Nested information sets**: weak ⊂ semi-strong ⊂ strong. A failure of a lower form implies failure of every higher form (strong efficiency implies the other two).
- **Active investors are the market's engine.** If nobody researched, prices would not be informative (Grossman-Stiglitz): efficiency is an equilibrium where research earns only its cost.
- **React to the surprise, not the news.** Pricing reflects expectations; only the unexpected part moves price. A "good" announcement that was fully expected causes no move.
- **Anomaly = hypothesis test with joint problem.** Detecting an anomaly tests the efficient market hypothesis and the asset-pricing model together. A "value anomaly" that disappears under Fama-French may just be risk the CAPM omitted.
- **Data mining is the null hypothesis for new anomalies** until proven persistent, out of sample and economically motivated.
- **Rational market, irrational individuals can coexist.** Efficiency needs the market to be rational on average and arbitrage to work, not every investor.

## Worked Example
**Bond default announcement (reading, Example 2).** A speculative-grade issuer announces just before the open that it will default; media had already reported cash-only supplier deliveries, deteriorating finances and negotiations on a private bank loan. In an efficient market:
1. The price fully reflects post-default value at the first trades after the open on the announcement day, not before (the announcement removes the chance the bank loan avoids default).
2. The information that matters is that the loan negotiations failed, the only piece first revealed by the announcement.

**Event-study logic.** A firm announces a special dividend. Expected return on the date (CAPM) is 0.10%, actual return 3.10%: excess return 3.00%. If excess returns of this size occur only on the announcement day and are zero afterward, the data support semi-strong efficiency. If positive excess returns continue for weeks, a trader could buy after the announcement and earn abnormal returns, which contradicts semi-strong efficiency.

**Overestimated value from risk misjudgment (Example 3).** Cash flows are accurately forecast, the market is judged efficient, yet intrinsic value exceeds price. Most likely explanation: the analyst underestimated risk, used a too-low discount rate and overstated intrinsic value.

**Cost-bounded arbitrage.** An asset trades at 100.00 on exchange X and 100.15 on exchange Y; the lowest-cost arbitrageur pays 0.20 round trip. The gap is inside the bounds of arbitrage, so it persists without implying inefficiency.

## Anti-patterns
- **Taking a back-tested anomaly as a strategy**: with enough testing, something always worked in the past; require persistence out of sample and an economic rationale.
- **Ignoring transaction and information costs**: gross anomalies (closed-end discounts, reversals inside the bid-ask spread, calendar effects) vanish net of costs.
- **Evaluating an anomaly with an inadequate risk model**: size and value "anomalies" partly vanish under multi-factor risk adjustment.
- **Equating "efficient" with "random walk"** or "efficient" with "price is right every time".
- **Concluding "market inefficient" from a delayed or muted reaction without checking** for uncertainty or confusion (Tesla "funding secured" example).
- **Concluding fundamental analysis is useless**: it is the mechanism of price discovery; the question is whether *you* have an edge.
- **Using weak-form-efficiency evidence for emerging markets**: some developing-market studies find exploitable technical rules.
- **Assuming behavioral bias automatically yields a profit**: bias explains mispricing; whether it can be exploited is a separate, unproven question.

## Exam Focus & Traps
- **Price changes in an efficient market are driven by new information**, not by insiders' private information (strong form is not expected) and not by yesterday's price change.
- **Nested forms**: semi-strong efficient implies weak-form efficient (distractor: "semi-strong markets are not necessarily weak-form efficient" is wrong).
- **Identify the form from the information set**: past prices and volume only = weak; all public = semi-strong; plus private = strong.
- **Which evidence contradicts which form**: technical rule profits or momentum contradict weak; value effect / earnings surprise drift contradict semi-strong; profitable insider trading contradicts strong.
- **Efficient market: intrinsic value minus market value = zero** (on average). Undervalued asset: intrinsic value > market value; market value is the price at which the asset can currently be bought or sold.
- **Regulation**: restricting participation (for example foreign traders) or short selling impedes efficiency; insider-trading penalties and disclosure rules contribute to it. Allowing short sales increases efficiency.
- **More participants and analyst coverage increase efficiency** (the small-cap example).
- **Trading costs define the bounds of arbitrage**; a violation inside the bounds is not an inefficiency.
- **Reading's evidence summary**: developed markets weak and semi-strong efficient, not strong-form; emerging markets less so; mutual funds on average match the market before fees and lag after fees.
- **January effect**: tax-loss selling and window dressing explain part; not persistent after risk adjustment.
- **Overreaction vs momentum**: long horizon (3-5 years) reversal vs short horizon continuation.
- **IPO**: underpricing (first-day gains) is real, but subsequent investors earn below-average returns.
- **Behavioral finance**: a market can be efficient even if some participants are irrational (herding); efficiency only requires that investors cannot consistently beat the market risk-adjusted.

## Key Takeaways
1. Efficiency = prices reflect information quickly and rationally; only surprises move prices.
2. Three forms: weak (past market data), semi-strong (public information), strong (all information); evidence supports weak and semi-strong in developed markets, not strong.
3. Efficient markets favor passive investing because costs of active management are not recouped; the portfolio manager's role then shifts to objectives, diversification, asset allocation, risk and tax.
4. Fundamental analysis and informed trading are what make prices efficient; edge is possible only with a comparative advantage.
5. Participants, information disclosure and ability to trade (including shorting) increase efficiency; costs set bounds within which mispricing is tolerated.
6. Most anomalies are not persistent, vanish after risk adjustment and costs, or are artifacts of data mining.
7. Behavioral finance explains observed biases but does not prove markets are exploitably inefficient.

## Connects To
- **ch01**: operational efficiency (low trading costs), short selling and information-motivated traders are the preconditions for informational efficiency.
- **ch02**: efficient markets justify index funds and ETFs; size, value and momentum anomalies reappear as equal-weighted, fundamental-weighted and cap-weighted index tilts.
- **ch04-ch06**: passive vs active choice in the portfolio approach; CAPM and multifactor models define the "expected return" used to measure abnormal returns.
- **ch09 (technical analysis)**: weak-form efficiency is the challenge to technical analysis.
- **`cfa-level1-curriculum` ch09-10**: personal revision notes on indexes and market efficiency.
- **`cfa-equity-portfolio-management` ch02**: passive investing, indexing and active-passive allocation under the efficiency debate.
