'''
A nutritionist who works for a fitness club helps members by evaluating their diets.
As part of her evaluation, she asks members for
the number of fat grams and carbohydrate grams that they consumed in a day.
Then, she calculates the number of calories that result from the fat,
using the following formula:
calories from fat fat grams * 9
Next, she calculates the number of calories that result from the carbohydrates,
using the following formula:
calories from carbs carb grams * 4
The nutritionist asks you to write a program that will make these calculations
'''

# function calculates the calories from fat and the calories from carbs.
# the parameters are the user's inputs
def calculate(fat, carbs):
    # returns both calories from fat and calories from carbs
    return fat * 9, carbs * 4

def main():
    fat_grams = float(input('Enter number of fat grams consumed in a day: '))
    carbs_grams = float(input('Enter number of carbohydrate grams consumed in a day: '))

    # call calculate function to get calories from fat and calories from carbs
    cal_from_fat, cal_from_carbs = calculate(fat_grams, carbs_grams)
    print('Calories from fat is', format(cal_from_fat, '.2f'), 'grams.')
    print('Calories from carbohydrates is', format(cal_from_carbs, '.2f'), 'grams.')

main()