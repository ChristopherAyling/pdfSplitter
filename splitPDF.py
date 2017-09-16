'''
INPUT: splitPDF2 pdfPath name page name page name page ...

Splits the specified pdf into multiple.
'''
# imports
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

# open PDF and initialise new PDFs
input = PdfFileReader(open(sys.argv[1], "rb"))
pages = input.getNumPages()
spec = sys.argv[2:]
names = spec[0::2]
pageAmts = [int(i) for i in spec[1::2]]
outputDocs = []
for doc in names:
	outputDocs.append(PdfFileWriter())

# split the PDF
sectionEnd = 0
sectionBegin = 0
for doc in range(len(outputDocs)):
	sectionBegin = sectionEnd
	sectionEnd = sectionEnd + pageAmts[doc]
	for page in range(pageAmts[doc]):
		outputDocs[doc].addPage(input.getPage(sectionBegin + page))

# save new pdfs
for doc in range(len(outputDocs)):
	outputStream = open(names[doc], "wb")
	outputDocs[doc].write(outputStream)
	outputStream.close()