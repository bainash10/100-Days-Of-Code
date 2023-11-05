#Note always google things about each library dont read it on detail understand it and edit it as per your use

# from PyPDF2 import PdfMerger
# import os

# merger = PdfMerger()
# files=[file for file in os.listdir("Day76-Exercise 8 Merge the PDF") if file.endswith(".pdf")]

# for pdf in files:
#     merger.append(pdf)

# merger.write("Day76-Exercise 8 Merge the PDF/merged-pdf.pdf")
# merger.close()

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
#Remember: The files to be merged most be outside of the Day 76 folder and the o/p will also be shown outside i.e merged-pdf.pdf