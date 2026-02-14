my_list=[]
new_list=[]
string_new=""
for index in range(5):
    string_new=input("Ingrese una nueva palabra:")
    my_list.append(string_new)
for index in range(5):
    if len(my_list[index])>4:
        new_list.append(my_list[index])
print(my_list)
print(f"Nueva lista:{new_list}")