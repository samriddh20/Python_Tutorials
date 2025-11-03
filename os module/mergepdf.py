import os

from pypdf import PdfReader, PdfWriter

folderPath = r"D:\python1\os module\data"

# # creating a pdf reader object
# reader = PdfReader('D:\python1\os module\data\Sample_1.pdf')

# # printing number of pages in the pdf
# print(len(reader.pages))

# # creating a page object
# page = reader.pages[0]

# print(page.extract_text())

def PDFmerge(pdfs, output):
    # creating a pdf file writer object
    pdfWriter = PdfWriter()

    # appending the pdfs one by one
    for pdf in pdfs:
        reader = PdfReader(pdf)
        pdfWriter.append(reader)
    
    # writing combined pdfs to output pdf file
    with open(output, 'wb') as f:
        pdfWriter.write(f)

pdf = [os.path.join(folderPath, i) for i in os.listdir(folderPath) if i.lower().startswith('Sample_')]
# pdfs = ['Sample_1.pdf', 'Sample_2.pdf']

output_file = os.path.join(folderPath, 'Merged_Sample_copy.pdf')

PDFmerge(pdfs = pdf, output = output_file)

