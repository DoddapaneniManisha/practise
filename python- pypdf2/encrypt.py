import PyPDF2

with open('document.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

    pdf_writer.encrypt('password')

    with open('encrypted.pdf', 'wb') as encrypted_file:
        pdf_writer.write(encrypted_file)
