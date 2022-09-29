from PyPDF2 import PdfMerger

""" 
Author: Alannah Cullinane Cooney
Date: 29/09/2022

Create a list with the pdfs that you would like to merge
For example I am using these two files from an Agile Processes lecture

Add the PDf files that you would like to merge into the python directory that you are using!
"""

pdfs = ["chapter1.pdf", "Chapter2.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
