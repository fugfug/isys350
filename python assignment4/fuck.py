import person
def main():
    c = person.Customer('Firstname Lastname','111 1st St., SF, CA',
                        '415-555-5555', '1234', False)
    print(c.get_cust_num())
main()

# end of inner try statement
# print(emp_dict.items())


# end of main, before pickle, after ifs
# delete this later ******************************************************************
# print('\n',emp_dict.items())

# for pickling testing
#       emp_file = open('employee.dat', 'rb')
#    emp_file = open('employee.dat','wb')


#change_emp:
# emp = employee.Employee(name, id, dept, job)
# employee_dictionary[id] = emp
#end of if:
# display - delete this later *****************************************************
# print(employee_dictionary[id])


# emp_file = open('employee_file.dat', 'rb')
'''
end_of_file = False
while not end_of_file:
    try:
        emp_dict = pickle.load(emp_file)
        print(emp_dict.items())
    except EOFError:
        end_of_file = True
emp_file.close()
'''

# emp_file = open('employee_file.dat','wb')


'''

#emp_dict[47899].__str__()

    #emp_dict = pickle.load(emp_file)
    #emp_dict = {emp1.get_id(): emp1}
    #print(emp_dict.items())




    def change
       # employee.Employee.set_name(name)
       # employee.Employee.set_dept(dept)
       # employee.Employee.set_job(job)



    #emps = pickle.load(emp_file)

    emp1 = employee.Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    emp2 = employee.Employee('Mark Jones', '39119', 'IT', 'Programmer')
    emp3 = employee.Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
    #emp_dict = {emp1.get_id(): emp1, emp2.get_id():emp2, emp3.get_id():emp3}





    print('what?: \n'
          '1. look up emp\n',
          '2. add new emp\n',
          '3. change entry\n',
          '4. remove emp\n',
          'anything else to quit program')
    what_do = int(input(''))

    if what_do == 1:
        look_up()
    elif what_do == 2:
        name = input('enter name: ')
        id_num= input('enter id ')
        department = input('enter dept: ')
        job_title = input('enter job ')
        add_new(name, id_num, department, job_title)
        emp_dict.update(id_num, add_new(name, id_num, department, job_title))
    elif what_do == 3:
        change()
    elif what_do == 4:
        remove_emp()

'''