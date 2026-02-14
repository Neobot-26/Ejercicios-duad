import csv

def read_csv_file(file_path,classification):
  num_register=0
  head_list=[]
  counter_games=0
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if num_register==0:
        head_list=row
        print("-"*40)
        print(f"Games with Classification {classification}:") 
        print("-"*40)
      else:
        if row[3]==classification:
          print(f"{row[0]}")
          counter_games+=1
      num_register+=1
    if counter_games==0:
      print("There are not Games with this Classification")

def read_data():
  path='Games.csv'
  my_classification=input("Enter Classification to search:") 
  read_csv_file(path,my_classification)

#main
read_data()