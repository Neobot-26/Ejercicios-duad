grade_counter=1
approved_grades_counter=0
desapproved_grades_counter=0
approved_grades_average=0
desapproved_grades_average=0
total_grades_average=0
grade_quantity = int(input("Enter Quantity of Grades :"))
while grade_counter<=grade_quantity:
    current_grade=int(input(f"Enter Student grade #{grade_counter}:"))
    if current_grade < 70:
        desapproved_grades_counter += 1
        desapproved_grades_average = desapproved_grades_average + current_grade
    else:
        approved_grades_counter += 1
        approved_grades_average = approved_grades_average + current_grade
    total_grades_average = total_grades_average + (current_grade//grade_quantity)
    grade_counter += 1
if desapproved_grades_counter!=0:
    desapproved_grades_average = (desapproved_grades_average // desapproved_grades_counter)
    print(f"The Student got an average of {desapproved_grades_average}% desapproved grades")
else:
    print("The Student got an average of 0% desapproved grades")
if approved_grades_counter!=0:
    approved_grades_average = (approved_grades_average // approved_grades_counter)
    print(f"The Student got an average of {approved_grades_average}% approved grades")
else:
    print("The Student got an average of 0% approved grades")
print(f"The Student got {approved_grades_counter} approved grades")
print(f"The Student got {desapproved_grades_counter} desapproved grades")
print(f"The Student got a grade total average of {total_grades_average}%")