import csv

def verification_csv_file(file_path):
  error=0
  try:
    with open(file_path,"r",encoding='utf-8')as csvfile:
      reader = csv.reader(csvfile)
  except FileNotFoundError as e:
    print(f"Error [FileNotFoundError]: Unable to find file CSV. Details:{e}")
    error=1
  return error

def write_csv_filedata(file_path, data_list):
  with open(file_path, 'a', encoding='utf-8', newline='' ) as file:
    writer = csv.writer(file)
    writer.writerow(data_list)

def write_csv_fileheader(file_path,data_list):
  with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(data_list)

def store_data():
  file_name='students_register.csv'
  if verification_csv_file(file_name)==0:
    print("File exist")
  else:
    print("File does not exist, would you like to create a new database?")

def read_csv_file(file_path):
  num_register=0
  head_list=[]
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if num_register==0:
        head_list=row
      else:
        for index in range(len(head_list)-1):
          print(f"{head_list[index].capitalize()}: {row[index]}")
        print(" ")
      num_register+=1

def read_average_score(file_path):
  num_register=0
  head_list=[]
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if num_register==0:
        head_list=row
      else:
        print(f"{head_list[0].capitalize()}: {row[0]}")
        print(f"{head_list[1].capitalize()}: {row[1]}")
        print(f"{head_list[6].capitalize()}: {row[6]}")
        print(" ")
      num_register+=1

def top_three_average(file_path):
  num_register=0
  names_list=[]
  top_three=[]
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      names_list.append(row['name'])
      top_three.append(float(row['average']))
    for index_list1 in range(len(names_list)-1):
      for index_list2 in range(len(names_list)-1-index_list1):
        if top_three[index_list2]<top_three[index_list2+1]:
          aux_variable=top_three[index_list2]
          top_three[index_list2]=top_three[index_list2+1]
          top_three[index_list2+1]=aux_variable
          aux_name=names_list[index_list2]
          names_list[index_list2]=names_list[index_list2+1]
          names_list[index_list2+1]=aux_name
    while num_register<3:
      print(f"Name:{names_list[num_register]}")
      print(f"Average:{top_three[num_register]}")
      print(" ")
      num_register+=1

def student_in_class(file_path,name,classroom):
  num_register=0
  head_list=[]
  student_exist=0
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if num_register==0:
        head_list=row
      else:
        if row[0]==name and row[1]==classroom:
          student_exist=1
          break
      num_register+=1
    return student_exist

def delete_student(file_path,name,classroom,list_of_headers):
  register_students=[]
  with open(file_path, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
      if row['name'] != name and row['classroom'] != classroom:
        register_students.append(row)
  with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=list_of_headers)
    writer.writeheader()
    writer.writerows(register_students)

def students_failing(file_path):
  num_register=0
  head_list=[]
  quantity_of_students=0
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if num_register==0:
        head_list=row
      else:
        if int(row[2])<60:
          print(f"{head_list[0].capitalize()}: {row[0]}")
          print(f"{head_list[1].capitalize()}: {row[1]}")
          print(f"{head_list[2].capitalize()}: {row[2]}")
          if int(row[3])<60:
            print(f"{head_list[3].capitalize()}: {row[3]}")
          if int(row[4])<60:
            print(f"{head_list[4].capitalize()}: {row[4]}")
          if int(row[5])<60:
            print(f"{head_list[5].capitalize()}: {row[5]}")
          print(" ")
          quantity_of_students=1
        elif int(row[3])<60:
          print(f"{head_list[0].capitalize()}: {row[0]}")
          print(f"{head_list[1].capitalize()}: {row[1]}")
          print(f"{head_list[3].capitalize()}: {row[3]}")
          if int(row[4])<60:
            print(f"{head_list[4].capitalize()}: {row[4]}")
          if int(row[5])<60:
            print(f"{head_list[5].capitalize()}: {row[5]}")
          print(" ")
          quantity_of_students=1
        elif int(row[4])<60:
          print(f"{head_list[0].capitalize()}: {row[0]}")
          print(f"{head_list[1].capitalize()}: {row[1]}")
          print(f"{head_list[4].capitalize()}: {row[4]}")
          if int(row[5])<60:
            print(f"{head_list[5].capitalize()}: {row[5]}")
          print(" ")
          quantity_of_students=1
        elif int(row[5])<60:
          print(f"{head_list[0].capitalize()}: {row[0]}")
          print(f"{head_list[1].capitalize()}: {row[1]}")
          print(f"{head_list[5].capitalize()}: {row[5]}")
          print(" ")
          quantity_of_students=1
      num_register+=1
    if quantity_of_students==0:
      print("There are not failing students in registers")