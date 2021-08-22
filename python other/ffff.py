'''
1043
1079
'''

#ch 9 p 1043
def main():


    birthdays = {}
    name = input('enter a name: ')
    bday = input('enter b day: ')





# ch 9 p 1037
# tldr

# ch 8 p 976 - password
'''
def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password) >= 7:
        correct_length = True
        for char in password:
            if char.isupper():
                has_uppercase = True
            if char.islower():
                has_lowercase = True
            if char.isdigit():
                has_digit = True
    if correct_length and has_digit and has_lowercase and has_uppercase:
        return True
    else:
        return False
def main():
    print(valid_password('sdjdFkj9sdfkjfds'))
main()
'''


# ch 8 p 957 - student login; wrong, works
''' 
def main():
    id_number = 'ENG6721'
    first = first_three_chars('Amanda')
    last = first_three_chars('Spencer')
    last_three_id = last_three(id_number)
    print(first + last + last_three_id)

def first_three_chars(name):
    if len(name) >= 3:
        return name[0:3]
    else:
        return name

def last_three(id):
    if len(id) >= 3:
        return id[-3:]
    else:
        return id

main()

'''



'''
string = 'asd?fadf*adf'
strin = ''
for char in string:
    if char.isalnum():
        strin += char
    else:
        print(char)
print(strin)

for char in range(len(string)):
    if not string[char].isalnum():
        print(char)
'''