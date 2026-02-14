import json

def open_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        my_data = json.load(file)
        return my_data
    
def request_type():
    type_to_search=input("Enter type of Pokemon to search(Fire, Water, Electric,etc):")
    return type_to_search

def print_data(list_pokemon,my_type):
    print(f"---- The list of Pokemon type {my_type} are ----")
    for pokemon in list_pokemon:
        my_name=pokemon["name"]["english"]
        for index_type in pokemon["type"]:
            if index_type == my_type:
                print(my_name)
        

def main():
    file_name="pokemon.json"
    data=open_file(file_name)
    my_type=request_type()
    print_data(data,my_type)

#main
main()

