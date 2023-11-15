#Always google things that you dont know get help of google
from pypdf import PdfWriter
import os

merger = PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
#Note the pdf files must be outside of Day 82 Folder