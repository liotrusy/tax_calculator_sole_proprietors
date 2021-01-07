# Tax Calculator For Sole Proprietors (PIVA Forfettaria)

The goal of the project is to create a tax calculator for sole proprietors in Italy. The final outcome is to return a value that helps users set aside the necessary funds for tax liquidations. The value may be accompanied by some other information.

This first version is designed to run on a local machine with a python 3.9 installation.

I designed the calculator with as much modularity as possibile in order to account for potential regulatory changes and calculation procedures. Furthermore, for the same reason, I separated the expense coefficient assignment, tax calculation logic and calculator app.

## Main components

1. calculator.py (main application)
2. calculation_logic module (contains the logic for the numerical elaboration)
3. assignment_logic module (selects the expense coefficient given an activity code)
4. tes_components.py (testing suite and cases for the components above, test runner pytest)

To run the application on your machine download the first three components.

NOTES:
* In this application, I've used the decimal data type. That's because, due to the financial nature of the app, it needed a higher level of precision.
* Since values should not exceed 65,000 (the income limit imposed by law on forfait sole proprietors) the decimal data type will not significantly impede execution or performance.

## Calculation logic

What are the main drivers of the calculation.

1. income (on cash basis)
2. expense coefficient assigned on based on the activity code - [ATECO code](https://www.codiceateco.it/codice-ateco)
3. tax percentage determined by the years of activity

### 1. Income

The income is calcualted on a cash basis, not with accruals.


### 2. Expense coefficient

One of the most important components of the calculator is the expense coefficient selector. That's because the coefficient is the one of the key variable used to calculate the gross taxable income.

[Here is the link to the table](https://www.agenziaentrate.gov.it/portale/documents/20143/241208/allegato%2B4.pdf/d69be7fc-b18a-3c73-bd2e-b0f3c1970218) regarding the expense coefficient issued by  the Italian Tax Authorities (AdE).

### 3. Tax percentage

Tax percentage has two scenarios depending on the years of activity of the sole proprietor.

1. less or equal than 5 years.
2. more than 5 years.