'''File: voyager.py
Author: Aspen Frazee
Date completed: 10/02/2022
Description: Calculate the distance traveled by the Voyager since 09/25/1997
in miles, kilometers, and Astronomical Units. Calculate and print the time it 
takes radio waves to make a round trip in meters per hour.
'''

num_days = int(input("Enter the desired number of days traveled after September 25, 1977: "))

distance_mi = 38_241 * num_days + 16_637_000_000  # These are the calculations required for the solution to be printed.
distance_km = distance_mi * 1.609344
distance_au = distance_mi / 92_955_887.6
distance_m = distance_km * 1_000

limit_km = round(distance_km, 3) #Limits the decimal points printed
limit_au = round(distance_au, 3) 

# radio waves 299_792_458 m/s * 60 * 60 = 1_079_252_850_000 m/h
radio_waves = 1_079_252_850_000 
round_trip_rw = distance_m * 2 / radio_waves

limit_round_trip = round(round_trip_rw, 3)

print("The distance is -\n"
    f"Miles: {distance_mi: ,}\n"  # the f"{} function adds commas to the numbers to make them more readable.
    f"Kilometers: {limit_km: ,}\n"
    f"Astronomical Units: {limit_au: ,}\n"
    f"It takes {limit_round_trip: ,}", "hours for radio waves to travel, round trip.")

'''
voyager.py

1) Using f-string, we can type this directly:

print(f"It takes {limit_round_trip: ,} hours for radio waves to travel, round trip.")'''