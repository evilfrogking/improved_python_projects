'''
perfect_square.py
Aspen Frazee
10/9/2022
Determines if a number is a perfect square.
If not, it will prompt the user for a new number.
'''
import math

number = int(input("Enter a number to determine if it's a perfect square: "))


while math.sqrt(number) % 1 != 0:
    print(number, "is not a perfect square.")
    number = int(input("Enter a new number: "))
else:
    print(number, "is a perfect square!!!")

