constant=3

def remove_values(my_list):
    index=0
    while (index < len(my_list)):
        if my_list[index] % 3 == 0:
            my_list.pop(index)
        else:
            index += 1


def multi_values(my_list):
    for index, number in enumerate (my_list):
        my_list[index] = number * constant

def change_global_var():
    global constant
    constant = 2

def main(aux_list):
    initial_list = [45, 56, 84, 33, 13, 91]
    aux_list=initial_list
    print("Lista inicial")
    print(initial_list)
    print("Removiendo valores divisibles entre 3")
    remove_values(initial_list)
    print(initial_list)
    print(f"Multiplicando valores por {constant}")
    multi_values(initial_list)
    print(initial_list)
    print("Modificando variable global")
    change_global_var()
    print(f"Multiplicando valores por {constant}")   
    multi_values(aux_list)
    print(aux_list)
#main
new_list=[]
main(new_list)