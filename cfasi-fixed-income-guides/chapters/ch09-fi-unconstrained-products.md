# Chapter 9: The Phenomenon of "Unconstrained" Fixed Income Products
> **Source**: CFA Society Italy × Advisor Private, "Fixed Income" guide (May–June 2018), Chapter 9 (Il fenomeno dei prodotti "unconstrained") | Davide Montaldo (fund selector, Banca del Piemonte)

## Core Idea
Benchmarked bond funds hold what indebted issuers issue, and after a 35-year decline in yields they offer high duration risk for little yield premium. Unconstrained ("go anywhere") fixed income funds drop the benchmark constraint to pursue return and volatility targets with rates, credit, FX and derivatives. The catch: classification is non-standard, risk is hard to read from holdings, many such funds quietly load on credit (high yield, emerging markets, financials) and correlate with equities, so selection and monitoring must be mostly qualitative. This chapter is the selector's playbook; chapters 12-17 of this skill (the dedicated Unconstrained guide) go deeper.

## Frameworks Introduced
- **Fund vs bond difference**: a bond matures (YTM and duration converge to zero, so duration matters only for mark-to-market); a fund never matures, so YTM and duration are rolling statistics. A benchmarked fund sits on the curve segment defined by its benchmark; an unconstrained fund's duration is manager-controlled.
  | | Single plain bond | Traditional (benchmarked) fund | Unconstrained fund |
  |---|---|---|---|
  | YTM | Converges to par; effect only in mark-to-market | Moves with yields and spreads and benchmark composition | Dynamic, set by manager positioning |
  | Duration | Falls to zero at maturity | Range around the benchmark's curve segment | Variable, strategy-driven |
  | Maturity | Defined | None | None |
- **Why a fund beats a bond for a retail investor**: diversification of issuer risk (a 50-bond fund at 2% each loses at most 2% from one default), cushioning of spread widening, regulatory change (bail-in makes subordination matter; new issues have minimum tickets of EUR 100,000 or more).
- **Benchmark-debt link**: indices weight issuers by amount outstanding, so heavily indebted issuers dominate. Global Aggregate by country (28 Feb 2018): US 37.4%, Japan 17.6%, France 6.1%, UK 5.6%, Germany 5.3%, Italy 4.0%; the index is mostly government debt. Debt/GDP: Japan about 224%, Greece 180%, Italy 131% (Dec 2017 estimates).
- **Historical argument for traditional products**: (1) falling rates or spreads lift all bonds, constant rates still pay carry; (2) strong flows (flight to quality or carry hunting); (3) secular fall in yields. Post-2012 the capital-gain leg faded: returns came from coupons, while duration rose (lower yields allowed issuers to extend maturities), hence "high duration risk, thin premium".
- **Unconstrained mandate types**
  - **Absolute return**: target vs a money-market rate with a volatility cap (illustrative: beat 3-month Euribor by 3% rolling over 2 years with volatility under 5%).
  - **Total return**: broad mandate, outperform a market index over horizons longer than 12 months.
  - **Downside protection overlay**: some fund houses add drawdown hedges.
  - Some managers state no objective; peer-group assignment is then judgmental.
- **UCITS origins**: UCITS III (2001/107/EC and 2001/108/EC) allowed derivatives for investment, shorts, leverage (synthetic). Post-2007/08, hedge fund managers launched "Newcits" (since 2009), bringing CDS, swaps, basis trades, relative value and capital arbitrage into retail wrappers. Flexible bond fund assets distributed in Europe rose from about EUR 90bn (early 2013) to EUR 280bn (end 2017), about 200% (Morningstar).
- **Classification issue**: most providers have no "unconstrained" category; they sit in Flexible Bond (EUR, GBP, USD, Global, hedged variants). The same fund can fall in different categories across providers. Build your own peer groups by guidelines or realized volatility.
- **Positioning grid** (market segment × region × strategy): government (local or hard currency), IG, HY, ABS/MBS, structured, convertibles, FX, equity, cash; global/Europe/US/EM. Three levers often used: FX strategies, limited equity, cash as an asset class (debated; some selectors require fully invested managers).
- **Traditional vs alternative implementation**: relative value, roll-down, yield-curve strategies in physical bonds are "traditional"; the same strategies via derivatives and leverage are "alternative"; structured or hedge-fund-style underlyings make a product a Liquid Alternative.
- **Investment process**: macro-first (scenario, FX, rates view) then asset allocation across debt segments, then selection and strategy (classic or hedge-like); or bottom-up stock picking.
- **Duration styles** (illustrative managers A-D): A hedges duration with short Treasury/Bund futures; B refuses shorting as inefficient and risky; C (credit) keeps duration because credit comes with duration and prefers duration times spread (spread duration); D modulates duration by momentum, using floaters, ABS/MBS (positive exposure to rising rates).
- **Reading duration in an unconstrained fund**: the single number aggregates multiple curves and segments. Ask: duration by country and sector, which positions are hedged, with which futures (10-year US, UK, EUR) and the basis risk of that hedge (curve segment, different base curves), what happens if negative (inverse sensitivity: 100 bp up gives +x%), on which rates the manager is positioned to profit from a rise, and why.
- **Selection and monitoring**
  - Quantitative (starting point only): Sharpe ratio, volatility, drawdown, correlation to other managers and markets (HY, EM, equity), return dispersion within the peer group, regression on markets to detect hidden credit/rate beta.
  - Qualitative (dominant): direct dialogue; stress periods (Taper Tantrum May 2013, 2011 sovereign crisis, summer 2015 sell-off, early 2016); internal limits (sector, geography, currency), return/volatility targets, permitted instruments, leverage definition, cash limits, risk controls, liquidity crisis handling, risk-neutral stance; style drift check.
  - Hybrid metrics: AUM and sustainability (closure risk), fee structure (entry, management, performance, exit, swing pricing), base currency and investor target (a US-designed product repackaged for Europe may hold more MBS/Treasuries), hedging of NAV vs underlying, investor type concentration, capacity limits and manager commitment to them.
  - Risk-exposure view: show the portfolio as % of NAV risk buckets (US rates, ex-US rates, US MBS, CMBS, agency ABS, non-agency, HY, IG, EM bonds, volatility, downside protection) rather than only asset class.
- **Due diligence summary table** (per manager): category, objectives and characteristics, performance in difficult windows, max drawdown, recovery period, notes. Use two correlation matrices on different windows (short and one year).

## Key Concepts
- **OICR / UCITS** — collective investment undertakings; EU regulation for retail funds.
- **Newcits** — hedge-fund-style strategies in UCITS wrappers.
- **Liquid Alternatives** — hedged/derivatives strategies in liquid format; overlaps with unconstrained, but alternative-only managers are a separate family.
- **Go-anywhere** — fund house label for no benchmark constraint.
- **Absolute return vs total return** — cash-plus target with volatility cap vs index-beating with a longer horizon.
- **Spread duration** — sensitivity to credit spread changes.
- **Style drift** — manager departing from the stated approach.
- **Peer group** — homogeneous set of comparable funds; subjective by construction.
- **Swing pricing** — NAV adjustment charging flows' transaction costs.
- **Capacity** — maximum AUM before performance suffers.
- **Taper Tantrum** — May 2013 bond sell-off on Fed tapering news.

## Formulas & Reference Tables
- `Max loss from one default in an equally weighted n-bond fund = 1/n of NAV` (50 bonds, 2% each).
- Duration reading: `ΔNAV% ≈ −Duration × Δy`; duration −2 means a 100 bp rise gains about 2%.
- Illustrative correlation matrices of four unconstrained managers (3-month window): pairwise from 0.35 to 0.63; (1-year window): 0.17 to 0.43. Treat as examples: correlations are unstable and rise in stress.
- Window returns in the guide's case study (26 Jan-9 Feb 2018): Funds A-D −0.73%, −0.67%, −0.93%, −0.76%; Euro Aggregate −0.45%, Global HY −2.21%, Global Aggregate +0.40%, Global Equity −7.63%. Over one year all four were positive.

## Mental Models
- Use "fund is not a bond": never quote a fund's YTM like a bond's.
- Use unconstrained funds as a satellite for diversification or when benchmark duration is unattractive; check correlation to HY, EM and equity first.
- Use risk-bucket exposure charts rather than holdings lists to compare managers.
- Use stress-window analysis (2013, 2015, early 2016, Feb 2018) to learn what the "flexibility" actually does.
- Use manager conversations to test duration hedges: basis risk and conviction matter more than the headline number.
- Combine multi-manager selection with correlation matrices on multiple windows, but expect correlations to rise in a crisis.

## Worked Example
Dispersion check from the guide's case: four unconstrained funds with differing mandates (multi-strategy long/short, credit stock picking, top-down macro, plain vanilla credit) all fell 0.67% to 0.93% in a risk-off fortnight when global aggregate rose 0.40%.
1. Excess loss vs Global Aggregate: A `−0.73 − 0.40 = −1.13` pts; B −1.07; C −1.33; D −1.16.
2. Compare with Global HY (−2.21) and equity (−7.63): the funds lost roughly a third to two fifths of HY's loss (0.67/2.21 = 30% to 0.93/2.21 = 42%), signalling credit beta.
3. One-year returns were all positive but different; correlations 0.17-0.43 over one year.
Interpretation: the funds diversified versus equities but not versus credit; they did not behave like safe-haven bonds. Ask each manager why.

## Anti-patterns
- Choosing from the product name or the provider's category.
- Rating managers by Sharpe ratio alone, without the stress windows.
- Treating a "negative duration" figure as true rate protection without checking hedge instruments.
- Holding several unconstrained funds that all load on HY and EM.
- Letting the client believe an unconstrained fund is safe because it is not a benchmarked bond product.
- Ignoring fund base currency and investor-target design.

## Practitioner Notes
- The guide recommends a dedicated selector/monitor and periodic calls, newsletters and one-to-one meetings with managers and risk managers.
- It advises writing a concise due diligence document summarizing the rationale for an investment committee, to be updated after each interview.
- Fee structure and swinging price details are part of the product decision, not an afterthought.

## Key Takeaways
1. Funds and bonds are different: no maturity, rolling YTM and duration.
2. Bond indices overweight the most indebted issuers; after 2012 returns are mostly carry with high duration risk.
3. Unconstrained funds target absolute or total return and use rates, credit, FX and derivatives.
4. No standard classification: build peer groups yourself and keep them fluid.
5. Many unconstrained managers drifted into credit, raising correlation with equity.
6. Duration of an unconstrained fund is a composite that can mislead; decompose it.
7. Selection is mostly qualitative; monitoring is permanent and covers drift, capacity, fees, investor base.
8. Use correlation matrices on several windows to assemble multi-manager portfolios.

## Connects To
- **ch07**: absolute return and active mandate types.
- **ch08**: duration, key rate duration, tracking error for benchmarked funds.
- **ch11**: EM bonds often used by unconstrained managers.
- **ch12-ch17** (`cfasi-fixed-income-guides`): the dedicated Unconstrained Fixed Income guide with fuller treatment.
- **`cfa-alternative-investments`**: hedge fund strategies behind Liquid Alternatives.
