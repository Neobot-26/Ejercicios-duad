time_req=0
time_sec=int(input("Enter the time in seconds:"))
if time_sec>600:
    print("Major")
elif time_sec==600:
    print("Equal")
else:    
    time_req=600-time_sec
    print(f"There are {time_req} seconds required to achieve 10 minutes")