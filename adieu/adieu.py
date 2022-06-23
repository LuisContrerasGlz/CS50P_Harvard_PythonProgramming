# Implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and  names with  commas and one and, as in the below:
# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

# Importing inflect
import inflect

p = inflect.engine()

# Creating a list of names
names_list = []

# Creating an infinite Loop
while True:
    try:
        # Declaring a variable for user input
        inpname = input("Name: ")
        names_list.append(inpname)
    except EOFError:
        # Creating a new line and then stoping the loop
        print()
        break

# Printing using inflect module
output = p.join(names_list)
print("Adieu, adieu, to "+ output)