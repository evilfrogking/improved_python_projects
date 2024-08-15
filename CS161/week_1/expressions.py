'''File: expressions.py
Author: Aspen Frazee
Date Completed: 10/02/2022
Description: Prints the results of the equations expressed by x and y
'''

x = (2**4+7-3*4)/5 # Float function ensures the decimal is not dropped
y = ((1+3**2)*(16%7))/7
limited_y = round(y, 3) # This rounds up the results to the 3rd decimal place

print("x = (2^4+7-3*4)/5", "y = ((1+3^2)*(16mod7))/5", sep = '\n')

print("x = ", x, "and y = ", limited_y) 

'''expression.py

1) Don't need to cast the type here. 

/ division, and // is integer division (this is the one that will drop the fractional part)
'''