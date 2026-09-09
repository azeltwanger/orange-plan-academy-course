# Temporary literal manuscript; removed after integration.
LESSONS = {
'7.1': '''You can have a retirement plan that works on paper and still lose access to the asset it depends on. Custody is how we make the Bitcoin position usable, recoverable, and manageable for the household.

The question isn't, “Which setup looks most advanced?” It is, “Which responsibilities am I willing to carry, and what happens when one part fails?”

Every method trades one kind of dependence for another.

Direct self-custody gives you control of the keys rather than relying on a company to permit a withdrawal. It also makes you responsible for recovery, physical security, and a process your family can follow.

Professional custody can provide administration and support. You accept the provider's control, terms, withdrawal process, and counterparty risk. Read the actual legal arrangement instead of assuming professional support means every loss is insured or recoverable.

Collaborative multisig can let more than one key participate in authorization, with professional help for part of the process. A two-of-three setup can tolerate certain single-key failures. It also requires the correct configuration, sufficient independent keys, and people who understand the procedure. More keys don't mean no risk.

An intentional split is a way to combine methods. It isn't automatically best. Each additional setup should reduce a named failure the existing arrangement leaves too concentrated, and the household needs to maintain the extra work.

Start by naming the job of each holding. Is this personally controlled long-term Bitcoin? Retirement-account exposure? A position pledged for borrowing? Money that will need a sale for spending? Different jobs may justify different arrangements.

Then state how important direct control is to you. For some people, retaining meaningful Bitcoin that a provider cannot freeze is non-negotiable. Others place more weight on support and family simplicity. We can recognize both without pretending the trade-offs disappear.

Here is a useful comparison. Two households hold the same amount. One has a well-understood direct-custody setup, proven recovery, and another person capable of following the process. The other has one operator and a family that would have no idea where to begin.

The second household doesn't necessarily need a more complicated wallet. Its immediate problem may be dependence on one person. Professional support, a simpler arrangement, or a carefully designed split could address that problem more directly than adding keys nobody else understands.

Now run the one-failure test. What if the provider disappears? The device is lost? The home is inaccessible? The usual operator is unavailable for six months? Which of those events could interrupt or destroy too much of the plan?

Look at shared dependencies. Two devices using the same backup are not independent wallets. Two companies may depend on the same underlying custodian. Several recovery items kept together can fail in the same fire or theft.

You don't have to eliminate every conceivable risk. Find the failure with the greatest consequence and choose a manageable improvement. The safest-looking arrangement on a diagram is not useful if the family cannot operate it.

For Alex and Morgan, we will review the actual direct and professionally held Bitcoin in the example without inventing a completed recovery test. We will also keep Bitcoin-fund exposure in retirement accounts separate; its family access relies on the account process, not the wallet backup for personally held coins.

Finish with a custody direction and the first unfinished protection step. That might be verifying a backup, securing a provider account, making the non-secret family instructions usable, or comparing professional support for a specific portion.

Don't move everything during this discussion. Choose the direction first, prepare and test the destination, and verify the legal and operational process before meaningful money depends on it. The next lesson explains what recovery proof actually means.''',
'7.2': '''Owning a hardware wallet and owning a working backup are not the same thing. The device can work perfectly today while the recovery information is incomplete, mistaken, or unavailable when it is needed.

We want to find that out without putting the funded wallet at risk.

A wallet backup lets compatible software or a device recreate the keys for the corresponding wallet. The hardware device is not where the Bitcoin itself lives. Losing the device can be survivable when the correct recovery materials and procedure are available.

A PIN protects access to the device. It is not a substitute for the wallet backup. A passphrase, when used, changes which wallet the backup opens. That passphrase must also be available and exact. Multisig can require several keys and the wallet configuration. The right test depends on the setup you actually chose.

Start with the current official instructions for the exact device, software, and backup format. Don't combine a few steps from different models or follow an unsolicited support link. Where supported, a non-destructive backup check can compare the recorded backup with the active wallet material without wiping the device.

For learning, use a separate small-value practice wallet or another properly isolated training setup. Keep real recovery words, keys, passphrases and secrets out of recordings, course uploads, screenshots, chat and shared notes.

In the demonstration, the practice wallet gets a small test transaction, follows its official recovery procedure, and is checked against the expected wallet. That lets you understand the sequence before meaningful savings depend on your own execution.

But the result has a limit: recovering the practice wallet proves that practice setup. It does not prove the backup of a different funded wallet.

Your actual wallet needs its own appropriate verification. That may include its official backup-check process and, when suitable and safely arranged, recovery on a compatible spare device while the working device remains intact. A passphrase or multisig arrangement needs the additional steps that prove the intended wallet can be reached, not just that one word list is valid.

Check a known non-secret wallet identifier or receive address using the verified process, not only that an application shows some balance. A mistyped passphrase can open a different valid wallet. Seeing an empty wallet is a reason to stop and investigate, not immediately send money into it.

Before any destructive step, understand what it removes and what recovery evidence already exists. Do not wipe the only working access to meaningful funds as a casual test. A failed check needs careful official support and a safe plan—not repeated guesses under pressure.

Store backups so the failures you're concerned about don't take all copies at once. Durability protects against damage. Separate storage can reduce shared physical loss. Both add responsibilities about privacy and family access. A photographed backup may be easy to find but exposed to devices and accounts you didn't intend to trust.

After a successful test, record only the evidence that is safe to keep in the planning record: which setup was tested, the type of test, date, outcome, and what still needs checking. Don't record the recovery material itself.

For the Reeds, “wallet recorded” and “recovery verified” remain separate statuses. Their fixture tells us what they hold. It doesn't establish that anyone restored a wallet or that Morgan can follow the process.

The working chapter should finish with an honest status. Either the relevant check was completed safely and its scope is clear, or there is a named next step before more money relies on the setup. Watching the demonstration is not recovery proof for your wallet.

That is the practical benefit of this lesson: you know what you would need after device loss and have a safe way to verify it, instead of discovering the missing piece when the device is already gone.''',
'7.3': '''A wallet can be well protected while the email account used for financial access is weak. A strong password can also be undermined by an insecure recovery route. Security works as a chain, so we're going to close the obvious gaps around the setup you chose.

Start with the account that can reset access to the others—often email. Use a unique strong password and the strongest supported multifactor method you can maintain. A password manager can help avoid reusing the same password across unrelated services.

Where available, phishing-resistant security keys or passkeys can add protection against lookalike login pages. A hardware security key helps authenticate the real service. It is not the same device or job as a hardware wallet that holds Bitcoin signing keys.

Set up a recovery route too. Losing your usual phone or security key should not leave the account dependent on an improvised emergency workaround. A registered spare key and safely stored recovery information can help, subject to the provider's actual process. Test that recovery arrangement without removing the only working access first.

Then inspect the provider account itself. Review active sessions and devices, withdrawal restrictions or delays where available, approved addresses, notifications, and the recovery contact details. Use the protections actually offered; don't assume every institution has the same controls.

Those settings reduce some account-takeover risks. They don't remove the provider's own business or custody risk. That was part of the architecture decision, not something a stronger login can solve.

Let's work through a familiar scam pattern. A message says your wallet or account is compromised and urges you to act now. It gives you a link, a phone number, or a recovery page.

The pressure is the first reason to slow down. Don't use the contact details supplied by the warning to verify the warning. Open the known official app or a independently verified site and contact the provider through that route.

A support agent asking for recovery words, a private key, or a transfer to a supposed safe wallet is not helping you secure the existing wallet. Never share those secrets with someone who contacts you. An official device procedure you deliberately initiate is different from a stranger asking to inspect your backup.

The same care applies to an investment opportunity. Guaranteed returns, a new friendship that turns into a private platform recommendation, or a demand to send more money to unlock withdrawals should stop the process. The plan doesn't need a rushed unfamiliar product to remain a plan.

Physical privacy matters as well. Think about who knows what you hold, which devices and recovery materials share a location, and whether family instructions expose more than their reader needs. Don't publish a map that makes access easier for an attacker.

Choose one important account and complete the hardening before moving on. Confirm the new sign-in method works, the backup method works, and notifications go to the right place. Recording “enable security key” on a list isn't the same as registering and testing it.

Then apply the same check to the other accounts the family depends on. You don't need a weekly rebuild of every security setting. You need a known configuration, a review rhythm, and a response when a device, provider, or household role changes.

For this chapter, the demonstration will use an authorized example account and show the outcome without exposing credentials or recovery codes. Provider screens change, so final instructions must match the actual version.

Finish knowing how to sign in securely, how to recover legitimate access, and how to verify a warning without following the attacker's instructions. Next we will turn the whole arrangement into a map another person can understand.''',
'7.4': '''You may understand exactly where your Bitcoin is and still leave your family with no usable starting point. A list of account names isn't enough when nobody knows what those accounts are for or whom to contact.

The Family Custody Map explains the arrangement without becoming a document full of secrets.

For each meaningful holding, record what it is, who owns it, the custody method, its role in the plan, the relevant contact or process, and the status of the supporting work. Use non-secret identifiers that let the family distinguish one arrangement from another.

Don't put recovery words, private keys, passphrases, passwords, PINs, or precise secret-storage locations in this map. The map points to the protected process. It doesn't replace that process or make every reader able to move the funds.

Consider Alex and Morgan's different holdings. Personally controlled Bitcoin needs a recovery and authorization process. Professionally custodied Bitcoin needs the provider's access and family procedures. A Bitcoin fund in a retirement account uses that account's ownership and beneficiary process.

Writing “Bitcoin” on three lines would miss those differences. We want the family to know which kind of help applies to each one.

Now look at the people. Who normally operates the setup? Who can begin the process if that person is unavailable? Has that person agreed, and do they know where the safe instructions begin?

A technical helper and a legally authorized person may be different. Knowing how to restore keys doesn't automatically give someone authority to use another person's assets. The estate section connects those roles; the custody map should not blur them.

Use honest status language. “Backup exists” is different from “backup checked.” “Practice recovery succeeded” is different from “this funded setup has been verified.” “Provider contacted” is different from “family access process confirmed.” Record what actually happened.

Then test the map with one absence scenario. Suppose the usual operator is unavailable for six months. Ask the backup person to explain where they start and which accounts or obligations need timely attention. Don't ask them to reveal secrets or move money for the rehearsal.

If they cannot distinguish the personal wallet from the retirement fund, fix the labels. If they cannot find the professional contact, fix that step. If every answer requires calling the unavailable person, the map has exposed the problem it was meant to find.

Keep the map short enough to use, with the detailed protected instructions maintained separately. Extra pages are not an improvement when they hide the first action.

Also plan for a family member who does not want to keep the same Bitcoin allocation. They need a safe, lawful path to review or liquidate it, not a document that works only if they adopt your conviction. We can protect against rushed mistakes without requiring the heir to become a Bitcoin expert.

Finish by storing a current dated map, telling the relevant people where the safe starting point is, and assigning any unfinished protection task. Then review it when custody, people, or account ownership changes.

The next section makes sure the legal authority and family documents agree with this operational picture. A workable custody setup and a workable inheritance plan need each other.''',
'8.1': '''Your family can know where the assets are and still be unable to act when you're unavailable. The documents and people need to match the ownership and the situation.

We're going to identify those roles before discussing more complicated estate structures.

There are two different questions. Who can help while you are alive but unable to manage things? And who is authorized after you die?

A financial power of attorney can authorize an agent to act under its terms while you are alive. Healthcare decision-making has its own documents and scope. After death, the estate, trust, and beneficiary processes determine the relevant authority. The same person may have more than one role, but the role is not interchangeable just because their name appears on a document.

Start with the people you would want involved. For financial decisions, choose someone reliable, willing, and able to follow the process. They can seek professional help; they don't have to be the household's best investor. For healthcare, choose someone who understands your wishes and can handle the responsibility.

For children, discuss guardianship and how assets would be managed for them with an estate attorney. The person who cares for a child and the person managing money for that child do not necessarily need to be the same person.

Name backups. A plan depending on one helper can fail when that person is also unavailable or no longer willing to act. Ask the people before treating their names as a completed arrangement.

Now review the documents you already have. Is there a current will? Appropriate financial and healthcare authority? Any trust already in use? Are the signed versions findable, and do they reflect current wishes?

An old draft in a folder is not proof a document was properly executed. A nominated executor may need appointment through the applicable process before acting. A trust only governs assets under its actual terms and ownership arrangements. We will not infer authority from a course worksheet.

Beneficiary designations deserve a separate check. Some accounts and policies transfer through their own beneficiary or ownership rules rather than following the will in the way you expect. Compare primary and contingent beneficiaries with the intended estate plan and get discrepancies reviewed.

For Alex and Morgan, having children and several account types makes that coordination important. We are not writing them a trust or selecting a guardian in this example. We are identifying the choices and documents that need to agree.

Take one account and ask: who owns it today, who is intended to receive it, and which record or process carries that intention? If those answers conflict, you have a specific question for the attorney or provider.

Then choose the highest-impact unfinished action. It might be appointing the right backup person, updating a beneficiary, locating an executed document, or arranging legal review. Give it an owner and a date.

You do not need every optional structure to finish this step. You need a coherent set of people, documents, and account instructions appropriate to your household. The next lesson tests whether those people can actually use that authority with the assets they would need to manage.''',
'8.2': '''A person can have legal authority and still not know how to begin with a Bitcoin wallet. Another person can know how the wallet works and have no legal authority to use it.

The family plan has to connect both sides without giving unnecessary access to everyone involved.

Start with one absence scenario. Suppose the normal operator is alive but unable to manage the household for several months. Bills continue, a loan may need monitoring, and someone may need information from a financial institution.

Identify the person authorized under the relevant documents and the provider's process. Then identify the technical support they may need. These could be different people working together.

A trusted contact on an account can be useful when the institution is concerned about exploitation or can't reach the owner. It does not automatically give that contact authority to trade or withdraw money. Verify the actual role before relying on it.

Now take the death scenario. The process changes. A power of attorney is not the continuing authority for administering the deceased person's estate. A beneficiary, trustee, or estate representative may act through different procedures, depending on the asset and jurisdiction.

Don't leave the instruction “use my login.” The provider may require proof of identity, legal status, and specific documents. An authorized person should use the correct process rather than impersonate the owner or improvise around access controls.

Direct Bitcoin introduces a practical requirement in addition to authority. The person responsible needs a lawful route to the required keys and configuration, with appropriate technical help. A will by itself does not recreate a missing backup. A backup by itself does not settle who owns the assets.

Let's use the map from Custody. For a retirement account holding a Bitcoin fund, the family starts with the custodian and the beneficiary process. For personally held Bitcoin, it starts with the designated legal and operational roles and the protected recovery procedure. For a collateral-backed position, loan obligations and lender rights need attention as well.

Those are different workflows. The map should point to the right one, not direct every helper to the same recovery words.

Ask what money is available while a longer process is underway. Immediate household bills should not depend on a complicated recovery being completed that day. Check the legally available cash and payment arrangements in the actual household plan rather than assume every joint or individual account can be used in the same way.

Then rehearse the first steps with no real transfers. Give the helper the safe starting document and ask whom they would contact, what authority that person needs, and which item is urgent. The exercise should reveal a missing contact or document before an emergency does.

When the answer is unclear, fix that connection. Perhaps the provider hasn't confirmed its requirements. Perhaps the attorney and technical helper have never discussed the arrangement. Put that specific coordination task on the list.

A family that expects to sell Bitcoin still needs this process. The goal is an orderly, authorized decision, not convincing a grieving spouse to preserve your exact portfolio. Build instructions that remain useful when the heir's preferences differ.

You finish when the authority, access route, support contact and immediate cash needs connect for the assets that matter. The next lesson puts those first actions into a letter and packet the family can actually use.''',
'8.3': '''A folder full of estate documents can still leave your family asking, “What do I do first?” The Heir Letter and Executor Packet are there to answer that without turning the family into a financial or technical expert overnight.

The letter is the starting point. The packet carries the supporting information. Neither replaces properly prepared legal documents or grants authority on its own.

Start the letter with what the reader should do and what they should avoid rushing. Use ordinary language. They need a calm first step, not an explanation of every investment you've ever made.

A simple example might read like this:

“If I'm unavailable, start with the family contact list and speak with the person authorized for this situation. The attorney listed there can help confirm the legal steps. Our custody map describes the accounts and which provider or technical helper applies to each one. Do not share wallet recovery words or follow links from someone claiming urgent action is required. Check the household payment list so essential bills and time-sensitive obligations receive attention. You do not have to make every long-term investment decision immediately.”

That is example language to adapt with your legal and family process, not a complete legal instruction or an assertion that a particular person already has authority.

Then explain where the supporting records begin. The Executor Packet can include the safe account inventory, ownership and beneficiary information, legal-document locations, professional contacts, regular obligations, and relevant tax-record references. Keep full sensitive records in the appropriate protected place, shared only through the agreed process.

The Family Custody Map remains the guide to Bitcoin arrangements. Don't duplicate recovery secrets into the letter to make it seem complete. A document that helps an heir find the legitimate process should not become a shortcut for anyone who finds the document.

Use the existing templates as a starting structure. Fill them with the household's actual people and instructions. Delete irrelevant sections rather than make a reader sort through hypothetical trusts, providers, or loans the family doesn't use.

Date the documents and identify who maintains them. A contact who moved, an account that closed, or a changed beneficiary can make an old packet misleading even when most of it remains accurate.

Now test delivery, not just wording. Can the intended person find the letter when needed? Do they know it exists? Is the backup contact also prepared? A beautifully written file inside the unavailable person's locked laptop is not a usable handoff.

Any check-in or delayed-notification service is only an additional communication layer. It needs consent, reliable contact details, a false-alarm process and a test of what is actually delivered. It doesn't replace legal authority or safe custody, and it should not automatically distribute secrets.

For a rehearsal, use a harmless test message and an authorized recipient. Do not stage a real death notice or send sensitive instructions to someone without agreement. If the app has not demonstrated that delivery feature, keep it as an outside task rather than pretend the test occurred.

Read the first page with the person who would use it. Ask them to describe the first action back to you. Then ask what they would do if the primary contact didn't answer. Their hesitation tells you where the explanation is missing.

Fix the missing step before adding more pages. The useful outcome is a findable starting point and an understandable path to help.

For this section's working chapter, prepare the letter and packet, connect them to the existing custody map, and complete the no-secrets rehearsal. Record what was understood and which outside legal or provider action is still needed. The family should know where to begin without being handed unrestricted access to everything.''',
'8.4': '''Insurance is meant to keep a large setback from forcing the rest of the financial plan to absorb a cost it cannot comfortably carry. The useful question isn't how many policies you own. It is which loss would leave the household without a workable response.

Start with the risk, then review the protection already in place.

If one income stops because someone dies, what money would the family still need? If a person cannot work because of disability, what income continues and for how long? If someone faces a major liability claim or needs extended care, which assets and cash flows are exposed?

We can compare those gaps without assuming every household needs the same coverage.

For a simple life-insurance illustration, suppose a family expects a $40,000 annual shortfall for ten years after an income loss. Multiplying gives $400,000 before growth, inflation, taxes, changing needs, other costs and resources. It is a way to see the scale of the problem, not a final policy recommendation.

Now add the obligations and subtract the resources genuinely available for that purpose. Existing insurance, survivor benefits, another reliable income or accessible assets may help. Don't count an asset toward both the surviving household's retirement and a different obligation without testing the consequence.

The duration matters too. Support needed while children are dependent has a different shape from a permanent estate-liquidity need. Term and permanent insurance have different coverage periods, costs and features. Compare the actual purpose and contract with a qualified professional rather than choosing a product because of a sales illustration.

Employer coverage is part of the inventory, but check what happens when employment ends or changes. A benefit that disappears at retirement cannot remain in the post-retirement plan by habit.

Disability coverage also needs its actual definition and limits. What counts as disabled under the policy? When do benefits begin? How long can they last, and what income would they replace after any tax? The Reserve may need to support the waiting period or costs the benefit doesn't cover.

For liability protection, review home and auto coverage and whether an umbrella policy fits the exposure. The limits, exclusions and required underlying coverage need to work together. A high net worth doesn't establish the correct limit by itself, and an umbrella doesn't cover every possible claim.

Healthcare and long-term support deserve separate attention. Do not assume ordinary health insurance or Medicare covers every ongoing care need. Compare the actual benefits, the possibility of self-funding, and how a prolonged care cost would affect the other person in the household.

You don't need to solve every coverage question today. Complete the insurance audit with the current policy, owner, insured person, benefit or limit, premium, exclusions to investigate, beneficiary where relevant, and review date.

Then identify the most important gap. “Confirm whether this benefit continues after I leave work” is an actionable question. “Buy more insurance because we have Bitcoin” is not a needs analysis.

When comparing a replacement, keep existing protection until the new arrangement is actually approved and in force, unless a qualified review establishes a deliberate different plan. A quote or application isn't coverage.

For Alex and Morgan, the lesson gives us the process, not invented policy details or insurability. Their actual audit stays open where the source does not supply coverage evidence.

The section is finished when the household understands the risks it is keeping, the ones transferred through actual coverage, and the specific gaps being addressed. Bring premiums and any retained cash needs back into the financial plan. Insurance should protect that plan, not sit in a separate folder nobody checks.'''
}
NOTES = {
'7.1':'Custody deck trade-offs and latest August26 owner-source correction govern over old wealth ladder. Institutional custody is not inferior bydefinition;splitrequiresnamedriskandmaintainability. No client$1mstoryoractualReedrecovery invented. Visualthree methods+architecturechoices;testperson/provider/location/key/configfailures. Support/recourse/insurance are contract-specific. Advanced7.1–7.3 own detailedcomparisons.',
'7.2':'Preserve D07 safepractice versusactualwallet distinction. Current officialTrezor guides on walletbackups, Checkbackup, passphrase and troubleshooting checked; exactdevice/format/firmware procedure is still a captureprecondition. Never genericwipe fundedwallet, sharesecrets, assumecheckprovesfullpassphrase/multisig,or claimpracticecertifiesdifferentfundedwallet. Metadataonlyproofandstopconditions retained. A validwordlist≠intendedwallet.',
'7.3':'CISA phishing-resistant MFA/currentsecurity-key guidance supports mechanism;not absoluteaccountorproviderprotection. Synthetic/provider-authorizeddemonstrationonly. Registerbackupandtestbefore removingsoleworkingfactor. No secretvalues,credentials,liveclientaccountsorattack simulation. Walletdevice≠loginauthenticator. Fix prose article independentlyverified if needed.',
'7.4':'Use existing FamilyCustodyMap, notanotherworkbook. Preserveownership,custodymethod,providerandlegalroutes,scopeofrecoveryproof,operatorbackup,andprivacy ofxpub/configmetadata. Mainmapscontainno secretsorexactsecretlocations. A familyintenttoliquidate is legitimate;noforcedconvictionstory. Tabletopnoactualtransfer.',
'8.1':'Estate deck basicroles/documents/beneficiaries and currentlegalboundaries. CFPB POA and trust definitions checked;jurisdiction-specific execution/authority remainattorneyreview. Nominatedexecutor≠currentlyappointed;beneficiarydesignation≠will;trustfundingmatters. No draftedlegalinstrument,chosenReedguardianorautomatictrustrecommendation.',
'8.2':'Estateauthority pluscustodyoperationalaccess;incapacityversusdeathseparate. PrimaryCFPB trustedcontact/POA guidance;actualdeathauthority/providerrequirements dependonlawanddocuments. Neveruseownerloginasdefault or bypasssecurity;technicalhelpernotlegalowner. Immediatecashlegallyaccessiblemustbechecked. Read existing source framework notguaranteeallassetsavailable.',
'8.3':'Existing HeirLetter/ExecutorPacket examplesandnonssecret deliverystructure. Quoted paragraph is NEW illustrativeletterlanguage forlegal/familyadaptation,notlegaladviceorapprovedReedprocess. No privateclientfacts. Delivery/check-in remainsoptionalproof-requiredactualcapability;harmlessconsentedtestonly;nosecretsorfalseemergencysent.',
'8.4':'Estate/insuranceauditandGlobalBrain risk-gap framework. Generic40k×10=400k is scale-only withall omittedfactorsnamed,notcoverageadviceorReedpolicy. NAICconsumerinsuranceguideindex supports expertpolicyreview;actualtermscontrol. Medicare/noncoveredcarecurrentverification required. Preserveexistingprotectionuntilnewcoverageeffective;noinsurabilityorquote invented.'
}
CHECKPOINTS = {
'7.1':'Choose a custody direction that addresses the named failure and identify the first unfinished protection action.',
'7.2':'Record the exact scope and result of an appropriate safe recovery check, or a specific prerequisite; never certify an untested funded wallet.',
'7.3':'Complete and verify the applicable account-hardening and backup-access steps, and explain how to verify an urgent warning safely.',
'7.4':'Produce a dated no-secrets map and have the backup person explain the legitimate starting process without moving funds.',
'8.1':'Align intended people, backups, executed-document status, ownership and beneficiaries; assign the specific legal/provider correction.',
'8.2':'Connect lawful authority, operational access, immediate cash needs and technical help for incapacity and death separately.',
'8.3':'Complete the Heir Letter and Executor Packet, verify they can be found, and rehearse first actions with consent and no secret exposure.',
'8.4':'Identify actual coverage, retained risk and the most important gap; verify any replacement before relying on it and reflect costs in the plan.'
}
