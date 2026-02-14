import json

def open_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        my_data = json.load(file)
        return my_data

def find_types(list_pokemon):
    print("--------------- Pokemon List ---------------")
    list_types=[]
    for pokemon in list_pokemon:
        my_level=pokemon.get("level")
        for index_type in range(len(pokemon["type"])):
            my_list={}
            my_type = pokemon["type"][index_type]
            my_list["type"]=my_type
            my_list["level"]=my_level
            list_types.append(my_list)
    return list_types

def calcule_levels(list_levels):
    data_list = {}
    data_qty ={}
    my_qty=1
    for index in range(len(list_levels)):
        my_type = list_levels[index]["type"]
        my_level = list_levels[index]["level"]
        if data_list.get(my_type)!=None:
            level_aux = data_list.get(my_type)
            my_level = (level_aux + my_level)
            aux_qty = data_qty.get(my_type)
            my_qty = aux_qty + 1
        data_list[my_type] = my_level
        data_qty[my_type] = my_qty
        my_qty=1
    for pokemons in data_list:
        print(f"Type:{pokemons} -> average of level:{data_list[pokemons]/data_qty[pokemons]}")


def main():
    file_name="pokemon.json"
    data=open_file(file_name)
    types=find_types(data)
    calcule_levels(types)

#main
main()

