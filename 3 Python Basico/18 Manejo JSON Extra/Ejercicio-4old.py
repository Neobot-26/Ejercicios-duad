import json

def open_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        my_data = json.load(file)
        return my_data

def find_types(list_pokemon):
    print("---- Pokemon List ----")
    list_types=[]
    for pokemon in list_pokemon:
        my_level=pokemon.get("level")
        for index_type in range(len(pokemon["type"])):
            my_list={}
            my_type = pokemon["type"][index_type]
            my_list["type"]=my_type
            my_list["my_level"]=my_level
            list_types.append(my_list)
    for types_pokemon in list_types:
        print(types_pokemon)

    #print(list_types)
 
def main():
    file_name="pokemon.json"
    data=open_file(file_name)
    find_types(data)

#main
main()

