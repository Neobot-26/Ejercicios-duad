import csv

def read_csv_file(file_path,developer):
  num_register=0
  head_list=[]
  counter_games=0
  with open(file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if num_register==0:
        head_list=row
        print("-"*40)
        print(f"Video games developed by {developer}:") 
        print("-"*40)
      else:
        if row[2]==developer:
          print(f"-{row[0]} (Classification:{row[3]}, Genre:{row[1]})")
          counter_games+=1
      num_register+=1
    if counter_games==0:
      print(f"There are not Games developed by {developer}")

def read_data():
  path='Games.csv'
  my_developer=input("Enter Developer of video game to search:") 
  read_csv_file(path,my_developer)

#main
read_data()