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
        list_dictionary.append(my_dictionary)
      num_register+=1
    return list_dictionary
  
def counter(data):
  list={}
  for my_list_index in range(len(data)):
    my_genre = data[my_list_index]["genre"]
    if list.get(my_genre)!=None:
      counter_aux = list.get(my_genre)
      my_counter = counter_aux + 1
    else:
      my_counter=1
    list[my_genre] = my_counter
  return list

def print_dict(data_dict):
  print("Genres found in CSV file:")
  for index_dict in data_dict:
    print(f"{index_dict}: {data_dict[index_dict]}")

def read_data():
  data=[]
  genre_list=[]
  path='Games.csv' 
  data=read_csv_file(path)
  genre_list=counter(data)
  print_dict(genre_list)

#main
read_data()