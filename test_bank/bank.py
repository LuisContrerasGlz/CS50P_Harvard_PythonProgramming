# Reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. Only main should call print.

def main():
    # Getting user input for greeting
    greeting = input("Greeting: ")
    # Storing the result of value function
    value_to_print = value(greeting)
    print(f"${value_to_print}")


def value(greeting):
    # Converting greeting in all lower with the lower method and without whitespaces with strip
    greeting = greeting.lower().strip()
    # Checking if the answer has 'hello', return 0
    if 'hello' in greeting:
        return 0
    # Checking if answer starts with 'h', return 20 and otherwise return 100
    elif 'h' == greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()