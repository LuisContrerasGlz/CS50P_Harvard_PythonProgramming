# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
# Reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    # Getting user input
    message = input("Input: ")
    # Removing vowels and saving it
    message_without_vowels = shorten(message)
    # Printing the output
    print("Output: " + message_without_vowels)


def shorten(word):
    word_without_vowels = ""
    # Looping through every letter
    for letter in word:
        # Checking if it is not vowels whether inputted in upper case or lowercase
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            # Adding the letter
            word_without_vowels += letter
    # Returning the new word
    return word_without_vowels


if __name__ == "__main__":
    main()