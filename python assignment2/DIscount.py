'''
A software company sells a package that retails for $99.
Quantity discounts are given according to the following table:
Quantity Discount
10–19 20%
20–49 30%
50–99 40%
100 or more 50%
Write a program that asks the user to enter the number of packages purchased. The
program should then display the amount of the discount (if any) and the total
amount of the purchase after the discount.
'''
def main():
    RETAIL_PRICE = 99
    purchased = int(input('enter number purchased: '))
    price = purchased * RETAIL_PRICE

    discount = determine_discount(purchased)
    total = calculate_discount(price, discount)
    print('Discount: ', discount, '%',
          '\nTotal price after discount: $', format(total, ',.2f'), sep='')

def determine_discount(num_purchased):
    # each constant variable represents
    # the discount for that amount purchased
    DISCOUNT_10_TO_19 = 20
    DISCOUNT_20_TO_49 = 30
    DISCOUNT_50_TO_99 = 40
    DISCOUNT_OVER_100 = 50
    if num_purchased >= 10 and num_purchased <= 19:
        discount = DISCOUNT_10_TO_19
    elif num_purchased >= 20 and num_purchased <= 49:
        discount = DISCOUNT_20_TO_49
    elif num_purchased >= 50 and num_purchased <= 99:
        discount = DISCOUNT_50_TO_99
    elif num_purchased >= 100:
        discount = DISCOUNT_OVER_100
    else:   # no discount for less than 10 purchased
        discount = 0
    return discount

def calculate_discount(total, discount):
    discount /= 100
    return total - (total * discount)

main()
