counter=1
table_number=int(input("Enter table number you wish to see:"))
for counter in range(1,13):
    print(f"{table_number}X{counter}=",table_number*counter)