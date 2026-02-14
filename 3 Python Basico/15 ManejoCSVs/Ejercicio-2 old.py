import csv

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8', newline='' ) as file:
    writer = csv.DictWriter(file, headers,delimiter=" ")
    writer.writeheader()
    writer.writerows(data)

def store_data():
  list_of_dictionary=[]
  list_of_headers=["name","gender","developer","classification"]
  while True:
    list_of_info=[]
    dictionary_games={}
    my_data1=input("Enter name of game:")
    my_data2=input("Enter genre of the game:")
    my_data3=input("Enter name of developer of the game:")
    my_data4=input("Enter classification of the game:")
    list_of_info.append(my_data1)
    list_of_info.append(my_data2)
    list_of_info.append(my_data3)
    list_of_info.append(my_data4)
    index_info=0
    for index_header in list_of_headers:
      dictionary_games[index_header]=list_of_info[index_info]
      index_info+=1
    list_of_dictionary.append(dictionary_games)
    cycle=input("Would you like to add a new register?Y/N:")
    if cycle == "N" or cycle == "n":
      break
  print(list_of_dictionary)
  write_csv_file('Games2.csv',list_of_dictionary,list_of_headers)

#main
store_data()
