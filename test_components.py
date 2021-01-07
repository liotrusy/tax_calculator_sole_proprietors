import pytest
import calculation_logic.calculation_logic as calc_logic
import assignment_logic.assignment_logic as assignment

class TestCalculationLogic:

    def test_tax_percentage_assigner(self):
        assert calc_logic.assign_tax_percentage(5) == 0.05
        assert calc_logic.assign_tax_percentage(6) == 0.15

    def test_gross_taxable_income_calculator(self):
        """test the gross taxable income calculator, accepted values are validated prior to passing the arguments"""
        assert calc_logic.calculate_gross_taxable_income(1000, 0.78) == 780
        assert calc_logic.calculate_gross_taxable_income(1000, 0.54) == 540

    def test_net_taxable_income_calculator(self):
        assert calc_logic.calculate_net_taxable_income(799, 0) == 799
        assert calc_logic.calculate_net_taxable_income(799, 100) == 699

    def test_calculation_logic(self):
        assert calc_logic.calculate_net_tax(799, 0.15, 0) == 119.85
        assert calc_logic.calculate_net_tax(699, 0.15, 0) == 104.85
        assert calc_logic.calculate_net_tax(799, 0.15, 50) == 69.85

class TestAssignmentLogic:

    def test_input_response(self):
        assert assignment.clean_input("10.10") == "1010"
        assert assignment.clean_input("10.10.20.10") == -1 # input too long
        assert assignment.clean_input("01.10") == "0110"

    def test_group_1(self):
        assert assignment.assign_expense_coefficient("101111") == (0.40, 1)
        assert assignment.assign_expense_coefficient("111011") == (0.40, 1)

    def test_group_2(self):
        assert assignment.assign_expense_coefficient("462310") == (0.40, 2)
        assert assignment.assign_expense_coefficient("473510") == (0.40, 2)
        assert assignment.assign_expense_coefficient("479100") == (0.40, 2)
        assert assignment.assign_expense_coefficient("4510101") == (0.40, 2)

    def test_group_3(self):
        assert assignment.assign_expense_coefficient("4781") == (0.4, 3)

    def test_group_4(self):
        assert assignment.assign_expense_coefficient("4782") == (0.4, 4)
        assert assignment.assign_expense_coefficient("4789") == (0.4, 4)

    def test_group_5(self):
        assert assignment.assign_expense_coefficient("410000") == (0.86, 5)
        assert assignment.assign_expense_coefficient("421010") == (0.86, 5)
        assert assignment.assign_expense_coefficient("431010") == (0.86, 5)
        assert assignment.assign_expense_coefficient("680000") == (0.86, 5)     

    def test_group_6(self):
        assert assignment.assign_expense_coefficient("4611") == (0.62, 6)
        assert assignment.assign_expense_coefficient("46189") == (0.62, 6)

    def test_group_7(self):
        assert assignment.assign_expense_coefficient("551010") == (0.4, 7)
        assert assignment.assign_expense_coefficient("561011") == (0.4, 7)

    def test_group_8(self):
        assert assignment.assign_expense_coefficient("651010") == (0.78, 8)
        assert assignment.assign_expense_coefficient("720101") == (0.78, 8)
        assert assignment.assign_expense_coefficient("850000") == (0.78, 8)
        assert assignment.assign_expense_coefficient("880000") == (0.78, 8)

    def test_group_9(self):
        assert assignment.assign_expense_coefficient("011010") == (0.67, 9)
        assert assignment.assign_expense_coefficient("061010") == (0.67, 9)
        assert assignment.assign_expense_coefficient("201010") == (0.67, 9)
        assert assignment.assign_expense_coefficient("351010") == (0.67, 9)
        assert assignment.assign_expense_coefficient("371010") == (0.67, 9)
        assert assignment.assign_expense_coefficient("491010") == (0.67, 9)
        assert assignment.assign_expense_coefficient("999999") == (0.67, 9)

class TestTaxCalculator:
    def test_tax_calculator(self):
        assert calc_logic.tax_calculator(10000, 6, "72.10.10", 1000, 0) == 1020
        assert calc_logic.tax_calculator(10000, 6, "72.10.10", 1000, 20) == 1000
        assert calc_logic.tax_calculator(10000, 5, "72.10.10", 1000, 0) == 340
        assert calc_logic.tax_calculator(10000, 5, "72.10.10", 1000, 140) == 200