'''
The colors red, blue, and yellow are known as the primary colors because they
cannot be made by mixing other colors. When you mix two primary colors, you get
a secondary color, as shown here:
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.
Design a program that prompts the user to enter the names of two primary colors to
mix. If the user enters anything other than “red,” “blue,” or “yellow,” the program
should display an error message. Otherwise, the program should display the name
of the secondary color that results.
'''

def main():
    c1 = input('Enter color 1: ')
    c2 = input('Enter color 2: ')

    # used a list to quickly determine if inputs are valid
    colors_list = ['red', 'blue', 'yellow']

    # if inputs are not valid,
    # keep asking user to input colors until both inputs are valid.
    while c1 not in colors_list or c2 not in colors_list:
        print('\nError. Enter red, blue, or yellow.')
        c1 = input('Enter color 1: ')
        c2 = input('Enter color 2: ')
    # if both inputs are valid, determine the resulting color.
    color_result = determine_color(c1, c2)
    print(c1, ' + ', c2, ' = ', color_result)

# function determines the color that results from the user's inputs
def determine_color(color1, color2):
    if color1 == 'red' and color2 == 'blue' or color1 == 'blue' and color2 == 'red':
        return 'purple'
    elif color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
        return 'orange'
    elif color1 == 'blue' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'blue':
        return 'green'

main()


