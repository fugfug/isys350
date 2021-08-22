'''
4. Employee Class:
Write a class named Employee that holds the following data about an employee in attributes:
name, ID number, department, and job title.
Once you have written the class,
write a program that creates three Employee objects to hold the following data:
Name            ID Number   Department      Job Title
Susan Meyers    47899       Accounting      Vice President
Mark Jones      39119       IT              Programmer
Joy Rogers      81774       Manufacturing   Engineer
The program should store this data the three objects,
then display the data for each employee on the screen.
'''
import employee
def main():
    # creates three Employee objects
    emp1 = employee.Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    emp2 = employee.Employee('Mark Jones', '39119', 'IT', 'Programmer')
    emp3 = employee.Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    # display the data for each employee
    print('Name\t\t\t ID\t\t\t Department\t\t Job Title')
    print(emp1.get_name(), '\t', emp1.get_id(), '\t\t',
          emp1.get_dept(), '\t',emp1.get_job())
    print(emp2.get_name(), '\t\t', emp2.get_id(), '\t\t',
          emp2.get_dept(), '\t\t\t', emp2.get_job())
    print(emp3.get_name(), '\t\t', emp3.get_id(), '\t\t',
          emp3.get_dept(), '\t', emp3.get_job())

main()


