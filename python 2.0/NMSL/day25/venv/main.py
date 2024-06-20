import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Text+Files/*.txt")

for file in filepaths:
    df =open(file, "r")
    content = df.read()
    filename = Path(file).stem
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=15, style="B")
    pdf.cell(w=50, h=8, txt=filename.title(), align="L", ln=1)
    pdf.set_font(family="Times", size=11)
    pdf.multi_cell(w=0, h=5, txt=content, align="L")
    pdf.output(f"pdfs/{filename}.pdf")