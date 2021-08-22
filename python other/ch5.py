


''' p606 ch 5
def main():
    monthly_sales = get_sales()
    advanced_pay = get_ad_pay()
    commission = det_comm(monthly_sales)
    calc_pay(monthly_sales, advanced_pay, commission)
def get_sales():
    return float(input('sales: '))
def get_ad_pay():
    return float(input('advanced pay: '))
def det_comm(sales):
    if sales < 10000:
        commission = 10
    elif sales <= 14999 and sales >= 10000:
        commission = 12
    elif sales < 18000 and sales >= 15000:
        commission = 14
    elif sales <= 21999 and sales >= 18000:
        commission = 16
    else:
        commission = 18
    return commission/100
def calc_pay(sales, ad_pay, comm):
    pay = sales*comm - ad_pay
    print('pay: $', pay, sep='')
    if(pay < 0):
        print('reimburse')
main()
'''

''' p586
import random
HEADS = 1
TAILS = 2
TOSSES = 10
def main():
    for x in range(TOSSES):
        toss()
def toss():
    coin = random.randint(HEADS, TAILS)
    if coin == HEADS:
        print('heads')
    else:
        print('tails')
main()

'''


''' p546
def intro():
    print('explains what the program does')
def convert(cups):
    fl_oz = cups * 8
    print(fl_oz)
def main():
    intro()
    num_cups = float(input('number of cups: '))
    convert(num_cups)
main()
'''

'''
def main():
    value = 5
    show_double(value)
    print(value)

def show_double(number):
    result = number *2
    print(result)

main()
'''