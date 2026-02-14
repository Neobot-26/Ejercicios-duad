def read_file(path):
    my_string=""
    with open(path,"r", encoding="utf-8") as file:
        for line in file.readlines():
            my_string=my_string+" "+line.upper()
        return my_string

def save_file(path,my_text):
    with open(path,"w", encoding="utf-8") as file:
         file.write(my_text)

def main():
    my_text=""
    my_text=(read_file("Hola2.txt"))
    save_file("Hola3.txt",my_text)
#main
main()