counter=0
sumatory=0
number_request=int(input("Enter a number to calculate sumatory:"))
for counter in range(number_request+1):
    sumatory=sumatory+counter
print(f"The sum of all value from 1 to {number_request} is {sumatory}")
