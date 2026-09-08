# Primary-source register — professional research audit

**Verified:** 2026-08-25  
**Scope:** Module 5; Advanced A5.1–A5.3 and A6.1–A6.2; Module 7 and A7.1–A7.4; 8.1–8.5; A8.1.

This is the source layer behind the scripts. It is not read on camera. The scripts keep durable concepts in spoken prose; current-year figures and jurisdiction-specific rules stay in student text, the app, or a targeted professional signoff.

## Tax and healthcare

### Digital-asset basis and lot identification

- IRS, **Frequently asked questions on digital asset transactions**, especially Q81–Q88: transfers between the taxpayer’s own wallets; specific identification for unhosted and hosted wallets; broker identification after 2025; FIFO default when identification fails.  
  https://www.irs.gov/individuals/international-taxpayers/frequently-asked-questions-on-digital-asset-transactions
- IRS, **Publication 550 — Investment Income and Expenses**: capital gains and losses, wash-sale rule for stock or securities, annual capital-loss deduction, carryforwards.  
  https://www.irs.gov/publications/p550
- IRS, **Instructions for Form 8949**: reporting basis adjustments and explaining a basis that differs from reported basis.  
  https://www.irs.gov/instructions/i8949
- IRS, **Digital assets** and Form 1099-DA guidance: taxpayers remain responsible for reporting transactions and reconciling basis even when no information return or incomplete basis information is received.  
  https://www.irs.gov/filing/digital-assets

### Retirement accounts, RMDs, conversions, and inherited accounts

- IRS, **RMD FAQs** and **Retirement Topics — RMDs**: applicable ages, calculation, Roth-account treatment, beneficiary rules.  
  https://www.irs.gov/retirement-plans/retirement-plan-and-ira-required-minimum-distributions-faqs  
  https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-required-minimum-distributions-rmds
- IRS, **Internal Revenue Bulletin 2026-06**: SECURE 2.0 applicable age is 73 for the intermediate cohort and 75 for people attaining 74 after 2032; designated Roth accounts have no lifetime RMD.  
  https://www.irs.gov/irb/2026-06_IRB
- IRS, **Publication 590-B** and **Publication 575**: distribution tables and taxable-distribution mechanics.  
  https://www.irs.gov/publications/p590b  
  https://www.irs.gov/publications/p575
- IRS, **Instructions for Form 8606**: Roth IRA qualified-distribution and basis rules.  
  https://www.irs.gov/instructions/i8606
- IRS, **Publication 559** and Form 8949 instructions: inherited-property basis is generally date-of-death fair market value, subject to exceptions and consistent-basis reporting.  
  https://www.irs.gov/publications/p559

### Capital-gain interactions, loans, and health coverage

- IRS, **Net Investment Income Tax**: 3.8% tax, MAGI thresholds, and capital gains included in net investment income.  
  https://www.irs.gov/individuals/net-investment-income-tax
- IRS, **Topic 431 — Canceled debt** and Publication 525: borrowed proceeds are generally not income because they carry an obligation to repay; cancellation or collateral disposition can create tax consequences.  
  https://www.irs.gov/taxtopics/tc431  
  https://www.irs.gov/publications/p525
- IRS, **Premium Tax Credit** guidance and 2026 applicable-percentage table: Marketplace credits depend on household income and the benchmark plan; the enhanced pandemic-era subsidy rules ended after 2025.  
  https://www.irs.gov/affordable-care-act/individuals-and-families/questions-and-answers-on-the-premium-tax-credit  
  https://www.irs.gov/pub/irs-drop/rp-25-25.pdf
- CMS / HealthCare.gov, **2026 Marketplace changes** and cost-sharing reductions: current eligibility and Silver-plan rules must be checked in the enrollment year.  
  https://www.healthcare.gov/lower-costs/save-on-monthly-premiums/  
  https://www.healthcare.gov/lower-costs/save-on-out-of-pocket-costs/

## Bitcoin custody and authentication

### Wallet backups, passphrases, multisig, and descriptors

- BIP 39: mnemonic lengths and optional passphrase; every passphrase derives a valid seed.  
  https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
- BIP 380: output descriptors describe wallet scripts and keys; a descriptor is wallet-policy/watch-only data, not a signature.  
  https://github.com/bitcoin/bips/blob/master/bip-0380.mediawiki
- BIP 383: `multi(k,...)` threshold semantics.  
  https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki
- SLIP 39: a supported threshold-backup standard; splitting a BIP39 mnemonic by hand is not threshold secret sharing.  
  https://github.com/satoshilabs/slips/blob/master/slip-0039.md
- Bitcoin Core, **Descriptors** documentation.  
  https://github.com/bitcoin/bitcoin/blob/master/doc/descriptors.md

### Authentication and operational verification

- NIST SP 800-63B-4: PSTN/SMS is restricted; manually entered OTPs are not phishing-resistant; cryptographic authenticators can be phishing-resistant.  
  https://csrc.nist.gov/pubs/sp/800/63/b/4/final
- Device and wallet procedures must be checked against the exact manufacturer, firmware, backup standard, script type, and wallet software used. Vendor-supported backup checks or a spare-device restore are safer first tests than destroying the only working copy.

## Insurance

- NAIC, **Life Insurance** and consumer guidance: term versus permanent, needs analysis, policy replacement, beneficiary review.  
  https://content.naic.org/consumer/life-insurance.htm
- NAIC, **What’s an umbrella policy?**: excess liability and defense-cost purpose, underlying-limit requirements, and exclusions.  
  https://content.naic.org/article/whats-umbrella-policy
- NAIC, **Long-Term Care Insurance**: policy forms, benefit triggers, exclusions, premiums, rate changes, and alternatives vary materially.  
  https://content.naic.org/consumer/long-term-care-insurance
- IRS, **Life insurance proceeds** and **Disability pensions**: death proceeds are generally excluded from income with exceptions; disability-benefit taxation depends on who paid premiums and whether premiums were paid pre- or after-tax.  
  https://www.irs.gov/help/ita/are-the-life-insurance-proceeds-i-received-taxable  
  https://www.irs.gov/taxtopics/tc410
- NAIC, healthcare-sharing ministries: these arrangements are not insurance and generally do not carry a legal obligation to pay claims.  
  https://content.naic.org/article/consumer-alert-health-care-sharing-ministries

## Estate, digital assets, and trusts

- Uniform Law Commission, **Revised Uniform Fiduciary Access to Digital Assets Act**: fiduciary access, online tools, and explicit consent for content of electronic communications.  
  https://www.uniformlaws.org/committees/community-home?CommunityKey=f7237fc4-74c2-4728-81c6-b39a91ecdf22
- Uniform Law Commission, **Uniform Prudent Investor Act**: portfolio-level prudence and diversification as the general default, subject to the trust’s terms and state enactment.  
  https://www.uniformlaws.org/committees/community-home?CommunityKey=58f87d0a-3617-4635-a2af-9a4d02d119c9
- U.S. Department of Labor, **Retirement plan beneficiaries / spouse protections**: plan terms, federal law, spousal consent, and QDROs can affect who receives retirement assets.  
  https://www.dol.gov/agencies/ebsa/workers-and-families/death-of-a-family-member
- IRS, **Publication 559**, **Estate and Gift Taxes**, and gross-estate guidance: retained powers, ownership, completed gifts, and trust terms determine estate inclusion and basis consequences.  
  https://www.irs.gov/publications/p559  
  https://www.irs.gov/businesses/small-businesses-self-employed/estate-and-gift-taxes

## Evidence standard

1. Federal tax claims use IRS material first.
2. Protocol claims use BIPs, Bitcoin Core, or the exact vendor’s current documentation.
3. Insurance-category claims use NAIC and contract language; quotes and recommendations require a licensed producer.
4. Estate claims use federal sources and uniform-law texts for the general rule; state-specific wording requires counsel licensed in the governing state.
5. A current source does not turn a general rule into personalized advice. Student action still depends on their records, jurisdiction, contracts, and plan.