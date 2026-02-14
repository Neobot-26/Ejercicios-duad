def request_text():
     my_text=input("Enter a new line of text:")
     my_text=my_text+"\n"
     return my_text

def save_file(path,my_text):
    with open(path,"a", encoding="utf-8") as file:
         file.write(my_text)

#main
my_text=request_text()
save_file("Ejercicio4.txt",my_text)
