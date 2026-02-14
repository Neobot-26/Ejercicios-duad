def read_file_of_songs(path):
    my_list=[]
    with open(path,"r", encoding="utf-8") as file:
        for line in file.readlines():
            my_list.append(line)
        return my_list

def sort_list(aux_list):
    for index in range(len(aux_list)):
        for index2 in range(1,(len(aux_list)-index)):
            var_temp=aux_list[index2-1]
            if var_temp>aux_list[index2]:
                aux_list[index2-1]=aux_list[index2]
                aux_list[index2]=var_temp
    return aux_list

def list_to_text(my_list):
    my_text=""
    for index in my_list:
        my_text=my_text+index
    return my_text


def write_songs(path,my_text):
    with open(path,"w",encoding="utf-8") as file:
        file.write(my_text)

def main():
    aux_list=[]
    my_text=""
    my_list=read_file_of_songs("cancion.txt")
    print("List of songs from the file:")
    print(my_list)
    aux_list=sort_list(my_list)
    my_text=list_to_text(aux_list)
    print("List of songs in alphabetical order:")
    print(my_text)
    write_songs("songs.txt",my_text)


#main
main()


