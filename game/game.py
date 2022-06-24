# implement a program that:
# Prompts the user for a level, n. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#.        If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#.        If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#.        If the guess is the same as that integer, the program should output Just right! and exit.

# Importing random
import random
import random

# Get level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

# Set random number
random_number = random.randint(1, level)

# Get guess and check
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                break
    except:
        pass