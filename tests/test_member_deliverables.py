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

    def test_existing_inventory_is_preserved(self):
        counts = json.loads(read('COURSE-MANIFEST.json'))['counts']
        self.assertEqual(counts, {'core':51, 'advanced':15, 'working_sessions':10, 'device_demos':1})


if __name__ == '__main__':
    unittest.main(verbosity=2)
