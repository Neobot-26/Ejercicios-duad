import json

def open_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        my_data = json.load(file)
        return my_data

def print_data(list_pokemon):
    print("---- Pokemon List ----")
    for pokemon in list_pokemon:
        my_type=""
        my_name=pokemon["name"]["english"]
        my_level=pokemon.get("level")
        for index_type in range(len(pokemon["type"])):
            my_type = my_type+pokemon["type"][index_type]
            if index_type!=(len(pokemon["type"])-1):
                my_type=my_type+"/"
        my_attack=pokemon["base"]["Attack"]
        print(f"Name:{my_name}")
        print(f"Type:{my_type}")
        print(f"Level:{my_level}")
        print(f"Base Attack:{my_attack}")
        print("")

def main():
    file_name="pokemon.json"
    data=open_file(file_name)
    print_data(data)

#main
main()

