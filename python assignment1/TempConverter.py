'''

Write a program that converts Celsius temperatures to Fahrenheit temperatures.
The formula is as follows:
F = (9/5)*C +32
The program should ask the user to enter a temperature in Celsius,
then display the temperature converted to Fahrenheit.

'''

celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = ((9/5) * celsius) + 32

print(celsius, 'degrees Celsius is', format(fahrenheit,'.2f'), 'Fahrenheit.')