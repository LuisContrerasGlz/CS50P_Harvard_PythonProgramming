# Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list

# Creating the list with the name of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Creating an infinite loop
while True:
     # Ask for user input and saving it in date variable
    date = input("Date: ")
    if "/" in date:
        month, day, year = date.split("/")
    elif "," in date:
        date = date.replace(",","")
        month, day, year = date.split(" ")
        if month in months:
            month = months.index(month) + 1
    try:
        if int(month) > 12 or int(day) > 31:
            continue
        else: break
    except ValueError:
        continue

# Printing the answer
print(year + "-" + f"{int(month):02}" + "-" + f"{int(day):02}")