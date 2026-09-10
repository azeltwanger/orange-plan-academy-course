# W01 — Build the first working plan

Status: CONVERSATIONAL_CAPTURE_REVIEW — revised demonstration narration; actual app/device capture remains pending.
Kind: capture
Gate: APP_CAPTURE
Sources: FOUNDATION, DICTATION, APP

### Production basis — not spoken

Use PR #227 accepted direction at reference head `21fedfbb1290bfdd637f3b0879bf7e7d6bfdbbc2`; the [latest directive](https://github.com/azeltwanger/orange-plan/pull/227#issuecomment-5618008737) governs future behavior. This is a capture manuscript, not proof that the planned screens or writers ship. The unchanged Reed fixture and a separately reviewed synthetic extension supply all household facts. Use separate takes after the paired lessons. Only Narration blocks are spoken; overlays are added in editing. All amounts inside an app recording must come from its actual inputs and result. Common rules: [stepwise script standard](../../production/STEPWISE-SCRIPT-STANDARD.md).

#### Chapter 1 — Find the first task · after 0.1

**Show:** Open the intended Home → Your Plan entry, then Plan → Build & improve. Point to the next incomplete source record. Show the four destinations only as orientation. Use a separate three-line card for the existing mortgage, expected college support and possible renovation.

**Narration:**

We're going to start building the plan from the information you have today. Here on Home, I'll open the plan and use Build & improve to get to the next piece we need.

Before we add anything, notice the difference between these three examples. The Reeds' mortgage already exists, so it's a debt. College support is a future commitment with dates attached. The renovation is still an idea, so we'll compare it separately.

Let's begin with the first account that needs attention, with the latest statement beside it. We'll work through that record before moving on, so we can see where each number comes from.

**Overlay:** Current fact · Expected change · Possible choice

**Verify:** The next task opens its actual owner, not a duplicate form. Starting Plan is clearly preliminary and has no success percentage. Return to the same task after viewing its record.

**Capture dependency:** PR #227 foundation contract: Home/Plan/Build & improve and Starting Plan states on the approved implementation head. Confirm actual task ownership and empty-state behavior; no invented probability or minimum-input requirement.

#### Chapter 2 — Review accounts and holdings · after 1.2

**Show:** Use Home → Your Money to open the category-filtered Accounts view and one account detail. Review the existing checking account ($18,000), Alex Roth ($145,000) and direct-Bitcoin location (3.4 BTC) in separate takes. Use the approved contextual add/update entry only where a record is missing.

**Narration:**

Here we're looking at one account from the money category on Home. Before getting into what it owns, I'm matching its name, owner and account type to the statement. If it's already entered, this is the record we're reviewing. Adding another would count the same money twice.

Alex's Roth IRA tells us the account type, but we still need the investments inside it. For cash, we're checking the balance. For the Bitcoin location, we're checking the quantity and where the coins are held, using a plain name without recovery information.

After a correction is saved, I'll reopen the account beside the same statement. That lets us see whether the record now describes what the household actually owns.

**Overlay:** One account · Correct owner/type · Holdings explain the balance

**Verify:** One record per account. Quantity, total, owner/type and source date survive the saved readback. Direct Bitcoin and fund exposure retain different identities.

**Capture dependency:** Foundation account-detail and maintenance writer paths, scoped ownership and truthful update dates. Fixture amounts require frozen-price treatment; actual holdings, HSA/education composition and any missing owners require a separately reviewed capture extension. Do not choose example tickers to fill gaps.

#### Chapter 3 — Read what the connection supplies · after 1.2

**Show:** Open account detail → How this account updates in an authorized synthetic connected-source case. Read the actual capability receipt for balance, holdings, activity and purchase details, including an incomplete case and its supported next step.

**Narration:**

This account is connected, but let's look at what that connection actually supplies. The balance tells us the total. Holdings explain what's inside it. Activity and purchase details answer different questions about how it got there.

If the total arrived without the investments, the statement can help us fill in that composition. Missing purchase history can stay with the tax question it needs to answer. We're also looking at when the financial information was last confirmed; opening the page today doesn't make an older balance current.

That tells us what's ready to use and which part still needs our input. Next we'll look at an account where we know the total but need to explain the investments.

**Overlay:** Balance · Holdings · Activity · Purchase details

**Verify:** The receipt describes the actual supplied products and timestamps. Missing positions are not shown as cash, zero holdings or fully synced; one supported next action is identified.

**Capture dependency:** D34/D62 capability receipts and financial-fact freshness. Capture requires certified synthetic evidence and the approved receipt/recovery UI. No live credentials, provider connection, paid refresh or staged provider response.

#### Chapter 4 — Explain a balance-only investment account · after 1.2

**Show:** At the same $145,000 Roth account, use Holdings needed → Add investments. Enter verified positions or use the accepted mutually exclusive Estimated mix path. Where identities are unresolved, show the source $116,000 spot-fund exposure/$29,000 stocks only as the estimated categories they support.

**Narration:**

We know this Roth account is worth $145,000. What we're doing here is explaining that balance, so the plan knows how the money is invested.

When the statement supplies actual investment names and quantities, those are what we use. If all we have is an approximate mix, it stays labeled as an estimate. The Reeds' teaching example has $116,000 of spot Bitcoin-fund exposure and $29,000 of stocks inside the same $145,000 account. Those amounts explain the total; they don't increase it.

Any cash needs to come from the statement too. We won't make an unexplained remainder into cash just to finish the record. After saving, let's reopen the account and make sure the composition explains the same total once. Any remaining difference stays visible until we can explain it.

**Overlay:** Fictional categories: $116,000 + $29,000 = one $145,000 account

**Verify:** Exact positions or Estimated mix is the saved composition, never both added together. Unknown basis/date remains unknown; no fake purchase, cash remainder or extra balance appears.

**Capture dependency:** D65 complete balance-only workflow, multi-position entry, classification, estimated/exact mutual exclusion, discrepancy state, atomic save and reload. Keep this chapter pending if the approved implementation cannot perform the full path.

#### Chapter 5 — Attach history to what you already own · when relevant records are available after 1.2

**Show:** In one account detail, use Upload account activity or the supported purchase-details route for a reviewed fictional buy/transfer chain. Show an overlap already present and its deduplication treatment. Record a transfer to self-custody through the accepted transfer flow, not a sale/repurchase substitute.

**Narration:**

This part is useful when you have purchase or transfer records for holdings already in your plan. If those records don't apply, or you don't have them yet, note what's missing and continue to chapter six for the monthly picture. You don't need to repair an unrelated old purchase before you do that.

Here, the purchase explains Bitcoin already included in today's holdings. It isn't a new purchase today. As we follow it from the exchange to the wallet, the transfer keeps the original history attached. If the same purchase is already here, accepting it again would give us a duplicate.

I'll compare the household quantity before and after the history is attached. It only changes if we've identified a real position that was missing. Otherwise, we've learned more about the same Bitcoin. Unsupported purchase details stay unknown, and we can move on to the monthly starting picture.

**Overlay:** Existing holding + supporting history = the same Bitcoin counted once

**Verify:** No duplicate quantity, transaction or lot; transfer retains history and basis without a taxable-sale substitution. Deliberate overlap is recognized; unresolved discrepancy remains visible.

**Capture dependency:** Certified upload adapter, scoped mapping, transfer ledger, history/position reconciliation and deduplication receipt. A safe synthetic fixture needs dates, fees and provenance supplied before capture. Missing history does not block unrelated cash-flow work.

#### Chapter 6 — Enter the starting monthly picture · after 1.2

**Show:** Open Cash Flow → Income, Taxes and withholding, Everyday spending, Debt payments and Saving and investing as needed. Enter original source state only. Present the exact Reed cash bridge as a separate teaching graphic, never a fabricated app result.

**Narration:**

Now we're connecting the accounts to the money moving through the household each month. The first thing I'm checking is what each income amount includes. Alex's gross pay is before deductions. Morgan's example income is after ordinary business costs, but the equipment payment is counted separately. Those meanings need to match the fields.

In our teaching calculation, gross income is about $19,417 a month. After the $4,000 tax allowance, $10,800 living costs and about $3,342 required debt, there's $1,275. Alex's $775 contribution leaves $500 for other priorities. The employer's $387.50 goes into retirement saving; it isn't bill money.

Let's follow the app's actual result from its income and tax inputs. If it differs from the illustration, we need to understand those inputs before assigning another transfer. That's the monthly picture we'll use when we record the retirement question next.

**Overlay:** Fictional bridge: $1,275 before employee − $775 = $500; employer $387.50 separate

**Verify:** Original spending remains $10,800. Required payments and payroll deductions are counted once. The source provision is distinguished from calculated tax and any genuine discrepancy is explained.

**Capture dependency:** D32/D48 income and withholding semantics, payroll election, business-loan inclusion, debt source and employer-match route. Exact inputs: $19,416.67 − $4,000 provision − $10,800 − $3,341.67 = $1,275. No balancing override to force the app to $500; approved tax jurisdiction and payroll details are required.

#### Chapter 7 — Record each person’s retirement question · after 1.2

**Show:** Use Plan → Build & improve to reach the accepted retirement timing and spending owners. Enter Alex’s intended age 52, Morgan’s separately supported timeline and the reviewed fictional spending/benefit/horizon extension. Show each date and dollar basis before saving.

**Narration:**

With the starting facts in place, we can enter the work-change question you wrote down at the beginning. Alex wants work to become optional at 52. That records his intention; the calculation will test whether it can be funded. Morgan's income stays on its own timeline.

For retirement spending, we'll begin with current costs, remove the ones that really end and add healthcare or other costs that begin. The dollar units shown here matter, so we don't apply inflation twice. Any Social Security or pension estimate belongs to the right person and start date.

Once this is saved, we have a question to test. A missing benefit estimate stays visible until there's a source for it. Next we'll read the assumptions the plan uses to look beyond today's facts.

**Overlay:** Work date · Spending basis · Each person’s income · Horizon

**Verify:** Saved timing affects the correct person once. Spending units, horizon and sourced benefits survive readback; no missing benefit is replaced with invented income.

**Capture dependency:** Approved timing/spending owners and date conventions. Source fixture supplies age-52 intent, not birth dates or a final benefit quote. Do not automatically adopt the separate $96,000/$12,000/$40,000 retirement illustration as the baseline.

#### Chapter 8 — Read assumptions and test one change · after 1.4

**Show:** Open Plan → Overview → Assumptions to identify the approved build's actual new-plan standard preset and read its saved path, inflation, income growth and horizon. Retain it unless a reasoned change is being demonstrated. Use Plan → Scenarios for one less-favorable growth comparison with all household choices unchanged. Inspect early/later path years, then return to Current without adopting it.

**Narration:**

These are the assumptions behind the plan we just built. We'll start with the app's standard preset for a new plan and read what it means. You can keep it while you learn; changing it needs a reason beyond making the result look better.

I'm looking at the return path in an early year and a later year, then inflation and the planning horizon. A declining growth path can be quite different from one fixed annual rate. Now we'll make a separate weaker-growth comparison with retirement timing, spending and contributions unchanged.

Let's follow the first year where the funding differs and see which income or account has to do more. That tells us which household decision becomes harder under this assumption. Then we'll return to the current plan. Testing a weaker path doesn't choose it as the new starting assumption, and we can read the main result with that distinction clear.

**Overlay:** One changed assumption · Same household choices

**Verify:** Current and comparison identities remain explicit; only the selected assumption changes. Results are current for that comparison; returning leaves saved Current unchanged.

**Capture dependency:** Approved Assumptions and Scenarios owners, actual new-plan preset identity, custom-path availability, holding classification and result-receipt identity. Confirm the standard preset exists and show its real name/values; do not infer a default risk level. No preset percentages or calculated outcome is supplied by the script; show the actual approved build.

#### Chapter 9 — Read the first complete result · after 1.5

**Show:** Read Plan → Overview’s full-Plan receipt: chosen timing/spending/horizon, displayed percentage and exact successful count. Open the first year after the work change and its funding detail. If the plan is still preliminary, demonstrate the specific missing input instead of presenting full results.

**Narration:**

Here we're ready to read the first complete result. I'll start with the work date, spending and horizon, because the percentage describes that question. The successful-path count tells us how many modeled futures funded it under these rules; it doesn't promise what happens to this family.

Let's open the first year after work changes and follow the income, costs and taxes, then what investments have to supply. If that withdrawal is surprising, the event or obligation behind it is what we need to understand.

From there, we can choose a fact to correct or a realistic change to compare. If the starting plan fits, keeping it is a valid result too, with its important limitation still visible. In the next take, we'll use Ask to help trace one of these numbers back to its source.

**Overlay:** Question tested → successful paths → funding year → next action

**Verify:** Percentage/count use the same full-Plan receipt, inputs and horizon. No chosen age is passed off as a calculated result. The year detail supports the explanation and no illustration is inserted into the interface.

**Capture dependency:** D16/D50 preliminary-to-full states, exact standard, successful count, missing-input gating and automatic result currentness. The generic 790/1,000 teaching example must remain outside the app. No invented Refresh/Recalculate shell control.

#### Chapter 10 — Trace an Ask explanation · after 1.5

**Show:** Open Ask with the populated plan and ask a specific question about a visible result. Follow the actual response back to its source rows. Add a separately captured current market-report or outside-AI-summary demonstration only after availability and content verification.

**Narration:**

Let's use Ask for a question we can check against the plan. I'm asking it to walk from income to the monthly amount remaining and explain what's already been deducted. That gives us something concrete to compare with the cash-flow rows.

The date, income, taxes and existing contribution all need to match. If they don't, we keep that question open and find the difference before changing the plan. We can use the same approach for a retirement withdrawal or a missing tax input.

If you use an outside AI review, read the actual summary before sharing it. A restore backup has a different purpose, and removing a name doesn't remove every private detail. What we're taking forward is the fact or choice we need to work on. Next we'll go into Cash Flow and check how the monthly amount matches your records.

**Overlay:** Ask for the source · Match the date and inputs · Choose the action yourself

**Verify:** Actual response is traceable and no saved input changes implicitly. Export is identified correctly and inspected; no wallet secrets, credentials or assumed anonymization.

**Capture dependency:** Approved Ask route/context/permissions and source links. Market report requires real date and sources; external AI feature requires actual availability and reviewed export schema/privacy. No staged AI answer, connected account action or outside message is authorized by this manuscript.

### Member checkpoint

Accounts and holdings reconcile to the available records without duplicate assets or invented history. Income, deductions, living costs, required debt and existing saving explain the starting monthly amount. Each person's work timing and the spending question are saved, the starting assumptions are identified, and one weaker comparison has been reviewed. You can trace the first complete result to its inputs and name the next improvement. If a missing source prevents that result, record the exact source and next action instead of treating the preliminary plan as complete.

### Source and continuity notes — not spoken

The paired teaching scripts retain their deck/source IDs and dated research boundaries. Original dictation, accepted Reserve reference and prior manuscripts remain preserved; this stepwise rewrite follows Austin’s September 10 authorization. It changes no household fixture, financial model, provider state, learner account or real-world financial instruction. Build-dependent proof, final voice review and any qualified review remain separate.
