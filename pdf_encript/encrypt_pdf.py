# coding=utf8
import PyPDF2


def encript(input_file, output_file, passwd):
    with open(input_file, 'rb') as pdf_file:

        reader = PyPDF2.PdfFileReader(pdf_file)
        writer = PyPDF2.PdfFileWriter()

        for pag in range(reader.getNumPages()):
            page = reader.getPage(pag)
            writer.addPage(page)

        writer.encrypt(user_pwd=passwd)

        with open(output_file, 'wb') as encrypted_file:
            writer.write(encrypted_file)
