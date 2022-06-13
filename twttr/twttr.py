# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

# Getting the user input and printing it on the screen

answr = input("Input: ")
print("Output: ", end="")


# Looping through every letter of the input

for let in answr:
    # Checking if it is not vowels whether in uppercase or lowercase and printing the letter
    if not let.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(let, end="")
print()