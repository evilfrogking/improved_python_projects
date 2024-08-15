'''
1) Gradanator
2) Aspen Frazee
3) 10/17/2022
4) User inputs their grades from the term and the programs
calculates their progrected final grade.
'''

print("This program reads exam/homework scores \n"
"and reports your overall course grade.")


def main():
    exam_one = exam("Exam 1: ")
    exam_two = exam("Exam 2: ")
    exam_three = exam("Final: ")
    
    print("Homework:")
    homework_score = homework()
    
    course_grade(exam_one, exam_two, exam_three, homework_score)


def exam(exam_name: str):
    print(f"\n{exam_name} ")
    
    while True:
        weight = int(input("Weight (0-100)? "))
        if weight >= 0 and weight <= 100:
            break
    
    score = int(input("Score earned? "))
    score = min(score, 100)
    
    weighted_score = float(score / 100 * weight)
    
    print(f"Total points = {score} / 100 \n"
    f"Weighted Score: {weighted_score: .1f} \n")

    return round(weighted_score, 1)


def homework():
    while True:
         weight = int(input("Weight (0-100)? "))
         if weight >= 0 and weight <= 100:
            break
    
    assignments_num = int(input("Number of assignments? "))
    
    assignment_score = 0 # starting point for the assignment_score counter
    assignment_max = 0   # starting point for the assignment_max counter
    sections_max = 34

    for i in range(1, assignments_num+1):
        assignment_score += int(input(f"Assignment {i} score? "))
        assignment_max += int(input(f"Assignment {i} max points? "))
    
    sections = int(input("How many sections did you attend? ")) * 3
    sections = min(sections, 34)

    weighted_score_hw = float(((assignment_score + sections) / (assignment_max + sections_max))) * weight
    
    print(f"Section points = {sections} / 34 \n"
    f"Total points = {assignment_score + sections} / {assignment_max + sections_max} \n"
    f"Weighted Score: = {weighted_score_hw: .1f} \n")

    return round(weighted_score_hw, 1)


def course_grade(exam_one, exam_two, exam_three, homework_score):
    course_grade = float(exam_one + exam_two + exam_three + homework_score)
    
    if course_grade >= 90:
        letter = "A \nA is for Awesome!! Be proud!"
    elif 80 <= course_grade <= 89.99:
        letter = "B \nB is for Brilliant! Way to go!"
    elif 70 <= course_grade <= 79.99:
        letter = "C \nC is for Capable. You got the job done!"
    elif 60 <= course_grade <=69.99:
        letter = "D \nD is for Decent! You got this!"
    else:
        letter = "F \nHey, it's okay! We can try again together!"
    
    print(f"Overall percentage = {round(course_grade, 1)} \n"
    f"Your grade wil be at least: {letter}")


if __name__ == "__main__":
    main()