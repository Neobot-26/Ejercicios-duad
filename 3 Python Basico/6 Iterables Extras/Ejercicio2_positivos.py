my_list=[3,6,0,-2,4]
counter=0
for index in range(len(my_list)):
    if my_list[index]<=0:
        counter+=1
if counter>0:
    print("Hay al menos un numero negativo o cero")
else:
    print("Todos los elementos de la lista son positivos")
