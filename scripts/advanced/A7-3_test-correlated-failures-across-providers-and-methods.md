# A7.3 — Test correlated failures across providers and methods

Status: PRE_DICTATION — editorial review complete; Austin approval pending.
Adapted source: `course-v2/advanced/02-access-custody-and-estate.md` at `2343e6dc7a21b4ce6edf8e170a1890bc3cb70c9b`.
App references: accepted redesign direction; final screen behavior requires capture evidence.

Kind: advanced
Gate: CUSTODY_REVIEW
Sources: CUSTODY, BRAIN, PRIMARY
Use when: several accounts or custody methods appear diversified but may share dependencies.

### Read aloud

Multiple accounts do not automatically create independent protection. Trace the dependencies behind each method.

Two exchanges may rely on the same custodian. Two devices may share a software path. Several backups can be stored in one disaster zone. Different accounts may all be recoverable through the same email and phone. A family can have many documents and still depend on one person to interpret them.

Draw a simple dependency map. For each meaningful pool, identify the provider, signing method, recovery material, authentication channel, location category, and person who starts the process. Keep exact sensitive details in the separate protected system.

Then test one failure at a time. What becomes unavailable if the email is lost? If one provider stops serving customers? If a device and its nearby backup are destroyed? If the operator is absent? Which remaining resources actually restore access, and how has that been verified?

Also test combinations that plausibly occur together. A home disaster may affect devices, paper records, and communication access. A provider event may affect several branded services. A family emergency may reduce the time and expertise available to solve a technical problem.

For Alex and Morgan, an intentional split should reduce exposure to the failures they care about. It should not merely create another login or move Bitcoin between two services sharing the same underlying dependence. The amount assigned to each method should reflect both its job and the consequence of failure.

A lender is another custody exposure. A loan can be modest relative to total wealth while a large share of the Bitcoin is held as collateral. Record that dependence in the same family risk picture rather than isolating it in a separate borrowing spreadsheet.

The outcome is a short list of meaningful changes: separate a recovery dependence, reduce a provider concentration, prove an independent recovery path, or simplify a process. No system eliminates every risk. The objective is to know which failures remain and keep any one of them from unnecessarily controlling the whole plan.

Return to Protect with the completed non-secret map, the tested path, and the next review trigger. Revisit when the balance becomes materially larger or a provider, person, or device changes.

### Production notes

No unsupported security claims about named providers. Independence must be verified from actual architecture, not branding. Do not publish configuration/locations or detailed recovery sequences. Return to 7.3 and 8.2.

### Member checkpoint

- Map shared dependencies and correlated failures.
- Verify an independent recovery route where claimed.
- Choose a targeted change and a review trigger.
