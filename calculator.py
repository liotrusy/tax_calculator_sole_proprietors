import calculation_logic.calculation_logic as logic
import decimal as dm

def convert_to_num(a_string):
    """Function to convert string to input. If user provide a non convertible string returns empty"""
    try:
        number = dm.Decimal(a_string)
        return number
    except:
        return ""

def capture_inputs():
    """ This function captures the key information for the tax calculation"""
    calculation_inputs = {}

    print("How much income have you generated (register the one that have been paid)?")
    calculation_inputs['income'] = convert_to_num(input(">> "))

    print("Since how many years have you operated your sole proprietorship?")
    calculation_inputs['years_of_activity'] = convert_to_num(input(">> "))
    print("What is your activity code? Use the notation xx.xx.xx (for example 78.10.20)")
    calculation_inputs['activity_code'] = input(">> ")
    print("How much contributions have you paid this year?")
    calculation_inputs['paid_contributions'] = convert_to_num(input(">> "))
    print("How much is your tax prepayment?")
    calculation_inputs['tax_prepayment'] = convert_to_num(input(">> "))


    return calculation_inputs


inputs = capture_inputs()
while "" in inputs.values():
    print("We cannot calculate your taxes without all the right info")
    print("Let's start from the top :)")
    inputs = capture_inputs()

tax_to_be_paid = logic.tax_calculator(inputs['income'], \
    inputs['years_of_activity'], \
    inputs['activity_code'], \
    inputs['paid_contributions'], \
    inputs['tax_prepayment'])

print("------------ YOUR RESULT ------------------")
print(f"Great, The taxes you have to pay are {tax_to_be_paid}")
print("Thank you for using our service!")
