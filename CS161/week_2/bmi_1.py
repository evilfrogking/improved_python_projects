'''
bmi_1.py
Aspen Frazee
10/9/2022
Calculates the user's BMI.
'''

body_weight = int(input("Enter your weight in pounds: "))
body_height = int(input("Enter your height in inches: "))

weight_kg = body_weight * 0.45359237 # converts lbs to kg
height_meters = body_height * 0.0254 # converts inches to meters

bmi = weight_kg / height_meters ** 2 # calculates bmi

limit_bmi = round(bmi, 1) # limits the decimals printed to the tenths place

print("Your BMI is", limit_bmi)