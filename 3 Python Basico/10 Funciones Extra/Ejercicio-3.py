def verification(my_string):
    qty_vowels=0
    for index in range(len(my_string)):
        if my_string[index]=="a" or my_string[index]=="e" or my_string[index]=="i" or my_string[index]=="o" or my_string[index]=="u":
            qty_vowels+=1
    return qty_vowels

#main
my_sentence=input("Ingrese el string para verificar la cantidad de vocales:")
print(f"Se encontraron {verification(my_sentence)} vocales")