import fitz
from isbnlib import *
from sqlalchemy import *
import os


book_file_input = r'V:\data\practice\python' + '\\' + r'hudson_j_physical_security.pdf'
if book_file_input.endswith('.pdf'):
    doc = fitz.open(book_file_input)
    for n in range(0, doc.pageCount):
        page = doc.loadPage(n)
        text = page.getText()
        if text:
            isbn_list = get_isbnlike(text, level='normal')
            for isbn in isbn_list:
                print(isbn)
doc.close()
os.remove(book_file_input)