# Split access: dual control and redundancy

- **Dual control:** one person or item cannot authorize the whole spend.
- **Redundancy:** one loss cannot permanently block recovery.

A single-signature backup copied three times is redundant by location but every copy can still spend. A passphrase creates two required recovery elements but is not on-chain multisig. A tested 2-of-3 policy can pass both tests when the policy/descriptor is recoverable.

The course no longer prescribes one universal Level 2 holder arrangement. For a single-signature wallet, record who can technically recover, who is legally authorized, how copies are protected, whether one-person spending is accepted, and the trigger for moving to a different design.

Legal roles and key roles must agree. The descriptor cannot sign and does not change the multisig threshold.

## YOUR DECISION

Which access test the setup passes, which it fails, and why that trade-off is accepted.

## PUT IT IN ORANGE PLAN

Record the level and recovery-test status in Protect without storing the secret distribution.

## YOU ARE DONE WHEN

Both tests are answered honestly and the intended recovery team has tested the process without giving one unintended person enough to spend.

*Research source: `research/PRIMARY-SOURCE-REGISTER.md`.*
