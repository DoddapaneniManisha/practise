import PyPDF2

pdf1 = PyPDF2.PdfFileReader(open('document1.pdf', 'rb'))
pdf2 = PyPDF2.PdfFileReader(open('document2.pdf', 'rb'))

pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf1.getNumPages()):
    page = pdf1.getPage(page_num)
    pdf_writer.addPage(page)

for page_num in range(pdf2.getNumPages()):
    page = pdf2.getPage(page_num)
    pdf_writer.addPage(page)

with open('merged.pdf', 'wb') as merged_file:
    pdf_writer.write(merged_file)
