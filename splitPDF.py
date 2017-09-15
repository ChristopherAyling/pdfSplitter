'''
INPUT: splitPDF pdfPath name page name page name page ...

Splits the specified pdf into multiple. Each new
document begins at the given page numbers and ends
before the next. Names new documents.
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

print("pages: ", pages)#debug
print("spec ", spec)#debug
print("names ", names)#debug
print("pageAmts", pageAmts)#debug
print("amount to output: ",len(outputDocs))#debug

# split the PDF
sectionEnd = 0
sectionBegin = 0
for doc in range(len(outputDocs)):
	print('working on doc: ', doc)#debug
	sectionBegin = sectionEnd
	sectionEnd = sectionEnd + pageAmts[doc]
	print('beginning, end', sectionBegin, sectionEnd)#debug
	for page in range(pageAmts[doc]):
		print(outputDocs[doc])#debug
		print(sectionBegin + page)#debug
		outputDocs[doc].addPage(input.getPage(sectionBegin + page))

#save new pdfs
for doc in range(len(outputDocs)):
	outputStream = open(names[doc], "wb")
	outputDocs[doc].write(outputStream)
	outputStream.close()
