# Implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
# Treat the user’s input case-insensitively.

# Declaring an empty dictionary
grocery = {}

# Creating an infinite loop
while True:
    try:
        # Ask for user input and saving it in date variable
        items = input()
        # Changing the item to lowercase and then checking if it is on the list
        if items.lower() in grocery:
            grocery[items.lower()] += 1
        else:
            grocery[items.lower()] = 1
    except EOFError:
        # Printing the items in alphabetical order and then stop the loop
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        break