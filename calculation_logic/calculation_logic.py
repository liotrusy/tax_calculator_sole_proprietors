import assignment_logic.assignment_logic as assignment
import decimal as dm

def assign_tax_percentage(years_of_activity:int):
    """Return tax percentage based on years of activity"""
    if years_of_activity <= 5:
        tax_percentage = dm.Decimal(0.05)
    else:
        tax_percentage = dm.Decimal(0.15)
    return tax_percentage

def calculate_gross_taxable_income(income:float, expense_coefficient: dm.Decimal):
    """Returns the gross taxable income"""
    gross_taxable_income = income * expense_coefficient
    return gross_taxable_income

def calculate_net_taxable_income(gross_taxable_income:float, paid_contributions:float):
    """Returns the next taxable income"""
    net_taxable_income = gross_taxable_income - paid_contributions
    return net_taxable_income

def calculate_net_tax(net_taxable_income:float, tax_percentage:dm.Decimal, tax_prepayment:float):
    """Returns both the gross tax and net tax"""
    gross_tax = round(net_taxable_income * tax_percentage, 2)
    net_tax = gross_tax - tax_prepayment
    return net_tax

def tax_calculator(income:float, years_of_activity:int, activity_code:str, paid_contributions:float, tax_prepayment:float):
    """Returns the tax amount to be paid"""
    tax_percentage = assign_tax_percentage(years_of_activity)
    ateco_code_clean = assignment.clean_input(activity_code)
    expense_coefficient = assignment.assign_expense_coefficient(ateco_code_clean)[0]

    gross_taxable_income = calculate_gross_taxable_income(income, expense_coefficient)
    net_taxable_income = calculate_net_taxable_income(gross_taxable_income, paid_contributions)

    tax_to_be_paid = calculate_net_tax(net_taxable_income, tax_percentage, tax_prepayment) 

    return tax_to_be_paid