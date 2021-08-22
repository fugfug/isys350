'''
A painting company has determined that for every 115 square feet of wall space,
one gallon of paint and eight hours of labor will be required.
The company charges $20.00 per hour for labor.
Write a program that asks the user to
enter the square feet of wall space to be painted and
the price of the paint per gallon.

The program should display the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
'''
DEFAULT_SQFT = 115   # for every 115 square feet of wall space,
GALLON_PAINT = 1     # one gallon of paint ...
HRS_LABOR = 8        # ... and eight hours of labor will be required.
RT_PER_HR_LABOR = 20 # charges $20.00 per hour for labor

def main():
    sqft = float(input('Enter the square feet of wall space to be painted: '))
    paint_price = float(input('Enter the price of the paint per gallon: $'))
    gallons, labor_hrs, cost_of_paint, \
    labor_charges, total_cost = calculations(sqft, paint_price)

    print('\nNumber of gallons of paint required: ', format(gallons, '.1f'),
    '\nHours of labor required: ', format(labor_hrs, '.1f'),
    '\nCost of the paint: $', format(cost_of_paint, ',.2f'),
    '\nLabor charges: $', format(labor_charges,',.2f'),
    '\nTotal cost of the paint job: $', format(total_cost, ',.2f'), sep='')
def calculations(sqft, paint_price):
    gallons = sqft / DEFAULT_SQFT
    labor_hrs = (HRS_LABOR * sqft) / DEFAULT_SQFT
    cost_of_paint = gallons * paint_price
    labor_charges = labor_hrs * RT_PER_HR_LABOR
    total = cost_of_paint + labor_charges
    # return multiple values
    return gallons, labor_hrs, cost_of_paint, labor_charges, total
main()