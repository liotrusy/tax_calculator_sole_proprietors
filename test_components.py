import pytest
import calculation_logic.calculation_logic as calculator
import assignment_logic.assignment_logic as assignment

class TestCalculationLogic:

    def test_tax_percentage_assigner(self):
        assert calculator.assign_tax_percentage(5) == 0.05
        assert calculator.assign_tax_percentage(6) == 0.15

    def test_gross_taxable_income_calculator(self):
        """test the gross taxable income calculator, accepted values are validated prior to passing the arguments"""
        assert calculator.calculate_gross_taxable_income(1000, 0.78) == 780
        assert calculator.calculate_gross_taxable_income(1000, 0.54) == 540

    def test_net_taxable_income_calculator(self):
        assert calculator.calculate_net_taxable_income(799, 0) == 799
        assert calculator.calculate_net_taxable_income(799, 100) == 699

    def test_tax_calculator(self):
        assert calculator.calculate_tax(799, 0.15, 0) == (119.85, 119.85)
        assert calculator.calculate_tax(699, 0.15, 0) == (104.85, 104.85)
        assert calculator.calculate_tax(799, 0.15, 50) == (119.85, 69.85)

class TestAssignmentLogic:
    pass
    # there are three main variables that should be return after the assignment

    # expense_coefficient
    # sector_group
    # progressive_id

    # looking at the table the definiton is based on codes that range from 2 to 5 characters (.dot included)