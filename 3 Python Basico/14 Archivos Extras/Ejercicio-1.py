def read_file(path):
    my_string=""
    with open(path,"r", encoding="utf-8") as file:
        for line in file.readlines():
            my_string=my_string+" "+line.strip()
        return my_string


#main
print(read_file("hola.txt"))