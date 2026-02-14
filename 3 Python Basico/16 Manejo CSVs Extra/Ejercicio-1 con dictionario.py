import csv

def read_csv_file(file_path):
  num_register=0
  list_dictionary=[]
  head_list=[]
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      my_dictionary={}
      if num_register==0:
        head_list=row
      else:
        for index in range(len(head_list)):
          my_dictionary[head_list[index]]=row[index]
          print(f"{head_list[index]}: {row[index]}")
        list_dictionary.append(my_dictionary)
        print(" ")
      num_register+=1

def read_data():
  data={}
  path='Games.csv' 
  read_csv_file(path)

#main
read_data()