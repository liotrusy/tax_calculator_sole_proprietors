import pytest
import calculation_logic as calculator

def test_tax_percentage_assigner():
    assert calculator.assign_tax_percentage(5) == 0.05
    assert calculator.assign_tax_percentage(6) == 0.15

def test_gross_taxable_income_calculator():
    """test the gross taxable income calculator, accepted values are validated prior to passing the arguments"""
    assert calculator.calculate_gross_taxable_income(1000, 0.78) == 780
    assert calculator.calculate_gross_taxable_income(1000, 0.54) == 540

def test_net_taxable_income_calculator():
    assert calculator.calculate_net_taxable_income(799, 0) == 799
    assert calculator.calculate_net_taxable_income(799, 100) == 699

def test_tax_calculator():
    assert calculator.calculate_tax(799, 0.15, 0) == (119.85, 119.85)
    assert calculator.calculate_tax(699, 0.15, 0) == (104.85, 104.85)
    assert calculator.calculate_tax(799, 0.15, 50) == (119.85, 69.85)