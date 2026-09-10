"""Source-pinned checks for the Academy member deliverables. No network or writes."""
from decimal import Decimal as D
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['family-custody-map', 'heir-letter', 'executor-packet',
         'insurance-coverage-audit', 'household-plan-summary', 'annual-plan-refresh']


def read(path):
    return (ROOT / path).read_text(encoding='utf-8')


def blob_id(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


class MemberDeliverables(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(read('fixtures/reed-household.json'), parse_float=D)
        cls.worked = read('delivery/reed-worked-plan.md')
        cls.docs = [read('toolkit/deliverables/' + name + '.md') for name in NAMES]

    def test_source_fixture_is_exact_reviewed_blob(self):
        self.assertEqual(blob_id((ROOT / 'fixtures/reed-household.json').read_bytes()),
                         '0359ef0bc3a87387488fd32980dbe7f670776467')

    def test_all_six_blank_and_fictional_examples_exist(self):
        for text in self.docs:
            self.assertEqual(text.count('## Blank template'), 1)
            self.assertEqual(text.count('## Filled fictional example'), 1)

    def test_source_and_new_prose_are_distinguished(self):
        for text in self.docs:
            self.assertIn('ec021e3a0368a0955ab689551602104e426350a6', text)
            self.assertIn('fictional', text.lower())

    def test_family_documents_keep_secrets_private(self):
        for text in self.docs[:4]:
            self.assertIn('privat', text.lower())
            self.assertIn('recovery', text.lower())
        self.assertIn('not a will', self.docs[1])
        self.assertIn('does not appoint an executor', self.docs[2])
        self.assertIn('does not choose a policy', self.docs[3])

    def test_balance_sheet_and_denominator(self):
        a = self.fixture['accounts']
        total = sum(D(x['value']) for x in a)
        general = sum(D(x['value']) for x in a if x['general_portfolio'])
        debt = sum(D(x['balance']) for x in self.fixture['debts'])
        self.assertEqual((total, general, debt, total-debt),
                         (D(1996000), D(1307000), D(444500), D(1551500)))
        for value in [total, general, debt, total-debt]:
            self.assertIn(f'${value:,.0f}', self.worked)

    def test_bitcoin_exposure_not_native_units(self):
        a = self.fixture['accounts']
        quantity = sum(D(str(x.get('btc_quantity', 0))) for x in a)
        native = sum(D(x.get('holdings', {}).get('bitcoin', 0)) for x in a)
        funds = sum(D(x.get('holdings', {}).get('bitcoin_spot_fund', 0)) for x in a)
        self.assertEqual((quantity, native, funds), (D('4.1'), D(410000), D(318000)))
        self.assertIn('$728,000', self.worked)

    def test_original_and_reduced_cash_flow_do_not_mix(self):
        c = self.fixture['cash_flow']
        income = (D(c['alex_annual_gross']) + D(c['morgan_annual_income'])) / 12
        employee = D(c['alex_annual_gross']) * c['alex_employee_percent'] / 12
        payments = sum(D(x['monthly_payment']) if 'monthly_payment' in x else
                       D(x['balance'])*x['apr']/12 for x in self.fixture['debts'])
        available = income - D(c['monthly_tax_provision']) - employee - payments - D(c['original_monthly_living'])
        reduced = available + D(c['adopted_monthly_spending_reduction'])
        self.assertEqual(available.quantize(D('.01')), D('500.00'))
        self.assertEqual(reduced.quantize(D('.01')), D('1700.00'))
        self.assertEqual(D(c['reduced_spending_monthly_reserve_build']) +
                         D(c['reduced_spending_monthly_extra_card']), reduced.quantize(D('.01')))
        self.assertIn('$0.00', self.worked)

    def test_match_is_separate(self):
        c = self.fixture['cash_flow']
        match = D(c['alex_annual_gross'])*c['alex_employee_percent']*c['employer_match_per_employee_dollar']/12
        self.assertEqual(match, D('387.5000'))
        self.assertIn('never added to spendable surplus', self.worked)

    def test_reserve_target_gap_and_months(self):
        r = self.fixture['reserve']
        target = D(r['essential_monthly_outflow'])*D(r['target_months'])
        gap = target-D(r['assigned_current_value'])
        self.assertEqual((target, gap, gap/D(r['monthly_build'])), (D(43200), D(11200), D('22.4')))
        self.assertTrue(r['includes_required_debt_service'])
        self.assertIn('month 23', self.worked)

    def test_college_is_not_extra_available_money(self):
        e = self.fixture['education_example']
        gap = D(e['annual_parent_commitment'])*D(e['years_supported'])-D(e['oldest_assignment'])
        self.assertEqual((gap, gap/D(e['months_to_prefund'])), (D(51000), D(850)))
        self.assertIn('does not fit on top', self.worked)

    def test_future_routing_is_conditional(self):
        f = self.fixture['future_routing_example']
        self.assertEqual(f['personally_held_bitcoin']+f['taxable_stock_fund'], f['available_after_card'])
        self.assertEqual(f['available_after_card'], 1605)
        self.assertIn('conditional future comparison', self.worked)
        self.assertIn('not a report that a year has passed', self.docs[5])

    def test_no_invented_forecast_or_recovery_acceptance(self):
        self.assertIn('Not calculated in this pass', self.worked)
        self.assertIn('No recovery proof supplied', self.docs[0])
        self.assertIn('Rehearsal status: not performed', self.docs[2])
        self.assertNotIn('82.4%', self.worked)
        self.assertEqual(blob_id((ROOT / 'CAPTURE-RECEIPTS.md').read_bytes()),
                         '3f2593d83d57f979070b0d1dae95a958671263af')

    def test_relative_links_resolve(self):
        paths = list((ROOT / 'toolkit/deliverables').glob('*.md')) + [ROOT/'toolkit/README.md']
        for path in paths:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if not target.startswith(('https:', 'http:', '#')):
                    self.assertTrue((path.parent / target.split('#')[0]).resolve().is_file(), (path, target))

    def test_inventory_and_authorized_custody_merge(self):
        manifest = json.loads(read('COURSE-MANIFEST.json'))
        self.assertEqual(manifest['counts'], {'core':25, 'advanced':8, 'working_sessions':10, 'device_demos':1})
        ids = {row['id'] for row in manifest['lessons']}
        self.assertEqual(len(ids), 44)
        self.assertNotIn('A7.2', ids)
        self.assertEqual(len(manifest['member_order']), 33)
        self.assertEqual(len(set(manifest['member_order'])), 33)
        merged = manifest['merged_lessons']
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]['id'], 'A7.2')
        self.assertEqual(merged[0]['source_commit'], 'f6392a6341c23c557e605506dab3530b67efa146')
        self.assertEqual(merged[0]['blob'], '0443c4640a4f4b431429eab204f5fe9dc0b67413')
        self.assertEqual(merged[0]['original_destinations'], ['7.1', '7.4', 'W07'])
        self.assertEqual(merged[0]['destinations'], ['7.1', '8.1', 'W07'])
        self.assertTrue(set(merged[0]['destinations']).issubset(ids))
        self.assertFalse((ROOT / merged[0]['path']).exists())


    def test_consolidation_maps_every_prior_script(self):
        c=json.loads(read('production/consolidation.json'))
        self.assertEqual(len(c['mapping']),65)
        self.assertEqual(len({r['old_id'] for r in c['mapping']}),65)
        self.assertEqual(sum(r['retired_active_file'] for r in c['mapping']),32)
        self.assertTrue(all(r['destinations'] for r in c['mapping']))
        for r in c['mapping']:
            if r['retired_active_file']:self.assertFalse((ROOT/r['old_path']).exists())

    def test_preserved_accepted_reserve_is_exact_except_prior_approved_language(self):
        import sys
        sys.path.insert(0,str(ROOT/'tools'))
        from guided_course import accepted_reserve_bytes
        # New owner direction authorizes the active rewrite; its predecessor stays exact.
        # test_stepwise_filming separately pins and exercises the active scripts.
        current=(ROOT/'source-material/pre-stepwise/02-3_size-the-reserve-for-the-job-it-has-to-do.md').read_bytes()
        self.assertEqual(blob_id(accepted_reserve_bytes(current)),'2c107a394a93cc877c73f011dfe37fb5ad3d94b1')

    def test_situation_and_reference_are_not_extra_main_videos(self):
        c=json.loads(read('production/consolidation.json'))
        self.assertEqual(len(c['main_ids']),25)
        self.assertEqual(len(c['situation_ids']),8)
        self.assertNotIn('2.5',c['main_ids'])
        self.assertIn('2.5',c['situation_ids'])
        self.assertEqual(set(c['reference_files']),{'A1.1','A5.3','A7.4'})
        for path in c['reference_files'].values():self.assertTrue((ROOT/path).is_file())

    def test_consolidated_loan_extension(self):
        self.assertEqual((D(28000)+25000)*D('1.12'),D(59360))
        self.assertEqual(D(59360)-50000,D(9360))


class September10ScriptFinish(unittest.TestCase):
    def test_borrowing_boundaries_and_reserve(self):
        loan=read('teleprompter/advanced/A3-1.txt')
        for text in ['3.125', '2.5 BTC', '71.4%', '16%', 'maturity', 'confirmation', '12%', '$59,360']:
            self.assertIn(text,loan)
        self.assertIn("Exactly 3.125 isn't enough",loan)
        self.assertIn("It can't simply take Bitcoin from your cold wallet",loan)
        self.assertEqual(D(50000)/D('.8')/20000,D('3.125'))
        self.assertGreater(D(50000)/(D('3.5')*20000),D('.65'))
        self.assertLess(D(50000)/(D('3.5')*20000),D('.8'))

    def test_guardrail_cap_and_source_boundary(self):
        text=read('teleprompter/core/6-8.txt')
        for phrase in ['60% or below','95% or above','different rules from Orange Plan',
                       "The cap hasn't restored 80% confidence",'made up','$92,700','$26,350','$7,700']:
            self.assertIn(phrase,text)
        inflated=D(100000)*D('1.03')
        self.assertEqual(max(D(86000),inflated*D('.9')),92700)
        self.assertEqual(max(D(99000),inflated*D('.9')),99000)
        self.assertEqual(min(D(120000),inflated*D('1.1')),113300)
        self.assertEqual((D(92700)-40000)/12*6,26350)

    def test_insurance_uses_needs_not_a_net_worth_cutoff(self):
        text=read('teleprompter/core/8-4.txt')
        self.assertIn("I wouldn't use one net-worth number for everyone",text)
        self.assertIn('later retirement and other obligations are funded separately',text)
        self.assertIn('income interrupted at the same time',text)
        self.assertIn('Personal umbrella',text)
        self.assertEqual(D(40000)*10-100000-200000,100000)
        self.assertEqual(D(2000000)-500000-1000000,500000)

    def test_missed_voice_lines_and_security_order_are_fixed(self):
        files={'2-3':['cannot','genuinely available','They are also'],
               '4-5':['seventy percent','fifty-nine and a half'],
               '3-6':['then multiply by 100'],
               '6-3':["We'll compare coverage, check how income"],
               '7-1':["That's how we'll choose custody:"],
               '7-2':['We want the first situation.','They perform different jobs.']}
        for lid,phrases in files.items():
            text=read('teleprompter/core/'+lid+'.txt')
            for phrase in phrases:self.assertNotIn(phrase,text)
        self.assertNotIn('eight hundred fifty',read('teleprompter/advanced/2-5.txt'))
        text=read('teleprompter/core/7-2.txt')
        self.assertLess(text.index('security keys or passkeys'),text.index('authenticator app'))
        self.assertLess(text.index('authenticator app'),text.index('SMS as a last resort'))
        self.assertNotIn('phishing-proof',text)

    def test_preserved_reserve_only_contains_prior_authorized_wording_changes(self):
        import sys
        sys.path.insert(0,str(ROOT/'tools'))
        from guided_course import accepted_reserve_bytes
        p='source-material/pre-stepwise/02-3_size-the-reserve-for-the-job-it-has-to-do.md'
        data=read(p).encode()
        expected='2c107a394a93cc877c73f011dfe37fb5ad3d94b1'
        self.assertEqual(blob_id(accepted_reserve_bytes(data)),expected)
        mutated=data.replace(b'$43,200',b'$44,200')
        self.assertNotEqual(blob_id(accepted_reserve_bytes(mutated)),expected)


class BoundedReviewFollowup(unittest.TestCase):
    def test_loan_sizing_conditions_appear_before_initial_posting(self):
        text = read('teleprompter/advanced/A3-1.txt')
        start = text.index("I wouldn't borrow right up to that number")
        end = text.index("Once I've sized the loan at $50,000")
        sizing = text[start:end]
        self.assertIn("interest and fees are paid from cash flow we've already allowed for", sizing)
        self.assertIn("If they'll be added to the balance", sizing)
        self.assertIn("reduce the starting loan or set aside more Bitcoin before borrowing", sizing)
        self.assertIn("All $6,000 of room is gone", text)
        self.assertEqual(D(56000) - 50000, D(50000) * D('.12'))
        self.assertEqual(D(50000) * D('1.12') / 70000, D('.8'))

    def test_loan_custody_comparison_names_both_denominators(self):
        text = read('teleprompter/advanced/A3-1.txt')
        self.assertIn("Posting all 3.5 BTC upfront would start the same loan at about 14.3% LTV", text)
        self.assertIn("That's why I might start at 50% instead", text)
        self.assertEqual((D(50000) / (D('3.5') * 100000) * 100).quantize(D('.1')), D('14.3'))

    def test_main_borrowing_comparison_is_not_a_competing_default(self):
        text = read('teleprompter/core/3-6.txt')
        self.assertIn("posting more collateral to start the same loan at 25% LTV", text)
        self.assertIn("25% shows the effect of more upfront collateral, not a recommended starting point", text)
        self.assertIn("Then I might start the chosen loan at 50% LTV", text)

    def test_assumptions_keep_failure_mode_and_conservative_reason(self):
        text = read('teleprompter/core/1-4.txt')
        self.assertIn("Don't choose the most optimistic return just to reach the retirement date you want.", text)
        self.assertIn("I'd rather be conservative and end up with more than plan aggressively and fall short.", text)

    def test_owner_sources_do_not_claim_upstream_edits_or_licensed_review(self):
        text = read('reference/owner-decisions-20260910.md')
        self.assertIn("I think it depends on risk tolerance", text)
        self.assertIn("If their family can thrive with assets", text)
        self.assertIn("where does alfred come from? we are using claude to cross check.", text)
        self.assertIn("It is superseded as the current course's posted-LTV default", text)
        self.assertIn("does **not** claim those external originals or project settings were edited", text)
        self.assertIn("Model review is not licensed", text)
        for path in ['AUSTIN-AUTHORITY.md', 'reference/script-finishing-sources.md',
                     'scripts/08-4_identify-the-risks-you-will-transfer-or-carry.md']:
            self.assertIn('owner-decisions-20260910.md', read(path))

    def test_bounded_pass_original_insurance_and_reserve_remain_preserved(self):
        for path, expected in [
            ('source-material/pre-stepwise/8-4.txt', '393118d5c8d582b77927138a5014e7ba2c41aa7e438574f287c5b314a8f96f1b'),
            ('source-material/pre-stepwise/02-3_size-the-reserve-for-the-job-it-has-to-do.md', 'bcf42a95d1ee40e7e5164cf1e259a59ccc1d939d897af16cbcafa63a3728b8f7'),
        ]:
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
