import json

def open_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        my_data = json.load(file)
        return my_data

def print_data(list_pokemon):
    print("---- Statistics for Pokemon List ----")
    for pokemon in list_pokemon:
        my_name=pokemon["name"]["english"]
        my_attack=pokemon["base"]["Attack"]
        my_defense=pokemon["base"]["Defense"]
        my_speed=pokemon["base"]["Speed"]
        print(f"Name:{my_name}")
        print(f"Attack:{my_attack}")
        print(f"Defense:{my_defense}")
        print(f"Speed:{my_speed}")
        print("")

def main():
    file_name="pokemon.json"
    data=open_file(file_name)
    print_data(data)

#main
main()

