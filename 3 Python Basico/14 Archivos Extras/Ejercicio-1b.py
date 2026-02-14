def read_file(path):
    my_string=""
    my_word=""
    with open(path,"r", encoding="utf-8") as file:
        for line in file.readlines():
            #my_word=""
            #for my_char in range(len(line)-1):
            #    my_word=my_word+line[my_char]
            #my_string=my_string+" "+my_word
            my_string=my_string+" "+line.strip()
        return my_string




#main
print(read_file("hola.txt"))