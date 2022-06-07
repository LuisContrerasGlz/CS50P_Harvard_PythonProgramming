# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# Declaring m which will be the input from user and then converting it to int
m = (int(input("m: ")))

# Declaring c which it is a constant with the value 300000000
c = 300000000

# Declaring E which will be the calculation of the fomrula for the result
E = m * (c ** 2)

# Printing E which is the result of this program
print(E)