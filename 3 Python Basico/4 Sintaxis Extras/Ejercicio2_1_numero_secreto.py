import random
user_value=0
secret_number=random.randint(1,10)
while user_value!=secret_number:
    user_value=int(input("Enter value to guess secret number:"))
print("You got the secret number!!!!")