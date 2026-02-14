my_list=[9,4,7,1,5]
value_min=my_list[0]
for index in range(1,len(my_list)):
    if my_list[index]<value_min:
        value_min=my_list[index]
print(f"El menor valor es {value_min}")
