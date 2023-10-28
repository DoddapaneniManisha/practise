import PyPDF2

with open('sample.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    page = pdf_reader.getPage(0)
    text = page.extractText()
    print(text)
