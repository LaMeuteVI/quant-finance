# Chapter 11: Systematic Investing as a Behavioural De-biasing Tool
> **Source**: CFA Society Italy × Advisor Private, *Systematic Investments* guide (2019), Ch. 3 "Gli investimenti sistematici: strumento di de-biasing comportamentale?" | Camilla Mazzoli

## Core Idea
Behavioural finance shows investors process information with shortcuts, emotions and social pressure, producing recurring errors at two critical moments: **opening** a position and **closing** it. **De-biasing** means reducing those errors. Education and advice help but are not sufficient for self-directed investors. **Systematic (rule-based, automated) investing** helps because the rule is set ex ante, away from the emotional moment, and execution does not need an explicit act of will. It mainly cures **emotional** bias; **cognitive and social** bias survive because humans write the rules.

## Frameworks Introduced
- **Three families of conditioning**: internal-cognitive (how reasoning works), internal-emotional (feelings), external-social (the judgment of the group we belong to). Use to diagnose which bias a rule can and cannot fix.
- **Bias map by decision phase**
  | Phase | Bias | Mechanism | Does a systematic rule help? |
  |---|---|---|---|
  | Open | Confirmation bias | Seek only evidence that supports a position already wanted | Partly: rules set before the idea is formed fix the inputs |
  | Open | Prior-loss aversion | A past realised loss in a name leads to subjective, non-objective probability of a new loss, so the investor skips or under-sizes it even in a different environment | Yes: rule ignores the personal history |
  | Open | Availability cascade / ease of recall | Ideas repeated in conversations, media, symbols seem more plausible | Partly: rules ignore media volume |
  | Open | Conformity effect / herding | Follow average judgment of others; analysts' forecasts and peers' views form "group think" | Partly: the crowd can still be encoded (see crowding, ch10) |
  | Close | Anchoring | Initial hypothesis is not revised enough when facts change | Yes if exit criteria are coded ex ante |
  | Close | Cognitive dissonance | Mental conflict when evidence says the belief was wrong; avoid new information or build twisted arguments | Yes |
  | Close | Regret aversion | Fear of the regret of realising a loss or of selling a winner that continues up | Yes if the order is automatic |
  | Close | Disposition effect | Hold losers too long, sell winners too soon | Yes |
- **Stop loss and profit target**: price levels fixed in advance at which a loss is cut or a gain is banked. They help against regret aversion because they pre-commit the exit, but a manual stop still needs the investor to press the button, which is a loophole. The systematic version (orders pre-set and executed automatically when the market hits the level) removes the human act and brings the decision into an ex ante, emotionally cold context.
- **Four de-biasing instruments** (Consob-type literature cited): financial education (most effective against errors from poor financial literacy and rule-of-thumb simplification), advice (guides through information overload but advisers are human too and are irrelevant for self-directed investing), self-awareness (often overridden by emotion), and **automation/systematisation**.
- **Sponsor insert (GAM, "Irrazionalità prevedibile")** adds: an algorithm is never tired, ill, or forgetting a report; does not feel loss aversion; weights all data equally unless the researcher chooses recency; can hold a crowded position only by deliberate logic, not herd instinct; codified models treat "price did not do what was expected" as information and exit, countering overconfidence; can even trade on the predictable reactions of biased investors. Human edge = one or few deeply researched ideas; systematic edge = hundreds of good ideas at once; hence complement.

## Key Concepts
- **De-biasing**: any method that reduces the effect of behavioural errors on decisions.
- **Behavioural finance**: study of how cognitive limits, emotions and social ties shape financial choice, departing from full rationality.
- **Loss aversion**: weight of losses exceeds equal gains (Kahneman-Tversky prospect theory, 1979).
- **Disposition effect**: sell winners early, keep losers.
- **Anchoring**: insufficient adjustment from an initial hypothesis.
- **Cognitive dissonance**: discomfort when evidence contradicts a belief, resolved by avoiding evidence.
- **Regret aversion**: ex ante anticipation of the ex post emotion of regret; drives both late loss-cutting and early profit-taking.
- **Confirmation bias**: selective evidence gathering.
- **Availability cascade / ease of recall**: salience driven by repeated discussion or vivid past events.
- **Conformity effect**: adopting the behavior or judgment of the majority without verification.
- **Recency bias**, **overconfidence**, **herding** (sponsor insert): classic biases an algorithm does not share by construction.
- **Performance gap**: recurring difference between simulated and real performance, attributed by the author partly to behaviour.

## Formulas & Reference Tables
No formulas in the chapter. Reference grid: the bias map above (phase x bias x help from rules). Stop-loss rule in code form: `exit if P_t <= P_entry x (1 - s)`; profit target `exit if P_t >= P_entry x (1 + g)`, with `s`, `g` set ex ante.

## Mental Models
- Use **"decide when cold, execute when hot"**: write exit and sizing rules before entry.
- Use **"rule hygiene"** when you automate: the algorithm removes the emotional bias of execution, but the choice of data, sample period, and parameters inherits the designer's bias.
- Use **phase mapping** to choose the tool: entry biases need selection rules; exit biases need pre-committed orders.
- Use **education + automation** together for self-directed investors; neither alone is enough.

## Worked Example
Disposition effect, illustrative numbers. Two holdings: A is +20% and B is -20% from cost. A discretionary investor sells A to "lock in the gain" and keeps B hoping to break even. Under a systematic rule with stop 10% and trailing exit on winners at 10% below peak: B was already sold at -10% (loss avoided: a further -10 points on that position). A runs on while its peak minus 10% is not touched, so a +20% gain can continue. Portfolio effect on equal weights: discretionary outcome `(+20 + -20)/2 = 0%`; rule-based at stop `(+20 retained, -10 realised)/2 = +5%` before any further gain in A. Interpretation: the rule's value comes from cutting losers, not from predicting direction. Caveat: stop losses can whipsaw in range-bound markets; the effect depends on re-entry rules (see ch10).

## Anti-patterns
- Believing "automated" means "unbiased": rule design is human.
- Setting a stop mentally (not as a working order): it relies on the very willpower the stop is meant to replace.
- Using hindsight-selected parameters (back-test bias is a cognitive bias in the researcher).
- Using systematic rules to avoid ever reviewing the thesis when the regime changes.
- Treating "75% psychology" (a sponsor claim) as measured fact.

## Practitioner Notes
- For self-directed or advised clients, the practical offer is a pre-agreed rule set (rebalancing bands, stop and target levels, entry criteria) executed by platform orders.
- Residual risk: the author says the full behavioural problem remains open and is probably solved only by combining several de-biasing tools.
- Sponsor statements (GAM) on algorithms are advocacy; the independent content is the bias taxonomy.

## Key Takeaways
1. Errors come from cognitive, emotional and social conditioning, at entry and exit.
2. Education and advice are useful but insufficient for autonomous investing.
3. Systematic rules fix emotional errors best because they are set before emotional involvement and executed automatically.
4. Exit-phase biases (anchoring, dissonance, regret, disposition) are the main targets; stop loss and profit target are the tools.
5. Cognitive and social biases remain because humans build the rules.
6. Use several de-biasing tools in combination.

## Connects To
- **ch09**: the "black box" and discretionary vs systematic debate.
- **ch10**: stop-loss evidence (Klement) and crowding as the social bias of quant.
- **ch12**: the factor model whose rules this chapter wants to be free of bias.
- **`cfa-portfolio-management`**: behavioural finance reading (loss aversion, mental accounting).
