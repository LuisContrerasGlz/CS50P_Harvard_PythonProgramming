# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

# Implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. 
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

def main():
    time = input("What time is it? ")

    conv_time = convert(time)

    # Between 7:00 and 8:00 is breakfast
    if (conv_time >= 7 and conv_time <= 8):
        print("breakfast time")

    #  Between 12:00 and 13:00 is lunch
    if (conv_time >= 12 and conv_time <= 13):
        print("lunch time")

    # Between 18:00 and 19:00 is dinner
    if (conv_time >= 18 and conv_time <= 19):
        print("dinner time")


# Defining function to take the time, spliting user input into 2 and then converting it so it can be used
def convert(time):
    hours, minutes = time.split(":")

    conv_minute = int(minutes) / 60

    return int(hours) + conv_minute


if __name__ == "__main__":
    main()