# Chapter 4: Introduction to Asset-Backed Securities
> **Source**: CFA Program Curriculum 2020, Level I, Reading 45 · Fixed Income | Frank J. Fabozzi, PhD, CPA, CFA

## Core Idea
Securitization moves loans and receivables off an originator's balance sheet into a **bankruptcy-remote special purpose entity (SPE)**, which issues securities paid only from the pool's cash flows. Structuring does not create or destroy risk. It **redistributes** it: **credit tranching** (subordination) reallocates default losses, and **time tranching** (sequential-pay, PAC/support) reallocates **prepayment risk**, split into contraction risk and extension risk. To analyze any ABS, you ask three questions: what backs it, who absorbs losses first, and who absorbs prepayment variability.

## Learning Outcomes Covered
- Explain the benefits of securitization for economies and financial markets.
- Describe the securitization process, the parties involved and their roles.
- Describe typical structures, including credit tranching and time tranching.
- Describe the residential mortgage designs that are typically securitized.
- Describe RMBS (pass-throughs, CMOs), with their cash flows and risks.
- Define prepayment risk and describe it for MBS.
- Describe CMBS characteristics and risks.
- Describe non-mortgage ABS (auto loans, credit cards), with their cash flows and risks.
- Describe CDOs, with their cash flows and risks.

## Frameworks Introduced
- **Benefits of securitization**
  - **Disintermediation**: investors get a direct legal claim on loan pools, without the bank's other business risks attached.
  - **Tailored exposure**: investors choose their level of credit and interest-rate risk through tranches.
  - **More lending capacity for banks**: banks recycle their balance sheet and earn origination fees.
  - **Liquidity**: tradable securities are more liquid than whole loans, which lowers systemic liquidity risk.
  - **Cheaper funding for the originator**: some tranches are rated above the originator's own rating.
  - **Residual risks that remain**:
    - Timing risks: contraction and extension.
    - The inherent credit risk of the collateral.
    - Both were central to the 2007–2009 crisis.

- **Parties to a securitization (the Mediquip → MET template)**
  | Party | Role |
  |---|---|
  | Seller / **depositor** / originator | Originates the loans and sells them to the SPE in a **true sale** |
  | **SPE / SPV** (issuer, trust) | Buys the collateral and issues the ABS. **Bankruptcy remote** from the seller |
  | **Servicer** | Collects payments, chases delinquencies, repossesses and disposes of collateral. Often the originator, but it need not be |
  | Trustee | Safeguards the assets, holds funds due to holders, issues **remittance reports** |
  | Lawyers | Draft the **purchase agreement** (representations and warranties on collateral quality) and the prospectus (waterfall, fees, credit enhancements) |
  | Underwriters, rating agencies | Same roles as in a plain bond offering. Each tranche gets its own rating |
  | Financial guarantors (monoline insurers) | External credit enhancement. Rarely used since monolines were downgraded in 2007–2008 |
  - Every party other than the seller (including the servicer, when it is a separate firm) is a **third party** to the securitization.

- **Why the SPE lowers funding cost (the key legal mechanism)**
  1. A **secured corporate bond** is priced mainly off the issuer's rating and only slightly off its collateral. The **absolute priority rule** holds in liquidation but courts have not always upheld it in **reorganization**, so the collateral claim is uncertain.
  2. In a securitization, the assets legally belong to the SPE. The originator's bankruptcy leaves the SPE untouched, and courts have no discretion to rewrite the waterfall.
  3. Investors therefore price the **collateral pool**, not the originator. Senior tranches can be rated investment grade even when the seller is BB.
  - Failure modes:
    - A transfer can be challenged as a **fraudulent conveyance** and unwound.
    - Where trust law is weak, true-sale treatment may not hold. Always check the jurisdiction.

- **Credit tranching (senior/subordinated structure, "waterfall")**
  - Losses hit the most junior class first, then move up. Worked on the text's A 180 / B 14 / C 6 structure (US$m):
    - Losses ≤ 6: C only.
    - Losses of 6–20: C is wiped out and B absorbs the next 14.
    - Class A loses only if total losses exceed **20**, its **attachment point**.
  - Purpose: investors pick the level of credit risk they want to bear.
  - A coupon step-up down the capital stack (e.g., 4.00% Class A → 4.80% Class B) signals credit tranching.

- **Time tranching**: create classes with different **expected maturities** so that prepayment risk (extension vs. contraction) is redistributed. Deals commonly combine credit tranching and time tranching.

- **Internal vs. external credit enhancement**
  | Internal | External |
  |---|---|
  | Subordination (credit tranching), overcollateralization, reserve accounts (cash reserve, **excess spread account**) | Financial guarantees (banks, monoline insurers), letters of credit, cash collateral accounts |
  - **Loss order**: excess spread → overcollateralization / reserve account → the most junior tranche upward.
  - The required level of enhancement is set by the rating agency, working back from the rating the issuer wants.

- **Mortgage design checklist (5 dimensions)**
  1. **Maturity**: US 15–30y; Europe 20–40y (France and Spain up to 50y); Japan up to 100y.
  2. **Rate determination**:
     - **Fixed rate**: US, France.
     - **Adjustable (ARM)**, of two kinds:
       - **Index-referenced**: Spain, South Korea, and the US/Canada minority.
       - **Reviewable** (the lender sets the rate): standard in the UK, Ireland and Australia.
       - ARMs carry periodic and lifetime caps.
     - **Initial-period fixed**:
       - **Rollover/renegotiable** (resets to a new fixed rate): Canada, Denmark, Germany, NL, Switzerland.
       - **Hybrid** (fixed, then floating): the UK.
     - **Convertible** (the borrower can switch between fixed and floating): about half of Japan.
  3. **Amortization**:
     - Fully amortizing.
     - Partially amortizing, with a **balloon** at the end.
     - **Interest-only** for an initial period.
     - **Interest-only lifetime / bullet**: the balloon equals the original loan amount.
  4. **Prepayment option** and **prepayment penalties**, where the penalty is effectively **yield maintenance**. Penalties are common in Europe and rare in the US.
  5. **Lender's rights in foreclosure**:
     - **Recourse**: the lender can claim the shortfall from the borrower's other assets. Most of Europe.
     - **Non-recourse**: the property is the only source of recovery. Many US states.
     - Non-recourse raises the incentive for a **strategic default** on an underwater mortgage.

- **US RMBS sectors**
  | Sector | Issuer / guarantor | Credit protection |
  |---|---|---|
  | Agency, federal agency | **Ginnie Mae** (part of HUD) | **Full faith and credit** of the US government |
  | Agency, GSE | **Fannie Mae, Freddie Mac** (in conservatorship since Sept 2008) | The GSE's own guarantee, for a fee. Not a US government guarantee. Collateral must be **conforming** (limits on loan size, documentation, max LTV, insurance) |
  | Non-agency (private label) | Thrifts, commercial banks, private conduits | **Credit enhancement** only (subordination, OC, reserves). Collateral is often **non-conforming** |

- **Sequential-pay CMO rule**: coupon interest is paid to every tranche on its outstanding balance. **All principal** (scheduled plus prepayments) goes to Tranche A until it is retired, then to B, and so on.
  - Short tranches get **extension protection**, supplied by the long tranches.
  - Long tranches get **contraction protection**, supplied by the short tranches.
  - Each tranche is protected on **one side only**.

- **PAC / support structure**
  - The **PAC tranche** follows a principal schedule that holds for any constant prepayment speed inside the **initial PAC collar (band)**, e.g., 100–250 PSA. The protection is **two-sided**:
    - When prepayments are **slow**, support tranches get no principal until the PAC schedule is met.
    - When prepayments are **fast**, the excess over the PAC schedule goes to the support tranches.
  - Outside the band, the support tranche still absorbs prepayment variability first. Once it is paid off, the PAC schedule is **"busted"** and all principal goes to the PAC.
  - The quality of protection depends on the amount of **support tranche outstanding**.
  - Support (companion) tranches carry the **highest prepayment risk**. Correctly priced, they have a higher expected return.

- **CMBS call protection**
  - **Structural**: sequential pay **by rating**. AAA is retired before AA, and so on. Losses still run from the bottom up.
  - **Loan-level**, four mechanisms:
    1. **Prepayment lockout**: no prepayment allowed for a period.
    2. **Prepayment penalty points**: 1 point = 1% of the outstanding balance.
    3. **Yield maintenance (make-whole) charge**: makes the lender indifferent to the timing of prepayment.
    4. **Defeasance**: the borrower funds a portfolio of government securities that replicates the loan's remaining cash flows.

- **CDO economics (arbitrage CDO)**
  - An SPE issues senior, mezzanine and equity tranches.
  - A **collateral manager** actively buys and sells the collateral.
  - Equity earns the spread between the collateral yield and the funding cost, net of fees and swap payments. It is a **leveraged** position.
  - **Coverage and quality tests**: a failure diverts principal to pay down the senior class, which **deleverages** the CDO by shrinking its cheapest funding source.
  - Viability hinges on offering a **competitive return to the equity (subordinated) tranche**.

## Key Concepts
- **Collateral / securitized assets**: the pool of loans or receivables whose cash flows service the ABS.
- **Bankruptcy remote**: the originator's bankruptcy cannot touch the SPE's assets. Holders face only the credit risk of the underlying borrowers.
- **Loan-to-value ratio (LTV)**: mortgage amount / property value. Lower LTV means more borrower equity, lower default probability and higher recovery.
- **Prime vs. subprime**: prime borrowers have strong credit, income and equity. Subprime means weaker credit **or** a loan that is not a first lien.
- **Prepayment**: any principal paid above the scheduled amortization.
- **Contraction risk**: when rates fall, prepayments speed up. The investor must reinvest at lower rates and price upside is capped (**negative convexity**).
- **Extension risk**: when rates rise, prepayments slow. The security lengthens just as its price falls.
- **Pass-through rate (net coupon)**: WAC minus servicing and guarantee fees.
- **WAC / WAM**: coupon and remaining maturity of the pool, each weighted by outstanding balance.
- **Weighted average life (average life)**: the convention-based average time to receipt of projected principal (scheduled plus prepaid). It is the MBS substitute for "maturity". **Legal maturity** tells you little.
- **PSA prepayment benchmark**: CPR rises by 0.2% a month from month 1 to **6% at month 30**, then stays flat. x PSA scales the whole path by x/100.
- **Shifting interest mechanism**: in non-agency RMBS, if the senior tranches' enhancement deteriorates, junior classes are locked out of prepayments for a period so that subordination is preserved.
- **First-loss piece / residual / equity tranche**: the unrated bottom tranche. In a CMBS it absorbs losses first and has no stated coupon.
- **Balloon risk**: at maturity the borrower cannot refinance or sell to meet the balloon. The lender extends through a **workout period** at a **default interest rate**. Balloon risk is a form of **extension risk**.
- **DSC ratio (DSCR)**: property NOI / annual debt service. Above 1.0 means the property's cash flow covers debt service.
- **Lockout (revolving) period**: in non-amortizing ABS (credit cards), principal repaid is reinvested in new receivables. Holders receive only finance charges and fees.
- **Early (rapid) amortization provision**: triggered by pre-specified adverse events. It is the only way to alter the principal cash flows of a credit card ABS.
- **CDO family**:
  - **CBO**: corporate and EM bonds.
  - **CLO**: leveraged bank loans.
  - **Structured finance CDO**: ABS, RMBS, CMBS and other CDOs.
  - **Synthetic CDO**: a portfolio of CDS.

## Formulas & Reference Tables
- **Single monthly mortality rate**: `SMM = Prepayment_t / (Beginning balance_t − Scheduled principal_t)`
- **Conditional prepayment rate** (annualized SMM): `CPR = 1 − (1 − SMM)¹²` ⇔ `SMM = 1 − (1 − CPR)^(1/12)`
  - A CPR of 6% means about 6% of the balance outstanding at the start of the year is prepaid by year-end.
- **PSA benchmark** (t = months since origination): `CPR_100PSA(t) = 6% × min(t, 30)/30`, and `CPR_xPSA = (x/100) × CPR_100PSA`.
  - Example: 80 PSA rises 0.16% a month and peaks at **4.8%**. 165 PSA peaks at **9.9%**.
- **Pass-through monthly cash flow** (level-payment, fixed-rate pool):
  - `Payment = B₀ × i / (1 − (1 + i)^−n)`, with i = WAC/12 and n = WAM in months.
  - `Gross interest = B × WAC/12`
  - `Net interest = B × pass-through rate/12`
  - `Scheduled principal = Payment − Gross interest`
  - `Prepayment = SMM × (B − Scheduled principal)`
  - `Cash flow to investors = Net interest + Scheduled principal + Prepayment`
  - `B_next = B − Scheduled principal − Prepayment`
- **WAC** `= Σ wᵢ × couponᵢ`, **WAM** `= Σ wᵢ × monthsᵢ`, with `wᵢ = balanceᵢ / Σ balance`.
- **LTV** `= Loan / Property value`. **DSCR** `= NOI / Debt service`, where NOI = rental income − cash operating expenses − replacement reserve.
- **Tranche loss**: `Loss_tranche = min(Par_tranche, max(0, Total loss − Subordination below it))`

**Average life vs. PSA: collateral and the sequential CMO-01** (US$800m, 5.5% pass-through, WAC 6%, WAM 357; A 389 / B 72 / C 193 / D 146)
| PSA | Collateral | A | B | C | D |
|---|---|---|---|---|---|
| 100 | 11.2 | 4.7 | 10.4 | 15.1 | 24.0 |
| 165 | 8.6 | 3.4 | 7.3 | 10.9 | 19.8 |
| 250 | 6.4 | 2.7 | 5.3 | 7.9 | 15.2 |
| 600 | 3.2 | 1.6 | 2.8 | 3.8 | 7.0 |

**PAC vs. support, CMO-02** (PAC 487.6 / support 312.4; collar 100–250 PSA)
| PSA | 50 | 75 | 100 | 165 | 250 | 400 | 600 |
|---|---|---|---|---|---|---|---|
| PAC avg life | 10.2 | 8.6 | 7.7 | 7.7 | 7.7 | 5.5 | 4.0 |
| Support avg life | 24.9 | 22.7 | 20.0 | 10.7 | 3.3 | 1.9 | 1.4 |

**Tranche selection by risk concern**
| Investor worry | Buy | Avoid |
|---|---|---|
| Extension risk (rates up) | Short sequential (A/B), early PAC (P-A) | Long sequential, support |
| Contraction risk (rates down) | Long sequential (C/D), **last PAC (P-D)** | Short sequential, support |
| Both, wants predictability | PAC | Support |
| Wants to be paid for prepayment risk | Support | — |
| Expects rates to fall | **Inverse floater** tranche | Floater |

**Amortizing vs. non-amortizing ABS**
| | Auto loan ABS | Credit card ABS |
|---|---|---|
| Collateral | Amortizing | Non-amortizing (revolving) |
| Prepayment risk | Yes: sales, trade-ins, repossessions, insurance payoffs, early payoff | **No** during the lockout period |
| Principal to holders | Monthly | Only after the lockout, or on **early amortization** |
| Typical enhancement | Senior/sub + OC + reserve (excess spread account) | Senior/sub (e.g., Aaa/A2/Baa2) |

## Mental Models
- **Conservation of risk**: tranching is a zero-sum reallocation. Every unit of protection a PAC or senior tranche enjoys is exported to a support or junior tranche. Always ask "who is the shock absorber, and how much of it is left?"
- **Think of an MBS as a bond short a call**: the homeowner holds a refinancing option. Rates down means the call is exercised (contraction, capped upside). Rates up means the call is left unexercised (extension, full downside). That is negative convexity.
- **Price the pool, not the originator**: once the true sale holds, the originator's rating is irrelevant to ABS holders. What matters are the collateral quality (LTV, DSCR, FICO, seasoning), the servicer's quality and the enhancement levels.
- **CMBS ≈ corporate bond, RMBS ≈ callable amortizer**: loan-level call protection makes CMBS trade like bullets. Their dominant risks are **credit** (non-recourse, property by property) and **balloon/extension** risk, not refinancing contraction.
- **CDO equity = a levered carry trade**: the return is the collateral yield minus the funding cost, multiplied by the leverage. It is highly sensitive to defaults and to test-triggered deleveraging.

## Worked Example
**1. First-month cash flow of the US$800m pass-through** (WAC 6%, pass-through 5.5%, WAM 357, 165 PSA, pool seasoned 3 months, so month 1 = seasoning month 4)
- CPR at month 4 of seasoning = 1.65 × (0.2% × 4) = **1.32%**. SMM = 1 − (1 − 0.0132)^(1/12) = **0.1107%**.
- Payment = 800m × 0.005/(1 − 1.005^−357) = **4,810,844**.
- Gross interest = 800m × 0.5% = 4,000,000, so scheduled principal = **810,844**.
- Net interest = 800m × 5.5%/12 = **3,666,667**. The fee strip of 333,333 goes to the servicer and guarantor.
- Prepayment = 0.1107% × (800,000,000 − 810,844) = **884,472**. Total principal = **1,695,316**.
- Cash flow to investors = **5,361,982**. Next balance = **798,304,684**. This matches the source exhibit.
- From month 27 onward (seasoning month 30), CPR = 9.9% and SMM = 0.865%.

**2. Arbitrage CDO equity return** (US$100m: senior 80 at Libor + 70bp, mezzanine 10 at UST + 200bp, equity 10; collateral at UST + 400bp; 10y UST = 7%; the manager pays UST + 100bp fixed and receives Libor on 80m)
- Inflows: collateral 11% × 100m = 11.0m, plus swap receipts of Libor × 80m.
- Outflows:
  - Senior: 80m × (Libor + 0.70%).
  - Mezzanine: 9% × 10m = 0.9m.
  - Swap fixed leg: 8% × 80m = 6.4m.
- Libor cancels out. Net = 11.0 − 0.9 − 6.4 − 0.56 = **3.14m**. After a manager fee of 0.64m, equity gets **2.5m**, a **25%** return on 10m par.
- Interpretation: the swap removes the fixed/floating mismatch. Equity is exposed only to the credit spread earned and to defaults. With no defaults and no calls this is a best case: each 1m of collateral lost to default (zero recovery) wipes out 10% of the equity's principal and cuts annual income by 0.11m, i.e., 1.1 points of equity return.

**3. Loss allocation with OC and reserve** (AmeriCredit 2013-4)
- OC = 49.87m and reserve = 19.00m, so losses up to **68.87m** hit no note.
- A further 40m loss beyond the enhancement goes to Class E (22.33m, wiped out) and then to Class D (**17.67m**). Losses are applied sequentially, not pro rata.

## Anti-patterns
- **Treating securitization as risk reduction**: it redistributes credit and timing risk. The pool's total risk is unchanged.
- **Quoting an MBS's legal maturity**: use average life (under a stated PSA) or effective duration. A 30-year MBS and a 30-year bullet at the same coupon have very different rate risk.
- **Reading "X PSA" as "X% of balances prepaid"**: it means X% of the benchmark's monthly CPR path.
- **Buying a PAC and ignoring the support balance**: fast prepayments can burn through the support tranche, after which the PAC behaves like a plain sequential tranche.
- **Assuming a GSE guarantee equals the US government's**: only Ginnie Mae carries full faith and credit.
- **Relying on a secured corporate bond's collateral as if it were a true sale**: reorganization courts can override priority. Only the SPE structure decouples the two credits.
- **Applying prepayment models to credit card ABS during the revolving period**: principal is reinvested, so there is no prepayment risk until the lockout ends or early amortization is triggered.

## Exam Focus & Traps
- **Depositor = seller of the collateral. Issuer = the SPE/trust.** The servicer, not the SPE, collects payments and repossesses collateral.
- **Collateral = the loans/receivables** (e.g., the promissory notes), not the physical assets (cars, equipment) and not the ABS notes.
- **Attachment point**: the senior tranche loses only when losses exceed the **sum of all tranches below it**, plus OC and reserve if these are present. Example: with A 200 / B 20 / C 5, A is hit only above €25m (answer: €26m).
- **CMO collateral is a pass-through (or a pool of pass-throughs), not the mortgages themselves.**
- **Longest sequential tranche**: lowest contraction risk, but the longest average life and the highest extension risk.
- **Most contraction-protected PAC** is the **last** PAC (P-D). Excess principal is absorbed in order: support, then P-A, P-B, P-C and finally P-D.
- **Pass-through rate < WAC** always, by the servicing and guarantee fees.
- **SMM falls when extension risk rises** (fewer prepayments). The SMM is not constant at 100 PSA during the first 30 months.
- **Credit card ABS in lockout**: holders receive **only finance charges and fees**. There is no prepayment risk.
- **First line of defence in auto ABS**: the **excess spread account**.
- **Failed CDO test**: senior class paid down, i.e., **deleveraged** through the cheapest funding source (not the most expensive).
- **Extra risk of a CDO vs. an ABS**: **manager risk**, meaning the manager fails to earn enough to pay senior and mezzanine holders. Default risk and fixed/floating mismatch are common to both.
- **Non-recourse loan**: the lender's claim is limited to the property (foreclosure proceeds). Strategic default is more likely.
- **Bullet mortgage**: the balloon equals the **original** amount. A partially amortizing loan's balloon equals the **unpaid** balance.
- **⚠ Correction**: the note under the source's Exhibit 2 says the month-1 CPR is "0.132%" and that the pool "seasons at 6% in month 27". At 165 PSA the month-1 CPR is **1.32%** (SMM 0.111%) and the peak CPR reached at month 27 is **9.9%** (SMM 0.865%). 6% is the 100 PSA peak.

## Key Takeaways
1. The SPE's bankruptcy remoteness and true sale let ABS be rated on the collateral, which is why securitization can fund below the originator's corporate cost.
2. Credit tranching allocates default losses bottom-up. Time tranching allocates prepayment variability. Real deals use both.
3. Prepayment risk = contraction (rates ↓) + extension (rates ↑). Measure it with SMM/CPR against the PSA benchmark and summarize it with average life.
4. Sequential tranches give one-sided protection. PACs give two-sided protection inside the collar, paid for by support tranches.
5. Agency (Ginnie = government; Fannie/Freddie = GSE) vs. non-agency (credit enhancement, shifting interest) is the credit dividing line in US RMBS.
6. CMBS: credit risk runs property by property (DSCR ↑, LTV ↓ = safer). Heavy call protection. The key timing risk is balloon (extension) risk.
7. Auto ABS amortize and prepay. Credit card ABS revolve (lockout) and only amortize early on a trigger.
8. A CDO is a managed, levered spread trade. Equity viability and manager skill are what make it work.

## Connects To
- **ch01**: bond indentures and credit enhancements (subordination, OC, excess spread, guarantees).
- **ch03**: amortizing bond cash flows and yield measures used to value pass-throughs.
- **ch05**: effective duration and negative convexity of MBS. Why modified duration fails for prepayable securities.
- **ch06**: credit analysis, recovery and seniority. The absolute priority rule in reorganizations.
- **ch09**: valuation of bonds with embedded options (OAS, effective duration), the tools used for MBS and callable structures.
- **ch11**: credit default swaps, the building block of synthetic CDOs.
- **`tuckman-fixed-income` ch20**: mortgages and MBS in depth (prepayment modeling, OAS, IO/PO, negative convexity).
- **`tuckman-fixed-income` ch19**: corporate credit and CDS, for tranche credit risk.
- **`cfa-level1-curriculum` ch17**: condensed revision notes on the same reading.
