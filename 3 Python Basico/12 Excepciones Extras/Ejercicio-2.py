def convert_to_integer(list):
    print("Resultado:")
    for element in list:
        try:
            aux=int(element)
            print(f"{element} convertido a {aux}")
        except ValueError as e:
            print(f"No se pudo convertir el elemento: {element}")

#main
my_list=["4","hola","10","4","5.2"]
name=convert_to_integer(my_list)

