#!/usr/bin/env python3
"""Check the debt pilot's arithmetic and single-video manuscript structure.

Run from any directory: python pilots/debt/check_debt_pilot.py
These checks are not a learner test, lender quote, or app-engine receipt.
"""
from __future__ import annotations
import json
import math
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
checks: list[str] = []


def near(name: str, actual: float, expected: float, tolerance: float = 1e-8) -> None:
    if not math.isclose(actual, expected, rel_tol=0, abs_tol=tolerance):
        raise AssertionError(f"{name}: got {actual}, expected {expected}")
    checks.append(name)


def payoff(balance: float, apr: float, payment: float) -> tuple[int, float]:
    """Monthly interest followed by month-end payment; final payment is smaller."""
    total_interest = 0.0
    for month in range(1, 1201):
        interest = balance * apr / 12
        actual_payment = min(payment, balance + interest)
        if actual_payment <= interest:
            raise ValueError("Payment does not amortize the balance")
        balance += interest - actual_payment
        total_interest += interest
        if balance < 1e-8:
            return month, total_interest
    raise ValueError("Payoff exceeds 100 years")


def main() -> None:
    f = json.loads((ROOT / 'fixtures/reed-household.json').read_text())
    assets = sum(a['value'] for a in f['accounts'])
    debts = sum(d['balance'] for d in f['debts'])
    payments = sum(d.get('monthly_payment', d['balance'] * d['apr'] / 12) for d in f['debts'])
    income = (f['cash_flow']['alex_annual_gross'] + f['cash_flow']['morgan_annual_income']) / 12
    employee = f['cash_flow']['alex_annual_gross'] * f['cash_flow']['alex_employee_percent'] / 12
    original_surplus = income - payments - f['cash_flow']['monthly_tax_provision'] - f['cash_flow']['original_monthly_living'] - employee
    stress_assets = 0.0
    for account in f['accounts']:
        if account['id'] == 'home':
            stress_assets += account['value'] * .8
        elif 'holdings' in account:
            for asset, value in account['holdings'].items():
                multiplier = .3 if asset in ('bitcoin', 'bitcoin_spot_fund') else .7 if asset == 'stocks' else 1
                stress_assets += value * multiplier
        else:
            stress_assets += account['value']

    cases = [
        ('business interest', 100000*.05, 5000),
        ('expected project return', 100000*.18, 18000),
        ('interest on extra principal', 10000*.04, 400),
        ('generic debt/assets', 200000/800000, .25),
        ('Reed asset total', assets, 1996000),
        ('Reed debt total', debts, 444500),
        ('Reed equity', assets-debts, 1551500),
        ('Reed debt/assets rounded', round(debts/assets*100), 22),
        ('Reed payments rounded', round(payments), 3342),
        ('Reed income rounded', round(income), 19417),
        ('Reed DTI rounded', round(payments/income*100), 17),
        ('original surplus', original_surplus, 500),
        ('generic DTI', 2000/8000, .25),
        ('chosen payment ceiling', 8000*.25, 2000),
        ('ratio payment room', 2000-1600, 400),
        ('tighter cash room', min(400,250), 250),
        ('proposed payment shortfall', 350-250, 100),
        ('chosen asset ceiling', 800000*.25, 200000),
        ('stressed assets', stress_assets, 1217200),
        ('stressed ratio rounded', round(debts/stress_assets*100), 37),
        ('halved-income DTI rounded', round(payments/(income/2)*100), 34),
        ('reserve months', 32000/7200, 4.444444444444445),
        ('reserve target', 7200*6, 43200),
        ('reserve gap', 43200-32000, 11200),
        ('rally example original payments', 1200/8000, .15),
        ('rally example new payments', (1200+2000)/8000, .4),
        ('loan IO monthly', 20000*.08/12, 133.33333333333334),
        ('loan IO interest five years', 20000*.08*5, 8000),
        ('stressed BTC price', 100000*(1-.8), 20000),
        ('stressed supporting BTC', 3.5*20000, 70000),
        ('flat loan stressed LTV', 50000/70000, .7142857142857143),
        ('liquidation dollars', 50000/.8, 62500),
        ('liquidation coins', 50000/.8/20000, 3.125),
        ('liquidation boundary multiplier', (1-.8)*.8, .16),
        ('liquidation debt boundary', 350000*.16, 56000),
        ('one-year accrued interest', 50000*1.12, 56000),
        ('headroom consumed', 56000-50000, 6000),
        ('LTV with accrued balance', 56000/70000, .8),
        ('65% cure collateral', 50000/.65, 76923.07692307692),
        ('65% cure BTC', 50000/.65/20000, 3.8461538461538463),
        ('65% cure BTC with interest', 56000/.65/20000, 4.3076923076923075),
        ('65% debt capacity', 70000*.65, 45500),
        ('opening cure boundary with interest', 45500/1.12, 40625),
        ('resized loan with interest', 35000*1.12, 39200),
        ('resized stressed LTV', 39200/70000, .56),
        ('resized initial collateral dollars', 35000/.5, 70000),
        ('resized initial collateral BTC', 35000/.5/100000, .7),
        ('resized reserved BTC', 3.5-.7, 2.8),
        ('resized all-posted LTV', 35000/350000, .1),
        ('initial price drop to 80% liquidation', 1-.5/.8, .375),
        ('HELOC interest rounded', round(46000*.08/12), 307),
        ('reserve after project', 32000-30000, 2000),
        ('reduced-spending surplus', original_surplus+1200, 1700),
        ('uses of surplus', 500+1200, 1700),
        ('total card payment', 405+1200, 1605),
    ]
    pmt = 20000*(.08/12)/(1-(1+.08/12)**-60)
    cases += [
        ('amortizing monthly payment', pmt, 405.5278857682771),
        ('payment flexibility rounded', round(pmt-20000*.08/12), 272),
        ('amortizing total interest rounded', round(pmt*60-20000), 4332),
    ]
    slow_months, slow_interest = payoff(13500,.209,405)
    fast_months, fast_interest = payoff(13500,.209,1605)
    cases += [
        ('fixed 405 payoff months', slow_months, 51),
        ('fixed 1605 payoff months', fast_months, 10),
        ('fixed 405 interest rounded', round(slow_interest), 6879),
        ('fixed 1605 interest rounded', round(fast_interest), 1226),
        ('interest saved rounded', round(slow_interest-fast_interest), 5653),
    ]
    for name, actual, expected in cases:
        near(name, actual, expected)

    text = (HERE/'DEBT-VIDEO.md').read_text()
    chapters = re.findall(r'^## (\d)\. ',text,re.M)
    if chapters != list('123456'):
        raise AssertionError(f"Expected six ordered chapters, got {chapters}")
    if text.count('[SCREEN SHARE BEGINS.') != 1:
        raise AssertionError('Expected one clearly marked screen-share transition')
    if re.search(r'\b(TODO|TBD|INSERT SCRIPT)\b',text):
        raise AssertionError('Unwritten content placeholder')
    required = ['$76,923','3.85 BTC','4.31 BTC','$40,625','$39,200','56% LTV',
                'no stricter cure or maturity limit','51 months','10 months','$5,653',
                'fixed payment amounts','not a claim that the unfinished app',
                'Zero debt is fine too',"Saving a plan doesn't move the money."]
    for phrase in required:
        if phrase not in text:
            raise AssertionError(f'Missing decision-critical wording: {phrase}')
    for local_target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', (HERE/'REVIEW-NOTES.md').read_text()):
        if '://' not in local_target and not (HERE/local_target).resolve().is_file():
            raise AssertionError(f'Broken local reference: {local_target}')
    print(f'PASS: {len(checks)} arithmetic checks; six-chapter structure; explicit capture boundary; decision-critical wording; local links.')
    print('No app-engine run, human learner test, licensed review or owner approval is asserted.')


if __name__ == '__main__':
    main()
