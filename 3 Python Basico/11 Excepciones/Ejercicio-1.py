def add(current,value):
    try:
        result=current+value
        return result
    except TypeError as e:
        print(f"Error [TypeError]: Invalid operation using a string. Details:{e}")

def subtract(current,value):
    try:
        result=current-value
        return result
    except TypeError as e:
        print(f"Error [TypeError]: Invalid operation using a string. Details:{e}")

def multiply(current,value):
    try:
        result=current*value
        return result
    except TypeError as e:
        print(f"Error [TypeError]: Invalid operation using a string. Details:{e}")

def divide(current,value):
    try:
        result=current/value
        return result
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Invalid divide a value by zero. Details:{e}")
    

def run_calculator():
    current=10
    option=0
    while option != 6:
        try:
            option=int(input("Enter an option: 1.Add 2.Subtract 3.Multiplication 4.Division 5.Erase result 6.Exit:"))
        except ValueError as e:
            print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
            option=0  
            continue 
        if option==1:
            try:
                value=int(input("Enter value:"))
                result=add(current,value)
                print(f"The result of addition is:{result}")
                current=result
            except ValueError as e:
                print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
        elif option==2:
            try:
                value=int(input("Enter value:"))
                result=subtract(current,value)
                print(f"The result of subtraction is:{result}")
                current=result
            except ValueError as e:
                print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
        elif option==3:
            try:
                value=int(input("Enter value:"))
                result=multiply(current,value)
                print(f"The result of multiplication is:{result}")
                current=result
            except ValueError as e:
                print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
        elif option==4:
            try:
                value=int(input("Enter value:"))
                result=divide(current,value)
                if result!=None:
                    print(f"The result of division is:{result}")
                    current=result
            except ValueError as e:
                print(f"Error [ValueError]: Unable to convert the value 'abc' to integer. Details:{e}")
        elif option==5:
            current=0
            print("Last stored value has been erased")
        else:
            if option!=6:
                print("Invalid option, select a valid option")    

#main
run_calculator()