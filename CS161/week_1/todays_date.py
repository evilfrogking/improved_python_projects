'''File: todays_date.py
Author: Aspen Frazee
Date completed: 10/02/2022
Description: Find a module that prints todays date along with my name.
'''
# Found this code on GeeksforGeeks.org
from datetime import date

todays_date = date.today()

name = "Aspen Frazee"

print("Name: ", name)
print("Today's date is: ", todays_date)