import PyPDF2

with open('document.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        page.rotateClockwise(90)
        pdf_writer.addPage(page)

    with open('rotated.pdf', 'wb') as rotated_file:
        pdf_writer.write(rotated_file)
