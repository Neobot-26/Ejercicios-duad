import json

def open_file(path):
    with open(path, 'r',encoding='utf-8') as file:
        my_data = json.load(file)
        return my_data

def load_data():
    my_dictionary={}
    name_dictionary={}
    base_dictionary={}
    type_list=[]
    name_dictionary["english"]=input("Enter new Pokemon's name:")
    my_dictionary["name"]=name_dictionary
    my_dictionary["level"]=int(input("Enter level of new Pokemon:"))
    while True:
        pokemon_type=input("Enter Pokemon's type:")
        type_list.append(pokemon_type)
        exit_type=input("Would you like to add additional type? Y/N:")
        if exit_type=="N" or exit_type=="n":
            break
    my_dictionary["type"]=type_list
    base_dictionary["HP"]=int(input("Enter Pokemon's HP:"))
    base_dictionary["Attack"]=int(input("Enter Pokemon's Attack:"))
    base_dictionary["Defense"]=int(input("Enter Pokemon's Defense:"))
    base_dictionary["Sp. Attack"]=int(input("Enter Pokemon's Sp. Attack:"))
    base_dictionary["Sp. Defense"]=int(input("Enter Pokemon's Sp. Defense:"))
    base_dictionary["Speed"]=int(input("Enter Pokemon's Speed:"))
    my_dictionary["base"]=base_dictionary
    return my_dictionary
    
def write_file(path,my_data):
    with open(path, 'w',encoding='utf-8') as file:
        json.dump(my_data,file)

def main():
    file_name="pokemon.json"
    data=open_file(file_name)
    new_pokemon=load_data()
    data.append(new_pokemon)
    write_file(file_name,data)

#main
main()

