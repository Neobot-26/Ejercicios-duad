def add_values(list):
    sum=0.0
    aux=0.0
    for element in list:
        try:
            aux=float(element)
            sum=sum+aux
            print(f"{aux} sumado correctamente")
        except ValueError as e:
            print(f"Elemento inválido:{element}")
    return sum
#main
my_list=['10','manzana','5.5','3','n/a']
print(f"Total de la suma: {add_values(my_list)}")