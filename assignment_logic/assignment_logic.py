def clean_input(input_ateco_code):
    """ Clean the input provided by the user """
    ateco_code = input_ateco_code.replace(".", "")
    if len(ateco_code) <= 6:
        return ateco_code
    else:
        return -1

def assign_expense_coefficient(ateco_code):
    """ Assign expense coefficient based on ateco code """
    ateco_class = ateco_code[:4]
    ateco_group = int(ateco_code[:3])
    ateco_division = int(ateco_code[:2])

    # class assignment
    if ateco_class == "4781":
        expense_coefficient = 0.4
        group = 3

    elif ateco_class == "4782" or ateco_class == "4789":
        expense_coefficient = 0.4
        group = 4
    
    # group assignment
    elif ateco_group == 461:
        expense_coefficient = 0.62
        group = 6

    elif \
    (ateco_group >= 462 and ateco_group <= 469) or  \
    (ateco_group >= 471 and ateco_group <= 477) or  \
    (ateco_group == 479) or \
    ateco_division == 45:

        expense_coefficient = 0.4
        group = 2

    # division assignment

    elif ateco_division == 10 or ateco_division == 11:
        expense_coefficient = 0.4
        group = 1

    elif (ateco_division >= 41 and ateco_division <= 43) or ateco_division == 68:
        expense_coefficient = 0.86
        group = 5

    elif ateco_division == 55 or ateco_division == 56:
        expense_coefficient = 0.4
        group = 7

    elif \
    (ateco_division >= 64 and ateco_division <= 66) or \
    (ateco_division >= 69 and ateco_division <= 75) or \
    (ateco_division >= 85 and ateco_division <= 88):
        
        expense_coefficient = 0.78
        group = 8

    else:
        expense_coefficient = 0.67
        group = 9
  
    return (expense_coefficient, group)
 

