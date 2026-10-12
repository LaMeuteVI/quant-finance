# Chapter 12: Overview of Equity Securities (Equity)

## Core Idea
Equity is a residual claim. Common shares carry the operating upside, votes and last place in liquidation. Preference shares sit between debt and common equity. Beyond public common stock, investors reach equity through private equity, direct foreign listings and depository receipts, each with its own risk, liquidity and return profile.

## Frameworks Introduced
- **Debt vs equity**:
  - Debt: a contractual liability (principal + interest).
  - Equity: a residual claim with no contractual payments. Equity investors seek total return (capital gains + dividends).
- **Common shares**: share in operating performance, have voting rights and hold a residual claim in liquidation. There can be several classes of shares.
  - **Statutory voting**: 1 share = 1 vote per director seat.
  - **Cumulative voting**: votes = shares × seats, which can be concentrated on one candidate. This helps minority shareholders.
  - **Proxy voting**: another party votes on the shareholder's behalf.
  - Other features: callable and putable common shares.
- **Preference (preferred) shares**: rank above common shares for dividends and liquidation. Their dividends are fixed but not contractual. They usually carry no votes.
  - **Cumulative**: unpaid dividends accrue and must be paid before any common dividend. **Non-cumulative**: no accrual.
  - **Participating**: fixed dividend + extra dividend if profits exceed a threshold, and possibly an extra liquidation share. **Non-participating**: fixed dividend + par only.
  - **Convertible** into common shares at a set ratio: higher dividend + upside. Popular in VC/PE because it limits downside.
- **Private vs public equity**:
  - Private equity: no active market, illiquid, lower disclosure, longer horizon, and potentially better governance through owner control.
  - Types: **venture capital** (seed and early stage), **LBO/MBO** (debt-financed takeover, then restructure and re-IPO), **PIPE** (private investment in public equity, for quick capital).
- **Non-domestic equity**:
  - **Direct investing**: in local currency and under local rules.
  - **Depository receipts (DRs)**: a bank holds the foreign shares and issues receipts at a ratio. **Sponsored** (the issuer is involved; holders get votes) vs **unsponsored** (no votes).
  - **GDR**: issued outside both the home country and the US. **ADR/ADS**: USD, traded in the US. Level I is OTC; Levels II and III are exchange-listed; Level III and Rule 144A allow capital raising.
  - **Global registered share (GRS)**: the identical share traded in several currencies.
  - **BLDR**: an ETF holding a basket of DRs.
- **Equity return**: `R = (P₁ − P₀ + D₁)/P₀`. Foreign holdings add **currency return**: (1 + R_local)(1 + R_FX) − 1.
- **Risk**: uncertainty of future cash flows. Preferred < common, because dividends and liquidation claims are fixed and paid first. Putable shares are less risky; callable shares riskier.
- **Equity and company value**: capital is raised to fund growth (capex, R&D, M&A), meet regulatory capital or covenants, and provide an acquisition currency and incentives.
- **ROE** = NI available to common / average book value of equity.
  - ROE is an *accounting* return. The **cost of equity** is the *investor's* minimum required return.
  - Value is created when ROE > cost of equity.
  - Market value ≠ book value. P/B reflects expected future ROE relative to the cost of equity.

## Key Concepts
- **Book value of equity** = assets − liabilities. **Market value** = price × shares.
- **Cost of equity** = the required return, estimated with CAPM or DDM.
- **Dual listing**: shares traded in more than one market.

## Mental Models
- **Seniority ladder**: debt > preferred > common, in both cash flows and liquidation.
- **ROE vs cost of equity is the value-creation test.** Leverage can raise ROE without creating value.
- **DRs give access, not immunity**: FX and home-country risk remain.

## Anti-patterns
- **Reading a high ROE as success without decomposing it** (leverage vs margins vs turnover).
- **Treating preferred dividends as guaranteed**: they can be skipped. Cumulative prefs only defer them.
- **Ignoring currency** in foreign equity returns.

## Worked Example
**Return on a foreign share.** A US investor buys a DR on a UK share at £10 (1 DR = 1 share). A year later the price is £10.50 and a £0.30 dividend has been paid. GBP/USD moves from 1.25 to 1.20.
- Local return = (10.50 − 10 + 0.30)/10 = **8%**.
- FX return = 1.20/1.25 − 1 = **−4%**.
- USD return = 1.08 × 0.96 − 1 = **+3.68%**.

## Key Takeaways
1. Common: votes, upside, residual claim. Preferred: fixed dividend and priority, usually no votes.
2. Cumulative, participating and convertible features change the risk and return of preferreds.
3. Private equity (VC, LBO, PIPE) is illiquid and longer-horizon. DRs, GDRs, ADRs and GRSs give foreign access.
4. Equity return = capital gain + dividend (+ FX for foreign holdings).
5. Value is created when ROE exceeds the cost of equity.

## Connects To
- **Ch 8**: markets and orders.
- **Ch 13**: valuation (DDM, preferred valuation, multiples).
- **Ch 7**: FX returns.
