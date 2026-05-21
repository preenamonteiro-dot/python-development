import random


secret_number = random.randint(1, 100)


print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")


attempts = 0
max_attempts = 5


while attempts < max_attempts:

   
    guess = int(input("Enter your guess: "))

   
    attempts += 1

   
    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Congratulations! You guessed correctly.")
        break


if guess != secret_number:
    print("Game Over!")
    print("The correct number was:", secret_number)