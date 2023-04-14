import sys
from PyPDF2 import PdfMerger
if len(sys.argv) < 3 :
    print("usage: python PDF_merge.py mergefile.pdf input1.pdf input2.pdf input3.pdf")
else:
    #Create an instance of PdfFileMerger() class
    merger = PdfMerger()

    #Create a list with the file paths
    pdf_files = sys.argv[2:]

    #Iterate over the list of the file paths
    for pdf_file in pdf_files:
        #Append PDF files
        merger.append(pdf_file)

    #Write out the merged PDF file
    merger.write(sys.argv[1])
    merger.close()