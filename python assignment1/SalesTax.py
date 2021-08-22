'''

1. Sales Tax
Write a program that will ask the user to enter the amount of a purchase.
The program should then compute the state and county sales tax.
Assume the state tax is 8 percent and county tax is 3.5 percent.
The program should display the amount of the purchase, the state sales tax
and the county sales tax, total sales tax, and the total of the sale
(which is the sum of the amount purchase plus total sales tax).

'''

STATE_TAX_RATE = .08    # 8% state tax rate
COUNTY_TAX_RATE = .035  # 3.5% county tax rate
amt_purchase = float(input("Enter the amount of a purchase: $"))

state_tax = amt_purchase * STATE_TAX_RATE   #calculate state tax
county_tax = amt_purchase * COUNTY_TAX_RATE
total_tax = state_tax + county_tax      # calculate total tax
total_sale = total_tax + amt_purchase

print("Amount of purchase: $", format(amt_purchase, ',.2f'), sep='')
print("State sales tax: $", format(state_tax, '.2f'), sep='')
print("County sales tax: $", format(county_tax, '.2f'), sep='')
print("Total sales tax: $", format(total_tax, '.2f'), sep='')
print("Total sales: $", format(total_sale, '.2f'), sep='')

