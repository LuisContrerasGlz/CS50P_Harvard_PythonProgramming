# Implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. 
# Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

# Creating the menu dictionary
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Declaring a variable for the amount and starting it to 0

amount = 0

# Creating an infinite loop
while True:
    try:
        # Ask for user input, tittle will make the first letter of each word uppercase
        item = input("Item: ").title()
        # Check if item is already in the dictionary
        if item in menu:
            # Add the item price to total_amount
            amount += menu[item]
            # Print the current total_amount
            print("Total: $", end="")
            print("{:.2f}".format(amount))
    except EOFError:
        # Print a new line and stop the loop
        print()
        break