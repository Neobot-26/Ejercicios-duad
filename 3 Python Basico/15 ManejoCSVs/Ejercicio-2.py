import csv

def write_csv_filedata(file_path, data_list):
  with open(file_path, 'a', encoding='utf-8', newline='' ) as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(data_list)

def write_csv_fileheader(file_path,data_list):
  with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(data_list)
   

def store_data():
  file_name='Gamesfile.csv'
  list_of_headers=["name","genre","developer","classification"]
  write_csv_fileheader(file_name,list_of_headers)
  while True:
    list_of_info=[]
    list_of_info.append(input("Enter name of game:"))
    list_of_info.append(input("Enter genre of the game:"))
    list_of_info.append(input("Enter name of developer of the game:"))
    list_of_info.append(input("Enter classification of the game:"))
    write_csv_filedata(file_name, list_of_info)
    cycle=input("Would you like to add a new register?Y/N:")
    if cycle == "N" or cycle == "n":
      break

#main
store_data()
