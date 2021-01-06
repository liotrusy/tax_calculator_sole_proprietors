# Tax Calculator For Sole Proprietors (PIVA Forfettaria)

The goal of the project is to create a tax calculator for sole proprietors in Italy. The final outcome is to return a value that helps users set aside the necessary funds for tax liquidations. The value may be accompanied by some other information.

This first version will be locally on a Windows Machine with a python 3.9 installation.

I designed the calculator with as much modularity as possibile in order to account for potential regulatory changes and calculation procedures. Furthermore, for the same reason, I separated the calcualtion logic from the calculator app.

## Calculation logic

What are the main drivers of the calculation?

1. income (on cash basis)
2. taxable income determined by the progressive code
3. tax percentage determined by the years of activity

### 1. Income

The income


### 2. Taxable income

The gross taxable income is calculated from the income based on two variables:

1. the activity code
2. the contributions paid in the current year

The gross taxable income is calculated by deducting a fixed amount of expenses based on the activity code. This is done using the expense coefficient.
The net taxable income is calculated by subtracting the contributions paid in the current year from the gross taxable income.

### 3. Tax percentage

Tax percentage has two scenarios depending on the years of activity of the sole proprietor.

1. less or equal than 5 years.
2. more than 5 years.

## Main components

* Input and output module
* gross taxable income calculator
* expense coefficient selector
* tax percentage selector
* tax calculator
* contributions 