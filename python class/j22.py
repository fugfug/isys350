

myset = set(['1', '2', '3'])
myset1 = set(['3','5','6'])

myset2 = myset.symmetric_difference(myset1)
print(myset2)

#for val in myset:
 #   print(val)

#myset = set()
#myset.add(1)
#myset.add(2)
#myset.add(3)
#print(myset)

# create a dictionary, length of dictionary, print keys
# print value of a key, update a value, clear
'''
phonebook = {'chris':'555-111',
              'katie': '555-222', 'joanne':'555-333'}
print('length: ',len(phonebook))
print(phonebook.keys())
print('katie:',phonebook['katie'])

phonebook['chris'] = '555-444'
print(phonebook)
phonebook.clear()
print(phonebook)
'''

# ch 8
# string delimiter
'''
def main():
    date_string = '11/26/2021'
    date_list = date_string.split('/')
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])
main()
'''

# find in a string
'''
text = 'John Green Don is 26 years old'
if 'Don' in text:
    print('string \'don\' found in text')
else:
    print('no')
'''

# slice a string
'''
fullname = 'mother fucking shit'
middlename = fullname[7:15]
print(middlename)
'''

# string concat
'''
message = 'fick'
message2 = 'dich'
twomessages = message + ' ' + message2
print(twomessages)
print(message[3])
'''

# chars in a string
'''
def main():
    count = 0
    my_string = input('enter a sentence ')
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count +=1
    print('letter t appears', count, 'times')
main()
'''