#!/usr/bin/env python

from pyPdf import PdfFileWriter, PdfFileReader
from pyPdf.pdf import PageObject

input1 = PdfFileReader(open('page1.pdf', 'rb'))

page1 = input1.getPage(0)

width, height = (page1.mediaBox.getWidth(), page1.mediaBox.getHeight())

output = PdfFileWriter()

for i in range(10):
    page = PageObject.createBlankPage(None, width, height)
    page.mergeScaledTranslatedPage(page1, 0.5, 0, 0)
    page.mergeScaledTranslatedPage(page1, 0.5, width/2, height/2)
    page.mergeScaledTranslatedPage(page1, 0.5, 0, height/2)
    page.mergeScaledTranslatedPage(page1, 0.5, width/2, 0)

    output.addPage(page)

outputStream = open('output.pdf', 'wb')
output.write(outputStream)
outputStream.close()
