# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. 
# For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. 
# If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. 
# If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# Implement a program that:

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.

# Importing random
import random

# main function calling get levelgenerate_game functions and printing the score by calling the score funtion
def main():
    level = get_level()
    score = generate_game(level)
    print("Score:", score)


# Get level function
def get_level():
    while True:
        try:
            # Getting input from the user to check for the level checking for it to be between 1 and 3
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except:
            pass
    return level

# generate_integer function to select the values of x and y depending on the level selected by the user
def generate_integer(level):
    # Using the random.randit method to generate the random numbers for x and y based on the level selected by the user
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    # Returning the value of x and y in order to use them when calling the function
    return x,y

# Function to handle the rounds on the game, giving 3 rounds to the user to get the answer and if not fnishing and giving the answer
def generate_round(x, y):
    num_of_tries = 1
    while num_of_tries <= 3:
        try:
            question = int(input(f"{x} + {y} = "))
            if question == (x + y):
                return True
            else:
                print("EEE")
                num_of_tries += 1
        except:
            print("EEE")
            num_of_tries += 1
            pass
    print(f"{x} + {y} = {x + y}")
    return False

# Handling the game here
def generate_game(level):
    rounds_count = 0
    score = 0
    while rounds_count < 10:
        x, y = generate_integer(level)
        response = generate_round(x, y)
        if response == True:
            score += 1
        rounds_count += 1
    return score


# Calling name function to run
if __name__ == "__main__":
    main()