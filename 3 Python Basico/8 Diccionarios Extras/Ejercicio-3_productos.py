products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
my_dictionary = {}
for index in range(len(products)):
    my_category = products[index]["category"]
    my_price = products[index]["price"]
    if my_dictionary.get(my_category)!=None:
        price_aux = my_dictionary.get(my_category)
        my_price = price_aux + my_price
    my_dictionary[my_category] = my_price
print(my_dictionary)
