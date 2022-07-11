# Implement a program that:
# Expects the user to provide two command-line arguments:
# 1. The name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# 2. The name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.
# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.


# Making the imports that will be used on the program
import sys
import csv

def main():
    commandline_argcheck()
    output = []
    # Logic for openning the file and working with it
    try:
        # Opening the csv file and using the DictReader to work with it as a dictorionary, then creating name, last name and adding them to dict
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_name = row['name'].split(",")
                output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row['house']})
    # Handling the exception for when the file does not exists, it will exit with sys and shows the message
    except FileNotFoundError:
        sys.exit("File not found")

    # Writing the new csv file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row['first'], "last": row['last'], "house": row['house']})

def commandline_argcheck():
    #Check how many elements in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Check if it is a CSV file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()