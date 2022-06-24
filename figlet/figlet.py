# FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:
# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

# Importing sys and random
import sys
import random

from pyfiglet import Figlet
figlet = Figlet()

# Zero if the user would like to output text in a random font.
if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    isRandom = False
else:
    print("Invalid usage")
    sys.exit(1)

# Getting a list of available fonts like this:
figlet.getFonts()

if isRandom == False:
    try:
        # Setting the font like this, wherein f is the font’s name as a str:
        font = figlet.setFont(font=sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    # Setting the font with code like this, wherein f is the font’s name as a str:
    font = random.choice(figlet.getFonts())

# Getting user input
msg = input("Input: ")

# Output text in that font ike this, wherein s is that text as a str:
output = figlet.renderText(msg)

print("Output: ")
print(output)