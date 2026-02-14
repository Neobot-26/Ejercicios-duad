my_list=[]
value_h=0
for index in range(10):
    value=int(input("Ingrese un nuevo valor:"))
    my_list.append(value)
    if value_h<value:
        value_h=value
print(my_list)
print(f"El más alto fue {value_h}.")
