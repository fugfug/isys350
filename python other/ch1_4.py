# ch 1-4

''' #7
days = 4
salary_day = 1
salary = 0
for i in range(days):
    print("Salary for day ", i + 1, " ", 0.01 * salary_day)
    # Calculating total salary in dime
    salary += salary_day
    salary_day *= 2
print("The total salary is $", 0.01 * salary)
# https://www.slader.com/textbook/9780134444321-starting-out-with-python-4th-edition/204/programming-exercises/7/#
'''


''' p500 #13
starting_num = 2
avg_incr = .3
avg_incr2 = 30
days_multiply = 10
population = starting_num

print(1, population)
for day in range(1, days_multiply+1):
#    for p in range(1, days_multiply):
   # population += (avg_incr*population)
    population *= (1+avg_incr2/100)
    print(day, population)
# https://www.slader.com/textbook/9780134444321-starting-out-with-python-4th-edition/205/programming-exercises/13/#
'''

''' p501 #15
for r in range(6):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')
'''

''' p481, ch 4
for r in range(6):
    for c in range(r):
        print(' ', end='')
    print('#')
'''

'''
for x in range(8):
    for y in range(x+1):
        print('*', end='')
    print()
'''

''' p475, ch 4
for x in range(8):
    for y in range(6):
        print('*', end='')
    print('')
'''

''' p472, ch 4
num_students = int(input('how many students?: '))
num_scores_per_student = int(input('how many test scores per student?: '))


for student in range(num_students):
    print('student number', student+1)
    print('-----------------------')
    test_total_score = 0
    for test_num in range(num_scores_per_student):

        print("test number ", test_num+1, ': ', end='')
        test_score = float(input(''))
        test_total_score += test_score
    average = test_total_score / num_scores_per_student
    print('the avg for student number ', student+1, 'is: ', average, '\n\n')

'''

'''  p 465, ch 4
MARK_UP = 2.5
another = 'y'
while another == 'y' or another == 'Y':
    wholesale = float(input("enter wholesale: $"))
    while wholesale < 0:
        wholesale = float(input('no, again: '))
    retail = wholesale * MARK_UP
    print('Retail price: $', format(retail, ',.2f'), sep='')
    another = input('again? ')

'''

'''
lot = int(input("enter lot number, enter 0 to end: "))
while lot > 0:
    prop_value = int(input("enter property value: "))
    property_tax = prop_value * .0065
    print("property tax for lot", lot, " is ", property_tax)
    lot = int(input("enter lot number, enter 0 to end: "))

'''

'''
MAX = 130
MIN = 60
print("kph\t\tmph")
for kph in range(MIN, MAX+1, 10):
    mph = kph*.6214
    print(kph, "\t\t", format(mph,'.1f'))
'''


'''
for number in range(6):
    print(number)
# prints 
0 
1 
2 
3 
4 
5

'''