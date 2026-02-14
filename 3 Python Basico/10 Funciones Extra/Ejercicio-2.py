def verification(my_list,qty_char):
    new_list=[]
    for index in range(len(my_list)):
        if len(my_list[index])>qty_char:
            new_list.append(my_list[index])
    return new_list

#main
my_list=["cielo", "sol", "maravilloso", "día"]
qty_chars=int(input("Ingrese el numero de letras minimas en la palabra: "))
print(verification(my_list,qty_chars))