import random
number_entered=0
secret_number= random.randint(1,10)
while number_entered!=secret_number:
    number_entered=int(input("Enter a number to guess the secret number:"))
print(f"You got it !!!! The secret number was {number_entered}")