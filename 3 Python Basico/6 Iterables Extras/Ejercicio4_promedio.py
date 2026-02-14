my_list=[10,20,30,40,50]
new_list=[]
value_average=0
value_sum=0
for index in range(len(my_list)):
    value_sum=value_sum+my_list[index]
value_average=value_sum//len(my_list)
print(f"Promedio: {value_average}")
for index in range(len(my_list)):
    if my_list[index]>value_average:
        new_list.append(my_list[index])
print(f"Nueva lista:{new_list}")