# 7.3 — Harden accounts and remove the largest shared failure

Status: SOURCE_LED_REVIEW — source-based editorial pass complete; integrated wording awaits Austin's voice/judgment review. Publication gates remain open.
Adapted source: `course-v2/sessions/07-custody.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: teach
Gate: CUSTODY_REVIEW
Sources: CUSTODY, DICTATION, PRIMARY, CLIENT_THEMES

### Read aloud

Look beyond the wallet to the accounts and people around it. A weak recovery email, a shared device, or an urgent-looking message can undermine an otherwise thoughtful custody arrangement. Find the largest avoidable failure and address it first.

Start with the email account used to recover financial accounts. Use a unique strong password and the strongest supported authentication you can maintain. A phishing-resistant security key or passkey can reduce attacks that rely on a convincing fake sign-in page. An authenticator code is useful where that stronger option is unavailable, but a code can still be entered into the wrong site.

Secure the recovery path too. An excellent primary login can be undermined by a weak recovery email, easily abused phone reset, or lost backup authentication method. Keep the recovery information private and make sure a lost phone or key does not leave you unable to access the account.

For exchanges and custodians, review withdrawal controls, address allowlisting where supported, delays, alerts, and the provider's recovery process. These controls have different limitations. An allowlist does not protect a seed stored in the wrong place, and a delayed withdrawal does not eliminate provider or account-takeover risk.

Use trusted bookmarks or enter the known address when logging in. A message that says the account is in danger should lead you to independently contact the provider, not to follow the message's link or call the number it supplied. Urgency is often used to make someone skip verification.

No legitimate support process needs your seed phrase or private key. A request to move funds to a supposed safe wallet, send money to unlock a withdrawal, or accept an unsolicited recovery expert deserves an immediate stop. Verify through a known official channel before doing anything with the assets.

Now look for shared failures. Two backup envelopes in the same building can be lost in the same disaster. Two devices may depend on the same software or vendor. Two providers may rely on one custodian. A family process can depend entirely on one technically capable person.

Rank the few weaknesses by consequence and likelihood, then fix one at a time. An additional method should solve the failure you named. Adding hardware or accounts without improving independence can make the household harder to maintain without making recovery more robust.

For the Reeds, compare three possible first actions: strengthen critical account access, verify the actual wallet backup, or make the family starting instructions usable without Alex. Choose the one addressing the largest uncovered consequence, then verify that improvement before adding more equipment or accounts.

If a lost phone would block both the financial login and its recovery path, adding a second account behind the same phone has not fixed the problem. Trace the dependency all the way through the recovery process.

Review physical risk as well. Publicly sharing exact holdings or locations can create exposure. The financial plan needs enough information to explain the assets and their custody, not a complete map for finding and moving them. Keep sensitive recovery instructions separate and appropriately protected.

A calm routine helps with transactions too. Verify the destination, amount, network, fee, and purpose before authorizing a move. Use the current official procedure and a small test when appropriate. Stop when a screen, address, or instruction differs from what you expected.

This working-session chapter records the top unfinished action, the responsible person, and the deadline. The external security work happens with the provider or device. Mark it complete only when the control was actually enabled or the process tested.

Record the improvement, who carries it out, and what evidence will show it worked. After enabling or testing it, update the status honestly. The result should be fewer ways for one mistake or unavailable resource to disrupt the household—not simply more security products to maintain.

### Production notes

CISA phishing-resistant MFA guidance supports the authentication distinction. Avoid statistical claims such as most Bitcoin losses occur by one specific cause unless sourced. Do not claim passkeys prevent every takeover or every provider supports all controls. No personal bank-fraud story invented for Austin.

### Member checkpoint

- Secure primary and recovery channels for critical accounts.
- Identify shared provider, device, location, and person dependencies.
- Complete and verify one material security improvement.

### Source-led visual and teaching notes — not spoken

Primary access → recovery access → independent backup route. Run one lost-phone or unavailable-person test without exposing recovery codes, phone numbers or key material. No claim a particular provider offers every control.

Editorial reason: Give account hardening a prioritized practical test rather than an undifferentiated security checklist.

See `delivery/source-led-completion.md` for the source and verification boundary. Existing factual and professional gates are not waived. New wording is an editorial proposal, not prior Austin dictation.
