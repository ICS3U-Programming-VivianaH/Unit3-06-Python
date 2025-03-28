#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 27 2025
# This program tells if you guess is right
import random

# Asking the user for a input
user_number = input("Guess a number between 0 and 9: ")

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)

try:
    # Convert user input to an integer
    user_number = int(user_number)

    # Check if the guess is correct
    if user_number == random_number:
        print("You guessed correctly!")
        # Check if the guess is wrong
    else:
        print("You guessed wrong, the answer is", random_number)
        # Check if the guess is not an integer
except ValueError:
    print(user_number, "is not an integer")

if __name__ == "__main__":
    main()
