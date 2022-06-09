# Implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

# Declaring a variable called answer which will take the input from user and change it to lower case and deleting the spaces so it covers prerequisites on the problem
greeting = input("Greeting: ").lower().strip()

# Using startswith method to check if the greeting starts with hello, else checking if it starts with H and else just prin the $100
if greeting.startswith("hello"):
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")