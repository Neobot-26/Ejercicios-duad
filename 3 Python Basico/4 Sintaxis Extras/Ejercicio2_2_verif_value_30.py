value1=int(input("Enter first value to verify:"))
value2=int(input("Enter second value to verify:"))
value3=int(input("Enter third value to verify:"))
if value1==30 or value2==30 or value3==30:
    print("Correct!!!")
elif (value1+value2+value3)==30:
    print("Correct!!!")
else:
    print("Incorrect!!!")
