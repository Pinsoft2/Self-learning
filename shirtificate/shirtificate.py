from fpdf import FPDF

# class PDF(FPDF):
#     def header(self):
#         # Rendering logo:
#         self.image("shirtificate.png")
#         # Setting font: helvetica bold 15
#         # self.set_font("helvetica", "B", 15)
#         # Moving cursor to the right:
#         self.cell(80)
#         # Printing title:
#         with self.set_text_color(255, 255, 255):
#                 self.cell(txt="Pinsoft", border=1)
#         # Performing a line break:
#     #     self.ln(20)
 # hmm

    # def footer(self):
    #     # Position cursor at 1.5 cm from bottom:
    #     self.set_y(-15)
    #     # Setting font: helvetica italic 8
    #     self.set_font("helvetica", "I", 8)
    #     # Printing page number:
    #     self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class

# The orientation of the PDF should be Portrait.
# The format of the PDF should be A4, which is 210mm wide by 297mm tall.
pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
# The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally
pdf.image("shirtificate.png",0,30)
pdf.set_font("helvetica", "B", 50)
pdf.set_text_color(0, 0, 0)
pdf.cell(200,0,txt='CS50 Shirtificate', align='C')
pdf.set_font("helvetica", "B", 30)
pdf.set_text_color(255, 255, 255)
name=input("What's your name? ")+" took CS50"
pdf.cell(-200,160,txt=name,border=0,align='C')
pdf.output("shirtificate.pdf")
# print("ilove you jj")

# The shirt’s image should be centered horizontally.
# The user’s name should be on top of the shirt, in white text.

