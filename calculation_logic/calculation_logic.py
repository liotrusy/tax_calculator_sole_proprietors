import assignment_logic.assignment_logic as assignment

def assign_tax_percentage(years_of_activity):
    """Assigns tax percentage based on years of activity"""
    if years_of_activity <= 5:
        tax_percentage = 0.05
    else:
        tax_percentage = 0.15
    return tax_percentage

def calculate_gross_taxable_income(income, expense_coefficient):
    """Returns the gross taxable income"""
    gross_taxable_income = income * expense_coefficient
    return gross_taxable_income

def calculate_net_taxable_income(gross_taxable_income, paid_contributions):
    """Returns the next taxable income"""
    net_taxable_income = gross_taxable_income - paid_contributions
    return net_taxable_income

def calculate_net_tax(net_taxable_income, tax_percentage, tax_prepayment):
    """Returns both the gross tax and net tax"""
    gross_tax = round(net_taxable_income * tax_percentage, 2)
    net_tax = gross_tax - tax_prepayment
    return net_tax

def tax_calculator(income, years_of_activity, activity_code, paid_contributions, tax_prepayment):
    """Returns the tax amount to be paid"""
    tax_percentage = assign_tax_percentage(years_of_activity)
    ateco_code_clean = assignment.clean_input(activity_code)
    expense_coefficient = assignment.assign_expense_coefficient(ateco_code_clean)[0]

    gross_taxable_income = calculate_gross_taxable_income(income, expense_coefficient)
    net_taxable_income = calculate_net_taxable_income(gross_taxable_income, paid_contributions)

    tax_to_be_paid = calculate_net_tax(net_taxable_income, tax_percentage, tax_prepayment) 

    return tax_to_be_paid