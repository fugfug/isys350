
#try exceptions

def main():
    try:
        hours = int(input('how many hrs worked?'))
        pay_rate = int(input('hrly rate:'))
        gross_pay = pay_rate * hours
        print('gross pay: $', format(gross_pay, '.2f'))
    except ValueError:
        print('ERROR: hours worked and hrly rate must be a valid number')

main()




# files
'''
def main():
    infile = open('nameText.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    infile.close()

    print(line1)
    print(line2)
    print(line3)
    print(line4)

main()
'''

'''
def main():
    outfile = open('nameText.txt', 'a')

    outfile.write('jo locke\n')
    outfile.write('da hume\n')

    outfile.close()

main()
'''

'''
import math
def main():
    number = float(input('enter a number:'))
    square_root = math.sqrt(number)
    print('the square root of', number, ' is ', format(square_root, '.2f'))
main()
'''


#functions
'''
def main():
    first_age = int(input('enter age: '))
    second_age = int(input('enter the second age: '))
    total = sum(first_age, second_age)
    print('together, you are', total, 'years old')

def sum(first, second):
    return first+second

main()
'''

'''
CONTRIBUTION = .05
def main():
    gross_pay = float(input('enter gross pay: '))
    bonus = float(input('enter bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION
    print('contribution for gross pay: $', format(contrib, '.2f'), sep='')
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION
    print('contribution for bonuses: $', format(contrib, '.2f'), sep='')
main()
'''

'''
def main():
    value = 5
    show_double(value)
    print(value)

def show_double(number):
    result = number * 2
    print(result)

main()
'''

'''
def main():
    texas()
    california()

def texas():
    birds = 5000
    print('texas has', birds, 'birds')

def california():
    birds = 8000
    print('california has', birds, 'birds')

main()

'''

'''
def main():
    print('main function')
    message()

def message():
    print('message function')

main()

'''