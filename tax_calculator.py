def assign_tax_percentage(years_of_activity):
    """Assigns tax percentage based on years of activity"""
    if years_of_activity <= 5:
        tax_percentage = 0.05
    else:
        tax_percentage = 0.15
    return tax_percentage

def calculate_gross_taxable_income(income, expense_coefficient):
    gross_taxable_income = income * expense_coefficient
    return gross_taxable_income

def calculate_tax(gross_taxable_income, tax_percentage, paid_contributions):
    net_taxable_income = gross_taxable_income - paid_contributions
    tax_to_be_paid = round(net_taxable_income * tax_percentage, 2)
    return tax_to_be_paid