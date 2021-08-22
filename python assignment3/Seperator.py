'''
3. Word Separator:
Write a program that accepts as input a sentence in which all of the words are run together
but the first character of each word is uppercase.
Convert the sentence to a string in which the words are separated by spaces
and only the first word starts with an uppercase letter.
For example, the string “StopAndSmellTheRoses.” would be converted to “Stop and smell the roses.”
'''
def main():
    string1 = input('Enter a sentence: ')
    string2 = string1[0]
            # initialize string2 with first char of string1,
            # so the first char will be left unchanged.

    for i in range(1, len(string1)):
        if string1[i].isupper():
            string2 += ' ' + string1[i].lower()
        else:
            string2 += string1[i]
    print(string2)
main()


#####################################

'''
for char in string:
    if char.isupper():
        str += ' ' + char
    else:
        str += char
print(str)
'''