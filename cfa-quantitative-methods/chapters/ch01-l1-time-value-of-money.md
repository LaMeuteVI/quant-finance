# Chapter 1: The Time Value of Money
> **Source**: CFA Program Curriculum 2020, Level I, Reading 6 · Quantitative Methods | DeFusco, McLeavey, Pinto, Runkle

## Core Idea
Money received earlier is worth more than the same amount received later, so cash flows can only be compared or added once they are indexed at the same date on a time line. Every valuation in finance (bonds, stocks, mortgages, pensions) reduces to moving single sums and annuities along that time line with the interest rate as the exchange rate between dates.

## Learning Outcomes Covered
- interpret an interest rate as a required rate of return, a discount rate or an opportunity cost
- decompose an interest rate into the real risk-free rate plus inflation, default, liquidity and maturity premiums
- calculate and interpret the effective annual rate (EAR) from the stated annual rate and compounding frequency
- solve TVM problems under any compounding frequency (including continuous)
- compute FV and PV of a single sum, ordinary annuity, annuity due, perpetuity (PV only) and uneven cash flows
- use a time line to model and solve TVM problems

## Frameworks Introduced
- **Interest rate = required return = discount rate = opportunity cost**: three readings of the same r.
  - When to use: to decide how to frame r in a given problem (hurdle for investors, rate for discounting, forgone return of consuming now).
  - How: given a payment of 10,000 in one year equivalent to 9,500 today, r = 500/9,500 = 5.26%.
- **Build-up of a market interest rate**: `r = real risk-free rate + inflation premium + default risk premium + liquidity premium + maturity premium`.
  - When to use: to explain yield differences between two instruments, or to bound the rate of a new instrument.
  - How: real rate + inflation premium = nominal risk-free rate (T-bill proxy). Compare two instruments that differ in only one attribute; the rate gap isolates that premium. Same maturity, different liquidity: gap = liquidity premium. Same maturity and liquidity, different credit: gap = default premium. Same everything but longer maturity: gap = maturity premium.
  - Failure mode: the additive form is an approximation; exactly, `(1 + nominal) = (1 + real)(1 + inflation)`.
- **Time line method (the 4-step TVM routine)**:
  1. Draw the time line, index today as t = 0.
  2. Place every cash flow at its date; identify the structure (lump sum, ordinary annuity, annuity due, perpetuity, uneven).
  3. Check that r and N use the same time unit (periodic rate with number of periods).
  4. Move each block to a single common date, add (cash flow additivity), then move to the target date.
  - Why it works: PV and FV are equivalent measures separated in time. A lump sum equals an annuity (an amortization table proves it), and an annuity equals its FV.
- **Cash flow additivity principle**: amounts indexed at the same date are additive.
  - When to use: uneven streams. Split into a level annuity plus lump sums, or annuity minus annuity.
  - How: e.g. flows 4 then 24 = a 2-year annuity of 4 plus a lump sum of 20 at t = 2.
- **Annuity as a difference of two perpetuities**: a 4-payment annuity = perpetuity starting t = 1 minus perpetuity starting t = 5.
- **Delayed annuity / perpetuity rule**: an annuity or perpetuity whose first payment is at t = k has its formula value at t = k − 1 (one period before the first payment). Then discount that value back to t = 0 as a lump sum.
- **Solving for the unknown**: rearrange the same equations for r (or growth rate g), N, or the annuity payment A.

## Key Concepts
- **Required rate of return**: the minimum return an investor must receive to accept an investment.
- **Discount rate**: the rate used to translate a future amount into present value; synonymous with r in most uses.
- **Opportunity cost**: the value forgone by choosing one action over another (e.g. the return lost by consuming today).
- **Real risk-free rate**: single-period rate on a riskless security if no inflation were expected; reflects time preference for consumption.
- **Nominal risk-free rate**: real risk-free rate plus the inflation premium; a short T-bill rate is the usual proxy.
- **Default risk premium**: compensation for the chance the borrower misses a promised payment.
- **Liquidity premium**: compensation for the risk of loss versus fair value when selling quickly.
- **Maturity premium**: compensation for the higher price sensitivity to rate changes of longer-dated debt.
- **Stated annual (quoted) interest rate, rₛ**: periodic rate times periods per year; ignores intra-year compounding. Preferred general term over APR (APR carries legal definitions that vary by country).
- **Periodic rate**: `rₛ/m`, the rate actually earned each compounding period.
- **Effective annual rate (EAR)**: the growth of one unit over a year including interest on interest (APY in the US, equivalent annual rate in the UK).
- **Annuity / ordinary annuity / annuity due**: finite level cash flows; first payment at t = 1 for ordinary, at t = 0 for due.
- **Perpetuity**: level, never-ending cash flows with the first at t = 1.
- **Simple vs compound interest**: simple interest = rate × original principal each period; compound interest adds interest on previously earned interest.
- **Compound growth rate (CAGR)**: the single rate that compounds a starting value into the ending value; a geometric mean of the one-period growth factors.
- **Continuous compounding**: the limit as m → ∞; gives the maximum FV for a given stated rate.

## Formulas & Reference Tables
Symbols: PV present value, FV future value, r periodic rate, N number of periods (or years when m is used), rₛ stated annual rate, m compounding periods per year, A level payment.

| Quantity | Formula |
|---|---|
| FV, single sum | `FV_N = PV (1 + r)^N` |
| FV, m periods per year | `FV_N = PV (1 + rₛ/m)^(mN)` |
| FV, continuous | `FV_N = PV · e^(rₛN)` |
| PV, single sum | `PV = FV_N (1 + r)^(−N)` ; with frequency `PV = FV_N (1 + rₛ/m)^(−mN)` |
| EAR, discrete | `EAR = (1 + rₛ/m)^m − 1` |
| EAR, continuous | `EAR = e^(rₛ) − 1` ; inverse `rₛ = ln(1 + EAR)` |
| Periodic rate from EAR | `r_periodic = (1 + EAR)^(1/m) − 1` |
| FV, ordinary annuity | `FV_N = A [((1 + r)^N − 1)/r]` |
| PV, ordinary annuity | `PV = A [(1 − (1 + r)^(−N))/r]` |
| PV, annuity due | `PV_due = PV_ordinary × (1 + r)` (also = A + PV of ordinary annuity of N−1 payments) |
| FV, annuity due | `FV_due = FV_ordinary × (1 + r)` |
| PV, perpetuity | `PV = A/r` (value one period before the first payment; r > 0, level payments only) |
| Growth rate / CAGR | `g = (FV_N/PV)^(1/N) − 1` |
| Number of periods | `N = ln(FV/PV)/ln(1 + r)` |
| Level payment (loan) | `A = PV / [(1 − (1 + r)^(−N))/r]` |
| Fisher relation | `(1 + nominal) = (1 + real)(1 + inflation)` |
| Rule of 72 | years to double ≈ 72 / (stated rate in %) |

Effect of compounding frequency on 1 unit at a stated 8% for 1 year (verified):

| Frequency | Periodic rate | Terminal value | EAR |
|---|---|---|---|
| Annual | 8% | 1.080000 | 8.000% |
| Semiannual | 4% | 1.081600 | 8.160% |
| Quarterly | 2% | 1.082432 | 8.243% |
| Monthly | 0.6667% | 1.083000 | 8.300% |
| Daily (365) | 0.0219% | 1.083278 | 8.328% |
| Continuous | n/a | 1.083287 | 8.329% |

Properties: FV rises with N and with r; PV falls with N and with r; more frequent compounding means higher FV and higher EAR; continuous compounding is the ceiling.

## Mental Models
- **Every cash flow has a date stamp.** Never add or compare two amounts unless they carry the same stamp; move them first.
- **Annuity formulas land one period before the first payment.** Draw the line, find where the formula "lives", then shift with a lump-sum factor. This single rule solves deferred annuities, delayed perpetuities and pension liabilities.
- **A lump sum and an annuity are the same thing in different clothes.** An initial balance that earns r and is drawn down by A per period hits zero exactly at N; this is how every amortized loan works.
- **A rate quote is a convention, not a growth factor.** `1 + rₛ` is not a future value factor when compounding exceeds annual; always convert to a periodic rate or to the EAR.
- **Annuity due = ordinary annuity shifted one period earlier**, so multiply by (1 + r), both for PV and FV.
- **Interest rate and growth rate are the same math.** Solve `(FV/PV)^(1/N) − 1` for sales, earnings or any series; it is the geometric mean of annual growth factors, not the average of growth rates.

## Worked Example
**A. Retirement funding gap (the "missing annuity" problem).** A saver puts 2,000 per year at t = 1..15, wants 100,000 per year for 20 years with the first draw at t = 41, and earns 8%. Find the savings X for t = 16..40.
1. FV of savings at t = 15: `2,000 × 27.152114 = 54,304.23`.
2. Value of the retirement annuity at t = 40 (one period before first payment): `100,000 × 9.818147 = 981,814.74`.
3. Discount that to t = 15 (25 periods): `981,814.74 × 1.08^(−25) = 143,362.53`.
4. Shortfall at t = 15: `143,362.53 − 54,304.23 = 89,058.30`.
5. Annuity over 25 payments with PV 89,058.30: `X = 89,058.30 / 10.674776 = 8,342.87`.
Interpretation: bring all flows to one date (t = 15 here), match inflows with outflows, then solve; the answer is independent of the chosen date.

**B. Lump sum vs annuity due.** Option 1 pays 2,000,000 today; option 2 pays 200,000 per year for 20 years starting today, rate 7%. PV(option 2) = 200,000 + 200,000 × 10.335595 (19-payment ordinary annuity) = 2,267,119.05 > 2,000,000, so option 2 is worth more, ignoring taxes.

**C. EAR and level payment.** 8% stated, quarterly compounding: periodic 2%, EAR = 1.02⁴ − 1 = 8.243%. A 100,000 30-year mortgage at 8% stated, monthly: r = 0.8%/12 = 0.6667%, N = 360, annuity factor 136.2835, payment = 733.76.

## Anti-patterns
- **Mixing time units**: using an annual rate with a monthly N (or vice versa); the periodic rate and number of periods must be compatible.
- **Treating the stated rate as the true yearly return**: ignoring compounding understates what the investor earns (8% semiannual is 8.16%, not 8%). Compare offers on EAR.
- **Applying the annuity formula without shifting**: forgetting that a deferred annuity's PV must be rolled back from the date one period before its first payment.
- **Using A/r for non-level or finite flows**: the perpetuity formula needs constant payments, infinite life and r > 0.
- **Averaging growth rates arithmetically**: use the geometric (compound) rate; the arithmetic mean overstates multi-period growth.
- **Early rounding**: carry 6+ decimals in factors; round only the final answer. On a calculator enter 0.08/12 rather than 0.67.
- **Table lookups**: factor tables are less accurate than calculators or spreadsheets.

## Exam Focus & Traps
- Annuity due versus ordinary: first check where the first payment sits; "payment starts today" means due.
- Perpetuity with first payment k periods out: the value A/r sits at t = k − 1, not t = k (a quarterly preferred share paying first in 5 quarters is valued at A/r discounted 4 periods; with 2.00 per quarter and 6%/4 = 1.5% this is 133.33/1.015⁴ = 125.62).
- Deposit schedules with compounding finer than the cash-flow frequency: use the effective periodic rate for the cash-flow interval, or compound each deposit with rₛ/m over its own number of periods (4% stated, semiannual, deposits 4,000/8,000/7,000/10,000 at ends of years 1-4 gives 30,447 per the curriculum answer pattern).
- EAR of 4.08% from a stated 4.00% implies daily compounding (quarterly gives 4.06%, semiannual 4.04%).
- Continuous vs daily compounding differences are tiny: 1,000,000 for 4 years at 3% differs by about 5.56 (answer ~6) because compounding frequency matters little at low rates.
- Real vs nominal: the nominal risk-free rate = real + expected inflation; the liquidity premium (not maturity) explains the Treasury vs small-issuer gap at equal maturity.
- Sign and timing in the interest-rate bound problem: a lower-maturity but less liquid bond can still yield more than a longer liquid one if the liquidity premium exceeds the maturity premium.
- Rule of 72 gives 10.29 years versus the exact 10.24 at 7%; it is only an approximation.
- Calculator: set P/Y = 1 and END mode (BGN for annuity due), clear memory between problems.

## Key Takeaways
1. Index every cash flow on a time line first; add or compare only at the same date.
2. Convert any quoted rate to the periodic rate or EAR before use; compare offers on EAR.
3. Annuity and perpetuity formulas give values one period before the first payment; shift the result with a lump-sum factor.
4. Annuity due = ordinary annuity × (1 + r) for both PV and FV.
5. Use cash flow additivity to decompose uneven streams into annuities and lump sums, or annuity = perpetuity − delayed perpetuity.
6. Solve unknowns by rearrangement: `g = (FV/PV)^(1/N) − 1`, `N = ln(FV/PV)/ln(1+r)`, `A = PV/annuity factor`.
7. An interest rate decomposes into real rate plus inflation, default, liquidity and maturity premiums; match instruments differing by one attribute to isolate a premium.
8. Continuous compounding sets the ceiling: `EAR = e^rₛ − 1`.

## Connects To
- **ch 02**: the compound growth rate here is the geometric mean covered there.
- **ch 04**: the lognormal distribution links continuously compounded returns to holding period returns.
- **`cfa-level1-curriculum`**: TVM is the engine of bond and equity valuation in later readings.
- **`cfa-fixed-income` ch 03**: bond pricing is PV of an annuity plus a lump sum with the ytm as discount rate.
- **`cfa-corporate-finance` ch 02**: NPV and IRR are PV and rate-solving applications.
