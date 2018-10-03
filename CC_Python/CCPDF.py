import copy
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader


class CCPDF:

    # Removes blank pages from a PDF.
    # Does not work on scanned pdfs currently
    def removeBlankPages(self, inpdf, outpdf):
        pdfFileObj = open(inpdf, 'rb')
        input = PdfFileReader(pdfFileObj)
        output = PdfFileWriter()

        for i in range(0, input.getNumPages()):
            page = input.getPage(i)
            contents = page.getContents()
            if contents:
                output.addPage(page)

        outStream = open(outpdf, "wb")
        output.write(outStream)
        outStream.close()
        pdfFileObj.close()
