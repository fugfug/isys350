'''
Write a class named Person with data attributes for a person’s name, address, and
telephone number. Next, write a class named Customer that is a subclass of the Person
class.
The Customer class should have a data attribute for a customer number and a
Boolean data attribute indicating whether the customer wishes to be on a mailing list.
Demonstrate an instance of the Customer class in a simple program.
'''

class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone = phone_number

    # use accessor and mutator methods,
    # because the attributes in this class are private
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone_number):
        self.__phone = phone_number

class Customer(Person):
    def __init__(self, name, address, phone_number, cust_number, mail_list):
        Person.__init__(self, name, address, phone_number)
        self.__customer_number = cust_number
        self.__mailing_list = mail_list

    # use accessor and mutator methods,
    # because the attributes in this class are private
    def get_cust_num(self):
        return self.__customer_number
    def get_mailing_list(self):
        return self.__mailing_list

    def set_cust_num(self, new_num):
        self.__customer_number = new_num
    def set_mailing_list(self, mail_list):
        self.__mailing_list = mail_list


''''''
import person
def main():
    #p = person.Person('Firstname Lastname','111 1st St., SF, CA', '555-5555')
    c = person.Customer('Firstname Lastname','111 1st St., SF, CA', '555-5555', '123456', False)
   # print(c.get_address())

main()
