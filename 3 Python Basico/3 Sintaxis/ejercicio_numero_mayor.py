number_one=int(input("Enter first number:"))
number_two=int(input("Enter second number:"))
number_three=int(input("Enter third number:"))
if number_one>number_two and number_two>number_three:
    print(f"{number_one} is the highest number")
elif number_two>number_one and number_two>number_three:
    print(f"{number_two} is the highest number")
else:
    print(f"{number_three} is the highest number")