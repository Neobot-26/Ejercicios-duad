import data

def student_register(file_name,list_of_headers):
    new_database="Y"
    if data.verification_csv_file(file_name)!=0:
        print("-"*60)
        new_database=input("File does not exist, would you like to create a new database? Y/N:")
        if new_database=="y" or new_database=="Y":
            data.write_csv_fileheader(file_name,list_of_headers)
    if new_database=="y" or new_database=="Y":
        while True:
            try:
                list_of_info=[]
                name_student=input("Enter name of student:")
                while is_valid_name(name_student)==1:
                    print("Text entered for name is not valid, enter a valid name")
                    name_student=input("Enter name of student:")
                classroom_student=input("Enter classroom of student:")
                while is_valid_classroom(classroom_student)==1:
                    print("Text entered for Classroom is not valid, enter a valid data")
                    classroom_student=input("Enter classroom of student:")
                if data.student_in_class(file_name,name_student,classroom_student)==0:
                    list_of_info.append(name_student)
                    list_of_info.append(classroom_student)
                    spanish_score=subject_matter("Spanish")
                    list_of_info.append(spanish_score)
                    english_score=subject_matter("English")
                    list_of_info.append(english_score)
                    history_score=subject_matter("History")
                    list_of_info.append(history_score)
                    science_score=subject_matter("Science")
                    list_of_info.append(science_score)
                    list_of_info.append((spanish_score+english_score+history_score+science_score)/4)
                    data.write_csv_filedata(file_name, list_of_info)
                else:
                    print("Student already exists in classroom...")
                cycle=input("Would you like to add a new register?Y/N:")
                if cycle == "N" or cycle == "n":
                    break
            except ValueError as e:
                print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
                print("Re-enter information of Student")

def student_delete(file_name,list_of_headers):
    confirm_delete="Y"
    if data.verification_csv_file(file_name)!=0:
        print_database_error()
    else:
        name_student=input("Enter name of student to delete:")
        while is_valid_name(name_student)==1:
            print("Text entered for name is not valid, enter a valid name")
            name_student=input("Enter name of student to delete:")
        classroom_student=input("Enter classroom of student to delete:")
        while is_valid_classroom(classroom_student)==1:
            print("Text entered for Classroom is not valid, enter a valid data")
            classroom_student=input("Enter classroom of student to delete:")
        if data.student_in_class(file_name,name_student,classroom_student)==1:
            confirm_delete=input("Student exist in registers, would you like to proceed, Y/N:")
            if confirm_delete=="Y" or confirm_delete=="y":
                data.delete_student(file_name,name_student,classroom_student,list_of_headers)
                print(f"The student:{name_student} from classroom:{classroom_student} was deleted")
        else:
            print("Student is not present is registers")


def student_read(file_name):
    if data.verification_csv_file(file_name)!=0:
        print_database_error()
    else:
        data.read_csv_file(file_name)
        
def student_average(file_name):
    if data.verification_csv_file(file_name)!=0:
        print_database_error()
    else:   
        data.read_average_score(file_name)

def student_top_three_average(file_name):
    if data.verification_csv_file(file_name)!=0:
        print_database_error()
    else:   
        data.top_three_average(file_name)


def is_valid_name(name):
    valid_name=0
    if name==" ":
        valid_name=1
    else:
        if not name.replace(" ","").isalpha():
            valid_name=1
    return valid_name

def is_valid_classroom(classroom):
    valid_classroom=0
    if classroom==" ":
        valid_classroom=1
    elif len(classroom)!=3:
        valid_classroom=1
    elif not classroom[0].isdigit() or not classroom[1].isdigit() or not classroom[2].isalpha():
        valid_classroom=1
    return valid_classroom

def is_valid_score(score):
    valid_score=0
    if score==" ":
        valid_score=1
    elif score<0 or score>100:
        valid_score=1
    return valid_score

def students_under_sixty(file_name):
    if data.verification_csv_file(file_name)!=0:
        print_database_error()
    else:
        data.students_failing(file_name)

def print_database_error():
    print("-"*60)
    print("Database does not exist, select another option ")
    print("-"*60)

def subject_matter(field_of_study):
    subject_score=int(input(f"Enter {field_of_study} Score:"))
    while is_valid_score(subject_score)==1:
        print("Score not valid, enter a valid score")
        subject_score=int(input(f"Enter {field_of_study} Score:"))
    return subject_score