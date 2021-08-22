import turtle

NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATIONS_SPEED = 0

turtle.speed(ANIMATIONS_SPEED)

for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)
turtle.done()

'''
MAX = 5
total = 0.0

print("calculates sum of", MAX, 'numbers you will enter')
for counter in range(MAX):
    number = int(input('enter number: '))
    total += number
print('the total is', total)


#

print('number\tsquare')
print("-------------------")
for number in range(1,11):
    square = number**2
    print(number,'\t\t',square)
'''

#for x in range(5):
#    print(x, ' Hell') ################# <---------------

#for num in [1,2,3,4,5]:
#    print(num)

#for name in ['a','b','c','d']:
#    print(name)


'''
keep_going = 'y'
while keep_going == 'y':
    sales = float(input("enter amount of sales: "))
    comm_rate = float(input("enter commission rate: "))

    commission = sales * comm_rate
    print("the commission is $" + format(commission, '.2f'))

    keep_going = input("do you want to calculate another 'commission'? enter y for yes: ")

####

BASE_HOURS = 40
OT_MULTIPLIER = 1.5

hours = float(input("enter # hours worked: "))
pay_rate = float(input("enter hrly pay rate: "))

if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER
    gross_pay = BASE_HOURS * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate
# print("gross pay is $" + gross_pay)     #error
# print("gross pay is $", gross_pay)    #should be this
print("gross pay is $" + format(gross_pay, '.2f'))
'''


