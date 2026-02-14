employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
my_dictionary = {}
for index in range(len(employees)):
    my_name = employees[index]["name"]
    my_department = employees[index]["department"]
    if my_dictionary.get(my_department)!=None:
        name_aux = my_dictionary.get(my_department)
        my_name = name_aux +", "+ my_name
    my_dictionary[my_department] = my_name
print(my_dictionary)
