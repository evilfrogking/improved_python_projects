'''
bmi_2.py
Aspen Frazee
10/9/2022
Places the user's BMI into its weight status.
'''
import bmi_1    # imports bmi_1.py


if bmi_1.limit_bmi <= 18.5:   
    print("Your weight status is Underweight.")
elif 18.5 <= bmi_1.limit_bmi <= 24.9:
    print("Your weight status is Normal.")
elif 25.0 <= bmi_1.limit_bmi <=29.9:
    print("Your weight status is Overweight.")
else:
    print("Your weight status is Obese.")
