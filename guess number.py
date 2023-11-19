import random

def guess_number():
    number = random.randint(100, 999) 
    guess = 0
    attempts = 0

    print("guess number between 100-999:")
    while guess != number:
        guess = int(input("your guess is: "))
        attempts += 1

        if guess > number:
            print("Guess a lower number!!!")
        elif guess < number:
            print("Guess a higher number")

    print(f"your number is:{number} with {attempts} guess")

guess_number()