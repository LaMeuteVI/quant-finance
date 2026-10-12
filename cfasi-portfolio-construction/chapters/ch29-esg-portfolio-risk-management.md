# Chapter 29: ESG Portfolio Risk Management
> **Source**: CFA Society Italy × Advisor Private (AP Advisor Private n. 13, Sep-Oct 2018), *Investimenti ESG*, Chapter 10 "Gestione del Rischio ESG di portafoglio" | Paolo Capelli (Risk Management, Etica SGR); methods published in CFA Society Italy professional papers

## Core Idea
There is no standard statistical measure of "ESG risk" with a direct economic reading. An ESG score is a level of quality, not a forecast: a weighted average of holdings' ESG scores says how good a fund is, but not how uncertain its ESG profile is. The chapter proposes (1) adding ESG variables to factor-based risk models (the ESG share of Component VaR is about 5.5%), (2) a **entropy-based ESG risk metric (RESG)** computed from portfolio weights and ESG scores, which scales with financial risk (Spearman correlation with undiversified VaR mostly above 0.90), (3) a joint relative-risk indicator (**MRR**) separating ESG selection and allocation effects, and (4) a three-legged holistic risk indicator (VaR, relative VaR, RESG). The message: ESG adds information to ex-ante risk estimation rather than noise.

## Frameworks Introduced
- **ESG and small caps**: regression studies (e.g. Harvard publications) show that for small caps a good ESG score often goes with lower financial risk (e.g. volatility). But traditional asset management prefers large and mid caps for liquidity, so a method is needed that works for large-cap-heavy international equity funds.
- **Adding ESG to fundamental risk factors**: a 2016 PRI practical guide (ESG integration for equity investing) stressed that ESG factors can improve ex-ante portfolio volatility estimates: standard factors (size, value, growth, momentum, style, dividend yield) alone left about 8% unexplained that ESG variables could capture. Test on an international equity fund (mainly large/mid cap): adding ESG factors improves the ex-ante risk estimate versus the traditional factor approach (returns already embed ESG effects implicitly). In a Component VaR decomposition (first-order contributions), the ESG-attributable part is about **5.5% of total VaR**: ignoring it is not the prudent choice.
- **Entropy-based ESG risk (RESG)**
  - Problem: a weighted average ESG score has no ex-ante statistical meaning; a fund may have better average ESG quality than another and still carry higher financial risk.
  - Construction: take Shannon entropy (disorder measures uncertainty) of the distribution of portfolio weight across ESG-score classes (frequency = weight). The authors add a corrective (details in the CFA Society Italy papers) to make the estimate more conservative and to penalize allocation to low-ESG issuers. Inputs: portfolio weights and ESG scores of holdings; applies to equity, bond and balanced funds on an increasing risk scale consistent with the mandate. No correlations are used.
  - Reading: more spread across score classes (more disorder) means higher RESG; the maximum is a uniform allocation across classes, the benchmark for "most uncertain".
  - Empirical findings (about 3 years of monthly data, equity, balanced, bond funds): (1) higher ex-ante financial risk (VaR) goes with higher ESG risk, "perfectly in scale"; the correspondence between VaR levels and RESG holds, especially for undiversified VaR (UVaR, VaR with no diversification benefit, to which RESG is proportional); (2) decomposition by sector and by country: Spearman rank correlation between component ESG risk (CR_ESG) and component UVaR is mostly well above 0.90 (rank correlation: when one is higher, so is the other); (3) correlation is not causation, but persistence suggests ESG variables influence or help explain financial risk; the relation holds at sector and country level, **not necessarily stock by stock** (especially small caps), which is why it is calibrated to large-cap-heavy funds; (4) RESG can show whether active management also mitigates ESG risk compared with a uniform allocation to risk classes.
- **Integrated measurement: MRR (relative risk)**
  - Reference: an equally weighted investment in the whole Investable Universe (issuers chosen with high ESG scores). Joint indicator MRR combines relative financial risk (Relative VaR versus benchmark) and ESG risk (RESG), allowed to move independently. Use: measure true activism in stock selection (alternative to tracking error volatility) and efficiency of ESG allocation; distinguish the **selection effect** from the **allocation effect** (as in performance attribution) in ESG terms.
  - Example for an equity fund (Etica Azionario): since mid-2016 the ESG part of joint relative risk averaged above 6% with a maximum of 11%, and decreased when market volatility (financial component) rose significantly. Exact causes of the dynamics are still under study.
- **Holistic three-legged risk indicator (R)**: VaR, Relative VaR and ESG risk (RESG) as three legs; compare actual values with a tactical maximum (e.g. reset monthly) and a strategic maximum (e.g. annual); the "risk saving" versus these thresholds varies with market conditions and ESG variables.
- **Summary evidence**: ESG share of equity portfolio VaR about 5.5%; ESG risk by sector/country allocation significantly correlated with undiversified financial risk; ESG contribution to relative risk about 6% on average (peak about 11%); keep controlling absolute risk (VaR) and benchmark-relative risk while also watching ESG risk. Adding ESG variables improves the information set and raises confidence and prudence of ex-ante estimates.

## Key Concepts
- **ESG risk**: uncertainty about the ESG quality of a portfolio, distinct from its average ESG level.
- **Shannon entropy**: `H = -sum p_k ln p_k`; measures disorder of a distribution.
- **RESG**: entropy-based ESG risk metric using weights and ESG scores.
- **Component VaR**: decomposition of VaR into additive contributions by factor or position.
- **UVaR**: undiversified VaR (sum of stand-alone VaRs, ignores correlation).
- **Spearman rank correlation**: ordinal association between two variables.
- **Relative VaR**: VaR of the active position versus the benchmark.
- **MRR**: joint relative-risk indicator combining financial and ESG relative risk.
- **Selection effect / allocation effect**: ESG-relative risk from picking issuers vs from category allocation.
- **Investable Universe**: set of high-ESG-score issuers used as reference.
- **ESG factor**: ESG-based explanatory variable in a risk model.

## Formulas & Reference Tables
- Entropy of weights over ESG-score classes: `H = - sum_k p_k * ln(p_k)`, `p_k` = total portfolio weight in class k; maximum `ln(K)` for K classes (uniform). **Note**: the source cites the Shannon formulation but states a conservative corrective that is not given in the text; the formula above is the base form, not the exact RESG.
- ESG share of risk: `ESG Component VaR / total VaR = 5.5%` (equity fund, factor model).
- Weighted average ESG score (for contrast): `sum_i w_i * ESG_i` - descriptive, not predictive.

## Mental Models
- Use "average ESG score = quality; entropy = uncertainty" to explain why two numbers are needed.
- Use RESG next to VaR: if financial risk rises but RESG does not (or vice versa) you have a mismatch worth investigating.
- Use sector and country decomposition, not single-stock, to read ESG risk.
- Use MRR to test whether tracking-error budget is spent on ESG selection or allocation.
- Use the tri-leg indicator as a dashboard with tactical and strategic limits.

## Worked Example
**Base entropy over four ESG classes (recomputed, without the source's corrective).**
- Portfolio A weights across classes (best to worst): 70% / 20% / 10% / 0% -> `H = 0.802`, 58% of the maximum `ln 4 = 1.386`.
- Portfolio B: 40% / 30% / 20% / 10% -> `H = 1.280`, 92% of the maximum.
- Uniform: `H = 1.386`, 100%.
- Interpretation: A is concentrated in the top ESG class so its ESG outcome is more predictable (lower disorder); B is spread out and so more uncertain. A real RESG would additionally penalize weight in low classes (the corrective), so B's gap versus A would be larger than this base calculation shows.

## Anti-patterns
- Using the weighted average ESG score as if it were a risk measure.
- Assuming ESG-risk relations hold stock by stock.
- Reading the correlation between RESG and VaR as causation.
- Applying the approach to small-cap-heavy funds without validation.
- Treating ESG risk as noise to be dropped from financial models.

## Practitioner Notes
- The method is the author's own and is validated on a limited time window (about three years of monthly data); treat as promising, not standard.
- Relevant for compliance: an ESG risk dashboard gives a documented, ex-ante control that complements ratings.
- Keep absolute (VaR) and relative (benchmark) controls; add ESG risk as a third view.
- Further detail is in CFA Society Italy professional papers (cited in the source).

## Key Takeaways
1. No standard statistical ESG risk metric exists; ESG scores alone are not forecasts.
2. ESG factors explain a non-trivial part of ex-ante risk (about 5.5% of VaR in the test).
3. An entropy-based metric (RESG) uses weights and scores and scales with financial risk.
4. RESG ranks track undiversified VaR closely at sector and country level (Spearman mostly above 0.90).
5. MRR separates ESG selection and allocation effects in relative risk (ESG about 6% on average).
6. A tri-leg indicator (VaR, relative VaR, RESG) supports holistic limits.
7. Adding ESG variables raises the information content and prudence of risk estimates.

## Connects To
- **ch20**: ESG integration as an investment strategy.
- **ch23**: ratings and benchmarks feeding the scores.
- **ch24**: ESG performance measurement and KPI quality.
- **ch27**: climate risk metrics (WACI, carbon footprint) as complementary risk views.
- **ch30**: engagement as a risk-reduction tool.
- **`cfa-quantitative-methods`**: entropy and rank-correlation background.
