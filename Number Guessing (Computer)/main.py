import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Please guess the number!"))
        if guess > random_number:
            print("The number is too high!")
        elif guess < random_number:
            print("The number is too low!")
    else:
        print("Congrats, you guessed the correct answer!")

guess(10)