def load_data():
    try:
        my_data=input("Ingrese su nombre:")
        if my_data.isdigit():
            raise ValueError("El nombre no puede ser un número")
        return my_data
    except ValueError as e:
        print(f"Error [ValueError]: El nombre no puede ser un número. Detalles: {e}")
def load_data2():
    try:
        my_age=int(input("Ingrese su edad:"))
        return my_age
    except ValueError as e:
        print(f"Error [ValueError]: Número no valido. Detalles: {e}")

def verify(name,age):
    if name!=None and age!=None:
        print(f"Hola {name}, su edad es {age}")    
    else:
        print("Alguno de los dos datos es incorrecto")
    
#main
name=load_data()
age=load_data2()
verify(name,age)

