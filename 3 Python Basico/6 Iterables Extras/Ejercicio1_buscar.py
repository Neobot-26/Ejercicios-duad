my_list=[]
value_f=0
counter=0
for index in range(7):
    value=int(input("Ingrese un nuevo valor:"))
    my_list.append(value)
value_f=int(input("Ingrese numero a buscar:"))
index=0
for index in range(len(my_list)):
    if my_list[index]==value_f:
        counter+=1 
#print(my_list)
print(f"El número {value_f} aparece {counter} veces.")
