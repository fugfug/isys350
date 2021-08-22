'''
Create a program that stores Employee objects in a dictionary.
Use the employee ID number as the key.
The program should present a menu that lets the user perform the following actions:
• Look up an employee in the dictionary
• Add a new employee to the dictionary
• Change an existing employee’s name, department, and job title in the dictionary
• Delete an employee from the dictionary
• Quit the program
When the program ends, it should pickle the dictionary and save it to a file.
Each time the program starts, it should try to load the pickled dictionary from the file.
If the file does not exist, the program should start with an empty dictionary
'''

import employee
import pickle

def look_up(employee_dictionary):
    id = input('\nWhat employee do you want to look up? '+
               '\nEnter their ID: ')
    if id in employee_dictionary:
        return print(employee_dictionary[id])
    else:
        print('Employee not found.')

def add_new(employee_dictionary):
    name = input('\nEnter employee\'s name: ')
    id = input('Enter employee\'s ID: ')
    dept = input('Enter employee\'s department: ')
    job = input('Enter employee\'s job title: ')

    # create new employee object &
    # add object to the dictionary as the value of the key
    employee_dictionary[id] = employee.Employee(name, id, dept, job)

def change_employee(employee_dictionary):
    id = input('\nWhich employee do you want to change? '
               + '\nEnter their ID: ')

    if id in employee_dictionary:
        name = input('Enter employee\'s name: ')
        dept = input('Enter employee\'s department: ')
        job = input('Enter employee\'s job title: ')

        # use mutator methods from the Employee class
        # to change the object's attributes
        value = employee_dictionary[id]
        value.set_name(name)
        value.set_dept(dept)
        value.set_job(job)
    else:
        print('Employee not found.')

def remove_emp(employee_dictionary):
    id = input('\nWhich employee do you want to remove? '
               + '\nEnter their ID: ')
    if id in employee_dictionary:
        del employee_dictionary[id]
    else:
        print('Employee not found.')


def main():

    # while loop for loading each object from file
    # try to load the pickled dictionary from the file
    try:
        emp_file = open('employee_file.dat', 'rb')
        end_of_file = False
        while not end_of_file:
            try:
                emp_dict = pickle.load(emp_file)
            except EOFError:
                end_of_file = True
        emp_file.close()

    # If the file does not exist, program starts with an empty dictionary
    except FileNotFoundError:
        emp_dict = {}

    # menu choice constants
    LOOK_UP_EMPLOYEE = 1
    ADD_NEW_EMPLOYEE = 2
    CHANGE_EMPLOYEE = 3
    REMOVE_EMPLOYEE = 4

    # menu
    print('What do you want to do? \n'+
          'Press: \n'+
          '1 to Look up an employee\n' +
          '2 to Add a new employee\n'+
          '3 to Change an employee entry\n'+
          '4 to Remove an employee\n'+
          'Enter any other number to quit program.')

    try:
        action = int(input(''))
    except ValueError:  # in case a letter is entered
        action = int(input('Enter a number: '))

    if action == LOOK_UP_EMPLOYEE:
        look_up(emp_dict)
    elif action == ADD_NEW_EMPLOYEE:
        add_new(emp_dict)
    elif action == CHANGE_EMPLOYEE:
        change_employee(emp_dict)
    elif action == REMOVE_EMPLOYEE:
        remove_emp(emp_dict)

    # pickle dictionary
    emp_file = open('employee_file.dat', 'wb')
    pickle.dump(emp_dict,emp_file)
    emp_file.close()

main()


