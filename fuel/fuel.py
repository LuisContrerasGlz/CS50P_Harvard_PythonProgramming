# Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# Creating an infinite loop
while True:
    # Ask for user input and saving it in date variable
    fuel = input("Fraction: ")
    try:
        numer, denomin = fuel.split("/")
        new_numer = int(numer)
        new_denomin = int(denomin)
        p = new_numer / new_denomin
        if p <= 1:
            break
    # "Catching" the exception for ValueError and ZeroDivisionError
    except (ValueError, ZeroDivisionError):
        pass

# Comparing and printing depending on result
p2 = int(p * 100)
if p2 <= 1:
    print("E")
elif p2 >= 99:
    print("F")
else:
    print(f"{p2}%")