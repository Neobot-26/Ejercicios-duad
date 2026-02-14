def read_file(path):
    my_string=""
    with open(path,"r", encoding="utf-8") as file:
        for line in file.readlines():
            my_string=my_string+" "+line.strip()
        return my_string

def counter_words(text):
    my_counter=0
    for index in range (len(text)):
        if text[index]==" ":
            my_counter+=1
    return my_counter

def main():
    my_text=""
    my_text=(read_file("document.txt"))
    qty_words=counter_words(my_text)
    print(f"This file has {qty_words} words")

#main
main()