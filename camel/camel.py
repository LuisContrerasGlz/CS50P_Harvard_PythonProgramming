# Implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

# Getting user input which will be camelCase

camelCaseInput = input("camelCase: ")

# Declaring variable for snake_case blank which will be filled later

snake_case = ""

# Looping through every letter searching for upperCase and printing underscores and the letter in lowercase if there is one

for i in range(len(camelCaseInput)):
    if camelCaseInput[i].isupper():
        snake_case = snake_case + "_" + camelCaseInput[i].lower()
    else:
        snake_case += camelCaseInput[i]

print("snake case: ", snake_case)