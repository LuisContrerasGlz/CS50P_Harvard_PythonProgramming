# Implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.
# f the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.
# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

# Importing sys to access the command-line arguments

import sys

# Checking for the command-line arguments to be 2 since the name of the file is 1 and checking for the extension of the file
if len(sys.argv) == 2:
    if sys.argv[1][-2:] == "py":
# Logic for openning the file and working with it
        try:
            with open(sys.argv[1]) as file:
                numbOfLines = 0
                for line in file:
                    #Checking for comment and removing blank spaces
                    if not line.lstrip().startswith("#") and line.lstrip() != "":
                        # Adding 1 to our numbOfLines variable
                        numbOfLines = numbOfLines + 1
            #Printing the value of numbOfLines
            print(numbOfLines)
        #Handling the exception for when the file does not exists, it will exit with sys and shows the message
        except FileNotFoundError:
            sys.exit("File not found")
    elif sys.argv[1][-2:] != "py":
        sys.exit("Not a python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
