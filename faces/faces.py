# Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

# Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. 

# Main function calling convert function to replace the faces with emoji and then print the final message
def main():
    userI = input()
    userO = convert(userI)
    print(userO)

# Convert function which takes the text and "scans" it to search for :( or :) and then do the replacement 
def convert(text):
    smill = text.replace(":)", "🙂")
    sad = smill.replace(":(", "🙁")

    return sad

main()