# Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# Creating an infinite loop
while True:
    # Ask for user input and saving it in date variable
    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        p = new_numerator / new_denominator
        if p <= 1:
            break
    # "Catching" the exception for ValueError and ZeroDivisionError
    except (ValueError, ZeroDivisionError):
        pass

new_p = int(p * 100)
if new_p <= 1:
    print("E")
elif new_p >= 99:
    print("F")
else:
    print(f"{new_p}%")