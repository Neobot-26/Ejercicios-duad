import actions

def menu_options():
    file_path='students_register.csv'
    list_of_headers=["name","classroom","score_spanish","score_english","score_history","score_science","average"]
    while True:
        try:
            print("1. Register a new Student")
            print("2. Delete student from Register")
            print("3. See list of students who failed")
            print("4. See Information for all students")
            print("5. See Top 3 students")
            print("6. See average score per student")
            print("7. Exit")
            option_selected=int(input("Select option:"))
            if option_selected==1:
                print("Register a new Student")
                actions.student_register(file_path,list_of_headers)
            elif option_selected==2:
                print("Delete student from Register")
                actions.student_delete(file_path,list_of_headers)
            elif option_selected==3:
                print("See list of students who failed")
                actions.students_under_sixty(file_path)
            elif option_selected==4:
                print("See Information for all students")
                actions.student_read(file_path)
            elif option_selected==5:
                print("See Top 3 students")
                actions.student_top_three_average(file_path)
            elif option_selected==6:
                print("See average score per student")
                actions.student_average(file_path)
            elif option_selected==7:
                break
            else:
                print("Invalid option, select correct option")
        except ValueError as e:
            print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")