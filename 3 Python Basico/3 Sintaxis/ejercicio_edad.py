name = input("Enter your name:")
last_name = input("Enter your last_name:")
age= int(input("Enter your age:"))
if age>=65:
    print(f"{name} {last_name} is an major adult")
elif age>=40:
    print(f"{name} {last_name} is an adult")
elif age>=18:
    print(f"{name} {last_name} is a young adult")
elif age>=13:
    print(f"{name} {last_name} is a teenager")    
elif age>=10:
    print(f"{name} {last_name} is a pre-teenager")
elif age>=3:
    print(f"{name} {last_name} is a kid")
else:
    print(f"{name} {last_name} is a baby")       