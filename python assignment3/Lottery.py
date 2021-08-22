'''
1. Lottery Number Generator:
Design a program that generates a seven-digit lottery number.
The program should generate seven random numbers, each in the range of 0 through 9,
and assign each number to a list element.
(Random numbers were discussed in Chapter 6.)
Then write another loop that displays the contents of the list.
'''
def main():
    import random
    DIGITS = 7
    RAND_MIN = 0
    RAND_MAX = 9
    lottery_nums = list() # create an empty list

    # assigns each number to a list element
    for i in range(DIGITS):
        # generates 7 random numbers
        lottery_nums.insert(i, random.randint(RAND_MIN, RAND_MAX))

    #displays the contents of the list
    for element in range(len(lottery_nums)):
        print(lottery_nums[element], end=' ')

main()