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
class Employee:
    def __init__(self, name, id_num, department, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

    # use accessor methods to return attributes,
    # because the attributes in this class are private
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id_num
    def get_dept(self):
        return self.__department
    def get_job(self):
        return self.__job_title

    # mutator methods
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id_num = id
    def set_dept(self, dept):
        self.__department = dept
    def set_job(self, job):
        self.__job_title = job

    def __str__(self):
        return self.get_id() + \
            '\t' + self.get_name() + \
            '\t' + self.get_dept() + \
            '\t' + self.get_job()