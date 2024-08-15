'''
CS160 Fall 2020 Final Project
Name: Aspen Frazee
Date: poo
'''
# 1
import random
# 2
yes_no = input("Do you want to go on an adventure? (Yes/No) ").lower().strip()
# hint: the program should convert player's input to lowercase
# and get rid of any space player enters
# hint: check out what .upper(), .lower(), .strip()
# do on a string, reference: https://www.w3schools.com/python/python_ref_string.asp
# 3
if yes_no == "yes":
    # hint: pay attention to the variable name
    # 4
    left_right= input("You are lost in the forest and the path splits."
                      "Do you go left or right? (Left/Right) ").lower().strip()
    if left_right == "left" or left_right == "Left" or left_right == "LEFT":
    # 5
        run_attack = input("An evil witch tries to cast a spell on you,"
                           "do you run or attack? (Run/Attack) ").lower().strip()
        if run_attack == "attack":
            print("She turned you into a green one-legged chicken, you lost!")
    # 6
        elif run_attack == "run":
            print("Wise choice, you made it away safely.")
            car_plane = input("You see a car and a plane."
                            "Which would you like to take? (Car/Plane) ").lower().strip()
            if car_plane == "plane":
                print("Unfortunately, there is no pilot. You are stuck!")
            elif car_plane == "car":
                print("You found your way home. Congrats, you won!")
            # 7
            else:
                print("You spent too much time deciding...")
        else:
            print("You are frozen and can't talk for 100 years...")
    elif left_right == "right":
        # hint: the program should randomly generate a
        # number in betwwen 1 and 3 (including 1 and 3)
        # hint: remember random module?
        # reference: https://www.w3schools.com/python/module_random.asp
    # 8
        num = random.randint(1,4)
    # 9
        number_input = input("Pick a number from 1 to 3: ")
    # hint: will the following if statment ever be executed
    # even when the values of answer and num are the same? If not, can you fix the problem?
    # hint: the error is not necessarily in the line below.
        if number_input == num:
            print(f"I'm also thinking about {num}")
            print("You woke up from this dream.")
        else:
            print("You fall into deep sand and get swallowed up. You lost!")
# 10
else:
    print("That's too bad!")
