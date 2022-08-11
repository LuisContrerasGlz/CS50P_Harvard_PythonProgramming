#  Implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard, with these specifications:
# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
# The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.
# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.

# Importing Lib

from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", size=50)
        # Heading
        self._pdf.cell(w=0, h=60, txt="CS50 Shirtificate",
                       new_x="LMARGIN", new_y="NEXT", align="C")
        # Creating the Image
        self._pdf.image("shirtificate.png", w=self._pdf.epw,
                        alt_text="CS50 Shirtificate")
        # Putting the Text
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")

        
    def save(self, name):
        self._pdf.output(name)

# Getting user name, creating pdf and finally creating output file

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")