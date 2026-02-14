def char_counter(my_string,char):
    counter=0
    for index in range(len(my_string)):
        if my_string[index]==char:
            counter+=1
    return counter

#main
new_word=input("Ingrese una palabra:")
new_char=input("Ingrese el caracter que desea buscar:")
print(f"Se a encontrado {char_counter(new_word,new_char)} veces el caracter")