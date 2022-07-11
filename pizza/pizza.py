# implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
# Format the table using the library’s grid format.
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, the program should instead exit via sys.exit.

# Making the imports that will be used on the program

import tabulate
import sys
import csv

# Check for the command-line arguments
if len(sys.argv) ==2:
    # Checking for validating the extension of the file is correct
    if sys.argv[1][-3:] == "csv":
        # Logic for openning the file and working with it
        try:
            with open(sys.argv[1]) as file:
                # Storing the data in csv in a dictionary format with DictReader
                reader = csv.DictReader(file)
                #Printing the information in the requested format by using the tabulate module which needs to be installed first with pip install tabulate
                print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
        #Handling the exception for when the file does not exists, it will exit with sys and shows the message
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("File not found")

# Checking for to many command arguments or to few
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")