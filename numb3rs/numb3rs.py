# Implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.
# An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet, akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#.
# But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range! If only NUMB3RS had validated the address in that scene!

# Importing Lib
import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^[0-9_]+\.[0-9_]+\.[0-9_]+\.[0-9_]+$", ip):
        indip = ip.split(".")
        for postn in indip:
            if int(postn) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()